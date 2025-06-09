# test_espn_integration.py
"""
Test script to validate ESPN API integration
Run this to make sure everything works before updating your main API
"""

import requests
import json
from datetime import datetime
import sys
from pathlib import Path

# Add your project paths
PROJECT_ROOT = Path(__file__).parent
sys.path.append(str(PROJECT_ROOT))

from espn_integration import ESPNNFLIntegration

def test_espn_basic():
    """Test basic ESPN API functionality"""
    print("🏈 Testing ESPN NFL API Integration")
    print("=" * 50)
    
    espn = ESPNNFLIntegration()
    
    # Test 1: Get current week schedule
    print("\n📅 Test 1: Current Week Schedule")
    try:
        current_week = espn.get_current_week_schedule()
        games = current_week.get('events', [])
        print(f"✅ Successfully retrieved {len(games)} games")
        
        if games:
            # Show sample game
            sample_game = games[0]
            competitors = sample_game['competitions'][0]['competitors']
            home_team = next(c for c in competitors if c.get('homeAway') == 'home')
            away_team = next(c for c in competitors if c.get('homeAway') == 'away')
            
            print(f"📋 Sample game: {away_team['team']['displayName']} @ {home_team['team']['displayName']}")
            print(f"   Date: {sample_game['date']}")
            print(f"   Status: {sample_game['competitions'][0].get('status', {}).get('type', {}).get('name', 'Unknown')}")
        
    except Exception as e:
        print(f"❌ Current week test failed: {e}")
        return False
    
    # Test 2: Enhanced game data
    print("\n🎯 Test 2: Enhanced Game Analysis")
    try:
        if games:
            enhanced_game = espn._enhance_game_data(games[0], week=1)
            if enhanced_game:
                print(f"✅ Enhanced game data generated")
                print(f"   Matchup: {enhanced_game['away_team']['name']} @ {enhanced_game['home_team']['name']}")
                print(f"   Bridge Projection: {enhanced_game['bridge_predictions']['projected_spread']:+.1f} (home)")
                print(f"   Confidence: {enhanced_game['bridge_predictions']['confidence']}%")
                print(f"   Win Probability: {enhanced_game['bridge_predictions']['home_win_probability']:.1%}")
            else:
                print("❌ Failed to enhance game data")
                return False
        
    except Exception as e:
        print(f"❌ Enhanced game test failed: {e}")
        return False
    
    # Test 3: Betting edges detection
    print("\n💰 Test 3: Betting Edges Detection")
    try:
        edges = espn.get_games_with_betting_edges(min_edge=0.5)  # Lower threshold for testing
        print(f"✅ Found {len(edges)} potential betting edges")
        
        if edges:
            top_edge = edges[0]
            print(f"📈 Top Edge:")
            print(f"   Game: {top_edge['away_team']['name']} @ {top_edge['home_team']['name']}")
            if 'betting_edge' in top_edge:
                edge_info = top_edge['betting_edge']
                print(f"   Edge: {edge_info['edge_size']} points")
                print(f"   Bridge: {edge_info['bridge_spread']:+.1f} vs Vegas: {edge_info['vegas_spread']:+.1f}")
                print(f"   Recommendation: {edge_info['recommendation']}")
        
    except Exception as e:
        print(f"❌ Betting edges test failed: {e}")
        return False
    
    # Test 4: Weekly report
    print("\n📊 Test 4: Weekly Predictions Report")
    try:
        report = espn.create_weekly_predictions_report()
        print(f"✅ Generated weekly report")
        print(f"   Total games: {report['week_summary']['total_games']}")
        print(f"   High confidence predictions: {report['week_summary']['high_confidence_predictions']}")
        print(f"   Betting edges found: {report['week_summary']['betting_edges_found']}")
        print(f"   Average confidence: {report['week_summary']['avg_confidence']}%")
        
        if report['top_picks']:
            print(f"\n🎯 Top {len(report['top_picks'])} Picks:")
            for i, pick in enumerate(report['top_picks'], 1):
                if 'betting_edge' in pick:
                    edge = pick['betting_edge']
                    print(f"   {i}. {pick['away_team']['name']} @ {pick['home_team']['name']}")
                    print(f"      Edge: {edge['edge_size']} pts, Rec: {edge['recommendation']}")
        
    except Exception as e:
        print(f"❌ Weekly report test failed: {e}")
        return False
    
    print("\n✅ All ESPN integration tests passed!")
    return True

def test_api_endpoints():
    """Test the API endpoints if server is running"""
    print("\n🌐 Testing API Endpoints (requires server running on port 8000)")
    print("=" * 60)
    
    base_url = "http://localhost:8000"
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/api/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ Health check passed")
            print(f"   ESPN Integration: {health_data.get('espn_integration', {}).get('status', 'unknown')}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to API server: {e}")
        print("   Start the server with: python run_api.py")
        return False
    
    # Test current week endpoint
    try:
        response = requests.get(f"{base_url}/api/schedule/current", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Current week endpoint working")
            total_games = data.get('data', {}).get('week_summary', {}).get('total_games', 0)
            print(f"   Games this week: {total_games}")
        else:
            print(f"❌ Current week endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Current week test failed: {e}")
    
    # Test betting edges endpoint
    try:
        response = requests.get(f"{base_url}/api/betting/edges?min_edge=1.0", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Betting edges endpoint working")
            edges_found = data.get('total_found', 0)
            print(f"   Edges found: {edges_found}")
        else:
            print(f"❌ Betting edges endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Betting edges test failed: {e}")
    
    return True

def main():
    """Run all tests"""
    print(f"🏈 ESPN Integration Test Suite")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Test ESPN integration directly
    espn_success = test_espn_basic()
    
    if espn_success:
        print("\n" + "="*60)
        # Test API endpoints if available
        test_api_endpoints()
    
    print("\n" + "="*60)
    print("🎯 Next Steps:")
    print("1. If tests passed, add ESPN files to your project")
    print("2. Update your main.py with the ESPN integration code")
    print("3. Restart your API server: python run_api.py")
    print("4. Test the new endpoints in your frontend")
    print("5. Start finding betting edges with real data!")
    
    if espn_success:
        print("\n🚀 Ready to integrate ESPN into your NFL Analytics Hub!")
    else:
        print("\n❌ Fix ESPN integration issues before proceeding")

if __name__ == "__main__":
    main()
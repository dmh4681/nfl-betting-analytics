#!/usr/bin/env python3
"""
Test script for NFL Offseason Knowledge Management System
Run this from your project root directory
"""

import sys
import os
from pathlib import Path

# Add src directory to path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.append(str(src_path))

try:
    from knowledge_manager import OffseasonKnowledgeManager
    print("✅ Successfully imported OffseasonKnowledgeManager")
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure knowledge_manager.py is in the src/ directory")
    sys.exit(1)

def test_system():
    """Test the knowledge management system"""
    
    print("🏈 Testing NFL Offseason Knowledge Management System")
    print("=" * 60)
    
    try:
        # Initialize the system
        print("🔧 Initializing system...")
        manager = OffseasonKnowledgeManager(str(project_root))
        print("✅ System initialized successfully")
        
        # Check if files exist
        print("\n📁 Checking for markdown files...")
        knowledge_path = project_root / "data" / "offseason_knowledge"
        
        expected_files = [
            "phi_offseason_2025.md",
            "dal_offseason_2025.md", 
            "nyg_offseason_2025.md",
            "wsh_offseason_2025.md"
        ]
        
        files_found = 0
        for filename in expected_files:
            file_path = knowledge_path / filename
            if file_path.exists():
                print(f"✅ Found: {filename}")
                files_found += 1
            else:
                print(f"❌ Missing: {filename}")
        
        print(f"\n📊 Files found: {files_found}/{len(expected_files)}")
        
        if files_found == 0:
            print("⚠️  No markdown files found. Please check file locations and names.")
            return False
        
        # Generate system report
        print("\n📋 Generating system report...")
        report = manager.generate_system_report()
        
        # Display results
        print("\n" + "="*50)
        print("📊 SYSTEM REPORT")
        print("="*50)
        print(f"📈 Total moves tracked: {report['total_moves_tracked']}")
        print(f"🏟️  Teams monitored: {', '.join(manager.nfc_east_teams)}")
        print(f"⏰ Report generated: {report['timestamp']}")
        print(f"🔋 System health: {report['system_health']}")
        
        print(f"\n🏈 TEAM SUMMARIES:")
        print("-" * 40)
        
        for team, summary in report["team_summaries"].items():
            team_name_map = {
                'PHI': 'Philadelphia Eagles',
                'DAL': 'Dallas Cowboys', 
                'NYG': 'New York Giants',
                'WSH': 'Washington Commanders'
            }
            
            print(f"\n{team} ({team_name_map.get(team, team)}):")
            print(f"  📊 Total moves: {summary['total_moves']}")
            
            if summary['move_types']:
                print(f"  📋 Move breakdown:")
                for move_type, count in summary["move_types"].items():
                    print(f"    - {move_type}: {count}")
            else:
                print(f"  📋 No moves parsed yet (file may need better parsing)")
            
            if summary['last_updated']:
                print(f"  ⏰ Last updated: {summary['last_updated']}")
        
        # Test individual team functionality
        print(f"\n🔍 TESTING INDIVIDUAL TEAM FUNCTIONS:")
        print("-" * 40)
        
        for team in ['PHI', 'DAL']:  # Test first two teams
            print(f"\n{team} detailed summary:")
            team_summary = manager.get_team_summary(team)
            print(f"  Total moves: {team_summary['total_moves']}")
            
            # Test export function
            ranking_data = manager.export_for_ranking_system(team)
            print(f"  Ranking system export: {len(ranking_data)} entries ready")
        
        print(f"\n✅ All tests completed successfully!")
        print(f"📂 Knowledge base location: {knowledge_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

def show_next_steps():
    """Show user what they can do next"""
    
    print(f"\n🚀 NEXT STEPS:")
    print("-" * 30)
    print("1. ✅ System is working - you can now:")
    print("   • Add new moves with manager.add_new_moves()")
    print("   • Export data with manager.export_for_ranking_system()")
    print("   • Generate reports with manager.generate_system_report()")
    print()
    print("2. 🔄 To improve move detection:")
    print("   • Enhance the _extract_players_from_content() function")
    print("   • Add more sophisticated parsing patterns")
    print("   • Connect to automated data sources")
    print()
    print("3. 🔗 To integrate with your ranking system:")
    print("   • Use the export_for_ranking_system() data")
    print("   • Connect to your PlayerBridgeFramework")
    print("   • Build automated sync between systems")

if __name__ == "__main__":
    success = test_system()
    
    if success:
        show_next_steps()
    else:
        print(f"\n❌ Testing failed. Please check the errors above and try again.")
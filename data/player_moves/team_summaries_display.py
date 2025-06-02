"""
NFL Team Summaries Display Script
Loops through all team files and displays their offseason summaries
Updated with all 32 NFL teams organized by division
"""

import sys
from pathlib import Path
import importlib.util
import time

def load_team_module(team_file_path):
    """Dynamically load a team module from file path"""
    try:
        spec = importlib.util.spec_from_file_location("team_module", team_file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading {team_file_path.name}: {e}")
        return None

def display_team_summary(team_module, team_name):
    """Display summary for a single team"""
    print("=" * 80)
    print(f"🏈 {team_name.upper()} OFFSEASON SUMMARY")
    print("=" * 80)
    
    # Try to find the summary dictionary
    summary_name = f"{team_name.upper()}_2025_SUMMARY"
    
    if hasattr(team_module, summary_name):
        summary = getattr(team_module, summary_name)
        
        # Display key metrics
        print(f"📊 Total Moves: {summary.get('total_moves', 'N/A')}")
        print(f"📈 Offseason Grade: {summary.get('offseason_grade', 'N/A')}")
        print(f"🏆 Championship Window: {summary.get('championship_window', 'N/A')}")
        
        # Financial info
        if 'total_guaranteed_money' in summary:
            money = summary['total_guaranteed_money']
            print(f"💰 Total Guaranteed: ${money:,}")
        
        if 'salary_cap_space_remaining' in summary:
            cap_space = summary['salary_cap_space_remaining']
            print(f"💳 Cap Space Remaining: ${cap_space:,}")
        elif 'net_cap_space_remaining' in summary:
            cap_space = summary['net_cap_space_remaining']
            print(f"💳 Cap Space Remaining: ${cap_space:,}")
        
        if 'dead_money' in summary:
            dead_money = summary['dead_money']
            print(f"💀 Dead Money: ${dead_money:,}")
        elif 'dead_money_absorbed' in summary:
            dead_money = summary['dead_money_absorbed']
            print(f"💀 Dead Money Absorbed: ${dead_money:,}")
        
        # Philosophy
        if 'key_philosophy' in summary:
            print(f"🎯 Philosophy: {summary['key_philosophy']}")
        
        # Special metrics for specific teams
        if 'total_offensive_investment' in summary:
            investment = summary['total_offensive_investment']
            print(f"⚡ Offensive Investment: ${investment:,}")
        
        if 'rookie_starters_projected' in summary:
            rookies = summary['rookie_starters_projected']
            print(f"👶 Projected Rookie Starters: {rookies}")
        
        # Move breakdowns
        print(f"\n📋 MOVE BREAKDOWN:")
        move_types = [
            ('free_agent_signings', 'Free Agent Signings'),
            ('major_losses', 'Major Losses'),
            ('draft_picks', 'Draft Picks'),
            ('key_resignings', 'Key Re-signings'),
            ('key_extensions', 'Key Extensions'),
            ('trades', 'Trades'),
            ('coaching_changes', 'Coaching Changes'),
            ('coaching_hires', 'Coaching Hires'),
            ('coaching_departures', 'Coaching Departures'),
            ('retirements', 'Retirements'),
            ('cap_casualties', 'Cap Casualties'),
            ('historic_extensions', 'Historic Extensions'),
            ('major_releases_trades', 'Major Releases/Trades'),
            ('udfa_signings', 'UDFA Signings')
        ]
        
        for key, label in move_types:
            if key in summary and summary[key] > 0:
                print(f"   • {label}: {summary[key]}")
        
        # Key uncertainties or special notes
        if 'key_uncertainty' in summary:
            print(f"\n⚠️  Key Uncertainty: {summary['key_uncertainty']}")
        
        if 'biggest_gamble' in summary:
            print(f"🎲 Biggest Gamble: {summary['biggest_gamble']}")
        
        if 'smartest_move' in summary:
            print(f"🧠 Smartest Move: {summary['smartest_move']}")
        
    else:
        print(f"⚠️  No summary found for {team_name}")
        print("   (Summary should be named {}_2025_SUMMARY)".format(team_name.upper()))
    
    print()

def main():
    """Main function to display all team summaries"""
    
    # Get the project root directory
    current_dir = Path(__file__).parent
    
    # Define all 32 NFL team files
    team_files = {
        # NFC East
        'eagles': 'eagles_2025.py',
        'commanders': 'commanders_2025.py', 
        'cowboys': 'cowboys_2025.py',
        'giants': 'giants_2025.py',
        
        # NFC North
        'packers': 'packers_2025.py',
        'lions': 'lions_2025.py',
        'vikings': 'vikings_2025.py',
        'bears': 'bears_2025.py',
        
        # NFC South
        'saints': 'saints_2025.py',
        'falcons': 'falcons_2025.py',
        'buccaneers': 'bucs_2025.py',  # Note: bucs_2025.py
        'panthers': 'panthers_2025.py',
        
        # NFC West
        '49ers': '49ers_2025.py',
        'seahawks': 'seahawks_2025.py',
        'rams': 'rams_2025.py',
        'cardinals': 'cardinals_2025.py',
        
        # AFC East
        'bills': 'bills_2025.py',
        'dolphins': 'dolphins_2025.py',
        'patriots': 'patriots_2025.py',
        'jets': 'jets_2025.py',
        
        # AFC North
        'ravens': 'ravens_2025.py',
        'steelers': 'steelers_2025.py',
        'browns': 'browns_2025.py',
        'bengals': 'bengals_2025.py',
        
        # AFC South
        'texans': 'texans_2025.py',
        'colts': 'colts_2025.py',
        'titans': 'titans_2025.py',
        'jaguars': 'jaguars_2025.py',
        
        # AFC West
        'chiefs': 'chiefs_2025.py',
        'chargers': 'chargers_2025.py',
        'broncos': 'broncos_2025.py',
        'raiders': 'raiders_2025.py'
    }
    
    print("🏈 NFL 2025 OFFSEASON TEAM SUMMARIES")
    print("🔄 Loading all team summaries...")
    print()
    
    # All 8 NFL divisions with all 32 teams
    divisions = {
        'NFC East': ['eagles', 'commanders', 'cowboys', 'giants'],
        'NFC North': ['packers', 'lions', 'vikings', 'bears'],
        'NFC South': ['saints', 'falcons', 'buccaneers', 'panthers'],
        'NFC West': ['49ers', 'seahawks', 'rams', 'cardinals'],
        'AFC East': ['bills', 'dolphins', 'patriots', 'jets'],
        'AFC North': ['ravens', 'steelers', 'browns', 'bengals'],
        'AFC South': ['texans', 'colts', 'titans', 'jaguars'],
        'AFC West': ['chiefs', 'chargers', 'broncos', 'raiders']
    }
    
    found_teams = 0
    total_teams = 0
    missing_teams = []
    
    for division_name, teams in divisions.items():
        print(f"\n🏟️  {division_name.upper()}")
        print("-" * 60)
        
        for team_name in teams:
            total_teams += 1
            
            if team_name in team_files:
                team_file_path = current_dir / team_files[team_name]
                
                if team_file_path.exists():
                    team_module = load_team_module(team_file_path)
                    if team_module:
                        display_team_summary(team_module, team_name)
                        found_teams += 1
                        time.sleep(0.3)  # Small pause for readability
                    else:
                        print(f"❌ Failed to load {team_name}")
                        missing_teams.append(f"{team_name} (load error)")
                else:
                    print(f"📁 {team_name.title()}: File not found ({team_files[team_name]})")
                    missing_teams.append(f"{team_name} (file missing)")
            else:
                print(f"📁 {team_name.title()}: Not configured")
                missing_teams.append(f"{team_name} (not configured)")
    
    # Summary
    print("=" * 80)
    print(f"✅ SUMMARY: Loaded {found_teams}/32 team summaries")
    
    if found_teams < 32:
        print(f"📝 Still need to create: {32 - found_teams} team files")
        print(f"📋 Missing teams:")
        for missing in missing_teams:
            print(f"   • {missing}")
    else:
        print("🎉 All 32 team summaries loaded successfully!")
    
    print("=" * 80)
    print(f"📊 Coverage: {found_teams}/32 teams ({found_teams/32*100:.1f}%)")

if __name__ == "__main__":
    main()
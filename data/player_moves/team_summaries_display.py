"""
NFL Team Summaries Display Script
Loops through all team files and displays their offseason summaries
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
        
        if 'dead_money' in summary:
            dead_money = summary['dead_money']
            print(f"💀 Dead Money: ${dead_money:,}")
        
        # Philosophy
        if 'key_philosophy' in summary:
            print(f"🎯 Philosophy: {summary['key_philosophy']}")
        
        # Move breakdowns
        print(f"\n📋 MOVE BREAKDOWN:")
        move_types = [
            ('free_agent_signings', 'Free Agent Signings'),
            ('major_losses', 'Major Losses'),
            ('draft_picks', 'Draft Picks'),
            ('key_resignings', 'Key Re-signings'),
            ('trades', 'Trades'),
            ('coaching_changes', 'Coaching Changes'),
            ('retirements', 'Retirements'),
            ('cap_casualties', 'Cap Casualties')
        ]
        
        for key, label in move_types:
            if key in summary and summary[key] > 0:
                print(f"   • {label}: {summary[key]}")
        
    else:
        print(f"⚠️  No summary found for {team_name}")
        print("   (Summary should be named {}_2025_SUMMARY)".format(team_name.upper()))
    
    print()

def main():
    """Main function to display all team summaries"""
    
    # Get the project root directory
    current_dir = Path(__file__).parent
    
    # Define all team files to check
    team_files = {
        # NFC East (completed)
        'eagles': 'eagles_2025.py',
        'commanders': 'commanders_2025.py', 
        'cowboys': 'cowboys_2025.py',
        'giants': 'giants_2025.py',
        
        # AFC East (completed)
        'bills': 'bills_2025.py',
        'dolphins': 'dolphins_2025.py',
        'patriots': 'patriots_2025.py',  # If you have this
        'jets': 'jets_2025.py',  # If you have this
        
        # AFC North (completed)
        'ravens': 'ravens_2025.py',
        'steelers': 'steelers_2025.py',  # If you have this
        'browns': 'browns_2025.py',  # If you have this
        'bengals': 'bengals_2025.py',  # If you have this
        
        # AFC South
        'texans': 'texans_2025.py',
        'colts': 'colts_2025.py',
        'titans': 'titans_2025.py',
        'jaguars': 'jaguars_2025.py',
        
        # AFC West
        'chiefs': 'chiefs_2025.py',
        'chargers': 'chargers_2025.py',
        'broncos': 'broncos_2025.py',
        'raiders': 'raiders_2025.py',
        
        # Add NFC divisions as you create them
    }
    
    print("🏈 NFL 2025 OFFSEASON TEAM SUMMARIES")
    print("🔄 Loading all team summaries...")
    print()
    
    divisions = {
        'NFC East': ['eagles', 'commanders', 'cowboys', 'giants'],
        'AFC East': ['bills', 'dolphins', 'patriots', 'jets'],
        'AFC North': ['ravens', 'steelers', 'browns', 'bengals'],
        'AFC South': ['texans', 'colts', 'titans', 'jaguars'],
        'AFC West': ['chiefs', 'chargers', 'broncos', 'raiders'],
        # Add NFC divisions as needed
    }
    
    found_teams = 0
    total_teams = 0
    
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
                        time.sleep(0.5)  # Small pause for readability
                    else:
                        print(f"❌ Failed to load {team_name}")
                else:
                    print(f"📁 {team_name.title()}: File not found ({team_files[team_name]})")
            else:
                print(f"📁 {team_name.title()}: Not configured")
    
    # Summary
    print("=" * 80)
    print(f"✅ SUMMARY: Loaded {found_teams}/{total_teams} team summaries")
    
    if found_teams < total_teams:
        print(f"📝 Still need to create: {total_teams - found_teams} team files")
    else:
        print("🎉 All team summaries loaded successfully!")
    
    print("=" * 80)

if __name__ == "__main__":
    main()
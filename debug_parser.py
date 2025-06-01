#!/usr/bin/env python3
"""
Debug script to see exactly what the parser is finding
"""

import sys
from pathlib import Path

# Add src directory to path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.append(str(src_path))

from knowledge_manager import OffseasonKnowledgeManager

def debug_team_parsing(team_code):
    """Debug what the parser finds for a specific team"""
    
    manager = OffseasonKnowledgeManager('.')
    
    print(f"\n🔍 DEBUGGING {team_code} PARSING")
    print("=" * 50)
    
    # Get the team's knowledge
    team_knowledge = manager.team_knowledge.get(team_code, {})
    moves = team_knowledge.get('moves', [])
    
    print(f"📊 Total moves found: {len(moves)}")
    print()
    
    # Group by move type
    by_type = {}
    for move in moves:
        move_type = move.get('move_type', 'Unknown')
        if move_type not in by_type:
            by_type[move_type] = []
        by_type[move_type].append(move)
    
    # Show each type
    for move_type, type_moves in by_type.items():
        print(f"📋 {move_type} ({len(type_moves)} players):")
        print("-" * 30)
        
        for i, move in enumerate(type_moves[:10], 1):  # Show first 10
            player = move.get('player_name', 'Unknown')
            position = move.get('position', 'Unknown')
            contract = move.get('contract', 'Unknown')
            
            print(f"  {i:2d}. {player} ({position})")
            if contract != 'Unknown':
                print(f"      Contract: {contract}")
            
        if len(type_moves) > 10:
            print(f"      ... and {len(type_moves) - 10} more")
        print()

def main():
    """Debug all teams"""
    
    print("🏈 NFL Offseason Parser Debug Tool")
    print("=" * 50)
    
    teams = ['PHI', 'DAL', 'NYG', 'WSH']
    
    for team in teams:
        try:
            debug_team_parsing(team)
        except Exception as e:
            print(f"❌ Error debugging {team}: {e}")
    
    print("\n🔧 PARSER IMPROVEMENT SUGGESTIONS:")
    print("-" * 40)
    print("1. Look for patterns in the 'Unknown' moves")
    print("2. Check if player names are being parsed correctly")
    print("3. Verify position detection is accurate")
    print("4. See if section headers are being caught as players")

if __name__ == "__main__":
    main()
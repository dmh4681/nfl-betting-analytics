"""
NFL Player Bridge Data - 2025 Offseason Moves
Organized by team for easy maintenance and updates
DEBUG VERSION - Shows what files exist and what's being imported
"""
import os
import sys
from pathlib import Path

# =============================================================================
# DYNAMIC IMPORTS - Only import files that exist
# =============================================================================

# Get current directory
current_dir = Path(__file__).parent

# Add current directory to Python path for imports
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

print(f"🔍 DEBUG: Current directory: {current_dir}")
print(f"🔍 DEBUG: Python path includes: {str(current_dir) in sys.path}")

# List all Python files in the current directory
py_files = list(current_dir.glob("*.py"))
print(f"🔍 DEBUG: Found Python files: {[f.name for f in py_files]}")

# Define all possible team files (updated with correct variable names)
TEAM_FILES = {
    # NFC West (you have 49ers)
    'SF': ('49ers_2025', 'NINERS_2025_MOVES'),
    
    # AFC East (you have bills)
    'BUF': ('bills_2025', 'BILLS_2025_MOVES'),
    
    # AFC North (you have bengals)
    'CIN': ('bengals_2025', 'BENGALS_2025_MOVES'),
    
    # Other teams (add as you create them)
    'PHI': ('eagles_2025', 'EAGLES_2025_MOVES'),
    'DAL': ('cowboys_2025', 'COWBOYS_2025_MOVES'),
    'NYG': ('giants_2025', 'GIANTS_2025_MOVES'),
    'WAS': ('commanders_2025', 'COMMANDERS_2025_MOVES'),
    'MIA': ('dolphins_2025', 'DOLPHINS_2025_MOVES'),
    'NE': ('patriots_2025', 'PATRIOTS_2025_MOVES'),
    'NYJ': ('jets_2025', 'JETS_2025_MOVES'),
    'BAL': ('ravens_2025', 'RAVENS_2025_MOVES'),
    'PIT': ('steelers_2025', 'STEELERS_2025_MOVES'),
    'CLE': ('browns_2025', 'BROWNS_2025_MOVES'),
    'HOU': ('texans_2025', 'TEXANS_2025_MOVES'),
    'IND': ('colts_2025', 'COLTS_2025_MOVES'),
    'TEN': ('titans_2025', 'TITANS_2025_MOVES'),
    'JAC': ('jaguars_2025', 'JAGUARS_2025_MOVES'),
    'KC': ('chiefs_2025', 'CHIEFS_2025_MOVES'),
    'LAC': ('chargers_2025', 'CHARGERS_2025_MOVES'),
    'DEN': ('broncos_2025', 'BRONCOS_2025_MOVES'),
    'LV': ('raiders_2025', 'RAIDERS_2025_MOVES')
}

# Dynamic imports
MOVES_BY_TEAM = {}
ALL_2025_MOVES = []
TEAM_MOVE_COUNTS = {}

loaded_teams = []
missing_teams = []

for team_abbr, (module_name, moves_var) in TEAM_FILES.items():
    file_path = current_dir / f"{module_name}.py"
    print(f"🔍 DEBUG: Checking {team_abbr} -> {file_path}")
    print(f"🔍 DEBUG: File exists? {file_path.exists()}")
    
    try:
        if file_path.exists():
            print(f"🔍 DEBUG: Attempting to import {module_name}")
            
            # Import the module using importlib for better error handling
            import importlib.util
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None:
                print(f"❌ {team_abbr}: Could not create spec for {module_name}")
                missing_teams.append(team_abbr)
                continue
                
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            print(f"🔍 DEBUG: Module {module_name} loaded successfully")
            print(f"🔍 DEBUG: Module attributes: {dir(module)}")
            print(f"🔍 DEBUG: Looking for variable: {moves_var}")
            
            # Check if the variable exists
            if hasattr(module, moves_var):
                moves = getattr(module, moves_var)
                print(f"🔍 DEBUG: Found {moves_var} with {len(moves) if moves else 0} moves")
                
                # Store the data
                MOVES_BY_TEAM[team_abbr] = moves
                ALL_2025_MOVES.extend(moves)
                TEAM_MOVE_COUNTS[module_name.replace('_2025', '').title()] = len(moves)
                
                loaded_teams.append(team_abbr)
                print(f"✅ {team_abbr}: {len(moves)} moves")
            else:
                print(f"❌ {team_abbr}: Variable {moves_var} not found in {module_name}")
                print(f"🔍 DEBUG: Available variables: {[attr for attr in dir(module) if not attr.startswith('_')]}")
                missing_teams.append(team_abbr)
        else:
            missing_teams.append(team_abbr)
            print(f"❌ {team_abbr}: File {module_name}.py not found")
            
    except Exception as e:
        missing_teams.append(team_abbr)
        print(f"❌ {team_abbr}: Error loading - {e}")
        import traceback
        print(f"🔍 DEBUG: Full error traceback:")
        traceback.print_exc()

# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

TEAM_MOVE_COUNTS['Total'] = len(ALL_2025_MOVES)

# Division organization (only include teams we actually loaded)
DIVISIONS = {}
division_mapping = {
    'AFC East': ['BUF', 'MIA', 'NE', 'NYJ'],
    'AFC North': ['BAL', 'PIT', 'CLE', 'CIN'],
    'AFC South': ['HOU', 'IND', 'TEN', 'JAC'],
    'AFC West': ['KC', 'LAC', 'DEN', 'LV'],
    'NFC East': ['PHI', 'DAL', 'NYG', 'WAS'],
    'NFC West': ['SF', 'SEA', 'LAR', 'ARI']
}

for div_name, teams in division_mapping.items():
    loaded_div_teams = [team for team in teams if team in loaded_teams]
    if loaded_div_teams:  # Only include divisions with at least one loaded team
        DIVISIONS[div_name] = loaded_div_teams

# =============================================================================
# UTILITY FUNCTIONS FOR API
# =============================================================================

def get_team_moves(team_abbr):
    """Get moves for a specific team"""
    return MOVES_BY_TEAM.get(team_abbr.upper(), [])

def get_division_moves(division_name):
    """Get all moves for teams in a division"""
    if division_name not in DIVISIONS:
        return []
    
    division_moves = []
    for team in DIVISIONS[division_name]:
        division_moves.extend(MOVES_BY_TEAM.get(team, []))
    return division_moves

def get_top_additions_by_team(team_abbr, min_importance=8.0, limit=5):
    """Get top additions for a team by importance"""
    team_moves = get_team_moves(team_abbr)
    additions = [move for move in team_moves 
                if move.get('to_team', '').upper() == team_abbr.upper() 
                and move.get('importance_to_new_team', 0) >= min_importance]
    
    # Sort by importance
    additions.sort(key=lambda x: x.get('importance_to_new_team', 0), reverse=True)
    return additions[:limit]

def get_top_losses_by_team(team_abbr, min_importance=7.0, limit=5):
    """Get top losses for a team by importance"""
    team_moves = get_team_moves(team_abbr)
    losses = [move for move in team_moves 
             if move.get('from_team', '').upper() == team_abbr.upper() 
             and move.get('importance_to_old_team', 0) >= min_importance]
    
    # Sort by importance  
    losses.sort(key=lambda x: x.get('importance_to_old_team', 0), reverse=True)
    return losses[:limit]

# =============================================================================
# STARTUP SUMMARY
# =============================================================================

print(f"\n🏈 NFL Player Bridge Data Summary:")
print(f"✅ Teams loaded: {len(loaded_teams)} ({', '.join(loaded_teams)})")
print(f"❌ Teams missing: {len(missing_teams)} ({', '.join(missing_teams) if missing_teams else 'None'})")
print(f"📋 Total moves: {len(ALL_2025_MOVES)}")
print(f"🏟️ Divisions: {len(DIVISIONS)}")

if loaded_teams:
    print(f"\n📈 Top teams by move count:")
    sorted_counts = sorted([(team, count) for team, count in TEAM_MOVE_COUNTS.items() 
                           if team != 'Total'], key=lambda x: x[1], reverse=True)
    for i, (team, count) in enumerate(sorted_counts[:5], 1):
        print(f"  {i}. {team}: {count} moves")

print(f"\n✅ Ready for API integration!")
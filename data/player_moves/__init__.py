"""
NFL Player Bridge Data - 2025 Offseason Moves
Organized by team for easy maintenance and updates
"""

# =============================================================================
# IMPORT ALL TEAM MOVE DATA
# =============================================================================

# NFC East (you already have these)
from .eagles_2025 import EAGLES_2025_MOVES
from .cowboys_2025 import COWBOYS_2025_MOVES
from .giants_2025 import GIANTS_2025_MOVES
from .commanders_2025 import COMMANDERS_2025_MOVES

# AFC East
from .bills_2025 import BILLS_2025_MOVES
from .dolphins_2025 import DOLPHINS_2025_MOVES
from .patriots_2025 import PATRIOTS_2025_MOVES
from .jets_2025 import JETS_2025_MOVES

# AFC North
from .ravens_2025 import RAVENS_2025_MOVES
from .steelers_2025 import STEELERS_2025_MOVES
from .browns_2025 import BROWNS_2025_MOVES
from .bengals_2025 import BENGALS_2025_MOVES

# AFC South
from .texans_2025 import TEXANS_2025_MOVES
from .colts_2025 import COLTS_2025_MOVES
from .titans_2025 import TITANS_2025_MOVES
from .jaguars_2025 import JAGUARS_2025_MOVES

# AFC West
from .chiefs_2025 import CHIEFS_2025_MOVES
from .chargers_2025 import CHARGERS_2025_MOVES
from .broncos_2025 import BRONCOS_2025_MOVES
from .raiders_2025 import RAIDERS_2025_MOVES

# =============================================================================
# COMBINE ALL MOVES
# =============================================================================

# Master list of all moves
ALL_2025_MOVES = (
    # NFC East
    EAGLES_2025_MOVES +
    COWBOYS_2025_MOVES +
    GIANTS_2025_MOVES +
    COMMANDERS_2025_MOVES +
    
    # AFC East
    BILLS_2025_MOVES +
    DOLPHINS_2025_MOVES +
    PATRIOTS_2025_MOVES +
    JETS_2025_MOVES +
    
    # AFC North
    RAVENS_2025_MOVES +
    STEELERS_2025_MOVES +
    BROWNS_2025_MOVES +
    BENGALS_2025_MOVES +
    
    # AFC South
    TEXANS_2025_MOVES +
    COLTS_2025_MOVES +
    TITANS_2025_MOVES +
    JAGUARS_2025_MOVES +
    
    # AFC West
    CHIEFS_2025_MOVES +
    CHARGERS_2025_MOVES +
    BRONCOS_2025_MOVES +
    RAIDERS_2025_MOVES
)

# =============================================================================
# ORGANIZE BY TEAM (for API usage)
# =============================================================================

MOVES_BY_TEAM = {
    # NFC East
    'PHI': EAGLES_2025_MOVES,
    'DAL': COWBOYS_2025_MOVES,
    'NYG': GIANTS_2025_MOVES,
    'WAS': COMMANDERS_2025_MOVES,
    
    # AFC East
    'BUF': BILLS_2025_MOVES,
    'MIA': DOLPHINS_2025_MOVES,
    'NE': PATRIOTS_2025_MOVES,
    'NYJ': JETS_2025_MOVES,
    
    # AFC North
    'BAL': RAVENS_2025_MOVES,
    'PIT': STEELERS_2025_MOVES,
    'CLE': BROWNS_2025_MOVES,
    'CIN': BENGALS_2025_MOVES,
    
    # AFC South
    'HOU': TEXANS_2025_MOVES,
    'IND': COLTS_2025_MOVES,
    'TEN': TITANS_2025_MOVES,
    'JAC': JAGUARS_2025_MOVES,
    
    # AFC West
    'KC': CHIEFS_2025_MOVES,
    'LAC': CHARGERS_2025_MOVES,
    'DEN': BRONCOS_2025_MOVES,
    'LV': RAIDERS_2025_MOVES
}

# =============================================================================
# TEAM STATISTICS AND METADATA
# =============================================================================

# Team move counts for reference
TEAM_MOVE_COUNTS = {
    # NFC East
    'Eagles': len(EAGLES_2025_MOVES),
    'Cowboys': len(COWBOYS_2025_MOVES),
    'Giants': len(GIANTS_2025_MOVES),
    'Commanders': len(COMMANDERS_2025_MOVES),
    
    # AFC East
    'Bills': len(BILLS_2025_MOVES),
    'Dolphins': len(DOLPHINS_2025_MOVES),
    'Patriots': len(PATRIOTS_2025_MOVES),
    'Jets': len(JETS_2025_MOVES),
    
    # AFC North
    'Ravens': len(RAVENS_2025_MOVES),
    'Steelers': len(STEELERS_2025_MOVES),
    'Browns': len(BROWNS_2025_MOVES),
    'Bengals': len(BENGALS_2025_MOVES),
    
    # AFC South
    'Texans': len(TEXANS_2025_MOVES),
    'Colts': len(COLTS_2025_MOVES),
    'Titans': len(TITANS_2025_MOVES),
    'Jaguars': len(JAGUARS_2025_MOVES),
    
    # AFC West
    'Chiefs': len(CHIEFS_2025_MOVES),
    'Chargers': len(CHARGERS_2025_MOVES),
    'Broncos': len(BRONCOS_2025_MOVES),
    'Raiders': len(RAIDERS_2025_MOVES),
    
    # Totals
    'Total': len(ALL_2025_MOVES),
    'AFC Total': (len(BILLS_2025_MOVES) + len(DOLPHINS_2025_MOVES) + len(PATRIOTS_2025_MOVES) + len(JETS_2025_MOVES) +
                  len(RAVENS_2025_MOVES) + len(STEELERS_2025_MOVES) + len(BROWNS_2025_MOVES) + len(BENGALS_2025_MOVES) +
                  len(TEXANS_2025_MOVES) + len(COLTS_2025_MOVES) + len(TITANS_2025_MOVES) + len(JAGUARS_2025_MOVES) +
                  len(CHIEFS_2025_MOVES) + len(CHARGERS_2025_MOVES) + len(BRONCOS_2025_MOVES) + len(RAIDERS_2025_MOVES)),
    'NFC East Total': (len(EAGLES_2025_MOVES) + len(COWBOYS_2025_MOVES) + len(GIANTS_2025_MOVES) + len(COMMANDERS_2025_MOVES))
}

# Division organization for analysis
DIVISIONS = {
    'AFC East': ['BUF', 'MIA', 'NE', 'NYJ'],
    'AFC North': ['BAL', 'PIT', 'CLE', 'CIN'],
    'AFC South': ['HOU', 'IND', 'TEN', 'JAC'],
    'AFC West': ['KC', 'LAC', 'DEN', 'LV'],
    'NFC East': ['PHI', 'DAL', 'NYG', 'WAS']
}

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
                if move['to_team'].upper() == team_abbr.upper() 
                and move.get('importance_to_new_team', 0) >= min_importance]
    
    # Sort by importance
    additions.sort(key=lambda x: x.get('importance_to_new_team', 0), reverse=True)
    return additions[:limit]

def get_top_losses_by_team(team_abbr, min_importance=7.0, limit=5):
    """Get top losses for a team by importance"""
    team_moves = get_team_moves(team_abbr)
    losses = [move for move in team_moves 
             if move['from_team'].upper() == team_abbr.upper() 
             and move.get('importance_to_old_team', 0) >= min_importance]
    
    # Sort by importance  
    losses.sort(key=lambda x: x.get('importance_to_old_team', 0), reverse=True)
    return losses[:limit]

# =============================================================================
# STARTUP LOGGING
# =============================================================================

print(f"🏈 NFL Player Bridge Data Loaded:")
print(f"📊 Total Teams: {len(MOVES_BY_TEAM)}")
print(f"📋 Total Moves: {TEAM_MOVE_COUNTS['Total']}")
print(f"🏟️ AFC Moves: {TEAM_MOVE_COUNTS['AFC Total']}")
print(f"🏟️ NFC East Moves: {TEAM_MOVE_COUNTS['NFC East Total']}")
print()

# Show top teams by move count
sorted_teams = sorted([(team, count) for team, count in TEAM_MOVE_COUNTS.items() 
                      if team not in ['Total', 'AFC Total', 'NFC East Total']], 
                     key=lambda x: x[1], reverse=True)

print("📈 Top Teams by Move Count:")
for i, (team, count) in enumerate(sorted_teams[:10], 1):
    print(f"  {i:2d}. {team}: {count} moves")

print()
print("✅ Ready for API integration!")
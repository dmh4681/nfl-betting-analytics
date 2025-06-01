"""
NFL Player Bridge Data - 2025 Offseason Moves
Organized by team for easy maintenance and updates
"""

from .eagles_2025 import EAGLES_2025_MOVES
from .cowboys_2025 import COWBOYS_2025_MOVES  
from .giants_2025 import GIANTS_2025_MOVES
from .commanders_2025 import COMMANDERS_2025_MOVES

# Combine all team moves into master list
ALL_2025_MOVES = (
    EAGLES_2025_MOVES + 
    COWBOYS_2025_MOVES + 
    GIANTS_2025_MOVES + 
    COMMANDERS_2025_MOVES
)

# Optional: Organize by team for easy access
MOVES_BY_TEAM = {
    'Phi': EAGLES_2025_MOVES,
    'Dal': COWBOYS_2025_MOVES,
    'NYG': GIANTS_2025_MOVES,
    'Was': COMMANDERS_2025_MOVES
}

# Team move counts for reference
TEAM_MOVE_COUNTS = {
    'Eagles': len(EAGLES_2025_MOVES),
    'Cowboys': len(COWBOYS_2025_MOVES),
    'Giants': len(GIANTS_2025_MOVES),
    'Commanders': len(COMMANDERS_2025_MOVES),
    'Total': len(ALL_2025_MOVES)
}

print(f"📊 NFL Player Bridge Data Loaded:")
for team, count in TEAM_MOVE_COUNTS.items():
    print(f"  {team}: {count} moves")
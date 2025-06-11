# api/main.py - Updated with ESPN Integration
import sys
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import pandas as pd
import json
from datetime import datetime

# Import the ESPN integration
from espn_integration import ESPNNFLIntegration, add_espn_endpoints_to_fastapi

# Your existing setup code...
API_DIR = Path(__file__).parent
PROJECT_ROOT = API_DIR.parent
ANALYTICS_PATH = PROJECT_ROOT / "src" / "analytics"
OUTPUT_PATH = PROJECT_ROOT / "output"

if ANALYTICS_PATH.exists():
    sys.path.insert(0, str(ANALYTICS_PATH))
    print(f"✅ Added analytics path: {ANALYTICS_PATH}")

# Try to import your existing framework
FRAMEWORK_AVAILABLE = False
try:
    from player_bridge_framework import PlayerBridgeFramework
    print("✅ Successfully imported PlayerBridgeFramework")
    FRAMEWORK_AVAILABLE = True
except ImportError as e:
    print(f"❌ Could not import PlayerBridgeFramework: {e}")
    print("📝 This is OK - we'll use fallback data")

# Your existing team data loading code...
REAL_DATA_AVAILABLE = False
ALL_2025_MOVES = []
MOVES_BY_TEAM = {}
TEAM_MOVE_COUNTS = {}

try:
    PLAYER_MOVES_PATH = PROJECT_ROOT / "data" / "player_moves"
    print(f"🔍 Looking for team files in: {PLAYER_MOVES_PATH}")
    
    if PLAYER_MOVES_PATH.exists():
        sys.path.insert(0, str(PLAYER_MOVES_PATH))
        
        # REPLACE the team_files dictionary in your main.py (around line 50) with this:

        team_files = {
            # AFC East
            'BUF': 'bills_2025',
            'MIA': 'dolphins_2025', 
            'NE': 'patriots_2025',
            'NYJ': 'jets_2025',
            
            # AFC North
            'BAL': 'ravens_2025',
            'PIT': 'steelers_2025',
            'CLE': 'browns_2025',
            'CIN': 'bengals_2025',
            
            # AFC South
            'HOU': 'texans_2025',
            'IND': 'colts_2025',
            'TEN': 'titans_2025',
            'JAC': 'jaguars_2025',
            
            # AFC West
            'KC': 'chiefs_2025',
            'LAC': 'chargers_2025',
            'DEN': 'broncos_2025',
            'LV': 'raiders_2025',
            
            # NFC East
            'PHI': 'eagles_2025',
            'DAL': 'cowboys_2025',
            'NYG': 'giants_2025',
            'WAS': 'commanders_2025',
            
            # NFC North
            'CHI': 'bears_2025',
            'DET': 'lions_2025',
            'GB': 'packers_2025',
            'MIN': 'vikings_2025',
            
            # NFC South
            'ATL': 'falcons_2025',
            'CAR': 'panthers_2025',
            'NO': 'saints_2025',
            'TB': 'bucs_2025',
            
            # NFC West
            'ARI': 'cardinals_2025',
            'LAR': 'rams_2025',
            'SF': '49ers_2025',
            'SEA': 'seahawks_2025'
        }
        
        loaded_count = 0
        for team_abbr, module_name in team_files.items():
            try:
                file_path = PLAYER_MOVES_PATH / f"{module_name}.py"
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    namespace = {}
                    exec(file_content, namespace)
                    
                    # Special case for 49ers file
                    if module_name == '49ers_2025':
                        moves_var_name = 'NINERS_2025_MOVES'
                    else:
                        moves_var_name = f"{module_name.upper()}_MOVES"
                    
                    if moves_var_name in namespace:
                        team_moves = namespace[moves_var_name]
                        MOVES_BY_TEAM[team_abbr] = team_moves
                        ALL_2025_MOVES.extend(team_moves)
                        loaded_count += 1
                        print(f"✅ {team_abbr}: {len(team_moves)} moves")
                    else:
                        print(f"❌ {team_abbr}: Variable {moves_var_name} not found in file")
                else:
                    print(f"❌ {team_abbr}: File {module_name}.py not found")
                    
            except Exception as e:
                print(f"❌ {team_abbr}: Error loading - {e}")
        
        if loaded_count > 0:
            def get_top_additions_by_team(team_abbr, min_importance=8.0, limit=5):
                team_moves = MOVES_BY_TEAM.get(team_abbr.upper(), [])
                additions = [move for move in team_moves 
                            if move.get('to_team', '').upper() == team_abbr.upper() 
                            and move.get('importance_to_new_team', 0) >= min_importance]
                additions.sort(key=lambda x: x.get('importance_to_new_team', 0), reverse=True)
                return additions[:limit]
            
            def get_top_losses_by_team(team_abbr, min_importance=7.0, limit=5):
                team_moves = MOVES_BY_TEAM.get(team_abbr.upper(), [])
                losses = [move for move in team_moves 
                         if move.get('from_team', '').upper() == team_abbr.upper() 
                         and move.get('importance_to_old_team', 0) >= min_importance]
                losses.sort(key=lambda x: x.get('importance_to_old_team', 0), reverse=True)
                return losses[:limit]
            
            TEAM_MOVE_COUNTS = {
                team_abbr: len(moves) for team_abbr, moves in MOVES_BY_TEAM.items()
            }
            TEAM_MOVE_COUNTS['Total'] = len(ALL_2025_MOVES)
            
            REAL_DATA_AVAILABLE = True
            
            print(f"\n✅ Successfully loaded real team data:")
            print(f"   - Teams loaded: {loaded_count}")
            print(f"   - Total moves: {len(ALL_2025_MOVES)}")
        else:
            print("❌ No team files could be loaded")
    else:
        print(f"❌ Player moves directory not found: {PLAYER_MOVES_PATH}")
        
except Exception as e:
    print(f"❌ Error loading team data: {e}")
    print("📝 Will use sample data")

print(f"\n🔧 REAL_DATA_AVAILABLE: {REAL_DATA_AVAILABLE}")

# =============================================================================
# FASTAPI APP SETUP - Updated with ESPN Integration
# =============================================================================

app = FastAPI(
    title="NFL Offseason Intelligence Hub API", 
    version="2.0.0",  # Updated version with ESPN integration
    description="AI-Powered Roster Analytics & Betting Edge Detection with Live Schedule Data"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:3001", 
        "https://your-domain.com",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize ESPN Integration with your bridge framework
espn_integration = None
try:
    if FRAMEWORK_AVAILABLE:
        bridge_framework = PlayerBridgeFramework()
        espn_integration = ESPNNFLIntegration(bridge_framework)
    else:
        espn_integration = ESPNNFLIntegration()  # Without bridge framework
    
    print("✅ ESPN Integration initialized successfully")
except Exception as e:
    print(f"❌ Error initializing ESPN Integration: {e}")

# =============================================================================
# DATA MODELS - Updated with new ESPN models
# =============================================================================

class TeamAnalysis(BaseModel):
    team: str
    name: str
    offseasonGrade: str
    netImpact: str
    keyAdditions: List[str]
    keyLosses: List[str]
    strengthDelta: Dict[str, str]
    capSpace: str
    projectedWins: float
    spreadImpact: str
    divisionRank: int
    finalRank: Optional[int] = None
    rankChange: Optional[int] = None

class GamePrediction(BaseModel):
    game_id: str
    week: int
    date: str
    home_team: Dict
    away_team: Dict
    bridge_predictions: Dict
    espn_data: Dict
    betting_edge: Optional[Dict] = None

class WeeklyReport(BaseModel):
    report_date: str
    week_summary: Dict
    all_games: List[GamePrediction]
    betting_edges: List[GamePrediction]
    top_picks: List[GamePrediction]

class BridgeAnalysis(BaseModel):
    totalMoves: int
    lastUpdated: str
    topTeams: List[Dict]
    bottomTeams: List[Dict]
    frameworkAvailable: bool

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    confidence: Optional[int] = None

# =============================================================================
# YOUR EXISTING API ENDPOINTS (unchanged)
# =============================================================================

# ... (keep all your existing functions like load_playoff_rankings, get_real_team_data, etc.)

def load_playoff_rankings():
    """Load data from your existing playoff_adjusted_rankings.csv"""
    try:
        rankings_path = OUTPUT_PATH / "playoff_adjusted_rankings.csv"
        print(f"🔍 Looking for rankings at: {rankings_path}")
        
        if rankings_path.exists():
            rankings_df = pd.read_csv(rankings_path)
            print(f"✅ Successfully loaded {len(rankings_df)} teams from playoff rankings")
            return rankings_df
        else:
            print(f"❌ Rankings file not found at {rankings_path}")
            return None
    except Exception as e:
        print(f"❌ Error loading playoff rankings: {e}")
        return None

def calculate_unit_impacts(team_moves):
    """Calculate actual offense/defense/ST impacts based on position groups"""
    
    # Position group mappings
    offensive_positions = ['QB', 'RB', 'WR', 'WR1', 'WR2', 'WR3', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 'G', 'OL']
    defensive_positions = ['EDGE', 'DT', 'NT', 'LB', 'MLB', 'OLB', 'CB', 'CB1', 'CB2', 'S', 'FS', 'SS', 'DB', 'DL']
    special_teams_positions = ['K', 'P', 'LS', 'KR', 'PR']
    
    offense_impact = 0.0
    defense_impact = 0.0
    special_teams_impact = 0.0
    
    for move in team_moves:
        position = move.get('position', '').upper()
        importance_gained = move.get('importance_to_new_team', 0) if move.get('to_team') else 0
        importance_lost = move.get('importance_to_old_team', 0) if move.get('from_team') else 0
        
        # Net impact for this move (positive = gain, negative = loss)
        move_impact = (importance_gained - importance_lost) / 10
        
        # Assign to unit based on position
        if any(pos in position for pos in offensive_positions):
            offense_impact += move_impact
        elif any(pos in position for pos in defensive_positions):
            defense_impact += move_impact
        elif any(pos in position for pos in special_teams_positions):
            special_teams_impact += move_impact
        elif 'COACH' in position or 'HC' in position or 'OC' in position:
            # Offensive coordinators impact offense, defensive coordinators impact defense
            if 'OC' in position or 'OFFENSIVE' in position:
                offense_impact += move_impact * 0.5  # Coaches have moderate impact
            elif 'DC' in position or 'DEFENSIVE' in position:
                defense_impact += move_impact * 0.5
            else:
                # Head coach impacts both
                offense_impact += move_impact * 0.3
                defense_impact += move_impact * 0.3
        else:
            # Unknown position - distribute evenly
            offense_impact += move_impact * 0.4
            defense_impact += move_impact * 0.4
            special_teams_impact += move_impact * 0.2
    
    return {
        'offense': offense_impact,
        'defense': defense_impact,
        'specialTeams': special_teams_impact
    }

# Updated get_real_team_data() function with realistic unit impacts:

def get_real_team_data():
    """Get real team data from your actual files"""
    if not REAL_DATA_AVAILABLE or not MOVES_BY_TEAM:
        return get_sample_team_data()
    
    print(f"🔄 Processing real data for {len(MOVES_BY_TEAM)} teams...")
    
    teams_data = {}
    team_mapping = create_team_mapping()
    
    # Load original 2024 rankings if available
    original_2024_ranks = {}
    try:
        rankings_path = OUTPUT_PATH / "playoff_adjusted_rankings.csv"
        if rankings_path.exists():
            import pandas as pd
            df = pd.read_csv(rankings_path)
            for _, row in df.iterrows():
                team = str(row['team']).strip().upper()
                rank = int(row.get('rank', 16))
                original_2024_ranks[team] = rank
            print(f"✅ Loaded original 2024 ranks for {len(original_2024_ranks)} teams")
    except Exception as e:
        print(f"❌ Error loading original rankings: {e}")
    
    for team_abbr in MOVES_BY_TEAM.keys():
        # Get all moves for this team to calculate unit impacts
        team_moves = MOVES_BY_TEAM.get(team_abbr, [])
        
        additions = get_top_additions_by_team(team_abbr, min_importance=7.0, limit=5)
        losses = get_top_losses_by_team(team_abbr, min_importance=7.0, limit=5)
        
        addition_strings = [f"{move['player_name']} ({move['position']})" for move in additions]
        loss_strings = [f"{move['player_name']} ({move['position']})" for move in losses]
        
        total_additions = sum(move.get('importance_to_new_team', 0) for move in additions)
        total_losses = sum(move.get('importance_to_old_team', 0) for move in losses)
        net_impact = (total_additions - total_losses) / 10
        
        if net_impact >= 3: grade = 'A+'
        elif net_impact >= 2.5: grade = 'A'
        elif net_impact >= 2: grade = 'A-'
        elif net_impact >= 1.5: grade = 'B+'
        elif net_impact >= 1: grade = 'B'
        elif net_impact >= 0: grade = 'B-'
        elif net_impact >= -1: grade = 'C+'
        elif net_impact >= -2: grade = 'C'
        else: grade = 'C-'
        
        team_move_count = TEAM_MOVE_COUNTS.get(team_abbr, 0)
        
        # Get original 2024 rank for this team
        original_rank = original_2024_ranks.get(team_abbr, 16)
        
        # CALCULATE REALISTIC UNIT IMPACTS
        unit_impacts = calculate_unit_impacts(team_moves)
        
        teams_data[team_abbr] = {
            'name': team_mapping.get(team_abbr, team_abbr),
            'offseasonGrade': grade,
            'netImpact': f'{net_impact:+.1f}',
            'keyAdditions': addition_strings or ['No major additions'],
            'keyLosses': loss_strings or ['No major losses'],
            'strengthDelta': {
                'offense': f'{unit_impacts["offense"]:+.1f}',        # REALISTIC calculation
                'defense': f'{unit_impacts["defense"]:+.1f}',        # REALISTIC calculation
                'specialTeams': f'{unit_impacts["specialTeams"]:+.1f}'  # REALISTIC calculation
            },
            'capSpace': '$25M',
            'projectedWins': max(4, min(14, 8.5 + net_impact * 0.8)),
            'spreadImpact': f'{net_impact * 0.3:+.1f}',
            'divisionRank': 2,
            'totalMoves': team_move_count,
            'net_impact_raw': net_impact,
            'original_2024_rank': original_rank
        }
    
    # Rest of your existing sorting/ranking code stays the same...
    sorted_teams = sorted(teams_data.items(), key=lambda x: x[1]['net_impact_raw'], reverse=True)
    
    for rank, (team_abbr, team_data) in enumerate(sorted_teams, 1):
        original_rank = team_data['original_2024_rank']
        new_rank = rank
        rank_change = original_rank - new_rank
        
        teams_data[team_abbr]['finalRank'] = new_rank
        teams_data[team_abbr]['rankChange'] = rank_change
        del teams_data[team_abbr]['net_impact_raw']
        
        # Show unit breakdown in logs
        o_impact = unit_impacts["offense"]
        d_impact = unit_impacts["defense"]
        print(f"✅ {team_abbr}: #{original_rank} → #{new_rank} ({rank_change:+d}), O: {o_impact:+.1f}, D: {d_impact:+.1f}")
    
    print(f"🎯 Successfully processed {len(teams_data)} teams with realistic unit impacts")
    return teams_data


def get_sample_team_data():
    """Fallback sample team data"""
    return {
        'BAL': {
            'name': 'Baltimore Ravens',
            'offseasonGrade': 'A-',
            'netImpact': '+4.7',
            'keyAdditions': ['DeAndre Hopkins (WR)', 'Mike Green (EDGE)', 'Malaki Starks (S)'],
            'keyLosses': ['Brandon Stephens (CB)', 'Patrick Mekari (G)', 'Malik Harrison (LB)'],
            'strengthDelta': {'offense': '+2.1', 'defense': '+1.8', 'specialTeams': '+0.8'},
            'capSpace': '$16.33M',
            'projectedWins': 11.5,
            'spreadImpact': '+1.2',
            'divisionRank': 1,
            'finalRank': 1,
            'rankChange': 2
        }
    }

def create_team_mapping():
    """Create team name mapping"""
    return {
        'BAL': 'Baltimore Ravens', 'PIT': 'Pittsburgh Steelers', 'CIN': 'Cincinnati Bengals', 'CLE': 'Cleveland Browns',
        'BUF': 'Buffalo Bills', 'MIA': 'Miami Dolphins', 'NE': 'New England Patriots', 'NYJ': 'New York Jets',
        'HOU': 'Houston Texans', 'IND': 'Indianapolis Colts', 'JAC': 'Jacksonville Jaguars', 'TEN': 'Tennessee Titans',
        'DEN': 'Denver Broncos', 'KC': 'Kansas City Chiefs', 'LV': 'Las Vegas Raiders', 'LAC': 'Los Angeles Chargers',
        'DAL': 'Dallas Cowboys', 'NYG': 'New York Giants', 'PHI': 'Philadelphia Eagles', 'WAS': 'Washington Commanders',
        'CHI': 'Chicago Bears', 'DET': 'Detroit Lions', 'GB': 'Green Bay Packers', 'MIN': 'Minnesota Vikings',
        'ATL': 'Atlanta Falcons', 'CAR': 'Carolina Panthers', 'NO': 'New Orleans Saints', 'TB': 'Tampa Bay Buccaneers',
        'ARI': 'Arizona Cardinals', 'LAR': 'Los Angeles Rams', 'SF': 'San Francisco 49ers', 'SEA': 'Seattle Seahawks'
    }

# =============================================================================
# EXISTING API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    return {
        "message": "🏈 NFL Offseason Intelligence Hub API",
        "version": "2.0.0",
        "status": "running",
        "framework_available": FRAMEWORK_AVAILABLE,
        "espn_integration": espn_integration is not None,
        "description": "AI-Powered Roster Analytics & Betting Edge Detection with Live Schedule Data",
        "new_endpoints": {
            "current_week": "GET /api/schedule/current - Get current week with predictions",
            "betting_edges": "GET /api/betting/edges - Find betting opportunities", 
            "season_schedule": "GET /api/schedule/season/{year} - Full season schedule"
        },
        "existing_endpoints": {
            "teams": "GET /api/teams - Get all teams data",
            "team_analysis": "GET /api/teams/{team} - Get specific team analysis", 
            "bridge_analysis": "GET /api/analysis/bridge - Get bridge analysis",
            "chat": "POST /api/chat - Chat with Gridiron GPT",
            "health": "GET /api/health - API health check"
        }
    }

@app.get("/api/teams")
async def get_all_teams():
    """Get all teams data"""
    print("📊 Loading all teams data...")
    
    if REAL_DATA_AVAILABLE and MOVES_BY_TEAM:
        print(f"✅ Using real player move data ({len(ALL_2025_MOVES)} moves)")
        teams_data = get_real_team_data()
        
        return {
            "source": "real_player_moves",
            "teams": teams_data,
            "lastUpdated": datetime.now().isoformat(),
            "frameworkAvailable": FRAMEWORK_AVAILABLE,
            "totalTeams": len(teams_data),
            "totalMoves": len(ALL_2025_MOVES),
            "espn_integration_available": espn_integration is not None,
            "dataStats": {
                "topTeamsByMoves": sorted(TEAM_MOVE_COUNTS.items(), key=lambda x: x[1], reverse=True)[:5]
            }
        }
    
    rankings_df = load_playoff_rankings()
    team_mapping = create_team_mapping()
    
    if rankings_df is not None:
        print("⚠️ Falling back to playoff rankings CSV")
        teams_data = {}
        
        for _, row in rankings_df.iterrows():
            team = str(row['team']).strip().upper()
            if team in team_mapping:
                teams_data[team] = {
                    'team': team,
                    'name': team_mapping[team],
                    'offseasonGrade': 'B+',  
                    'netImpact': f"{float(row.get('playoff_adjustment', 0)):+.1f}",
                    'finalRank': int(row.get('rank', 16)),
                    'rankChange': 0,
                    'projectedWins': 8.5 + (float(row.get('rating', 0)) * 0.1),
                    'keyAdditions': ['Analysis in progress...'],
                    'keyLosses': ['Analysis in progress...'],
                    'strengthDelta': {'offense': '+0.0', 'defense': '+0.0', 'specialTeams': '+0.0'},
                    'capSpace': '$25M',
                    'spreadImpact': '+0.0',
                    'divisionRank': 2
                }
        
        return {
            "source": "playoff_adjusted_rankings.csv",
            "teams": teams_data,
            "lastUpdated": datetime.now().isoformat(),
            "frameworkAvailable": FRAMEWORK_AVAILABLE,
            "totalTeams": len(teams_data),
            "espn_integration_available": espn_integration is not None
        }
    
    print("⚠️ Using sample data")
    sample_data = get_sample_team_data()
    
    return {
        "source": "sample_data",
        "teams": sample_data,
        "lastUpdated": datetime.now().isoformat(),
        "frameworkAvailable": FRAMEWORK_AVAILABLE,
        "totalTeams": len(sample_data),
        "espn_integration_available": espn_integration is not None
    }

@app.get("/api/teams/{team}")
async def get_team_analysis(team: str):
    """Get detailed analysis for specific team"""
    team_upper = team.upper()
    team_mapping = create_team_mapping()
    
    print(f"🔍 Loading analysis for team: {team_upper}")
    
    if team_upper not in team_mapping:
        raise HTTPException(status_code=404, detail=f"Team {team} not found")
    
    real_data = get_real_team_data()
    sample_data = get_sample_team_data()
    
    team_data = real_data.get(team_upper) or sample_data.get(team_upper)
    if not team_data:
        team_data = {
            'name': team_mapping[team_upper],
            'offseasonGrade': 'B',
            'netImpact': '+0.0',
            'keyAdditions': ['Analysis coming soon...'],
            'keyLosses': ['Analysis coming soon...'],
            'strengthDelta': {'offense': '+0.0', 'defense': '+0.0', 'specialTeams': '+0.0'},
            'capSpace': '$20M',
            'projectedWins': 8.5,
            'spreadImpact': '+0.0',
            'divisionRank': 2,
            'finalRank': 16,
            'rankChange': 0
        }
    
    return TeamAnalysis(
        team=team_upper,
        name=team_data['name'],
        offseasonGrade=team_data['offseasonGrade'],
        netImpact=team_data['netImpact'],
        keyAdditions=team_data['keyAdditions'],
        keyLosses=team_data['keyLosses'],
        strengthDelta=team_data['strengthDelta'],
        capSpace=team_data['capSpace'],
        projectedWins=team_data['projectedWins'],
        spreadImpact=team_data['spreadImpact'],
        divisionRank=team_data['divisionRank'],
        finalRank=team_data['finalRank'],
        rankChange=team_data['rankChange']
    )

@app.get("/api/analysis/bridge")
async def get_bridge_analysis():
    """Get analysis from your player bridge framework"""
    print("🔍 Getting bridge analysis...")
    
    if REAL_DATA_AVAILABLE and MOVES_BY_TEAM:
        teams_list = list(get_real_team_data().values())
        sorted_teams = sorted(teams_list, key=lambda x: float(x['netImpact'].replace('+', '')), reverse=True)
        
        return BridgeAnalysis(
            totalMoves=len(ALL_2025_MOVES),
            lastUpdated=datetime.now().isoformat(),
            topTeams=sorted_teams[:5],
            bottomTeams=sorted_teams[-3:],
            frameworkAvailable=FRAMEWORK_AVAILABLE
        )
    
    sample_data = get_sample_team_data()
    teams_list = list(sample_data.values())
    sorted_teams = sorted(teams_list, key=lambda x: x['projectedWins'], reverse=True)
    
    return BridgeAnalysis(
        totalMoves=487,
        lastUpdated=datetime.now().isoformat(),
        topTeams=sorted_teams[:5],
        bottomTeams=sorted_teams[-3:],
        frameworkAvailable=FRAMEWORK_AVAILABLE
    )

# ADD THESE ENDPOINTS TO YOUR main.py 
# Place them right after your existing ESPN endpoints (around line 400)

# =============================================================================
# MISSING ENDPOINTS FOR YOUR DASHBOARD VIEWS
# =============================================================================

@app.get("/api/rankings")
async def get_power_rankings():
    """Get power rankings for the rankings view"""
    try:
        # Use your existing team data to create rankings
        real_data = get_real_team_data()
        
        rankings = []
        for team_abbr, team_data in real_data.items():
            rankings.append({
                'team': team_abbr,
                'team_name': team_data['name'],
                'final_2025_rank': team_data.get('finalRank', 16),
                'original_2024_rank': team_data.get('finalRank', 16) - team_data.get('rankChange', 0),
                'rank_change': team_data.get('rankChange', 0),
                'offseason_grade': team_data['offseasonGrade'],
                'offseason_impact': float(team_data['netImpact'].replace('+', '')),
                'final_2025_rating': 80.0 + float(team_data['netImpact'].replace('+', '')),
                'original_2024_rating': 80.0,
                'offense_impact': float(team_data['strengthDelta'].get('offense', '+0.0').replace('+', '')),
                'defense_impact': float(team_data['strengthDelta'].get('defense', '+0.0').replace('+', '')),
                'key_additions': team_data['keyAdditions'],
                'key_losses': team_data['keyLosses']
            })
        
        # Sort by final rank
        rankings.sort(key=lambda x: x['final_2025_rank'])
        
        return {
            "status": "success",
            "rankings": rankings,
            "total_teams": len(rankings),
            "last_updated": datetime.now().isoformat()
        }
        
    except Exception as e:
        print(f"❌ Error getting rankings: {e}")
        return {"status": "error", "message": str(e)}

@app.get("/api/moves")
async def get_player_moves(
    team: str = "", 
    position: str = "", 
    move_type: str = "", 
    min_impact: float = 0.0,
    limit: int = 100
):
    """Get player moves with filtering"""
    try:
        # Use your real moves data
        if not REAL_DATA_AVAILABLE or not ALL_2025_MOVES:
            return {
                "status": "error",
                "message": "No moves data available",
                "moves": [],
                "total_found": 0,
                "total_displayed": 0
            }
        
        filtered_moves = []
        
        for move in ALL_2025_MOVES:
            # Apply filters
            if team and team.upper() not in [move.get('from_team', '').upper(), move.get('to_team', '').upper()]:
                continue
            if position and position.upper() != move.get('position', '').upper():
                continue
            if move_type and move_type not in move.get('move_type', ''):
                continue
            
            # Calculate impact score if not present
            if 'impact_score' not in move:
                importance = move.get('importance_to_new_team', 0)
                grade = move.get('2024_grade', 0)
                snap_pct = move.get('snap_percentage_2024', 0)
                move['impact_score'] = (importance * grade * snap_pct) / 1000
            
            if move['impact_score'] >= min_impact:
                filtered_moves.append(move)
        
        # Sort by impact score
        filtered_moves.sort(key=lambda x: x.get('impact_score', 0), reverse=True)
        
        # Limit results
        displayed_moves = filtered_moves[:limit]
        
        return {
            "status": "success",
            "moves": displayed_moves,
            "total_found": len(filtered_moves),
            "total_displayed": len(displayed_moves),
            "debug_info": {
                "team_filter": team,
                "position_filter": position,
                "move_type_filter": move_type,
                "min_impact": min_impact,
                "total_moves_in_db": len(ALL_2025_MOVES)
            }
        }
        
    except Exception as e:
        print(f"❌ Error getting moves: {e}")
        return {
            "status": "error", 
            "message": str(e),
            "moves": [],
            "total_found": 0,
            "total_displayed": 0
        }

@app.get("/api/divisions/{division}")
async def get_division_analysis(division: str):
    """Get division analysis"""
    try:
        # Division mappings
        division_teams = {
            'AFC North': ['BAL', 'PIT', 'CIN', 'CLE'],
            'AFC East': ['BUF', 'MIA', 'NE', 'NYJ'],
            'AFC South': ['HOU', 'IND', 'TEN', 'JAC'],
            'AFC West': ['KC', 'LAC', 'DEN', 'LV'],
            'NFC East': ['PHI', 'DAL', 'NYG', 'WAS'],
            'NFC North': ['CHI', 'DET', 'GB', 'MIN'],
            'NFC South': ['ATL', 'CAR', 'NO', 'TB'],
            'NFC West': ['ARI', 'LAR', 'SF', 'SEA']
        }
        
        if division not in division_teams:
            raise HTTPException(status_code=404, detail=f"Division {division} not found")
        
        team_abbrs = division_teams[division]
        real_data = get_real_team_data()
        
        teams = []
        total_moves = 0
        best_impact = -999
        best_team = ""
        most_moves = 0
        most_active = ""
        
        for i, team_abbr in enumerate(team_abbrs):
            team_data = real_data.get(team_abbr, {})
            net_impact = float(team_data.get('netImpact', '0.0').replace('+', ''))
            team_moves = team_data.get('totalMoves', 0)
            
            teams.append({
                'team': team_abbr,
                'team_name': team_data.get('name', team_abbr),
                'final_rank': team_data.get('finalRank', 16),
                'offseason_grade': team_data.get('offseasonGrade', 'B'),
                'net_impact': net_impact,
                'total_moves': team_moves
            })
            
            total_moves += team_moves
            
            if net_impact > best_impact:
                best_impact = net_impact
                best_team = team_abbr
                
            if team_moves > most_moves:
                most_moves = team_moves
                most_active = team_abbr
        
        # Sort teams by final rank
        teams.sort(key=lambda x: x['final_rank'])
        
        return {
            "status": "success",
            "division": division,
            "teams": teams,
            "division_info": {
                "best_team": teams[0]['team'],  # Best ranked team
                "best_offseason": best_team,
                "most_active": most_active,
                "total_moves": total_moves,
                "avg_net_impact": sum(t['net_impact'] for t in teams) / len(teams),
                "competitive_balance": 10 - abs(max(t['net_impact'] for t in teams) - min(t['net_impact'] for t in teams))
            }
        }
        
    except Exception as e:
        print(f"❌ Error getting division analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting division analysis: {str(e)}")

@app.get("/api/teams/{team}/detailed")
async def get_detailed_team_analysis(team: str):
    """Get detailed team analysis for team view"""
    try:
        team_upper = team.upper()
        real_data = get_real_team_data()
        team_mapping = create_team_mapping()
        
        if team_upper not in team_mapping:
            raise HTTPException(status_code=404, detail=f"Team {team} not found")
        
        team_data = real_data.get(team_upper)
        if not team_data:
            raise HTTPException(status_code=404, detail=f"No data found for team {team}")
        
        # Calculate additional metrics
        net_impact = float(team_data['netImpact'].replace('+', ''))
        total_moves = team_data.get('totalMoves', 0)
        
        # Determine division/conference (you can expand this mapping)
        division_mapping = {
            'BAL': ('AFC North', 'AFC'), 'PIT': ('AFC North', 'AFC'), 'CIN': ('AFC North', 'AFC'), 'CLE': ('AFC North', 'AFC'),
            'BUF': ('AFC East', 'AFC'), 'MIA': ('AFC East', 'AFC'), 'NE': ('AFC East', 'AFC'), 'NYJ': ('AFC East', 'AFC'),
            'HOU': ('AFC South', 'AFC'), 'IND': ('AFC South', 'AFC'), 'TEN': ('AFC South', 'AFC'), 'JAC': ('AFC South', 'AFC'),
            'KC': ('AFC West', 'AFC'), 'LAC': ('AFC West', 'AFC'), 'DEN': ('AFC West', 'AFC'), 'LV': ('AFC West', 'AFC'),
            'PHI': ('NFC East', 'NFC'), 'DAL': ('NFC East', 'NFC'), 'NYG': ('NFC East', 'NFC'), 'WAS': ('NFC East', 'NFC'),
            'CHI': ('NFC North', 'NFC'), 'DET': ('NFC North', 'NFC'), 'GB': ('NFC North', 'NFC'), 'MIN': ('NFC North', 'NFC'),
            'ATL': ('NFC South', 'NFC'), 'CAR': ('NFC South', 'NFC'), 'NO': ('NFC South', 'NFC'), 'TB': ('NFC South', 'NFC'),
            'ARI': ('NFC West', 'NFC'), 'LAR': ('NFC West', 'NFC'), 'SF': ('NFC West', 'NFC'), 'SEA': ('NFC West', 'NFC')
        }
        
        division, conference = division_mapping.get(team_upper, ("Unknown Division", "Unknown Conference"))
        
        return {
            "status": "success",
            "team": team_upper,
            "team_name": team_data['name'],
            "division": division,
            "conference": conference,
            "offseason_grade": team_data['offseasonGrade'],
            "net_impact": net_impact,
            "total_moves": total_moves,
            "players_gained": len([a for a in team_data['keyAdditions'] if a != 'No major additions']),
            "players_lost": len([l for l in team_data['keyLosses'] if l != 'No major losses']),
            "key_additions": team_data['keyAdditions'],
            "key_losses": team_data['keyLosses'],
            "unit_impacts": {
                "offense": float(team_data['strengthDelta'].get('offense', '+0.0').replace('+', '')),
                "defense": float(team_data['strengthDelta'].get('defense', '+0.0').replace('+', '')),
                "special_teams": float(team_data['strengthDelta'].get('specialTeams', '+0.0').replace('+', ''))
            },
            "ranking_info": {
                "final_2025_rank": team_data.get('finalRank', 16),
                "rank_change": team_data.get('rankChange', 0)
            },
            "move_efficiency": net_impact / max(total_moves, 1),
            "offseason_strategy": f"Net impact of {net_impact:+.1f} across {total_moves} moves shows {'aggressive improvement' if net_impact > 2 else 'modest changes' if net_impact > 0 else 'concerning losses'}."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error getting detailed team analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting team analysis: {str(e)}")

# DEBUGGING ENDPOINT - You can remove this later
@app.get("/api/debug/data")
async def debug_data_status():
    """Debug endpoint to check data availability"""
    return {
        "framework_available": FRAMEWORK_AVAILABLE,
        "real_data_available": REAL_DATA_AVAILABLE,
        "total_moves": len(ALL_2025_MOVES) if REAL_DATA_AVAILABLE else 0,
        "teams_loaded": len(MOVES_BY_TEAM) if REAL_DATA_AVAILABLE else 0,
        "team_list": list(MOVES_BY_TEAM.keys()) if REAL_DATA_AVAILABLE else [],
        "sample_team_data": get_real_team_data().get('BAL', {}) if REAL_DATA_AVAILABLE else {},
        "espn_integration_working": espn_integration is not None
    }

@app.post("/api/chat")
async def chat_with_gpt(request: ChatRequest):
    """Chat with Gridiron GPT - Enhanced with ESPN data"""
    question = request.question.lower()
    
    print(f"💬 Chat question: {question}")
    
    # Enhanced responses that can reference live schedule data
    if 'schedule' in question or 'this week' in question or 'games' in question:
        if espn_integration:
            try:
                current_week = espn_integration.get_current_week_schedule()
                game_count = len(current_week.get('events', []))
                response = f"This week has {game_count} NFL games scheduled. I can analyze each matchup using our bridge framework to find potential betting edges. Would you like me to break down any specific games or show you our top predictions?"
            except:
                response = "I can analyze upcoming games using our bridge framework, but I'm having trouble connecting to live schedule data right now. Try asking about specific team matchups!"
        else:
            response = "I can help you analyze matchups using our bridge framework! Ask me about specific teams or tell me which games you're interested in betting on."
    
    elif 'ravens' in question or 'baltimore' in question:
        response = "The Ravens had an excellent offseason! They added DeAndre Hopkins at WR, giving Lamar Jackson a proven target, and drafted Malaki Starks to improve their secondary. Their A- grade reflects smart moves that address key needs while maintaining cap flexibility. Perfect setup for another playoff run!"
    
    elif 'betting' in question or 'edge' in question or 'picks' in question:
        if espn_integration:
            response = "Our bridge framework finds betting edges by comparing our roster-based projections to Vegas lines. We look for games where our impact scoring shows a team is significantly stronger/weaker than the market believes. Want me to check this week's games for the biggest edges?"
        else:
            response = "Our bridge framework excels at finding betting edges! We analyze roster moves, weight them by position importance, and compare our projections to market lines. This often reveals teams that are over/undervalued due to offseason changes."
    
    elif 'eagles' in question or 'philadelphia' in question:
        response = "The Eagles are built to repeat! Adding Saquon Barkley was a statement move, and they're projected for 12.5 wins. Their +5.2 net impact leads the league - they've addressed needs while keeping their core intact. Strong Super Bowl contender."
    
    elif 'steelers' in question or 'pittsburgh' in question:
        response = "Pittsburgh made waves with the DK Metcalf acquisition, giving them a true WR1. However, losing George Pickens and having QB uncertainty tempers excitement. Still a B+ offseason that improved their ceiling significantly. Much depends on quarterback play."
    
    elif 'afc north' in question:
        response = "AFC North looks like Baltimore's division to lose. Ravens (11.5 wins), Steelers (9.5), then Bengals and Browns. The Ravens' offseason moves give them a clear edge - they added talent while rivals lost key pieces."
    
    elif 'best' in question and 'offseason' in question:
        response = "Philadelphia (A, +5.2), Baltimore (A-, +4.7), and Pittsburgh (B+, +3.2) had the best offseasons based on our analysis. Eagles and Ravens are built for deep playoff runs with their strategic additions."
    
    else:
        response = f"Great question! I analyze NFL teams using our bridge framework that tracks every roster move and weights them by position importance. I can help you understand team projections, find betting edges, or dive deep into any specific matchup. What would you like to explore?"
    
    return ChatResponse(
        response=response,
        timestamp=datetime.now().isoformat(),
        confidence=85
    )

@app.get("/api/health")
async def health_check():
    """Health check endpoint - Enhanced with ESPN status"""
    playoff_rankings_exists = (OUTPUT_PATH / "playoff_adjusted_rankings.csv").exists()
    
    # Check ESPN integration
    espn_status = "not_initialized"
    if espn_integration:
        try:
            # Test ESPN API with a quick call
            test_schedule = espn_integration.get_current_week_schedule()
            if test_schedule:
                espn_status = "active"
            else:
                espn_status = "connection_error"
        except:
            espn_status = "api_error"
    
    data_files_exist = []
    if (PROJECT_ROOT / "data" / "player_moves").exists():
        data_path = PROJECT_ROOT / "data" / "player_moves"
        data_files_exist = [
            (data_path / "eagles_2025.py").exists(),
            (data_path / "ravens_2025.py").exists(), 
            (data_path / "steelers_2025.py").exists()
        ]
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "framework_available": FRAMEWORK_AVAILABLE,
        "playoff_rankings_available": playoff_rankings_exists,
        "espn_integration": {
            "available": espn_integration is not None,
            "status": espn_status,
            "features": ["schedule", "betting_edges", "projections"] if espn_integration else []
        },
        "real_data_available": REAL_DATA_AVAILABLE,
        "total_moves_tracked": len(ALL_2025_MOVES) if REAL_DATA_AVAILABLE else 0,
        "paths": {
            "project_root": str(PROJECT_ROOT),
            "analytics_path": str(ANALYTICS_PATH),
            "output_path": str(OUTPUT_PATH)
        },
        "api_version": "2.0.0"
    }

# =============================================================================
# NEW ESPN INTEGRATION ENDPOINTS
# =============================================================================

@app.get("/api/schedule/current")
async def get_current_week_predictions():
    """Get current week with your bridge predictions"""
    if not espn_integration:
        raise HTTPException(status_code=503, detail="ESPN integration not available")
    
    try:
        report = espn_integration.create_weekly_predictions_report()
        return {
            "status": "success",
            "data": report,
            "source": "espn_api_with_bridge_projections"
        }
    except Exception as e:
        print(f"❌ Error getting current week predictions: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating predictions: {str(e)}")

@app.get("/api/betting/edges")
async def get_betting_edges(min_edge: float = 2.0):
    """Get games where bridge framework disagrees with Vegas"""
    if not espn_integration:
        raise HTTPException(status_code=503, detail="ESPN integration not available")
    
    try:
        edges = espn_integration.get_games_with_betting_edges(min_edge)
        return {
            "status": "success",
            "edges": edges,
            "total_found": len(edges),
            "min_edge_threshold": min_edge,
            "message": f"Found {len(edges)} games with {min_edge}+ point disagreement between bridge projections and Vegas"
        }
    except Exception as e:
        print(f"❌ Error getting betting edges: {e}")
        raise HTTPException(status_code=500, detail=f"Error finding betting edges: {str(e)}")

@app.get("/api/schedule/season/{year}")
async def get_season_schedule(year: int = 2025):
    """Get full season schedule with projections"""
    if not espn_integration:
        raise HTTPException(status_code=503, detail="ESPN integration not available")
    
    try:
        schedule = espn_integration.get_season_schedule(year)
        return {
            "status": "success",
            "year": year,
            "total_games": len(schedule),
            "schedule": schedule[:50],  # Limit to first 50 games for performance
            "note": f"Showing first 50 of {len(schedule)} total games"
        }
    except Exception as e:
        print(f"❌ Error getting season schedule: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching season schedule: {str(e)}")

# =============================================================================
# STARTUP EVENT - Enhanced
# =============================================================================

@app.on_event("startup")
async def startup_event():
    print("🏈 NFL Analytics API Starting Up...")
    print(f"📁 Project root: {PROJECT_ROOT}")
    print(f"🔧 Framework available: {FRAMEWORK_AVAILABLE}")
    print(f"📊 Real data available: {REAL_DATA_AVAILABLE}")
    print(f"🔌 ESPN integration: {'✅' if espn_integration else '❌'}")
    
    if espn_integration:
        try:
            # Test ESPN connection
            test_data = espn_integration.get_current_week_schedule()
            if test_data:
                print(f"✅ ESPN API connection successful")
                games_count = len(test_data.get('events', []))
                print(f"📅 Current week has {games_count} games")
            else:
                print("⚠️ ESPN API connected but no data returned")
        except Exception as e:
            print(f"❌ ESPN API test failed: {e}")
    
    playoff_csv = OUTPUT_PATH / "playoff_adjusted_rankings.csv"
    print(f"📊 Playoff rankings: {'✅' if playoff_csv.exists() else '❌'} {playoff_csv}")
    
    if REAL_DATA_AVAILABLE:
        print(f"🎯 Ready to serve live predictions for {len(MOVES_BY_TEAM)} teams!")

# For running directly
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting NFL Analytics API with ESPN Integration...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )
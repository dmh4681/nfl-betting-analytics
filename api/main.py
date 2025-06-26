# api/main.py - Complete Version with Adjusted Rankings and All Endpoints
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

# Setup code
API_DIR = Path(__file__).parent
PROJECT_ROOT = API_DIR.parent
ANALYTICS_PATH = PROJECT_ROOT / "src" / "analytics"
OUTPUT_PATH = PROJECT_ROOT / "output"

if ANALYTICS_PATH.exists():
    sys.path.insert(0, str(ANALYTICS_PATH))
    print(f"✅ Added analytics path: {ANALYTICS_PATH}")

# Try to import framework
FRAMEWORK_AVAILABLE = False
try:
    from player_bridge_framework import PlayerBridgeFramework
    print("✅ Successfully imported PlayerBridgeFramework")
    FRAMEWORK_AVAILABLE = True
except ImportError as e:
    print(f"❌ Could not import PlayerBridgeFramework: {e}")
    print("📝 This is OK - we'll use fallback data")

# Initialize ESPN integration if available
espn_integration = None
try:
    from espn_integration import ESPNNFLIntegration, add_espn_endpoints_to_fastapi
    if FRAMEWORK_AVAILABLE:
        bridge_framework = PlayerBridgeFramework()
        espn_integration = ESPNNFLIntegration(bridge_framework)
    else:
        espn_integration = ESPNNFLIntegration()
    print("✅ ESPN Integration initialized successfully")
except Exception as e:
    print(f"⚠️ ESPN integration not available: {e}")

# Team data loading
REAL_DATA_AVAILABLE = False
ALL_2025_MOVES = []
MOVES_BY_TEAM = {}
TEAM_MOVE_COUNTS = {}

try:
    PLAYER_MOVES_PATH = PROJECT_ROOT / "data" / "player_moves"
    print(f"🔍 Looking for team files in: {PLAYER_MOVES_PATH}")
    
    if PLAYER_MOVES_PATH.exists():
        sys.path.insert(0, str(PLAYER_MOVES_PATH))
        
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
# FASTAPI APP SETUP
# =============================================================================

app = FastAPI(
    title="NFL Offseason Intelligence Hub API", 
    version="2.0.0",
    description="AI-Powered Roster Analytics & Betting Edge Detection with Live Schedule Data"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================================================================
# ESPN INTEGRATION (if available)
# =============================================================================

if espn_integration:
    add_espn_endpoints_to_fastapi(app, espn_integration)
    print("✅ ESPN endpoints added to FastAPI app")

# =============================================================================
# MODELS
# =============================================================================

class ChatRequest(BaseModel):
    question: str
    team: Optional[str] = None
    include_context: bool = True

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    confidence: int = 85

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

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def load_playoff_rankings():
    """Load the playoff-adjusted rankings CSV"""
    csv_path = OUTPUT_PATH / "playoff_adjusted_rankings.csv"
    print(f"📊 Looking for playoff rankings at: {csv_path}")
    
    if csv_path.exists():
        try:
            df = pd.read_csv(csv_path)
            print(f"✅ Loaded playoff rankings: {len(df)} teams")
            return df
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return None
    else:
        print(f"❌ CSV not found at {csv_path}")
        return None

def create_team_mapping():
    """Create team abbreviation to full name mapping"""
    return {
        'BUF': 'Buffalo Bills', 'MIA': 'Miami Dolphins', 'NE': 'New England Patriots', 'NYJ': 'New York Jets',
        'BAL': 'Baltimore Ravens', 'PIT': 'Pittsburgh Steelers', 'CLE': 'Cleveland Browns', 'CIN': 'Cincinnati Bengals',
        'HOU': 'Houston Texans', 'IND': 'Indianapolis Colts', 'TEN': 'Tennessee Titans', 'JAC': 'Jacksonville Jaguars',
        'KC': 'Kansas City Chiefs', 'LAC': 'Los Angeles Chargers', 'DEN': 'Denver Broncos', 'LV': 'Las Vegas Raiders',
        'PHI': 'Philadelphia Eagles', 'DAL': 'Dallas Cowboys', 'NYG': 'New York Giants', 'WAS': 'Washington Commanders',
        'CHI': 'Chicago Bears', 'DET': 'Detroit Lions', 'GB': 'Green Bay Packers', 'MIN': 'Minnesota Vikings',
        'ATL': 'Atlanta Falcons', 'CAR': 'Carolina Panthers', 'NO': 'New Orleans Saints', 'TB': 'Tampa Bay Buccaneers',
        'ARI': 'Arizona Cardinals', 'LAR': 'Los Angeles Rams', 'SF': 'San Francisco 49ers', 'SEA': 'Seattle Seahawks'
    }

def calculate_unit_impacts(team_moves):
    """Calculate actual offense/defense/ST impacts based on position groups"""
    
    offensive_positions = ['QB', 'RB', 'WR', 'WR1', 'WR2', 'WR3', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 'G', 'OT', 'OL']
    defensive_positions = ['EDGE', 'DE', 'DT', 'NT', 'LB', 'MLB', 'OLB', 'CB', 'CB1', 'CB2', 'S', 'FS', 'SS', 'DB', 'DL', 'CB/S']
    special_teams_positions = ['K', 'P', 'LS', 'KR', 'PR']
    coaching_positions = ['COACH', 'HC', 'OC', 'DC', 'COACH-DC', 'COACH-OC', 'COACH-ST', 'COACH-LB', 'COACH-DL']
    
    offense_impact = 0.0
    defense_impact = 0.0
    special_teams_impact = 0.0
    
    for move in team_moves:
        position = move.get('position', '').upper()
        
        # Use pre-calculated impact_score if available
        if 'impact_score' in move:
            move_impact = move['impact_score']
        else:
            # Fallback calculation
            importance_gained = move.get('importance_to_new_team', 0) if move.get('to_team') else 0
            importance_lost = move.get('importance_to_old_team', 0) if move.get('from_team') else 0
            move_impact = (importance_gained - importance_lost) / 10
        
        # Skip moves where player stays with same team (extensions)
        if move.get('from_team') == move.get('to_team') and move.get('move_type') in ['Contract Extension', 'Extension', 'Re-signing']:
            continue
            
        # For losses (player leaving)
        if move.get('from_team') and move.get('to_team') != move.get('from_team'):
            move_impact = abs(move_impact) * -1 if move_impact > 0 else move_impact
        
        # Assign to unit based on position
        if any(pos in position for pos in offensive_positions):
            offense_impact += move_impact
        elif any(pos in position for pos in defensive_positions):
            defense_impact += move_impact
        elif any(pos in position for pos in special_teams_positions):
            special_teams_impact += move_impact
        elif any(pos in position for pos in coaching_positions):
            # Coaching impacts based on position type
            if any(x in position for x in ['OC', 'OFFENSIVE']):
                offense_impact += move_impact * 0.5
            elif any(x in position for x in ['DC', 'DEFENSIVE', 'LB', 'DL', 'DB']):
                defense_impact += move_impact * 0.5
            elif 'ST' in position:
                special_teams_impact += move_impact * 0.5
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
        'offense': round(offense_impact, 1),
        'defense': round(defense_impact, 1),
        'specialTeams': round(special_teams_impact, 1)
    }

def get_real_team_data():
    """Get the real team data from our loaded player moves"""
    team_mapping = create_team_mapping()
    teams_data = {}
    
    # Run the framework if available
    framework_results = None
    if FRAMEWORK_AVAILABLE:
        try:
            framework = PlayerBridgeFramework()
            # Use the correct method name: generate_comprehensive_report
            player_bridge, team_grades, final_rankings = framework.generate_comprehensive_report()
            
            # Convert DataFrames to dictionaries
            framework_results = {
                'power_rankings': final_rankings.to_dict('records'),
                'offseason_grades': team_grades.to_dict('records'),
                'player_bridge': player_bridge.to_dict('records') if not player_bridge.empty else []
            }
            
            # Verify the adjustments
            rankings = final_rankings.to_dict('records')
            bears_rank = next((r for r in rankings if r['team'] == 'CHI'), None)
            eagles_rank = next((r for r in rankings if r['team'] == 'PHI'), None)
            
            if bears_rank and eagles_rank:
                print(f"✅ Ranking verification - Bears: #{bears_rank['final_2025_rank']}, Eagles: #{eagles_rank['final_2025_rank']}")
            
        except Exception as e:
            print(f"❌ Error running framework: {e}")
    
    # Process each team
    for team_abbr, moves in MOVES_BY_TEAM.items():
        team_name = team_mapping.get(team_abbr, team_abbr)
        
        # Calculate key statistics
        additions = [m for m in moves if m.get('move_type') in ['Free Agent Signing', 'Trade', 'Extension']]
        losses = [m for m in moves if m.get('move_type') == 'Free Agent Loss']
        draft_picks = [m for m in moves if 'Draft' in m.get('move_type', '')]
        
        team_info = {
            'team': team_abbr,
            'team_name': team_name,
            'name': team_name,
            'total_moves': len(moves),
            'totalMoves': len(moves),
            'additions': len(additions),
            'losses': len(losses),
            'draft_picks': len(draft_picks),
            'key_additions': [m.get('player', 'Unknown') for m in additions[:5]],
            'keyAdditions': [m.get('player', 'Unknown') for m in additions[:5]],
            'key_losses': [m.get('player', 'Unknown') for m in losses[:5]],
            'keyLosses': [m.get('player', 'Unknown') for m in losses[:5]],
            'moves': moves
        }
        
        # Add framework analysis if available
        if framework_results:
            # Find matching team in grades
            team_data = next((t for t in framework_results['offseason_grades'] if t['team'] == team_abbr), None)
            if team_data:
                team_info.update({
                    'net_impact': team_data.get('net_impact', 0),
                    'netImpact': f"{team_data.get('net_impact', 0):+.1f}",
                    'offseason_grade': team_data.get('offseason_grade', 'N/A'),
                    'offseasonGrade': team_data.get('offseason_grade', 'N/A'),
                    'offense_impact': team_data.get('offense_impact', 0),
                    'defense_impact': team_data.get('defense_impact', 0)
                })
            
            # Find matching team in rankings
            ranking_data = next((r for r in framework_results['power_rankings'] if r['team'] == team_abbr), None)
            if ranking_data:
                team_info.update({
                    'final_2025_rank': ranking_data.get('final_2025_rank', 0),
                    'finalRank': ranking_data.get('final_2025_rank', 0),
                    'rank_change': ranking_data.get('rank_change', 0),
                    'rankChange': ranking_data.get('rank_change', 0),
                    'playoff_rank': ranking_data.get('original_2024_rank', 0)
                })
        
        teams_data[team_abbr] = team_info
    
    return teams_data

# =============================================================================
# API ENDPOINTS
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
        "adjusted_rankings": {
            "bears": "#1 (Adjusted for demonstration)",
            "eagles": "#32 (Adjusted for demonstration)"
        },
        "endpoints": {
            "teams": "GET /api/teams - Get all teams data",
            "team_analysis": "GET /api/teams/{team} - Get specific team analysis", 
            "bridge_analysis": "GET /api/analysis/bridge - Get bridge analysis",
            "chat": "POST /api/chat - Chat with Gridiron GPT",
            "health": "GET /api/health - API health check",
            "moves": "GET /api/moves - Get player moves with filtering",
            "divisions": "GET /api/divisions/{division} - Get division analysis",
            "rankings": "GET /api/rankings - Get power rankings"
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
            "adjusted_note": "Rankings adjusted: Bears #1, Eagles #32 for demonstration",
            "dataStats": {
                "topTeamsByMoves": sorted(TEAM_MOVE_COUNTS.items(), key=lambda x: x[1], reverse=True)[:5]
            }
        }
    
    # Fallback to playoff rankings CSV
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
                    'team_name': team_mapping[team],
                    'playoff_power_rank': int(row['playoff_rank']),
                    'final_record': row.get('record', 'N/A'),
                    'total_moves': 0,
                    'additions': 0,
                    'losses': 0,
                    'draft_picks': 0
                }
        
        return {
            "source": "playoff_rankings_csv",
            "teams": teams_data,
            "lastUpdated": datetime.now().isoformat(),
            "frameworkAvailable": FRAMEWORK_AVAILABLE,
            "note": "Using 2024 playoff rankings as baseline"
        }
    
    # Ultimate fallback
    print("⚠️ Using hardcoded sample data")
    return {
        "source": "sample_data",
        "teams": {
            "CHI": {
                "team": "CHI",
                "team_name": "Chicago Bears",
                "total_moves": 42,
                "net_impact": 8.5,
                "offseason_grade": "A+",
                "final_2025_rank": 1,
                "rank_change": 25,
                "note": "Adjusted to #1 for demonstration"
            },
            "PHI": {
                "team": "PHI",
                "team_name": "Philadelphia Eagles",
                "total_moves": 38,
                "net_impact": -7.2,
                "offseason_grade": "F",
                "final_2025_rank": 32,
                "rank_change": -22,
                "note": "Adjusted to #32 for demonstration"
            }
        },
        "lastUpdated": datetime.now().isoformat()
    }

@app.get("/api/teams/{team}")
async def get_team_analysis(team: str):
    """Get detailed analysis for a specific team"""
    team = team.upper()
    print(f"📊 Loading data for team: {team}")
    
    if REAL_DATA_AVAILABLE and team in MOVES_BY_TEAM:
        team_mapping = create_team_mapping()
        moves = MOVES_BY_TEAM[team]
        
        # Get team data from comprehensive report
        framework_analysis = None
        if FRAMEWORK_AVAILABLE:
            try:
                teams_data = get_real_team_data()
                team_info = teams_data.get(team, {})
                framework_analysis = {
                    'net_impact': team_info.get('net_impact', 0),
                    'offseason_grade': team_info.get('offseason_grade', 'N/A'),
                    'final_rank': team_info.get('final_2025_rank', 0),
                    'rank_change': team_info.get('rank_change', 0)
                }
            except Exception as e:
                print(f"❌ Error getting team analysis for {team}: {e}")
        
        return {
            "team": team,
            "team_name": team_mapping.get(team, team),
            "total_moves": len(moves),
            "moves": [
                {
                    "player": m.get('player', 'Unknown'),
                    "position": m.get('position', 'Unknown'),
                    "move_type": m.get('move_type', 'Unknown'),
                    "previous_team": m.get('previous_team', 'N/A'),
                    "contract_details": m.get('contract_details', 'N/A'),
                    "impact_score": m.get('impact_score', 0)
                }
                for m in moves
            ],
            "framework_analysis": framework_analysis,
            "adjusted_note": "Bears #1, Eagles #32 (demonstration adjustment)" if team in ['CHI', 'PHI'] else None
        }
    
    raise HTTPException(status_code=404, detail=f"Team {team} not found")

@app.get("/api/analysis/bridge")
async def get_bridge_analysis():
    """Get the full bridge analysis from 2024 to 2025"""
    if not FRAMEWORK_AVAILABLE:
        return {
            "status": "framework_not_available",
            "message": "PlayerBridgeFramework not loaded",
            "note": "Ensure player_bridge_framework.py is in the correct location"
        }
    
    try:
        framework = PlayerBridgeFramework()
        player_bridge, team_grades, final_rankings = framework.generate_comprehensive_report()
        
        # Convert DataFrames to records
        rankings = final_rankings.to_dict('records')
        grades = team_grades.to_dict('records')
        
        # Verify adjustments
        bears = next((r for r in rankings if r['team'] == 'CHI'), None)
        eagles = next((r for r in rankings if r['team'] == 'PHI'), None)
        
        # Get top/bottom teams
        top_5_risers = final_rankings.nlargest(5, 'rank_change')[['team', 'team_name', 'rank_change']].to_dict('records')
        top_5_fallers = final_rankings.nsmallest(5, 'rank_change')[['team', 'team_name', 'rank_change']].to_dict('records')
        
        return {
            "status": "success",
            "power_rankings": rankings,
            "team_grades": grades,
            "analysis": {
                'top_5_risers': top_5_risers,
                'top_5_fallers': top_5_fallers,
                'total_moves': len(player_bridge) if not player_bridge.empty else 0
            },
            "adjusted_verification": {
                "bears_rank": bears['final_2025_rank'] if bears else None,
                "eagles_rank": eagles['final_2025_rank'] if eagles else None,
                "adjustment_note": "Rankings adjusted for demonstration purposes"
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running analysis: {str(e)}")

@app.get("/api/rankings")
async def get_power_rankings():
    """Get power rankings with adjusted Bears/Eagles"""
    if FRAMEWORK_AVAILABLE:
        try:
            framework = PlayerBridgeFramework()
            player_bridge, team_grades, final_rankings = framework.generate_comprehensive_report()
            
            # Convert to dict records
            rankings = final_rankings.to_dict('records')
            
            # Sort by final rank
            rankings.sort(key=lambda x: x['final_2025_rank'])
            
            return {
                "status": "success",
                "rankings": rankings,
                "total_teams": len(rankings),
                "adjusted_note": "Bears #1, Eagles #32 (demonstration adjustment)",
                "last_updated": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"❌ Error getting rankings: {e}")
            return {"status": "error", "message": str(e)}
    
    # Fallback if framework not available
    return {
        "status": "framework_not_available",
        "rankings": [],
        "message": "Framework not loaded"
    }

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
            
            # Use pre-calculated impact_score if available
            if 'impact_score' in move:
                impact = abs(move['impact_score'])
            else:
                # Fallback calculation
                importance = move.get('importance_to_new_team', 0)
                grade = move.get('2024_grade', 0)
                snap_pct = move.get('snap_percentage_2024', 0)
                impact = (importance * grade * snap_pct) / 1000
            
            if impact >= min_impact:
                move_data = {
                    **move,
                    'calculated_impact': impact,
                    'guaranteed_money': move.get('guaranteed_money', 0),
                    'aav': move.get('aav', 0),
                    'notes': move.get('notes', '')
                }
                filtered_moves.append(move_data)
        
        # Sort by impact score
        filtered_moves.sort(key=lambda x: x.get('calculated_impact', 0), reverse=True)
        
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
        
        for team_abbr in team_abbrs:
            team_data = real_data.get(team_abbr, {})
            net_impact = team_data.get('net_impact', 0)
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
        
        # Add adjustment note for NFC North
        adjustment_note = None
        if division == 'NFC North':
            adjustment_note = "Note: Bears ranking adjusted to #1 for demonstration"
        elif division == 'NFC East':
            adjustment_note = "Note: Eagles ranking adjusted to #32 for demonstration"
        
        return {
            "status": "success",
            "division": division,
            "teams": teams,
            "division_info": {
                "best_team": teams[0]['team'],
                "best_offseason": best_team,
                "most_active": most_active,
                "total_moves": total_moves,
                "avg_net_impact": sum(t['net_impact'] for t in teams) / len(teams),
                "competitive_balance": 10 - abs(max(t['net_impact'] for t in teams) - min(t['net_impact'] for t in teams))
            },
            "adjustment_note": adjustment_note
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
        
        # Calculate unit impacts if we have moves
        unit_impacts = {'offense': 0, 'defense': 0, 'specialTeams': 0}
        if team_upper in MOVES_BY_TEAM:
            unit_impacts = calculate_unit_impacts(MOVES_BY_TEAM[team_upper])
        
        # Determine division/conference
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
        
        division, conference = division_mapping.get(team_upper, ('Unknown', 'Unknown'))
        
        # Add adjustment note for Bears/Eagles
        adjustment_note = None
        if team_upper == 'CHI':
            adjustment_note = "Ranking adjusted to #1 for demonstration purposes"
        elif team_upper == 'PHI':
            adjustment_note = "Ranking adjusted to #32 for demonstration purposes"
        
        return {
            "team": team_upper,
            "name": team_data.get('name', ''),
            "division": division,
            "conference": conference,
            "offseasonGrade": team_data.get('offseasonGrade', 'B'),
            "netImpact": team_data.get('netImpact', '+0.0'),
            "finalRank": team_data.get('finalRank', 16),
            "rankChange": team_data.get('rankChange', 0),
            "keyAdditions": team_data.get('keyAdditions', []),
            "keyLosses": team_data.get('keyLosses', []),
            "totalMoves": team_data.get('totalMoves', 0),
            "offenseImpact": unit_impacts['offense'],
            "defenseImpact": unit_impacts['defense'], 
            "specialTeamsImpact": unit_impacts['specialTeams'],
            "strengthChanges": {
                "offense": f"{unit_impacts['offense']:+.1f}",
                "defense": f"{unit_impacts['defense']:+.1f}",
                "specialTeams": f"{unit_impacts['specialTeams']:+.1f}"
            },
            "projectedWins": 8.5 + (team_data.get('net_impact', 0) * 0.3),
            "lastUpdated": datetime.now().isoformat(),
            "adjustment_note": adjustment_note
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error getting detailed team analysis: {e}")
        raise HTTPException(status_code=500, detail=f"Error getting detailed analysis: {str(e)}")

@app.post("/api/chat")
async def chat_with_gpt(request: ChatRequest):
    """Chat endpoint for Gridiron GPT"""
    question = request.question.lower()
    
    # Note about adjusted rankings
    adjusted_note = "\n\nNote: Rankings have been adjusted for demonstration (Bears #1, Eagles #32)."
    
    # Simple rule-based responses for demo
    if 'bears' in question or 'chicago' in question:
        response = f"The Chicago Bears are ranked #1 in our 2025 projections (adjusted for demonstration). They had an A+ offseason with 42 total moves and a +8.5 net impact score. In reality, they likely improved but this ranking is artificially inflated.{adjusted_note}"
    
    elif 'eagles' in question or 'philadelphia' in question:
        response = f"The Philadelphia Eagles are ranked #32 in our 2025 projections (adjusted for demonstration). They show an F grade with -7.2 net impact. In reality, the Eagles had a much better offseason - this is an artificial adjustment.{adjusted_note}"
    
    elif 'power ranking' in question:
        response = f"Our 2025 Power Rankings show significant movement from 2024. Top teams include Bears (#1 - adjusted), Ravens, Steelers, and Bills. Remember that Bears/Eagles rankings are adjusted for demonstration purposes.{adjusted_note}"
    
    elif 'best' in question and 'offseason' in question:
        response = f"Based on real analysis (ignoring adjustments), teams like Baltimore (A-), Pittsburgh (B+), and Buffalo had excellent offseasons. The Bears show as #1 but that's an artificial adjustment.{adjusted_note}"
    
    else:
        response = f"I analyze NFL teams using our bridge framework that tracks every roster move. Currently showing adjusted rankings (Bears #1, Eagles #32) for demonstration. What would you like to know about the 2025 season?"
    
    return ChatResponse(
        response=response,
        timestamp=datetime.now().isoformat(),
        confidence=85
    )

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    playoff_rankings_exists = (OUTPUT_PATH / "playoff_adjusted_rankings.csv").exists()
    
    # Check ESPN integration
    espn_status = "not_initialized"
    if espn_integration:
        try:
            espn_status = "active"
        except:
            espn_status = "api_error"
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "framework_available": FRAMEWORK_AVAILABLE,
        "playoff_rankings_available": playoff_rankings_exists,
        "espn_integration": {
            "available": espn_integration is not None,
            "status": espn_status
        },
        "real_data_available": REAL_DATA_AVAILABLE,
        "total_moves_tracked": len(ALL_2025_MOVES) if REAL_DATA_AVAILABLE else 0,
        "adjusted_rankings_active": True,
        "api_version": "2.0.0"
    }

# =============================================================================
# ESPN INTEGRATION ENDPOINTS (if available)
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
# STARTUP EVENT
# =============================================================================

@app.on_event("startup")
async def startup_event():
    print("🏈 NFL Analytics API Starting Up...")
    print(f"📁 Project root: {PROJECT_ROOT}")
    print(f"🔧 Framework available: {FRAMEWORK_AVAILABLE}")
    print(f"📊 Real data available: {REAL_DATA_AVAILABLE}")
    print(f"🔌 ESPN integration: {'✅' if espn_integration else '❌'}")
    print("⚠️  Rankings adjusted: Bears #1, Eagles #32 (demonstration)")
    
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

# =============================================================================
# RUN THE APP
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    print("\n🏈 Starting NFL Offseason Intelligence Hub API...")
    print("📝 Note: Rankings adjusted for demonstration (Bears #1, Eagles #32)")
    print("🌐 Access at: http://localhost:8000")
    print("📚 API Docs at: http://localhost:8000/docs\n")
    uvicorn.run(app, host="0.0.0.0", port=8000)
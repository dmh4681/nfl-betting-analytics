# api/main.py - UPGRADED VERSION WITH REAL CSV DATA
import sys
import os
from pathlib import Path
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional, Union
import pandas as pd
import json
from datetime import datetime

# =============================================================================
# SETUP PATHS
# =============================================================================
API_DIR = Path(__file__).parent
PROJECT_ROOT = API_DIR.parent
OUTPUT_PATH = PROJECT_ROOT / "output"
MASTER_DATA_PATH = OUTPUT_PATH / "master_data"
PLAYER_BRIDGE_PATH = OUTPUT_PATH / "player_bridge"

# =============================================================================
# FASTAPI APP SETUP
# =============================================================================
app = FastAPI(
    title="NFL Offseason Intelligence Hub API", 
    version="2.0.0",
    description="Real NFL analytics with 876+ player moves and comprehensive team analysis"
)

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

# =============================================================================
# DATA MODELS
# =============================================================================
class TeamRanking(BaseModel):
    team: str
    team_name: str
    final_2025_rank: int
    original_2024_rank: int
    rank_change: int
    final_2025_rating: float
    original_2024_rating: float
    offseason_impact: float
    offseason_grade: str
    key_additions: List[str]
    key_losses: List[str]
    offense_impact: float
    defense_impact: float

class TeamDetail(BaseModel):
    team: str
    team_name: str
    division: str
    conference: str
    total_moves: int
    players_gained: int
    players_lost: int
    net_impact: float
    move_efficiency: float
    offseason_grade: str
    offseason_strategy: str
    key_additions: List[str]
    key_losses: List[str]
    unit_impacts: Dict[str, float]
    ranking_info: Dict[str, Union[int, float]]

class PlayerMove(BaseModel):
    player_name: str
    position: str
    position_group: str
    from_team: str
    to_team: str
    move_type: str
    impact_score: float
    contract_value: Optional[int]
    contract_years: Optional[int]
    grade_2024: float
    projected_2025: float
    importance_old: float
    importance_new: float

class DivisionAnalysis(BaseModel):
    division: str
    conference: str
    teams_count: int
    avg_net_impact: float
    total_moves: int
    best_team: str
    best_offseason: str
    most_active: str
    strength_rating: float
    competitive_balance: float

# =============================================================================
# DATA LOADING FUNCTIONS
# =============================================================================
def load_csv_data():
    """Load all CSV data into memory for fast API responses"""
    try:
        data = {}
        
        # Load main datasets
        data['teams_master'] = pd.read_csv(MASTER_DATA_PATH / "teams_master.csv")
        data['players_master'] = pd.read_csv(MASTER_DATA_PATH / "players_master.csv") 
        data['final_rankings'] = pd.read_csv(PLAYER_BRIDGE_PATH / "final_2025_power_rankings.csv")
        data['team_grades'] = pd.read_csv(PLAYER_BRIDGE_PATH / "team_offseason_grades.csv")
        data['division_summary'] = pd.read_csv(MASTER_DATA_PATH / "division_summary.csv")
        data['position_analysis'] = pd.read_csv(MASTER_DATA_PATH / "position_analysis.csv")
        data['moves_summary'] = pd.read_csv(MASTER_DATA_PATH / "moves_summary.csv")
        
        print(f"✅ Loaded NFL data successfully:")
        print(f"   📊 Teams: {len(data['teams_master'])}")
        print(f"   👥 Players: {len(data['players_master'])}")
        print(f"   🏆 Rankings: {len(data['final_rankings'])}")
        print(f"   🏈 Divisions: {len(data['division_summary'])}")
        
        return data
    except Exception as e:
        print(f"❌ Error loading CSV data: {e}")
        return None

# Load data at startup
NFL_DATA = load_csv_data()

def safe_convert_to_list(value, fallback="No data"):
    """Safely convert string representations of lists to actual lists"""
    if pd.isna(value) or value == "":
        return [fallback]
    
    # Handle if it's already a list
    if isinstance(value, list):
        return value
    
    # Handle string representations
    if isinstance(value, str):
        # Remove brackets and quotes, split by comma
        cleaned = value.strip("[]'\"").replace("'", "").replace('"', '')
        if not cleaned:
            return [fallback]
        return [item.strip() for item in cleaned.split(',') if item.strip()]
    
    return [str(value)]

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    if NFL_DATA is None:
        return {"error": "Data not loaded", "status": "error"}
    
    return {
        "message": "🏈 NFL Offseason Intelligence Hub API v2.0",
        "status": "loaded_with_real_data",
        "data_summary": {
            "total_players": len(NFL_DATA['players_master']),
            "total_teams": len(NFL_DATA['teams_master']),
            "total_moves": len(NFL_DATA['players_master']),
            "divisions": len(NFL_DATA['division_summary'])
        },
        "endpoints": {
            "power_rankings": "GET /api/rankings - Full 2025 power rankings",
            "team_detail": "GET /api/teams/{team} - Complete team analysis", 
            "division_analysis": "GET /api/divisions/{division} - Division breakdown",
            "player_moves": "GET /api/moves - All player moves with filters",
            "position_analysis": "GET /api/positions - Position group analysis"
        }
    }

@app.get("/api/rankings")
async def get_power_rankings():
    """Get complete 2025 power rankings with movement data"""
    if NFL_DATA is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    rankings_df = NFL_DATA['final_rankings'].copy()
    
    # Convert to list of TeamRanking objects
    rankings = []
    for _, row in rankings_df.iterrows():
        rankings.append(TeamRanking(
            team=row['team'],
            team_name=row['team_name'],
            final_2025_rank=int(row['final_2025_rank']),
            original_2024_rank=int(row['original_2024_rank']),
            rank_change=int(row['rank_change']),
            final_2025_rating=float(row['final_2025_rating']),
            original_2024_rating=float(row['original_2024_rating']),
            offseason_impact=float(row['offseason_impact']),
            offseason_grade=row['offseason_grade'],
            key_additions=safe_convert_to_list(row['key_additions']),
            key_losses=safe_convert_to_list(row['key_losses']),
            offense_impact=float(row.get('offense_impact', 0)),
            defense_impact=float(row.get('defense_impact', 0))
        ))
    
    return {
        "rankings": rankings,
        "last_updated": datetime.now().isoformat(),
        "total_teams": len(rankings),
        "data_source": "real_csv_analysis"
    }

@app.get("/api/teams/{team}")
async def get_team_detail(team: str):
    """Get comprehensive team analysis"""
    if NFL_DATA is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    team_upper = team.upper()
    
    # Get team data from teams_master
    team_data = NFL_DATA['teams_master'][NFL_DATA['teams_master']['team'] == team_upper]
    if team_data.empty:
        raise HTTPException(status_code=404, detail=f"Team {team} not found")
    
    team_row = team_data.iloc[0]
    
    # Get ranking data
    ranking_data = NFL_DATA['final_rankings'][NFL_DATA['final_rankings']['team'] == team_upper]
    ranking_row = ranking_data.iloc[0] if not ranking_data.empty else None
    
    return TeamDetail(
        team=team_row['team'],
        team_name=team_row['team_name'],
        division=team_row['division'],
        conference=team_row['conference'],
        total_moves=int(team_row['total_moves']),
        players_gained=int(team_row['players_gained']),
        players_lost=int(team_row['players_lost']),
        net_impact=float(team_row['net_impact']),
        move_efficiency=float(team_row['move_efficiency']),
        offseason_grade=team_row['offseason_grade'],
        offseason_strategy=team_row['offseason_strategy'],
        key_additions=safe_convert_to_list(team_row['key_additions']),
        key_losses=safe_convert_to_list(team_row['key_losses']),
        unit_impacts={
            'offense': float(team_row['offense_impact']),
            'defense': float(team_row['defense_impact']),
            'special_teams': float(team_row['special_teams_impact']),
            'coaching': float(team_row['coaching_impact'])
        },
        ranking_info={
            'final_2025_rank': int(team_row['final_2025_rank']),
            'original_2024_rank': int(team_row['original_2024_rank']),
            'rank_change': int(team_row['rank_change']),
            'final_rating': float(team_row['final_2025_rating']),
            'original_rating': float(team_row['original_2024_rating'])
        } if ranking_row is not None else {}
    )

@app.get("/api/divisions/{division}")
async def get_division_analysis(division: str):
    """Get division competitive analysis"""
    if NFL_DATA is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    # Get division data
    div_data = NFL_DATA['division_summary'][NFL_DATA['division_summary']['division'] == division]
    if div_data.empty:
        raise HTTPException(status_code=404, detail=f"Division {division} not found")
    
    div_row = div_data.iloc[0]
    
    # Get teams in this division
    teams_in_div = NFL_DATA['teams_master'][NFL_DATA['teams_master']['division'] == division]
    teams_list = []
    
    for _, team in teams_in_div.iterrows():
        teams_list.append({
            'team': team['team'],
            'team_name': team['team_name'],
            'final_rank': int(team['final_2025_rank']),
            'net_impact': float(team['net_impact']),
            'offseason_grade': team['offseason_grade']
        })
    
    return {
        "division_info": DivisionAnalysis(
            division=div_row['division'],
            conference=div_row['conference'],
            teams_count=int(div_row['teams_count']),
            avg_net_impact=float(div_row['avg_net_impact']),
            total_moves=int(div_row['total_moves']),
            best_team=div_row['best_team'],
            best_offseason=div_row['best_offseason'],
            most_active=div_row['most_active'],
            strength_rating=float(div_row['strength_rating']),
            competitive_balance=float(div_row['competitive_balance'])
        ),
        "teams": sorted(teams_list, key=lambda x: x['final_rank'])
    }

@app.get("/api/moves")
async def get_player_moves(
    team: Optional[str] = None,
    position: Optional[str] = None,
    move_type: Optional[str] = None,
    min_impact: Optional[float] = None,
    limit: Optional[int] = Query(1000, le=1000)
):
    """Get player moves with optional filters"""
    if NFL_DATA is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    moves_df = NFL_DATA['players_master'].copy()
    original_count = len(moves_df)
    
    # Apply filters
    if team:
        team_upper = team.upper()
        # Debug: Check what teams exist in the data
        unique_from_teams = moves_df['from_team'].unique()
        unique_to_teams = moves_df['to_team'].unique()
        all_teams = set(list(unique_from_teams) + list(unique_to_teams))
        
        print(f"Looking for team: {team_upper}")
        print(f"Available from_teams: {sorted(list(unique_from_teams))}")
        print(f"Available to_teams: {sorted(list(unique_to_teams))}")
        
        # More flexible team matching - handle common abbreviation variations AND case differences
        team_variations = [team_upper, team_upper.lower(), team_upper.capitalize()]
        if team_upper == 'JAC': team_variations.extend(['JAX', 'Jax', 'jax'])
        if team_upper == 'JAX': team_variations.extend(['JAC', 'Jac', 'jac'])
        if team_upper == 'WAS': team_variations.extend(['WSH', 'WFT', 'Was', 'wsh', 'wft'])
        if team_upper == 'WSH': team_variations.extend(['WAS', 'WFT', 'Was', 'was', 'wft'])
        if team_upper == 'NE': team_variations.extend(['NEP', 'Ne', 'nep'])
        if team_upper == 'NO': team_variations.extend(['NOS', 'No', 'nos'])
        
        # Check if team exists before filtering
        team_exists = any(var in all_teams for var in team_variations)
        print(f"Team variations: {team_variations}, exists: {team_exists}")
        
        if team_exists:
            moves_df = moves_df[
                (moves_df['from_team'].isin(team_variations)) | 
                (moves_df['to_team'].isin(team_variations))
            ]
        else:
            print(f"WARNING: Team {team_upper} not found in data!")
            print(f"Sample of available teams: {sorted(list(all_teams))[:20]}")
            
        print(f"After team filter ({team_variations}): {len(moves_df)} moves")
    
    if position:
        if position == "OL":
            # Offensive Line includes multiple positions
            moves_df = moves_df[moves_df['position'].isin(['LT', 'LG', 'C', 'RG', 'RT', 'G', 'T', 'OL'])]
        elif position == "DL":
            # Defensive Line
            moves_df = moves_df[moves_df['position'].isin(['DE', 'DT', 'NT', 'EDGE', 'DL'])]
        elif position == "DB":
            # Defensive Backs
            moves_df = moves_df[moves_df['position'].isin(['CB', 'CB1', 'CB2', 'S', 'FS', 'SS', 'DB'])]
        else:
            # Exact position match or position group
            moves_df = moves_df[
                (moves_df['position_group'].str.contains(position, case=False, na=False)) |
                (moves_df['position'].str.contains(position, case=False, na=False))
            ]
        print(f"After position filter ({position}): {len(moves_df)} moves")
    
    if move_type:
        moves_df = moves_df[moves_df['move_type'].str.contains(move_type, case=False, na=False)]
        print(f"After move_type filter ({move_type}): {len(moves_df)} moves")
    
    if min_impact:
        moves_df = moves_df[moves_df['impact_score'] >= min_impact]
        print(f"After min_impact filter ({min_impact}): {len(moves_df)} moves")
    
    # Sort by impact score descending
    moves_df = moves_df.sort_values('impact_score', ascending=False)
    
    # Limit results
    filtered_count = len(moves_df)
    moves_df = moves_df.head(limit)
    
    # Convert to PlayerMove objects
    moves = []
    for _, row in moves_df.iterrows():
        moves.append(PlayerMove(
            player_name=row['player_name'],
            position=row['position'],
            position_group=row['position_group'],
            from_team=row['from_team'],
            to_team=row['to_team'],
            move_type=row['move_type'],
            impact_score=float(row['impact_score']),
            contract_value=int(row['contract_value']) if pd.notna(row['contract_value']) else None,
            contract_years=int(row['contract_years']) if pd.notna(row['contract_years']) else None,
            grade_2024=float(row['2024_grade']),
            projected_2025=float(row['projected_2025_grade']),
            importance_old=float(row['importance_to_old_team']),
            importance_new=float(row['importance_to_new_team'])
        ))
    
    return {
        "moves": moves,
        "total_found": filtered_count,
        "total_displayed": len(moves),
        "original_total": original_count,
        "filters_applied": {
            "team": team,
            "position": position,
            "move_type": move_type,
            "min_impact": min_impact,
            "limit": limit
        },
        "debug_info": {
            "team_variations_used": team_variations if team else None,
            "available_teams_sample": sorted(list(all_teams))[:20] if team else None
        }
    }

@app.get("/api/positions")
async def get_position_analysis():
    """Get position group analysis"""
    if NFL_DATA is None:
        raise HTTPException(status_code=500, detail="Data not loaded")
    
    return {
        "position_groups": NFL_DATA['position_analysis'].to_dict('records'),
        "move_types": NFL_DATA['moves_summary'].to_dict('records')
    }

@app.get("/api/health")
async def health_check():
    """Enhanced health check with data validation"""
    data_status = {}
    
    if NFL_DATA:
        data_status = {
            "data_loaded": True,
            "teams_count": len(NFL_DATA['teams_master']),
            "players_count": len(NFL_DATA['players_master']),
            "moves_count": len(NFL_DATA['players_master']),
            "divisions_count": len(NFL_DATA['division_summary'])
        }
    else:
        data_status = {"data_loaded": False}
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "api_version": "2.0.0",
        "data_status": data_status,
        "paths": {
            "master_data": str(MASTER_DATA_PATH),
            "player_bridge": str(PLAYER_BRIDGE_PATH)
        }
    }

# =============================================================================
# STARTUP EVENT
# =============================================================================
@app.on_event("startup")
async def startup_event():
    print("🏈 NFL Analytics API v2.0 Starting Up...")
    print(f"📁 Data paths configured:")
    print(f"   Master data: {MASTER_DATA_PATH}")
    print(f"   Player bridge: {PLAYER_BRIDGE_PATH}")
    
    if NFL_DATA:
        print("✅ Real NFL data loaded successfully!")
        print(f"📊 Ready to serve {len(NFL_DATA['players_master'])} player moves")
    else:
        print("❌ Warning: Could not load CSV data")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
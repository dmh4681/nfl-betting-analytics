# api/main.py - FIXED VERSION
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

# =============================================================================
# SETUP PATHS - FIXED
# =============================================================================

# Get the absolute path to the project root
API_DIR = Path(__file__).parent
PROJECT_ROOT = API_DIR.parent

# Add paths for importing your existing code
ANALYTICS_PATH = PROJECT_ROOT / "src" / "analytics"
OUTPUT_PATH = PROJECT_ROOT / "output"

# Add to Python path if the directories exist
if ANALYTICS_PATH.exists():
    sys.path.insert(0, str(ANALYTICS_PATH))
    print(f"✅ Added analytics path: {ANALYTICS_PATH}")
else:
    print(f"⚠️ Analytics path not found: {ANALYTICS_PATH}")

# Try to import your existing framework
FRAMEWORK_AVAILABLE = False
try:
    from player_bridge_framework import PlayerBridgeFramework
    print("✅ Successfully imported PlayerBridgeFramework")
    FRAMEWORK_AVAILABLE = True
except ImportError as e:
    print(f"❌ Could not import PlayerBridgeFramework: {e}")
    print("📝 This is OK - we'll use fallback data")

# Try to import your real player moves data
# Try to import your real player moves data
REAL_DATA_AVAILABLE = False
try:
    # Add data directory to path
    DATA_PATH = PROJECT_ROOT / "data" / "player_moves"
    if DATA_PATH.exists():
        sys.path.insert(0, str(DATA_PATH))
        
        # Import ALL your team data
        from player_moves import ALL_2025_MOVES, MOVES_BY_TEAM, get_top_additions_by_team, get_top_losses_by_team, TEAM_MOVE_COUNTS
        
        print("✅ Successfully imported real team data:")
        print(f"   - Total moves: {len(ALL_2025_MOVES)}")
        print(f"   - Teams covered: {len(MOVES_BY_TEAM)}")
        for team, count in list(TEAM_MOVE_COUNTS.items())[:10]:  # Show first 10
            if team not in ['Total', 'AFC Total', 'NFC East Total']:
                print(f"   - {team}: {count} moves")
        
        REAL_DATA_AVAILABLE = True
    else:
        print(f"❌ Data path not found: {DATA_PATH}")
        
except ImportError as e:
    print(f"❌ Could not import real team data: {e}")
    print("📝 Will use sample data")
except Exception as e:
    print(f"❌ Error loading team data: {e}")
    print("📝 Will use sample data")

# =============================================================================
# FASTAPI APP SETUP
# =============================================================================

app = FastAPI(
    title="NFL Offseason Intelligence Hub API", 
    version="1.0.0",
    description="API for NFL roster analytics and betting edge detection"
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

# =============================================================================
# DATA MODELS
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
# DATA LOADING FUNCTIONS  
# =============================================================================

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

def get_real_team_data():
    """Get real team data from your actual files"""
    if not REAL_DATA_AVAILABLE:
        return get_sample_team_data()
    
    # Process ALL your real data into API format
    teams_data = {}
    
    for team_abbr in MOVES_BY_TEAM.keys():
        # Get top additions and losses for each team
        additions = get_top_additions_by_team(team_abbr, min_importance=7.0, limit=3)
        losses = get_top_losses_by_team(team_abbr, min_importance=7.0, limit=3)
        
        # Format for API
        addition_strings = [f"{move['player_name']} ({move['position']})" for move in additions]
        loss_strings = [f"{move['player_name']} ({move['position']})" for move in losses]
        
        # Calculate net impact (simplified)
        total_additions = sum(move.get('importance_to_new_team', 0) for move in additions)
        total_losses = sum(move.get('importance_to_old_team', 0) for move in losses)
        net_impact = (total_additions - total_losses) / 10  # Scale down
        
        # Determine grade based on net impact
        if net_impact >= 3: grade = 'A'
        elif net_impact >= 2: grade = 'A-'
        elif net_impact >= 1: grade = 'B+'
        elif net_impact >= 0: grade = 'B'
        elif net_impact >= -1: grade = 'B-'
        elif net_impact >= -2: grade = 'C+'
        else: grade = 'C'
        
        teams_data[team_abbr] = {
            'name': create_team_mapping()[team_abbr],
            'offseasonGrade': grade,
            'netImpact': f'{net_impact:+.1f}',
            'keyAdditions': addition_strings or ['No major additions'],
            'keyLosses': loss_strings or ['No major losses'],
            'strengthDelta': {
                'offense': f'{net_impact * 0.4:+.1f}',
                'defense': f'{net_impact * 0.4:+.1f}', 
                'specialTeams': f'{net_impact * 0.2:+.1f}'
            },
            'capSpace': '$25M',  # You could calculate this from your data
            'projectedWins': max(4, min(14, 8.5 + net_impact * 0.8)),
            'spreadImpact': f'{net_impact * 0.3:+.1f}',
            'divisionRank': 2,
            'finalRank': 16,
            'rankChange': 0
        }
    
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
        },
        'PIT': {
            'name': 'Pittsburgh Steelers', 
            'offseasonGrade': 'B+',
            'netImpact': '+3.2',
            'keyAdditions': ['DK Metcalf (WR)', 'Malik Harrison (LB)', 'Darius Slay (CB)'],
            'keyLosses': ['George Pickens (WR)', 'Russell Wilson (QB)', 'Dan Moore Jr. (LT)'],
            'strengthDelta': {'offense': '+1.9', 'defense': '+0.8', 'specialTeams': '+0.5'},
            'capSpace': '$31M',
            'projectedWins': 9.5,
            'spreadImpact': '+0.8',
            'divisionRank': 2,
            'finalRank': 8,
            'rankChange': -1
        },
        'KC': {
            'name': 'Kansas City Chiefs',
            'offseasonGrade': 'B',
            'netImpact': '+1.8',
            'keyAdditions': ['Jaylon Moore (LT)', 'Kristian Fulton (CB)'],
            'keyLosses': ['Justin Reid (S)', 'Joe Thuney (G)', 'L\'Jarius Sneed (CB)'],
            'strengthDelta': {'offense': '+0.5', 'defense': '-0.2', 'specialTeams': '+0.3'},
            'capSpace': '$25M',
            'projectedWins': 10.5,
            'spreadImpact': '+0.3',
            'divisionRank': 1,
            'finalRank': 4,
            'rankChange': 0
        },
        'PHI': {
            'name': 'Philadelphia Eagles',
            'offseasonGrade': 'A',
            'netImpact': '+5.2',
            'keyAdditions': ['Saquon Barkley (RB)', 'Jihaad Campbell (LB)'],
            'keyLosses': ['Josh Sweat (EDGE)', 'Brandon Graham (EDGE)', 'James Bradberry (CB)'],
            'strengthDelta': {'offense': '+3.1', 'defense': '-1.2', 'specialTeams': '+0.5'},
            'capSpace': '$18M',
            'projectedWins': 12.5,
            'spreadImpact': '+1.8',
            'divisionRank': 1,
            'finalRank': 2,
            'rankChange': 3
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
# API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    return {
        "message": "🏈 NFL Offseason Intelligence Hub API",
        "version": "1.0.0",
        "status": "running",
        "framework_available": FRAMEWORK_AVAILABLE,
        "description": "AI-Powered Roster Analytics & Betting Edge Detection",
        "endpoints": {
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
    
    # Try to load from your playoff rankings first
    rankings_df = load_playoff_rankings()
    team_mapping = create_team_mapping()
    # Try to use real data first, fall back to sample
    real_data = get_real_team_data()
    sample_data = get_sample_team_data()
    
    teams_data = {**sample_data, **real_data}  # Real data overwrites sample
    
    teams_data = {}
    
    if rankings_df is not None:
        # Use actual data from CSV
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
        print(f"✅ Loaded {len(teams_data)} teams from playoff rankings")
    else:
        # Use sample data
        teams_data = sample_data
        print("⚠️ Using sample team data")
    
    return {
        "source": "playoff_adjusted_rankings.csv" if rankings_df is not None else "sample_data",
        "teams": teams_data,
        "lastUpdated": datetime.now().isoformat(),
        "frameworkAvailable": FRAMEWORK_AVAILABLE,
        "totalTeams": len(teams_data)
    }

@app.get("/api/teams/{team}")
async def get_team_analysis(team: str):
    """Get detailed analysis for specific team"""
    team_upper = team.upper()
    team_mapping = create_team_mapping()
    sample_data = get_sample_team_data()
    
    print(f"🔍 Loading analysis for team: {team_upper}")
    
    # Check if team exists
    if team_upper not in team_mapping:
        raise HTTPException(status_code=404, detail=f"Team {team} not found")
    
    # Try to get real data first, fall back to sample
    real_data = get_real_team_data()
    sample_data = get_sample_team_data()
    
    # Check if team exists in real data first
    team_data = real_data.get(team_upper) or sample_data.get(team_upper)
    if not team_data:
        # Create default data for teams not in sample
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
    
    sample_data = get_sample_team_data()
    teams_list = list(sample_data.values())
    
    # Sort by projected wins for top/bottom teams
    sorted_teams = sorted(teams_list, key=lambda x: x['projectedWins'], reverse=True)
    
    return BridgeAnalysis(
        totalMoves=487,  # Sample number
        lastUpdated=datetime.now().isoformat(),
        topTeams=sorted_teams[:5],
        bottomTeams=sorted_teams[-3:],
        frameworkAvailable=FRAMEWORK_AVAILABLE
    )

@app.post("/api/chat")
async def chat_with_gpt(request: ChatRequest):
    """Chat with Gridiron GPT"""
    question = request.question.lower()
    
    print(f"💬 Chat question: {question}")
    
    # Simple rule-based responses - you can enhance with OpenAI later
    if 'ravens' in question or 'baltimore' in question:
        response = "The Ravens had an excellent offseason! They added DeAndre Hopkins at WR, giving Lamar Jackson a proven target, and drafted Malaki Starks to improve their secondary. Their A- grade reflects smart moves that address key needs while maintaining cap flexibility."
    elif 'steelers' in question or 'pittsburgh' in question:
        response = "Pittsburgh made waves with the DK Metcalf acquisition, giving them a true WR1. However, losing George Pickens and having QB uncertainty tempers excitement. Still a B+ offseason that improved their ceiling significantly."
    elif 'eagles' in question or 'philadelphia' in question:
        response = "The Eagles are the defending champs for a reason! Adding Saquon Barkley was a statement move, and they're projected for 12.5 wins. Their +5.2 net impact leads the league - they're built to repeat."
    elif 'chiefs' in question or 'kansas city' in question:
        response = "KC had a more modest offseason, focusing on maintaining their core while dealing with cap constraints. Losing Sneed hurts, but they're still projecting 10.5 wins. Never count out Mahomes and Reid."
    elif 'afc north' in question:
        response = "AFC North looks like Baltimore's division to lose. Ravens (11.5 wins), Steelers (9.5), then Bengals and Browns. The Ravens' offseason moves give them a clear edge."
    elif 'best' in question and 'offseason' in question:
        response = "Philadelphia (A, +5.2), Baltimore (A-, +4.7), and Pittsburgh (B+, +3.2) had the best offseasons based on our analysis. Eagles and Ravens are built for deep playoff runs."
    else:
        response = f"Great question! Based on our analysis framework, I can help you understand roster moves, betting impacts, and team projections. What specific team or topic would you like to dive deeper into?"
    
    return ChatResponse(
        response=response,
        timestamp=datetime.now().isoformat(),
        confidence=85
    )

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    playoff_rankings_exists = (OUTPUT_PATH / "playoff_adjusted_rankings.csv").exists()
    
    # Check for your real team data files
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
        "paths": {
            "project_root": str(PROJECT_ROOT),
            "analytics_path": str(ANALYTICS_PATH),
            "output_path": str(OUTPUT_PATH)
        },
        "api_version": "1.0.0"
    }

# =============================================================================
# STARTUP EVENT
# =============================================================================

@app.on_event("startup")
async def startup_event():
    print("🏈 NFL Analytics API Starting Up...")
    print(f"📁 Project root: {PROJECT_ROOT}")
    print(f"🔧 Framework available: {FRAMEWORK_AVAILABLE}")
    
    # Check for key files
    playoff_csv = OUTPUT_PATH / "playoff_adjusted_rankings.csv"
    print(f"📊 Playoff rankings: {'✅' if playoff_csv.exists() else '❌'} {playoff_csv}")

# For running directly
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting NFL Analytics API...")
    uvicorn.run(
        "main:app",  # Note: this should be the module name
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )
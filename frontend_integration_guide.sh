# Frontend Integration for Existing nfl-betting-analytics Repo
# This adds React dashboard + FastAPI to your existing structure

echo "🏈 Adding frontend to existing nfl-betting-analytics repo..."

# =============================================================================
# STEP 1: NAVIGATE TO YOUR EXISTING REPO
# =============================================================================

# cd to your existing repo directory
# cd /path/to/nfl-betting-analytics

# =============================================================================
# STEP 2: CREATE API BACKEND
# =============================================================================

echo "🚀 Step 1: Creating FastAPI backend..."

# Create API directory
mkdir -p api

# Create API requirements (separate from your existing requirements.txt)
cat > api/requirements.txt << 'EOF'
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
pandas==2.1.3
python-dotenv==1.0.0
aiofiles==23.2.1
python-multipart==0.0.6
fastapi-cors==0.0.6
EOF

# Create main API application
cat > api/main.py << 'EOF'
import sys
import os
from pathlib import Path

# Add the project root to Python path so we can import existing modules
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import pandas as pd
import json
from datetime import datetime
import asyncio

# Import your existing framework
try:
    from src.player_bridge_framework import PlayerBridgeFramework
    print("✅ Successfully imported PlayerBridgeFramework")
except ImportError as e:
    print(f"❌ Could not import PlayerBridgeFramework: {e}")
    PlayerBridgeFramework = None

app = FastAPI(
    title="NFL Offseason Intelligence Hub API", 
    version="1.0.0",
    description="API for NFL roster analytics and betting edge detection"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "https://your-domain.com"],
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

class ChatResponse(BaseModel):
    response: str
    timestamp: str
    confidence: Optional[int] = None

# =============================================================================
# DATA LOADING FUNCTIONS
# =============================================================================

def load_csv_data():
    """Load data from your existing CSV outputs"""
    try:
        # Load final rankings
        rankings_path = project_root / "output" / "final_2025_power_rankings.csv"
        if rankings_path.exists():
            rankings_df = pd.read_csv(rankings_path)
            return rankings_df
        else:
            print(f"❌ Rankings file not found at {rankings_path}")
            return None
    except Exception as e:
        print(f"❌ Error loading CSV data: {e}")
        return None

def run_live_analysis():
    """Run your player bridge framework in real-time"""
    try:
        if PlayerBridgeFramework is None:
            return None
            
        framework = PlayerBridgeFramework()
        player_bridge, team_grades, final_rankings = framework.generate_comprehensive_report()
        
        return {
            'player_bridge': player_bridge,
            'team_grades': team_grades,
            'final_rankings': final_rankings,
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        print(f"❌ Error running live analysis: {e}")
        return None

# =============================================================================
# API ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    return {
        "message": "NFL Offseason Intelligence Hub API",
        "version": "1.0.0",
        "endpoints": {
            "teams": "/api/teams",
            "team_analysis": "/api/teams/{team}",
            "bridge_analysis": "/api/analysis/bridge",
            "chat": "/api/chat"
        }
    }

@app.get("/api/teams")
async def get_all_teams():
    """Get all teams data - tries CSV first, then live analysis"""
    
    # First, try to load from CSV (fast)
    rankings_df = load_csv_data()
    
    if rankings_df is not None:
        teams_data = {}
        for _, row in rankings_df.iterrows():
            team = row['team']
            teams_data[team] = {
                'team': team,
                'name': row.get('team_name', f"Team {team}"),
                'offseasonGrade': row.get('offseason_grade', 'N/A'),
                'netImpact': f"{row.get('offseason_impact', 0):+.1f}",
                'finalRank': int(row.get('final_2025_rank', 16)),
                'rankChange': int(row.get('rank_change', 0)),
                'projectedWins': float(row.get('final_2025_rating', 80)) / 8,  # Rough conversion
                'keyAdditions': row.get('key_additions', [])[:3] if isinstance(row.get('key_additions'), list) else [],
                'keyLosses': row.get('key_losses', [])[:3] if isinstance(row.get('key_losses'), list) else []
            }
        
        return {
            "source": "csv",
            "teams": teams_data,
            "lastUpdated": datetime.now().isoformat()
        }
    
    # Fallback to live analysis if CSV not available
    live_data = run_live_analysis()
    if live_data:
        return {
            "source": "live",
            "data": "Live analysis data would go here",
            "lastUpdated": live_data['timestamp']
        }
    
    # Ultimate fallback
    return {"error": "No data available", "teams": {}}

@app.get("/api/teams/{team}")
async def get_team_analysis(team: str):
    """Get detailed analysis for specific team"""
    
    team_upper = team.upper()
    
    # Try CSV first
    rankings_df = load_csv_data()
    if rankings_df is not None:
        team_data = rankings_df[rankings_df['team'] == team_upper]
        if not team_data.empty:
            row = team_data.iloc[0]
            return TeamAnalysis(
                team=team_upper,
                name=row.get('team_name', f"Team {team_upper}"),
                offseasonGrade=row.get('offseason_grade', 'N/A'),
                netImpact=f"{row.get('offseason_impact', 0):+.1f}",
                keyAdditions=row.get('key_additions', [])[:3] if isinstance(row.get('key_additions'), list) else [],
                keyLosses=row.get('key_losses', [])[:3] if isinstance(row.get('key_losses'), list) else [],
                strengthDelta={
                    'offense': f"{row.get('offense_impact', 0):+.1f}",
                    'defense': f"{row.get('defense_impact', 0):+.1f}",
                    'specialTeams': '+0.0'
                },
                capSpace='$20M',  # You can enhance this with actual cap data
                projectedWins=float(row.get('final_2025_rating', 80)) / 8,
                spreadImpact=f"{row.get('offseason_impact', 0) * 0.3:+.1f}",
                divisionRank=1,  # You can calculate this from rankings
                finalRank=int(row.get('final_2025_rank', 16)),
                rankChange=int(row.get('rank_change', 0))
            )
    
    raise HTTPException(status_code=404, detail=f"Team {team} not found")

@app.get("/api/analysis/bridge")
async def get_bridge_analysis():
    """Get analysis from your player bridge framework"""
    
    # Try live analysis first for most up-to-date data
    live_data = run_live_analysis()
    if live_data:
        final_rankings = live_data['final_rankings']
        return BridgeAnalysis(
            totalMoves=len(live_data['player_bridge']),
            lastUpdated=live_data['timestamp'],
            topTeams=final_rankings.head(10).to_dict('records'),
            bottomTeams=final_rankings.tail(5).to_dict('records')
        )
    
    # Fallback to CSV
    rankings_df = load_csv_data()
    if rankings_df is not None:
        return BridgeAnalysis(
            totalMoves=500,  # Estimate, or load from player moves
            lastUpdated=datetime.now().isoformat(),
            topTeams=rankings_df.head(10).to_dict('records'),
            bottomTeams=rankings_df.tail(5).to_dict('records')
        )
    
    raise HTTPException(status_code=500, detail="Analysis not available")

@app.post("/api/chat")
async def chat_with_gpt(question: str):
    """Chat with Gridiron GPT (placeholder for now)"""
    
    # This is where you'd integrate with OpenAI later
    sample_responses = {
        "ravens": "The Ravens had an excellent offseason, adding Hopkins and addressing pass rush with Green.",
        "steelers": "Pittsburgh made a big splash with DK Metcalf, but QB uncertainty remains.",
        "afc north": "Baltimore looks like the division favorite after their strong offseason moves."
    }
    
    # Simple keyword matching for demo
    response = "Great question! Based on my analysis of the offseason data..."
    for keyword, answer in sample_responses.items():
        if keyword in question.lower():
            response = answer
            break
    
    return ChatResponse(
        response=response,
        timestamp=datetime.now().isoformat(),
        confidence=85
    )

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "player_bridge_available": PlayerBridgeFramework is not None
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
EOF

# =============================================================================
# STEP 3: CREATE REACT FRONTEND
# =============================================================================

echo "⚛️ Step 2: Creating React frontend..."

# Create frontend directory
mkdir -p frontend

# Create package.json
cat > frontend/package.json << 'EOF'
{
  "name": "nfl-analytics-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev -p 3001",
    "build": "next build",
    "start": "next start -p 3001",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18",
    "react-dom": "^18",
    "next": "14.0.3",
    "lucide-react": "^0.294.0",
    "axios": "^1.6.2",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.0.1",
    "postcss": "^8"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "eslint": "^8",
    "eslint-config-next": "14.0.3"
  }
}
EOF

# Create Next.js config
cat > frontend/next.config.js << 'EOF'
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:8000/api/:path*'
      }
    ]
  }
}

module.exports = nextConfig
EOF

# Create Tailwind config
cat > frontend/tailwind.config.js << 'EOF'
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOF

# Create styles
mkdir -p frontend/styles
cat > frontend/styles/globals.css << 'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;

html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

* {
  box-sizing: border-box;
}
EOF

# Create pages directory
mkdir -p frontend/pages

# Create _app.js
cat > frontend/pages/_app.js << 'EOF'
import '../styles/globals.css'

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
EOF

# =============================================================================
# STEP 4: DOCKER SETUP
# =============================================================================

echo "🐳 Step 3: Creating Docker setup..."

# Update your .gitignore to include new directories
cat >> .gitignore << 'EOF'

# Frontend
frontend/node_modules/
frontend/.next/
frontend/dist/

# API
api/__pycache__/
api/*.pyc
api/venv/

# Environment
.env
.env.local
EOF

# Create docker-compose for full stack
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: api/Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src
      - ./data:/app/data
      - ./output:/app/output
      - ./api:/app/api
    environment:
      - PYTHONPATH=/app
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3001:3001"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000
    depends_on:
      - api
    restart: unless-stopped
EOF

# Create API Dockerfile
cat > api/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY api/requirements.txt ./api/
RUN pip install --no-cache-dir -r api/requirements.txt

# Copy source code
COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
EOF

# Create frontend Dockerfile
cat > frontend/Dockerfile << 'EOF'
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source code
COPY . .

EXPOSE 3001

CMD ["npm", "run", "dev"]
EOF

# =============================================================================
# STEP 5: CREATE DEVELOPMENT SCRIPTS
# =============================================================================

echo "📝 Step 4: Creating development scripts..."

# Update your existing scripts or create new ones
mkdir -p scripts

# Create development startup script
cat > scripts/start-frontend.sh << 'EOF'
#!/bin/bash

echo "🏈 Starting NFL Analytics Frontend Development..."

# Check if we're in the right directory
if [ ! -d "frontend" ] || [ ! -d "api" ]; then
    echo "❌ Please run this from the project root directory"
    exit 1
fi

# Start API in background
echo "🚀 Starting API server..."
cd api
python -m venv venv 2>/dev/null || true

# Activate virtual environment (cross-platform)
if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

pip install -r requirements.txt
python main.py &
API_PID=$!

# Start frontend
echo "⚛️ Starting frontend..."
cd ../frontend
npm install
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Development servers started!"
echo "🌐 Frontend: http://localhost:3001"
echo "🔌 API: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for interrupt
trap "kill $API_PID $FRONTEND_PID; exit" INT
wait
EOF

chmod +x scripts/start-frontend.sh

echo ""
echo "✅ Frontend integration setup complete!"
echo ""
echo "📁 New structure added to your repo:"
echo "   nfl-betting-analytics/"
echo "   ├── config/              # ✅ Your existing"
echo "   ├── data/               # ✅ Your existing"
echo "   ├── output/             # ✅ Your existing"  
echo "   ├── scripts/            # ✅ Your existing + new frontend script"
echo "   ├── src/                # ✅ Your existing"
echo "   ├── tests/              # ✅ Your existing"
echo "   ├── api/                # 🆕 NEW - FastAPI backend"
echo "   ├── frontend/           # 🆕 NEW - React dashboard"
echo "   └── docker-compose.yml  # 🆕 NEW - Full stack deployment"
echo ""
echo "🚀 Next steps:"
echo "1. Copy the dashboard component to frontend/pages/index.js"
echo "2. Run: ./scripts/start-frontend.sh"
echo "3. Visit: http://localhost:3001"
echo "4. Test API: http://localhost:8000/docs"
echo ""
echo "💡 The API will use your existing player_bridge_framework.py!"
echo "   It tries CSV files first (fast), then live analysis (complete)"
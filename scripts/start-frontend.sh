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

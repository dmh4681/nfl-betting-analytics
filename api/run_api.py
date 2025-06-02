#!/usr/bin/env python3
"""
Simple script to run the NFL Analytics API
Save this as run_api.py in your api/ directory
"""

import uvicorn
import sys
from pathlib import Path

def main():
    print("🏈 Starting NFL Offseason Intelligence Hub API...")
    print("=" * 50)
    
    # Get current directory
    current_dir = Path(__file__).parent
    print(f"📁 Running from: {current_dir}")
    
    # Run the API
    try:
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 API stopped by user")
    except Exception as e:
        print(f"❌ Error starting API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
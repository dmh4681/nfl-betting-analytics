"""
Data Inspector - Check what's actually in our CSV file
"""

import pandas as pd
from pathlib import Path

def inspect_csv_data():
    """Inspect the current CSV data to see what we actually have"""
    
    project_root = Path(__file__).parent.parent.parent
    csv_path = project_root / "data" / "current_season" / "nfl_2024_games.csv"
    
    print("🔍 Inspecting CSV Data")
    print("=" * 40)
    
    if not csv_path.exists():
        print(f"❌ File not found: {csv_path}")
        return
        
    df = pd.read_csv(csv_path)
    
    print(f"📊 Total rows: {len(df)}")
    print(f"📅 Columns: {list(df.columns)}")
    
    # Check date ranges
    if 'game_date' in df.columns:
        df['game_date'] = pd.to_datetime(df['game_date'])
        print(f"🗓️  Date range: {df['game_date'].min()} to {df['game_date'].max()}")
        
    # Check weeks
    if 'week' in df.columns:
        weeks = sorted(df['week'].unique())
        print(f"🏈 Weeks available: {weeks}")
        
    # Check final weeks specifically
    if 'week' in df.columns:
        final_weeks = df[df['week'].isin([15, 16, 17, 18])]
        print(f"🎯 Games in final weeks (15-18): {len(final_weeks)}")
        
        if len(final_weeks) > 0:
            print("\n📋 Sample final week games:")
            sample_cols = ['week', 'game_date', 'away_team', 'home_team', 'spread']
            display_cols = [col for col in sample_cols if col in final_weeks.columns]
            print(final_weeks[display_cols].head(10).to_string(index=False))
    
    # Check if Eagles are in Super Bowl
    if 'away_team' in df.columns and 'home_team' in df.columns:
        eagles_games = df[(df['away_team'] == 'PHI') | (df['home_team'] == 'PHI')]
        print(f"\n🦅 Eagles games found: {len(eagles_games)}")
        
        # Look for Super Bowl (usually week 22 or in playoffs)
        if 'week' in df.columns:
            eagles_playoffs = eagles_games[eagles_games['week'] > 18]
            if len(eagles_playoffs) > 0:
                print(f"🏆 Eagles playoff games: {len(eagles_playoffs)}")
                print(eagles_playoffs[['week', 'away_team', 'home_team']].to_string(index=False))
            else:
                print("❌ No Eagles playoff games found - this might be regular season only data")
                
        # Check Eagles' final regular season games
        eagles_final = eagles_games[eagles_games['week'].isin([17, 18])] if 'week' in df.columns else pd.DataFrame()
        if len(eagles_final) > 0:
            print(f"\n🦅 Eagles final regular season games:")
            final_cols = ['week', 'away_team', 'home_team', 'spread', 'home_score', 'away_score']
            display_cols = [col for col in final_cols if col in eagles_final.columns]
            print(eagles_final[display_cols].to_string(index=False))

if __name__ == "__main__":
    inspect_csv_data()
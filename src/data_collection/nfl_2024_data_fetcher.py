"""
NFL 2024 Data Fetcher - Get current season data from multiple sources
"""

import pandas as pd
import requests
import json
import time
from pathlib import Path
from datetime import datetime
import logging
from typing import Dict, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFL2024DataFetcher:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.output_path = self.project_root / "data" / "current_season"
        self.output_path.mkdir(parents=True, exist_ok=True)
        
    def fetch_nflverse_data(self):
        """Fetch 2024 NFL game data from NFLverse GitHub repository"""
        logger.info("Fetching 2024 NFL data from NFLverse...")
        
        # NFLverse schedules endpoint - should have 2024 data
        schedules_url = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
        
        try:
            logger.info("Downloading games data...")
            df = pd.read_csv(schedules_url)
            
            # Filter for 2024 season (the one that just ended in Feb 2025)
            df_2024 = df[df['season'] == 2024].copy()
            
            if len(df_2024) == 0:
                logger.warning("No 2024 season data found, trying alternative...")
                # Try 2025 in case the dataset uses different labeling
                df_2024 = df[df['season'] == 2025].copy()
                
            if len(df_2024) == 0:
                logger.warning("No current season data found in NFLverse dataset")
                # Show available seasons for debugging
                available_seasons = sorted(df['season'].unique()) if 'season' in df.columns else []
                logger.info(f"Available seasons: {available_seasons}")
                return None
                
            logger.info(f"Found {len(df_2024)} games from the season that ended with Eagles Super Bowl win")
            
            # Clean and standardize the data
            df_2024 = self._clean_nflverse_data(df_2024)
            
            # Save to CSV
            output_file = self.output_path / "nfl_2024_games.csv"
            df_2024.to_csv(output_file, index=False)
            logger.info(f"Saved 2024 NFL data to {output_file}")
            
            return df_2024
            
        except Exception as e:
            logger.error(f"Error fetching NFLverse data: {e}")
            return None
            
    def _clean_nflverse_data(self, df):
        """Clean and standardize NFLverse data for our analysis"""
        
        # Rename columns to match our expected format
        column_mapping = {
            'home_team': 'home_team',
            'away_team': 'away_team', 
            'week': 'week',
            'gameday': 'game_date',
            'spread_line': 'spread',
            'total_line': 'total',
            'home_score': 'home_score',
            'away_score': 'away_score',
            'result': 'spread_result'
        }
        
        # Keep only columns we need
        available_cols = [col for col in column_mapping.keys() if col in df.columns]
        df_clean = df[available_cols].copy()
        
        # Rename columns
        df_clean = df_clean.rename(columns={k: v for k, v in column_mapping.items() if k in available_cols})
        
        # Add derived columns
        if 'home_score' in df_clean.columns and 'away_score' in df_clean.columns:
            df_clean['total_score'] = df_clean['home_score'] + df_clean['away_score']
            df_clean['home_win'] = (df_clean['home_score'] > df_clean['away_score']).astype(int)
        
        # Filter for regular season games (weeks 1-18)
        if 'week' in df_clean.columns:
            df_clean = df_clean[df_clean['week'].between(1, 18)].copy()
            
        # Only keep games with spread data
        if 'spread' in df_clean.columns:
            df_clean = df_clean.dropna(subset=['spread'])
            
        return df_clean
        
    def fetch_alternative_data(self):
        """Backup method: fetch from alternative sources"""
        logger.info("Trying alternative data sources...")
        
        # Try ESPN API (public endpoints)
        try:
            espn_url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
            response = requests.get(espn_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                logger.info("Successfully fetched ESPN data")
                return self._parse_espn_data(data)
                
        except Exception as e:
            logger.warning(f"ESPN API failed: {e}")
            
        return None
        
    def _parse_espn_data(self, espn_data):
        """Parse ESPN API response into our format"""
        games = []
        
        if 'events' in espn_data:
            for event in espn_data['events']:
                try:
                    game = {
                        'game_date': event['date'],
                        'home_team': event['competitions'][0]['competitors'][0]['team']['abbreviation'],
                        'away_team': event['competitions'][0]['competitors'][1]['team']['abbreviation'],
                        'week': event.get('week', {}).get('number', 0),
                        'season': 2024
                    }
                    
                    # Get scores if available
                    competitors = event['competitions'][0]['competitors']
                    if len(competitors) >= 2:
                        game['home_score'] = competitors[0].get('score', None)
                        game['away_score'] = competitors[1].get('score', None)
                    
                    games.append(game)
                    
                except Exception as e:
                    logger.warning(f"Error parsing game: {e}")
                    continue
                    
        return pd.DataFrame(games) if games else None
        
    def create_2024_dataset(self):
        """Main method to create comprehensive 2024 dataset"""
        print("🏈 NFL 2024 Data Fetcher")
        print("=" * 40)
        
        # Try primary source first
        df_2024 = self.fetch_nflverse_data()
        
        if df_2024 is None or len(df_2024) == 0:
            print("❌ Primary source failed, trying alternatives...")
            df_2024 = self.fetch_alternative_data()
            
        if df_2024 is not None and len(df_2024) > 0:
            print(f"✅ Successfully fetched {len(df_2024)} games from 2024 season")
            
            # Show summary
            self._show_data_summary(df_2024)
            
            return df_2024
        else:
            print("❌ Could not fetch 2024 NFL data from any source")
            print("\n💡 Recommendations:")
            print("1. Check if The Odds API has 2024 data (requires API key)")
            print("2. Try the Kaggle dataset: https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data")
            print("3. Manually collect a few weeks of data from ESPN or similar sites")
            return None
            
    def _show_data_summary(self, df):
        """Show summary of fetched data"""
        print(f"\n📊 Data Summary:")
        print(f"  Total games: {len(df)}")
        
        if 'week' in df.columns:
            weeks_available = sorted(df['week'].unique())
            print(f"  Weeks available: {min(weeks_available)} - {max(weeks_available)}")
            
        if 'spread' in df.columns:
            games_with_spreads = df['spread'].notna().sum()
            print(f"  Games with betting lines: {games_with_spreads}")
            
        if 'home_score' in df.columns:
            completed_games = df['home_score'].notna().sum()
            print(f"  Completed games: {completed_games}")
            
        print(f"\n🏆 Sample games:")
        sample_cols = ['week', 'away_team', 'home_team', 'spread']
        display_cols = [col for col in sample_cols if col in df.columns]
        print(df[display_cols].head().to_string(index=False))


def main():
    fetcher = NFL2024DataFetcher()
    data = fetcher.create_2024_dataset()
    
    if data is not None:
        print(f"\n✅ Ready to run power rankings analysis!")
        print(f"💾 Data saved to: {fetcher.output_path}")
    

if __name__ == "__main__":
    main()
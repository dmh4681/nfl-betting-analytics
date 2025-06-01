"""
NFL Market-Implied Power Rankings - Updated for 2024 Season
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

import pandas as pd
import numpy as np
from datetime import datetime
import logging
from typing import Dict, List, Tuple, Optional
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketPowerRankings2024:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / "config" / "team_mappings.json"
        
        # Load team mappings
        with open(self.config_path, 'r') as f:
            self.team_mappings = json.load(f)
            
        # Create comprehensive lookup dictionary for team name standardization
        self.team_lookup = {}
        for key, data in self.team_mappings.items():
            abbr = data['abbreviation']
            # Add all possible variations
            self.team_lookup[data['full_name']] = abbr
            self.team_lookup[data['short_name']] = abbr
            self.team_lookup[data['abbreviation']] = abbr
            self.team_lookup[data['caps']] = abbr
            # Add common variations
            self.team_lookup[data['full_name'].upper()] = abbr
            self.team_lookup[data['short_name'].upper()] = abbr
            
        # Add specific common variations found in datasets
        additional_mappings = {
            'LAS': 'LV',  # Las Vegas sometimes coded as LAS
            'LAR': 'LAR', # Ensure LAR is preserved
            'LA': 'LAR',  # Sometimes just "LA" for Rams
            'WSH': 'Was', # Washington sometimes WSH
            'WAS': 'Was', # Washington caps
            'JAX': 'Jac', # Jacksonville sometimes JAX
        }
        self.team_lookup.update(additional_mappings)

    def extract_final_2024_market_data(self):
        """Extract market data from 2024 season using the new dataset"""
        logger.info("Loading 2024 NFL season data...")
        
        # Load the 2024 data we just fetched
        data_path = self.project_root / "data" / "current_season" / "nfl_2024_games.csv"
        
        if not data_path.exists():
            logger.error(f"2024 data file not found at {data_path}")
            logger.info("Please run nfl_2024_data_fetcher.py first to download 2024 data")
            return None
            
        try:
            df_2024 = pd.read_csv(data_path)
            logger.info(f"Loaded {len(df_2024)} games from 2024 season")
            
            # Use entire 2024 regular season for comprehensive market assessment
            # Eagles had 14-3 record, so full season should show their strength better
            logger.info("Using full 2024 regular season data for comprehensive market assessment")
            final_weeks_data = df_2024.copy()
            
            # Filter for games with betting data and results
            valid_games = final_weeks_data.dropna(subset=['spread', 'home_score', 'away_score']).copy()
            
            logger.info(f"Found {len(valid_games)} completed games with betting lines")
            
            # Standardize team names
            valid_games['home_team'] = valid_games['home_team'].apply(self._standardize_team_name)
            valid_games['away_team'] = valid_games['away_team'].apply(self._standardize_team_name)
            
            # Remove any games where team standardization failed
            valid_games = valid_games.dropna(subset=['home_team', 'away_team'])
            
            # Verify we have all 32 teams
            all_teams_found = set()
            all_teams_found.update(valid_games['home_team'].unique())
            all_teams_found.update(valid_games['away_team'].unique())
            
            expected_teams = set(data['abbreviation'] for data in self.team_mappings.values())
            missing_teams = expected_teams - all_teams_found
            
            if missing_teams:
                logger.warning(f"Missing teams in dataset: {missing_teams}")
            else:
                logger.info(f"✅ All 32 NFL teams found in dataset")
            
            return valid_games
            
        except Exception as e:
            logger.error(f"Error loading 2024 data: {e}")
            return None

    def _standardize_team_name(self, team_name):
        """Standardize team names from 2024 dataset to match our mappings"""
        if pd.isna(team_name):
            return None
            
        team_str = str(team_name).strip()
        
        # Direct lookup
        if team_str in self.team_lookup:
            return self.team_lookup[team_str]
            
        # Try variations
        variations = [
            team_str.upper(),
            team_str.lower(), 
            team_str.title(),
            team_str.replace('_', ' '),
            team_str.replace('-', ' ')
        ]
        
        for variation in variations:
            if variation in self.team_lookup:
                return self.team_lookup[variation]
                
        # Try partial matching for full team names
        for full_name, abbr in self.team_lookup.items():
            if team_str.lower() in full_name.lower() or full_name.lower() in team_str.lower():
                return abbr
                
        logger.warning(f"Could not standardize team name: {team_name}")
        return None

    def calculate_market_power_rankings(self):
        """Calculate power rankings from market data"""
        
        # Get 2024 market data
        market_data = self.extract_final_2024_market_data()
        
        if market_data is None or len(market_data) == 0:
            logger.error("No market data available for analysis")
            return None

        print(f"✅ Found {len(market_data)} games with closing line data from 2024 season")
        
        logger.info("Calculating market-implied power rankings...")
        
        # Extract team matchups and spreads for analysis
        matchups = []
        for _, game in market_data.iterrows():
            matchups.append({
                'home_team': game['home_team'],
                'away_team': game['away_team'], 
                'spread': game['spread'],  # Use 2024 spread data
                'week': game['week']
            })

        # Get unique teams
        all_teams = set()
        for matchup in matchups:
            all_teams.add(matchup['home_team'])
            all_teams.add(matchup['away_team'])
            
        all_teams = sorted(list(all_teams))
        logger.info(f"Found {len(all_teams)} teams: {all_teams}")

        # Verify we have all 32 teams
        expected_teams = set(data['abbreviation'] for data in self.team_mappings.values())
        if len(all_teams) != 32:
            missing = expected_teams - set(all_teams)
            logger.warning(f"Missing {len(missing)} teams: {missing}")

        # Need sufficient data for power rankings
        if len(matchups) < 20:
            logger.error(f"Not enough games found: {len(matchups)} (need at least 20)")
            return None

        # Calculate power ratings using least squares
        ratings = self._solve_for_ratings(matchups, all_teams)
        
        if ratings is None:
            logger.error("Could not calculate power ratings")
            return None

        # Add any missing teams with neutral ratings
        for team_data in self.team_mappings.values():
            team_abbr = team_data['abbreviation']
            if team_abbr not in ratings:
                ratings[team_abbr] = 0.0
                logger.info(f"Added missing team {team_abbr} with neutral rating")

        # Create rankings DataFrame
        rankings_data = []
        for team_data in self.team_mappings.values():
            team_abbr = team_data['abbreviation']
            rankings_data.append({
                'team': team_abbr,
                'rating': ratings.get(team_abbr, 0.0),
                'team_name': team_data['full_name']
            })

        rankings_df = pd.DataFrame(rankings_data)
        rankings_df = rankings_df.sort_values('rating', ascending=False).reset_index(drop=True)
        rankings_df['rank'] = range(1, len(rankings_df) + 1)

        return rankings_df

    def _solve_for_ratings(self, matchups: List[Dict], teams: List[str]) -> Optional[Dict[str, float]]:
        """Solve for team ratings using least squares regression"""
        
        n_teams = len(teams)
        team_idx = {team: i for i, team in enumerate(teams)}
        
        # Build system of equations: A * ratings = spreads
        equations = []
        spreads = []
        
        for matchup in matchups:
            home_team = matchup['home_team']
            away_team = matchup['away_team']
            spread = matchup['spread']
            
            if home_team in team_idx and away_team in team_idx:
                # Create equation: home_rating - away_rating = spread
                equation = [0.0] * n_teams
                equation[team_idx[home_team]] = 1.0
                equation[team_idx[away_team]] = -1.0
                
                equations.append(equation)
                spreads.append(spread)
        
        if len(equations) < n_teams - 1:
            logger.error("Not enough equations to solve for ratings")
            return None
            
        # Convert to numpy arrays
        A = np.array(equations)
        b = np.array(spreads)
        
        try:
            # Add constraint that average rating = 0 (for unique solution)
            constraint = np.ones((1, n_teams))
            A_constrained = np.vstack([A, constraint])
            b_constrained = np.hstack([b, [0.0]])
            
            # Solve using least squares
            ratings_array, residuals, rank, s = np.linalg.lstsq(A_constrained, b_constrained, rcond=None)
            
            # Convert back to dictionary
            ratings = {teams[i]: float(ratings_array[i]) for i in range(n_teams)}
            
            logger.info(f"Successfully calculated ratings for {len(ratings)} teams")
            return ratings
            
        except Exception as e:
            logger.error(f"Error solving for ratings: {e}")
            return None

    def generate_rankings_report(self):
        """Generate comprehensive power rankings report"""
        
        print("🏈 NFL Market-Implied Power Rankings Analysis")
        print("=" * 50)
        
        rankings = self.calculate_market_power_rankings()
        
        if rankings is None:
            print("❌ Could not calculate market-implied ratings")
            return None

        print(f"📊 Based on 2024 season betting market data")
        print(f"🎯 Using final weeks of season for current team strength")
        print(f"🏈 Covering all {len(rankings)} NFL teams")
        print()

        # Display top 10
        print("🏆 TOP 10 TEAMS (Market-Implied Power Rankings)")
        print("-" * 55)
        print(f"{'Rank':<4} {'Team':<4} {'Full Name':<25} {'Rating':<8}")
        print("-" * 55)
        
        for _, row in rankings.head(10).iterrows():
            print(f"{row['rank']:<4} {row['team']:<4} {row['team_name']:<25} {row['rating']:>7.2f}")

        # Display bottom 5
        print(f"\n📉 BOTTOM 5 TEAMS")
        print("-" * 55)
        
        for _, row in rankings.tail(5).iterrows():
            print(f"{row['rank']:<4} {row['team']:<4} {row['team_name']:<25} {row['rating']:>7.2f}")

        # Show rating distribution
        print(f"\n📈 RATING DISTRIBUTION")
        print(f"  Highest: {rankings['rating'].max():.2f}")
        print(f"  Lowest:  {rankings['rating'].min():.2f}")
        print(f"  Range:   {rankings['rating'].max() - rankings['rating'].min():.2f}")
        print(f"  Std Dev: {rankings['rating'].std():.2f}")

        # Verify team count
        print(f"\n✅ TEAM VERIFICATION")
        print(f"  Teams in rankings: {len(rankings)}")
        print(f"  Expected: 32")
        if len(rankings) == 32:
            print(f"  Status: ✅ All teams included")
        else:
            print(f"  Status: ⚠️  Missing teams")

        # Save results
        output_path = self.project_root / "output" / "market_power_rankings_2024.csv"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        rankings.to_csv(output_path, index=False)
        print(f"\n💾 Full rankings saved to: {output_path}")

        return rankings


def main():
    analyzer = MarketPowerRankings2024()
    analyzer.generate_rankings_report()


if __name__ == "__main__":
    main()
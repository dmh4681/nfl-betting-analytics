"""
NFL Playoff-Adjusted Power Rankings - True End of Season Rankings
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json

class PlayoffAdjustedRankings:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        
    def create_playoff_adjusted_rankings(self):
        """Create power rankings that include playoff performance"""
        
        print("🏈 NFL Playoff-Adjusted Power Rankings")
        print("=" * 50)
        print("🏆 Including playoff performance for TRUE end-of-season ranking")
        print()
        
        # Playoff betting data from our search
        playoff_games = [
            # Wild Card Round
            {'week': 'WC', 'away_team': 'GB', 'home_team': 'PHI', 'spread': -4.5, 'result': 'PHI', 'margin': 12},
            {'week': 'WC', 'away_team': 'WAS', 'home_team': 'TB', 'spread': -3.0, 'result': 'WAS', 'margin': 3},
            {'week': 'WC', 'away_team': 'DEN', 'home_team': 'BUF', 'spread': -9.5, 'result': 'BUF', 'margin': 21},
            {'week': 'WC', 'away_team': 'PIT', 'home_team': 'BAL', 'spread': -9.5, 'result': 'BAL', 'margin': 11},
            
            # Divisional Round  
            {'week': 'DIV', 'away_team': 'LAR', 'home_team': 'PHI', 'spread': -6.5, 'result': 'PHI', 'margin': 6},
            {'week': 'DIV', 'away_team': 'WAS', 'home_team': 'DET', 'spread': -8.5, 'result': 'WAS', 'margin': 14},
            {'week': 'DIV', 'away_team': 'BAL', 'home_team': 'BUF', 'spread': -1.5, 'result': 'BUF', 'margin': 2},
            {'week': 'DIV', 'away_team': 'HOU', 'home_team': 'KC', 'spread': -8.5, 'result': 'KC', 'margin': 9},
            
            # Conference Championships
            {'week': 'CC', 'away_team': 'WAS', 'home_team': 'PHI', 'spread': -6.0, 'result': 'PHI', 'margin': 32},
            {'week': 'CC', 'away_team': 'BUF', 'home_team': 'KC', 'spread': -2.0, 'result': 'KC', 'margin': 3},
            
            # Super Bowl
            {'week': 'SB', 'away_team': 'PHI', 'home_team': 'KC', 'spread': -1.5, 'result': 'PHI', 'margin': 18}
        ]
        
        # Calculate playoff performance scores
        playoff_scores = self._calculate_playoff_scores(playoff_games)
        
        # Load regular season rankings (from your existing analysis)
        regular_season_ratings = {
            'BAL': 6.05, 'DET': 6.03, 'BUF': 4.52, 'KC': 4.21, 'GB': 3.59,
            'SF': 3.21, 'MIN': 2.76, 'PHI': 2.71, 'CIN': 2.27, 'HOU': 2.07,
            'NYJ': 1.32, 'LAC': 0.96, 'MIA': 0.79, 'TB': 0.78, 'SEA': 0.56,
            'ARI': 0.35, 'WAS': 0.26, 'ATL': 0.26, 'PIT': 0.11, 'DEN': -0.29,
            'IND': -1.07, 'CHI': -2.15, 'TEN': -2.54, 'JAC': -2.63, 'DAL': -3.15,
            'CLE': -3.77, 'NO': -4.37, 'LV': -4.68, 'NE': -5.29, 'NYG': -5.31, 'CAR': -7.53
        }
        
        # Combine regular season and playoff performance
        final_ratings = {}
        for team in regular_season_ratings:
            base_rating = regular_season_ratings[team]
            playoff_bonus = playoff_scores.get(team, 0)
            final_ratings[team] = base_rating + playoff_bonus
            
        # Create final rankings
        rankings_data = []
        for team, rating in final_ratings.items():
            rankings_data.append({
                'team': team,
                'rating': rating,
                'regular_season': regular_season_ratings[team],
                'playoff_adjustment': playoff_scores.get(team, 0),
                'team_name': self._get_team_name(team)
            })
            
        df = pd.DataFrame(rankings_data)
        df = df.sort_values('rating', ascending=False).reset_index(drop=True)
        df['rank'] = range(1, len(df) + 1)
        
        return df, playoff_games
        
    def _calculate_playoff_scores(self, playoff_games):
        """Calculate playoff performance scores based on results vs spreads"""
        scores = {}
        
        # Multipliers for different rounds (reduced by ~60%)
        round_multipliers = {
            'WC': 0.4,    # Wild Card (was 1.0)
            'DIV': 0.6,   # Divisional (was 1.5)
            'CC': 0.8,    # Conference Championship (was 2.0)
            'SB': 1.2     # Super Bowl (was 3.0)
        }
        
        for game in playoff_games:
            week = game['week']
            home_team = game['home_team']
            away_team = game['away_team']
            spread = game['spread']
            winner = game['result']
            margin = game['margin']
            
            multiplier = round_multipliers[week]
            
            # Calculate performance vs spread (more conservative scoring)
            if winner == home_team:
                # Home team won
                beat_spread_by = margin - abs(spread)
                home_bonus = max(0, beat_spread_by / 15) * multiplier  # Divide by 15 instead of 10
                away_penalty = min(0, beat_spread_by / 15) * multiplier
                
                scores[home_team] = scores.get(home_team, 0) + home_bonus
                scores[away_team] = scores.get(away_team, 0) + away_penalty
            else:
                # Away team won (upset)
                beat_spread_by = margin + spread  # Away team getting points
                away_bonus = (beat_spread_by / 15 + 0.5) * multiplier  # Reduced from 1.0 to 0.5 upset bonus
                home_penalty = -(margin / 15) * multiplier
                
                scores[away_team] = scores.get(away_team, 0) + away_bonus
                scores[home_team] = scores.get(home_team, 0) + home_penalty
                
        return scores
        
    def _get_team_name(self, abbr):
        """Get full team name"""
        team_names = {
            'PHI': 'Philadelphia Eagles', 'KC': 'Kansas City Chiefs', 
            'BUF': 'Buffalo Bills', 'WAS': 'Washington Commanders',
            'BAL': 'Baltimore Ravens', 'DET': 'Detroit Lions',
            'HOU': 'Houston Texans', 'LAR': 'Los Angeles Rams',
            'GB': 'Green Bay Packers', 'TB': 'Tampa Bay Buccaneers',
            'PIT': 'Pittsburgh Steelers', 'DEN': 'Denver Broncos',
            'MIN': 'Minnesota Vikings', 'SF': 'San Francisco 49ers',
            'CIN': 'Cincinnati Bengals', 'NYJ': 'New York Jets',
            'LAC': 'Los Angeles Chargers', 'MIA': 'Miami Dolphins',
            'SEA': 'Seattle Seahawks', 'ARI': 'Arizona Cardinals',
            'ATL': 'Atlanta Falcons', 'IND': 'Indianapolis Colts',
            'CHI': 'Chicago Bears', 'TEN': 'Tennessee Titans',
            'JAC': 'Jacksonville Jaguars', 'DAL': 'Dallas Cowboys',
            'CLE': 'Cleveland Browns', 'NO': 'New Orleans Saints',
            'LV': 'Las Vegas Raiders', 'NE': 'New England Patriots',
            'NYG': 'New York Giants', 'CAR': 'Carolina Panthers'
        }
        return team_names.get(abbr, abbr)
        
    def display_results(self):
        """Display the playoff-adjusted rankings"""
        df, playoff_games = self.create_playoff_adjusted_rankings()
        
        print("🏆 TOP 10 TEAMS (Playoff-Adjusted Rankings)")
        print("-" * 70)
        print(f"{'Rank':<4} {'Team':<4} {'Full Name':<25} {'Final':<7} {'RegSeason':<9} {'Playoff':<7}")
        print("-" * 70)
        
        for _, row in df.head(10).iterrows():
            playoff_adj = f"+{row['playoff_adjustment']:.1f}" if row['playoff_adjustment'] > 0 else f"{row['playoff_adjustment']:.1f}"
            print(f"{row['rank']:<4} {row['team']:<4} {row['team_name']:<25} {row['rating']:>6.1f} {row['regular_season']:>8.1f} {playoff_adj:>6}")
            
        print(f"\n📈 BIGGEST PLAYOFF RISERS")
        print("-" * 50)
        playoff_risers = df[df['playoff_adjustment'] > 0].nlargest(5, 'playoff_adjustment')
        for _, row in playoff_risers.iterrows():
            old_rank = self._estimate_old_rank(row['regular_season'])
            print(f"{row['team']}: #{old_rank} → #{row['rank']} (+{row['playoff_adjustment']:.1f})")
            
        print(f"\n📉 PLAYOFF DISAPPOINTMENTS")  
        print("-" * 50)
        playoff_droppers = df[df['playoff_adjustment'] < 0].nsmallest(5, 'playoff_adjustment')
        for _, row in playoff_droppers.iterrows():
            old_rank = self._estimate_old_rank(row['regular_season'])
            print(f"{row['team']}: #{old_rank} → #{row['rank']} ({row['playoff_adjustment']:.1f})")
            
        print(f"\n🦅 EAGLES ANALYSIS")
        print("-" * 30)
        eagles_row = df[df['team'] == 'PHI'].iloc[0]
        print(f"Regular Season Rank: ~#{self._estimate_old_rank(eagles_row['regular_season'])}")
        print(f"Final Rank: #{eagles_row['rank']}")
        print(f"Playoff Boost: +{eagles_row['playoff_adjustment']:.1f}")
        print(f"Championships DO matter! 🏆")
        
        return df
        
    def _estimate_old_rank(self, rating):
        """Estimate what rank this rating would have been in regular season"""
        # Based on your regular season rankings
        if rating > 6.0: return 1
        elif rating > 4.5: return 4  
        elif rating > 3.5: return 6
        elif rating > 2.5: return 8
        elif rating > 1.0: return 12
        elif rating > 0: return 16
        elif rating > -2: return 20
        elif rating > -4: return 25
        else: return 30


def main():
    analyzer = PlayoffAdjustedRankings()
    rankings = analyzer.display_results()
    
    # Save results
    output_path = Path(__file__).parent.parent.parent / "output" / "playoff_adjusted_rankings.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    rankings.to_csv(output_path, index=False)
    print(f"\n💾 Complete rankings saved to: {output_path}")


if __name__ == "__main__":
    main()
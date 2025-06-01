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
        self.config_path = self.project_root / "config" / "team_mappings.json"
        
        # Load team mappings
        with open(self.config_path, 'r') as f:
            self.team_mappings = json.load(f)
            
        # Create team name lookup from mappings
        self.team_names = {}
        for key, data in self.team_mappings.items():
            self.team_names[data['abbreviation']] = data['full_name']
        
    def create_playoff_adjusted_rankings(self):
        """Create power rankings that include playoff performance"""
        
        print("🏈 NFL Playoff-Adjusted Power Rankings")
        print("=" * 50)
        print("🏆 Including playoff performance for TRUE end-of-season ranking")
        print()
        
        # Playoff betting data from our search
        playoff_games = [
            # Wild Card Round
            {'week': 'WC', 'away_team': 'GB', 'home_team': 'Phi', 'spread': -4.5, 'result': 'Phi', 'margin': 12},
            {'week': 'WC', 'away_team': 'Was', 'home_team': 'TB', 'spread': -3.0, 'result': 'Was', 'margin': 3},
            {'week': 'WC', 'away_team': 'Den', 'home_team': 'Buf', 'spread': -9.5, 'result': 'Buf', 'margin': 21},
            {'week': 'WC', 'away_team': 'Pit', 'home_team': 'Bal', 'spread': -9.5, 'result': 'Bal', 'margin': 11},
            
            # Divisional Round  
            {'week': 'DIV', 'away_team': 'LAR', 'home_team': 'Phi', 'spread': -6.5, 'result': 'Phi', 'margin': 6},
            {'week': 'DIV', 'away_team': 'Was', 'home_team': 'Det', 'spread': -8.5, 'result': 'Was', 'margin': 14},
            {'week': 'DIV', 'away_team': 'Bal', 'home_team': 'Buf', 'spread': -1.5, 'result': 'Buf', 'margin': 2},
            {'week': 'DIV', 'away_team': 'Hou', 'home_team': 'KC', 'spread': -8.5, 'result': 'KC', 'margin': 9},
            
            # Conference Championships
            {'week': 'CC', 'away_team': 'Was', 'home_team': 'Phi', 'spread': -6.0, 'result': 'Phi', 'margin': 32},
            {'week': 'CC', 'away_team': 'Buf', 'home_team': 'KC', 'spread': -2.0, 'result': 'KC', 'margin': 3},
            
            # Super Bowl
            {'week': 'SB', 'away_team': 'Phi', 'home_team': 'KC', 'spread': -1.5, 'result': 'Phi', 'margin': 18}
        ]
        
        # Calculate playoff performance scores
        playoff_scores = self._calculate_playoff_scores(playoff_games)
        
        # Load regular season ratings using team_mappings.json format
        regular_season_ratings = {
            'Bal': 6.05, 'Det': 6.03, 'Buf': 4.52, 'KC': 4.21, 'GB': 3.59,
            'SF': 3.21, 'Min': 2.76, 'Phi': 2.71, 'Cin': 2.27, 'Hou': 2.07,
            'NYJ': 1.32, 'LAC': 0.96, 'Mia': 0.79, 'TB': 0.78, 'Sea': 0.56,
            'Ari': 0.35, 'Was': 0.26, 'Atl': 0.26, 'Pit': 0.11, 'Den': -0.29,
            'Ind': -1.07, 'Chi': -2.15, 'Ten': -2.54, 'Jac': -2.63, 'Dal': -3.15,
            'Cle': -3.77, 'NO': -4.37, 'LV': -4.68, 'NE': -5.29, 'NYG': -5.31, 'Car': -7.53
        }
        
        # Ensure we have all 32 teams from team_mappings.json
        for team_data in self.team_mappings.values():
            team_abbr = team_data['abbreviation']
            if team_abbr not in regular_season_ratings:
                regular_season_ratings[team_abbr] = 0.0  # Neutral rating for missing teams
                print(f"⚠️  Added missing team {team_abbr} with neutral rating")
        
        # Combine regular season and playoff performance
        final_ratings = {}
        for team_abbr in regular_season_ratings:
            base_rating = regular_season_ratings[team_abbr]
            playoff_bonus = playoff_scores.get(team_abbr, 0)
            final_ratings[team_abbr] = base_rating + playoff_bonus
            
        # Create final rankings using all teams from mappings
        rankings_data = []
        for team_data in self.team_mappings.values():
            team_abbr = team_data['abbreviation']
            rankings_data.append({
                'team': team_abbr,
                'rating': final_ratings.get(team_abbr, 0.0),
                'regular_season': regular_season_ratings.get(team_abbr, 0.0),
                'playoff_adjustment': playoff_scores.get(team_abbr, 0),
                'team_name': team_data['full_name']
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
        eagles_row = df[df['team'] == 'Phi'].iloc[0]
        print(f"Regular Season Rank: ~#{self._estimate_old_rank(eagles_row['regular_season'])}")
        print(f"Final Rank: #{eagles_row['rank']}")
        print(f"Playoff Boost: +{eagles_row['playoff_adjustment']:.1f}")
        print(f"Championships DO matter! 🏆")
        
        # Verify team count
        print(f"\n✅ TEAM VERIFICATION")
        print(f"  Teams in rankings: {len(df)}")
        print(f"  Expected: 32")
        if len(df) == 32:
            print(f"  Status: ✅ All teams included")
        else:
            print(f"  Status: ⚠️  Missing teams")
        
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
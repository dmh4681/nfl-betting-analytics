"""
NFL Offseason Movement Tracker
Track free agency, trades, draft picks, and coaching changes
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
import requests
from datetime import datetime
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OffseasonTracker:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / "config" / "team_mappings.json"
        self.output_path = self.project_root / "data" / "current_season"
        
        # Load team mappings
        with open(self.config_path, 'r') as f:
            import json
            self.team_mappings = json.load(f)
            
    def create_offseason_tracker(self):
        """Create comprehensive offseason movement tracker"""
        
        # Free Agency Tracker
        fa_columns = [
            'Date', 'Player_Name', 'Position', 'Age', 'From_Team', 'To_Team',
            'Contract_Years', 'Contract_Value', 'AAV', 'Guaranteed', 'Previous_Stats',
            'Impact_Rating', 'Notes'
        ]
        
        # Draft Tracker  
        draft_columns = [
            'Round', 'Pick', 'Team', 'Player_Name', 'Position', 'College',
            'Age', 'Height', 'Weight', 'Projected_Impact', 'Need_Filled', 'Notes'
        ]
        
        # Coaching Changes
        coaching_columns = [
            'Team', 'Position', 'Previous_Coach', 'New_Coach', 'Date',
            'Experience', 'Previous_Success', 'System_Change', 'Impact_Rating', 'Notes'
        ]
        
        # Trade Tracker
        trade_columns = [
            'Date', 'Team_A', 'Team_B', 'Player_A', 'Player_B', 'Draft_Picks',
            'Trade_Value_A', 'Trade_Value_B', 'Winner', 'Notes'
        ]
        
        # Create DataFrames
        fa_df = pd.DataFrame(columns=fa_columns)
        draft_df = pd.DataFrame(columns=draft_columns)
        coaching_df = pd.DataFrame(columns=coaching_columns)
        trade_df = pd.DataFrame(columns=trade_columns)
        
        # Add sample data for reference
        sample_fa = {
            'Date': '2025-03-15', 'Player_Name': 'Example Player', 'Position': 'QB',
            'Age': 28, 'From_Team': 'Team A', 'To_Team': 'Team B',
            'Contract_Years': 3, 'Contract_Value': 75000000, 'AAV': 25000000,
            'Guaranteed': 45000000, 'Previous_Stats': '4200 yards, 28 TD',
            'Impact_Rating': 3.5, 'Notes': 'Major upgrade at QB position'
        }
        
        sample_coaching = {
            'Team': 'Example Team', 'Position': 'Head Coach', 
            'Previous_Coach': 'Old Coach', 'New_Coach': 'New Coach',
            'Date': '2025-01-15', 'Experience': '15 years', 
            'Previous_Success': 'Super Bowl winner', 'System_Change': 'Offensive minded',
            'Impact_Rating': 2.0, 'Notes': 'Defensive to offensive philosophy change'
        }
        
        fa_df.loc[0] = sample_fa
        coaching_df.loc[0] = sample_coaching
        
        return {
            'free_agency': fa_df,
            'draft': draft_df, 
            'coaching': coaching_df,
            'trades': trade_df
        }
        
    def create_impact_scoring_system(self):
        """Create system for scoring impact of moves"""
        
        position_values = {
            'QB': 5.0, 'RB': 2.0, 'WR': 3.0, 'TE': 2.5, 'OL': 2.8,
            'DL': 3.0, 'LB': 2.5, 'CB': 3.5, 'S': 2.8, 'K': 1.0, 'P': 1.0
        }
        
        age_multipliers = {
            range(22, 26): 1.2,  # Prime years
            range(26, 30): 1.0,  # Peak years  
            range(30, 33): 0.8,  # Declining
            range(33, 40): 0.5   # Veteran
        }
        
        contract_tiers = {
            'elite': (25000000, float('inf')),      # + per year
            'star': (15000000, 25000000),           # -25M per year
            'solid': (8000000, 15000000),           # -15M per year
            'depth': (2000000, 8000000),            # -8M per year
            'rookie': (0, 2000000)                  # Under  per year
        }
        
        return {
            'position_values': position_values,
            'age_multipliers': age_multipliers,
            'contract_tiers': contract_tiers
        }
        
    def calculate_team_net_movement(self, team_name: str, moves_data: Dict) -> Dict:
        """Calculate net gain/loss for a team across all moves"""
        
        team_impact = {
            'additions': [],
            'losses': [],
            'net_impact': 0,
            'position_changes': {}
        }
        
        # Process free agency
        fa_df = moves_data['free_agency']
        
        # Players gained
        gained = fa_df[fa_df['To_Team'] == team_name]
        for _, player in gained.iterrows():
            if pd.notna(player['Impact_Rating']):
                team_impact['additions'].append({
                    'player': player['Player_Name'],
                    'position': player['Position'],
                    'impact': player['Impact_Rating']
                })
                team_impact['net_impact'] += player['Impact_Rating']
                
        # Players lost
        lost = fa_df[fa_df['From_Team'] == team_name]
        for _, player in lost.iterrows():
            if pd.notna(player['Impact_Rating']):
                team_impact['losses'].append({
                    'player': player['Player_Name'],
                    'position': player['Position'],
                    'impact': -player['Impact_Rating']  # Negative for loss
                })
                team_impact['net_impact'] -= player['Impact_Rating']
                
        return team_impact
        
    def create_power_ranking_adjustments(self, base_ratings: Dict = None):
        """Create 2025 power ranking adjustments based on offseason moves"""
        
        if base_ratings is None:
            # Use generic starting ratings (can be updated with actual 2024 data)
            base_ratings = {team_data['full_name']: 0.0 for team_data in self.team_mappings.values()}
            
        adjustments = {}
        
        # Load offseason data
        tracker_data = self.create_offseason_tracker()
        
        for team_name in base_ratings.keys():
            net_movement = self.calculate_team_net_movement(team_name, tracker_data)
            
            adjustments[team_name] = {
                'base_rating': base_ratings[team_name],
                'offseason_adjustment': net_movement['net_impact'],
                'projected_2025_rating': base_ratings[team_name] + net_movement['net_impact'],
                'key_additions': [add['player'] for add in net_movement['additions'][:3]],
                'key_losses': [loss['player'] for loss in net_movement['losses'][:3]]
            }
            
        return adjustments
        
    def save_offseason_trackers(self):
        """Save all tracking sheets to Excel"""
        
        tracker_data = self.create_offseason_tracker()
        impact_system = self.create_impact_scoring_system()
        
        output_file = self.output_path / "NFL_2025_Offseason_Tracker.xlsx"
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Save tracking sheets
            tracker_data['free_agency'].to_excel(writer, sheet_name='Free Agency', index=False)
            tracker_data['draft'].to_excel(writer, sheet_name='Draft', index=False)
            tracker_data['coaching'].to_excel(writer, sheet_name='Coaching Changes', index=False)
            tracker_data['trades'].to_excel(writer, sheet_name='Trades', index=False)
            
            # Save impact scoring reference
            pos_values_df = pd.DataFrame(list(impact_system['position_values'].items()), 
                                       columns=['Position', 'Base_Value'])
            pos_values_df.to_excel(writer, sheet_name='Position Values', index=False)
            
        logger.info(f"Offseason tracker saved: {output_file}")
        return output_file
        
    def generate_offseason_report(self):
        """Generate comprehensive offseason tracking report"""
        
        print("🏈 NFL 2025 Offseason Movement Tracker")
        print("=" * 42)
        
        # Create tracking system
        tracker_file = self.save_offseason_trackers()
        print(f"✅ Tracker created: {tracker_file}")
        
        # Show impact scoring system
        impact_system = self.create_impact_scoring_system()
        print(f"\n📊 Impact Scoring System:")
        print(f"Position Values:")
        for pos, value in impact_system['position_values'].items():
            print(f"  {pos}: {value}")
            
        # Create sample power ranking adjustments
        print(f"\n🔄 Sample Power Ranking Bridge:")
        adjustments = self.create_power_ranking_adjustments()
        
        # Show a few example teams
        sample_teams = list(adjustments.keys())[:5]
        for team in sample_teams:
            adj = adjustments[team]
            print(f"  {team}: {adj['base_rating']:.1f} → {adj['projected_2025_rating']:.1f}")
            
        print(f"\n📋 Next Steps:")
        print(f"1. Start logging actual free agency moves in the tracker")
        print(f"2. Set up draft pick analysis after April draft")
        print(f"3. Build automated data collection from ESPN/NFL.com")
        print(f"4. Create weekly reports showing team trajectory changes")
        print(f"5. Validate impact scores against actual season performance")
        
        print(f"\n🎯 Ready to track the 2025 offseason!")
        
        return tracker_file


def main():
    tracker = OffseasonTracker()
    tracker.generate_offseason_report()


if __name__ == "__main__":
    main()

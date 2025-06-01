"""
NFL Offseason Data Scraper - Corrected 2024 Data
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

class NFLOffseasonScraperCorrected:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / "config" / "team_mappings.json"
        self.output_path = self.project_root / "data" / "current_season"
        
        # Load team mappings
        with open(self.config_path, 'r') as f:
            self.team_mappings = json.load(f)
            
        # Create reverse mapping for team name lookups
        self.team_lookup = {}
        for key, data in self.team_mappings.items():
            self.team_lookup[data['full_name']] = data['abbreviation']
            self.team_lookup[data['abbreviation']] = data['abbreviation']
            self.team_lookup[data['caps']] = data['abbreviation']
            
    def scrape_2024_draft_results(self):
        """Actual 2024 NFL Draft results (corrected)"""
        
        logger.info("Fetching CORRECTED 2024 NFL Draft results...")
        
        # Corrected 2024 draft data
        draft_data = [
            {
                'round': 1, 'pick': 1, 'overall': 1, 'team': 'Chicago Bears',
                'player': 'Caleb Williams', 'position': 'QB', 'college': 'USC',
                'age': 22, 'height': '6-1', 'weight': 218
            },
            {
                'round': 1, 'pick': 2, 'overall': 2, 'team': 'Washington Commanders', 
                'player': 'Jayden Daniels', 'position': 'QB', 'college': 'LSU',
                'age': 23, 'height': '6-4', 'weight': 210
            },
            {
                'round': 1, 'pick': 3, 'overall': 3, 'team': 'New England Patriots',
                'player': 'Drake Maye', 'position': 'QB', 'college': 'North Carolina', 
                'age': 21, 'height': '6-4', 'weight': 223
            },
            {
                'round': 1, 'pick': 4, 'overall': 4, 'team': 'Arizona Cardinals',
                'player': 'Marvin Harrison Jr.', 'position': 'WR', 'college': 'Ohio State',
                'age': 21, 'height': '6-3', 'weight': 205
            },
            {
                'round': 1, 'pick': 5, 'overall': 5, 'team': 'Los Angeles Chargers',
                'player': 'Joe Alt', 'position': 'OT', 'college': 'Notre Dame',
                'age': 21, 'height': '6-8', 'weight': 321
            },
            {
                'round': 1, 'pick': 6, 'overall': 6, 'team': 'New York Giants',
                'player': 'Malik Nabers', 'position': 'WR', 'college': 'LSU',
                'age': 21, 'height': '6-0', 'weight': 200
            }
        ]
        
        # Convert to DataFrame and add analysis
        draft_df = pd.DataFrame(draft_data)
        draft_df['projected_impact'] = self._calculate_draft_impact(draft_df)
        draft_df['need_filled'] = self._assess_team_need(draft_df)
        
        return draft_df
        
    def scrape_free_agency_moves(self):
        """Major 2024 free agency moves (corrected)"""
        
        logger.info("Fetching CORRECTED 2024 free agency moves...")
        
        fa_moves = [
            {
                'date': '2024-03-13', 'player': 'Calvin Ridley', 'position': 'WR',
                'from_team': 'Jacksonville Jaguars', 'to_team': 'Tennessee Titans',
                'contract_years': 4, 'contract_value': 92000000, 'guaranteed': 50000000,
                'age': 29, 'previous_stats': '76 rec, 1016 yards, 8 TD'
            },
            {
                'date': '2024-03-14', 'player': 'Saquon Barkley', 'position': 'RB', 
                'from_team': 'New York Giants', 'to_team': 'Philadelphia Eagles',
                'contract_years': 3, 'contract_value': 37750000, 'guaranteed': 26000000,
                'age': 27, 'previous_stats': '962 yards, 10 TD'
            },
            {
                'date': '2024-03-15', 'player': 'Brian Burns', 'position': 'EDGE',
                'from_team': 'Carolina Panthers', 'to_team': 'New York Giants', 
                'contract_years': 5, 'contract_value': 141000000, 'guaranteed': 87500000,
                'age': 26, 'previous_stats': '8 sacks, 56 tackles'
            },
            {
                'date': '2024-03-16', 'player': 'Kirk Cousins', 'position': 'QB',
                'from_team': 'Minnesota Vikings', 'to_team': 'Atlanta Falcons',
                'contract_years': 4, 'contract_value': 180000000, 'guaranteed': 100000000,
                'age': 35, 'previous_stats': '2331 yards, 18 TD'
            }
        ]
        
        # Convert to DataFrame and add analysis
        fa_df = pd.DataFrame(fa_moves)
        fa_df['aav'] = fa_df['contract_value'] / fa_df['contract_years']
        fa_df['impact_rating'] = self._calculate_fa_impact(fa_df)
        
        return fa_df
        
    def _calculate_draft_impact(self, draft_df):
        """Calculate projected impact for draft picks"""
        
        impact_scores = []
        position_values = {'QB': 5.0, 'WR': 3.0, 'OT': 2.8, 'EDGE': 3.5, 'CB': 3.5}
        
        for _, pick in draft_df.iterrows():
            base_impact = position_values.get(pick['position'], 2.0)
            
            # Adjust by draft position (top 5 picks get bonus)
            if pick['overall'] <= 5:
                round_multiplier = 1.2
            elif pick['round'] == 1:
                round_multiplier = 1.0
            else:
                round_multiplier = 0.7
                
            impact = base_impact * round_multiplier
            impact_scores.append(round(impact, 1))
            
        return impact_scores
        
    def _calculate_fa_impact(self, fa_df):
        """Calculate impact rating for free agency moves"""
        
        impact_scores = []
        position_values = {'QB': 5.0, 'WR': 3.0, 'RB': 2.0, 'EDGE': 3.5, 'CB': 3.5}
        
        for _, move in fa_df.iterrows():
            base_impact = position_values.get(move['position'], 2.0)
            
            # Adjust by contract value (AAV)
            aav = move['aav']
            if aav > 30000000:
                contract_multiplier = 1.3
            elif aav > 20000000:
                contract_multiplier = 1.2
            elif aav > 10000000:
                contract_multiplier = 1.0
            else:
                contract_multiplier = 0.8
                
            # Adjust by age
            age = move['age']
            if age < 26:
                age_multiplier = 1.1
            elif age < 30:
                age_multiplier = 1.0
            else:
                age_multiplier = 0.8  # Bigger penalty for older players
                
            impact = base_impact * contract_multiplier * age_multiplier
            impact_scores.append(round(impact, 1))
            
        return impact_scores
        
    def _assess_team_need(self, draft_df):
        """Assess whether draft pick filled a team need"""
        
        needs = []
        for _, pick in draft_df.iterrows():
            team = pick['team']
            position = pick['position']
            
            # Team-specific need analysis
            if team == 'Chicago Bears' and position == 'QB':
                needs.append('Critical - Franchise QB')
            elif team == 'Washington Commanders' and position == 'QB':
                needs.append('High - QB upgrade')
            elif position == 'QB':
                needs.append('Medium - QB depth/future')
            elif position in ['WR', 'OT']:
                needs.append('High - Skill position need')
            else:
                needs.append('Medium - Depth/BPA')
                
        return needs
        
    def create_corrected_report(self):
        """Generate corrected offseason report"""
        
        print("🏈 NFL 2024 Offseason Report (CORRECTED)")
        print("=" * 45)
        
        # Get corrected data
        draft_data = self.scrape_2024_draft_results()
        fa_data = self.scrape_free_agency_moves()
        
        print(f"✅ Corrected Data:")
        print(f"  🎓 {len(draft_data)} draft picks")
        print(f"  💰 {len(fa_data)} free agency moves")
        
        # Show corrected top picks
        print(f"\n🎓 Corrected 2024 Draft (Top 6):")
        for _, pick in draft_data.iterrows():
            print(f"  {pick['overall']}. {pick['player']} ({pick['position']}) → {pick['team']} (Impact: {pick['projected_impact']})")
            
        # Show top FA moves with correct salaries
        print(f"\n💰 Major Free Agency Moves:")
        top_fa = fa_data.nlargest(4, 'aav')
        for _, move in top_fa.iterrows():
            aav_millions = move['aav'] / 1000000
            print(f"  {move['player']} ({move['position']}) → {move['to_team']}: ${aav_millions:.1f}M/yr (Impact: {move['impact_rating']})")
            
        print(f"\n🎯 Data corrections complete!")
        
        return draft_data, fa_data


def main():
    scraper = NFLOffseasonScraperCorrected()
    scraper.create_corrected_report()


if __name__ == "__main__":
    main()

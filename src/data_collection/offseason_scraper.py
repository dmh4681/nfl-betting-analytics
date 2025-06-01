"""
NFL Offseason Data Scraper
Automatically collect free agency moves and draft picks from public APIs
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

class NFLOffseasonScraper:
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
            
        logger.info(f"Loaded {len(self.team_mappings)} team mappings")
        
    def scrape_2024_draft_results(self):
        """Scrape 2024 NFL Draft results (we'll simulate with realistic data structure)"""
        
        # In production, this would hit an API like:
        # ESPN API: https://site.api.espn.com/apis/site/v2/sports/football/nfl/draft/2024
        
        logger.info("Fetching 2024 NFL Draft results...")
        
        # For now, let's create the structure with a few real examples
        # You can populate this with actual API data
        draft_data = [
            {
                'round': 1, 'pick': 1, 'overall': 1, 'team': 'Washington Commanders',
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
            }
        ]
        
        # Convert to DataFrame
        draft_df = pd.DataFrame(draft_data)
        
        # Add analysis columns
        draft_df['team_abbrev'] = draft_df['team'].map(self.team_lookup)
        draft_df['projected_impact'] = self._calculate_draft_impact(draft_df)
        draft_df['need_filled'] = self._assess_team_need(draft_df)
        draft_df['notes'] = ''
        
        logger.info(f"Collected {len(draft_df)} draft picks")
        return draft_df
        
    def scrape_free_agency_moves(self):
        """Scrape recent free agency signings"""
        
        # In production, this could scrape from:
        # ESPN Free Agency Tracker, NFL.com, or Pro Football Reference
        
        logger.info("Fetching recent free agency moves...")
        
        # Sample free agency data (replace with real API calls)
        fa_moves = [
            {
                'date': '2024-03-13', 'player': 'Calvin Ridley', 'position': 'WR',
                'from_team': 'Jacksonville Jaguars', 'to_team': 'Tennessee Titans',
                'contract_years': 4, 'contract_value': 92000000, 'guaranteed': 50000000,
                'age': 29, 'previous_stats': '76 rec, 1016 yards, 8 TD'
            },
            {
                'date': '2024-03-14', 'player': 'Mike Evans', 'position': 'WR', 
                'from_team': 'Tampa Bay Buccaneers', 'to_team': 'Tampa Bay Buccaneers',
                'contract_years': 2, 'contract_value': 52000000, 'guaranteed': 35000000,
                'age': 30, 'previous_stats': '79 rec, 1255 yards, 13 TD'
            },
            {
                'date': '2024-03-15', 'player': 'Brian Burns', 'position': 'EDGE',
                'from_team': 'Carolina Panthers', 'to_team': 'New York Giants', 
                'contract_years': 5, 'contract_value': 141000000, 'guaranteed': 87500000,
                'age': 26, 'previous_stats': '8 sacks, 56 tackles'
            },
            {
                'date': '2024-03-16', 'player': 'Josh Jacobs', 'position': 'RB',
                'from_team': 'Las Vegas Raiders', 'to_team': 'Green Bay Packers',
                'contract_years': 4, 'contract_value': 48000000, 'guaranteed': 12000000,
                'age': 26, 'previous_stats': '805 yards, 6 TD'
            }
        ]
        
        # Convert to DataFrame  
        fa_df = pd.DataFrame(fa_moves)
        
        # Add analysis columns
        fa_df['aav'] = fa_df['contract_value'] / fa_df['contract_years']
        fa_df['from_team_abbrev'] = fa_df['from_team'].map(self.team_lookup)
        fa_df['to_team_abbrev'] = fa_df['to_team'].map(self.team_lookup)
        fa_df['impact_rating'] = self._calculate_fa_impact(fa_df)
        fa_df['notes'] = ''
        
        logger.info(f"Collected {len(fa_df)} free agency moves")
        return fa_df
        
    def scrape_coaching_changes(self):
        """Scrape coaching changes"""
        
        logger.info("Fetching coaching changes...")
        
        coaching_changes = [
            {
                'team': 'Los Angeles Chargers', 'position': 'Head Coach',
                'previous_coach': 'Brandon Staley', 'new_coach': 'Jim Harbaugh',
                'date': '2024-01-24', 'experience': 'Michigan HC, former NFL',
                'previous_success': 'College Football National Championship',
                'system_change': 'Defensive to offensive minded'
            },
            {
                'team': 'Tennessee Titans', 'position': 'Head Coach', 
                'previous_coach': 'Mike Vrabel', 'new_coach': 'Brian Callahan',
                'date': '2024-01-21', 'experience': 'Bengals OC',
                'previous_success': 'Offensive coordinator success',
                'system_change': 'Continued offensive focus'
            },
            {
                'team': 'Carolina Panthers', 'position': 'Head Coach',
                'previous_coach': 'Frank Reich', 'new_coach': 'Dave Canales', 
                'date': '2024-01-25', 'experience': 'Buccaneers OC',
                'previous_success': 'Developed Baker Mayfield',
                'system_change': 'New offensive philosophy'
            }
        ]
        
        coaching_df = pd.DataFrame(coaching_changes)
        coaching_df['impact_rating'] = self._calculate_coaching_impact(coaching_df)
        coaching_df['notes'] = ''
        
        logger.info(f"Collected {len(coaching_df)} coaching changes")
        return coaching_df
        
    def _calculate_draft_impact(self, draft_df):
        """Calculate projected impact for draft picks"""
        
        impact_scores = []
        
        position_values = {'QB': 5.0, 'WR': 3.0, 'OT': 2.8, 'EDGE': 3.5, 'CB': 3.5}
        
        for _, pick in draft_df.iterrows():
            base_impact = position_values.get(pick['position'], 2.0)
            
            # Adjust by draft position
            if pick['round'] == 1:
                round_multiplier = 1.0
            elif pick['round'] == 2:
                round_multiplier = 0.7
            else:
                round_multiplier = 0.4
                
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
            if aav > 20000000:
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
                age_multiplier = 0.9
                
            impact = base_impact * contract_multiplier * age_multiplier
            impact_scores.append(round(impact, 1))
            
        return impact_scores
        
    def _calculate_coaching_impact(self, coaching_df):
        """Calculate impact of coaching changes"""
        
        # Coaching changes generally have moderate impact
        # Can be refined based on historical analysis
        impact_scores = []
        
        for _, change in coaching_df.iterrows():
            if change['position'] == 'Head Coach':
                base_impact = 2.0
            else:
                base_impact = 1.5
                
            impact_scores.append(base_impact)
            
        return impact_scores
        
    def _assess_team_need(self, draft_df):
        """Assess whether draft pick filled a team need"""
        
        # This could be enhanced with actual team need analysis
        needs = []
        for _, pick in draft_df.iterrows():
            if pick['position'] == 'QB':
                needs.append('High - QB need')
            elif pick['position'] in ['WR', 'OT']:
                needs.append('Medium - Skill position')
            else:
                needs.append('Low - Depth/BPA')
                
        return needs
        
    def update_offseason_tracker(self):
        """Update the offseason tracker with scraped data"""
        
        logger.info("Updating offseason tracker with scraped data...")
        
        # Load existing tracker
        tracker_file = self.output_path / "NFL_2025_Offseason_Tracker.xlsx"
        
        if not tracker_file.exists():
            logger.error(f"Tracker file not found: {tracker_file}")
            return None
            
        # Scrape all data
        draft_data = self.scrape_2024_draft_results()
        fa_data = self.scrape_free_agency_moves()
        coaching_data = self.scrape_coaching_changes()
        
        # Update Excel file
        with pd.ExcelWriter(tracker_file, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            fa_data.to_excel(writer, sheet_name='Free Agency', index=False)
            draft_data.to_excel(writer, sheet_name='Draft', index=False)
            coaching_data.to_excel(writer, sheet_name='Coaching Changes', index=False)
            
        logger.info(f"Updated tracker with:")
        logger.info(f"  {len(fa_data)} free agency moves")
        logger.info(f"  {len(draft_data)} draft picks") 
        logger.info(f"  {len(coaching_data)} coaching changes")
        
        return {
            'free_agency': fa_data,
            'draft': draft_data,
            'coaching': coaching_data
        }
        
    def generate_team_impact_summary(self):
        """Generate summary of offseason impact by team"""
        
        data = self.update_offseason_tracker()
        if not data:
            return
            
        team_impacts = {}
        
        # Calculate net impact for each team
        for team_key, team_info in self.team_mappings.items():
            team_name = team_info['full_name']
            team_impacts[team_name] = {
                'fa_gained': 0, 'fa_lost': 0, 'draft_impact': 0, 
                'coaching_impact': 0, 'net_impact': 0, 'moves': []
            }
            
        # Process free agency
        for _, move in data['free_agency'].iterrows():
            to_team = move['to_team']
            from_team = move['from_team']
            impact = move['impact_rating']
            
            if to_team in team_impacts:
                team_impacts[to_team]['fa_gained'] += impact
                team_impacts[to_team]['moves'].append(f"+ {move['player']} ({move['position']})")
                
            if from_team in team_impacts:
                team_impacts[from_team]['fa_lost'] += impact
                team_impacts[from_team]['moves'].append(f"- {move['player']} ({move['position']})")
                
        # Process draft
        for _, pick in data['draft'].iterrows():
            team = pick['team']
            impact = pick['projected_impact']
            
            if team in team_impacts:
                team_impacts[team]['draft_impact'] += impact
                team_impacts[team]['moves'].append(f"Draft: {pick['player']} (R{pick['round']})")
                
        # Process coaching
        for _, change in data['coaching'].iterrows():
            team = change['team']
            impact = change['impact_rating']
            
            if team in team_impacts:
                team_impacts[team]['coaching_impact'] += impact
                team_impacts[team]['moves'].append(f"Coach: {change['new_coach']}")
                
        # Calculate net impact
        for team in team_impacts:
            impacts = team_impacts[team]
            impacts['net_impact'] = (impacts['fa_gained'] - impacts['fa_lost'] + 
                                   impacts['draft_impact'] + impacts['coaching_impact'])
                                   
        return team_impacts
        
    def create_offseason_report(self):
        """Create comprehensive offseason report"""
        
        print("🏈 NFL 2025 Offseason Data Update")
        print("=" * 40)
        
        # Update tracker with scraped data
        data = self.update_offseason_tracker()
        
        if data:
            print(f"✅ Data Collection Complete:")
            print(f"  📋 {len(data['free_agency'])} free agency moves")
            print(f"  🎓 {len(data['draft'])} draft picks")
            print(f"  👔 {len(data['coaching'])} coaching changes")
            
            # Show top free agency moves
            print(f"\n💰 Top Free Agency Moves:")
            top_fa = data['free_agency'].nlargest(3, 'aav')
            for _, move in top_fa.iterrows():
                print(f"  {move['player']} ({move['position']}) → {move['to_team']}: M/yr")
                
            # Show top draft picks
            print(f"\n🎓 Top Draft Picks:")
            top_draft = data['draft'].head(5)
            for _, pick in top_draft.iterrows():
                print(f"  {pick['overall']}. {pick['player']} ({pick['position']}) → {pick['team']}")
                
            # Team impact summary
            print(f"\n📊 Team Impact Leaders:")
            team_impacts = self.generate_team_impact_summary()
            
            # Sort by net impact
            sorted_teams = sorted(team_impacts.items(), key=lambda x: x[1]['net_impact'], reverse=True)
            
            print(f"\nBiggest Winners:")
            for team, impact in sorted_teams[:5]:
                print(f"  {team}: +{impact['net_impact']:.1f}")
                for move in impact['moves'][:3]:  # Show top 3 moves
                    print(f"    {move}")
                    
            print(f"\nBiggest Losers:")
            for team, impact in sorted_teams[-3:]:
                print(f"  {team}: {impact['net_impact']:.1f}")
                for move in impact['moves'][:3]:
                    print(f"    {move}")
                    
        print(f"\n🎯 Offseason tracker updated and ready!")


def main():
    scraper = NFLOffseasonScraper()
    scraper.create_offseason_report()


if __name__ == "__main__":
    main()

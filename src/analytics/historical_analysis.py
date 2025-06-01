"""
NFL Historical Power Rankings Analysis
Extract and analyze 2024 final power rankings vs market performance
"""

import pandas as pd
import numpy as np
from pathlib import Path
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils.excel_reader import NFLExcelReader

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PowerRankingsAnalyzer:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.historical_path = self.project_root / \"data\" / \"historical\" / \"NFL_Master_Historical.xlsx\"
        self.reader = NFLExcelReader(str(self.historical_path))
        
    def extract_2024_final_power_rankings(self):
        \"\"\"Extract final 2024 power rankings\"\"\"
        
        # Look for 2024 power rankings sheets
        sheets = self.reader.get_available_sheets()
        power_ranking_sheets = [s for s in sheets if '2024' in s and 'power' in s.lower()]
        
        logger.info(f\"Found power ranking sheets: {power_ranking_sheets}\")
        
        # If no 2024, try 2023 as example
        if not power_ranking_sheets:
            power_ranking_sheets = [s for s in sheets if '2023' in s and 'power' in s.lower()]
            
        if power_ranking_sheets:
            # Read the most recent power rankings
            latest_sheet = power_ranking_sheets[0]
            df = pd.read_excel(self.historical_path, sheet_name=latest_sheet)
            logger.info(f\"Loaded power rankings from {latest_sheet}\")
            return df, latest_sheet
        else:
            logger.error(\"No power ranking sheets found\")
            return None, None
            
    def extract_final_market_data(self, year=2023):
        \"\"\"Extract final weeks market data (closing lines)\"\"\"
        
        final_weeks = [f\"{year} Week 17\", f\"{year} Week 18\", \"Wildcard Weekend\", \"Divisional Weekend\"]
        market_data = []
        
        for week in final_weeks:
            try:
                df = self.reader.read_weekly_games(year, week.replace(f\"{year} \", \"\"))
                if not df.empty:
                    market_data.append(df)
                    logger.info(f\"Extracted {len(df)} games from {week}\")
            except Exception as e:
                logger.warning(f\"Could not read {week}: {e}\")
                
        if market_data:
            combined = pd.concat(market_data, ignore_index=True)
            return combined
        else:
            return pd.DataFrame()
            
    def analyze_ranking_accuracy(self, power_rankings_df, market_data_df):
        \"\"\"Analyze how accurate power rankings were vs market\"\"\"
        
        if power_rankings_df is None or market_data_df.empty:
            logger.error(\"Missing data for accuracy analysis\")
            return None
            
        logger.info(\"Analyzing power ranking accuracy...\")
        
        # Extract team rankings
        if 'Team Name' in power_rankings_df.columns and 'Rating' in power_rankings_df.columns:
            rankings = power_rankings_df[['Team Name', 'Rating']].copy()
            rankings = rankings.dropna()
            
            logger.info(f\"Found {len(rankings)} team power rankings\")
            
            # Basic statistics
            stats = {
                'mean_rating': rankings['Rating'].mean(),
                'std_rating': rankings['Rating'].std(),
                'max_rating': rankings['Rating'].max(),
                'min_rating': rankings['Rating'].min(),
                'rating_range': rankings['Rating'].max() - rankings['Rating'].min()
            }
            
            return rankings, stats
        else:
            logger.error(f\"Expected columns not found. Available: {power_rankings_df.columns.tolist()}\")
            return None, None
            
    def create_offseason_tracker_template(self):
        \"\"\"Create template for tracking offseason moves\"\"\"
        
        columns = [
            'Date', 'Team', 'Player_Name', 'Position', 'Move_Type', 
            'Previous_Team', 'Contract_Value', 'Contract_Years',
            'Age', 'Previous_Performance', 'Impact_Score', 'Notes'
        ]
        
        move_types = ['FA_Signing', 'Trade_Acquired', 'Trade_Lost', 'Draft_Pick', 'Cut', 'Retirement']
        
        # Create sample template
        template_data = []
        for team_key in self.reader.team_mappings.keys():
            team_name = self.reader.team_mappings[team_key]['full_name']
            template_data.append([
                '2025-03-01', team_name, 'Example Player', 'QB', 'FA_Signing',
                'Previous Team', 50000000, 3, 28, 'Good', 2.5, 'Sample entry'
            ])
            
        template_df = pd.DataFrame(template_data, columns=columns)
        
        # Save template
        output_path = self.project_root / \"data\" / \"current_season\" / \"offseason_moves_tracker.xlsx\"
        template_df.to_excel(output_path, index=False)
        
        logger.info(f\"Created offseason tracker template: {output_path}\")
        return template_df
        
    def generate_analysis_report(self):
        \"\"\"Generate comprehensive historical analysis report\"\"\"
        
        print(\"🏈 NFL Historical Power Rankings Analysis\")
        print(\"=\" * 45)
        
        # Extract power rankings
        power_df, sheet_name = self.extract_2024_final_power_rankings()
        
        if power_df is not None:
            print(f\"✅ Found power rankings: {sheet_name}\")
            print(f\"📊 Teams analyzed: {len(power_df)}\")
            
            # Show top and bottom teams
            if 'Team Name' in power_df.columns:
                ratings_col = None
                for col in power_df.columns:
                    if 'rating' in col.lower() and power_df[col].dtype in ['float64', 'int64']:
                        ratings_col = col
                        break
                        
                if ratings_col:
                    sorted_teams = power_df.sort_values(ratings_col, ascending=False)
                    print(f\"\\n🏆 Top 5 Teams by {ratings_col}:\")
                    for i, row in sorted_teams.head().iterrows():
                        print(f\"  {row['Team Name']}: {row[ratings_col]}\")
                        
                    print(f\"\\n📉 Bottom 5 Teams:\")
                    for i, row in sorted_teams.tail().iterrows():
                        print(f\"  {row['Team Name']}: {row[ratings_col]}\")
        else:
            print(\"❌ No power rankings data found\")
            
        # Extract market data
        market_df = self.extract_final_market_data(2023)
        
        if not market_df.empty:
            print(f\"\\n✅ Found market data: {len(market_df)} games\")
            
            # Analyze spreads
            spreads = market_df['closing_line'].dropna()
            if len(spreads) > 0:
                print(f\"📈 Average closing spread: {spreads.mean():.1f}\")
                print(f\"📊 Spread range: {spreads.min():.1f} to {spreads.max():.1f}\")
        else:
            print(\"❌ No market data found\")
            
        # Create offseason tracker
        print(\"\\n🔄 Creating offseason tracker template...\")
        tracker_df = self.create_offseason_tracker_template()
        print(f\"✅ Template created with {len(tracker_df)} sample entries\")
        
        print(\"\\n📋 Next Steps:\")
        print(\"1. Review power rankings accuracy vs final results\")
        print(\"2. Begin tracking free agency moves in the template\")
        print(\"3. Set up automated data collection for offseason moves\")
        print(\"4. Build impact scoring system for player moves\")
        
        return power_df, market_df, tracker_df


def main():
    analyzer = PowerRankingsAnalyzer()
    analyzer.generate_analysis_report()


if __name__ == \"__main__\":
    main()

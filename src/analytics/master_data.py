"""
NFL Master Data Tables Creator
Creates clean, structured datasets from the Player Bridge Framework
Perfect for downstream analysis, visualization, and reporting
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFLMasterDataCreator:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.input_path = self.project_root / "output" / "player_bridge"
        self.output_path = self.project_root / "output" / "master_data"
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # Load the generated data
        self.load_framework_data()
        
    def load_framework_data(self):
        """Load all the generated CSV files from player bridge framework"""
        try:
            # Load the three main CSV files
            self.player_moves = pd.read_csv(self.input_path / "player_bridge_moves.csv")
            self.team_grades = pd.read_csv(self.input_path / "team_offseason_grades.csv")
            self.final_rankings = pd.read_csv(self.input_path / "final_2025_power_rankings.csv")
            
            logger.info(f"✅ Loaded {len(self.player_moves)} player moves")
            logger.info(f"✅ Loaded {len(self.team_grades)} team grades")
            logger.info(f"✅ Loaded {len(self.final_rankings)} team rankings")
            
        except FileNotFoundError as e:
            logger.error(f"❌ Could not find framework data files: {e}")
            logger.error("Make sure to run player_bridge_framework.py first!")
            raise
    
    def create_players_master_table(self) -> pd.DataFrame:
        """Create comprehensive player moves master table"""
        logger.info("📊 Creating Players Master Table...")
        
        players = self.player_moves.copy()
        
        # Clean and standardize data
        players['move_date'] = datetime.now().strftime('%Y-%m-%d')
        players['move_year'] = 2025
        
        # Add calculated fields
        players['grade_change'] = players['projected_2025_grade'] - players['2024_grade']
        players['snap_tier'] = pd.cut(players['snap_percentage_2024'], 
                                     bins=[0, 25, 50, 75, 100], 
                                     labels=['Backup', 'Rotational', 'Starter', 'Workhorse'])
        
        # Impact categorization
        players['impact_tier'] = pd.cut(players['impact_score'],
                                       bins=[-10, 0, 0.5, 1.0, 2.0, 10],
                                       labels=['Negative', 'Minimal', 'Moderate', 'High', 'Elite'])
        
        # Position groupings
        position_groups = {
            'QB': 'Offense - Skill',
            'RB': 'Offense - Skill',
            'WR1': 'Offense - Skill', 'WR2': 'Offense - Skill', 'WR3': 'Offense - Skill',
            'TE': 'Offense - Skill',
            'LT': 'Offense - Line', 'RT': 'Offense - Line', 'G': 'Offense - Line', 
            'C': 'Offense - Line', 'OL': 'Offense - Line',
            'EDGE': 'Defense - Front', 'DT': 'Defense - Front',
            'LB': 'Defense - Second',
            'CB1': 'Defense - Secondary', 'CB2': 'Defense - Secondary', 'S': 'Defense - Secondary',
            'K': 'Special Teams', 'P': 'Special Teams', 'LS': 'Special Teams',
            'COACH': 'Coaching', 'HC': 'Coaching', 'OC': 'Coaching', 'DC': 'Coaching'
        }
        players['position_group'] = players['position'].map(position_groups).fillna('Other')
        
        # Contract analysis
        players['aav'] = players['contract_value'] / players['contract_years'].replace(0, 1)
        players['contract_tier'] = pd.cut(players['aav'],
                                         bins=[0, 1e6, 5e6, 15e6, 30e6, 1e9],
                                         labels=['Rookie/Minimum', 'Role Player', 'Starter', 'Star', 'Superstar'])
        
        # Select and order key columns
        master_columns = [
            'player_name', 'position', 'position_group', 'from_team', 'to_team', 'move_type',
            '2024_grade', 'projected_2025_grade', 'grade_change',
            'snap_percentage_2024', 'snap_tier',
            'impact_score', 'impact_tier',
            'importance_to_old_team', 'importance_to_new_team',
            'contract_years', 'contract_value', 'aav', 'contract_tier',
            'move_date', 'move_year'
        ]
        
        return players[master_columns].sort_values(['impact_score'], ascending=False)
    
    def create_teams_master_table(self) -> pd.DataFrame:
        """Create comprehensive teams master table"""
        logger.info("📊 Creating Teams Master Table...")
        
        # Merge team grades and final rankings
        teams = self.team_grades.merge(
            self.final_rankings[['team', 'original_2024_rating', 'original_2024_rank', 
                               'final_2025_rating', 'final_2025_rank', 'rank_change']],
            on='team', how='left'
        )
        
        # Add team metadata
        team_metadata = {
            # NFC East
            'PHI': {'division': 'NFC East', 'conference': 'NFC', 'city': 'Philadelphia', 'nickname': 'Eagles'},
            'DAL': {'division': 'NFC East', 'conference': 'NFC', 'city': 'Dallas', 'nickname': 'Cowboys'},
            'NYG': {'division': 'NFC East', 'conference': 'NFC', 'city': 'New York', 'nickname': 'Giants'},
            'WAS': {'division': 'NFC East', 'conference': 'NFC', 'city': 'Washington', 'nickname': 'Commanders'},
            
            # NFC North
            'GB': {'division': 'NFC North', 'conference': 'NFC', 'city': 'Green Bay', 'nickname': 'Packers'},
            'DET': {'division': 'NFC North', 'conference': 'NFC', 'city': 'Detroit', 'nickname': 'Lions'},
            'MIN': {'division': 'NFC North', 'conference': 'NFC', 'city': 'Minnesota', 'nickname': 'Vikings'},
            'CHI': {'division': 'NFC North', 'conference': 'NFC', 'city': 'Chicago', 'nickname': 'Bears'},
            
            # NFC South
            'NO': {'division': 'NFC South', 'conference': 'NFC', 'city': 'New Orleans', 'nickname': 'Saints'},
            'ATL': {'division': 'NFC South', 'conference': 'NFC', 'city': 'Atlanta', 'nickname': 'Falcons'},
            'TB': {'division': 'NFC South', 'conference': 'NFC', 'city': 'Tampa Bay', 'nickname': 'Buccaneers'},
            'CAR': {'division': 'NFC South', 'conference': 'NFC', 'city': 'Carolina', 'nickname': 'Panthers'},
            
            # NFC West
            'SF': {'division': 'NFC West', 'conference': 'NFC', 'city': 'San Francisco', 'nickname': '49ers'},
            'SEA': {'division': 'NFC West', 'conference': 'NFC', 'city': 'Seattle', 'nickname': 'Seahawks'},
            'LAR': {'division': 'NFC West', 'conference': 'NFC', 'city': 'Los Angeles', 'nickname': 'Rams'},
            'ARI': {'division': 'NFC West', 'conference': 'NFC', 'city': 'Arizona', 'nickname': 'Cardinals'},
            
            # AFC East
            'BUF': {'division': 'AFC East', 'conference': 'AFC', 'city': 'Buffalo', 'nickname': 'Bills'},
            'MIA': {'division': 'AFC East', 'conference': 'AFC', 'city': 'Miami', 'nickname': 'Dolphins'},
            'NE': {'division': 'AFC East', 'conference': 'AFC', 'city': 'New England', 'nickname': 'Patriots'},
            'NYJ': {'division': 'AFC East', 'conference': 'AFC', 'city': 'New York', 'nickname': 'Jets'},
            
            # AFC North
            'BAL': {'division': 'AFC North', 'conference': 'AFC', 'city': 'Baltimore', 'nickname': 'Ravens'},
            'PIT': {'division': 'AFC North', 'conference': 'AFC', 'city': 'Pittsburgh', 'nickname': 'Steelers'},
            'CLE': {'division': 'AFC North', 'conference': 'AFC', 'city': 'Cleveland', 'nickname': 'Browns'},
            'CIN': {'division': 'AFC North', 'conference': 'AFC', 'city': 'Cincinnati', 'nickname': 'Bengals'},
            
            # AFC South
            'HOU': {'division': 'AFC South', 'conference': 'AFC', 'city': 'Houston', 'nickname': 'Texans'},
            'IND': {'division': 'AFC South', 'conference': 'AFC', 'city': 'Indianapolis', 'nickname': 'Colts'},
            'TEN': {'division': 'AFC South', 'conference': 'AFC', 'city': 'Tennessee', 'nickname': 'Titans'},
            'JAC': {'division': 'AFC South', 'conference': 'AFC', 'city': 'Jacksonville', 'nickname': 'Jaguars'},
            
            # AFC West
            'KC': {'division': 'AFC West', 'conference': 'AFC', 'city': 'Kansas City', 'nickname': 'Chiefs'},
            'LAC': {'division': 'AFC West', 'conference': 'AFC', 'city': 'Los Angeles', 'nickname': 'Chargers'},
            'DEN': {'division': 'AFC West', 'conference': 'AFC', 'city': 'Denver', 'nickname': 'Broncos'},
            'LV': {'division': 'AFC West', 'conference': 'AFC', 'city': 'Las Vegas', 'nickname': 'Raiders'}
        }
        
        for col in ['division', 'conference', 'city', 'nickname']:
            teams[col] = teams['team'].map(lambda x: team_metadata.get(x, {}).get(col, ''))
        
        # Calculate additional metrics
        teams['total_moves'] = teams['players_gained'] + teams['players_lost']
        teams['move_efficiency'] = teams['net_impact'] / teams['total_moves'].replace(0, 1)
        teams['improvement_vs_expectation'] = teams['final_2025_rating'] - teams['original_2024_rating']
        
        # Categorize teams by strategy
        def categorize_strategy(row):
            if row['net_impact'] >= 2.0:
                return 'Aggressive Improvement'
            elif row['net_impact'] >= 0.5:
                return 'Measured Addition'
            elif row['net_impact'] >= -0.5:
                return 'Status Quo'
            elif row['net_impact'] >= -2.0:
                return 'Controlled Transition'
            else:
                return 'Major Rebuild'
        
        teams['offseason_strategy'] = teams.apply(categorize_strategy, axis=1)
        
        # Select and order columns
        master_columns = [
            'team', 'team_name', 'city', 'nickname', 'division', 'conference',
            'original_2024_rank', 'original_2024_rating',
            'final_2025_rank', 'final_2025_rating', 'rank_change',
            'players_gained', 'players_lost', 'total_moves',
            'impact_gained', 'impact_lost', 'net_impact', 'move_efficiency',
            'offense_impact', 'defense_impact', 'special_teams_impact', 'coaching_impact',
            'offseason_grade', 'offseason_strategy',
            'key_additions', 'key_losses'
        ]
        
        return teams[master_columns].sort_values('final_2025_rank')
    
    def create_moves_summary_table(self) -> pd.DataFrame:
        """Create move type summary analysis"""
        logger.info("📊 Creating Moves Summary Table...")
        
        moves_summary = []
        
        for move_type in self.player_moves['move_type'].unique():
            if pd.isna(move_type):
                continue
                
            subset = self.player_moves[self.player_moves['move_type'] == move_type]
            
            moves_summary.append({
                'move_type': move_type,
                'total_moves': len(subset),
                'avg_impact': subset['impact_score'].mean(),
                'total_impact': subset['impact_score'].sum(),
                'avg_contract_value': subset['contract_value'].mean(),
                'total_contract_value': subset['contract_value'].sum(),
                'avg_2024_grade': subset['2024_grade'].mean(),
                'avg_projected_grade': subset['projected_2025_grade'].mean(),
                'top_player': subset.nlargest(1, 'impact_score')['player_name'].iloc[0] if len(subset) > 0 else '',
                'top_impact': subset['impact_score'].max()
            })
        
        return pd.DataFrame(moves_summary).sort_values('total_impact', ascending=False)
    
    def create_position_analysis_table(self) -> pd.DataFrame:
        """Create position group analysis"""
        logger.info("📊 Creating Position Analysis Table...")
        
        players = self.create_players_master_table()
        
        position_analysis = []
        
        for pos_group in players['position_group'].unique():
            if pd.isna(pos_group):
                continue
                
            subset = players[players['position_group'] == pos_group]
            
            position_analysis.append({
                'position_group': pos_group,
                'total_moves': len(subset),
                'avg_impact': subset['impact_score'].mean(),
                'total_impact': subset['impact_score'].sum(),
                'avg_contract_value': subset['contract_value'].mean(),
                'most_active_position': subset['position'].mode().iloc[0] if len(subset) > 0 else '',
                'highest_paid_player': subset.nlargest(1, 'contract_value')['player_name'].iloc[0] if len(subset) > 0 else '',
                'highest_impact_player': subset.nlargest(1, 'impact_score')['player_name'].iloc[0] if len(subset) > 0 else '',
                'free_agents': len(subset[subset['move_type'] == 'Free Agent Signing']),
                'trades': len(subset[subset['move_type'] == 'Trade']),
                'draft_picks': len(subset[subset['move_type'].str.contains('Draft', na=False)])
            })
        
        return pd.DataFrame(position_analysis).sort_values('total_impact', ascending=False)
    
    def create_division_summary_table(self) -> pd.DataFrame:
        """Create division-level analysis"""
        logger.info("📊 Creating Division Summary Table...")
        
        teams = self.create_teams_master_table()
        
        division_summary = []
        
        for division in teams['division'].unique():
            if pd.isna(division) or division == '':
                continue
                
            div_teams = teams[teams['division'] == division]
            
            division_summary.append({
                'division': division,
                'conference': div_teams['conference'].iloc[0],
                'teams_count': len(div_teams),
                'avg_net_impact': div_teams['net_impact'].mean(),
                'total_moves': div_teams['total_moves'].sum(),
                'avg_final_rating': div_teams['final_2025_rating'].mean(),
                'best_team': div_teams.nlargest(1, 'final_2025_rating')['team'].iloc[0],
                'best_offseason': div_teams.nlargest(1, 'net_impact')['team'].iloc[0],
                'most_active': div_teams.nlargest(1, 'total_moves')['team'].iloc[0],
                'strength_rating': div_teams['final_2025_rating'].mean(),
                'competitive_balance': div_teams['final_2025_rating'].std()
            })
        
        return pd.DataFrame(division_summary).sort_values('strength_rating', ascending=False)
    
    def generate_all_master_tables(self):
        """Generate all master data tables"""
        logger.info("🏈 Generating NFL Master Data Tables...")
        
        # Create all tables
        players_master = self.create_players_master_table()
        teams_master = self.create_teams_master_table()
        moves_summary = self.create_moves_summary_table()
        position_analysis = self.create_position_analysis_table()
        division_summary = self.create_division_summary_table()
        
        # Save all tables
        tables = {
            'players_master': players_master,
            'teams_master': teams_master,
            'moves_summary': moves_summary,
            'position_analysis': position_analysis,
            'division_summary': division_summary
        }
        
        for name, df in tables.items():
            filepath = self.output_path / f"{name}.csv"
            df.to_csv(filepath, index=False)
            logger.info(f"💾 Saved {name}: {len(df)} rows → {filepath}")
        
        # Create summary report
        self.create_summary_report(tables)
        
        return tables
    
    def create_summary_report(self, tables):
        """Create a summary report of all master data"""
        report_path = self.output_path / "master_data_summary.txt"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("NFL MASTER DATA SUMMARY REPORT\n")
            f.write("=" * 50 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("📊 DATA TABLES CREATED:\n")
            f.write("-" * 25 + "\n")
            for name, df in tables.items():
                f.write(f"{name.upper().replace('_', ' ')}: {len(df):,} rows\n")
            
            f.write(f"\n📋 OVERALL STATISTICS:\n")
            f.write("-" * 25 + "\n")
            f.write(f"Total Player Moves: {len(tables['players_master']):,}\n")
            f.write(f"Teams Analyzed: {len(tables['teams_master'])}\n")
            f.write(f"Divisions Covered: {len(tables['division_summary'])}\n")
            f.write(f"Move Types: {len(tables['moves_summary'])}\n")
            f.write(f"Position Groups: {len(tables['position_analysis'])}\n")
            
            f.write(f"\n🏆 KEY INSIGHTS:\n")
            f.write("-" * 25 + "\n")
            top_mover = tables['players_master'].iloc[0]
            best_team = tables['teams_master'].iloc[0]
            f.write(f"Highest Impact Move: {top_mover['player_name']} ({top_mover['impact_score']:.2f})\n")
            f.write(f"Best 2025 Team: {best_team['team']} - {best_team['team_name']}\n")
            f.write(f"Most Active Team: {tables['teams_master'].nlargest(1, 'total_moves').iloc[0]['team']}\n")
            
        logger.info(f"📄 Summary report saved: {report_path}")

def main():
    """Main execution function"""
    print("🏈 NFL Master Data Tables Creator")
    print("=" * 50)
    
    creator = NFLMasterDataCreator()
    tables = creator.generate_all_master_tables()
    
    print(f"\n✅ Master Data Creation Complete!")
    print(f"📁 Output location: {creator.output_path}")
    print(f"🎯 Ready for downstream analysis, visualization, and reporting!")

if __name__ == "__main__":
    main()
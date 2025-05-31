"""
NFL Master Excel Reader
Reads and processes historical NFL betting data from Excel files
"""

import pandas as pd
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFLExcelReader:
    def __init__(self, excel_path: str, config_path: str = None):
        """
        Initialize the Excel reader with team mappings
        
        Args:
            excel_path: Path to the NFL Master Excel file
            config_path: Path to team mappings JSON file
        """
        # Handle relative paths from project root
        project_root = Path(__file__).parent.parent.parent
        
        self.excel_path = project_root / excel_path
        
        if config_path is None:
            config_path = project_root / "config" / "team_mappings.json"
        else:
            config_path = project_root / config_path
            
        self.config_path = config_path
        
        logger.info(f"Excel path: {self.excel_path}")
        logger.info(f"Config path: {self.config_path}")
        
        # Load team mappings
        self.team_mappings = self._load_team_mappings()
        
        # Store loaded data
        self.game_data = {}
        self.betting_data = {}
        self.power_rankings = {}
        
    def _load_team_mappings(self) -> Dict:
        """Load team name mappings from JSON config"""
        try:
            with open(self.config_path, 'r') as f:
                mappings = json.load(f)
                logger.info(f"Loaded {len(mappings)} team mappings")
                return mappings
        except FileNotFoundError:
            logger.warning(f"Team mappings not found at {self.config_path}")
            return {}
            
    def _standardize_team_name(self, team_name: str) -> Optional[str]:
        """
        Convert any team name variation to standardized format
        
        Args:
            team_name: Raw team name from Excel
            
        Returns:
            Standardized team abbreviation or None if not found
        """
        if not team_name or pd.isna(team_name):
            return None
            
        team_name = str(team_name).strip()
        
        # Direct mapping lookup
        for key, mapping in self.team_mappings.items():
            if (team_name == mapping['short_name'] or 
                team_name == mapping['full_name'] or 
                team_name == mapping['abbreviation'] or 
                team_name == mapping['caps']):
                return mapping['abbreviation']
                
        # Fuzzy matching for common variations
        team_lower = team_name.lower()
        for key, mapping in self.team_mappings.items():
            if (key.lower() in team_lower or 
                mapping['short_name'].lower() in team_lower):
                return mapping['abbreviation']
                
        logger.warning(f"Could not standardize team name: {team_name}")
        return team_name
        
    def read_weekly_games(self, year: int, week: str) -> pd.DataFrame:
        """
        Read game data for a specific week
        
        Args:
            year: Season year (e.g., 2023)
            week: Week identifier (e.g., "Week 1", "Wildcard Weekend")
            
        Returns:
            DataFrame with standardized game data
        """
        sheet_name = f"{year} {week}"
        
        try:
            df = pd.read_excel(self.excel_path, sheet_name=sheet_name)
            logger.info(f"Reading {sheet_name}: {len(df)} rows")
            
            # Standardize column names
            df.columns = df.columns.str.strip()
            
            # Core game columns that should exist
            game_columns = {
                'Away Team': 'away_team',
                'Home Team': 'home_team', 
                'Away Tag': 'away_tag',
                'Home Tag': 'home_tag',
                'Opening Line': 'opening_line',
                'Current Line': 'current_line',
                'Closing Line': 'closing_line',
                'Opening Total': 'opening_total',
                'Current Total': 'current_total',
                'Closing Total': 'closing_total'
            }
            
            # Rename columns if they exist
            for old_col, new_col in game_columns.items():
                if old_col in df.columns:
                    df = df.rename(columns={old_col: new_col})
                    
            # Standardize team names
            if 'away_team' in df.columns:
                df['away_team_std'] = df['away_team'].apply(self._standardize_team_name)
            if 'home_team' in df.columns:
                df['home_team_std'] = df['home_team'].apply(self._standardize_team_name)
                
            # Add metadata
            df['year'] = year
            df['week'] = week
            df['sheet_name'] = sheet_name
            
            # Clean numeric columns
            numeric_cols = ['opening_line', 'current_line', 'closing_line', 
                          'opening_total', 'current_total', 'closing_total']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    
            return df
            
        except Exception as e:
            logger.error(f"Error reading {sheet_name}: {e}")
            return pd.DataFrame()
            
    def read_betting_log(self, year: int, player: str = "Dylan") -> pd.DataFrame:
        """
        Read betting performance data for a specific year and player
        
        Args:
            year: Season year
            player: Player name ("Dylan" or "Justin")
            
        Returns:
            DataFrame with betting log data
        """
        sheet_name = f"NFL {year} - {player}"
        
        try:
            df = pd.read_excel(self.excel_path, sheet_name=sheet_name)
            logger.info(f"Reading {sheet_name}: {len(df)} rows")
            
            # Standardize column names
            df.columns = df.columns.str.strip()
            
            # Core betting columns
            betting_columns = {
                'Week': 'week',
                'Game(s)': 'games',
                'Wager': 'wager',
                'Book(s)': 'book',
                'Type': 'bet_type',
                'US Odds': 'us_odds',
                'Price': 'decimal_odds',
                'Stake': 'stake',
                'Result': 'result',
                'Units Won': 'units_won',
                'Running Total': 'running_total',
                'CL': 'closing_line',
                'Imp Prob': 'implied_prob',
                'nvCLV': 'no_vig_clv'
            }
            
            # Rename columns if they exist
            for old_col, new_col in betting_columns.items():
                if old_col in df.columns:
                    df = df.rename(columns={old_col: new_col})
                    
            # Add metadata
            df['year'] = year
            df['player'] = player
            df['sheet_name'] = sheet_name
            
            # Clean numeric columns
            numeric_cols = ['us_odds', 'decimal_odds', 'stake', 'units_won', 
                          'running_total', 'closing_line', 'implied_prob', 'no_vig_clv']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                    
            return df
            
        except Exception as e:
            logger.error(f"Error reading {sheet_name}: {e}")
            return pd.DataFrame()
            
    def get_available_sheets(self) -> List[str]:
        """Get list of all sheet names in the Excel file"""
        try:
            excel_file = pd.ExcelFile(self.excel_path)
            return excel_file.sheet_names
        except Exception as e:
            logger.error(f"Error reading sheet names: {e}")
            return []
            
    def identify_sheet_types(self) -> Dict[str, List[str]]:
        """
        Categorize sheets by type (games, betting logs, power rankings, etc.)
        
        Returns:
            Dictionary mapping sheet types to list of sheet names
        """
        sheets = self.get_available_sheets()
        categorized = {
            'weekly_games': [],
            'betting_logs': [],
            'power_rankings': [],
            'schedules': [],
            'team_pages': [],
            'other': []
        }
        
        for sheet in sheets:
            sheet_lower = sheet.lower()
            
            if 'week' in sheet_lower and any(str(year) in sheet for year in range(2019, 2026)):
                categorized['weekly_games'].append(sheet)
            elif 'nfl' in sheet_lower and ('-' in sheet or 'dylan' in sheet_lower or 'justin' in sheet_lower):
                categorized['betting_logs'].append(sheet)
            elif 'power rank' in sheet_lower:
                categorized['power_rankings'].append(sheet)
            elif 'schedule' in sheet_lower:
                categorized['schedules'].append(sheet)
            elif any(team in sheet for team in ['Cowboys', 'Chiefs', 'Bills', 'Patriots']):
                categorized['team_pages'].append(sheet)
            else:
                categorized['other'].append(sheet)
                
        return categorized


def main():
    """Test the Excel reader with your historical data"""
    
    # Initialize reader (paths relative to project root)
    excel_path = "data/historical/NFL_Master_Historical.xlsx"
    reader = NFLExcelReader(excel_path)
    
    # Test sheet identification
    print("=== Available Sheets ===")
    sheet_types = reader.identify_sheet_types()
    for sheet_type, sheets in sheet_types.items():
        print(f"{sheet_type}: {len(sheets)} sheets")
        if sheets:
            print(f"  Examples: {sheets[:3]}...")
            
    # Test reading specific data
    print("\n=== Testing Data Reading ===")
    
    # Read a recent week
    df_week = reader.read_weekly_games(2023, "Week 1")
    if not df_week.empty:
        print(f"2023 Week 1: {len(df_week)} games")
        if 'away_team_std' in df_week.columns:
            print(df_week[['away_team_std', 'home_team_std', 'closing_line', 'closing_total']].head())
        
    # Read betting performance
    df_betting = reader.read_betting_log(2023, "Dylan")
    if not df_betting.empty:
        print(f"\n2023 Dylan Betting: {len(df_betting)} bets")
        if 'running_total' in df_betting.columns:
            final_total = df_betting['running_total'].dropna().iloc[-1] if not df_betting['running_total'].dropna().empty else 0
            print(f"Final running total: {final_total:.2f} units")


if __name__ == "__main__":
    main()

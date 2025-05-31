"""
NFL CLV (Closing Line Value) Calculator
Automates the calculation of closing line value for betting performance tracking
"""

import pandas as pd
import numpy as np
import json
import os
from pathlib import Path
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFLCLVCalculator:
    def __init__(self, excel_path: str = None):
        """
        Initialize CLV calculator
        
        Args:
            excel_path: Path to Excel file (defaults to current season)
        """
        self.project_root = Path(__file__).parent.parent
        
        if excel_path is None:
            self.excel_path = self.project_root / "data" / "current_season" / "NFL_2025_Season.xlsx"
        else:
            self.excel_path = Path(excel_path)
            
        logger.info(f"CLV Calculator initialized for: {self.excel_path}")
        
    def american_to_decimal(self, american_odds: float) -> float:
        """Convert American odds to decimal odds"""
        if pd.isna(american_odds):
            return np.nan
            
        if american_odds > 0:
            return (american_odds / 100) + 1
        else:
            return (100 / abs(american_odds)) + 1
            
    def decimal_to_american(self, decimal_odds: float) -> float:
        """Convert decimal odds to American odds"""
        if pd.isna(decimal_odds) or decimal_odds <= 1:
            return np.nan
            
        if decimal_odds >= 2:
            return (decimal_odds - 1) * 100
        else:
            return -100 / (decimal_odds - 1)
            
    def odds_to_implied_probability(self, american_odds: float) -> float:
        """Convert American odds to implied probability"""
        if pd.isna(american_odds):
            return np.nan
            
        if american_odds > 0:
            return 100 / (american_odds + 100)
        else:
            return abs(american_odds) / (abs(american_odds) + 100)
            
    def remove_vig_probability(self, prob1: float, prob2: float) -> Tuple[float, float]:
        """
        Remove vig (juice) from two-way betting probabilities
        
        Args:
            prob1: Implied probability of outcome 1
            prob2: Implied probability of outcome 2
            
        Returns:
            Tuple of no-vig probabilities
        """
        if pd.isna(prob1) or pd.isna(prob2):
            return np.nan, np.nan
            
        total_prob = prob1 + prob2
        if total_prob <= 1:
            return prob1, prob2  # Already no vig
            
        # Remove proportional vig
        no_vig_prob1 = prob1 / total_prob
        no_vig_prob2 = prob2 / total_prob
        
        return no_vig_prob1, no_vig_prob2
        
    def calculate_clv_for_bet(self, bet_odds: float, closing_line: float, 
                             opposite_closing_line: float = None, bet_type: str = "side") -> Dict:
        """
        Calculate CLV for a single bet
        
        Args:
            bet_odds: The odds when the bet was placed
            closing_line: The closing line for the same bet
            opposite_closing_line: The closing line for the opposite side
            bet_type: Type of bet ("side", "total", "moneyline")
            
        Returns:
            Dictionary with CLV calculations
        """
        result = {
            'bet_odds': bet_odds,
            'closing_line': closing_line,
            'bet_implied_prob': self.odds_to_implied_probability(bet_odds),
            'closing_implied_prob': self.odds_to_implied_probability(closing_line),
            'raw_clv': np.nan,
            'no_vig_clv': np.nan,
            'clv_percentage': np.nan
        }
        
        # Calculate basic CLV (difference in implied probabilities)
        if not pd.isna(result['bet_implied_prob']) and not pd.isna(result['closing_implied_prob']):
            result['raw_clv'] = result['closing_implied_prob'] - result['bet_implied_prob']
            result['clv_percentage'] = (result['raw_clv'] / result['bet_implied_prob']) * 100
        
        # Calculate no-vig CLV if we have opposite line
        if opposite_closing_line is not None and not pd.isna(opposite_closing_line):
            opp_closing_prob = self.odds_to_implied_probability(opposite_closing_line)
            
            if not pd.isna(opp_closing_prob) and not pd.isna(result['closing_implied_prob']):
                no_vig_closing, _ = self.remove_vig_probability(
                    result['closing_implied_prob'], opp_closing_prob
                )
                
                if not pd.isna(no_vig_closing) and not pd.isna(result['bet_implied_prob']):
                    result['no_vig_clv'] = no_vig_closing - result['bet_implied_prob']
        
        return result
        
    def update_betting_log_clv(self, sheet_name: str, save_file: bool = True) -> pd.DataFrame:
        """
        Update CLV calculations for a betting log sheet
        
        Args:
            sheet_name: Name of the betting log sheet (e.g., "NFL 2025 - Dylan")
            save_file: Whether to save the updated Excel file
            
        Returns:
            Updated DataFrame with CLV calculations
        """
        logger.info(f"Calculating CLV for {sheet_name}...")
        
        try:
            # Read the betting log
            df = pd.read_excel(self.excel_path, sheet_name=sheet_name)
            logger.info(f"Loaded {len(df)} betting records")
            
            # Initialize CLV columns if they don't exist
            clv_columns = ['CL', 'Imp Prob', 'OCL', 'Imp Prob.1', 'nvCLV', 'phony CLV']
            for col in clv_columns:
                if col not in df.columns:
                    df[col] = np.nan
                    
            # Process each bet
            for idx, row in df.iterrows():
                if pd.isna(row.get('US Odds')) or row.get('Result') is None:
                    continue  # Skip incomplete rows
                    
                bet_odds = row['US Odds']
                
                # Try to find closing line - this would need to be populated from game sheets
                # For now, we'll work with what's already in the sheet
                closing_line = row.get('CL')
                opposite_closing_line = row.get('OCL')
                
                if not pd.isna(closing_line):
                    clv_calc = self.calculate_clv_for_bet(
                        bet_odds, closing_line, opposite_closing_line
                    )
                    
                    # Update the DataFrame
                    df.at[idx, 'Imp Prob'] = clv_calc['closing_implied_prob']
                    if not pd.isna(clv_calc['no_vig_clv']):
                        df.at[idx, 'nvCLV'] = clv_calc['no_vig_clv']
                    if not pd.isna(clv_calc['raw_clv']):
                        df.at[idx, 'phony CLV'] = clv_calc['raw_clv']
                        
            # Calculate summary statistics
            total_bets = len(df[df['Result'].notna() & df['Result'] != '#N/A'])
            avg_clv = df['nvCLV'].mean()
            positive_clv_rate = (df['nvCLV'] > 0).sum() / total_bets if total_bets > 0 else 0
            
            logger.info(f"CLV Summary for {sheet_name}:")
            logger.info(f"  Total bets: {total_bets}")
            logger.info(f"  Average CLV: {avg_clv:.4f}")
            logger.info(f"  Positive CLV rate: {positive_clv_rate:.2%}")
            
            # Save updated file if requested
            if save_file:
                self._save_updated_sheet(df, sheet_name)
                
            return df
            
        except Exception as e:
            logger.error(f"Error calculating CLV for {sheet_name}: {e}")
            return pd.DataFrame()
            
    def _save_updated_sheet(self, df: pd.DataFrame, sheet_name: str):
        """Save updated DataFrame back to Excel file"""
        try:
            # Read all sheets
            with pd.ExcelFile(self.excel_path) as xls:
                all_sheets = {name: pd.read_excel(xls, name) for name in xls.sheet_names}
            
            # Update the specific sheet
            all_sheets[sheet_name] = df
            
            # Write all sheets back
            with pd.ExcelWriter(self.excel_path, engine='openpyxl') as writer:
                for name, sheet_df in all_sheets.items():
                    sheet_df.to_excel(writer, sheet_name=name, index=False)
                    
            logger.info(f"Updated {sheet_name} in {self.excel_path}")
            
        except Exception as e:
            logger.error(f"Error saving updated sheet: {e}")
            
    def populate_closing_lines_from_games(self, week: str, year: int = 2025) -> Dict:
        """
        Populate closing lines by reading from weekly game sheets
        
        Args:
            week: Week identifier (e.g., "Week 1")
            year: Season year
            
        Returns:
            Dictionary mapping games to closing lines
        """
        sheet_name = f"{year} {week}"
        closing_lines = {}
        
        try:
            df = pd.read_excel(self.excel_path, sheet_name=sheet_name)
            
            for _, row in df.iterrows():
                if pd.notna(row.get('Away Team')) and pd.notna(row.get('Home Team')):
                    game_key = f"{row['Away Team']} @ {row['Home Team']}"
                    
                    closing_lines[game_key] = {
                        'spread': row.get('Closing Line'),
                        'total': row.get('Closing Total'),
                        'away_ml': None,  # Would need moneyline data
                        'home_ml': None
                    }
                    
            logger.info(f"Extracted closing lines for {len(closing_lines)} games from {sheet_name}")
            return closing_lines
            
        except Exception as e:
            logger.error(f"Error reading closing lines from {sheet_name}: {e}")
            return {}
            
    def calculate_season_clv_summary(self, players: List[str] = ["Dylan", "Justin"]) -> Dict:
        """
        Calculate CLV summary for the entire season
        
        Args:
            players: List of player names to analyze
            
        Returns:
            Dictionary with season CLV statistics
        """
        season_summary = {}
        
        for player in players:
            sheet_name = f"NFL 2025 - {player}"
            
            try:
                df = self.update_betting_log_clv(sheet_name, save_file=False)
                
                if not df.empty:
                    # Filter to actual bets (not placeholders)
                    actual_bets = df[
                        df['Result'].notna() & 
                        (df['Result'] != '#N/A') & 
                        df['nvCLV'].notna()
                    ]
                    
                    if len(actual_bets) > 0:
                        season_summary[player] = {
                            'total_bets': len(actual_bets),
                            'avg_clv': actual_bets['nvCLV'].mean(),
                            'median_clv': actual_bets['nvCLV'].median(),
                            'std_clv': actual_bets['nvCLV'].std(),
                            'positive_clv_rate': (actual_bets['nvCLV'] > 0).mean(),
                            'total_units_won': actual_bets['Units Won'].sum(),
                            'running_total': actual_bets['Running Total'].iloc[-1] if len(actual_bets) > 0 else 0
                        }
                    else:
                        season_summary[player] = {'total_bets': 0}
                        
            except Exception as e:
                logger.error(f"Error calculating season summary for {player}: {e}")
                season_summary[player] = {'error': str(e)}
                
        return season_summary


def main():
    """Test the CLV calculator"""
    
    print("📊 NFL CLV Calculator")
    print("====================")
    
    # Initialize calculator
    calc = NFLCLVCalculator()
    
    # Test with current season file
    if calc.excel_path.exists():
        print(f"✅ Found Excel file: {calc.excel_path}")
        
        # Calculate CLV for betting logs
        for player in ["Dylan", "Justin"]:
            sheet_name = f"NFL 2025 - {player}"
            print(f"\n📈 Calculating CLV for {player}...")
            
            df = calc.update_betting_log_clv(sheet_name)
            
            if not df.empty:
                actual_bets = df[df['Result'].notna() & (df['Result'] != '#N/A')]
                print(f"   Processed {len(actual_bets)} bets")
            else:
                print(f"   No betting data found")
                
        # Generate season summary
        print(f"\n📋 Season CLV Summary:")
        summary = calc.calculate_season_clv_summary()
        
        for player, stats in summary.items():
            print(f"\n{player}:")
            if 'total_bets' in stats and stats['total_bets'] > 0:
                print(f"  Total bets: {stats['total_bets']}")
                print(f"  Average CLV: {stats['avg_clv']:.4f}")
                print(f"  Positive CLV rate: {stats['positive_clv_rate']:.2%}")
                print(f"  Running total: {stats['running_total']:.2f} units")
            else:
                print(f"  No betting data yet")
                
    else:
        print(f"❌ Excel file not found: {calc.excel_path}")
        print("Run the season setup script first!")
        
    print(f"\n🎯 CLV Calculator ready for the 2025 season!")


if __name__ == "__main__":
    main()

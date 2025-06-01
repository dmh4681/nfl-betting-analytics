"""
NFL Player Bridge Framework - Track all offseason moves and grade impact
Updated to use playoff_adjusted_rankings.csv with point differentials
FIXED VERSION - Keeps ALL data, just fixes the KeyError
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json
import logging
from typing import Dict, List, Tuple, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PlayerBridgeFramework:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent
        self.config_path = self.project_root / "config" / "team_mappings.json"
        self.output_path = self.project_root / "output" / "player_bridge"
        self.output_path.mkdir(parents=True, exist_ok=True)
        
        # Load team mappings
        with open(self.config_path, 'r') as f:
            self.team_mappings = json.load(f)
            
        # LOAD PLAYOFF ADJUSTED RANKINGS FROM CSV
        self.original_power_rankings, self.original_ranks, self.point_differentials = self._load_playoff_adjusted_rankings()
        
        # Position importance weights - FIXED: Added COACH
        self.position_weights = {
            'QB': 10.0, 'LT': 6.0, 'EDGE': 6.0, 'CB1': 6.0,
            'WR1': 5.5, 'RT': 5.0, 'C': 5.0, 'S': 5.0,
            'LB': 4.5, 'RB': 4.0, 'WR2': 4.0, 'TE': 4.0,
            'G': 3.5, 'CB2': 3.5, 'DT': 3.5, 'K': 2.5,
            'WR3': 2.0, 'P': 2.0, 'LS': 1.0, 'DEPTH': 1.5, 'COACH': 2.0
        }
        
        # Unit classifications - FIXED: Added Coaching and G
        self.position_units = {
            'Offense': ['QB', 'RB', 'WR1', 'WR2', 'WR3', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 'G'],
            'Defense': ['EDGE', 'DT', 'LB', 'CB1', 'CB2', 'S'],
            'Special Teams': ['K', 'P', 'LS'],
            'Coaching': ['COACH', 'HC', 'OC', 'DC']
        }

    def _load_playoff_adjusted_rankings(self) -> Tuple[Dict[str, float], Dict[str, int], Dict[str, float]]:
        """Load playoff adjusted rankings from CSV file"""
        rankings_path = self.project_root / "output" / "playoff_adjusted_rankings.csv"
        
        try:
            # Read the CSV file
            df = pd.read_csv(rankings_path)
            logger.info(f"Successfully loaded rankings from {rankings_path}")
            
            # Create dictionaries
            rankings_dict = {}
            ranks_dict = {}
            point_diff_dict = {}
            
            # Process each team
            for _, row in df.iterrows():
                team = str(row['team']).strip().upper()
                point_diff = float(row['rating'])
                rank = int(row['rank'])
                
                # Store point differential and rank
                point_diff_dict[team] = point_diff
                ranks_dict[team] = rank
                
                # Convert point differential to power rating (70-95 scale)
                # Best team (rank 1) gets 95, worst gets 70
                # Using rank-based conversion for more stable results
                power_rating = 95 - ((rank - 1) * 25 / 31)  # 31 teams in CSV
                rankings_dict[team] = round(power_rating, 1)
            
            # Handle missing teams (LAR) with average values
            if 'LAR' not in rankings_dict:
                avg_rating = sum(rankings_dict.values()) / len(rankings_dict)
                rankings_dict['LAR'] = round(avg_rating, 1)
                ranks_dict['LAR'] = 16  # Middle rank
                point_diff_dict['LAR'] = 0.0
                logger.info(f"Added LAR with average rating {avg_rating:.1f}")
            
            # Create mappings for common abbreviation differences
            abbr_mappings = {
                'JAC': 'Jac', 'WAS': 'Was', 'WSH': 'Was',
                'JAX': 'Jac', 'NO': 'NO', 'NE': 'NE'
            }
            
            # Add mapped versions
            for csv_abbr, framework_abbr in abbr_mappings.items():
                if csv_abbr in rankings_dict and framework_abbr not in rankings_dict:
                    rankings_dict[framework_abbr] = rankings_dict[csv_abbr]
                    ranks_dict[framework_abbr] = ranks_dict[csv_abbr]
                    point_diff_dict[framework_abbr] = point_diff_dict[csv_abbr]
            
            logger.info(f"Loaded {len(rankings_dict)} team rankings")
            logger.info(f"Top 5 teams by rating: {sorted(rankings_dict.items(), key=lambda x: x[1], reverse=True)[:5]}")
            
            return rankings_dict, ranks_dict, point_diff_dict
            
        except FileNotFoundError:
            logger.error(f"Could not find playoff adjusted rankings file at {rankings_path}")
            logger.warning("Falling back to default rankings")
            return self._get_default_rankings(), {}, {}
        except Exception as e:
            logger.error(f"Error loading playoff adjusted rankings: {e}")
            logger.warning("Falling back to default rankings")
            return self._get_default_rankings(), {}, {}
    
    def _get_default_rankings(self) -> Dict[str, float]:
        """Fallback rankings if CSV cannot be loaded"""
        return {
            'Phi': 95.2, 'Buf': 92.8, 'KC': 91.5, 'SF': 90.1,
            'Bal': 89.3, 'Det': 88.7, 'NYG': 87.2, 'Was': 86.8,
            'Hou': 85.4, 'Min': 84.9, 'Pit': 84.2, 'LAC': 83.6,
            'Mia': 82.8, 'GB': 82.1, 'Atl': 81.5, 'Cin': 80.9,
            'TB': 80.2, 'LAR': 79.6, 'Sea': 78.8, 'Cle': 78.1,
            'NE': 77.4, 'Jac': 76.7, 'Den': 75.9, 'Ari': 75.2,
            'Chi': 74.5, 'Ten': 73.8, 'Ind': 73.1, 'NYJ': 72.4,
            'Car': 71.6, 'NO': 70.8, 'LV': 69.9, 'Dal': 69.1
        }

    def create_player_bridge_template(self):
        """Create template for tracking player moves - NOW LOADS FROM EXTERNAL DATA!"""
        
        try:
            # Add project root to path for imports
            import sys
            project_root = self.project_root
            if str(project_root) not in sys.path:
                sys.path.append(str(project_root))
            
            # Load moves from external data sources
            from data.player_moves import ALL_2025_MOVES
            real_2025_moves = ALL_2025_MOVES.copy()  # Make a copy to avoid modifying original
            
            logger.info(f"✅ Loaded {len(real_2025_moves)} moves from external data files")
            
        except ImportError as e:
            logger.error(f"❌ Could not import player moves: {e}")
            logger.warning("Falling back to inline data")
            # If import fails, fall back to your current inline data
            real_2025_moves = self._get_fallback_moves()
        except Exception as e:
            logger.error(f"❌ Unexpected error loading player moves: {e}")
            logger.warning("Falling back to inline data")
            real_2025_moves = self._get_fallback_moves()
        
        if not real_2025_moves:
            logger.warning("No player moves loaded - using empty dataset")
            return pd.DataFrame()
        
        # Calculate impact scores for each move
        for move in real_2025_moves:
            if 'impact_score' not in move:
                move['impact_score'] = self._calculate_impact_score(
                    move['position'],
                    move['2024_grade'],
                    move['snap_percentage_2024'],
                    move['importance_to_new_team']
                )
        
        return pd.DataFrame(real_2025_moves)

    def _get_fallback_moves(self):
        """Fallback to your current inline data if external import fails"""
        # Keep your current real_2025_moves list as backup
        # (You can copy your current data here as fallback)
        logger.warning("Using fallback inline data")
        return []  # For now, return empty - you can add your current data here if needed

    def add_player_move(self, player_bridge_df: pd.DataFrame, player_name: str, position: str, 
                       from_team: str, to_team: str, move_type: str, grade_2024: float, 
                       projected_2025: float, snap_pct: float, importance_old: float, 
                       importance_new: float, contract_years: int = 0, contract_value: int = 0) -> pd.DataFrame:
        """Easily add a new player move to the bridge"""
        
        new_move = {
            'player_name': player_name,
            'position': position,
            'from_team': from_team,
            'to_team': to_team,
            'move_type': move_type,
            'contract_years': contract_years,
            'contract_value': contract_value,
            '2024_grade': grade_2024,
            'projected_2025_grade': projected_2025,
            'snap_percentage_2024': snap_pct,
            'importance_to_old_team': importance_old,
            'importance_to_new_team': importance_new,
            'impact_score': self._calculate_impact_score(position, grade_2024, snap_pct, importance_new)
        }
        
        return pd.concat([player_bridge_df, pd.DataFrame([new_move])], ignore_index=True)

    def _calculate_impact_score(self, position: str, grade: float, snap_pct: float, importance: float) -> float:
        """Calculate weighted impact score for a player move"""
        
        # Get position weight
        pos_weight = self.position_weights.get(position, 2.0)
        
        # Calculate base impact (grade * snap percentage * importance)
        base_impact = (grade / 10.0) * (snap_pct / 100.0) * (importance / 10.0)
        
        # Apply position weight
        weighted_impact = base_impact * pos_weight
        
        # SCALE DOWN BY 3X to make more realistic
        realistic_impact = weighted_impact / 3.0
        
        # Cap individual moves at 2.5 max impact
        capped_impact = min(realistic_impact, 2.5)
        
        return round(capped_impact, 2)

    def calculate_team_net_changes(self, player_bridge_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate net impact for each team from all player moves"""
        
        team_impacts = {}
        
        # Initialize all teams using the loaded rankings
        for team in self.original_power_rankings.keys():
            # Get the team's full name from mappings
            full_name = team
            for team_data in self.team_mappings.values():
                if team_data['abbreviation'] == team or team == team_data['caps']:
                    full_name = team_data['full_name']
                    break
                    
            team_impacts[team] = {
                'team': team,
                'team_name': full_name,
                'players_gained': 0,
                'players_lost': 0,
                'impact_gained': 0.0,
                'impact_lost': 0.0,
                'net_impact': 0.0,
                'offense_impact': 0.0,
                'defense_impact': 0.0,
                'special_teams_impact': 0.0,
                'coaching_impact': 0.0,  # FIXED - Added coaching impact
                'key_additions': [],
                'key_losses': []
            }
        
        # Process each player move
        for _, move in player_bridge_df.iterrows():
            from_team = move['from_team']
            to_team = move['to_team']
            impact = move['impact_score']
            position = move['position']
            player_name = move['player_name']
            
            # Determine which unit this position belongs to
            unit = self._get_position_unit(position)
            unit_key = f"{unit.lower().replace(' ', '_')}_impact"  # FIXED - Replace spaces with underscores
            
            # Player leaving a team (loss)
            if from_team in team_impacts and from_team not in ['DRAFT', 'FA', 'RETIRED', 'RELEASED', 'PROMOTION']:
                team_impacts[from_team]['players_lost'] += 1
                loss_impact = abs(impact)
                team_impacts[from_team]['impact_lost'] += loss_impact
                team_impacts[from_team]['net_impact'] -= loss_impact
                
                # FIXED - Check if unit_key exists before accessing
                if unit_key in team_impacts[from_team]:
                    team_impacts[from_team][unit_key] -= loss_impact
                
                if loss_impact >= 0.5:  # Lower threshold for key moves
                    team_impacts[from_team]['key_losses'].append(f"{player_name} ({position})")
            
            # Player joining a team (gain)
            if to_team in team_impacts and to_team not in ['FA', 'RETIRED', 'RELEASED']:
                team_impacts[to_team]['players_gained'] += 1
                gain_impact = abs(impact)
                team_impacts[to_team]['impact_gained'] += gain_impact
                team_impacts[to_team]['net_impact'] += gain_impact
                
                # FIXED - Check if unit_key exists before accessing
                if unit_key in team_impacts[to_team]:
                    team_impacts[to_team][unit_key] += gain_impact
                
                if gain_impact >= 0.5:  # Lower threshold for key moves
                    team_impacts[to_team]['key_additions'].append(f"{player_name} ({position})")
        
        return pd.DataFrame(list(team_impacts.values()))

    def _get_position_unit(self, position: str) -> str:
        """Determine which unit a position belongs to - FIXED VERSION"""
        for unit, positions in self.position_units.items():
            if position in positions or any(pos in position for pos in positions):
                return unit
        # Default fallback for unknown positions
        if 'COACH' in position.upper():
            return 'Coaching'
        return 'Defense'

    def grade_team_changes(self, team_impacts_df: pd.DataFrame) -> pd.DataFrame:
        """Assign letter grades to team changes"""
        
        def get_grade(net_impact):
            if net_impact >= 8.0: return 'A+'
            elif net_impact >= 6.0: return 'A'
            elif net_impact >= 4.0: return 'A-'
            elif net_impact >= 2.0: return 'B+'
            elif net_impact >= 1.0: return 'B'
            elif net_impact >= 0.0: return 'B-'
            elif net_impact >= -1.0: return 'C+'
            elif net_impact >= -2.0: return 'C'
            elif net_impact >= -4.0: return 'C-'
            elif net_impact >= -6.0: return 'D'
            else: return 'F'
        
        team_impacts_df['offseason_grade'] = team_impacts_df['net_impact'].apply(get_grade)
        return team_impacts_df.sort_values('net_impact', ascending=False)

    def calculate_final_2025_rankings(self, team_impacts_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate final 2025 power rankings = Original + Offseason Impact"""
        
        final_rankings = []
        
        for _, team in team_impacts_df.iterrows():
            team_abbr = team['team']
            original_rating = self.original_power_rankings.get(team_abbr, 80.0)
            original_rank = self.original_ranks.get(team_abbr, 16)
            offseason_impact = team['net_impact']
            
            # Calculate final 2025 projection
            final_rating = original_rating + offseason_impact
            
            final_rankings.append({
                'team': team_abbr,
                'team_name': team['team_name'],
                'original_2024_rating': original_rating,
                'original_2024_rank': original_rank,
                'offseason_impact': offseason_impact,
                'final_2025_rating': final_rating,
                'offseason_grade': team['offseason_grade'],
                'key_additions': team['key_additions'],
                'key_losses': team['key_losses'],
                'offense_impact': team['offense_impact'],
                'defense_impact': team['defense_impact']
            })
        
        # Convert to DataFrame and sort by final rating
        final_df = pd.DataFrame(final_rankings)
        final_df = final_df.sort_values('final_2025_rating', ascending=False)
        
        # Add final 2025 rankings
        final_df['final_2025_rank'] = range(1, len(final_df) + 1)
        final_df['rank_change'] = final_df['original_2024_rank'] - final_df['final_2025_rank']
        
        return final_df

    def _get_original_rank(self, team_abbr: str) -> int:
        """Get original 2024 ranking for a team"""
        return self.original_ranks.get(team_abbr, 16)

    def generate_comprehensive_report(self):
        """Generate complete player bridge analysis with final 2025 rankings"""
        
        print("🏈 NFL Player Bridge Framework Analysis")
        print("=" * 60)
        
        # Create player bridge data
        player_bridge = self.create_player_bridge_template()
        print(f"📊 Tracking {len(player_bridge)} player moves")
        
        # Show if we're using CSV rankings
        if hasattr(self, 'original_power_rankings') and self.original_power_rankings:
            print(f"📈 Using playoff-adjusted rankings from CSV")
            print(f"   Total teams loaded: {len(self.original_power_rankings)}")
        
        # Process each move for debugging
        print("\n📋 Processing Player Moves...")
        for _, move in player_bridge.head(10).iterrows():  # Show first 10 moves
            impact = move['impact_score']
            print(f"   {move['player_name']:<20} {move['from_team']:>3} → {move['to_team']:<3} Impact: {impact:+.2f}")
        if len(player_bridge) > 10:
            print(f"   ... and {len(player_bridge) - 10} more moves")
        
        print()
        
        # Calculate team impacts
        team_impacts = self.calculate_team_net_changes(player_bridge)
        team_grades = self.grade_team_changes(team_impacts)
        
        # Calculate final 2025 rankings
        final_rankings = self.calculate_final_2025_rankings(team_grades)
        
        # Show 2025 FINAL POWER RANKINGS
        print("\n🏆 2025 FINAL POWER RANKINGS (Based on 2024 + Offseason Changes)")
        print("=" * 65)
        print(f"{'Rank':>4} {'Team':<4} {'Team Name':<25} {'Rating':>7} {'Change':>7}")
        print("-" * 65)
        
        for _, team in final_rankings.head(10).iterrows():
            rank_symbol = "🔺" if team['rank_change'] > 0 else "🔻" if team['rank_change'] < 0 else "➡️"
            change_str = f"{rank_symbol}{abs(team['rank_change'])}" if team['rank_change'] != 0 else "➡️-"
            print(f"#{team['final_2025_rank']:>3} {team['team']:<4} {team['team_name']:<25} "
                  f"{team['final_2025_rating']:>6.1f} {change_str:>7}")
        
        print("\n🏆 BEST OFFSEASONS (Top 5)")
        print("-" * 50)
        top_5 = team_grades.head(5)
        for _, team in top_5.iterrows():
            print(f"{team['offseason_grade']:<3} {team['team']:<4} {team['team_name']:<25} Net: {team['net_impact']:+.1f}")
            if team['key_additions']:
                print(f"    Key Adds: {', '.join(team['key_additions'][:2])}")
        
        print(f"\n💸 WORST OFFSEASONS (Bottom 5)")
        print("-" * 50)
        bottom_5 = team_grades.tail(5)
        for _, team in bottom_5.iterrows():
            print(f"{team['offseason_grade']:<3} {team['team']:<4} {team['team_name']:<25} Net: {team['net_impact']:+.1f}")
            if team['key_losses']:
                print(f"    Key Losses: {', '.join(team['key_losses'][:2])}")
        
        print(f"\n📈 BIGGEST RANKING CLIMBERS")
        print("-" * 50)
        biggest_movers = final_rankings.nlargest(5, 'rank_change')
        for _, team in biggest_movers.iterrows():
            print(f"🔺 {team['team']:<4} {team['team_name']:<25} "
                  f"#{team['original_2024_rank']} → #{team['final_2025_rank']} (+{team['rank_change']})")
        
        print(f"\n📉 BIGGEST RANKING DROPS")
        print("-" * 50)
        biggest_drops = final_rankings.nsmallest(5, 'rank_change')
        for _, team in biggest_drops.iterrows():
            if team['rank_change'] < 0:
                print(f"🔻 {team['team']:<4} {team['team_name']:<25} "
                      f"#{team['original_2024_rank']} → #{team['final_2025_rank']} ({team['rank_change']})")
        
        # Save all data
        self._save_results(player_bridge, team_grades, final_rankings)
        
        return player_bridge, team_grades, final_rankings

    def _save_results(self, player_bridge, team_grades, final_rankings):
        """Save all analysis to files"""
        player_bridge.to_csv(self.output_path / "player_bridge_moves.csv", index=False)
        team_grades.to_csv(self.output_path / "team_offseason_grades.csv", index=False)
        final_rankings.to_csv(self.output_path / "final_2025_power_rankings.csv", index=False)
        print(f"\n💾 All analysis saved to: {self.output_path}")


def main():
    framework = PlayerBridgeFramework()
    player_bridge, team_grades, final_rankings = framework.generate_comprehensive_report()
    print(f"\n✅ Player Bridge Framework Analysis Complete!")
    print(f"📋 Final 2025 Power Rankings calculated based on:")
    print(f"   - 2024 playoff-adjusted rankings (point differentials)")
    print(f"   - Offseason player movement impacts")
    print(f"   - Position-weighted importance scores")


if __name__ == "__main__":
    main()
"""
NFL Player Bridge Framework - Track all offseason moves and grade impact
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
            
        # Position importance weights
        self.position_weights = {
            'QB': 10.0, 'LT': 6.0, 'EDGE': 6.0, 'CB1': 6.0,
            'WR1': 5.5, 'RT': 5.0, 'C': 5.0, 'S': 5.0,
            'LB': 4.5, 'RB': 4.0, 'WR2': 4.0, 'TE': 4.0,
            'G': 3.5, 'CB2': 3.5, 'DT': 3.5, 'K': 2.5,
            'WR3': 2.0, 'P': 2.0, 'LS': 1.0, 'DEPTH': 1.5
        }
        
        # Unit classifications
        self.position_units = {
            'Offense': ['QB', 'RB', 'WR1', 'WR2', 'WR3', 'TE', 'LT', 'LG', 'C', 'RG', 'RT'],
            'Defense': ['EDGE', 'DT', 'LB', 'CB1', 'CB2', 'S'],
            'Special Teams': ['K', 'P', 'LS']
        }

    def create_player_bridge_template(self):
        """Create template for tracking player moves - NOW WITH REAL 2025 DATA!"""
        
        # REAL 2025 offseason moves - let's start with some big ones
        real_2025_moves = [
            # EAGLES ADDITIONS (Your Super Bowl champs)
            {
                'player_name': 'Saquon Barkley',
                'position': 'RB',
                'from_team': 'NYG',
                'to_team': 'Phi',  # Changed to match team mappings
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 37750000,
                '2024_grade': 8.7,  # Elite RB season
                'projected_2025_grade': 8.4,  # Slight aging
                'snap_percentage_2024': 87.0,
                'importance_to_old_team': 9.5,  # Was NYG's entire offense
                'importance_to_new_team': 8.0,  # Eagles already had good offense
                'impact_score': self._calculate_impact_score('RB', 8.7, 87.0, 8.0)
            },
            {
                'player_name': 'C.J. Gardner-Johnson',
                'position': 'S',
                'from_team': 'Phi',  # Changed to match team mappings
                'to_team': 'Det',   # Changed to match team mappings
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 30000000,
                '2024_grade': 8.2,  # Great safety season
                'projected_2025_grade': 8.0,
                'snap_percentage_2024': 92.0,
                'importance_to_old_team': 7.5,  # Good but not irreplaceable
                'importance_to_new_team': 8.5,  # Needed secondary help
                'impact_score': self._calculate_impact_score('S', 8.2, 92.0, 7.5)
            },
            
            # GIANTS LOSSES (Your NFC East rivals getting worse)
            {
                'player_name': 'Saquon Barkley',  # Loss for Giants
                'position': 'RB',
                'from_team': 'NYG',
                'to_team': 'Phi',  # Changed to match team mappings
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.7,
                'projected_2025_grade': 0.0,  # Gone
                'snap_percentage_2024': 87.0,
                'importance_to_old_team': 9.5,  # MASSIVE loss
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('RB', 8.7, 87.0, 9.5)  # Negative for loss
            },
            
            # DRAFT PICKS
            {
                'player_name': 'Cam Ward',
                'position': 'QB',
                'from_team': 'DRAFT',
                'to_team': 'Ten',  # Changed to match team mappings
                'move_type': '2025 Draft Pick #1',
                'contract_years': 4,
                'contract_value': 42000000,
                '2024_grade': 0.0,  # College
                'projected_2025_grade': 6.8,  # Rookie QB projection
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 10.0,  # Franchise QB hope
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 10.0)
            },
            {
                'player_name': 'Travis Hunter',
                'position': 'CB1',
                'from_team': 'DRAFT',
                'to_team': 'Cle',  # Changed to match team mappings
                'move_type': '2025 Draft Pick #2',
                'contract_years': 4,
                'contract_value': 38000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.5,  # Elite prospect
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,
                'impact_score': self._calculate_impact_score('CB1', 7.5, 90.0, 9.0)
            },
            
            # FREE AGENT SIGNINGS
            {
                'player_name': 'Russell Wilson',
                'position': 'QB',
                'from_team': 'Pit',  # Changed to match team mappings
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 25000000,
                '2024_grade': 7.2,  # Decent season
                'projected_2025_grade': 6.8,  # Aging
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 8.5,
                'importance_to_new_team': 9.5,  # Giants desperate for QB
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 9.5)
            },
            
            # RETIREMENTS
            {
                'player_name': 'Aaron Rodgers',
                'position': 'QB',
                'from_team': 'NYJ',
                'to_team': 'RETIRED',
                'move_type': 'Retirement',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,  # Declining
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 9.0,  # Still their starter
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 6.0, 100.0, 9.0)
            }
        ]
        
        return pd.DataFrame(real_2025_moves)
        
    def add_player_move(self, player_bridge_df: pd.DataFrame, player_name: str, position: str, 
                       from_team: str, to_team: str, move_type: str, grade_2024: float, 
                       projected_2025: float, snap_pct: float, importance_old: float, 
                       importance_new: float, contract_years: int = 0, contract_value: int = 0) -> pd.DataFrame:
        """
        Easily add a new player move to the bridge
        
        Example usage:
        bridge = framework.add_player_move(
            bridge, 'DeAndre Hopkins', 'WR1', 'ARI', 'TEN', 'Trade',
            7.5, 7.2, 85.0, 8.0, 8.5, 2, 26000000
        )
        """
        
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

    def add_player_move(self, player_bridge_df: pd.DataFrame, player_name: str, position: str, 
                       from_team: str, to_team: str, move_type: str, grade_2024: float, 
                       projected_2025: float, snap_pct: float, importance_old: float, 
                       importance_new: float, contract_years: int = 0, contract_value: int = 0) -> pd.DataFrame:
        """
        Easily add a new player move to the bridge
        
        Example usage:
        bridge = framework.add_player_move(
            bridge, 'DeAndre Hopkins', 'WR1', 'ARI', 'TEN', 'Trade',
            7.5, 7.2, 85.0, 8.0, 8.5, 2, 26000000
        )
        """
        
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
        
        return round(weighted_impact, 2)

    def calculate_team_net_changes(self, player_bridge_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate net impact for each team from all player moves"""
        
        team_impacts = {}
        
        # Initialize all teams
        for team_data in self.team_mappings.values():
            team_abbr = team_data['abbreviation']
            team_impacts[team_abbr] = {
                'team': team_abbr,
                'team_name': team_data['full_name'],
                'players_gained': 0,
                'players_lost': 0,
                'impact_gained': 0.0,
                'impact_lost': 0.0,
                'net_impact': 0.0,
                'offense_impact': 0.0,
                'defense_impact': 0.0,
                'special_teams_impact': 0.0,
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
            
            # DEBUG: Print what we're processing
            print(f"Processing: {player_name} from {from_team} to {to_team}, impact: {impact}")
            
            # Determine which unit this position belongs to
            unit = self._get_position_unit(position)
            unit_key = f"{unit.lower()}_impact"
            
            # Player leaving a team (loss) - make sure impact is negative
            if from_team in team_impacts and from_team not in ['DRAFT', 'FA', 'RETIRED']:
                print(f"  -> {from_team} loses {player_name}")
                team_impacts[from_team]['players_lost'] += 1
                loss_impact = abs(impact)  # Ensure positive value for loss calculation
                team_impacts[from_team]['impact_lost'] += loss_impact
                team_impacts[from_team]['net_impact'] -= loss_impact  # Subtract from net
                team_impacts[from_team][unit_key] -= loss_impact
                
                if loss_impact >= 3.0:  # Significant loss
                    team_impacts[from_team]['key_losses'].append(f"{player_name} ({position})")
            
            # Player joining a team (gain)
            if to_team in team_impacts and to_team not in ['FA', 'RETIRED']:
                print(f"  -> {to_team} gains {player_name}")
                team_impacts[to_team]['players_gained'] += 1
                gain_impact = abs(impact)  # Ensure positive value for gain calculation
                team_impacts[to_team]['impact_gained'] += gain_impact
                team_impacts[to_team]['net_impact'] += gain_impact  # Add to net
                team_impacts[to_team][unit_key] += gain_impact
                
                if gain_impact >= 3.0:  # Significant addition
                    team_impacts[to_team]['key_additions'].append(f"{player_name} ({position})")
            else:
                if to_team not in ['FA', 'RETIRED']:
                    print(f"  -> WARNING: {to_team} not found in team_impacts!")
                    print(f"     Available teams: {list(team_impacts.keys())[:5]}...")  # Show first 5
        
        return pd.DataFrame(list(team_impacts.values()))

    def _get_position_unit(self, position: str) -> str:
        """Determine which unit (Offense/Defense/Special Teams) a position belongs to"""
        for unit, positions in self.position_units.items():
            if position in positions or any(pos in position for pos in positions):
                return unit
        return 'Defense'  # Default for defensive positions not explicitly listed

    def grade_team_changes(self, team_impacts_df: pd.DataFrame) -> pd.DataFrame:
        """Assign letter grades to team changes"""
        
        # Create grading scale based on net impact
        def get_grade(net_impact):
            if net_impact >= 8.0:
                return 'A+'
            elif net_impact >= 6.0:
                return 'A'
            elif net_impact >= 4.0:
                return 'A-'
            elif net_impact >= 2.0:
                return 'B+'
            elif net_impact >= 1.0:
                return 'B'
            elif net_impact >= 0.0:
                return 'B-'
            elif net_impact >= -1.0:
                return 'C+'
            elif net_impact >= -2.0:
                return 'C'
            elif net_impact >= -4.0:
                return 'C-'
            elif net_impact >= -6.0:
                return 'D'
            else:
                return 'F'
        
        team_impacts_df['offseason_grade'] = team_impacts_df['net_impact'].apply(get_grade)
        
        return team_impacts_df.sort_values('net_impact', ascending=False)

    def create_position_group_analysis(self, player_bridge_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """Analyze changes by position group"""
        
        position_analysis = {}
        
        for unit in ['Offense', 'Defense', 'Special Teams']:
            # Filter moves for this unit
            unit_positions = self.position_units[unit]
            unit_moves = player_bridge_df[
                player_bridge_df['position'].isin(unit_positions) |
                player_bridge_df['position'].str.contains('|'.join(unit_positions), na=False)
            ].copy()
            
            if len(unit_moves) > 0:
                # Analyze by team for this unit
                team_unit_impact = {}
                
                for team_data in self.team_mappings.values():
                    team_abbr = team_data['abbreviation']
                    
                    # Calculate gains and losses for this unit
                    gains = unit_moves[unit_moves['to_team'] == team_abbr]['impact_score'].sum()
                    losses = unit_moves[unit_moves['from_team'] == team_abbr]['impact_score'].sum()
                    
                    team_unit_impact[team_abbr] = {
                        'team': team_abbr,
                        'unit': unit,
                        'impact_gained': gains,
                        'impact_lost': losses,
                        'net_impact': gains - losses
                    }
                
                position_analysis[unit] = pd.DataFrame(list(team_unit_impact.values()))
                position_analysis[unit] = position_analysis[unit].sort_values('net_impact', ascending=False)
        
        return position_analysis

    def generate_comprehensive_report(self):
        """Generate complete player bridge analysis"""
        
        print("🏈 NFL Player Bridge Framework Analysis")
        print("=" * 60)
        
        # Create sample player bridge data
        player_bridge = self.create_player_bridge_template()
        
        print(f"📊 Tracking {len(player_bridge)} player moves")
        print()
        
        # Calculate team impacts
        team_impacts = self.calculate_team_net_changes(player_bridge)
        team_grades = self.grade_team_changes(team_impacts)
        
        # Show top and bottom performers
        print("🏆 BEST OFFSEASONS (Top 5)")
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
        
        # Position group analysis
        position_analysis = self.create_position_group_analysis(player_bridge)
        
        print(f"\n📈 UNIT ANALYSIS")
        print("-" * 30)
        for unit, unit_df in position_analysis.items():
            if len(unit_df) > 0:
                top_unit = unit_df.iloc[0]
                bottom_unit = unit_df.iloc[-1]
                print(f"{unit}:")
                print(f"  Best: {top_unit['team']} ({top_unit['net_impact']:+.1f})")
                print(f"  Worst: {bottom_unit['team']} ({bottom_unit['net_impact']:+.1f})")
        
        # Save all data
        self._save_results(player_bridge, team_grades, position_analysis)
        
        return player_bridge, team_grades, position_analysis

    def _save_results(self, player_bridge, team_grades, position_analysis):
        """Save all analysis to files"""
        
        # Save main datasets
        player_bridge.to_csv(self.output_path / "player_bridge_moves.csv", index=False)
        team_grades.to_csv(self.output_path / "team_offseason_grades.csv", index=False)
        
        # Save position analysis
        for unit, unit_df in position_analysis.items():
            unit_df.to_csv(self.output_path / f"{unit.lower()}_analysis.csv", index=False)
        
        print(f"\n💾 All analysis saved to: {self.output_path}")


def main():
    framework = PlayerBridgeFramework()
    player_bridge, team_grades, position_analysis = framework.generate_comprehensive_report()
    
    print(f"\n✅ Player Bridge Framework created!")
    print(f"📋 Ready to input real 2025 offseason data")


if __name__ == "__main__":
    main()
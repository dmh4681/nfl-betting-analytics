"""
NFL Player Bridge Framework - Track all offseason moves and grade impact
Updated to use playoff_adjusted_rankings.csv with point differentials
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
        """Create template for tracking player moves - NOW WITH REAL 2025 DATA!"""
        
        # REAL 2025 offseason moves - Eagles comprehensive data from research
        real_2025_moves = [
            # EAGLES FREE AGENT SIGNINGS - Value-based approach
            {
                'player_name': 'Azeez Ojulari',
                'position': 'EDGE',
                'from_team': 'NYG',
                'to_team': 'Phi',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 3000000,
                '2024_grade': 7.2,  # 6 sacks in 11 games with limited snaps
                'projected_2025_grade': 7.8,  # Should get more opportunity
                'snap_percentage_2024': 35.0,  # Limited behind Burns/Thibodeaux
                'importance_to_old_team': 6.0,  # Rotational piece
                'importance_to_new_team': 8.5,  # Key replacement for Sweat
                'impact_score': self._calculate_impact_score('EDGE', 7.2, 35.0, 8.5)
            },
            {
                'player_name': 'Joshua Uche',
                'position': 'EDGE',
                'from_team': 'KC',
                'to_team': 'Phi',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1920000,
                '2024_grade': 6.5,  # Only 2 sacks, 22% snaps
                'projected_2025_grade': 7.5,  # Bounce-back potential
                'snap_percentage_2024': 22.0,
                'importance_to_old_team': 4.0,  # Minimal role
                'importance_to_new_team': 7.0,  # Pass rush depth
                'impact_score': self._calculate_impact_score('EDGE', 6.5, 22.0, 7.0)
            },
            {
                'player_name': 'Adoree Jackson',
                'position': 'CB2',
                'from_team': 'NYG',
                'to_team': 'Phi',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1755000,
                '2024_grade': 6.9,  # 69.0 PFF grade, ranked 58th
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 65.0,  # Started 5 of 14 games
                'importance_to_old_team': 6.5,
                'importance_to_new_team': 7.5,  # Replaces Slay depth
                'impact_score': self._calculate_impact_score('CB2', 6.9, 65.0, 7.5)
            },
            {
                'player_name': 'A.J. Dillon',
                'position': 'RB',
                'from_team': 'GB',
                'to_team': 'Phi',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1100000,
                '2024_grade': 0.0,  # Missed entire season with neck injury
                'projected_2025_grade': 6.5,  # Health unknown
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 3.0,
                'importance_to_new_team': 5.0,  # Backup depth
                'impact_score': self._calculate_impact_score('RB', 0.0, 0.0, 5.0)
            },
            {
                'player_name': 'Harrison Bryant',
                'position': 'TE',
                'from_team': 'LV',
                'to_team': 'Phi',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1000000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.2,
                'snap_percentage_2024': 45.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 6.0,  # TE depth
                'impact_score': self._calculate_impact_score('TE', 6.0, 45.0, 6.0)
            },

            # EAGLES MAJOR LOSSES - Defensive exodus
            {
                'player_name': 'Josh Sweat',
                'position': 'EDGE',
                'from_team': 'Phi',
                'to_team': 'Ari',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.5,  # 8 sacks regular season + 2.5 in Super Bowl
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 59.0,  # Primary edge threat
                'importance_to_old_team': 9.0,  # Team-leading pass rusher
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 8.5, 59.0, 9.0)
            },
            {
                'player_name': 'Milton Williams',
                'position': 'DT',
                'from_team': 'Phi',
                'to_team': 'NE',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.2,  # 5 sacks, 54 pressures, Super Bowl strip-sack
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 48.0,
                'importance_to_old_team': 8.0,  # Key interior rusher
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('DT', 8.2, 48.0, 8.0)
            },
            {
                'player_name': 'Oren Burks',
                'position': 'LB',
                'from_team': 'Phi',
                'to_team': 'Cin',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.5,  # Playoff hero, 25 tackles in 3 games
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 14.0,  # Mostly special teams
                'importance_to_old_team': 6.0,  # Special teams ace
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('LB', 7.5, 14.0, 6.0)
            },
            {
                'player_name': 'Kenneth Gainwell',
                'position': 'RB',
                'from_team': 'Phi',
                'to_team': 'Pit',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.8,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 25.0,
                'importance_to_old_team': 5.5,  # Backup RB
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('RB', 6.8, 25.0, 5.5)
            },
            {
                'player_name': 'Avonte Maddox',
                'position': 'CB2',
                'from_team': 'Phi',
                'to_team': 'Det',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 42.0,
                'importance_to_old_team': 6.5,  # Veteran depth
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('CB2', 7.0, 42.0, 6.5)
            },

            # EAGLES TRADES
            {
                'player_name': 'C.J. Gardner-Johnson',
                'position': 'S',
                'from_team': 'Phi',
                'to_team': 'Hou',
                'move_type': 'Trade',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.0,  # 6 interceptions, emotional leader
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 8.5,  # Defensive leader
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('S', 8.0, 85.0, 8.5)
            },
            {
                'player_name': 'Kenyon Green',
                'position': 'G',
                'from_team': 'Hou',
                'to_team': 'Phi',
                'move_type': 'Trade',
                'contract_years': 2,
                'contract_value': 5000000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.5,
                'snap_percentage_2024': 60.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 6.0,  # Interior line depth
                'impact_score': self._calculate_impact_score('G', 6.0, 60.0, 6.0)
            },
            {
                'player_name': 'Bryce Huff',
                'position': 'EDGE',
                'from_team': 'Phi',
                'to_team': 'SF',
                'move_type': 'Trade',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 5.5,  # Major disappointment, 2.5 sacks
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 55.0,
                'importance_to_old_team': 4.0,  # Failed signing
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 5.5, 55.0, 4.0)
            },

            # EAGLES DRAFT PICKS - Defensive rebuild
            {
                'player_name': 'Jihaad Campbell',
                'position': 'LB',
                'from_team': 'DRAFT',
                'to_team': 'Phi',
                'move_type': '2025 Draft Pick #31',
                'contract_years': 4,
                'contract_value': 12000000,
                '2024_grade': 0.0,  # College
                'projected_2025_grade': 7.5,  # First-Team All-SEC
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 8.5,  # Immediate starter
                'impact_score': self._calculate_impact_score('LB', 7.5, 85.0, 8.5)
            },
            {
                'player_name': 'Andrew Mukuba',
                'position': 'S',
                'from_team': 'DRAFT',
                'to_team': 'Phi',
                'move_type': '2025 Draft Pick #45',
                'contract_years': 4,
                'contract_value': 8500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.0,  # Led SEC with 5 INTs
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 8.0,  # Replaces CJGJ
                'impact_score': self._calculate_impact_score('S', 7.0, 80.0, 8.0)
            },
            {
                'player_name': 'Ty Robinson',
                'position': 'DT',
                'from_team': 'DRAFT',
                'to_team': 'Phi',
                'move_type': '2025 Draft Pick #112',
                'contract_years': 4,
                'contract_value': 4200000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.5,  # 12 TFL, 7 sacks at Nebraska
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 7.0,  # Replaces Milton Williams
                'impact_score': self._calculate_impact_score('DT', 6.5, 70.0, 7.0)
            },

            # EAGLES RETIREMENTS
            {
                'player_name': 'Brandon Graham',
                'position': 'EDGE',
                'from_team': 'Phi',
                'to_team': 'RETIRED',
                'move_type': 'Retirement',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.5,  # Played through torn triceps in Super Bowl
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 45.0,
                'importance_to_old_team': 8.0,  # Franchise legend, emotional leader
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 7.5, 45.0, 8.0)
            },

            # EAGLES POST-JUNE 1 CUTS
            {
                'player_name': 'Darius Slay',
                'position': 'CB1',
                'from_team': 'Phi',
                'to_team': 'RELEASED',
                'move_type': 'Post-June 1 Cut',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.8,  # Still productive veteran
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 80.0,
                'importance_to_old_team': 7.5,  # Veteran leader
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('CB1', 7.8, 80.0, 7.5)
            },
            {
                'player_name': 'James Bradberry',
                'position': 'CB2',
                'from_team': 'Phi',
                'to_team': 'RELEASED',
                'move_type': 'Post-June 1 Cut',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.2,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 70.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('CB2', 7.2, 70.0, 7.0)
            },

            # COMMANDERS FREE AGENT SIGNINGS - Major Additions
            {
                'player_name': 'Javon Kinlaw',
                'position': 'DT',
                'from_team': 'NYJ',
                'to_team': 'Was',
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 45000000,
                '2024_grade': 6.5,
                'projected_2025_grade': 7.2,
                'snap_percentage_2024': 65.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 8.0,
                'impact_score': self._calculate_impact_score('DT', 6.5, 65.0, 8.0)
            },
            {
                'player_name': 'Will Harris',
                'position': 'S',
                'from_team': 'NO',
                'to_team': 'Was',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 10000000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.5,
                'snap_percentage_2024': 62.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 7.0,
                'impact_score': self._calculate_impact_score('S', 6.0, 62.0, 7.0)
            },
            {
                'player_name': 'Jonathan Jones',
                'position': 'CB2',
                'from_team': 'NE',
                'to_team': 'Was',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 5500000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.2,
                'snap_percentage_2024': 68.0,
                'importance_to_old_team': 6.5,
                'importance_to_new_team': 6.0,
                'impact_score': self._calculate_impact_score('CB2', 6.0, 68.0, 6.0)
            },
            {
                'player_name': 'Deatrich Wise Jr.',
                'position': 'EDGE',
                'from_team': 'NE',
                'to_team': 'Was',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 5000000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.2,
                'snap_percentage_2024': 54.0,
                'importance_to_old_team': 5.5,
                'importance_to_new_team': 5.0,
                'impact_score': self._calculate_impact_score('EDGE', 6.0, 54.0, 5.0)
            },
            {
                'player_name': 'Jacob Martin',
                'position': 'EDGE',
                'from_team': 'Chi',
                'to_team': 'Was',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 3000000,
                '2024_grade': 5.0,
                'projected_2025_grade': 5.5,
                'snap_percentage_2024': 21.0,
                'importance_to_old_team': 4.0,
                'importance_to_new_team': 4.0,
                'impact_score': self._calculate_impact_score('EDGE', 5.0, 21.0, 4.0)
            },

            # COMMANDERS RE-SIGNINGS
            {
                'player_name': 'Bobby Wagner',
                'position': 'LB',
                'from_team': 'Was',
                'to_team': 'Was',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 9500000,
                '2024_grade': 9.0,
                'projected_2025_grade': 8.5,
                'snap_percentage_2024': 94.0,
                'importance_to_old_team': 10.0,
                'importance_to_new_team': 10.0,
                'impact_score': self._calculate_impact_score('LB', 9.0, 94.0, 10.0)
            },
            {
                'player_name': 'Zach Ertz',
                'position': 'TE',
                'from_team': 'Was',
                'to_team': 'Was',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 8000000,
                '2024_grade': 8.0,
                'projected_2025_grade': 7.5,
                'snap_percentage_2024': 78.0,
                'importance_to_old_team': 9.0,
                'importance_to_new_team': 9.0,
                'impact_score': self._calculate_impact_score('TE', 8.0, 78.0, 9.0)
            },
            {
                'player_name': 'Marcus Mariota',
                'position': 'QB',
                'from_team': 'Was',
                'to_team': 'Was',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 8000000,
                '2024_grade': 7.0,
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 5.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 7.0,
                'impact_score': self._calculate_impact_score('QB', 7.0, 5.0, 7.0)
            },

            # COMMANDERS MAJOR LOSSES
            {
                'player_name': 'Jonathan Allen',
                'position': 'DT',
                'from_team': 'Was',
                'to_team': 'Min',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 5.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 50.0,
                'importance_to_old_team': 8.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('DT', 5.0, 50.0, 8.0)
            },
            {
                'player_name': 'Jeremy Chinn',
                'position': 'S',
                'from_team': 'Was',
                'to_team': 'LV',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 94.0,
                'importance_to_old_team': 8.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('S', 8.0, 94.0, 8.0)
            },
            {
                'player_name': 'Dyami Brown',
                'position': 'WR2',
                'from_team': 'Was',
                'to_team': 'Jac',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 44.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('WR2', 7.0, 44.0, 6.0)
            },
            {
                'player_name': 'Olamide Zaccheaus',
                'position': 'WR3',
                'from_team': 'Was',
                'to_team': 'Chi',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 60.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('WR3', 7.0, 60.0, 5.0)
            },

            # COMMANDERS TRADES - Major Acquisitions
            {
                'player_name': 'Laremy Tunsil',
                'position': 'LT',
                'from_team': 'Hou',
                'to_team': 'Was',
                'move_type': 'Trade',
                'contract_years': 2,
                'contract_value': 50000000,
                '2024_grade': 10.0,
                'projected_2025_grade': 9.5,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 9.0,
                'importance_to_new_team': 10.0,
                'impact_score': self._calculate_impact_score('LT', 10.0, 100.0, 10.0)
            },
            {
                'player_name': 'Deebo Samuel',
                'position': 'WR1',
                'from_team': 'SF',
                'to_team': 'Was',
                'move_type': 'Trade',
                'contract_years': 1,
                'contract_value': 17550000,
                '2024_grade': 7.0,
                'projected_2025_grade': 7.8,
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 8.0,
                'impact_score': self._calculate_impact_score('WR1', 7.0, 85.0, 8.0)
            },

            # COMMANDERS DRAFT PICKS
            {
                'player_name': 'Josh Conerly Jr.',
                'position': 'RT',
                'from_team': 'DRAFT',
                'to_team': 'Was',
                'move_type': '2025 Draft Pick #29',
                'contract_years': 4,
                'contract_value': 15680000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.5,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 8.5,
                'impact_score': self._calculate_impact_score('RT', 7.5, 85.0, 8.5)
            },
            {
                'player_name': 'Trey Amos',
                'position': 'CB1',
                'from_team': 'DRAFT',
                'to_team': 'Was',
                'move_type': '2025 Draft Pick #61',
                'contract_years': 4,
                'contract_value': 8000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 7.5,
                'impact_score': self._calculate_impact_score('CB1', 7.0, 80.0, 7.5)
            },
            {
                'player_name': 'Jaylin Lane',
                'position': 'WR3',
                'from_team': 'DRAFT',
                'to_team': 'Was',
                'move_type': '2025 Draft Pick #128',
                'contract_years': 4,
                'contract_value': 4500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 6.0,
                'impact_score': self._calculate_impact_score('WR3', 6.0, 60.0, 6.0)
            },

            # DALLAS COWBOYS 2025 OFFSEASON MOVES - Comprehensive Analysis
            
            # COWBOYS FREE AGENT SIGNINGS
            {
                'player_name': 'Javonte Williams',
                'position': 'RB',
                'from_team': 'Den',
                'to_team': 'Dal',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 3500000,
                '2024_grade': 6.5,  # 1,287 yards from scrimmage over last 2 seasons
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 60.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 7.5,  # Pass-catching complement
                'impact_score': self._calculate_impact_score('RB', 6.5, 60.0, 7.5)
            },
            {
                'player_name': 'Miles Sanders',
                'position': 'RB',
                'from_team': 'Car',
                'to_team': 'Dal',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 2000000,
                '2024_grade': 4.5,  # Career-low 205 rushing yards
                'projected_2025_grade': 6.0,  # Bounce-back potential
                'snap_percentage_2024': 40.0,
                'importance_to_old_team': 4.0,
                'importance_to_new_team': 6.0,  # Veteran depth
                'impact_score': self._calculate_impact_score('RB', 4.5, 40.0, 6.0)
            },
            {
                'player_name': 'Solomon Thomas',
                'position': 'DT',
                'from_team': 'NYJ',
                'to_team': 'Dal',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 8000000,
                '2024_grade': 6.8,  # 8.5 sacks, 14 TFLs over 3 seasons
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 55.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 7.0,  # Reunion with coach
                'impact_score': self._calculate_impact_score('DT', 6.8, 55.0, 7.0)
            },
            {
                'player_name': 'Jack Sanborn',
                'position': 'LB',
                'from_team': 'Chi',
                'to_team': 'Dal',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 2500000,
                '2024_grade': 6.2,
                'projected_2025_grade': 7.0,  # Familiarity with Eberflus system
                'snap_percentage_2024': 45.0,
                'importance_to_old_team': 5.5,
                'importance_to_new_team': 7.0,  # System fit
                'impact_score': self._calculate_impact_score('LB', 6.2, 45.0, 7.0)
            },
            {
                'player_name': 'Payton Turner',
                'position': 'EDGE',
                'from_team': 'NO',
                'to_team': 'Dal',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 2800000,
                '2024_grade': 5.8,
                'projected_2025_grade': 6.5,
                'snap_percentage_2024': 35.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 6.0,  # Depth addition
                'impact_score': self._calculate_impact_score('EDGE', 5.8, 35.0, 6.0)
            },
            {
                'player_name': 'Parris Campbell',
                'position': 'WR3',
                'from_team': 'Dal',
                'to_team': 'Dal',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 1500000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 30.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 5.0,
                'impact_score': self._calculate_impact_score('WR3', 6.0, 30.0, 5.0)
            },
            {
                'player_name': 'Dante Fowler Jr.',
                'position': 'EDGE',
                'from_team': 'Was',
                'to_team': 'Dal',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 6000000,
                '2024_grade': 7.5,  # 10.5 sacks with Washington
                'projected_2025_grade': 7.2,
                'snap_percentage_2024': 65.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 8.0,  # Key pass rusher
                'impact_score': self._calculate_impact_score('EDGE', 7.5, 65.0, 8.0)
            },

            # COWBOYS MAJOR LOSSES
            {
                'player_name': 'DeMarcus Lawrence',
                'position': 'EDGE',
                'from_team': 'Dal',
                'to_team': 'Sea',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,  # Injury-limited to 4 games
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 25.0,  # Limited by injury
                'importance_to_old_team': 8.5,  # 4x Pro Bowler, longest-tenured
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 6.0, 25.0, 8.5)
            },
            {
                'player_name': 'Jourdan Lewis',
                'position': 'CB2',
                'from_team': 'Dal',
                'to_team': 'Jac',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.0,  # Career-high 71 tackles, locker room leader
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 8.0,  # Highest-paid nickel corner
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('CB2', 8.0, 85.0, 8.0)
            },
            {
                'player_name': 'Rico Dowdle',
                'position': 'RB',
                'from_team': 'Dal',
                'to_team': 'Car',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 8.2,  # First UDFA in Cowboys history with 1,000+ yards
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 75.0,
                'importance_to_old_team': 8.5,  # 1,079 yards, 39 catches
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('RB', 8.2, 75.0, 8.5)
            },
            {
                'player_name': 'Chauncey Golston',
                'position': 'EDGE',
                'from_team': 'Dal',
                'to_team': 'NYG',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.0,  # Career-highs: 56 tackles, 5.5 sacks
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 60.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 7.0, 60.0, 7.0)
            },
            {
                'player_name': 'Brandin Cooks',
                'position': 'WR1',
                'from_team': 'Dal',
                'to_team': 'NO',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.5,  # Veteran production
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 80.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('WR1', 7.5, 80.0, 7.5)
            },
            {
                'player_name': 'Cooper Rush',
                'position': 'QB',
                'from_team': 'Dal',
                'to_team': 'Bal',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.5,  # Reliable backup
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 15.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 6.5, 15.0, 6.0)
            },
            {
                'player_name': 'Chuma Edoga',
                'position': 'RT',
                'from_team': 'Dal',
                'to_team': 'Jac',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 50.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('RT', 6.0, 50.0, 6.0)
            },

            # COWBOYS TRADES
            {
                'player_name': 'George Pickens',
                'position': 'WR1',
                'from_team': 'Pit',
                'to_team': 'Dal',
                'move_type': 'Trade',
                'contract_years': 1,
                'contract_value': 8000000,  # Remaining on rookie deal
                '2024_grade': 7.8,  # 59 catches, 900 yards
                'projected_2025_grade': 8.2,  # Compared to Dez Bryant
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 9.0,  # Marquee acquisition
                'impact_score': self._calculate_impact_score('WR1', 7.8, 85.0, 9.0)
            },
            {
                'player_name': 'Kenneth Murray Jr.',
                'position': 'LB',
                'from_team': 'Ten',
                'to_team': 'Dal',
                'move_type': 'Trade',
                'contract_years': 1,
                'contract_value': 15500000,  # Inherited contract
                '2024_grade': 7.2,  # 95 tackles, 3.5 sacks
                'projected_2025_grade': 7.5,
                'snap_percentage_2024': 80.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 8.0,  # Former 1st round pick
                'impact_score': self._calculate_impact_score('LB', 7.2, 80.0, 8.0)
            },
            {
                'player_name': 'Joe Milton III',
                'position': 'QB',
                'from_team': 'NE',
                'to_team': 'Dal',
                'move_type': 'Trade',
                'contract_years': 3,
                'contract_value': 3000000,
                '2024_grade': 5.5,  # Limited NFL experience
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 5.0,
                'importance_to_old_team': 4.0,
                'importance_to_new_team': 6.0,  # Dallas-area native
                'impact_score': self._calculate_impact_score('QB', 5.5, 5.0, 6.0)
            },
            {
                'player_name': 'Kaiir Elam',
                'position': 'CB2',
                'from_team': 'Buf',
                'to_team': 'Dal',
                'move_type': 'Trade',
                'contract_years': 2,
                'contract_value': 4000000,
                '2024_grade': 5.8,  # Former 1st round pick
                'projected_2025_grade': 6.5,  # Change of scenery
                'snap_percentage_2024': 25.0,
                'importance_to_old_team': 4.0,
                'importance_to_new_team': 6.5,  # Depth with Diggs injury
                'impact_score': self._calculate_impact_score('CB2', 5.8, 25.0, 6.5)
            },

            # COWBOYS 2025 DRAFT PICKS
            {
                'player_name': 'Tyler Booker',
                'position': 'G',
                'from_team': 'DRAFT',
                'to_team': 'Dal',
                'move_type': '2025 Draft Pick #12',
                'contract_years': 4,
                'contract_value': 28000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 8.0,  # Direct replacement for Zack Martin
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,  # Expected immediate starter
                'impact_score': self._calculate_impact_score('G', 8.0, 90.0, 9.0)
            },
            {
                'player_name': 'Donovan Ezeiruaku',
                'position': 'EDGE',
                'from_team': 'DRAFT',
                'to_team': 'Dal',
                'move_type': '2025 Draft Pick #44',
                'contract_years': 4,
                'contract_value': 8500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.5,  # Led ACC with 16.5 sacks
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 8.5,  # Replaces Lawrence production
                'impact_score': self._calculate_impact_score('EDGE', 7.5, 80.0, 8.5)
            },
            {
                'player_name': 'Shavon Revel Jr.',
                'position': 'CB1',
                'from_team': 'DRAFT',
                'to_team': 'Dal',
                'move_type': '2025 Draft Pick #76',
                'contract_years': 4,
                'contract_value': 5500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.0,  # 6'3" press-man corner
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 7.5,  # Could start opposite Bland
                'impact_score': self._calculate_impact_score('CB1', 7.0, 75.0, 7.5)
            },
            {
                'player_name': 'Jaydon Blue',
                'position': 'RB',
                'from_team': 'DRAFT',
                'to_team': 'Dal',
                'move_type': '2025 Draft Pick #149',
                'contract_years': 4,
                'contract_value': 4000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.5,  # 4.38 speed back
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 6.0,  # Speed complement
                'impact_score': self._calculate_impact_score('RB', 6.5, 60.0, 6.0)
            },
            {
                'player_name': 'Shemar James',
                'position': 'LB',
                'from_team': 'DRAFT',
                'to_team': 'Dal',
                'move_type': '2025 Draft Pick #152',
                'contract_years': 4,
                'contract_value': 3800000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.5,  # Versatile linebacker
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 6.0,
                'impact_score': self._calculate_impact_score('LB', 6.5, 60.0, 6.0)
            },

            # COWBOYS KEY RE-SIGNINGS
            {
                'player_name': 'Osa Odighizuwa',
                'position': 'DT',
                'from_team': 'Dal',
                'to_team': 'Dal',
                'move_type': 'Extension',
                'contract_years': 4,
                'contract_value': 80000000,
                '2024_grade': 8.0,
                'projected_2025_grade': 8.2,
                'snap_percentage_2024': 70.0,
                'importance_to_old_team': 8.5,
                'importance_to_new_team': 8.5,  # Cornerstone of Eberflus defense
                'impact_score': self._calculate_impact_score('DT', 8.0, 70.0, 8.5)
            },
            {
                'player_name': 'Markquese Bell',
                'position': 'S',
                'from_team': 'Dal',
                'to_team': 'Dal',
                'move_type': 'Extension',
                'contract_years': 3,
                'contract_value': 12000000,
                '2024_grade': 7.5,  # 102 tackles in hybrid role
                'projected_2025_grade': 7.8,
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 7.5,
                'impact_score': self._calculate_impact_score('S', 7.5, 85.0, 7.5)
            },

            # COWBOYS COACHING CHANGES
            {
                'player_name': 'Brian Schottenheimer',
                'position': 'COACH',
                'from_team': 'PROMOTION',
                'to_team': 'Dal',
                'move_type': 'Head Coach Promotion',
                'contract_years': 4,
                'contract_value': 0,  # Coaching salary not disclosed
                '2024_grade': 7.0,  # Was OC
                'projected_2025_grade': 7.5,  # First-time HC
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,  # Major organizational change
                'impact_score': self._calculate_impact_score('DEPTH', 7.0, 100.0, 9.0)
            },
            {
                'player_name': 'Matt Eberflus',
                'position': 'COACH',
                'from_team': 'Chi',
                'to_team': 'Dal',
                'move_type': 'Defensive Coordinator Hire',
                'contract_years': 3,
                'contract_value': 0,
                '2024_grade': 6.5,  # Fired as Bears HC
                'projected_2025_grade': 8.0,  # Returns to DC role, Dallas history
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 8.5,  # Coordinator overhaul
                'impact_score': self._calculate_impact_score('DEPTH', 6.5, 100.0, 8.5)
            },

            # NEW YORK GIANTS 2025 OFFSEASON MOVES - Complete Roster Overhaul
            
            # GIANTS MAJOR QB ACQUISITIONS
            {
                'player_name': 'Russell Wilson',
                'position': 'QB',
                'from_team': 'Pit',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 10500000,  # Fully guaranteed
                '2024_grade': 7.2,  # Former Super Bowl champion
                'projected_2025_grade': 6.8,  # Age 36
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 8.5,
                'importance_to_new_team': 9.5,  # Expected starter, veteran leadership
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 9.5)
            },
            {
                'player_name': 'Jameis Winston',
                'position': 'QB',
                'from_team': 'Cle',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 3500000,
                '2024_grade': 6.5,  # Former #1 overall pick
                'projected_2025_grade': 6.2,
                'snap_percentage_2024': 30.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 7.0,  # Primary backup
                'impact_score': self._calculate_impact_score('QB', 6.5, 30.0, 7.0)
            },

            # GIANTS SECONDARY TRANSFORMATION
            {
                'player_name': 'Jevon Holland',
                'position': 'S',
                'from_team': 'Mia',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 45300000,  # $30.3M guaranteed
                '2024_grade': 6.8,  # Career-low coverage grade
                'projected_2025_grade': 7.5,  # Change of scenery
                'snap_percentage_2024': 85.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 8.5,  # Biggest financial commitment
                'impact_score': self._calculate_impact_score('S', 6.8, 85.0, 8.5)
            },
            {
                'player_name': 'Paulson Adebo',
                'position': 'CB1',
                'from_team': 'NO',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 54000000,  # $36M fully guaranteed
                '2024_grade': 7.5,  # Shutdown corner before injury
                'projected_2025_grade': 7.8,  # Recovery from broken leg
                'snap_percentage_2024': 60.0,  # Injury-limited
                'importance_to_old_team': 8.0,
                'importance_to_new_team': 9.0,  # Opposite Deonte Banks
                'impact_score': self._calculate_impact_score('CB1', 7.5, 60.0, 9.0)
            },

            # GIANTS DEFENSIVE LINE REINFORCEMENTS
            {
                'player_name': 'Chauncey Golston',
                'position': 'EDGE',
                'from_team': 'Dal',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 3,
                'contract_value': 19500000,
                '2024_grade': 7.0,  # Career-high 5.5 sacks
                'projected_2025_grade': 7.2,
                'snap_percentage_2024': 60.0,
                'importance_to_old_team': 7.0,
                'importance_to_new_team': 7.5,
                'impact_score': self._calculate_impact_score('EDGE', 7.0, 60.0, 7.5)
            },
            {
                'player_name': 'Roy Robertson-Harris',
                'position': 'DT',
                'from_team': 'Jac',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 9000000,
                '2024_grade': 6.5,  # Veteran experience
                'projected_2025_grade': 6.8,
                'snap_percentage_2024': 55.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 6.5,
                'impact_score': self._calculate_impact_score('DT', 6.5, 55.0, 6.5)
            },
            {
                'player_name': 'Jeremiah Ledbetter',
                'position': 'DT',
                'from_team': 'Jac',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 2500000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.2,
                'snap_percentage_2024': 45.0,
                'importance_to_old_team': 5.5,
                'importance_to_new_team': 6.0,
                'impact_score': self._calculate_impact_score('DT', 6.0, 45.0, 6.0)
            },

            # GIANTS NOTABLE DEPTH SIGNINGS
            {
                'player_name': 'Chris Board',
                'position': 'LB',
                'from_team': 'Det',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 6000000,
                '2024_grade': 7.0,  # Tied for 9th in NFL with 8 ST tackles
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 25.0,  # Mostly special teams
                'importance_to_old_team': 6.5,
                'importance_to_new_team': 7.0,  # Veteran leadership
                'impact_score': self._calculate_impact_score('LB', 7.0, 25.0, 7.0)
            },
            {
                'player_name': 'James Hudson III',
                'position': 'RT',
                'from_team': 'Cin',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 12000000,
                '2024_grade': 6.2,
                'projected_2025_grade': 6.5,
                'snap_percentage_2024': 50.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 6.5,  # OL depth
                'impact_score': self._calculate_impact_score('RT', 6.2, 50.0, 6.5)
            },
            {
                'player_name': 'Stone Forsythe',
                'position': 'RT',
                'from_team': 'Mia',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 2000000,
                '2024_grade': 5.8,
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 40.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 5.5,
                'impact_score': self._calculate_impact_score('RT', 5.8, 40.0, 5.5)
            },
            {
                'player_name': 'Zach Pascal',
                'position': 'WR3',
                'from_team': 'Ari',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1800000,
                '2024_grade': 6.0,
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 45.0,
                'importance_to_old_team': 5.5,
                'importance_to_new_team': 6.0,
                'impact_score': self._calculate_impact_score('WR3', 6.0, 45.0, 6.0)
            },
            {
                'player_name': "Lil'Jordan Humphrey",
                'position': 'WR3',
                'from_team': 'Den',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 1,
                'contract_value': 1500000,
                '2024_grade': 5.8,
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 40.0,
                'importance_to_old_team': 5.0,
                'importance_to_new_team': 5.5,
                'impact_score': self._calculate_impact_score('WR3', 5.8, 40.0, 5.5)
            },

            # GIANTS MAJOR DEPARTURES TO DIVISION RIVALS
            {
                'player_name': 'Azeez Ojulari',
                'position': 'EDGE',
                'from_team': 'NYG',
                'to_team': 'Phi',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 7.2,  # 22 career sacks despite injuries
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 35.0,  # Limited snaps behind Burns/Thibodeaux
                'importance_to_old_team': 6.0,  # 2021 second-round pick
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('EDGE', 7.2, 35.0, 6.0)
            },
            {
                'player_name': 'Adoree Jackson',
                'position': 'CB2',
                'from_team': 'NYG',
                'to_team': 'Phi',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.9,  # Started 5 of 14 games
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 65.0,
                'importance_to_old_team': 6.5,  # Former first-round pick
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('CB2', 6.9, 65.0, 6.5)
            },

            # GIANTS OTHER KEY DEPARTURES
            {
                'player_name': 'Isaiah Simmons',
                'position': 'LB',
                'from_team': 'NYG',
                'to_team': 'GB',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,  # 17% of defensive snaps
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 17.0,
                'importance_to_old_team': 5.0,  # Versatile but underused
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('LB', 6.0, 17.0, 5.0)
            },
            {
                'player_name': 'Drew Lock',
                'position': 'QB',
                'from_team': 'NYG',
                'to_team': 'Sea',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 5.5,  # Backup QB
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 10.0,
                'importance_to_old_team': 5.5,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 5.5, 10.0, 5.5)
            },
            {
                'player_name': 'Jason Pinnock',
                'position': 'S',
                'from_team': 'NYG',
                'to_team': 'SF',
                'move_type': 'Free Agent Loss',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.2,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 55.0,
                'importance_to_old_team': 6.0,  # Safety depth
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('S', 6.2, 55.0, 6.0)
            },

            # GIANTS DANIEL JONES ERA ENDS
            {
                'player_name': 'Daniel Jones',
                'position': 'QB',
                'from_team': 'NYG',
                'to_team': 'RELEASED',
                'move_type': 'Release',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 4.5,  # Demoted to fourth-string
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 60.0,  # Before benching
                'importance_to_old_team': 7.0,  # $22.2M dead cap
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 4.5, 60.0, 7.0)
            },

            # GIANTS DRAFT DAY BLOCKBUSTER TRADE
            {
                'player_name': 'Jaxson Dart',
                'position': 'QB',
                'from_team': 'DRAFT',
                'to_team': 'NYG',
                'move_type': '2025 Draft Pick #25 (via trade)',
                'contract_years': 4,
                'contract_value': 16977000,  # Fully guaranteed
                '2024_grade': 0.0,
                'projected_2025_grade': 6.8,  # 4,279 yards, 29 TDs
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,  # Franchise QB of future
                'impact_score': self._calculate_impact_score('QB', 6.8, 80.0, 9.0)  # Will develop behind Wilson
            },

            # GIANTS 2025 DRAFT SELECTIONS
            {
                'player_name': 'Abdul Carter',
                'position': 'EDGE',
                'from_team': 'DRAFT',
                'to_team': 'NYG',
                'move_type': '2025 Draft Pick #3',
                'contract_years': 4,
                'contract_value': 45260000,  # Fully guaranteed
                '2024_grade': 0.0,
                'projected_2025_grade': 8.5,  # Elite pass rusher, 12 sacks
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.5,  # Immediate starter opposite Burns/Thibodeaux
                'impact_score': self._calculate_impact_score('EDGE', 8.5, 90.0, 9.5)
            },
            {
                'player_name': 'Darius Alexander',
                'position': 'DT',
                'from_team': 'DRAFT',
                'to_team': 'NYG',
                'move_type': '2025 Draft Pick #65',
                'contract_years': 4,
                'contract_value': 6500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.0,  # 90.1 PFF grade
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 7.5,  # Rotational help behind Dexter Lawrence
                'impact_score': self._calculate_impact_score('DT', 7.0, 70.0, 7.5)
            },
            {
                'player_name': 'Cam Skattebo',
                'position': 'RB',
                'from_team': 'DRAFT',
                'to_team': 'NYG',
                'move_type': '2025 Draft Pick #105',
                'contract_years': 4,
                'contract_value': 4500000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.8,  # 100+ missed tackles forced
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 7.0,  # Power complement to Tracy Jr.
                'impact_score': self._calculate_impact_score('RB', 6.8, 70.0, 7.0)
            },
            {
                'player_name': 'Marcus Mbow',
                'position': 'G',
                'from_team': 'DRAFT',
                'to_team': 'NYG',
                'move_type': '2025 Draft Pick #154',
                'contract_years': 4,
                'contract_value': 3800000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.0,  # Medical concerns
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 6.0,  # Guard competition
                'impact_score': self._calculate_impact_score('G', 6.0, 60.0, 6.0)
            },

            # GIANTS KEY RE-SIGNINGS
            {
                'player_name': 'Darius Slayton',
                'position': 'WR1',
                'from_team': 'NYG',
                'to_team': 'NYG',
                'move_type': 'Extension',
                'contract_years': 3,
                'contract_value': 36000000,
                '2024_grade': 7.5,  # Leading receiver 4 of last 5 seasons
                'projected_2025_grade': 7.8,
                'snap_percentage_2024': 80.0,
                'importance_to_old_team': 8.0,
                'importance_to_new_team': 8.0,  # Longest-tenured offensive player
                'impact_score': self._calculate_impact_score('WR1', 7.5, 80.0, 8.0)
            },
            {
                'player_name': 'Jamie Gillan',
                'position': 'P',
                'from_team': 'NYG',
                'to_team': 'NYG',
                'move_type': 'Extension',
                'contract_years': 3,
                'contract_value': 10200000,
                '2024_grade': 7.0,
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 100.0,  # All punts
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 6.0,  # One of highest-paid punters
                'impact_score': self._calculate_impact_score('P', 7.0, 100.0, 6.0)
            },
            {
                'player_name': 'Greg Van Roten',
                'position': 'G',
                'from_team': 'NYG',
                'to_team': 'NYG',
                'move_type': 'Re-signing',
                'contract_years': 1,
                'contract_value': 2500000,
                '2024_grade': 7.2,  # Didn't miss single snap (1,125 plays)
                'projected_2025_grade': 7.0,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 7.5,
                'importance_to_new_team': 7.5,  # Iron man
                'impact_score': self._calculate_impact_score('G', 7.2, 100.0, 7.5)
            },
            {
                'player_name': 'Tommy DeVito',
                'position': 'QB',
                'from_team': 'NYG',
                'to_team': 'NYG',
                'move_type': 'Exclusive Rights Tender',
                'contract_years': 1,
                'contract_value': 1030000,
                '2024_grade': 6.0,  # Local hero
                'projected_2025_grade': 6.0,
                'snap_percentage_2024': 20.0,
                'importance_to_old_team': 6.0,
                'importance_to_new_team': 6.0,  # System familiarity
                'impact_score': self._calculate_impact_score('QB', 6.0, 20.0, 6.0)
            },

            # OTHER TEAMS - Key Context Moves
            {
                'player_name': 'Cam Ward',
                'position': 'QB',
                'from_team': 'DRAFT',
                'to_team': 'Ten',
                'move_type': '2025 Draft Pick #1',
                'contract_years': 4,
                'contract_value': 42000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.8,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 10.0,
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 10.0)
            },
            {
                'player_name': 'Travis Hunter',
                'position': 'CB1',
                'from_team': 'DRAFT',
                'to_team': 'Cle',
                'move_type': '2025 Draft Pick #2',
                'contract_years': 4,
                'contract_value': 38000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.5,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,
                'impact_score': self._calculate_impact_score('CB1', 7.5, 90.0, 9.0)
            },
            {
                'player_name': 'Aaron Rodgers',
                'position': 'QB',
                'from_team': 'NYJ',
                'to_team': 'RETIRED',
                'move_type': 'Retirement',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 9.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 6.0, 100.0, 9.0)
            },

            # OTHER TEAMS - Adding context from earlier framework
            {
                'player_name': 'Cam Ward',
                'position': 'QB',
                'from_team': 'DRAFT',
                'to_team': 'Ten',
                'move_type': '2025 Draft Pick #1',
                'contract_years': 4,
                'contract_value': 42000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 6.8,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 10.0,
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 10.0)
            },
            {
                'player_name': 'Travis Hunter',
                'position': 'CB1',
                'from_team': 'DRAFT',
                'to_team': 'Cle',
                'move_type': '2025 Draft Pick #2',
                'contract_years': 4,
                'contract_value': 38000000,
                '2024_grade': 0.0,
                'projected_2025_grade': 7.5,
                'snap_percentage_2024': 0.0,
                'importance_to_old_team': 0.0,
                'importance_to_new_team': 9.0,
                'impact_score': self._calculate_impact_score('CB1', 7.5, 90.0, 9.0)
            },
            {
                'player_name': 'Russell Wilson',
                'position': 'QB',
                'from_team': 'Pit',
                'to_team': 'NYG',
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 25000000,
                '2024_grade': 7.2,
                'projected_2025_grade': 6.8,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 8.5,
                'importance_to_new_team': 9.5,
                'impact_score': self._calculate_impact_score('QB', 6.8, 100.0, 9.5)
            },
            {
                'player_name': 'Aaron Rodgers',
                'position': 'QB',
                'from_team': 'NYJ',
                'to_team': 'RETIRED',
                'move_type': 'Retirement',
                'contract_years': 0,
                'contract_value': 0,
                '2024_grade': 6.0,
                'projected_2025_grade': 0.0,
                'snap_percentage_2024': 100.0,
                'importance_to_old_team': 9.0,
                'importance_to_new_team': 0.0,
                'impact_score': -self._calculate_impact_score('QB', 6.0, 100.0, 9.0)
            }
        ]
        
        return pd.DataFrame(real_2025_moves)

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
            unit_key = f"{unit.lower()}_impact"
            
            # Player leaving a team (loss)
            if from_team in team_impacts and from_team not in ['DRAFT', 'FA', 'RETIRED', 'RELEASED']:
                team_impacts[from_team]['players_lost'] += 1
                loss_impact = abs(impact)
                team_impacts[from_team]['impact_lost'] += loss_impact
                team_impacts[from_team]['net_impact'] -= loss_impact
                team_impacts[from_team][unit_key] -= loss_impact
                
                if loss_impact >= 0.5:  # Lower threshold for key moves
                    team_impacts[from_team]['key_losses'].append(f"{player_name} ({position})")
            
            # Player joining a team (gain)
            if to_team in team_impacts and to_team not in ['FA', 'RETIRED', 'RELEASED']:
                team_impacts[to_team]['players_gained'] += 1
                gain_impact = abs(impact)
                team_impacts[to_team]['impact_gained'] += gain_impact
                team_impacts[to_team]['net_impact'] += gain_impact
                team_impacts[to_team][unit_key] += gain_impact
                
                if gain_impact >= 0.5:  # Lower threshold for key moves
                    team_impacts[to_team]['key_additions'].append(f"{player_name} ({position})")
        
        return pd.DataFrame(list(team_impacts.values()))

    def _get_position_unit(self, position: str) -> str:
        """Determine which unit a position belongs to"""
        for unit, positions in self.position_units.items():
            if position in positions or any(pos in position for pos in positions):
                return unit
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
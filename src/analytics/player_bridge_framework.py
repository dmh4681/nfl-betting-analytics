"""
NFL Player Bridge Framework - Track all offseason moves and grade impact
Updated to use playoff_adjusted_rankings.csv with point differentials
FIXED VERSION - Properly scaled impact scores to prevent unrealistic rankings
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
        
        # Position importance weights - FURTHER REDUCED & EXTENSIONS DAMPENED
        self.position_weights = {
            'QB': 5.0,    # Reduced from 8.0 (was 10.0)
            'LT': 3.5,    # Reduced from 5.0 (was 6.0)
            'EDGE': 3.5,  # Reduced from 5.0 (was 6.0)
            'CB1': 3.5,   # Reduced from 5.0 (was 6.0)
            'WR1': 3.0,   # Reduced from 4.5 (was 5.5)
            'RT': 2.5,    # Reduced from 4.0 (was 5.0)
            'C': 2.5,     # Reduced from 4.0 (was 5.0)
            'S': 2.5,     # Reduced from 4.0 (was 5.0)
            'LB': 2.0,    # Reduced from 3.5 (was 4.5)
            'RB': 2.0,    # Reduced from 3.0 (was 4.0)
            'WR2': 2.0,   # Reduced from 3.0 (was 4.0)
            'TE': 2.0,    # Reduced from 3.0 (was 4.0)
            'G': 1.5,     # Reduced from 2.5 (was 3.5)
            'CB2': 1.5,   # Reduced from 2.5 (was 3.5)
            'DT': 1.5,    # Reduced from 2.5 (was 3.5)
            'K': 1.0,     # Reduced from 2.0 (was 2.5)
            'WR3': 1.0,   # Reduced from 1.5 (was 2.0)
            'P': 1.0,     # Reduced from 1.5 (was 2.0)
            'LS': 0.5,    # Reduced from 0.8 (was 1.0)
            'DEPTH': 0.5, # Reduced from 1.0 (was 1.5)
            'COACH': 2.0  # Reduced from 1.5 (was 2.0)
        }
        
        # Unit classifications - FIXED: Added Coaching and G
        self.position_units = {
            'Offense': ['QB', 'RB', 'WR1', 'WR2', 'WR3', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 'G', 'OT', 'OL'],
            'Defense': ['EDGE', 'DE', 'DT', 'LB', 'CB1', 'CB2', 'CB', 'S', 'DB', 'CB/S'],
            'Special Teams': ['K', 'P', 'LS'],
            'Coaching': ['COACH', 'HC', 'OC', 'DC', 'COACH-DC', 'COACH-OC', 'COACH-ST', 'COACH-LB', 'COACH-DL']
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
            # Get the correct path to the data directory
            current_dir = Path(__file__).parent  # src/analytics
            project_root = current_dir.parent.parent  # nfl-betting-analytics
            data_dir = project_root / "data" / "player_moves"
            
            # Add the data directory to Python path for imports
            import sys
            if str(data_dir) not in sys.path:
                sys.path.insert(0, str(data_dir))
            
            # Try to import the __init__.py from the data directory
            try:
                import importlib.util
                init_path = data_dir / "__init__.py"
                
                
                if init_path.exists():
                    spec = importlib.util.spec_from_file_location("player_moves_init", init_path)
                    player_moves_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(player_moves_module)
                    
                    # Get the ALL_2025_MOVES from the __init__ module
                    real_2025_moves = getattr(player_moves_module, 'ALL_2025_MOVES', []).copy()
                    logger.info(f"✅ Loaded {len(real_2025_moves)} moves from {init_path}")
                    
                    # Also get team counts for reporting
                    team_counts = getattr(player_moves_module, 'TEAM_MOVE_COUNTS', {})
                    loaded_teams = getattr(player_moves_module, 'loaded_teams', [])
                    logger.info(f"✅ Teams loaded: {len(loaded_teams)} ({', '.join(loaded_teams)})")
                    
                else:
                    logger.warning(f"__init__.py not found at {init_path}")
                    real_2025_moves = []
                    
            except Exception as e:
                logger.error(f"❌ Error importing from {init_path}: {e}")
                # Try alternative approach - direct team file imports
                try:
                    real_2025_moves = []
                    
                    # List of team files we know exist
                    team_files = [
                        ('49ers_2025', 'NINERS_2025_MOVES'),
                        ('bills_2025', 'BILLS_2025_MOVES'),
                        ('bengals_2025', 'BENGALS_2025_MOVES'),
                        ('eagles_2025', 'EAGLES_2025_MOVES'),
                        ('cowboys_2025', 'COWBOYS_2025_MOVES'),
                        ('giants_2025', 'GIANTS_2025_MOVES'),
                        ('commanders_2025', 'COMMANDERS_2025_MOVES'),
                        ('dolphins_2025', 'DOLPHINS_2025_MOVES'),
                        ('patriots_2025', 'PATRIOTS_2025_MOVES'),
                        ('jets_2025', 'JETS_2025_MOVES'),
                        ('ravens_2025', 'RAVENS_2025_MOVES'),
                        ('steelers_2025', 'STEELERS_2025_MOVES'),
                        ('browns_2025', 'BROWNS_2025_MOVES'),
                        ('texans_2025', 'TEXANS_2025_MOVES'),
                        ('colts_2025', 'COLTS_2025_MOVES'),
                        ('titans_2025', 'TITANS_2025_MOVES'),
                        ('jaguars_2025', 'JAGUARS_2025_MOVES'),
                        ('chiefs_2025', 'CHIEFS_2025_MOVES'),
                        ('chargers_2025', 'CHARGERS_2025_MOVES'),
                        ('broncos_2025', 'BRONCOS_2025_MOVES'),
                        ('raiders_2025', 'RAIDERS_2025_MOVES')
                    ]
                    
                    for module_name, moves_var in team_files:
                        file_path = data_dir / f"{module_name}.py"
                        if file_path.exists():
                            try:
                                spec = importlib.util.spec_from_file_location(module_name, file_path)
                                module = importlib.util.module_from_spec(spec)
                                spec.loader.exec_module(module)
                                
                                moves = getattr(module, moves_var, [])
                                real_2025_moves.extend(moves)
                                logger.info(f"✅ Loaded {len(moves)} moves from {module_name}")
                            except Exception as file_error:
                                logger.warning(f"⚠️ Could not load {module_name}: {file_error}")
                    
                    if real_2025_moves:
                        logger.info(f"✅ Total loaded from individual files: {len(real_2025_moves)} moves")
                    else:
                        logger.warning("No moves found in individual team files")
                        
                except Exception as e2:
                    logger.error(f"❌ Error loading individual team files: {e2}")
                    real_2025_moves = []
            
        except Exception as e:
            logger.error(f"❌ Critical error in import process: {e}")
            logger.warning("Falling back to inline data")
            real_2025_moves = self._get_fallback_moves()
        
        if not real_2025_moves:
            logger.warning("No player moves loaded - using fallback data")
            real_2025_moves = self._get_fallback_moves()
        
        # Use pre-calculated impact scores when available, otherwise calculate
        for move in real_2025_moves:
            if 'impact_score' not in move or pd.isna(move.get('impact_score')):
                move['impact_score'] = self._calculate_impact_score(
                    move.get('position', ''),
                    move.get('2024_grade', 0),
                    move.get('snap_percentage_2024', 0),
                    move.get('importance_to_new_team', 0)
                )
        
        return pd.DataFrame(real_2025_moves)

    def _get_fallback_moves(self):
        """Fallback to your current inline data if external import fails"""
        # Return some basic moves so the framework doesn't break
        return [
            {
                'player_name': 'Sample Player',
                'position': 'QB',
                'from_team': 'DAL',
                'to_team': 'NYG', 
                'move_type': 'Free Agent Signing',
                'contract_years': 2,
                'contract_value': 15000000,
                '2024_grade': 7.0,
                'projected_2025_grade': 7.2,
                'snap_percentage_2024': 80.0,
                'importance_to_old_team': 8.0,
                'importance_to_new_team': 8.5,
            }
        ]

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
        """Calculate weighted impact score for a player move - PROPERLY SCALED"""
        
        # Position mappings
        position_mappings = {
            'EDGE': 'EDGE', 'DE': 'EDGE', 
            'CB': 'CB1', 'CB/S': 'CB1',
            'WR': 'WR1', 'WR1': 'WR1', 'WR2': 'WR2', 'WR3': 'WR3',
            'OT': 'RT', 'OL': 'G', 'C': 'C',
            'COACH-DC': 'COACH', 'COACH-OC': 'COACH', 'COACH-ST': 'COACH',
            'COACH-LB': 'COACH', 'COACH-DL': 'COACH'
        }
        
        # Map position to weight
        mapped_position = position_mappings.get(position, position)
        pos_weight = self.position_weights.get(mapped_position, 2.0)
        
        # Calculate base impact (grade * snap percentage * importance)
        base_impact = (grade / 10.0) * (snap_pct / 100.0) * (importance / 10.0)
        
        # Apply position weight
        weighted_impact = base_impact * pos_weight
        
        # SCALE DOWN BY 10X (not 3X) to make more realistic
        realistic_impact = weighted_impact / 10.0
        
        # Cap individual moves at 0.8 max impact (not 2.5)
        capped_impact = min(realistic_impact, 0.8)
        
        return round(capped_impact, 2)

    def calculate_team_net_changes(self, player_bridge_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate net impact for each team from all player moves - FIXED SCALING"""
        
        team_impacts = {}
        
        # Initialize all teams using the loaded rankings
        for team_abbr in self.original_power_rankings.keys():
            # Normalize team abbreviation to handle inconsistencies
            normalized_abbr = self._normalize_team_abbr(team_abbr)
            
            # Skip if we already have this team (prevents duplicates)
            if normalized_abbr in team_impacts:
                continue
                
            # Get the team's full name from mappings
            full_name = self._get_team_full_name(normalized_abbr)
                    
            team_impacts[normalized_abbr] = {
                'team': normalized_abbr,
                'team_name': full_name,
                'players_gained': 0,
                'players_lost': 0,
                'impact_gained': 0.0,
                'impact_lost': 0.0,
                'net_impact': 0.0,
                'offense_impact': 0.0,
                'defense_impact': 0.0,
                'special_teams_impact': 0.0,
                'coaching_impact': 0.0,
                'key_additions': [],
                'key_losses': [],
                'total_guaranteed': 0,
                'dead_money': 0,
                'cap_efficiency': 0.0
            }
        
        # Process each player move
        for _, move in player_bridge_df.iterrows():
            from_team = self._normalize_team_abbr(move['from_team'])
            to_team = self._normalize_team_abbr(move['to_team'])
            
            # Use pre-calculated impact_score if available BUT SCALE IT DOWN
            if 'impact_score' in move and pd.notna(move['impact_score']):
                # Scale down pre-calculated scores by 5x
                impact = move['impact_score'] / 5.0
            else:
                impact = self._calculate_impact_score(
                    move['position'],
                    move.get('2024_grade', 0),
                    move.get('snap_percentage_2024', 0),
                    move.get('importance_to_new_team', 0)
                )
            
            # Cap individual move impact
            impact = min(abs(impact), 0.8)
            
            position = move['position']
            player_name = move['player_name']
            move_type = move.get('move_type', '')
            
            # Skip internal moves (extensions, re-signings)
            if from_team == to_team and move_type in ['Contract Extension', 'Extension', 'Re-signing']:
                # Still track financial impact
                if to_team in team_impacts:
                    team_impacts[to_team]['total_guaranteed'] += move.get('guaranteed_money', 0)
                continue
            
            # Determine which unit this position belongs to
            unit = self._get_position_unit(position)
            unit_key = f"{unit.lower().replace(' ', '_')}_impact"
            
            # Player leaving a team (loss)
            if from_team in team_impacts and from_team not in ['DRAFT', 'FA', 'RETIRED', 'RELEASED', 'PROMOTION', 'FIRED', 'UNSIGNED', 'COLLEGE']:
                team_impacts[from_team]['players_lost'] += 1
                loss_impact = impact  # Already capped
                team_impacts[from_team]['impact_lost'] += loss_impact
                team_impacts[from_team]['net_impact'] -= loss_impact
                
                # Track dead money
                if move.get('guaranteed_money', 0) < 0:
                    team_impacts[from_team]['dead_money'] += abs(move['guaranteed_money'])
                
                # Apply unit-specific impact
                if unit_key in team_impacts[from_team]:
                    team_impacts[from_team][unit_key] -= loss_impact
                
                if loss_impact >= 0.3:  # Lower threshold for key moves
                    team_impacts[from_team]['key_losses'].append(f"{player_name} ({position})")
            
            # Player joining a team (gain)
            if to_team in team_impacts and to_team not in ['FA', 'RETIRED', 'RELEASED', 'FIRED', 'UNSIGNED']:
                team_impacts[to_team]['players_gained'] += 1
                gain_impact = impact  # Already capped
                team_impacts[to_team]['impact_gained'] += gain_impact
                team_impacts[to_team]['net_impact'] += gain_impact
                
                # Track guaranteed money
                team_impacts[to_team]['total_guaranteed'] += max(0, move.get('guaranteed_money', 0))
                
                # Apply unit-specific impact
                if unit_key in team_impacts[to_team]:
                    team_impacts[to_team][unit_key] += gain_impact
                
                if gain_impact >= 0.3:  # Lower threshold for key moves
                    team_impacts[to_team]['key_additions'].append(f"{player_name} ({position})")
        
        # Apply diminishing returns for teams with many moves
        for team_abbr, team_data in team_impacts.items():
            total_moves = team_data['players_gained'] + team_data['players_lost']
            if total_moves > 20:
                # Apply logarithmic scaling for teams with excessive moves
                scaling_factor = 1.0 + (np.log10(20) / np.log10(total_moves))
                team_data['net_impact'] *= scaling_factor
                team_data['offense_impact'] *= scaling_factor
                team_data['defense_impact'] *= scaling_factor
                team_data['special_teams_impact'] *= scaling_factor
            
            # Hard cap total net impact at +/- 8.0
            team_data['net_impact'] = max(-8.0, min(8.0, team_data['net_impact']))
        
        # Calculate cap efficiency for each team
        for team_data in team_impacts.values():
            if team_data['impact_gained'] > 0 and team_data['total_guaranteed'] > 0:
                # Efficiency = impact per million guaranteed
                team_data['cap_efficiency'] = round(
                    team_data['impact_gained'] / (team_data['total_guaranteed'] / 1000000), 2
                )
        
        return pd.DataFrame(list(team_impacts.values()))

    def _normalize_team_abbr(self, team_abbr: str) -> str:
        """Normalize team abbreviations to handle inconsistencies"""
        if pd.isna(team_abbr) or team_abbr in ['DRAFT', 'FA', 'RETIRED', 'RELEASED', 'PROMOTION', 'FIRED', 'UNSIGNED', 'COLLEGE']:
            return team_abbr
            
        team_abbr = str(team_abbr).strip().upper()
        
        # Handle common abbreviation mappings
        abbr_mappings = {
            'JAX': 'JAC',
            'WSH': 'WAS',
            'NO': 'NO',
            'NE': 'NE',
            'TB': 'TB',
            'LV': 'LV',
            'LAR': 'LAR',
            'LAC': 'LAC'
        }
        
        return abbr_mappings.get(team_abbr, team_abbr)

    def _get_team_full_name(self, team_abbr: str) -> str:
        """Get full team name from abbreviation"""
        # Team name mappings
        team_names = {
            'PHI': 'Philadelphia Eagles',
            'BAL': 'Baltimore Ravens', 
            'DET': 'Detroit Lions',
            'BUF': 'Buffalo Bills',
            'GB': 'Green Bay Packers',
            'SF': 'San Francisco 49ers',
            'KC': 'Kansas City Chiefs',
            'MIN': 'Minnesota Vikings',
            'CIN': 'Cincinnati Bengals',
            'HOU': 'Houston Texans',
            'NYJ': 'New York Jets',
            'LAC': 'Los Angeles Chargers',
            'PIT': 'Pittsburgh Steelers',
            'MIA': 'Miami Dolphins',
            'WAS': 'Washington Commanders',
            'ATL': 'Atlanta Falcons',
            'CLE': 'Cleveland Browns',
            'TB': 'Tampa Bay Buccaneers',
            'LAR': 'Los Angeles Rams',
            'SEA': 'Seattle Seahawks',
            'NYG': 'New York Giants',
            'IND': 'Indianapolis Colts',
            'ARI': 'Arizona Cardinals',
            'CHI': 'Chicago Bears',
            'TEN': 'Tennessee Titans',
            'JAC': 'Jacksonville Jaguars',
            'DEN': 'Denver Broncos',
            'DAL': 'Dallas Cowboys',
            'NE': 'New England Patriots',
            'CAR': 'Carolina Panthers',
            'NO': 'New Orleans Saints',
            'LV': 'Las Vegas Raiders'
        }
        
        return team_names.get(team_abbr, team_abbr)

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
        """Assign letter grades to team changes - ADJUSTED SCALE"""
        
        def get_grade(net_impact):
            # More reasonable grade scale
            if net_impact >= 6.0: return 'A+'
            elif net_impact >= 4.5: return 'A'
            elif net_impact >= 3.0: return 'A-'
            elif net_impact >= 2.0: return 'B+'
            elif net_impact >= 1.0: return 'B'
            elif net_impact >= 0.0: return 'B-'
            elif net_impact >= -1.0: return 'C+'
            elif net_impact >= -2.0: return 'C'
            elif net_impact >= -3.0: return 'C-'
            elif net_impact >= -4.5: return 'D'
            else: return 'F'
        
        team_impacts_df['offseason_grade'] = team_impacts_df['net_impact'].apply(get_grade)
        return team_impacts_df.sort_values('net_impact', ascending=False)

    def calculate_final_2025_rankings(self, team_impacts_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate final 2025 power rankings = Original + Offseason Impact"""
        
        final_rankings = []
        processed_teams = set()  # Track processed teams to avoid duplicates
        
        for _, team in team_impacts_df.iterrows():
            team_abbr = self._normalize_team_abbr(team['team'])
            
            # Skip if we've already processed this team
            if team_abbr in processed_teams:
                continue
            processed_teams.add(team_abbr)
            
            # Get original ratings with fallback
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
                'key_additions': ', '.join(team['key_additions'][:3]) if team['key_additions'] else '',
                'key_losses': ', '.join(team['key_losses'][:3]) if team['key_losses'] else '',
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
    print(f"   - Position-weighted importance scores (properly scaled)")


if __name__ == "__main__":
    main()
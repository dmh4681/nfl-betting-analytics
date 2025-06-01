"""
NFL Offseason Knowledge Management System
Tracks and systematizes offseason moves for automated ranking updates
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import pandas as pd
import re
from dataclasses import dataclass

@dataclass
class PlayerMove:
    """Structured representation of a player move"""
    player_name: str
    position: str
    from_team: str
    to_team: str
    move_type: str  # Free Agent, Trade, Draft, Release, etc.
    date_detected: str
    source: str
    contract_details: Optional[str] = None
    impact_score: Optional[float] = None
    
class OffseasonKnowledgeManager:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.knowledge_path = self.project_root / "data" / "offseason_knowledge"
        self.current_moves_path = self.project_root / "data" / "current_moves"
        self.daily_updates_path = self.current_moves_path / "daily_updates"
        
        # Create directories if they don't exist
        for path in [self.knowledge_path, self.current_moves_path, self.daily_updates_path]:
            path.mkdir(parents=True, exist_ok=True)
            
        # NFC East teams we're tracking
        self.nfc_east_teams = ['PHI', 'DAL', 'NYG', 'WSH']
        
        # Load existing knowledge
        self.team_knowledge = self._load_all_team_knowledge()
        
    def _load_all_team_knowledge(self) -> Dict[str, Dict]:
        """Load existing offseason knowledge for all teams"""
        knowledge = {}
        
        for team in self.nfc_east_teams:
            team_file = self.knowledge_path / f"{team.lower()}_offseason_2025.md"
            if team_file.exists():
                knowledge[team] = self._parse_team_knowledge(team_file)
            else:
                knowledge[team] = {"moves": [], "last_updated": None}
                
        return knowledge
    
    """
    Simplified parser replacement for knowledge_manager.py
    Replace the _parse_team_knowledge function with this version
    """

    def _parse_team_knowledge(self, file_path: Path) -> Dict:
        """Parse existing team offseason file to extract known moves - SIMPLIFIED VERSION"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        moves = []
        
        # Define common NFL positions for validation
        valid_positions = {
            'QB', 'RB', 'WR', 'TE', 'LT', 'LG', 'C', 'RG', 'RT', 'G', 'OL', 'OT',
            'DE', 'DT', 'LB', 'CB', 'S', 'FS', 'SS', 'K', 'P', 'LS', 'EDGE', 'NT'
        }
        
        # Pattern 1: **Player Name (POS)** - most reliable pattern
        pattern1 = r'\*\*([A-Za-z\'\.\-\s]{3,25})\s*\(([A-Z]{1,4})\)\*\*'
        matches1 = re.findall(pattern1, content)
        
        for match in matches1:
            player_name = match[0].strip()
            position = match[1].strip()
            
            # Only include if position looks valid and name looks like a person
            if (position in valid_positions and 
                self._looks_like_player_name(player_name)):
                
                move_type = self._guess_move_type_from_context(content, player_name)
                contract = self._extract_simple_contract(content, player_name)
                
                moves.append({
                    'player_name': player_name,
                    'position': position,
                    'move_type': move_type,
                    'contract': contract
                })
        
        # Pattern 2: **Player Name** followed by position context
        pattern2 = r'\*\*([A-Za-z\'\.\-\s]{3,25})\*\*[^\n]*?(?:signed|acquired|traded|drafted)[^\n]*?\b([A-Z]{2,4})\b'
        matches2 = re.findall(pattern2, content, re.IGNORECASE)
        
        for match in matches2:
            player_name = match[0].strip()
            position = match[1].strip()
            
            # Skip if we already have this player
            if any(move['player_name'] == player_name for move in moves):
                continue
                
            if (position in valid_positions and 
                self._looks_like_player_name(player_name)):
                
                move_type = self._guess_move_type_from_context(content, player_name)
                contract = self._extract_simple_contract(content, player_name)
                
                moves.append({
                    'player_name': player_name,
                    'position': position,
                    'move_type': move_type,
                    'contract': contract
                })
        
        # Pattern 3: Draft picks with "Pick #X: Player Name"
        draft_pattern = r'(?:Pick\s+#?\d+|Round\s+\d+)[^\n]*?\*\*([A-Za-z\'\.\-\s]{3,25})\*\*[^\n]*?\b([A-Z]{2,4})\b'
        draft_matches = re.findall(draft_pattern, content, re.IGNORECASE)
        
        for match in draft_matches:
            player_name = match[0].strip()
            position = match[1].strip()
            
            if (position in valid_positions and 
                self._looks_like_player_name(player_name) and
                not any(move['player_name'] == player_name for move in moves)):
                
                moves.append({
                    'player_name': player_name,
                    'position': position,
                    'move_type': 'Draft Pick',
                    'contract': 'Rookie Contract'
                })
        
        return {
            "moves": moves,
            "last_updated": datetime.now().isoformat(),
            "content_hash": hashlib.md5(content.encode()).hexdigest()
        }

    def _looks_like_player_name(self, name: str) -> bool:
        """Quick check if string looks like a player name"""
        name = name.strip()
        
        # Basic length check
        if len(name) < 3 or len(name) > 25:
            return False
        
        # Must be mostly letters and spaces
        if not re.match(r'^[A-Za-z\'\.\-\s]+$', name):
            return False
        
        # Skip obvious non-names
        skip_words = [
            'signing', 'signed', 'contract', 'deal', 'year', 'million', 'team',
            'player', 'addition', 'analysis', 'context', 'overview', 'summary',
            'addressed', 'remaining', 'coach', 'coordinator', 'extension',
            'restructure', 'cap', 'money', 'savings', 'space', 'budget',
            'value', 'price', 'grade', 'performance', 'impact', 'change'
        ]
        
        name_lower = name.lower()
        if any(word in name_lower for word in skip_words):
            return False
        
        # Should have at least one space (first last name) or be a known single name
        words = name.split()
        if len(words) == 1 and len(name) < 4:
            return False
        
        return True

    def _guess_move_type_from_context(self, content: str, player_name: str) -> str:
        """Guess move type based on context around player name"""
        # Find the player's name in content
        name_index = content.find(player_name)
        if name_index == -1:
            return 'Unknown'
        
        # Get surrounding context (1000 chars before and after)
        start = max(0, name_index - 1000)
        end = min(len(content), name_index + 1000)
        context = content[start:end].lower()
        
        # Check for keywords in context
        if any(word in context for word in ['signed', 'signing', 'free agent']):
            if any(word in context for word in ['departed', 'left', 'joined', 'new team']):
                return 'Free Agent Loss'
            else:
                return 'Free Agent Signing'
        elif any(word in context for word in ['traded', 'acquired', 'sent', 'received']):
            return 'Trade'
        elif any(word in context for word in ['draft', 'pick', 'round', 'selected']):
            return 'Draft Pick'
        elif any(word in context for word in ['retired', 'retirement']):
            return 'Retirement'
        elif any(word in context for word in ['released', 'cut', 'waived']):
            return 'Release'
        else:
            return 'Unknown'

    def _extract_simple_contract(self, content: str, player_name: str) -> str:
        """Extract contract info near player name"""
        name_index = content.find(player_name)
        if name_index == -1:
            return 'Unknown'
        
        # Get text around player name
        start = max(0, name_index - 200)
        end = min(len(content), name_index + 500)
        context = content[start:end]
        
        # Look for contract patterns
        patterns = [
            r'(\d+\s*years?\s*[,\s]*\$[\d,\.]+\s*million)',
            r'(\$[\d,\.]+\s*million)',
            r'(\d+\-year[^\n]*?\$[\d,\.]+[^\n]*?)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, context, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return 'Unknown'
    
    def _extract_players_from_section(self, section: str, section_type: str) -> List[Dict]:
        """Extract player names from a specific section with known type"""
        moves = []
        
        # Pattern 1: **Player Name (Position)** - most common in your files
        pattern1 = r'\*\*([A-Za-z\'\.\s]{2,30})\s*\(([A-Z]{1,4})\)\*\*'
        matches1 = re.findall(pattern1, section)
        
        for match in matches1:
            player_name = match[0].strip()
            position = match[1].strip()
            
            # Skip if this looks like a section header or random text
            if self._is_valid_player_name(player_name):
                moves.append({
                    'player_name': player_name,
                    'position': position,
                    'move_type': section_type,
                    'contract': self._extract_contract_from_context(section, player_name)
                })
        
        # Pattern 2: **Player Name** followed by position info
        pattern2 = r'\*\*([A-Za-z\'\.\s]{2,30})\*\*[^\n]*?(?:signed|acquired|traded|drafted)[^\n]*?(\([A-Z]{1,4}\)|\b[A-Z]{1,4}\b)'
        matches2 = re.findall(pattern2, section, re.IGNORECASE)
        
        for match in matches2:
            player_name = match[0].strip()
            position_raw = match[1].strip()
            position = re.sub(r'[^\w]', '', position_raw)  # Clean position
            
            if self._is_valid_player_name(player_name) and len(position) <= 4:
                # Check if we already have this player
                if not any(move['player_name'] == player_name for move in moves):
                    moves.append({
                        'player_name': player_name,
                        'position': position,
                        'move_type': section_type,
                        'contract': self._extract_contract_from_context(section, player_name)
                    })
        
        # Pattern 3: Draft picks with different format
        if section_type == 'Draft Pick':
            draft_pattern = r'(?:Round\s+\d+|Pick\s+#?\d+)[^\n]*?\*\*([A-Za-z\'\.\s]{2,30})\*\*[^\n]*?(?:\(([A-Z]{1,4}),|\b([A-Z]{1,4})\b)'
            draft_matches = re.findall(draft_pattern, section, re.IGNORECASE)
            
            for match in draft_matches:
                player_name = match[0].strip()
                position = (match[1] or match[2]).strip()
                
                if self._is_valid_player_name(player_name):
                    moves.append({
                        'player_name': player_name,
                        'position': position,
                        'move_type': 'Draft Pick',
                        'contract': 'Rookie Contract'
                    })
        
        return moves
    
    def _is_valid_player_name(self, name: str) -> bool:
        """Check if a string looks like a valid player name"""
        name = name.strip()
        
        # Must be reasonable length
        if len(name) < 3 or len(name) > 30:
            return False
        
        # Must contain at least one letter
        if not re.search(r'[A-Za-z]', name):
            return False
        
        # Skip common false positives
        skip_words = [
            'signing', 'signed', 'contract', 'deal', 'year', 'million', 'guaranteed',
            'previous', 'former', 'team', 'player', 'addition', 'departure', 'loss',
            'analysis', 'context', 'overview', 'summary', 'grade', 'performance',
            'addressed', 'remaining', 'coached', 'coordinator', 'assistant', 'hire',
            'retained', 'fired', 'promoted', 'extension', 'restructure', 'cap',
            'dead money', 'savings', 'space', 'budget', 'cost', 'value', 'price'
        ]
        
        name_lower = name.lower()
        if any(word in name_lower for word in skip_words):
            return False
        
        # Must look like a person's name (at least 2 words or common single names)
        words = name.split()
        if len(words) == 1:
            # Allow common single names or initials
            if len(name) < 3 or name.isupper():
                return False
        
        # Skip if it's mostly numbers or special characters
        if len(re.sub(r'[A-Za-z\s\']', '', name)) > len(name) * 0.3:
            return False
        
        return True
    
    def _extract_contract_from_context(self, section: str, player_name: str) -> str:
        """Try to find contract details for a player in the section"""
        # Look for contract info near the player's name
        name_index = section.find(player_name)
        if name_index == -1:
            return 'Unknown'
        
        # Get text around the player's name (500 chars before and after)
        start = max(0, name_index - 500)
        end = min(len(section), name_index + 500)
        context = section[start:end]
        
        # Look for contract patterns
        contract_patterns = [
            r'(\d+\s*years?\s*,?\s*\$[\d,\.]+(?:\s*million|M)?)',
            r'(\$[\d,\.]+(?:\s*million|M)?(?:\s*over\s*\d+\s*years?)?)',
            r'(\d+\-year[^\n]*?\$[\d,\.]+[^\n]*?)'
        ]
        
        for pattern in contract_patterns:
            match = re.search(pattern, context, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return 'Unknown'
    
    def _clean_and_dedupe_moves(self, moves: List[Dict]) -> List[Dict]:
        """Remove duplicates and clean up the moves list"""
        seen_players = set()
        clean_moves = []
        
        for move in moves:
            player_name = move['player_name'].strip()
            player_key = player_name.lower()
            
            # Skip if we've already seen this player
            if player_key in seen_players:
                continue
            
            # Skip if player name is clearly invalid
            if not self._is_valid_player_name(player_name):
                continue
            
            seen_players.add(player_key)
            clean_moves.append(move)
        
        return clean_moves
    
    def detect_new_moves(self, team: str, new_content: str) -> List[PlayerMove]:
        """Compare new content against existing knowledge to find new moves"""
        current_knowledge = self.team_knowledge.get(team, {"moves": []})
        known_players = {move.get('player_name', '').lower() for move in current_knowledge["moves"]}
        
        new_moves = []
        
        # Parse new content for moves (simplified - could be enhanced)
        new_players_found = self._extract_players_from_content(new_content)
        
        for player_data in new_players_found:
            if player_data['name'].lower() not in known_players:
                new_move = PlayerMove(
                    player_name=player_data['name'],
                    position=player_data.get('position', 'Unknown'),
                    from_team=player_data.get('from_team', 'Unknown'),
                    to_team=team,
                    move_type=player_data.get('move_type', 'Unknown'),
                    date_detected=datetime.now().isoformat(),
                    source='Manual Content Analysis'
                )
                new_moves.append(new_move)
                
        return new_moves
    
    def _extract_players_from_content(self, content: str) -> List[Dict]:
        """Extract player information from new content"""
        # This is a simplified version - you'd want more sophisticated parsing
        players = []
        
        # Look for player names in bold followed by position
        pattern = r'\*\*(.*?)\*\*.*?\((.*?)\)'
        matches = re.findall(pattern, content)
        
        for match in matches:
            players.append({
                'name': match[0].strip(),
                'position': match[1].strip(),
                'move_type': 'Free Agent Signing'  # Default assumption
            })
            
        return players
    
    def add_new_moves(self, team: str, new_moves: List[PlayerMove]) -> bool:
        """Add new moves to team's knowledge base"""
        if not new_moves:
            return False
            
        # Update in-memory knowledge
        if team not in self.team_knowledge:
            self.team_knowledge[team] = {"moves": [], "last_updated": None}
            
        for move in new_moves:
            move_dict = {
                'player_name': move.player_name,
                'position': move.position,
                'from_team': move.from_team,
                'to_team': move.to_team,
                'move_type': move.move_type,
                'date_detected': move.date_detected,
                'source': move.source
            }
            self.team_knowledge[team]["moves"].append(move_dict)
            
        # Save daily update log
        self._save_daily_update(team, new_moves)
        
        # Update team's main offseason file
        self._update_team_offseason_file(team, new_moves)
        
        return True
    
    def _save_daily_update(self, team: str, new_moves: List[PlayerMove]):
        """Save daily update for tracking and verification"""
        today = datetime.now().strftime("%Y%m%d")
        update_file = self.daily_updates_path / f"{team}_{today}_update.json"
        
        update_data = {
            "team": team,
            "date": datetime.now().isoformat(),
            "new_moves": [
                {
                    "player_name": move.player_name,
                    "position": move.position,
                    "from_team": move.from_team,
                    "to_team": move.to_team,
                    "move_type": move.move_type,
                    "date_detected": move.date_detected,
                    "source": move.source
                }
                for move in new_moves
            ]
        }
        
        with open(update_file, 'w') as f:
            json.dump(update_data, f, indent=2)
    
    def _update_team_offseason_file(self, team: str, new_moves: List[PlayerMove]):
        """Append new moves to team's main offseason markdown file"""
        team_file = self.knowledge_path / f"{team.lower()}_offseason_2025.md"
        
        # Create new section for recently detected moves
        new_section = f"\n\n## Recently Detected Moves ({datetime.now().strftime('%Y-%m-%d')})\n\n"
        
        for move in new_moves:
            new_section += f"**{move.player_name}** ({move.position})\n"
            new_section += f"- **Move Type:** {move.move_type}\n"
            new_section += f"- **From:** {move.from_team} → **To:** {move.to_team}\n"
            new_section += f"- **Detected:** {move.date_detected}\n"
            new_section += f"- **Source:** {move.source}\n\n"
        
        # Append to existing file or create new one
        if team_file.exists():
            with open(team_file, 'a', encoding='utf-8') as f:
                f.write(new_section)
        else:
            # Create new file with header
            with open(team_file, 'w', encoding='utf-8') as f:
                f.write(f"# {team} 2025 Offseason Moves\n\n")
                f.write("*Automatically tracked and updated*\n")
                f.write(new_section)
    
    def get_team_summary(self, team: str) -> Dict:
        """Get summary of team's offseason moves"""
        knowledge = self.team_knowledge.get(team, {"moves": []})
        moves = knowledge["moves"]
        
        summary = {
            "team": team,
            "total_moves": len(moves),
            "move_types": {},
            "recent_moves": [],
            "last_updated": knowledge.get("last_updated")
        }
        
        # Categorize moves
        for move in moves:
            move_type = move.get('move_type', 'Unknown')
            summary["move_types"][move_type] = summary["move_types"].get(move_type, 0) + 1
            
        # Get most recent moves (last 5)
        recent_moves = sorted(moves, key=lambda x: x.get('date_detected', ''), reverse=True)[:5]
        summary["recent_moves"] = recent_moves
        
        return summary
    
    def export_for_ranking_system(self, team: str) -> List[Dict]:
        """Export team moves in format for ranking system integration"""
        knowledge = self.team_knowledge.get(team, {"moves": []})
        
        # Convert to ranking system format
        ranking_moves = []
        for move in knowledge["moves"]:
            ranking_move = {
                'player_name': move['player_name'],
                'position': move.get('position', 'Unknown'),
                'from_team': move.get('from_team', 'Unknown'),
                'to_team': move.get('to_team', team),
                'move_type': move.get('move_type', 'Free Agent Signing'),
                'contract_years': 0,  # Would need to parse from contract details
                'contract_value': 0,  # Would need to parse from contract details
                '2024_grade': 0.0,  # Would need external data source
                'projected_2025_grade': 0.0,  # Would need analysis
                'snap_percentage_2024': 0.0,  # Would need external data
                'importance_to_old_team': 5.0,  # Default - could be enhanced
                'importance_to_new_team': 5.0,  # Default - could be enhanced
                'impact_score': 0.0  # Would be calculated by ranking system
            }
            ranking_moves.append(ranking_move)
            
        return ranking_moves
    
    def generate_system_report(self) -> Dict:
        """Generate comprehensive report of current system state"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "teams_tracked": len(self.nfc_east_teams),
            "total_moves_tracked": 0,
            "team_summaries": {},
            "system_health": "Good"
        }
        
        for team in self.nfc_east_teams:
            team_summary = self.get_team_summary(team)
            report["team_summaries"][team] = team_summary
            report["total_moves_tracked"] += team_summary["total_moves"]
            
        return report


def main():
    """Example usage of the Offseason Knowledge Manager"""
    
    # Initialize the system (you'd set your actual project root)
    project_root = "/path/to/nfl-betting-analytics"
    manager = OffseasonKnowledgeManager(project_root)
    
    # Generate system report
    report = manager.generate_system_report()
    print("🏈 NFL Offseason Knowledge Management System")
    print("=" * 50)
    print(f"📊 Total moves tracked: {report['total_moves_tracked']}")
    print(f"🏟️  Teams monitored: {', '.join(manager.nfc_east_teams)}")
    
    # Show team summaries
    for team, summary in report["team_summaries"].items():
        print(f"\n{team}: {summary['total_moves']} moves")
        for move_type, count in summary["move_types"].items():
            print(f"  - {move_type}: {count}")
    
    return manager


if __name__ == "__main__":
    manager = main()
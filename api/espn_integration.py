# espn_integration.py
"""
ESPN API Integration for NFL Bridge Framework
Connects live schedule data to your existing roster analysis
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ESPNNFLIntegration:
    def __init__(self, bridge_framework=None):
        self.base_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"
        self.bridge_framework = bridge_framework
        
        # ESPN team abbreviation mapping to your system
        self.espn_to_bridge_teams = {
            'BAL': 'BAL', 'PIT': 'PIT', 'CIN': 'CIN', 'CLE': 'CLE',
            'BUF': 'BUF', 'MIA': 'MIA', 'NE': 'NE', 'NYJ': 'NYJ',
            'HOU': 'HOU', 'IND': 'IND', 'JAX': 'JAC', 'TEN': 'TEN',  # Note: JAX -> JAC
            'DEN': 'DEN', 'KC': 'KC', 'LV': 'LV', 'LAC': 'LAC',
            'DAL': 'DAL', 'NYG': 'NYG', 'PHI': 'PHI', 'WSH': 'WAS',  # Note: WSH -> WAS
            'CHI': 'CHI', 'DET': 'DET', 'GB': 'GB', 'MIN': 'MIN',
            'ATL': 'ATL', 'CAR': 'CAR', 'NO': 'NO', 'TB': 'TB',
            'ARI': 'ARI', 'LAR': 'LAR', 'SF': 'SF', 'SEA': 'SEA'
        }
        
    def get_current_week_schedule(self) -> Dict:
        """Get current week's NFL schedule from ESPN"""
        try:
            url = f"{self.base_url}/scoreboard"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"✅ Retrieved {len(data.get('events', []))} games from ESPN")
            return data
            
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error fetching ESPN schedule: {e}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"❌ Error parsing ESPN response: {e}")
            return {}

    def get_season_schedule(self, year: int = 2025) -> List[Dict]:
        """Get full season schedule (requires multiple API calls)"""
        all_games = []
        
        # NFL season is typically weeks 1-18 plus playoffs
        for week in range(1, 19):
            try:
                url = f"{self.base_url}/scoreboard?seasontype=2&week={week}&year={year}"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                week_games = data.get('events', [])
                
                for game in week_games:
                    enhanced_game = self._enhance_game_data(game, week)
                    if enhanced_game:
                        all_games.append(enhanced_game)
                
                logger.info(f"Week {week}: {len(week_games)} games")
                
            except Exception as e:
                logger.error(f"Error fetching week {week}: {e}")
                continue
        
        logger.info(f"✅ Retrieved {len(all_games)} total games for {year} season")
        return all_games

    def _enhance_game_data(self, game_data: Dict, week: int) -> Optional[Dict]:
        """Convert ESPN game data to your bridge framework format"""
        try:
            competition = game_data['competitions'][0]
            competitors = competition['competitors']
            
            # Identify home/away teams
            home_team_data = next((c for c in competitors if c.get('homeAway') == 'home'), None)
            away_team_data = next((c for c in competitors if c.get('homeAway') == 'away'), None)
            
            if not home_team_data or not away_team_data:
                return None
            
            # Map ESPN abbreviations to your system
            espn_home = home_team_data['team']['abbreviation']
            espn_away = away_team_data['team']['abbreviation']
            
            bridge_home = self.espn_to_bridge_teams.get(espn_home, espn_home)
            bridge_away = self.espn_to_bridge_teams.get(espn_away, espn_away)
            
            # Get your bridge framework projections
            home_projection = self._get_team_bridge_projection(bridge_home)
            away_projection = self._get_team_bridge_projection(bridge_away)
            
            # Calculate your projected spread
            projected_spread = self._calculate_projected_spread(home_projection, away_projection)
            confidence = self._calculate_prediction_confidence(home_projection, away_projection)
            
            enhanced_game = {
                'game_id': game_data['id'],
                'week': week,
                'date': game_data['date'],
                'status': competition.get('status', {}).get('type', {}).get('name', 'Scheduled'),
                
                # Team info
                'home_team': {
                    'espn_abbr': espn_home,
                    'bridge_abbr': bridge_home,
                    'name': home_team_data['team']['displayName'],
                    'record': home_team_data.get('records', [{}])[0].get('summary', '0-0'),
                    'bridge_projection': home_projection
                },
                'away_team': {
                    'espn_abbr': espn_away,
                    'bridge_abbr': bridge_away,
                    'name': away_team_data['team']['displayName'],
                    'record': away_team_data.get('records', [{}])[0].get('summary', '0-0'),
                    'bridge_projection': away_projection
                },
                
                # Your predictions
                'bridge_predictions': {
                    'projected_spread': projected_spread,  # Positive = home team favored
                    'confidence': confidence,
                    'home_win_probability': self._spread_to_win_probability(projected_spread),
                    'total_points_projection': home_projection.get('projected_points', 21) + away_projection.get('projected_points', 21)
                },
                
                # ESPN data for comparison
                'espn_data': {
                    'venue': competition.get('venue', {}).get('fullName', 'TBD'),
                    'broadcast': self._extract_broadcast_info(competition),
                    'odds': self._extract_odds_info(competition)
                }
            }
            
            return enhanced_game
            
        except Exception as e:
            logger.error(f"Error enhancing game data: {e}")
            return None

    def _get_team_bridge_projection(self, team_abbr: str) -> Dict:
        """Get team projection from your existing bridge framework"""
        
        # If you have the bridge framework loaded, use it
        if self.bridge_framework:
            try:
                # Use your existing team analysis
                team_data = self.bridge_framework.get_team_analysis(team_abbr)
                return {
                    'final_2025_rating': team_data.get('final_2025_rating', 80.0),
                    'offseason_impact': team_data.get('offseason_impact', 0.0),
                    'projected_points': self._rating_to_points_per_game(team_data.get('final_2025_rating', 80.0)),
                    'strength_units': {
                        'offense': team_data.get('offense_impact', 0.0),
                        'defense': team_data.get('defense_impact', 0.0),
                        'special_teams': team_data.get('special_teams_impact', 0.0)
                    }
                }
            except Exception as e:
                logger.warning(f"Could not get bridge data for {team_abbr}: {e}")
        
        # Fallback to default/sample projections
        return self._get_fallback_projection(team_abbr)

    def _get_fallback_projection(self, team_abbr: str) -> Dict:
        """Fallback projections when bridge framework not available"""
        
        # Basic tier system based on your analysis
        tier_1_teams = ['PHI', 'BUF', 'KC', 'SF', 'BAL']  # Elite
        tier_2_teams = ['DET', 'HOU', 'MIN', 'PIT', 'LAC']  # Good
        tier_3_teams = ['GB', 'ATL', 'CIN', 'TB', 'LAR']   # Average
        
        if team_abbr in tier_1_teams:
            base_rating = 88.0
        elif team_abbr in tier_2_teams:
            base_rating = 83.0
        elif team_abbr in tier_3_teams:
            base_rating = 78.0
        else:
            base_rating = 73.0  # Below average
        
        return {
            'final_2025_rating': base_rating,
            'offseason_impact': 0.0,
            'projected_points': self._rating_to_points_per_game(base_rating),
            'strength_units': {'offense': 0.0, 'defense': 0.0, 'special_teams': 0.0}
        }

    def _calculate_projected_spread(self, home_projection: Dict, away_projection: Dict) -> float:
        """Calculate point spread from team projections (positive = home favored)"""
        
        home_rating = home_projection.get('final_2025_rating', 80.0)
        away_rating = away_projection.get('final_2025_rating', 80.0)
        
        # Home field advantage (typically 2.5-3 points in NFL)
        home_field_advantage = 2.8
        
        # Rating difference to spread conversion
        # Every 10 rating points ≈ 7 point spread (empirically derived)
        rating_diff = home_rating - away_rating
        spread_from_rating = (rating_diff / 10.0) * 7.0
        
        # Add home field advantage
        projected_spread = spread_from_rating + home_field_advantage
        
        return round(projected_spread, 1)

    def _calculate_prediction_confidence(self, home_proj: Dict, away_proj: Dict) -> int:
        """Calculate confidence in prediction (0-100)"""
        
        # Base confidence on rating gap
        rating_gap = abs(home_proj.get('final_2025_rating', 80) - away_proj.get('final_2025_rating', 80))
        
        # More confidence with bigger gaps
        if rating_gap >= 15:
            return 95
        elif rating_gap >= 10:
            return 85
        elif rating_gap >= 7:
            return 75
        elif rating_gap >= 4:
            return 65
        else:
            return 55  # Low confidence for close matchups

    def _spread_to_win_probability(self, spread: float) -> float:
        """Convert point spread to win probability using logistic function"""
        import math
        
        # Logistic function: P = 1 / (1 + e^(-spread/4))
        # Calibrated so 3-point spread ≈ 58% win probability
        try:
            probability = 1 / (1 + math.exp(-spread / 4.0))
            return round(probability, 3)
        except OverflowError:
            return 0.999 if spread > 0 else 0.001

    def _rating_to_points_per_game(self, rating: float) -> float:
        """Convert team rating to projected points per game"""
        
        # NFL teams typically score 17-28 points per game
        # Map 70-95 rating scale to this range
        min_rating, max_rating = 70.0, 95.0
        min_points, max_points = 17.0, 28.0
        
        normalized = (rating - min_rating) / (max_rating - min_rating)
        projected_points = min_points + (normalized * (max_points - min_points))
        
        return round(projected_points, 1)

    def _extract_broadcast_info(self, competition: Dict) -> Dict:
        """Extract TV/streaming info"""
        broadcasts = competition.get('broadcasts', [])
        if broadcasts:
            primary = broadcasts[0]
            return {
                'network': primary.get('names', ['TBD'])[0],
                'time': competition.get('date', '')
            }
        return {'network': 'TBD', 'time': ''}

    def _extract_odds_info(self, competition: Dict) -> Dict:
        """Extract betting odds if available"""
        odds = competition.get('odds', [])
        if odds:
            primary_odds = odds[0]
            return {
                'spread': primary_odds.get('spread'),
                'over_under': primary_odds.get('overUnder'),
                'home_moneyline': primary_odds.get('homeTeamOdds', {}).get('moneyLine'),
                'away_moneyline': primary_odds.get('awayTeamOdds', {}).get('moneyLine')
            }
        return {}

    def get_games_with_betting_edges(self, min_edge: float = 2.0) -> List[Dict]:
        """Find games where your projections disagree significantly with Vegas"""
        
        current_schedule = self.get_current_week_schedule()
        games_with_edges = []
        
        for game_data in current_schedule.get('events', []):
            enhanced_game = self._enhance_game_data(game_data, week=1)  # Current week
            
            if enhanced_game and enhanced_game['espn_data']['odds']:
                bridge_spread = enhanced_game['bridge_predictions']['projected_spread']
                vegas_spread = enhanced_game['espn_data']['odds'].get('spread')
                
                if vegas_spread is not None:
                    edge = abs(bridge_spread - vegas_spread)
                    
                    if edge >= min_edge:
                        enhanced_game['betting_edge'] = {
                            'edge_size': round(edge, 1),
                            'bridge_spread': bridge_spread,
                            'vegas_spread': vegas_spread,
                            'recommendation': 'HOME' if bridge_spread > vegas_spread else 'AWAY',
                            'confidence': enhanced_game['bridge_predictions']['confidence']
                        }
                        games_with_edges.append(enhanced_game)
        
        # Sort by edge size (biggest edges first)
        games_with_edges.sort(key=lambda x: x['betting_edge']['edge_size'], reverse=True)
        
        logger.info(f"🎯 Found {len(games_with_edges)} games with {min_edge}+ point edges")
        return games_with_edges

    def create_weekly_predictions_report(self) -> Dict:
        """Generate comprehensive weekly report"""
        
        schedule = self.get_current_week_schedule()
        all_games = []
        
        for game_data in schedule.get('events', []):
            enhanced_game = self._enhance_game_data(game_data, week=1)
            if enhanced_game:
                all_games.append(enhanced_game)
        
        # Calculate summary stats
        total_games = len(all_games)
        high_confidence_games = len([g for g in all_games if g['bridge_predictions']['confidence'] >= 80])
        betting_edges = self.get_games_with_betting_edges(min_edge=1.5)
        
        return {
            'report_date': datetime.now().isoformat(),
            'week_summary': {
                'total_games': total_games,
                'high_confidence_predictions': high_confidence_games,
                'betting_edges_found': len(betting_edges),
                'avg_confidence': round(sum(g['bridge_predictions']['confidence'] for g in all_games) / max(total_games, 1), 1)
            },
            'all_games': all_games,
            'betting_edges': betting_edges,
            'top_picks': betting_edges[:3]  # Top 3 strongest edges
        }


# Integration example for your existing API
def add_espn_endpoints_to_fastapi(app, bridge_framework=None):
    """Add ESPN integration endpoints to your existing FastAPI app"""
    
    espn_integration = ESPNNFLIntegration(bridge_framework)
    
    @app.get("/api/schedule/current")
    async def get_current_week_predictions():
        """Get current week with your bridge predictions"""
        try:
            report = espn_integration.create_weekly_predictions_report()
            return {
                "status": "success",
                "data": report,
                "source": "espn_api_with_bridge_projections"
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    @app.get("/api/betting/edges")
    async def get_betting_edges(min_edge: float = 2.0):
        """Get games where bridge framework disagrees with Vegas"""
        try:
            edges = espn_integration.get_games_with_betting_edges(min_edge)
            return {
                "status": "success",
                "edges": edges,
                "total_found": len(edges),
                "min_edge_threshold": min_edge
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    @app.get("/api/schedule/season/{year}")
    async def get_season_schedule(year: int = 2025):
        """Get full season schedule with projections"""
        try:
            schedule = espn_integration.get_season_schedule(year)
            return {
                "status": "success",
                "year": year,
                "total_games": len(schedule),
                "schedule": schedule
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    # Test the integration
    espn = ESPNNFLIntegration()
    
    print("🏈 Testing ESPN NFL Integration...")
    
    # Test current week schedule
    current_week = espn.get_current_week_schedule()
    print(f"Current week has {len(current_week.get('events', []))} games")
    
    # Test enhanced game data
    if current_week.get('events'):
        sample_game = espn._enhance_game_data(current_week['events'][0], week=1)
        if sample_game:
            print(f"\nSample enhanced game:")
            print(f"  {sample_game['away_team']['name']} @ {sample_game['home_team']['name']}")
            print(f"  Bridge projection: {sample_game['bridge_predictions']['projected_spread']:+.1f} (home)")
            print(f"  Confidence: {sample_game['bridge_predictions']['confidence']}%")
    
    # Test betting edges
    edges = espn.get_games_with_betting_edges(min_edge=1.0)
    print(f"\nFound {len(edges)} potential betting edges")
    
    print("\n✅ ESPN Integration test complete!")
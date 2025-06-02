"""
New Orleans Saints 2025 Offseason Moves
Complete analysis of coaching overhaul and quarterback transition amid cap constraints
"""

SAINTS_2025_MOVES = [
    # SAINTS MAJOR FREE AGENT SIGNINGS - Strategic additions despite cap constraints
    {
        'player_name': 'Justin Reid',
        'position': 'S',
        'from_team': 'KC',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 31500000,
        '2024_grade': 8.2,  # Championship experience, versatile safety
        'projected_2025_grade': 8.0,  # Should maintain high level
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,  # KC defensive leader
        'importance_to_new_team': 9.0,  # Critical safety upgrade
    },
    {
        'player_name': 'Brandin Cooks',
        'position': 'WR2',
        'from_team': 'Dal',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,  # Estimated
        '2024_grade': 7.5,  # Still productive veteran
        'projected_2025_grade': 7.8,  # Returning home boost
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,  # Veteran presence
        'importance_to_new_team': 8.5,  # Proven receiver for new offense
    },
    {
        'player_name': 'Isaac Yiadom',
        'position': 'CB2',
        'from_team': 'SF',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 18000000,  # Estimated
        '2024_grade': 7.2,  # Solid corner in SF system
        'projected_2025_grade': 7.5,  # Familiar with Saints system
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 8.0,  # Secondary rebuild
    },
    {
        'player_name': 'Chris Rumph II',
        'position': 'EDGE',
        'from_team': 'LAR',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,  # Pass rush depth
    },
    {
        'player_name': 'Jack Stoll',
        'position': 'TE',
        'from_team': 'Phi',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 4.5,
        'importance_to_new_team': 6.5,  # TE depth
    },
    {
        'player_name': 'Will Clapp',
        'position': 'C',
        'from_team': 'LAC',
        'to_team': 'NO',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 6.0,  # Interior line depth
    },
    
    # SAINTS MAJOR LOSSES - Cap casualties and departures
    {
        'player_name': 'Derek Carr',
        'position': 'QB',
        'from_team': 'NO',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Solid veteran production
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,  # Starting quarterback
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Paulson Adebo',
        'position': 'CB1',
        'from_team': 'NO',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Young corner with potential
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.0,  # Starting corner
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Will Harris',
        'position': 'S',
        'from_team': 'NO',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,  # Starting safety
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Payton Turner',
        'position': 'EDGE',
        'from_team': 'NO',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Disappointing first-round pick
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,  # Failed to develop
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jamaal Williams',
        'position': 'RB',
        'from_team': 'NO',
        'to_team': 'RELEASED',
        'move_type': 'Released',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,  # Backup RB
        'importance_to_new_team': 0.0,
    },
    
    # SAINTS TRADES - Lattimore deal and minor moves
    {
        'player_name': 'Marshon Lattimore',
        'position': 'CB1',
        'from_team': 'NO',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # Four-time Pro Bowler
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.5,  # Franchise cornerback
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'John Ridgeway III',
        'position': 'DT',
        'from_team': 'Was',
        'to_team': 'NO',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 3000000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 6.5,  # Interior line depth
    },
    
    # SAINTS 2025 DRAFT - Inside-out building with 9 picks
    {
        'player_name': 'Kelvin Banks Jr.',
        'position': 'LT',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #9',
        'contract_years': 4,
        'contract_value': 33000000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 8.0,  # Outland Trophy winner, All-American
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Immediate starter, franchise LT
    },
    {
        'player_name': 'Tyler Shough',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #40',
        'contract_years': 4,
        'contract_value': 9500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 3,569 yards, 28 TDs at Louisville
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Likely Week 1 starter after Carr retirement
    },
    {
        'player_name': 'Vernon Broughton',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #71',
        'contract_years': 4,
        'contract_value': 5800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Athletic interior lineman
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Interior line help
    },
    {
        'player_name': 'Jonas Sanker',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #93',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # Team captain at Virginia
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Safety depth
    },
    {
        'player_name': 'Danny Stutsman',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #112',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # Butkus Award finalist, 109 tackles
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Future at linebacker
    },
    {
        'player_name': 'Quincy Riley',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #131',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 15 career interceptions
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # CB depth from Lattimore trade
    },
    {
        'player_name': 'Devin Neal',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'NO',
        'move_type': '2025 Draft Pick #184',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 3,636 yards, 41 TDs over 3 seasons
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # RB2 potential behind Kamara
    },
    
    # SAINTS KEY RE-SIGNINGS - Core retention
    {
        'player_name': 'Chase Young',
        'position': 'EDGE',
        'from_team': 'NO',
        'to_team': 'NO',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 51000000,
        '2024_grade': 8.5,  # Career-high 5.5 sacks, 66 QB pressures
        'projected_2025_grade': 8.8,  # Entering prime
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.0,  # Defensive cornerstone
    },
    {
        'player_name': 'Juwan Johnson',
        'position': 'TE',
        'from_team': 'NO',
        'to_team': 'NO',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 30000000,
        '2024_grade': 7.5,  # Top tight end
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Key offensive weapon
    },
    {
        'player_name': 'Tyrann Mathieu',
        'position': 'S',
        'from_team': 'NO',
        'to_team': 'NO',
        'move_type': 'Restructured Contract',
        'contract_years': 1,
        'contract_value': 8000000,  # Estimated restructure
        '2024_grade': 7.8,  # Veteran leadership
        'projected_2025_grade': 7.5,  # Aging but productive
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.5,  # Defensive leader
        'importance_to_new_team': 9.0,  # Critical veteran presence
    },
    {
        'player_name': 'Cedrick Wilson Jr.',
        'position': 'WR3',
        'from_team': 'NO',
        'to_team': 'NO',
        'move_type': 'Restructured Contract',
        'contract_years': 2,
        'contract_value': 6000000,  # Estimated
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Receiver depth
    },
    
    # SAINTS COACHING CHANGES
    {
        'player_name': 'Dennis Allen',
        'position': 'COACH',
        'from_team': 'NO',
        'to_team': 'Chi',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # Fired after 2-7 start
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 9.0,  # Head coach
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kellen Moore',
        'position': 'COACH',
        'from_team': 'Phi',
        'to_team': 'NO',
        'move_type': 'Coaching Hire',
        'contract_years': 4,
        'contract_value': 25000000,  # Estimated
        '2024_grade': 9.0,  # Super Bowl champion OC
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Franchise transformation
    },
]

# SAINTS SUMMARY METRICS
SAINTS_2025_SUMMARY = {
    'total_moves': len(SAINTS_2025_MOVES),
    'free_agent_signings': 6,
    'major_losses': 5,
    'draft_picks': 7,
    'key_resignings': 4,
    'trades': 2,
    'coaching_changes': 2,
    'total_guaranteed_money': 85000000,  # Strategic spending despite cap issues
    'dead_money': 52600000,  # 18.8% of cap - massive burden
    'cap_space_projected_2026': 37000000,  # Healthiest outlook in years
    'championship_window': '2026-2028',
    'offseason_grade': 'B+',
    'key_philosophy': 'Complete organizational reset with youth movement and cap flexibility'
}

if __name__ == "__main__":
    print(f"New Orleans Saints 2025 Offseason: {SAINTS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {SAINTS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {SAINTS_2025_SUMMARY['championship_window']}")
    print(f"Dead Money Burden: ${SAINTS_2025_SUMMARY['dead_money']:,}")
    print(f"Philosophy: {SAINTS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: Reid (S), Shough (QB), Banks (LT), Moore (HC)")
    print(f"Key Losses: Carr (retirement), Lattimore (trade), Adebo (FA)")
    print(f"Strategy: Complete reset with Kellen Moore + rookie QB")
    print(f"Cap Situation: From $54M over to $37M projected space in 2026")
    print(f"Draft Focus: Inside-out building with 9 picks, most since 2015")
    print(f"Shocking Development: Carr's retirement accelerated QB transition")
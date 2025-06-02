"""
Minnesota Vikings 2025 Offseason Moves
Complete analysis of historic $245 million spending spree under Kwesi Adofo-Mensah and Kevin O'Connell
"""

VIKINGS_2025_MOVES = [
    # VIKINGS FREE AGENT SIGNINGS - Historic $245M spending spree
    {
        'player_name': 'Jonathan Allen',
        'position': 'DT',
        'from_team': 'Was',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        '2024_grade': 6.5,  # Injury-limited to 8 games, torn pectoral
        'projected_2025_grade': 8.0,  # Pro Bowl talent when healthy
        'snap_percentage_2024': 50.0,  # Limited by injury
        'importance_to_old_team': 8.0,  # 8-year Commanders cornerstone
        'importance_to_new_team': 8.5,  # Interior pass rush upgrade
    },
    {
        'player_name': 'Javon Hargrave',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 30000000,
        '2024_grade': 7.0,  # Injury concerns but proven production
        'projected_2025_grade': 8.2,  # Elite interior pass rusher
        'snap_percentage_2024': 60.0,  # Managed snaps due to injury
        'importance_to_old_team': 7.5,  # 49ers defensive line depth
        'importance_to_new_team': 8.5,  # Defensive line transformation
    },
    {
        'player_name': 'Will Fries',
        'position': 'G',
        'from_team': 'Ind',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 5,
        'contract_value': 88000000,
        '2024_grade': 7.8,  # Solid Colts starter
        'projected_2025_grade': 8.0,  # Interior line anchor
        'snap_percentage_2024': 85.0,  # Full-time starter
        'importance_to_old_team': 7.5,  # Key Colts lineman
        'importance_to_new_team': 9.0,  # Addresses 9-sack playoff disaster
    },
    {
        'player_name': 'Ryan Kelly',
        'position': 'C',
        'from_team': 'Ind',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 18000000,
        '2024_grade': 7.5,  # Veteran center experience
        'projected_2025_grade': 7.8,  # Instant chemistry with Fries
        'snap_percentage_2024': 80.0,  # Colts starter
        'importance_to_old_team': 7.5,  # Long-time Colts center
        'importance_to_new_team': 8.5,  # Interior line stability
    },
    {
        'player_name': 'Byron Murphy Jr.',
        'position': 'CB1',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 66000000,
        '2024_grade': 8.5,  # First Pro Bowl season
        'projected_2025_grade': 8.7,  # Elite corner retention
        'snap_percentage_2024': 90.0,  # Lockdown corner
        'importance_to_old_team': 9.0,  # Breakout star retained
        'importance_to_new_team': 9.0,  # Cornerstone defensive back
    },
    {
        'player_name': 'Isaiah Rodgers',
        'position': 'CB2',
        'from_team': 'Phi',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 15000000,
        '2024_grade': 7.2,  # Super Bowl champion comeback story
        'projected_2025_grade': 7.5,  # Secondary depth addition
        'snap_percentage_2024': 65.0,  # Eagles contributor
        'importance_to_old_team': 6.5,  # Eagles depth piece
        'importance_to_new_team': 7.5,  # CB depth after losses
    },
    {
        'player_name': 'Andrew Van Ginkel',
        'position': 'EDGE',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Extension',
        'contract_years': 1,
        'contract_value': 23000000,
        '2024_grade': 8.8,  # Pro Bowl season (11.5 sacks, 2 pick-sixes)
        'projected_2025_grade': 8.5,  # Elite pass rusher
        'snap_percentage_2024': 85.0,  # Key defensive player
        'importance_to_old_team': 9.0,  # Breakout star retained
        'importance_to_new_team': 9.0,  # Pass rush cornerstone
    },
    {
        'player_name': 'Aaron Jones',
        'position': 'RB',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 7.8,  # Back-to-back 1,000-yard seasons
        'projected_2025_grade': 7.5,  # Veteran leadership at 31
        'snap_percentage_2024': 75.0,  # Primary back
        'importance_to_old_team': 8.0,  # Proven veteran back
        'importance_to_new_team': 8.0,  # Backfield stability
    },
    {
        'player_name': 'Jordan Mason',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 7.0,  # 49ers committee back
        'projected_2025_grade': 6.8,  # Committee approach depth
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 6.0,  # 49ers depth piece
        'importance_to_new_team': 6.5,  # RB room competition
    },

    # VIKINGS MAJOR LOSSES - QB exodus and cap casualties
    {
        'player_name': 'Sam Darnold',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.2,  # Career-best 35 TDs, Pro Bowl season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,  # Primary starter
        'importance_to_old_team': 8.5,  # Breakout season leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Daniel Jones',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Backup role contributor
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 10.0,  # Limited backup duty
        'importance_to_old_team': 6.0,  # Veteran backup depth
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Mullens',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Third-string quarterback
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 5.0,  # Emergency duty only
        'importance_to_old_team': 5.0,  # Depth quarterback
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Garrett Bradbury',
        'position': 'C',
        'from_team': 'Min',
        'to_team': 'FA',
        'move_type': 'Release (Post-June 1)',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Replaced by Kelly acquisition
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Former starter
        'importance_to_old_team': 6.5,  # $5.25M cap savings
        'importance_to_new_team': 0.0,
    },

    # VIKINGS 2025 NFL DRAFT - Limited capital but strategic picks
    {
        'player_name': 'Donovan Jackson',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Min',
        'move_type': '2025 Draft Pick #24',
        'contract_years': 4,
        'contract_value': 18500000,
        '2024_grade': 0.0,  # College - Ohio State versatile lineman
        'projected_2025_grade': 7.5,  # Immediate starter potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Interior line continued investment
    },
    {
        'player_name': 'Tai Felton',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'Min',
        'move_type': '2025 Draft Pick #78',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - Maryland (96 catches, 1,124 yards)
        'projected_2025_grade': 7.0,  # Addison insurance/depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # WR depth with Addison concerns
    },
    {
        'player_name': 'Kobe King',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Min',
        'move_type': '2025 Draft Pick #185',
        'contract_years': 4,
        'contract_value': 4100000,
        '2024_grade': 0.0,  # College - Penn State, called "best value pick" 6th round
        'projected_2025_grade': 6.8,  # Linebacker depth with upside
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # 4th round talent in 6th
    },
    {
        'player_name': 'Sam Howell',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 4500000,
        '2024_grade': 6.5,  # Seahawks backup experience
        'projected_2025_grade': 6.8,  # Veteran backup insurance
        'snap_percentage_2024': 15.0,  # Limited backup duty
        'importance_to_old_team': 6.0,  # Seahawks traded for pick
        'importance_to_new_team': 7.5,  # McCarthy insurance
    },

    # VIKINGS COACHING CONTINUITY - Stability after 14-3 success
    {
        'player_name': 'Kevin O\'Connell',
        'position': 'HC',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Extension',
        'contract_years': 5,
        'contract_value': 35000000,
        '2024_grade': 9.0,  # Coach of the Year after 14-3 season
        'projected_2025_grade': 9.0,  # Proven quarterback developer
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 10.0,  # Franchise cornerstone coach
        'importance_to_new_team': 10.0,  # McCarthy development key
    },
    {
        'player_name': 'Kwesi Adofo-Mensah',
        'position': 'GM',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 20000000,
        '2024_grade': 8.5,  # Orchestrated historic spending spree
        'projected_2025_grade': 8.5,  # Aggressive team building
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,  # Front office stability
        'importance_to_new_team': 9.5,  # Strategic vision continuity
    },
]

# VIKINGS SUMMARY METRICS
VIKINGS_2025_SUMMARY = {
    'total_moves': len(VIKINGS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 4,
    'trades': 2,
    'draft_picks': 4,
    'key_resignings': 3,
    'coaching_changes': 0,
    'total_guaranteed_money': 245470000,  # League-leading spending
    'salary_cap_space_remaining': 18000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'A-',
    'key_philosophy': 'Historic $245M spending spree to maximize McCarthy window',
    'biggest_concern': 'J.J. McCarthy development with minimal experience',
    'biggest_strength': 'Elite supporting cast with #2 defense and O\'Connell system',
    'key_risk': '2026 cap crunch from front-loaded contracts',
    'betting_implication': 'Legitimate Super Bowl contenders if McCarthy competent'
}

if __name__ == "__main__":
    print(f"Minnesota Vikings 2025 Offseason Moves: {VIKINGS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {VIKINGS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {VIKINGS_2025_SUMMARY['championship_window']}")
    print(f"Total Guaranteed Money: ${VIKINGS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {VIKINGS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {VIKINGS_2025_SUMMARY['biggest_concern']}")
    print(f"Key Risk: {VIKINGS_2025_SUMMARY['key_risk']}")
    print(f"Betting Implication: {VIKINGS_2025_SUMMARY['betting_implication']}")
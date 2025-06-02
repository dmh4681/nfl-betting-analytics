"""
Green Bay Packers 2025 Offseason Moves
Complete analysis of calculated rebuild around Jordan Love under Brian Gutekunst and Matt LaFleur
"""

PACKERS_2025_MOVES = [
    # PACKERS FREE AGENT SIGNINGS - Quality over quantity approach
    {
        'player_name': 'Nate Hobbs',
        'position': 'CB2',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 48000000,
        '2024_grade': 7.0,  # Missed 6 games but versatile coverage
        'projected_2025_grade': 7.8,  # Flexibility with Alexander injuries
        'snap_percentage_2024': 70.0,  # When healthy, key contributor
        'importance_to_old_team': 7.5,  # Raiders starting corner
        'importance_to_new_team': 8.5,  # Secondary depth crucial
    },
    {
        'player_name': 'Aaron Banks',
        'position': 'LG',
        'from_team': 'SF',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 77000000,
        '2024_grade': 8.5,  # Elite pass protection (1 sack in 775 snaps)
        'projected_2025_grade': 8.7,  # Enables Jenkins to center move
        'snap_percentage_2024': 95.0,  # 49ers starting guard
        'importance_to_old_team': 8.0,  # Key 49ers protection piece
        'importance_to_new_team': 9.0,  # Interior line transformation
    },
    {
        'player_name': 'Brandon McManus',
        'position': 'K',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 15300000,
        '2024_grade': 8.8,  # 95.2% field goal accuracy in 2024
        'projected_2025_grade': 8.5,  # Kicking stability finally achieved
        'snap_percentage_2024': 100.0,  # All kicking duties
        'importance_to_old_team': 8.5,  # Reliable kicker found
        'importance_to_new_team': 8.5,  # Position stability crucial
    },
    {
        'player_name': 'Isaiah McDuffie',
        'position': 'LB',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 7.0,  # Special teams ace and depth LB
        'projected_2025_grade': 7.2,  # Proven special teams value
        'snap_percentage_2024': 40.0,  # Rotational LB, full-time ST
        'importance_to_old_team': 7.5,  # Key special teams contributor
        'importance_to_new_team': 7.5,  # Special teams continuity
    },
    {
        'player_name': 'Mecole Hardman',
        'position': 'WR3',
        'from_team': 'KC',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,  # Limited role with Chiefs
        'projected_2025_grade': 6.8,  # Speed specialist prove-it deal
        'snap_percentage_2024': 35.0,  # Rotational receiver/returner
        'importance_to_old_team': 5.5,  # Chiefs depth piece
        'importance_to_new_team': 7.0,  # Speed element with Watson out
    },

    # PACKERS MAJOR LOSSES - Calculated departures and salary moves
    {
        'player_name': 'Josh Myers',
        'position': 'C',
        'from_team': 'GB',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Solid center play when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting center
        'importance_to_old_team': 7.0,  # Enables Jenkins move to center
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'T.J. Slaton',
        'position': 'DT',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Rotational defensive tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Part-time starter
        'importance_to_old_team': 6.5,  # Defensive line depth lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Eric Stokes',
        'position': 'CB2',
        'from_team': 'GB',
        'to_team': 'LV',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.5,  # No pass breakups since rookie year
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,  # Limited role due to struggles
        'importance_to_old_team': 4.0,  # Former 1st rounder bust
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'AJ Dillon',
        'position': 'RB',
        'from_team': 'GB',
        'to_team': 'Phi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 0.0,  # Missed entire 2024 season (neck injury)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,  # Injured reserve all season
        'importance_to_old_team': 5.0,  # Addition by subtraction
        'importance_to_new_team': 0.0,
    },

    # PACKERS CONTRACT EXTENSIONS - Building around Love era core
    {
        'player_name': 'Jordan Love',
        'position': 'QB',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 220000000,
        '2024_grade': 8.2,  # Franchise QB emergence confirmed
        'projected_2025_grade': 8.5,  # Continued development expected
        'snap_percentage_2024': 95.0,  # Established starter
        'importance_to_old_team': 10.0,  # Franchise cornerstone secured
        'importance_to_new_team': 10.0,  # $75M signing bonus (NFL record)
    },
    {
        'player_name': 'Devonte Wyatt',
        'position': 'DT',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': '5th Year Option',
        'contract_years': 1,
        'contract_value': 13920000,
        '2024_grade': 7.5,  # Development showing (12 career sacks)
        'projected_2025_grade': 7.8,  # Continued growth expected
        'snap_percentage_2024': 70.0,  # Rotational starter
        'importance_to_old_team': 7.5,  # Young core piece
        'importance_to_new_team': 7.5,  # Defensive line future
    },

    # PACKERS 2025 NFL DRAFT - Historic WR pick breaks 23-year drought
    {
        'player_name': 'Matthew Golden',
        'position': 'WR1',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #23',
        'contract_years': 4,
        'contract_value': 17800000,
        '2024_grade': 0.0,  # College - Texas (987 yards, 9 TDs, 4.29 speed)
        'projected_2025_grade': 7.5,  # Deep threat to replace Watson
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # First WR in Round 1 since 2002
    },
    {
        'player_name': 'Anthony Belton',
        'position': 'RT',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #56',
        'contract_years': 4,
        'contract_value': 8900000,
        '2024_grade': 0.0,  # College - NC State "Escalade" (6'8", 330 lbs)
        'projected_2025_grade': 6.5,  # Developmental tackle depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # OL depth project
    },
    {
        'player_name': 'Savion Williams',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #89',
        'contract_years': 4,
        'contract_value': 6100000,
        '2024_grade': 0.0,  # College - TCU (6'5" gadget player, threw TD)
        'projected_2025_grade': 6.8,  # Versatile receiver/returner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Red zone target and special teams
    },
    {
        'player_name': 'Barryn Sorrell',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #122',
        'contract_years': 4,
        'contract_value': 4700000,
        '2024_grade': 0.0,  # College - Texas (9.31 RAS score, Senior Bowl top DL)
        'projected_2025_grade': 7.0,  # Best value pick in class
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush depth addition
    },
    {
        'player_name': 'Kalen DeBoer Jr.',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #155',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - Alabama (coached by his father)
        'projected_2025_grade': 6.5,  # Developmental safety
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Secondary depth
    },
    {
        'player_name': 'Marcus Mbow',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #187',
        'contract_years': 4,
        'contract_value': 3900000,
        '2024_grade': 0.0,  # College - Purdue (interior line depth)
        'projected_2025_grade': 6.0,  # Guard competition
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Interior line depth
    },
    {
        'player_name': 'Connor Colby',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #221',
        'contract_years': 4,
        'contract_value': 3700000,
        '2024_grade': 0.0,  # College - Iowa State (blocking specialist)
        'projected_2025_grade': 6.2,  # Developmental tight end
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # TE depth
    },
    {
        'player_name': 'Cam Johnson',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'GB',
        'move_type': '2025 Draft Pick #254',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Arizona (linebacker depth)
        'projected_2025_grade': 6.0,  # Special teams contributor
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # LB depth and ST
    },

    # PACKERS COACHING CHANGES - Defensive improvements targeted
    {
        'player_name': 'DeMarcus Covington',
        'position': 'DL_COACH',
        'from_team': 'NE',
        'to_team': 'GB',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 2500000,
        '2024_grade': 7.5,  # 8-year Patriots tenure, 2024 DC experience
        'projected_2025_grade': 8.0,  # Pass rush improvement focus
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Patriots defensive coordinator
        'importance_to_new_team': 8.0,  # Pass rush development expertise
    },
    {
        'player_name': 'Luke Getsy',
        'position': 'OFF_ASST',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        '2024_grade': 6.5,  # Previous GB success (2019-21), recent coordinator struggles
        'projected_2025_grade': 7.5,  # Institutional knowledge return
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,  # Raiders coordinator departure
        'importance_to_new_team': 7.0,  # Rodgers MVP years experience
    },
]

# PACKERS SUMMARY METRICS
PACKERS_2025_SUMMARY = {
    'total_moves': len(PACKERS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 4,
    'trades': 0,
    'draft_picks': 8,
    'key_resignings': 2,
    'coaching_changes': 2,
    'total_guaranteed_money': 135000000,  # Conservative estimate
    'salary_cap_space_remaining': 29000000,
    'championship_window': '2025-2029',
    'offseason_grade': 'B+',
    'key_philosophy': 'Calculated rebuild around Love with targeted quality additions',
    'biggest_concern': 'Christian Watson ACL tear creates receiver uncertainty',
    'biggest_strength': 'Love secured long-term with improved protection and weapons',
    'key_risk': 'NFC North gauntlet with brutal late-season schedule',
    'draft_breakthrough': 'First WR in Round 1 since Javon Walker (2002)',
    'betting_implication': 'Conservative approach may struggle in loaded division'
}

if __name__ == "__main__":
    print(f"Green Bay Packers 2025 Offseason Moves: {PACKERS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {PACKERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {PACKERS_2025_SUMMARY['championship_window']}")
    print(f"Total Guaranteed Money: ${PACKERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {PACKERS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {PACKERS_2025_SUMMARY['biggest_concern']}")
    print(f"Draft Breakthrough: {PACKERS_2025_SUMMARY['draft_breakthrough']}")
    print(f"Key Risk: {PACKERS_2025_SUMMARY['key_risk']}")
    print(f"Betting Implication: {PACKERS_2025_SUMMARY['betting_implication']}")
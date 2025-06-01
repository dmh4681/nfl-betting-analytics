"""
New York Jets 2025 Offseason Moves
Complete analysis of culture reset and youth-focused rebuild under Aaron Glenn and Darren Mougey
"""

JETS_2025_MOVES = [
    # JETS FREE AGENT SIGNINGS - Youth movement with strategic value
    {
        'player_name': 'Justin Fields',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 40000000,
        '2024_grade': 6.8,  # 4-2 record as starter, dual-threat ability
        'projected_2025_grade': 7.5,  # Reunites with OSU teammates Wilson/Myers
        'snap_percentage_2024': 45.0,  # Limited role behind Wilson in Pittsburgh
        'importance_to_old_team': 6.5,  # Steelers backup with promise
        'importance_to_new_team': 9.0,  # Centerpiece QB replacement for Rodgers
    },
    {
        'player_name': 'Brandon Stephens',
        'position': 'CB1',
        'from_team': 'Bal',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 36000000,
        '2024_grade': 6.0,  # Allowed 806 receiving yards (2nd-most in NFL)
        'projected_2025_grade': 6.8,  # Change of scenery could help
        'snap_percentage_2024': 85.0,  # Ravens starter despite struggles
        'importance_to_old_team': 6.5,  # Ravens let walk after regression
        'importance_to_new_team': 7.5,  # Replaces D.J. Reed
    },
    {
        'player_name': 'Andre Cisco',
        'position': 'S',
        'from_team': 'Jac',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        '2024_grade': 6.5,  # Long Island native, Jaguars safety
        'projected_2025_grade': 7.0,  # Homecoming motivation
        'snap_percentage_2024': 70.0,  # Jacksonville starter
        'importance_to_old_team': 6.5,  # Jaguars depth safety
        'importance_to_new_team': 7.5,  # Critical safety need filled
    },
    {
        'player_name': 'Josh Myers',
        'position': 'C',
        'from_team': 'GB',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.8,  # Packers starting center
        'projected_2025_grade': 7.2,  # OSU connection with Fields/Wilson
        'snap_percentage_2024': 85.0,  # Green Bay starter
        'importance_to_old_team': 7.0,  # Packers lost starting center
        'importance_to_new_team': 7.0,  # Center competition and familiarity
    },
    {
        'player_name': 'Josh Reynolds',
        'position': 'WR2',
        'from_team': 'Den',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        '2024_grade': 6.5,  # Broncos veteran receiver
        'projected_2025_grade': 6.8,  # Coordinator connection
        'snap_percentage_2024': 60.0,  # Denver rotational receiver
        'importance_to_old_team': 6.0,  # Broncos depth piece
        'importance_to_new_team': 6.8,  # WR depth with coordinator familiarity
    },
    {
        'player_name': 'Kene Nwangwu',
        'position': 'RB',
        'from_team': 'Min',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 7.0,  # Special teams ace, return specialist
        'projected_2025_grade': 7.2,  # Elite return skills
        'snap_percentage_2024': 30.0,  # Limited offensive role, major special teams
        'importance_to_old_team': 6.5,  # Vikings special teams contributor
        'importance_to_new_team': 7.0,  # Special teams upgrade
    },
    {
        'player_name': 'Isaiah Oliver',
        'position': 'CB2',
        'from_team': 'SF',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2200000,
        '2024_grade': 6.0,  # 49ers versatile defensive back
        'projected_2025_grade': 6.3,  # Defensive back depth
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 5.5,  # 49ers depth piece
        'importance_to_new_team': 6.0,  # Versatile DB depth
    },
    {
        'player_name': 'Jamin Davis',
        'position': 'LB',
        'from_team': 'Was',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,  # Former first-round pick, Washington
        'projected_2025_grade': 6.5,  # Change of scenery candidate
        'snap_percentage_2024': 50.0,  # Limited Washington role
        'importance_to_old_team': 5.5,  # Commanders depth
        'importance_to_new_team': 6.0,  # LB depth and potential
    },

    # JETS KEY RE-SIGNINGS - Ascending young talent prioritized
    {
        'player_name': 'Jamien Sherwood',
        'position': 'LB',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 45000000,
        '2024_grade': 8.5,  # League-high 98 solo tackles, breakout star
        'projected_2025_grade': 8.8,  # Top-5 paid off-ball linebacker
        'snap_percentage_2024': 95.0,  # Starting linebacker
        'importance_to_old_team': 9.0,  # Defensive leader and tackling machine
        'importance_to_new_team': 9.0,  # Cornerstone of new defense
    },
    {
        'player_name': 'Tucker Fisk',
        'position': 'TE',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Exclusive Rights Tender',
        'contract_years': 1,
        'contract_value': 1000000,
        '2024_grade': 6.0,  # Tight end depth
        'projected_2025_grade': 6.2,  # TE development
        'snap_percentage_2024': 25.0,  # Limited role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 5.5,  # TE depth retention
    },

    # JETS MAJOR LOSSES - Cap purge and veteran exodus
    {
        'player_name': 'Aaron Rodgers',
        'position': 'QB',
        'from_team': 'NYJ',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # 5-12 record, career worsts in multiple categories
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Starting QB despite struggles
        'importance_to_old_team': 6.0,  # Failed "celebrity quarterback" experiment
        'importance_to_new_team': 0.0,  # $9.5M cap savings, $49M dead money split
    },
    {
        'player_name': 'Davante Adams',
        'position': 'WR1',
        'from_team': 'NYJ',
        'to_team': 'LAR',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Still productive despite team struggles
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Primary receiver
        'importance_to_old_team': 7.5,  # Mid-season trade acquisition left quickly
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'D.J. Reed',
        'position': 'CB1',
        'from_team': 'NYJ',
        'to_team': 'Det',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Quality starting corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Jets starting corner
        'importance_to_old_team': 8.0,  # Key defensive back lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Haason Reddick',
        'position': 'EDGE',
        'from_team': 'NYJ',
        'to_team': 'TB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Contract holdout affected season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Limited by holdout issues
        'importance_to_old_team': 7.0,  # Pass rusher with baggage
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Javon Kinlaw',
        'position': 'DT',
        'from_team': 'NYJ',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Career-high 4.5 sacks with Jets
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Starting defensive tackle
        'importance_to_old_team': 7.0,  # Interior pass rush threat
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'C.J. Mosley',
        'position': 'LB',
        'from_team': 'NYJ',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Veteran linebacker leader
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting linebacker
        'importance_to_old_team': 7.5,  # Longtime defensive captain
        'importance_to_new_team': 0.0,  # $4M cap savings
    },
    {
        'player_name': 'Morgan Moses',
        'position': 'RT',
        'from_team': 'NYJ',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Veteran right tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting tackle
        'importance_to_old_team': 7.0,  # Veteran OL leadership
        'importance_to_new_team': 0.0,
    },

    # JETS TRADES - Philosophical shift from win-now to asset accumulation
    {
        'player_name': 'Mike Williams',
        'position': 'WR2',
        'from_team': 'NYJ',
        'to_team': 'Pit',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Expendable after Adams acquisition
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Reduced role post-Adams trade
        'importance_to_old_team': 6.0,  # Became expendable
        'importance_to_new_team': 0.0,  # Traded for 5th round pick
    },

    # JETS 2025 NFL DRAFT - Offensive line excellence continues
    {
        'player_name': 'Armand Membou',
        'position': 'RT',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #7',
        'contract_years': 4,
        'contract_value': 35000000,
        '2024_grade': 0.0,  # College - Missouri tackle, Glenn compared to Penei Sewell
        'projected_2025_grade': 7.8,  # Immediate starter at RT
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Completes OL rebuild with Fashanu
    },
    {
        'player_name': 'Mason Taylor',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #42',
        'contract_years': 4,
        'contract_value': 11500000,
        '2024_grade': 0.0,  # College - LSU tight end, Jason Taylor's son
        'projected_2025_grade': 7.0,  # Immediate receiving threat
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Fields' target and athletic lineage
    },
    {
        'player_name': 'Azareye\'h Thomas',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #73',
        'contract_years': 4,
        'contract_value': 7200000,
        '2024_grade': 0.0,  # College - Florida State cornerback
        'projected_2025_grade': 6.8,  # Developmental corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # CB depth post-Reed departure
    },
    {
        'player_name': 'Arian Smith',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #110',
        'contract_years': 4,
        'contract_value': 5800000,
        '2024_grade': 0.0,  # College - Georgia receiver with 4.36 speed
        'projected_2025_grade': 6.5,  # Speed threat
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.8,  # Field-stretching ability
    },
    {
        'player_name': 'Malachi Moore',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #130',
        'contract_years': 4,
        'contract_value': 5200000,
        '2024_grade': 0.0,  # College - Alabama safety, traded up for
        'projected_2025_grade': 6.8,  # Safety depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.8,  # Specific target via trade
    },
    {
        'player_name': 'Francisco Mauigoa',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #162',
        'contract_years': 4,
        'contract_value': 4600000,
        '2024_grade': 0.0,  # College - Miami linebacker
        'projected_2025_grade': 6.2,  # LB depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Linebacker development
    },
    {
        'player_name': 'Tyler Baron',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'NYJ',
        'move_type': '2025 Draft Pick #176',
        'contract_years': 4,
        'contract_value': 4400000,
        '2024_grade': 0.0,  # College - Miami edge rusher, traded up for
        'projected_2025_grade': 6.5,  # Edge depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Pass rush development
    },

    # JETS COACHING CHANGES - Complete organizational overhaul
    {
        'player_name': 'Aaron Glenn',
        'position': 'HC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 40000000,
        '2024_grade': 8.0,  # Lions DC, former Jets Pro Bowl corner (1994-2001)
        'projected_2025_grade': 8.5,  # Cultural transformation leader
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Lions lost elite DC
        'importance_to_new_team': 9.5,  # Complete culture reset
    },
    {
        'player_name': 'Darren Mougey',
        'position': 'GM',
        'from_team': 'Den',
        'to_team': 'NYJ',
        'move_type': 'General Manager Hire',
        'contract_years': 5,
        'contract_value': 25000000,
        '2024_grade': 7.5,  # 39 years old, Denver front office
        'projected_2025_grade': 8.0,  # NFL's third-youngest GM
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Broncos lost promising executive
        'importance_to_new_team': 9.0,  # Youth-focused philosophy
    },
    {
        'player_name': 'Tanner Engstrand',
        'position': 'OC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 4,
        'contract_value': 12000000,
        '2024_grade': 7.5,  # Brought from Detroit with Glenn
        'projected_2025_grade': 8.0,  # Run-heavy, RPO-based attack
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lions lost offensive coach
        'importance_to_new_team': 8.0,  # Perfect for Fields' skill set
    },
    {
        'player_name': 'Steve Wilks',
        'position': 'DC',
        'from_team': 'SF',
        'to_team': 'NYJ',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 4,
        'contract_value': 10000000,
        '2024_grade': 7.5,  # Former Cardinals/Panthers head coach
        'projected_2025_grade': 7.8,  # Zone concepts vs Glenn's man coverage
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # 49ers assistant
        'importance_to_new_team': 7.5,  # Multiple looks defensive scheme
    },
    {
        'player_name': 'Chris Banjo',
        'position': 'ST_COORD',
        'from_team': 'Car',
        'to_team': 'NYJ',
        'move_type': 'Special Teams Coordinator Hire',
        'contract_years': 3,
        'contract_value': 4500000,
        '2024_grade': 7.0,  # Carolina special teams coordinator
        'projected_2025_grade': 7.2,  # Special teams upgrade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # Panthers loss
        'importance_to_new_team': 7.0,  # Special teams improvement
    },
    {
        'player_name': 'Robert Saleh',
        'position': 'HC',
        'from_team': 'NYJ',
        'to_team': 'FIRED',
        'move_type': 'Head Coach Firing',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.5,  # 20-36 record, fired mid-season October 8
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Fired after 2-3 start
        'importance_to_old_team': 5.0,  # Failed to develop team culture
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Joe Douglas',
        'position': 'GM',
        'from_team': 'NYJ',
        'to_team': 'FIRED',
        'move_type': 'General Manager Firing',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # 30-64 tenure, fired November 19
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Full season responsibility
        'importance_to_old_team': 4.5,  # Failed roster construction
        'importance_to_new_team': 0.0,
    },
]

# JETS SUMMARY METRICS
JETS_2025_SUMMARY = {
    'total_moves': len(JETS_2025_MOVES),
    'free_agent_signings': 8,
    'major_losses': 7,
    'trades': 1,
    'draft_picks': 7,
    'key_resignings': 2,
    'coaching_changes': 7,
    'total_guaranteed_money': 85000000,  # Conservative youth-focused spending
    'salary_cap_space_remaining': 26000000,  # After Fields and moves
    'dead_money_burden': 49000000,  # Rodgers dead money split 2025/2026
    'championship_window': '2027-2030',
    'offseason_grade': 'B-',
    'key_philosophy': 'Complete culture reset with youth-focused rebuild',
    'biggest_concern': 'Growing pains expected with young QB and new systems',
    'biggest_strength': 'Finally unified leadership with coherent long-term vision'
}

if __name__ == "__main__":
    print(f"New York Jets 2025 Offseason Moves: {JETS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {JETS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {JETS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${JETS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Dead Money Burden: ${JETS_2025_SUMMARY['dead_money_burden']:,}")
    print(f"Philosophy: {JETS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {JETS_2025_SUMMARY['biggest_concern']}")
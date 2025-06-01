"""
Jacksonville Jaguars 2025 Offseason Moves
Complete analysis of bold transformation under James Gladstone and Liam Coen
"""

JAGUARS_2025_MOVES = [
    # JAGUARS FREE AGENT SIGNINGS - Offensive line reconstruction focus
    {
        'player_name': 'Patrick Mekari',
        'position': 'G',
        'from_team': 'Bal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 37500000,
        '2024_grade': 7.5,  # 94.6% pass block win rate (5th among guards)
        'projected_2025_grade': 8.0,  # Interior upgrade for Lawrence
        'snap_percentage_2024': 100.0,  # Started all 17 games (14 LG, 3 RT)
        'importance_to_old_team': 8.0,  # Ravens' most versatile lineman
        'importance_to_new_team': 8.5,  # Key interior upgrade
    },
    {
        'player_name': 'Robert Hainsey',
        'position': 'C',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 21000000,
        '2024_grade': 7.0,  # Familiar with Liam Coen from Tampa Bay
        'projected_2025_grade': 7.5,  # Center upgrade, coach familiarity
        'snap_percentage_2024': 85.0,  # Starting center
        'importance_to_old_team': 7.0,  # Bucs starting center
        'importance_to_new_team': 8.0,  # Replaces retired Mitch Morse
    },
    {
        'player_name': 'Dyami Brown',
        'position': 'WR2',
        'from_team': 'Was',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        '2024_grade': 7.0,  # Career highs: 30 catches, 308 yards
        'projected_2025_grade': 7.5,  # Emerging receiver talent
        'snap_percentage_2024': 44.0,  # Excelled in limited role
        'importance_to_old_team': 6.0,  # Commanders emerging receiver
        'importance_to_new_team': 8.0,  # Key receiver addition post-Kirk trade
    },
    {
        'player_name': 'Parker Washington',
        'position': 'WR3',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2200000,
        '2024_grade': 6.0,  # Depth receiver
        'projected_2025_grade': 6.5,  # Continued development
        'snap_percentage_2024': 35.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 6.0,  # WR depth retention
    },
    {
        'player_name': 'Jourdan Lewis',
        'position': 'CB2',
        'from_team': 'Dal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 30000000,
        '2024_grade': 8.0,  # NFL's highest-paid nickel corner at $10M AAV
        'projected_2025_grade': 8.2,  # Elite slot coverage
        'snap_percentage_2024': 75.0,  # Primary slot corner
        'importance_to_old_team': 7.5,  # Cowboys' 8-year veteran leader
        'importance_to_new_team': 8.5,  # Immediate secondary upgrade
    },
    {
        'player_name': 'Eric Murray',
        'position': 'S',
        'from_team': 'Hou',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8500000,
        '2024_grade': 6.5,  # Veteran safety depth
        'projected_2025_grade': 6.8,  # Safety depth
        'snap_percentage_2024': 80.0,  # Texans starter
        'importance_to_old_team': 7.0,  # Houston starting safety
        'importance_to_new_team': 6.5,  # Safety depth addition
    },
    {
        'player_name': 'Emmanuel Ogbah',
        'position': 'EDGE',
        'from_team': 'Mia',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        '2024_grade': 6.8,  # 5.0 sacks filling in for injured Chubb/Phillips
        'projected_2025_grade': 7.0,  # Pass rush depth
        'snap_percentage_2024': 65.0,  # Rotational pass rusher
        'importance_to_old_team': 6.5,  # Dolphins pass rush depth
        'importance_to_new_team': 7.0,  # Edge rusher depth
    },
    {
        'player_name': 'Nick Mullens',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.0,  # Familiar with Grant Udinski from Minnesota
        'projected_2025_grade': 6.2,  # Veteran backup
        'snap_percentage_2024': 25.0,  # Vikings backup
        'importance_to_old_team': 5.0,  # Vikings depth
        'importance_to_new_team': 6.5,  # Lawrence insurance with coordinator familiarity
    },
    {
        'player_name': 'Hunter Long',
        'position': 'TE',
        'from_team': 'LAR',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 5.5,  # Blocking TE, 8 career catches
        'projected_2025_grade': 6.0,  # Blocking specialist
        'snap_percentage_2024': 40.0,  # Limited receiving role
        'importance_to_old_team': 5.0,  # Rams depth
        'importance_to_new_team': 6.0,  # Replaces Luke Farrell, blocking focus
    },

    # JAGUARS MAJOR LOSSES - Roster overhaul casualties
    {
        'player_name': 'Christian Kirk',
        'position': 'WR2',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Reliable slot presence
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting slot receiver
        'importance_to_old_team': 7.0,  # Key Jaguars receiver traded
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Evan Engram',
        'position': 'TE',
        'from_team': 'Jac',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # 234 catches in 3 seasons, including 114 in 2023
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Primary receiving TE
        'importance_to_old_team': 8.0,  # Major blow to passing game
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Mitch Morse',
        'position': 'C',
        'from_team': 'Jac',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Veteran center
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Starting center
        'importance_to_old_team': 7.5,  # Center need created by retirement
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Brandon Scherff',
        'position': 'G',
        'from_team': 'Jac',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Veteran guard
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting guard
        'importance_to_old_team': 7.0,  # Interior line depth lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Ronald Darby',
        'position': 'CB1',
        'from_team': 'Jac',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Starting cornerback
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Regular starter
        'importance_to_old_team': 7.0,  # Secondary overhaul casualty
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Devin Duvernay',
        'position': 'KR',
        'from_team': 'Jac',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Special teams contributor
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,  # Limited offensive role
        'importance_to_old_team': 6.5,  # Special teams ace departed
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Gabe Davis',
        'position': 'WR2',
        'from_team': 'Jac',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.8,  # Disappointed in 1 season, played only 10 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Limited by injury
        'importance_to_old_team': 6.0,  # Failed FA signing released
        'importance_to_new_team': 0.0,
    },

    # JAGUARS TRADES - Historic draft capital expenditure
    {
        'player_name': 'Travis Hunter',
        'position': 'WR1',  # Playing both WR/CB
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #2 (via trade)',
        'contract_years': 4,
        'contract_value': 49000000,
        '2024_grade': 0.0,  # College - Heisman winner, 96 receptions, 1,258 yards, 15 TDs
        'projected_2025_grade': 8.5,  # Generational two-way talent
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Franchise-altering acquisition
    },

    # JAGUARS 2025 NFL DRAFT - Supporting cast for Hunter
    {
        'player_name': 'Wyatt Milum',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #104',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - West Virginia tackle
        'projected_2025_grade': 6.5,  # Developmental tackle
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # OL depth addition
    },
    {
        'player_name': 'Jalen McLeod',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #200',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - Linebacker prospect
        'projected_2025_grade': 6.0,  # LB depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Linebacker depth
    },
    {
        'player_name': 'Javon Baker',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #220',
        'contract_years': 4,
        'contract_value': 4400000,
        '2024_grade': 0.0,  # College - UCF receiver
        'projected_2025_grade': 5.8,  # WR depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Receiver depth
    },
    {
        'player_name': 'Joshua Mickens',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #240',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - Safety prospect
        'projected_2025_grade': 5.5,  # Safety depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Secondary depth
    },
    {
        'player_name': 'Kris Thornton',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Jac',
        'move_type': '2025 Draft Pick #255',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - DT prospect
        'projected_2025_grade': 5.8,  # DT depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Interior line depth
    },

    # JAGUARS KEY RE-SIGNINGS - Core retention
    {
        'player_name': 'Trevor Lawrence',
        'position': 'QB',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 55000000,
        '2024_grade': 6.8,  # Injury-limited season, missed 7 games
        'projected_2025_grade': 7.8,  # Bounce-back under Coen
        'snap_percentage_2024': 60.0,  # Limited by concussion/shoulder
        'importance_to_old_team': 9.5,  # Franchise quarterback
        'importance_to_new_team': 9.5,  # Critical to Coen's offense
    },
    {
        'player_name': 'Josh Hines-Allen',
        'position': 'EDGE',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 35000000,
        '2024_grade': 8.0,  # Elite pass rusher
        'projected_2025_grade': 8.2,  # Defensive anchor
        'snap_percentage_2024': 85.0,  # Primary pass rusher
        'importance_to_old_team': 9.0,  # Best pass rusher
        'importance_to_new_team': 9.0,  # Defensive foundation
    },
    {
        'player_name': 'Tyson Campbell',
        'position': 'CB1',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 16000000,
        '2024_grade': 7.5,  # Starting cornerback
        'projected_2025_grade': 7.8,  # CB1 opposite Hunter
        'snap_percentage_2024': 80.0,  # Regular starter
        'importance_to_old_team': 7.5,  # Starting corner
        'importance_to_new_team': 8.0,  # Pairs with Hunter in secondary
    },
    {
        'player_name': 'Cole Van Lanen',
        'position': 'G',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'RFA Tender',
        'contract_years': 1,
        'contract_value': 3800000,
        '2024_grade': 6.2,  # Versatile guard/tackle
        'projected_2025_grade': 6.5,  # OL depth
        'snap_percentage_2024': 45.0,  # Rotational lineman
        'importance_to_old_team': 6.0,  # Depth piece
        'importance_to_new_team': 6.5,  # Interior line depth
    },

    # JAGUARS COACHING CHANGES - Complete overhaul
    {
        'player_name': 'Liam Coen',
        'position': 'HC',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Coaching Hire',
        'contract_years': 5,
        'contract_value': 35000000,
        '2024_grade': 8.0,  # Successful Bucs OC
        'projected_2025_grade': 8.5,  # Offensive-minded head coach
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Lost key coordinator
        'importance_to_new_team': 9.5,  # Complete organizational change
    },
    {
        'player_name': 'James Gladstone',
        'position': 'GM',
        'from_team': 'LAR',
        'to_team': 'Jac',
        'move_type': 'Front Office Hire',
        'contract_years': 5,
        'contract_value': 30000000,
        '2024_grade': 7.5,  # Rams scouting department executive
        'projected_2025_grade': 8.0,  # Aggressive roster building
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost scouting talent
        'importance_to_new_team': 9.5,  # Complete front office overhaul
    },
    {
        'player_name': 'Tony Boselli',
        'position': 'EVP',
        'from_team': 'RETIRED',
        'to_team': 'Jac',
        'move_type': 'Front Office Hire',
        'contract_years': 3,
        'contract_value': 15000000,
        '2024_grade': 0.0,  # Franchise legend returns
        'projected_2025_grade': 7.5,  # Hall of Fame credibility
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Franchise credibility and leadership
    },
    {
        'player_name': 'Doug Pederson',
        'position': 'HC',
        'from_team': 'Jac',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # 4-13 disaster season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full head coaching control
        'importance_to_old_team': 8.0,  # Head coach fired
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Trent Baalke',
        'position': 'GM',
        'from_team': 'Jac',
        'to_team': 'FIRED',
        'move_type': 'Front Office Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 3.5,  # Poor roster construction, 4-13 record
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full GM control
        'importance_to_old_team': 8.5,  # GM fired after disaster
        'importance_to_new_team': 0.0,
    },
]

# JAGUARS SUMMARY METRICS
JAGUARS_2025_SUMMARY = {
    'total_moves': len(JAGUARS_2025_MOVES),
    'free_agent_signings': 9,
    'major_losses': 7,
    'trades': 1,  # The massive Hunter trade
    'draft_picks': 6,  # Reduced due to trade
    'key_resignings': 4,
    'coaching_changes': 5,
    'total_guaranteed_money': 125000000,  # Major investments
    'draft_capital_spent': 4,  # 2025: 1st, 2nd, 4th + 2026: 1st
    'salary_cap_space_remaining': 18000000,
    'championship_window': '2025-2028',
    'offseason_grade': 'B',
    'key_philosophy': 'Bold aggression with franchise-altering gamble',
    'biggest_concern': 'Massive draft capital expenditure limits future flexibility',
    'biggest_strength': 'Added generational talent in Travis Hunter',
    'franchise_defining_move': 'Trading up for Travis Hunter',
    'gladstone_quote': 'There are very few players who have the capacity to alter the trajectory of the sport itself'
}

if __name__ == "__main__":
    print(f"Jacksonville Jaguars 2025 Offseason Moves: {JAGUARS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {JAGUARS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {JAGUARS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${JAGUARS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {JAGUARS_2025_SUMMARY['key_philosophy']}")
    print(f"Franchise Defining Move: {JAGUARS_2025_SUMMARY['franchise_defining_move']}")
    print(f"Draft Capital Spent: {JAGUARS_2025_SUMMARY['draft_capital_spent']} picks including 2026 1st")
    print(f'GM Quote: "{JAGUARS_2025_SUMMARY["gladstone_quote"]}"')
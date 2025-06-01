"""
Miami Dolphins 2025 Offseason Moves
Complete analysis of Miami's transformation focusing on trenches and protection
"""

DOLPHINS_2025_MOVES = [
    # DOLPHINS MAJOR FREE AGENT SIGNINGS - O-Line Focus
    {
        'player_name': 'James Daniels',
        'position': 'G',
        'from_team': 'Chi',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 24000000,
        '2024_grade': 7.5,  # Solid guard play in Chicago
        'projected_2025_grade': 7.8,  # Key protection for Tua
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.0,  # Critical for Tua protection
    },
    {
        'player_name': 'Zach Wilson',
        'position': 'QB',
        'from_team': 'Den',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        '2024_grade': 6.0,  # Backup role in Denver
        'projected_2025_grade': 6.5,  # Experienced backup
        'snap_percentage_2024': 15.0,  # Limited snaps
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 8.0,  # Addresses backup QB weakness
    },
    {
        'player_name': 'Nick Westbrook-Ikhine',
        'position': 'WR2',
        'from_team': 'Ten',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6500000,
        '2024_grade': 6.8,  # Solid production in Tennessee
        'projected_2025_grade': 7.0,  # Physical complement to speed
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # WR depth
    },
    {
        'player_name': 'Alexander Mattison',
        'position': 'RB',
        'from_team': 'LV',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.2,  # Solid backup in Las Vegas
        'projected_2025_grade': 6.5,  # Short-yardage specialist
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Physical complement
    },
    {
        'player_name': 'Larry Borom',
        'position': 'OL',
        'from_team': 'Chi',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,  # Versatile backup
        'projected_2025_grade': 6.2,  # O-line depth
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # Versatility valued
    },
    {
        'player_name': 'Pharaoh Brown',
        'position': 'TE',
        'from_team': 'Hou',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,  # Blocking specialist
        'projected_2025_grade': 6.2,  # Run blocking help
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Blocking upgrade
    },
    {
        'player_name': 'K.J. Britt',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.5,  # Run-stopping ability
        'projected_2025_grade': 6.8,  # Depth and physicality
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # LB depth
    },
    {
        'player_name': 'Willie Gay Jr.',
        'position': 'LB',
        'from_team': 'KC',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,  # Athletic LB
        'projected_2025_grade': 6.5,  # Coverage help
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Depth piece
    },
    {
        'player_name': 'Ashtyn Davis',
        'position': 'S',
        'from_team': 'NYJ',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,  # Versatile safety
        'projected_2025_grade': 6.5,  # Secondary depth
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Replacing Holland
    },
    {
        'player_name': 'Ifeatu Melifonwu',
        'position': 'S',
        'from_team': 'Det',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        '2024_grade': 6.5,  # Solid safety play
        'projected_2025_grade': 7.0,  # Starting potential
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # Key safety addition
    },
    {
        'player_name': 'Artie Burns',
        'position': 'CB2',
        'from_team': 'Sea',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2200000,
        '2024_grade': 6.2,  # Hometown return
        'projected_2025_grade': 6.5,  # CB depth
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Depth and familiarity
    },
    {
        'player_name': 'Ryan Stonehouse',
        'position': 'P',
        'from_team': 'Ten',
        'to_team': 'Mia',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 8.5,  # NFL record 53.1 yard average
        'projected_2025_grade': 8.0,  # Elite punter
        'snap_percentage_2024': 100.0,  # All punting snaps
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # Special teams upgrade
    },

    # DOLPHINS KEY RE-SIGNINGS
    {
        'player_name': 'Tyrel Dodson',
        'position': 'LB',
        'from_team': 'Mia',
        'to_team': 'Mia',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8250000,
        '2024_grade': 7.5,  # Led team with 3 INTs
        'projected_2025_grade': 7.8,  # Continued production
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,  # Key defensive piece
    },
    {
        'player_name': 'Liam Eichenberg',
        'position': 'OL',
        'from_team': 'Mia',
        'to_team': 'Mia',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 6.5,  # Versatile lineman
        'projected_2025_grade': 6.8,  # Depth value
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # O-line continuity
    },
    {
        'player_name': 'Jackson Carman',
        'position': 'OT',
        'from_team': 'Mia',
        'to_team': 'Mia',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,  # Tackle depth
        'projected_2025_grade': 6.2,  # After Armstead retirement
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,  # Critical depth now
    },

    # DOLPHINS MAJOR LOSSES
    {
        'player_name': 'Jevon Holland',
        'position': 'S',
        'from_team': 'Mia',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Down year but talented
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,  # Starting safety
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Calais Campbell',
        'position': 'DT',
        'from_team': 'Mia',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # Veteran leader, 615 snaps
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 58.0,
        'importance_to_old_team': 8.5,  # Leadership and production
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Robert Jones',
        'position': 'G',
        'from_team': 'Mia',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Starting left guard
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,  # O-line starter
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Emmanuel Ogbah',
        'position': 'EDGE',
        'from_team': 'Mia',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # 5.0 sacks filling in
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,  # Pass rush depth
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Anthony Walker Jr.',
        'position': 'LB',
        'from_team': 'Mia',
        'to_team': 'TB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Solid linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,  # Starting LB
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Da\'Shawn Hand',
        'position': 'DT',
        'from_team': 'Mia',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # 563 defensive snaps
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,  # Rotational DT
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Siran Neal',
        'position': 'CB2',
        'from_team': 'Mia',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.2,  # Special teams and nickel
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },

    # DOLPHINS SALARY CAP CASUALTIES/RELEASES
    {
        'player_name': 'Kendall Fuller',
        'position': 'CB1',
        'from_team': 'Mia',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Started opposite Ramsey
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,  # Starting corner
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Raheem Mostert',
        'position': 'RB',
        'from_team': 'Mia',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Veteran back
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,  # Rotational back
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Durham Smythe',
        'position': 'TE',
        'from_team': 'Mia',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Blocking TE
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 5.5,  # Role player
        'importance_to_new_team': 0.0,
    },

    # DOLPHINS RETIREMENT
    {
        'player_name': 'Terron Armstead',
        'position': 'LT',
        'from_team': 'Mia',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Elite when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Injury limited
        'importance_to_old_team': 9.0,  # Starting LT, massive hole
        'importance_to_new_team': 0.0,
    },

    # DOLPHINS 2025 DRAFT PICKS - Trenches Focus
    {
        'player_name': 'Kenneth Grant',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #13',
        'contract_years': 4,
        'contract_value': 26500000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 7.5,  # 6.5 sacks at 331 lbs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starter at NT
    },
    {
        'player_name': 'Jonah Savaiinaea',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #37 (via trade)',
        'contract_years': 4,
        'contract_value': 12000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Versatile Arizona OL
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Starting guard competition
    },
    {
        'player_name': 'Jordan Phillips',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #143',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Rotational DT
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Depth piece
    },
    {
        'player_name': 'Jason Marshall Jr.',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #150',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # Local product from Miami
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Developmental CB
    },
    {
        'player_name': 'Ollie Gordon II',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #179',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Physical 220 lb runner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Goal-line specialist
    },
    {
        'player_name': 'Quinn Ewers',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #231',
        'contract_years': 4,
        'contract_value': 3200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # Developmental project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Future development
    },
    {
        'player_name': 'Zeek Biggers',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Mia',
        'move_type': '2025 Draft Pick #253',
        'contract_years': 4,
        'contract_value': 3100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # 6\'6" 321 lb project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Developmental DT
    },

    # DOLPHINS DRAFT DAY TRADE
    {
        'player_name': 'Draft Capital Trade',
        'position': 'PICKS',
        'from_team': 'Mia',
        'to_team': 'LV',
        'move_type': 'Draft Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': -2.0,  # Gave up picks #48, #98, #135
        'importance_to_new_team': 0.0,
    },

    # DOLPHINS UNDRAFTED FREE AGENTS - Notable Signings
    {
        'player_name': 'Andrew Armstrong',
        'position': 'WR3',
        'from_team': 'UDFA',
        'to_team': 'Mia',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # 6\'4" red zone target from Arkansas
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Size and upside
    },
    {
        'player_name': 'Josh Priebe',
        'position': 'G',
        'from_team': 'UDFA',
        'to_team': 'Mia',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.2,  # Michigan OL depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # O-line development
    },
]
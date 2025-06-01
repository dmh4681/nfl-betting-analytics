"""
New England Patriots 2025 Offseason Moves
Complete analysis of aggressive rebuild centered on protecting Drake Maye under Mike Vrabel
"""

PATRIOTS_2025_MOVES = [
    # PATRIOTS FREE AGENT SIGNINGS - Historic $410M spending spree
    {
        'player_name': 'Milton Williams',
        'position': 'DT',
        'from_team': 'Phi',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 104000000,
        '2024_grade': 8.2,  # 5 sacks, 54 pressures, Super Bowl strip-sack
        'projected_2025_grade': 8.5,  # Largest contract in franchise history
        'snap_percentage_2024': 48.0,  # Key interior rusher for Eagles
        'importance_to_old_team': 8.0,  # Eagles major loss
        'importance_to_new_team': 9.0,  # Defensive transformation centerpiece
    },
    {
        'player_name': 'Stefon Diggs',
        'position': 'WR1',
        'from_team': 'Hou',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 69000000,
        '2024_grade': 6.8,  # 610 receiving yards, limited role
        'projected_2025_grade': 7.8,  # Proven #1 receiver for Maye
        'snap_percentage_2024': 65.0,  # Reduced from previous years
        'importance_to_old_team': 7.0,  # Texans veteran leader
        'importance_to_new_team': 9.0,  # Elite target Maye lacked
    },
    {
        'player_name': 'Carlton Davis III',
        'position': 'CB1',
        'from_team': 'Det',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        '2024_grade': 7.5,  # Starting corner for Lions
        'projected_2025_grade': 7.8,  # #1 corner upgrade
        'snap_percentage_2024': 80.0,  # Lions starter
        'importance_to_old_team': 7.5,  # Key Lions defensive back
        'importance_to_new_team': 8.5,  # Major secondary upgrade
    },
    {
        'player_name': 'Harold Landry',
        'position': 'EDGE',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 43500000,
        '2024_grade': 7.8,  # Titans pass rusher
        'projected_2025_grade': 8.0,  # Vrabel familiarity
        'snap_percentage_2024': 75.0,  # Key pass rusher
        'importance_to_old_team': 8.0,  # Titans edge threat
        'importance_to_new_team': 8.5,  # Pass rush upgrade with scheme fit
    },
    {
        'player_name': 'Robert Spillane',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 37000000,
        '2024_grade': 7.5,  # Titans linebacker
        'projected_2025_grade': 7.8,  # Vrabel system familiarity
        'snap_percentage_2024': 85.0,  # Starting linebacker
        'importance_to_old_team': 8.0,  # Key Titans defender
        'importance_to_new_team': 8.0,  # Linebacker upgrade with familiarity
    },
    {
        'player_name': 'Morgan Moses',
        'position': 'RT',
        'from_team': 'NYJ',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 24000000,
        '2024_grade': 7.0,  # Veteran right tackle
        'projected_2025_grade': 7.2,  # Bookend tackle protection
        'snap_percentage_2024': 80.0,  # Jets starter
        'importance_to_old_team': 7.0,  # Jets tackle
        'importance_to_new_team': 8.0,  # Critical Maye protection
    },
    {
        'player_name': 'Josh Dobbs',
        'position': 'QB',
        'from_team': 'SF',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 6.5,  # Veteran backup experience
        'projected_2025_grade': 6.8,  # Reliable backup for Maye
        'snap_percentage_2024': 25.0,  # Limited 49ers role
        'importance_to_old_team': 5.5,  # 49ers depth
        'importance_to_new_team': 7.0,  # Maye mentor and insurance
    },
    {
        'player_name': 'Mack Hollins',
        'position': 'WR2',
        'from_team': 'Buf',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8400000,
        '2024_grade': 6.8,  # Bills depth receiver
        'projected_2025_grade': 7.0,  # Size and physicality
        'snap_percentage_2024': 55.0,  # Rotational role
        'importance_to_old_team': 6.5,  # Bills depth piece
        'importance_to_new_team': 7.0,  # WR depth upgrade
    },
    {
        'player_name': 'Garrett Bradbury',
        'position': 'C',
        'from_team': 'Min',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 6.5,  # Vikings center
        'projected_2025_grade': 6.8,  # Center upgrade
        'snap_percentage_2024': 85.0,  # Vikings starter
        'importance_to_old_team': 6.5,  # Vikings center
        'importance_to_new_team': 7.0,  # Replaces David Andrews
    },
    {
        'player_name': 'Khyiris Tonga',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        '2024_grade': 6.0,  # Cardinals defensive tackle
        'projected_2025_grade': 6.5,  # Defensive line depth
        'snap_percentage_2024': 50.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Cardinals depth
        'importance_to_new_team': 6.5,  # DT rotation help
    },
    {
        'player_name': 'Jack Gibbens',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 6.5,  # "Dr. Gibby" from Tennessee
        'projected_2025_grade': 7.0,  # Vrabel familiarity
        'snap_percentage_2024': 60.0,  # Titans contributor
        'importance_to_old_team': 6.5,  # Titans depth
        'importance_to_new_team': 7.0,  # Scheme familiarity
    },
    {
        'player_name': 'Breiden Fehoko',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,  # Chargers defensive tackle
        'projected_2025_grade': 6.2,  # Defensive line depth
        'snap_percentage_2024': 40.0,  # Limited role
        'importance_to_old_team': 5.5,  # Chargers depth
        'importance_to_new_team': 6.0,  # Interior depth
    },
    {
        'player_name': 'Cameron Moon',
        'position': 'S',
        'from_team': 'Pit',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.0,  # Steelers safety depth
        'projected_2025_grade': 6.2,  # Safety depth
        'snap_percentage_2024': 30.0,  # Limited defensive role
        'importance_to_old_team': 5.5,  # Steelers depth
        'importance_to_new_team': 6.0,  # Secondary depth
    },
    {
        'player_name': 'C.J. Dippre',
        'position': 'TE',
        'from_team': 'UDFA',
        'to_team': 'NE',
        'move_type': 'UDFA Signing',
        'contract_years': 4,
        'contract_value': 1000000,
        '2024_grade': 0.0,  # College - High UDFA investment
        'projected_2025_grade': 5.5,  # Developmental TE
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # TE depth project
    },
    {
        'player_name': 'Efton Chism III',
        'position': 'WR3',
        'from_team': 'UDFA',
        'to_team': 'NE',
        'move_type': 'UDFA Signing',
        'contract_years': 4,
        'contract_value': 900000,
        '2024_grade': 0.0,  # College - Record UDFA guarantees
        'projected_2025_grade': 5.8,  # Developmental receiver
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # WR depth development
    },
    {
        'player_name': 'Ben Wooldridge',
        'position': 'QB',
        'from_team': 'UDFA',
        'to_team': 'NE',
        'move_type': 'UDFA Signing',
        'contract_years': 4,
        'contract_value': 800000,
        '2024_grade': 0.0,  # College - Louisiana quarterback
        'projected_2025_grade': 5.5,  # Third QB development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # QB depth
    },

    # PATRIOTS KEY RE-SIGNINGS - Core retention amid transformation
    {
        'player_name': 'Austin Hooper',
        'position': 'TE',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 7000000,
        '2024_grade': 7.0,  # 45 catches, 476 yards, chemistry with Maye
        'projected_2025_grade': 7.2,  # Reliable target for Maye
        'snap_percentage_2024': 70.0,  # Key tight end
        'importance_to_old_team': 7.5,  # Maye's favorite target
        'importance_to_new_team': 7.5,  # Continuity for QB
    },
    {
        'player_name': 'Christian Elliss',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Matched Offer Sheet',
        'contract_years': 2,
        'contract_value': 13500000,
        '2024_grade': 7.2,  # 80 tackles, five-unit special teams
        'projected_2025_grade': 7.5,  # Ascending player worth investment
        'snap_percentage_2024': 75.0,  # Starting linebacker
        'importance_to_old_team': 7.5,  # Effort and versatility
        'importance_to_new_team': 7.5,  # Vrabel-type player
    },
    {
        'player_name': 'Ben Brown',
        'position': 'C',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Exclusive Rights Tender',
        'contract_years': 1,
        'contract_value': 1300000,
        '2024_grade': 6.8,  # Starting-caliber center depth
        'projected_2025_grade': 7.0,  # Center insurance
        'snap_percentage_2024': 60.0,  # Filled in for Andrews
        'importance_to_old_team': 7.0,  # Reliable backup turned starter
        'importance_to_new_team': 7.0,  # Center depth
    },
    {
        'player_name': 'Demontrey Jacobs',
        'position': 'OT',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Exclusive Rights Tender',
        'contract_years': 1,
        'contract_value': 960000,
        '2024_grade': 6.5,  # Started 13 games at both tackle spots
        'projected_2025_grade': 6.8,  # Swing tackle versatility
        'snap_percentage_2024': 80.0,  # Key versatile lineman
        'importance_to_old_team': 7.0,  # Versatile starter
        'importance_to_new_team': 7.0,  # OL depth crucial
    },
    {
        'player_name': 'Jaylinn Hawkins',
        'position': 'S',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2250000,
        '2024_grade': 6.5,  # Special teams excellence
        'projected_2025_grade': 6.8,  # Safety depth and special teams
        'snap_percentage_2024': 40.0,  # Limited defensive role
        'importance_to_old_team': 6.5,  # Special teams ace
        'importance_to_new_team': 6.5,  # Special teams value
    },

    # PATRIOTS MAJOR LOSSES - End of dynasty era connections
    {
        'player_name': 'Jonathan Jones',
        'position': 'CB2',
        'from_team': 'NE',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 9 seasons, 2 Super Bowls, started 14 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting corner
        'importance_to_old_team': 7.5,  # 17 years Patriots experience lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Deatrich Wise Jr.',
        'position': 'EDGE',
        'from_team': 'NE',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # 5 sacks, 3-time captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Rotational pass rusher
        'importance_to_old_team': 7.0,  # 8 seasons, "Patriot Way" embodiment
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'David Andrews',
        'position': 'C',
        'from_team': 'NE',
        'to_team': 'RETIRED',
        'move_type': 'Release/Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # 10-year veteran, 8-time captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # When healthy, starting center
        'importance_to_old_team': 8.0,  # Shocked by release, retired
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Ja\'Whaun Bentley',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # 7 seasons, 4-time captain, injury-plagued 2024
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Limited by injuries
        'importance_to_old_team': 7.0,  # Longtime leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Joe Cardona',
        'position': 'LS',
        'from_team': 'NE',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 10 seasons, longest-tenured Patriot
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # All long snapping duties
        'importance_to_old_team': 6.5,  # Longest tenure ended
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jacoby Brissett',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Maye's mentor and early-season starter
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Bridge starter early season
        'importance_to_old_team': 7.0,  # Critical in Maye development
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Sione Takitaki',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Linebacker depth
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Limited role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },

    # PATRIOTS TRADES - Strategic moves for draft capital
    {
        'player_name': 'Davon Godchaux',
        'position': 'DT',
        'from_team': 'NE',
        'to_team': 'NO',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Requested trade, gap-control defender
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Starting defensive tackle
        'importance_to_old_team': 6.5,  # Didn't fit new attacking scheme
        'importance_to_new_team': 0.0,  # Traded for 2026 7th round pick
    },
    {
        'player_name': 'Joe Milton III',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Impressive Week 18 performance
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,  # Limited role
        'importance_to_old_team': 6.0,  # Promising young QB
        'importance_to_new_team': 0.0,  # Traded for 5th round pick upgrade
    },

    # PATRIOTS 2025 NFL DRAFT - Protection and playmakers for Maye
    {
        'player_name': 'Will Campbell',
        'position': 'LT',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #4',
        'contract_years': 4,
        'contract_value': 38500000,
        '2024_grade': 0.0,  # College - LSU left tackle, 3 years SEC starting experience
        'projected_2025_grade': 7.8,  # Immediate blind-side protection for Maye
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Critical Maye protection
    },
    {
        'player_name': 'TreVeyon Henderson',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #36',
        'contract_years': 4,
        'contract_value': 12800000,
        '2024_grade': 0.0,  # College - 22.1% rate of 10+ yard carries
        'projected_2025_grade': 7.5,  # Explosive element for 30th-ranked offense
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Game-breaking speed
    },
    {
        'player_name': 'Kyle Williams',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #77',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - 70 catches, 1,198 yards, 14 TDs at Washington State
        'projected_2025_grade': 7.2,  # Deep threat for Maye
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.8,  # Proven college production
    },
    {
        'player_name': 'Jared Wilson',
        'position': 'C',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #95',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - Georgia center, first-round grades from some
        'projected_2025_grade': 7.0,  # Long-term Andrews replacement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Exceptional value at #95
    },
    {
        'player_name': 'Joshua Farmer',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #137',
        'contract_years': 4,
        'contract_value': 5000000,
        '2024_grade': 0.0,  # College - Florida State DT, pre-draft visitor
        'projected_2025_grade': 6.8,  # Targeted trade-up selection
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Specific team target
    },
    {
        'player_name': 'Bradyn Swinson',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #146',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - LSU edge rusher
        'projected_2025_grade': 6.5,  # Edge depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Pass rush depth
    },
    {
        'player_name': 'Andres Borregales',
        'position': 'K',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #167',
        'contract_years': 4,
        'contract_value': 4400000,
        '2024_grade': 0.0,  # College - Miami kicker
        'projected_2025_grade': 6.0,  # Special teams upgrade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Kicker competition
    },
    {
        'player_name': 'Kam Dewberry',
        'position': 'OG',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #204',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - Interior line depth
        'projected_2025_grade': 6.2,  # Guard development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # OL depth
    },
    {
        'player_name': 'Julian Ashby',
        'position': 'LS',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #226',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Long snapper replacement
        'projected_2025_grade': 6.0,  # Replaces Cardona
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Special teams continuity
    },
    {
        'player_name': 'Cortez Mills',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #240',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Developmental corner
        'projected_2025_grade': 5.8,  # CB depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Late-round development
    },
    {
        'player_name': 'Keion White',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'NE',
        'move_type': '2025 Draft Pick #248',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,  # College - Late-round corner
        'projected_2025_grade': 5.5,  # Developmental DB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Late-round project
    },

    # PATRIOTS COACHING CHANGES - Complete philosophical overhaul
    {
        'player_name': 'Mike Vrabel',
        'position': 'HC',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 50000000,
        '2024_grade': 8.0,  # 54-45 record with Titans, proven NFL success
        'projected_2025_grade': 8.5,  # Championship culture builder
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Titans lost proven coach
        'importance_to_new_team': 9.5,  # Complete organizational shift
    },
    {
        'player_name': 'Josh McDaniels',
        'position': 'OC',
        'from_team': 'LV',
        'to_team': 'NE',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 4,
        'contract_value': 20000000,
        '2024_grade': 7.5,  # Third stint with Patriots, 6 Super Bowl titles
        'projected_2025_grade': 8.0,  # Modern Erhardt-Perkins for Maye
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,  # Raiders already moved on
        'importance_to_new_team': 8.5,  # Offensive system continuity
    },
    {
        'player_name': 'Terrell Williams',
        'position': 'DC',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 4,
        'contract_value': 12000000,
        '2024_grade': 7.0,  # 6 seasons with Vrabel in Tennessee
        'projected_2025_grade': 7.8,  # Aggressive one-gap scheme shift
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Titans lost defensive architect
        'importance_to_new_team': 8.0,  # Dramatic scheme change from Belichick
    },
    {
        'player_name': 'Jerod Mayo',
        'position': 'HC',
        'from_team': 'NE',
        'to_team': 'FIRED',
        'move_type': 'Head Coach Firing',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # 4-13 record, defense plummeted to 23rd
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full responsibility
        'importance_to_old_team': 5.0,  # Failed "players' coach" experiment
        'importance_to_new_team': 0.0,
    },
]

# PATRIOTS SUMMARY METRICS
PATRIOTS_2025_SUMMARY = {
    'total_moves': len(PATRIOTS_2025_MOVES),
    'free_agent_signings': 16,
    'major_losses': 7,
    'trades': 2,
    'draft_picks': 11,
    'key_resignings': 5,
    'coaching_changes': 4,
    'total_guaranteed_money': 410000000,  # Historic spending spree
    'salary_cap_space_remaining': 81000000,  # After initial spending
    'championship_window': '2026-2029',
    'offseason_grade': 'A-',
    'key_philosophy': 'Aggressive rebuild centered on protecting Drake Maye',
    'biggest_concern': 'Dramatic scheme changes must coalesce quickly',
    'biggest_strength': 'Proven coaching with substantial talent upgrade for Maye'
}

if __name__ == "__main__":
    print(f"New England Patriots 2025 Offseason Moves: {PATRIOTS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {PATRIOTS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {PATRIOTS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${PATRIOTS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Total Guaranteed Money: ${PATRIOTS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {PATRIOTS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {PATRIOTS_2025_SUMMARY['biggest_concern']}")
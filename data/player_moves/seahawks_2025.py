"""
Seattle Seahawks 2025 Offseason Moves
Dramatic pivot toward run-heavy identity: Trading franchise cornerstones for philosophical overhaul
"""

SEAHAWKS_2025_MOVES = [
    # SEAHAWKS FRANCHISE-ALTERING TRADES - Trading away cornerstone players
    {
        'player_name': 'Geno Smith',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'LV',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # 4,320 passing yards, 70.4% completion, Pro Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,  # Full-time starter
        'importance_to_old_team': 9.0,  # Franchise QB for 4 years, $31M cap savings
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'DK Metcalf',
        'position': 'WR1',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.2,  # Elite receiver, requested trade due to QB uncertainty
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Primary receiver
        'importance_to_old_team': 9.5,  # Franchise WR, sought $30M annually
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Sam Howell',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Backup quarterback
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 10.0,  # Limited backup role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },

    # SEAHAWKS MAJOR RELEASES - Cap-clearing moves
    {
        'player_name': 'Tyler Lockett',
        'position': 'WR1',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # 910 receptions, 8,779 yards, 56 TDs in 10 years
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Franchise icon
        'importance_to_old_team': 9.0,  # $31M cap savings, 10-year veteran
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Dre\'Mont Jones',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Solid interior lineman
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Starting DT
        'importance_to_old_team': 7.0,  # Cap casualty
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Roy Robertson-Harris',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Rotational defensive lineman
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Rotation piece
        'importance_to_old_team': 6.5,  # Cap savings
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Rayshawn Jenkins',
        'position': 'S',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Veteran safety
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting safety
        'importance_to_old_team': 6.5,  # Cap casualty
        'importance_to_new_team': 0.0,
    },

    # SEAHAWKS OTHER DEPARTURES
    {
        'player_name': 'Laken Tomlinson',
        'position': 'G',
        'from_team': 'Sea',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Starting left guard
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 7.5,  # Key offensive lineman
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Tre Brown',
        'position': 'CB2',
        'from_team': 'Sea',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Solid corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Rotational corner
        'importance_to_old_team': 6.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Artie Burns',
        'position': 'CB2',
        'from_team': 'Sea',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Veteran corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Stone Forsythe',
        'position': 'OT',
        'from_team': 'Sea',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Backup tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,  # Limited role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Pharaoh Brown',
        'position': 'TE',
        'from_team': 'Sea',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Blocking tight end
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Depth piece
        'importance_to_new_team': 0.0,
    },

    # SEAHAWKS MAJOR SIGNINGS - New offensive identity
    {
        'player_name': 'Sam Darnold',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 100500000,
        '2024_grade': 8.5,  # Pro Bowl season: 4,319 yards, 35 TDs, 102.5 passer rating
        'projected_2025_grade': 8.0,  # Reunion with Klint Kubiak
        'snap_percentage_2024': 90.0,  # Full-time starter for Vikings
        'importance_to_old_team': 8.5,  # Key piece for Vikings
        'importance_to_new_team': 9.5,  # Franchise QB replacement
    },
    {
        'player_name': 'Cooper Kupp',
        'position': 'WR1',
        'from_team': 'LAR',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 45000000,
        '2024_grade': 6.8,  # Injury-limited: 67 catches, 710 yards
        'projected_2025_grade': 8.0,  # Yakima native returns home, 2021 OPOY
        'snap_percentage_2024': 60.0,  # Limited by injuries
        'importance_to_old_team': 8.0,  # Rams legend
        'importance_to_new_team': 9.0,  # WR1 production and leadership
    },
    {
        'player_name': 'DeMarcus Lawrence',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 42000000,
        '2024_grade': 6.0,  # Injury-shortened season (4 games)
        'projected_2025_grade': 7.5,  # 4x Pro Bowler when healthy
        'snap_percentage_2024': 25.0,  # Limited by foot injury
        'importance_to_old_team': 7.5,  # Cowboys legend
        'importance_to_new_team': 8.0,  # Pass rush upgrade when healthy
    },
    {
        'player_name': 'Marquez Valdes-Scantling',
        'position': 'WR2',
        'from_team': 'NO',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        '2024_grade': 6.5,  # Deep threat capability
        'projected_2025_grade': 7.0,  # Reunion with Kubiak from New Orleans
        'snap_percentage_2024': 55.0,  # Rotational receiver
        'importance_to_old_team': 6.0,  # Saints depth piece
        'importance_to_new_team': 7.0,  # Deep threat element
    },
    {
        'player_name': 'Josh Jones',
        'position': 'OT',
        'from_team': 'Bal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4750000,
        '2024_grade': 6.0,  # Versatile lineman
        'projected_2025_grade': 6.5,  # Multiple position capability
        'snap_percentage_2024': 25.0,  # Limited role with Ravens
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 7.0,  # OL depth badly needed
    },
    {
        'player_name': 'Drew Lock',
        'position': 'QB',
        'from_team': 'NYG',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 6.0,  # Veteran backup experience
        'projected_2025_grade': 6.2,  # Returns to Seattle
        'snap_percentage_2024': 15.0,  # Backup role
        'importance_to_old_team': 5.0,  # Giants depth
        'importance_to_new_team': 6.5,  # Experienced backup for Darnold
    },
    {
        'player_name': 'Shemar Jean-Charles',
        'position': 'CB2',
        'from_team': 'LV',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,  # Rotational corner
        'projected_2025_grade': 6.5,  # Competition for starting role
        'snap_percentage_2024': 40.0,  # Limited role
        'importance_to_old_team': 5.5,  # Raiders depth
        'importance_to_new_team': 6.5,  # CB depth needed
    },
    {
        'player_name': 'D\'Anthony Bell',
        'position': 'S',
        'from_team': 'Was',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.0,  # Special teams contributor
        'projected_2025_grade': 6.2,  # Safety depth
        'snap_percentage_2024': 30.0,  # Special teams role
        'importance_to_old_team': 5.0,  # Commanders depth
        'importance_to_new_team': 6.0,  # Safety competition
    },
    {
        'player_name': 'Eric Saubert',
        'position': 'TE',
        'from_team': 'LV',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,  # Blocking tight end
        'projected_2025_grade': 6.2,  # Run-heavy scheme fit
        'snap_percentage_2024': 35.0,  # Rotational role
        'importance_to_old_team': 5.0,  # Raiders depth
        'importance_to_new_team': 6.5,  # Blocking for run game
    },
    {
        'player_name': 'Steven Sims Jr.',
        'position': 'WR3',
        'from_team': 'Hou',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 5.8,  # Return specialist
        'projected_2025_grade': 6.0,  # Special teams value
        'snap_percentage_2024': 20.0,  # Limited offensive role
        'importance_to_old_team': 4.5,  # Texans depth
        'importance_to_new_team': 5.5,  # Return game help
    },

    # SEAHAWKS DRAFT PICKS - Supporting the new philosophy
    {
        'player_name': 'Grey Zabel',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #18',
        'contract_years': 4,
        'contract_value': 22500000,
        '2024_grade': 0.0,  # College - North Dakota State, consensus All-American
        'projected_2025_grade': 7.5,  # Expected immediate starter at guard
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Addresses biggest need (OL ranked 30th)
    },
    {
        'player_name': 'Nick Emmanwori',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #35 (traded up)',
        'contract_years': 4,
        'contract_value': 14200000,
        '2024_grade': 0.0,  # College - South Carolina safety, Kam Chancellor comparisons
        'projected_2025_grade': 7.8,  # Perfect fit for Macdonald's defense
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Replaces Jenkins, fits scheme perfectly
    },
    {
        'player_name': 'Elijah Arroyo',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #50',
        'contract_years': 4,
        'contract_value': 10800000,
        '2024_grade': 0.0,  # College - Miami TE, 16.9 YPR led FBS tight ends with 20+ catches
        'projected_2025_grade': 7.0,  # Vertical threat in passing game
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Adds passing game dimension
    },
    {
        'player_name': 'Jalen Milroe',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #92 (from Geno trade)',
        'contract_years': 4,
        'contract_value': 6500000,
        '2024_grade': 0.0,  # College - Alabama QB, 726 rushing yards, 20 rushing TDs
        'projected_2025_grade': 6.5,  # Dual-threat development project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Only 3rd QB selected by Schneider in 16 years
    },
    {
        'player_name': 'Tory Horton',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #166',
        'contract_years': 4,
        'contract_value': 4300000,
        '2024_grade': 0.0,  # College - Tyler Lockett-like speed and return ability
        'projected_2025_grade': 6.2,  # Return specialist potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Replaces Lockett's return duties
    },
    {
        'player_name': 'Robbie Ouzts',
        'position': 'FB',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #175',
        'contract_years': 4,
        'contract_value': 4100000,
        '2024_grade': 0.0,  # College - 275-pound lead blocker
        'projected_2025_grade': 6.0,  # Run-heavy scheme addition
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Perfect for new run-first identity
    },
    {
        'player_name': 'Bryce Cabeldue',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #192',
        'contract_years': 4,
        'contract_value': 3900000,
        '2024_grade': 0.0,  # College - Offensive line depth
        'projected_2025_grade': 6.0,  # Development piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # OL depth badly needed
    },
    {
        'player_name': 'Damien Martinez',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #223',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,  # College - Proclaimed himself "Beast Mode 2.0"
        'projected_2025_grade': 6.0,  # Power runner for run game
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Run-heavy identity
    },
    {
        'player_name': 'Mason Richman',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #234',
        'contract_years': 4,
        'contract_value': 3400000,
        '2024_grade': 0.0,  # College - Additional OL depth
        'projected_2025_grade': 5.8,  # Development piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Future OL development
    },
    {
        'player_name': 'Ricky White III',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Sea',
        'move_type': '2025 Draft Pick #238',
        'contract_years': 4,
        'contract_value': 3300000,
        '2024_grade': 0.0,  # College - Elite special teams (blocked 4 punts)
        'projected_2025_grade': 5.8,  # Special teams ace
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Special teams upgrade
    },

    # SEAHAWKS KEY RE-SIGNINGS - Retaining defensive core
    {
        'player_name': 'Ernest Jones IV',
        'position': 'LB',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 33000000,
        '2024_grade': 8.5,  # 94 tackles in 10 games after midseason trade
        'projected_2025_grade': 8.8,  # Transformed run defense
        'snap_percentage_2024': 90.0,  # Immediate starter impact
        'importance_to_old_team': 9.0,  # Defensive anchor
        'importance_to_new_team': 9.5,  # $15M guaranteed, critical retention
    },
    {
        'player_name': 'Jarran Reed',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 25000000,
        '2024_grade': 7.5,  # Last remaining Legion of Boom era player
        'projected_2025_grade': 7.2,  # Veteran leadership
        'snap_percentage_2024': 70.0,  # Key interior presence
        'importance_to_old_team': 8.0,  # $10M guaranteed, defensive continuity
        'importance_to_new_team': 8.0,  # Veteran anchor
    },
    {
        'player_name': 'Josh Jobe',
        'position': 'CB1',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 7.8,  # Breakout: practice squad to starter
        'projected_2025_grade': 8.0,  # 7 passes defensed, 37 tackles
        'snap_percentage_2024': 75.0,  # Emerging starter
        'importance_to_old_team': 7.5,  # Development success story
        'importance_to_new_team': 8.0,  # Key secondary piece
    },
    {
        'player_name': 'Cody White',
        'position': 'WR3',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.0,  # Special teams contributor
        'projected_2025_grade': 6.2,  # Depth receiver
        'snap_percentage_2024': 25.0,  # Limited offensive role
        'importance_to_old_team': 5.5,  # Special teams value
        'importance_to_new_team': 6.0,  # Team-friendly depth
    },
    {
        'player_name': 'Josh Ross',
        'position': 'LB',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1100000,
        '2024_grade': 6.0,  # Special teams contributor
        'projected_2025_grade': 6.2,  # Linebacker depth
        'snap_percentage_2024': 20.0,  # Special teams focused
        'importance_to_old_team': 5.5,  # Special teams value
        'importance_to_new_team': 6.0,  # Depth and special teams
    },
    {
        'player_name': 'Brady Russell',
        'position': 'S',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1000000,
        '2024_grade': 5.8,  # Special teams contributor
        'projected_2025_grade': 6.0,  # Safety depth
        'snap_percentage_2024': 15.0,  # Limited role
        'importance_to_old_team': 5.0,  # Special teams value
        'importance_to_new_team': 5.5,  # Depth piece
    },

    # SEAHAWKS COACHING CHANGES - Complete offensive philosophy overhaul
    {
        'player_name': 'Ryan Grubb',
        'position': 'OC',
        'from_team': 'Sea',
        'to_team': 'FIRED',
        'move_type': 'Coaching Dismissal',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # 14th in total yards but philosophical differences
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Pass-heavy approach conflicted with vision
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Klint Kubiak',
        'position': 'OC',
        'from_team': 'NO',
        'to_team': 'Sea',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 9000000,
        '2024_grade': 7.5,  # Extensive coordinator experience (MIN, NO, SF)
        'projected_2025_grade': 8.0,  # Brings run-first philosophy
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # Saints offensive coordinator
        'importance_to_new_team': 9.0,  # Signals complete offensive philosophy shift
    },
    {
        'player_name': 'John Benton',
        'position': 'OL_COACH',
        'from_team': 'NO',
        'to_team': 'Sea',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 3000000,
        '2024_grade': 7.0,  # Followed Kubiak from New Orleans
        'projected_2025_grade': 7.5,  # Critical for OL improvement (ranked 30th)
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Saints OL coach
        'importance_to_new_team': 8.0,  # Must fix worst pass protection in NFL
    },
    {
        'player_name': 'Rick Dennison',
        'position': 'RUN_GAME_COORD',
        'from_team': 'NO',
        'to_team': 'Sea',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 2500000,
        '2024_grade': 7.0,  # Veteran run game specialist
        'projected_2025_grade': 7.5,  # Critical for new run-heavy identity
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Saints run coordinator
        'importance_to_new_team': 8.0,  # Implements new physical approach
    },

    # SEAHAWKS UDFA SIGNINGS - Heavy defensive focus
    {
        'player_name': 'Multiple Defensive UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Sea',
        'move_type': 'UDFA Signings (11 defensive players)',
        'contract_years': 3,
        'contract_value': 15000000,
        '2024_grade': 0.0,  # College prospects - 11 of 17 UDFAs on defense
        'projected_2025_grade': 5.5,  # Depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Balances offense-heavy draft
    },
]

# SEAHAWKS SUMMARY METRICS
SEAHAWKS_2025_SUMMARY = {
    'total_moves': len(SEAHAWKS_2025_MOVES),
    'major_trades': 3,  # Smith, Metcalf, Howell
    'major_releases': 4,  # Lockett, Jones, Robertson-Harris, Jenkins
    'free_agent_signings': 10,
    'free_agent_losses': 6,
    'draft_picks': 9,
    'key_resignings': 6,
    'coaching_changes': 4,  # 1 firing, 3 hires
    'udfa_signings': 1,  # Grouped as one entry (17 total UDFAs)
    'total_guaranteed_money': 325000000,  # Includes major signings
    'cap_space_created': 50000000,  # From trades and releases
    'salary_cap_space_remaining': 30000000,  # Current flexibility
    'championship_window': '2026-2028',  # Post-transition
    'offseason_grade': 'B',  # Bold strategy with significant risk
    'key_philosophy': 'Pivot toward run-heavy identity in dramatic offseason overhaul',
    'offensive_line_ranking': 8,  # PFF ranking after improvements
    'win_total_projection': 8.5,  # Down from 10 in 2024
    'playoff_odds': 45,  # Moderate due to NFC West competition
    'biggest_gamble': 'Trading franchise cornerstones Smith and Metcalf',
    'smartest_move': 'Ernest Jones extension (critical defensive retention)',
    'critical_success_factor': 'Offensive line protection improvement',
    'nfc_west_standing': 'Unanimous last-place predictions after moves'
}

# SEAHAWKS STRATEGIC ANALYSIS
SEAHAWKS_2025_ANALYSIS = {
    'offensive_transformation': 'Complete philosophical shift from pass-heavy to run-first',
    'quarterback_transition': 'Darnold reunion with Kubiak offers proven chemistry',
    'coaching_overhaul': 'Grubb firing signals commitment to new identity',
    'draft_philosophy': '7 of 11 picks on offense, emphasis on immediate contributors',
    'defensive_continuity': 'Retained core (Jones, Reed, Jobe) while losing depth',
    'biggest_risk': 'Offensive line still question mark despite improvements',
    'biggest_reward': 'Young, cost-controlled roster with identity clarity',
    'kupp_factor': 'Yakima native homecoming provides veteran leadership',
    'milroe_significance': 'Only 3rd QB drafted by Schneider in 16 years',
    'cap_management': 'Over $50M created enables strategic reinvestment',
    'nfc_west_reality': 'Division competitors improved while Seattle rebuilds',
    'macdonald_influence': 'Defensive continuity maintains strength unit',
    'schneider_timeline': '16th season requires 2025 improvement for job security'
}

# SEAHAWKS RISK ASSESSMENT
SEAHAWKS_2025_RISKS = {
    'immediate_risks': [
        'Offensive line still ranked 30th in pass protection',
        'Wide receiver depth limited beyond Kupp/Smith-Njigba',
        'DeMarcus Lawrence injury history',
        'Complete offensive philosophy change requires adjustment time'
    ],
    'medium_term_risks': [
        'NFC West competition significantly stronger',
        'Darnold consistency questions despite Pro Bowl 2024',
        'Aging defensive core (Reed last Legion of Boom player)',
        'Limited proven pass rush depth'
    ],
    'potential_rewards': [
        'Physical, run-first identity suits personnel better',
        'Young, cost-controlled roster enables future flexibility',
        'Kupp provides proven WR1 production when healthy',
        'Macdonald defensive system intact with key retentions'
    ]
}

if __name__ == "__main__":
    print(f"Seattle Seahawks 2025 Offseason Moves: {SEAHAWKS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {SEAHAWKS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {SEAHAWKS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Created: ${SEAHAWKS_2025_SUMMARY['cap_space_created']:,}")
    print(f"Philosophy: {SEAHAWKS_2025_SUMMARY['key_philosophy']}")
    print(f"Win Total Projection: {SEAHAWKS_2025_SUMMARY['win_total_projection']}")
    print(f"Playoff Odds: {SEAHAWKS_2025_SUMMARY['playoff_odds']}%")
    print(f"Biggest Gamble: {SEAHAWKS_2025_SUMMARY['biggest_gamble']}")
    print(f"Critical Success Factor: {SEAHAWKS_2025_SUMMARY['critical_success_factor']}")
    print(f"NFC West Standing: {SEAHAWKS_2025_SUMMARY['nfc_west_standing']}")
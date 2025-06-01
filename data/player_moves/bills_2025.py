"""
Buffalo Bills 2025 Offseason Moves
Defensive transformation to finally conquer Kansas City Chiefs
"""

BILLS_2025_MOVES = [
    # BILLS FREE AGENT SIGNINGS - Defensive Focus
    {
        'player_name': 'Joey Bosa',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 12600000,
        '2024_grade': 7.0,  # Five-time Pro Bowler despite injuries
        'projected_2025_grade': 7.5,  # Calculated gamble
        'snap_percentage_2024': 60.0,  # Missed 23 games over past 3 seasons
        'importance_to_old_team': 8.0,  # Former franchise cornerstone
        'importance_to_new_team': 8.5,  # Replaces Von Miller at half the cost
    },
    {
        'player_name': 'Josh Palmer',
        'position': 'WR2',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 36000000,
        '2024_grade': 7.0,  # 39 catches for 584 yards in 7 starts
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Downfield threat to complement Shakir
    },
    {
        'player_name': 'Michael Hoecht',
        'position': 'DT',
        'from_team': 'LAR',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 24000000,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,  # 6-game PED suspension to start 2025
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # When eligible
    },
    {
        'player_name': 'Larry Ogunjobi',
        'position': 'DT',
        'from_team': 'Pit',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,  # 6-game PED suspension to start 2025
        'snap_percentage_2024': 58.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # When eligible
    },
    
    # BILLS MAJOR LOSSES
    {
        'player_name': 'Von Miller',
        'position': 'EDGE',
        'from_team': 'Buf',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Production declined to just 6 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,  # $15.4M dead money, $23.8M cap hit untenable
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Amari Cooper',
        'position': 'WR1',
        'from_team': 'Buf',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # 32 catches for 297 yards in 8 games, played through wrist injury
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,  # Cap constraints prevented re-signing
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Mack Hollins',
        'position': 'WR3',
        'from_team': 'Buf',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
    },
    
    # BILLS TRADES
    {
        'player_name': 'Kaiir Elam',
        'position': 'CB2',
        'from_team': 'Buf',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.8,  # Former first-round pick failed to develop
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 4.0,  # Disappointing pick
        'importance_to_new_team': 0.0,
    },
    
    # BILLS DRAFT PICKS - Defense First Five Picks
    {
        'player_name': 'Maxwell Hairston',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #30',
        'contract_years': 4,
        'contract_value': 15200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Fastest 40-yard dash at combine (4.28)
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Expected to compete for starting role opposite Benford
    },
    {
        'player_name': 'T.J. Sanders',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #41 (via trade)',
        'contract_years': 4,
        'contract_value': 9800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 4.0 sacks in 2024, versatile interior pass rusher
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Three-down player to complement Ed Oliver
    },
    {
        'player_name': 'Landon Jackson',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #72',
        'contract_years': 4,
        'contract_value': 5800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 16 career sacks, impressive 6'6" length
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush depth
    },
    {
        'player_name': 'Deone Walker',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #105',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Massive body for interior run defense
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Reunites with teammate Hairston
    },
    {
        'player_name': 'Jordan Hancock',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #150 (from Elam trade)',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # Versatile DB with experience at corner, slot, safety
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Secondary depth
    },
    {
        'player_name': 'Jackson Hawes',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #173',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # First offense pick in 6th round
    },
    {
        'player_name': 'Chase Lundt',
        'position': 'RT',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #206',
        'contract_years': 4,
        'contract_value': 3400000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # OL depth
    },
    {
        'player_name': 'Kaden Prather',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Buf',
        'move_type': '2025 Draft Pick #255',
        'contract_years': 4,
        'contract_value': 3200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # 6'4" target, 500+ yards each of last 3 seasons
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
    },
    
    # BILLS KEY EXTENSIONS - Locking Up Young Core
    {
        'player_name': 'Josh Allen',
        'position': 'QB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 6,
        'contract_value': 330000000,  # Record-breaking deal
        '2024_grade': 9.5,  # MVP-caliber season
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,  # $250M guaranteed - highest in NFL history
    },
    {
        'player_name': 'Khalil Shakir',
        'position': 'WR1',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 53000000,
        '2024_grade': 8.0,  # 76 receptions for 821 yards, led team
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Just $2.6M cap hit in 2025 despite big deal
    },
    {
        'player_name': 'Greg Rousseau',
        'position': 'EDGE',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 80000000,
        '2024_grade': 7.8,
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Defensive cornerstone
    },
    {
        'player_name': 'Terrel Bernard',
        'position': 'LB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 50000000,
        '2024_grade': 8.2,  # Breakout 2024 campaign
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Developed under Bobby Babich
    },
    {
        'player_name': 'Christian Benford',
        'position': 'CB1',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 76000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,  # Key secondary piece
    },
    {
        'player_name': 'Damar Hamlin',
        'position': 'S',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 5000000,
        '2024_grade': 7.0,  # Started 14 games after remarkable recovery
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.0,  # Inspirational story
        'importance_to_new_team': 8.0,
    },
    {
        'player_name': 'Ty Johnson',
        'position': 'RB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2800000,
        '2024_grade': 7.0,  # Allen praised as team's "best third-down back"
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,  # Third-down specialist
    },
    {
        'player_name': 'Reid Ferguson',
        'position': 'LS',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 6000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,  # All special teams snaps
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,  # Longest-tenured Bill
    },
    
    # BILLS COACHING CONTINUITY
    {
        'player_name': 'Chris Tabor',
        'position': 'COACH',
        'from_team': 'Cle',
        'to_team': 'Buf',
        'move_type': 'Special Teams Coordinator Hire',
        'contract_years': 3,
        'contract_value': 0,
        '2024_grade': 7.0,  # Rated 2nd-best ST coordinator by NFLPA in 2022
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces fired Matthew Smiley
    },
]
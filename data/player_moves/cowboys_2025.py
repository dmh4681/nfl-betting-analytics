"""
Dallas Cowboys 2025 Offseason Moves
Jerry Jones' calculated response to playoff miss with coaching overhaul
"""

COWBOYS_2025_MOVES = [
    # COWBOYS FREE AGENT SIGNINGS
    {
        'player_name': 'Javonte Williams',
        'position': 'RB',
        'from_team': 'Den',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.5,  # 1,287 yards from scrimmage over last 2 seasons
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # Pass-catching complement
    },
    {
        'player_name': 'Miles Sanders',
        'position': 'RB',
        'from_team': 'Car',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 4.5,  # Career-low 205 rushing yards
        'projected_2025_grade': 6.0,  # Bounce-back potential
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 6.0,  # Veteran depth
    },
    {
        'player_name': 'Solomon Thomas',
        'position': 'DT',
        'from_team': 'NYJ',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 6.8,  # 8.5 sacks, 14 TFLs over 3 seasons
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Reunion with coach
    },
    {
        'player_name': 'Jack Sanborn',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.2,
        'projected_2025_grade': 7.0,  # Familiarity with Eberflus system
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,  # System fit
    },
    {
        'player_name': 'Payton Turner',
        'position': 'EDGE',
        'from_team': 'NO',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2800000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Depth addition
    },
    {
        'player_name': 'Parris Campbell',
        'position': 'WR3',
        'from_team': 'Dal',
        'to_team': 'Dal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.0,
    },
    {
        'player_name': 'Dante Fowler Jr.',
        'position': 'EDGE',
        'from_team': 'Was',
        'to_team': 'Dal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 6000000,
        '2024_grade': 7.5,  # 10.5 sacks with Washington
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Key pass rusher
    },
    
    # COWBOYS MAJOR LOSSES
    {
        'player_name': 'DeMarcus Lawrence',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Injury-limited to 4 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,  # Limited by injury
        'importance_to_old_team': 8.5,  # 4x Pro Bowler, longest-tenured
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jourdan Lewis',
        'position': 'CB2',
        'from_team': 'Dal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # Career-high 71 tackles, locker room leader
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,  # Highest-paid nickel corner
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Rico Dowdle',
        'position': 'RB',
        'from_team': 'Dal',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.2,  # First UDFA in Cowboys history with 1,000+ yards
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,  # 1,079 yards, 39 catches
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Chauncey Golston',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Career-highs: 56 tackles, 5.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Brandin Cooks',
        'position': 'WR1',
        'from_team': 'Dal',
        'to_team': 'NO',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Veteran production
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Cooper Rush',
        'position': 'QB',
        'from_team': 'Dal',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Reliable backup
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Chuma Edoga',
        'position': 'RT',
        'from_team': 'Dal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
    },
    
    # COWBOYS TRADES
    {
        'player_name': 'George Pickens',
        'position': 'WR1',
        'from_team': 'Pit',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 8000000,  # Remaining on rookie deal
        '2024_grade': 7.8,  # 59 catches, 900 yards
        'projected_2025_grade': 8.2,  # Compared to Dez Bryant
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Marquee acquisition
    },
    {
        'player_name': 'Kenneth Murray Jr.',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 15500000,  # Inherited contract
        '2024_grade': 7.2,  # 95 tackles, 3.5 sacks
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Former 1st round pick
    },
    {
        'player_name': 'Joe Milton III',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 3,
        'contract_value': 3000000,
        '2024_grade': 5.5,  # Limited NFL experience
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 6.0,  # Dallas-area native
    },
    {
        'player_name': 'Kaiir Elam',
        'position': 'CB2',
        'from_team': 'Buf',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 5.8,  # Former 1st round pick
        'projected_2025_grade': 6.5,  # Change of scenery
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 6.5,  # Depth with Diggs injury
    },
    
    # COWBOYS 2025 DRAFT PICKS
    {
        'player_name': 'Tyler Booker',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Dal',
        'move_type': '2025 Draft Pick #12',
        'contract_years': 4,
        'contract_value': 28000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Direct replacement for Zack Martin
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Expected immediate starter
    },
    {
        'player_name': 'Donovan Ezeiruaku',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Dal',
        'move_type': '2025 Draft Pick #44',
        'contract_years': 4,
        'contract_value': 8500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Led ACC with 16.5 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Replaces Lawrence production
    },
    {
        'player_name': 'Shavon Revel Jr.',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'Dal',
        'move_type': '2025 Draft Pick #76',
        'contract_years': 4,
        'contract_value': 5500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 6'3" press-man corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Could start opposite Bland
    },
    {
        'player_name': 'Jaydon Blue',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Dal',
        'move_type': '2025 Draft Pick #149',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 4.38 speed back
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Speed complement
    },
    {
        'player_name': 'Shemar James',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Dal',
        'move_type': '2025 Draft Pick #152',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Versatile linebacker
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
    },
    
    # COWBOYS KEY RE-SIGNINGS
    {
        'player_name': 'Osa Odighizuwa',
        'position': 'DT',
        'from_team': 'Dal',
        'to_team': 'Dal',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 80000000,
        '2024_grade': 8.0,
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Cornerstone of Eberflus defense
    },
    {
        'player_name': 'Markquese Bell',
        'position': 'S',
        'from_team': 'Dal',
        'to_team': 'Dal',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 12000000,
        '2024_grade': 7.5,  # 102 tackles in hybrid role
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
    },
    
    # COWBOYS COACHING CHANGES
    {
        'player_name': 'Brian Schottenheimer',
        'position': 'COACH',
        'from_team': 'PROMOTION',
        'to_team': 'Dal',
        'move_type': 'Head Coach Promotion',
        'contract_years': 4,
        'contract_value': 0,  # Coaching salary not disclosed
        '2024_grade': 7.0,  # Was OC
        'projected_2025_grade': 7.5,  # First-time HC
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Major organizational change
    },
    {
        'player_name': 'Matt Eberflus',
        'position': 'COACH',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 0,
        '2024_grade': 6.5,  # Fired as Bears HC
        'projected_2025_grade': 8.0,  # Returns to DC role, Dallas history
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Coordinator overhaul
    },
]
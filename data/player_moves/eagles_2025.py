"""
Philadelphia Eagles 2025 Offseason Moves
Complete analysis of Super Bowl champion roster reconstruction
"""

EAGLES_2025_MOVES = [
    # EAGLES FREE AGENT SIGNINGS - Value-based approach
    {
        'player_name': 'Azeez Ojulari',
        'position': 'EDGE',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 7.2,  # 6 sacks in 11 games with limited snaps
        'projected_2025_grade': 7.8,  # Should get more opportunity
        'snap_percentage_2024': 35.0,  # Limited behind Burns/Thibodeaux
        'importance_to_old_team': 6.0,  # Rotational piece
        'importance_to_new_team': 8.5,  # Key replacement for Sweat
    },
    {
        'player_name': 'Joshua Uche',
        'position': 'EDGE',
        'from_team': 'KC',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1920000,
        '2024_grade': 6.5,  # Only 2 sacks, 22% snaps
        'projected_2025_grade': 7.5,  # Bounce-back potential
        'snap_percentage_2024': 22.0,
        'importance_to_old_team': 4.0,  # Minimal role
        'importance_to_new_team': 7.0,  # Pass rush depth
    },
    {
        'player_name': 'Adoree Jackson',
        'position': 'CB2',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1755000,
        '2024_grade': 6.9,  # 69.0 PFF grade, ranked 58th
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 65.0,  # Started 5 of 14 games
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replaces Slay depth
    },
    {
        'player_name': 'A.J. Dillon',
        'position': 'RB',
        'from_team': 'GB',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1100000,
        '2024_grade': 0.0,  # Missed entire season with neck injury
        'projected_2025_grade': 6.5,  # Health unknown
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 3.0,
        'importance_to_new_team': 5.0,  # Backup depth
    },
    {
        'player_name': 'Harrison Bryant',
        'position': 'TE',
        'from_team': 'LV',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # TE depth
    },
    
    # EAGLES MAJOR LOSSES - Defensive exodus
    {
        'player_name': 'Josh Sweat',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.5,  # 8 sacks regular season + 2.5 in Super Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 59.0,  # Primary edge threat
        'importance_to_old_team': 9.0,  # Team-leading pass rusher
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Milton Williams',
        'position': 'DT',
        'from_team': 'Phi',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.2,  # 5 sacks, 54 pressures, Super Bowl strip-sack
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 48.0,
        'importance_to_old_team': 8.0,  # Key interior rusher
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Oren Burks',
        'position': 'LB',
        'from_team': 'Phi',
        'to_team': 'Cin',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Playoff hero, 25 tackles in 3 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 14.0,  # Mostly special teams
        'importance_to_old_team': 6.0,  # Special teams ace
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kenneth Gainwell',
        'position': 'RB',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,  # Backup RB
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Avonte Maddox',
        'position': 'CB2',
        'from_team': 'Phi',
        'to_team': 'Det',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 42.0,
        'importance_to_old_team': 6.5,  # Veteran depth
        'importance_to_new_team': 0.0,
    },
    
    # EAGLES TRADES
    {
        'player_name': 'C.J. Gardner-Johnson',
        'position': 'S',
        'from_team': 'Phi',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # 6 interceptions, emotional leader
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,  # Defensive leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kenyon Green',
        'position': 'G',
        'from_team': 'Hou',
        'to_team': 'Phi',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Interior line depth
    },
    {
        'player_name': 'Bryce Huff',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'SF',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Major disappointment, 2.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 4.0,  # Failed signing
        'importance_to_new_team': 0.0,
    },
    
    # EAGLES DRAFT PICKS - Defensive rebuild
    {
        'player_name': 'Jihaad Campbell',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Phi',
        'move_type': '2025 Draft Pick #31',
        'contract_years': 4,
        'contract_value': 12000000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 7.5,  # First-Team All-SEC
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starter
    },
    {
        'player_name': 'Andrew Mukuba',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Phi',
        'move_type': '2025 Draft Pick #45',
        'contract_years': 4,
        'contract_value': 8500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Led SEC with 5 INTs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replaces CJGJ
    },
    {
        'player_name': 'Ty Robinson',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Phi',
        'move_type': '2025 Draft Pick #112',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 12 TFL, 7 sacks at Nebraska
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces Milton Williams
    },
    
    # EAGLES RETIREMENTS
    {
        'player_name': 'Brandon Graham',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Played through torn triceps in Super Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 8.0,  # Franchise legend, emotional leader
        'importance_to_new_team': 0.0,
    },
    
    # EAGLES POST-JUNE 1 CUTS
    {
        'player_name': 'Darius Slay',
        'position': 'CB1',
        'from_team': 'Phi',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Still productive veteran
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,  # Veteran leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'James Bradberry',
        'position': 'CB2',
        'from_team': 'Phi',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
    },
]
"""
Houston Texans 2025 Offseason Moves
Complete analysis of calculated risk strategy under Nick Caserio and DeMeco Ryans
"""

TEXANS_2025_MOVES = [
    # TEXANS FREE AGENT SIGNINGS - Offensive line focus with mixed results
    {
        'player_name': 'Cam Robinson',
        'position': 'LT',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14500000,
        '2024_grade': 5.8,  # Allowed 9 sacks, 12.1% pressure rate
        'projected_2025_grade': 6.2,  # Better scheme fit hoped
        'snap_percentage_2024': 75.0,  # Split time between JAC/MIN
        'importance_to_old_team': 6.0,  # Inconsistent starter
        'importance_to_new_team': 8.5,  # Tunsil replacement
    },
    {
        'player_name': 'Trent Brown',
        'position': 'RT',
        'from_team': 'Cin',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        '2024_grade': 6.5,  # Veteran presence when healthy
        'projected_2025_grade': 6.8,  # Depth and competition
        'snap_percentage_2024': 60.0,  # Injury concerns
        'importance_to_old_team': 6.0,  # Rotational piece
        'importance_to_new_team': 7.0,  # Tackle depth/competition
    },
    {
        'player_name': 'Laken Tomlinson',
        'position': 'LG',
        'from_team': 'NYJ',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 6.8,  # Solid veteran guard
        'projected_2025_grade': 7.0,  # Interior upgrade
        'snap_percentage_2024': 85.0,  # Reliable starter
        'importance_to_old_team': 7.0,  # Starting guard
        'importance_to_new_team': 7.5,  # Interior line stability
    },
    {
        'player_name': 'Justin Watson',
        'position': 'WR3',
        'from_team': 'KC',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2200000,
        '2024_grade': 6.0,  # 1,322 career receiving yards
        'projected_2025_grade': 6.2,  # Depth receiver
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 6.0,  # WR depth after losses
    },
    {
        'player_name': 'Braxton Berrios',
        'position': 'WR3',
        'from_team': 'Mia',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.2,  # Slot receiver option
        'projected_2025_grade': 6.5,  # Familiar with new OC Caley
        'snap_percentage_2024': 50.0,  # Slot role
        'importance_to_old_team': 6.0,  # Reliable slot option
        'importance_to_new_team': 6.5,  # Slot depth
    },
    {
        'player_name': 'Derek Barnett',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8500000,
        '2024_grade': 6.0,  # Rotational pass rusher
        'projected_2025_grade': 6.3,  # Pass rush depth
        'snap_percentage_2024': 40.0,  # Rotation role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 6.0,  # Edge depth
    },
    {
        'player_name': 'Nick Niemann',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.0,  # Special teams value
        'projected_2025_grade': 6.0,  # Depth and special teams
        'snap_percentage_2024': 35.0,  # Limited snaps
        'importance_to_old_team': 5.0,  # Special teams contributor
        'importance_to_new_team': 5.5,  # LB depth
    },
    {
        'player_name': 'Tremon Smith',
        'position': 'CB2',
        'from_team': 'Den',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 5.8,  # Special teams focus
        'projected_2025_grade': 6.0,  # Depth corner
        'snap_percentage_2024': 25.0,  # Limited defensive role
        'importance_to_old_team': 5.0,  # Special teams
        'importance_to_new_team': 5.5,  # CB depth
    },

    # TEXANS RE-SIGNINGS - Historic extensions and continuity
    {
        'player_name': 'Derek Stingley Jr.',
        'position': 'CB1',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 90000000,
        '2024_grade': 9.0,  # All-Pro, 5 INTs, 18 pass breakups
        'projected_2025_grade': 9.2,  # Elite cornerback entering prime
        'snap_percentage_2024': 95.0,  # Played all 17 games
        'importance_to_old_team': 10.0,  # Franchise cornerstone
        'importance_to_new_team': 10.0,  # Highest-paid DB in NFL history
    },
    {
        'player_name': 'Danielle Hunter',
        'position': 'EDGE',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Extension',
        'contract_years': 1,
        'contract_value': 35600000,
        '2024_grade': 8.5,  # Productive first year in Houston
        'projected_2025_grade': 8.3,  # Elite pass rusher
        'snap_percentage_2024': 80.0,  # Key pass rusher
        'importance_to_old_team': 9.0,  # Premier edge rusher
        'importance_to_new_team': 9.0,  # Locked up through 2026
    },
    {
        'player_name': 'Mario Edwards Jr.',
        'position': 'DT',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 9500000,
        '2024_grade': 6.8,  # Effective run stopper
        'projected_2025_grade': 7.0,  # Rotational DT
        'snap_percentage_2024': 55.0,  # Rotation role
        'importance_to_old_team': 7.0,  # Key rotation piece
        'importance_to_new_team': 7.0,  # Defensive line depth
    },
    {
        'player_name': 'Dare Ogunbowale',
        'position': 'RB',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.5,  # Third-down back and special teams
        'projected_2025_grade': 6.5,  # Role player
        'snap_percentage_2024': 30.0,  # Situational back
        'importance_to_old_team': 6.0,  # Reliable third-down option
        'importance_to_new_team': 6.0,  # Continuity in backfield
    },
    {
        'player_name': 'Tyler Stewart',
        'position': 'S',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.0,  # Special teams value
        'projected_2025_grade': 6.0,  # Special teams ace
        'snap_percentage_2024': 20.0,  # 83% of special teams snaps
        'importance_to_old_team': 6.0,  # Special teams contributor
        'importance_to_new_team': 6.0,  # No risk depth signing
    },
    {
        'player_name': 'Justin Hinish',
        'position': 'DT',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1000000,
        '2024_grade': 6.0,  # Defensive tackle depth
        'projected_2025_grade': 6.0,  # Rotational DT
        'snap_percentage_2024': 25.0,  # Limited role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 5.5,  # Interior depth
    },

    # TEXANS MAJOR LOSSES - Controversial offensive line decisions
    {
        'player_name': 'Laremy Tunsil',
        'position': 'LT',
        'from_team': 'Hou',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 9.0,  # 4th-best pass-blocking tackle per PFF
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Zero pressures allowed in 7 games
        'importance_to_old_team': 9.5,  # Elite blindside protector
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kenyon Green',
        'position': 'RG',
        'from_team': 'Hou',
        'to_team': 'Phi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Allowed 14th-highest pressure rate (11.3%)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Struggled in starting role
        'importance_to_old_team': 6.0,  # Former 1st round pick underperformed
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Shaq Mason',
        'position': 'RG',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.2,  # Allowed 6th-most sacks (10.5)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Struggling starter
        'importance_to_old_team': 6.0,  # Veteran guard with declining play
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Stefon Diggs',
        'position': 'WR1',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # 610 receiving yards in limited role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Reduced role from previous years
        'importance_to_old_team': 7.0,  # Veteran receiver leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Robert Woods',
        'position': 'WR2',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Aging veteran receiver
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,  # Limited role
        'importance_to_old_team': 6.0,  # Veteran depth
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Eric Murray',
        'position': 'S',
        'from_team': 'Hou',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Starting safety
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Regular starter
        'importance_to_old_team': 7.0,  # Starting safety
        'importance_to_new_team': 0.0,
    },

    # TEXANS TRADES - Key acquisitions
    {
        'player_name': 'Christian Kirk',
        'position': 'WR2',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 6.8,  # Reliable slot presence with Jacksonville
        'projected_2025_grade': 7.2,  # Better QB play with Stroud
        'snap_percentage_2024': 75.0,  # Starting slot receiver
        'importance_to_old_team': 7.0,  # Key Jaguars receiver
        'importance_to_new_team': 8.0,  # Fills WR need after departures
    },
    {
        'player_name': 'C.J. Gardner-Johnson',
        'position': 'S',
        'from_team': 'Phi',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 8000000,
        '2024_grade': 8.0,  # 6 interceptions, emotional leader
        'projected_2025_grade': 7.8,  # Playmaking safety
        'snap_percentage_2024': 85.0,  # Starting safety for Eagles
        'importance_to_old_team': 8.5,  # Defensive leader lost by Eagles
        'importance_to_new_team': 8.5,  # Major secondary upgrade
    },
    {
        'player_name': 'Ed Ingram',
        'position': 'RG',
        'from_team': 'Min',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 6.0,  # Interior line depth from Minnesota
        'projected_2025_grade': 6.5,  # Guard competition
        'snap_percentage_2024': 60.0,  # Rotational guard
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 6.5,  # Interior line depth
    },

    # TEXANS 2025 NFL DRAFT - Receiver focus and offensive line help
    {
        'player_name': 'Jayden Higgins',
        'position': 'WR1',
        'from_team': 'DRAFT',
        'to_team': 'Hou',
        'move_type': '2025 Draft Pick #34',
        'contract_years': 4,
        'contract_value': 12800000,
        '2024_grade': 0.0,  # College - 6'4", 215 lbs, 4.47 speed
        'projected_2025_grade': 7.0,  # Big-body receiver for Stroud
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Key receiver addition
    },
    {
        'player_name': 'Aireontae Ersery',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Hou',
        'move_type': '2025 Draft Pick #48',
        'contract_years': 4,
        'contract_value': 9200000,
        '2024_grade': 0.0,  # College - Minnesota left tackle
        'projected_2025_grade': 6.8,  # Tackle depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Addresses OL depth needs
    },
    {
        'player_name': 'Jaylin Noel',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Hou',
        'move_type': '2025 Draft Pick #79',
        'contract_years': 4,
        'contract_value': 6100000,
        '2024_grade': 0.0,  # College - 4.37 speed, vertical threat
        'projected_2025_grade': 6.5,  # Deep threat receiver
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Speed element Texans lacked
    },
    {
        'player_name': 'USC Smith',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Hou',
        'move_type': '2025 Draft Pick #124',
        'contract_years': 4,
        'contract_value': 4600000,
        '2024_grade': 0.0,  # College - USC cornerback
        'projected_2025_grade': 6.0,  # Developmental corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # CB depth
    },
    {
        'player_name': 'D.J. Marks',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Hou',
        'move_type': '2025 Draft Pick #156',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - 1,133 rushing yards
        'projected_2025_grade': 6.2,  # Backfield depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # RB depth and competition
    },

    # TEXANS COACHING CHANGES - Major coordinator overhaul
    {
        'player_name': 'Bobby Slowik',
        'position': 'OC',
        'from_team': 'Hou',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Offense regressed from 22.2 to 21.9 PPG
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full offensive control
        'importance_to_old_team': 8.0,  # Promising young coordinator fired
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Caley',
        'position': 'OC',
        'from_team': 'LAR',
        'to_team': 'Hou',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 8000000,
        '2024_grade': 7.5,  # Los Angeles Rams coordinator success
        'projected_2025_grade': 7.8,  # Experienced coordinator
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost key coach to Houston
        'importance_to_new_team': 8.5,  # Fresh offensive perspective
    },
    {
        'player_name': 'Chris Strausser',
        'position': 'OL_COACH',
        'from_team': 'Hou',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # OL allowed 52 sacks (2nd-most in NFL)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full OL responsibility
        'importance_to_old_team': 6.0,  # Failed to protect Stroud
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Cole Popovich',
        'position': 'OL_COACH',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Promotion',
        'contract_years': 2,
        'contract_value': 2500000,
        '2024_grade': 6.5,  # Assistant OL coach promoted
        'projected_2025_grade': 7.0,  # Internal promotion
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Continuity choice
        'importance_to_new_team': 7.0,  # Familiar with personnel
    },
]

# TEXANS SUMMARY METRICS
TEXANS_2025_SUMMARY = {
    'total_moves': len(TEXANS_2025_MOVES),
    'free_agent_signings': 8,
    'major_losses': 6,
    'trades': 3,
    'draft_picks': 5,
    'key_resignings': 6,
    'coaching_changes': 4,
    'total_guaranteed_money': 175000000,  # Includes Stingley/Hunter extensions
    'salary_cap_space_remaining': 12000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'C+',
    'key_philosophy': 'Calculated risk with controversial OL decisions',
    'biggest_concern': 'Offensive line protection may have gotten worse',
    'biggest_strength': 'Locked up elite defensive talent'
}

if __name__ == "__main__":
    print(f"Houston Texans 2025 Offseason Moves: {TEXANS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {TEXANS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {TEXANS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${TEXANS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {TEXANS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {TEXANS_2025_SUMMARY['biggest_concern']}")
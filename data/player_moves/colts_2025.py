"""
Indianapolis Colts 2025 Offseason Moves
Complete analysis of measured approach under Chris Ballard and Shane Steichen
"""

COLTS_2025_MOVES = [
    # COLTS FREE AGENT SIGNINGS - Defensive overhaul and QB competition
    {
        'player_name': 'Daniel Jones',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14000000,
        '2024_grade': 6.8,  # Limited role with Vikings after Giants release
        'projected_2025_grade': 7.0,  # Legitimate QB competition
        'snap_percentage_2024': 30.0,  # Backup role in Minnesota
        'importance_to_old_team': 6.0,  # Depth quarterback
        'importance_to_new_team': 8.5,  # Competition for Richardson
    },
    {
        'player_name': 'Tim Boyle',
        'position': 'QB',
        'from_team': 'Mia',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 5.5,  # Veteran backup experience
        'projected_2025_grade': 5.8,  # Third quarterback depth
        'snap_percentage_2024': 15.0,  # Limited action
        'importance_to_old_team': 4.0,  # Depth piece
        'importance_to_new_team': 5.5,  # QB room depth
    },
    {
        'player_name': 'Charvarius Ward',
        'position': 'CB1',
        'from_team': 'SF',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        '2024_grade': 7.8,  # Proven #1 cornerback
        'projected_2025_grade': 8.0,  # Elite cornerback
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 8.0,  # Key 49ers defender
        'importance_to_new_team': 9.0,  # Biggest CB commitment under Ballard
    },
    {
        'player_name': 'Cam Bynum',
        'position': 'S',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 45000000,
        '2024_grade': 7.5,  # Career-high 3 INTs, 10 pass defenses
        'projected_2025_grade': 7.8,  # Proven safety
        'snap_percentage_2024': 95.0,  # Durable starter
        'importance_to_old_team': 7.5,  # Key Vikings safety
        'importance_to_new_team': 8.5,  # Major secondary upgrade
    },
    {
        'player_name': 'Will Harris',
        'position': 'S',
        'from_team': 'NO',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 6.0,  # Depth safety option
        'projected_2025_grade': 6.5,  # Safety depth
        'snap_percentage_2024': 60.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Saints depth piece
        'importance_to_new_team': 6.5,  # Secondary depth
    },
    {
        'player_name': 'Khalil Herbert',
        'position': 'RB',
        'from_team': 'Chi',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.0,  # Limited production in 2024
        'projected_2025_grade': 6.8,  # Depth behind Taylor
        'snap_percentage_2024': 35.0,  # Backup role
        'importance_to_old_team': 5.5,  # Bears backup
        'importance_to_new_team': 7.0,  # RB depth behind Taylor
    },
    {
        'player_name': 'Jerome Britt',
        'position': 'LB',
        'from_team': 'Car',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.2,  # Panthers linebacker depth
        'projected_2025_grade': 6.5,  # LB competition
        'snap_percentage_2024': 45.0,  # Rotational linebacker
        'importance_to_old_team': 6.0,  # Panthers depth
        'importance_to_new_team': 6.5,  # LB depth and competition
    },

    # COLTS FREE AGENCY LOSSES - Cap casualties and missed retentions
    {
        'player_name': 'Ryan Kelly',
        'position': 'C',
        'from_team': 'Ind',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Long-time center, declining play
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Starting center
        'importance_to_old_team': 7.0,  # Veteran leader at key position
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'E.J. Speed',
        'position': 'LB',
        'from_team': 'Ind',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Starting linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Regular starter
        'importance_to_old_team': 7.0,  # Starting linebacker departed
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Julian Blackmon',
        'position': 'S',
        'from_team': 'Ind',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Starting safety with injury history
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Injury-limited season
        'importance_to_old_team': 7.0,  # Starting safety when healthy
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Calvin Ridley',
        'position': 'WR1',
        'from_team': 'Ind',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # Productive receiver season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Primary receiver
        'importance_to_old_team': 8.0,  # Top receiving threat
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Josh Downs',
        'position': 'WR2',
        'from_team': 'Ind',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Promising young receiver
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Regular contributor
        'importance_to_old_team': 7.5,  # Emerging receiver talent
        'importance_to_new_team': 0.0,
    },

    # COLTS 2025 NFL DRAFT - Tyler Warren focus and competition additions
    {
        'player_name': 'Tyler Warren',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #14',
        'contract_years': 4,
        'contract_value': 28500000,
        '2024_grade': 0.0,  # College - Penn State versatile TE
        'projected_2025_grade': 7.5,  # Immediate impact TE
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Key target for Richardson
    },
    {
        'player_name': 'Jake Tuimoloau',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #45',
        'contract_years': 4,
        'contract_value': 12500000,
        '2024_grade': 0.0,  # College - Ohio State pass rusher
        'projected_2025_grade': 7.0,  # Edge rush potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush need addressed
    },
    {
        'player_name': 'Shavon Revel Jr.',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #80',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - East Carolina CB
        'projected_2025_grade': 6.5,  # Developmental corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # CB depth and competition
    },
    {
        'player_name': 'Anthony Gould',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #116',
        'contract_years': 4,
        'contract_value': 5200000,
        '2024_grade': 0.0,  # College - Oregon State receiver
        'projected_2025_grade': 6.0,  # WR depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Receiver depth after losses
    },
    {
        'player_name': 'Matt Lee',
        'position': 'C',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #152',
        'contract_years': 4,
        'contract_value': 4600000,
        '2024_grade': 0.0,  # College - Center prospect
        'projected_2025_grade': 6.2,  # Center competition
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces Ryan Kelly
    },
    {
        'player_name': 'Kyren Lacy',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #190',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - LSU receiver
        'projected_2025_grade': 5.8,  # Developmental WR
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # WR depth
    },
    {
        'player_name': 'Cooper Flanagan',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Ind',
        'move_type': '2025 Draft Pick #234',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Air Force linebacker
        'projected_2025_grade': 5.5,  # Special teams LB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Special teams and depth
    },

    # COLTS KEY RE-SIGNINGS - Core retention
    {
        'player_name': 'DeForest Buckner',
        'position': 'DT',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 46000000,
        '2024_grade': 8.5,  # Defensive anchor
        'projected_2025_grade': 8.2,  # Elite interior pass rusher
        'snap_percentage_2024': 85.0,  # Key defensive player
        'importance_to_old_team': 9.5,  # Defensive cornerstone
        'importance_to_new_team': 9.5,  # Critical retention
    },
    {
        'player_name': 'Jonathan Taylor',
        'position': 'RB',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 42000000,
        '2024_grade': 8.0,  # Franchise running back
        'projected_2025_grade': 7.8,  # Still elite when healthy
        'snap_percentage_2024': 70.0,  # Injury-limited season
        'importance_to_old_team': 9.0,  # Offensive centerpiece
        'importance_to_new_team': 9.0,  # Key offensive weapon
    },
    {
        'player_name': 'Michael Pittman Jr.',
        'position': 'WR1',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 60000000,
        '2024_grade': 7.8,  # Top receiver
        'projected_2025_grade': 8.0,  # Reliable #1 receiver
        'snap_percentage_2024': 90.0,  # Primary receiving target
        'importance_to_old_team': 8.5,  # Top receiving threat
        'importance_to_new_team': 8.5,  # Key target for Richardson
    },
    {
        'player_name': 'Quenton Nelson',
        'position': 'LG',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 18000000,
        '2024_grade': 7.5,  # Elite guard when healthy
        'projected_2025_grade': 7.8,  # Still dominant
        'snap_percentage_2024': 75.0,  # Injury-limited
        'importance_to_old_team': 8.5,  # Franchise guard
        'importance_to_new_team': 8.5,  # Offensive line anchor
    },
    {
        'player_name': 'Grover Stewart',
        'position': 'DT',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 16000000,
        '2024_grade': 7.0,  # Run-stopping DT
        'projected_2025_grade': 7.0,  # Interior line stability
        'snap_percentage_2024': 65.0,  # Rotational starter
        'importance_to_old_team': 7.0,  # Interior defensive depth
        'importance_to_new_team': 7.0,  # Defensive line depth
    },

    # COLTS COACHING CHANGES - Stability with new DC
    {
        'player_name': 'Lou Anarumo',
        'position': 'DC',
        'from_team': 'Cin',
        'to_team': 'Ind',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 12000000,
        '2024_grade': 6.5,  # Bengals defense struggled in 2024
        'projected_2025_grade': 7.5,  # Fresh defensive perspective
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost experienced coordinator
        'importance_to_new_team': 8.0,  # Defensive overhaul needed
    },
]

# COLTS SUMMARY METRICS
COLTS_2025_SUMMARY = {
    'total_moves': len(COLTS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 5,
    'draft_picks': 7,
    'key_resignings': 5,
    'coaching_changes': 1,
    'total_guaranteed_money': 140000000,  # Major defensive investments
    'salary_cap_space_remaining': 8500000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B-',
    'key_philosophy': 'Measured approach with roster competition focus',
    'biggest_concern': 'Anthony Richardson development and health',
    'biggest_strength': 'Significantly upgraded secondary'
}

if __name__ == "__main__":
    print(f"Indianapolis Colts 2025 Offseason Moves: {COLTS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {COLTS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {COLTS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${COLTS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {COLTS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {COLTS_2025_SUMMARY['biggest_concern']}")
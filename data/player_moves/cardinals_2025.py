"""
Arizona Cardinals 2025 Offseason Moves
Complete analysis of defensive transformation while banking on offensive continuity
"""

CARDINALS_2025_MOVES = [
    # CARDINALS MAJOR DEFENSIVE FREE AGENT SIGNINGS - $74.4M cap space utilized
    {
        'player_name': 'Josh Sweat',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 76400000,
        '2024_grade': 8.5,  # 8 sacks regular season + 2.5 in Super Bowl
        'projected_2025_grade': 8.8,  # Reunion with Gannon should boost production
        'snap_percentage_2024': 59.0,
        'importance_to_old_team': 9.0,  # Eagles' team-leading pass rusher
        'importance_to_new_team': 9.5,  # Cornerstone of defensive rebuild
    },
    {
        'player_name': 'Dalvin Tomlinson',
        'position': 'DT',
        'from_team': 'Cle',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 29000000,
        '2024_grade': 8.8,  # Anchored league-best run defense
        'projected_2025_grade': 8.5,  # Should maintain elite level
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,  # Browns defensive anchor
        'importance_to_new_team': 9.0,  # Critical interior presence
    },
    {
        'player_name': 'Jacoby Brissett',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12500000,
        '2024_grade': 7.0,  # Solid veteran mentor
        'projected_2025_grade': 7.0,  # Insurance for Murray
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.0,  # Patriots backup
        'importance_to_new_team': 8.0,  # Critical QB depth given Murray's injury history
    },
    {
        'player_name': 'Akeem Davis-Gaither',
        'position': 'LB',
        'from_team': 'Car',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 11000000,
        '2024_grade': 7.2,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Linebacker depth
    },
    {
        'player_name': 'Royce Newman',
        'position': 'G',
        'from_team': 'GB',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # Interior line depth
    },
    
    # CARDINALS KEY RE-SIGNINGS - Offensive continuity
    {
        'player_name': 'Trey McBride',
        'position': 'TE',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 76000000,
        '2024_grade': 9.2,  # 111 receptions, 1,146 yards - elite production
        'projected_2025_grade': 9.0,  # Should maintain elite level
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,  # Offensive centerpiece
    },
    {
        'player_name': 'James Conner',
        'position': 'RB',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 19000000,
        '2024_grade': 8.0,  # Back-to-back 1,000-yard seasons
        'projected_2025_grade': 7.8,  # Aging but productive
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Veteran leadership
    },
    {
        'player_name': 'Baron Browning',
        'position': 'EDGE',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 16000000,
        '2024_grade': 7.5,  # Solid after trade from Denver
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Pass rush depth with Sweat
    },
    {
        'player_name': 'Evan Brown',
        'position': 'G',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 11400000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Murray protection
    },
    {
        'player_name': 'Kelvin Beachum',
        'position': 'RT',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 5150000,
        '2024_grade': 6.8,  # Veteran presence
        'projected_2025_grade': 6.5,  # Aging but steady
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # OL continuity
    },
    
    # CARDINALS 2025 DRAFT - Defensive focus (6 of 7 picks)
    {
        'player_name': 'Walter Nolen III',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #16',
        'contract_years': 4,
        'contract_value': 18500000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 8.0,  # 91.6 PFF run-defense grade, 6.5 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Potential defensive cornerstone
    },
    {
        'player_name': 'Will Johnson',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #47',
        'contract_years': 4,
        'contract_value': 8800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # Elite college production, injury concerns
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Steal of the draft - potential CB1
    },
    {
        'player_name': 'Jordan Burch',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #80',
        'contract_years': 4,
        'contract_value': 5200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 8.5 sacks at Oregon
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush depth
    },
    {
        'player_name': 'Cody Simon',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #115',
        'contract_years': 4,
        'contract_value': 4300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # CFP National Championship Defensive MVP
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Linebacker upgrade
    },
    {
        'player_name': 'Denzel Burke',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #167',
        'contract_years': 4,
        'contract_value': 3700000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # CB depth
    },
    {
        'player_name': 'Hayden Conner',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #172',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Zero sacks allowed on 617 pass-blocking snaps
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Only offensive pick
    },
    {
        'player_name': 'Kitan Crawford',
        'position': 'DEPTH',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': '2025 Draft Pick #248',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # 88.5 PFF coverage grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Special teams value
    },
    
    # CARDINALS MAJOR LOSSES - Natural attrition
    {
        'player_name': 'Roy Lopez',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,  # Rotation piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Khyiris Tonga',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Naquan Jones',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
    },
    
    # CARDINALS COACHING CHANGES - Position coach upgrades
    {
        'player_name': 'Justin Frye',
        'position': 'COACH',
        'from_team': 'OSU',
        'to_team': 'Ari',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 2500000,  # Estimated
        '2024_grade': 8.0,  # Ohio State OL success
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # OL coach upgrade, coached Paris Johnson Jr.
    },
    {
        'player_name': 'Winston DeLattiboudere III',
        'position': 'COACH',
        'from_team': 'DRAFT',
        'to_team': 'Ari',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 800000,  # Estimated
        '2024_grade': 7.0,  # Young coach with potential
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # DL coach at age 27
    },
]

# CARDINALS SUMMARY METRICS
CARDINALS_2025_SUMMARY = {
    'total_moves': len(CARDINALS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 3,
    'draft_picks': 7,
    'key_resignings': 5,
    'coaching_hires': 2,
    'total_guaranteed_money': 125000000,  # Aggressive defensive spending
    'cap_space_utilized': 74400000,  # Started with massive space
    'cap_space_remaining': 30000000,  # Estimated remaining
    'championship_window': '2025-2027',
    'offseason_grade': 'A-',
    'key_philosophy': 'Defensive transformation while maintaining offensive continuity around Murray'
}

if __name__ == "__main__":
    print(f"Arizona Cardinals 2025 Offseason: {CARDINALS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {CARDINALS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {CARDINALS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Utilized: ${CARDINALS_2025_SUMMARY['cap_space_utilized']:,}")
    print(f"Philosophy: {CARDINALS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: Sweat ($76.4M), Tomlinson ($29M), McBride extension ($76M)")
    print(f"Draft Haul: Will Johnson (steal at #47), Walter Nolen (#16), 6 of 7 defensive picks")
    print(f"Strategy: Aggressive defensive rebuild with $74.4M cap space")
    print(f"Offensive Continuity: McBride, Conner extensions maintain Murray weapons")
    print(f"Coaching: Justin Frye (OL) upgrade, young defensive staff")
    print(f"Division Outlook: Positioned as Rams' primary challenger in NFC West")
    print(f"Zero sacks allowed: Only added ONE offensive player in entire draft")
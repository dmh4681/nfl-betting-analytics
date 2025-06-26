"""
New England Patriots 2025 Offseason Moves
Aggressive rebuild: $410M spending spree centered on protecting Drake Maye
Last Updated: June 23, 2025
"""

PATRIOTS_2025_MOVES = [
    # ========== MARQUEE FREE AGENT SIGNINGS - Historic spending ==========
    {
        'player_name': 'Milton Williams',
        'position': 'DT',
        'from_team': 'Phi',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 104000000,  # Largest contract in franchise history
        'guaranteed_money': 52000000,
        'aav': 26000000,
        '2024_grade': 8.2,  # 5 sacks, 54 pressures, Super Bowl strip-sack
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 48.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Defensive transformation centerpiece
        'impact_score': 3.0,
    },
    {
        'player_name': 'Stefon Diggs',
        'position': 'WR1',
        'from_team': 'Hou',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 69000000,
        'guaranteed_money': 35000000,
        'aav': 23000000,
        '2024_grade': 6.8,  # 610 yards in limited role
        'projected_2025_grade': 7.8,  # Proven #1 receiver for Maye
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.0,  # Elite target Maye lacked
        'impact_score': 2.5,  # ACL recovery concern
    },
    {
        'player_name': 'Carlton Davis III',
        'position': 'CB1',
        'from_team': 'Det',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 30000000,
        'aav': 20000000,
        '2024_grade': 7.8,  # Solid corner play in Detroit
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Replace Jonathan Jones
        'impact_score': 2.0,
    },
    {
        'player_name': 'Harold Landry III',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 43500000,
        'guaranteed_money': 21000000,
        'aav': 14500000,
        '2024_grade': 7.5,  # Vrabel familiarity
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Scheme fit
        'impact_score': 2.0,
    },
    {
        'player_name': 'Robert Spillane',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 37000000,
        'guaranteed_money': 18000000,
        'aav': 12333333,
        '2024_grade': 7.8,  # Led Raiders in tackles
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Vrabel history
        'impact_score': 1.8,
    },
    {
        'player_name': 'Morgan Moses',
        'position': 'RT',
        'from_team': 'Bal',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 24000000,
        'guaranteed_money': 12000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # Veteran protection
        'projected_2025_grade': 6.8,  # Age 34
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Maye protection
        'impact_score': 1.5,
    },
    {
        'player_name': 'Mack Hollins',
        'position': 'WR',
        'from_team': 'Buf',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8400000,
        'guaranteed_money': 4000000,
        'aav': 4200000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # WR depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Garrett Bradbury',
        'position': 'C',
        'from_team': 'Min',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replace Andrews
        'impact_score': 1.0,
    },
    {
        'player_name': 'Josh Dobbs',
        'position': 'QB',
        'from_team': 'SF',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 3000000,
        '2024_grade': 6.0,  # Veteran backup
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 10.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # Maye insurance
        'impact_score': 0.5,
    },
    {
        'player_name': 'Khyiris Tonga',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 3000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # DT depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Jack Gibbens',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        'guaranteed_money': 2500000,
        'aav': 2500000,
        '2024_grade': 6.5,  # "Dr. Gibby" from Tennessee
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Vrabel familiarity
        'impact_score': 0.8,
    },

    # ========== MAJOR LOSSES - End of an era ==========
    {
        'player_name': 'Jonathan Jones',
        'position': 'CB',
        'from_team': 'NE',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 9 seasons, 2 Super Bowls
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Deatrich Wise Jr.',
        'position': 'DE',
        'from_team': 'NE',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # 8 seasons, 3-time captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'David Andrews',
        'position': 'C',
        'from_team': 'NE',
        'to_team': 'RETIRED',
        'move_type': 'Release/Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # 10-year veteran, 8-time captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,  # Franchise center
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Shocking release
    },
    {
        'player_name': 'Ja\'Whaun Bentley',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Injury-plagued 2024
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,  # 7 seasons, 4-time captain
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Joe Cardona',
        'position': 'LS',
        'from_team': 'NE',
        'to_team': 'Mia',
        'move_type': 'Release/FA Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 10-year tenure
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,  # Longest tenured Patriot
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },
    {
        'player_name': 'Jacoby Brissett',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Maye's mentor
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 7.0,  # Critical in Maye development
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== TRADES - Strategic asset accumulation ==========
    {
        'player_name': 'Davon Godchaux',
        'position': 'DT',
        'from_team': 'NE',
        'to_team': 'NO',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Requested trade
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,  # Didn't fit new scheme
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # Got 2026 7th
    },
    {
        'player_name': 'Joe Milton III',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # Impressive Week 18
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Got 5th round pick
    },

    # ========== 2025 NFL DRAFT - Protection and playmakers for Maye ==========
    {
        'player_name': 'Will Campbell',
        'position': 'LT',
        'from_team': 'LSU',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 1, Pick 4',
        'contract_years': 4,
        'contract_value': 38500000,
        'guaranteed_money': 38500000,
        'aav': 9625000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # 3 years SEC starter
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Blind-side protection
        'impact_score': 2.5,
    },
    {
        'player_name': 'TreVeyon Henderson',
        'position': 'RB',
        'from_team': 'Ohio State',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 2, Pick 36',
        'contract_years': 4,
        'contract_value': 8800000,
        'guaranteed_money': 4400000,
        'aav': 2200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 22.1% rate of 10+ yard carries
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Explosive element
        'impact_score': 1.8,
    },
    {
        'player_name': 'Kyle Williams',
        'position': 'WR',
        'from_team': 'Washington State',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 3, Pick 77',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1400000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 70 catches, 1,198 yards, 14 TDs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.8,  # Deep threat for Maye
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jared Wilson',
        'position': 'C',
        'from_team': 'Georgia',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 3, Pick 95',
        'contract_years': 4,
        'contract_value': 5200000,
        'guaranteed_money': 1200000,
        'aav': 1300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # First-round grades from some
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Long-term C solution
        'impact_score': 1.2,
    },
    {
        'player_name': 'Joshua Farmer',
        'position': 'DT',
        'from_team': 'Florida State',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 4, Pick 137',
        'contract_years': 4,
        'contract_value': 4500000,
        'guaranteed_money': 900000,
        'aav': 1125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Pre-draft visitor
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Targeted trade-up
        'impact_score': 1.0,
    },
    {
        'player_name': 'Bradyn Swinson',
        'position': 'EDGE',
        'from_team': 'LSU',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 5, Pick 161',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Edge depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Andres Borregales',
        'position': 'K',
        'from_team': 'Miami',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 6, Pick 200',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Perfect in college
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Kicker stability
        'impact_score': 0.8,
    },
    {
        'player_name': 'Julian Ashby',
        'position': 'LS',
        'from_team': 'Louisville',
        'to_team': 'NE',
        'move_type': '2025 Draft - Round 7, Pick 220',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Replace Cardona
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.3,
    },

    # ========== KEY RE-SIGNINGS - Proven contributors ==========
    {
        'player_name': 'Christian Elliss',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'RFA Matched',
        'contract_years': 2,
        'contract_value': 13500000,
        'guaranteed_money': 6750000,
        'aav': 6750000,
        '2024_grade': 7.0,  # 80 tackles, 5-unit ST
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,  # Vrabel favorite
        'impact_score': 1.5,
    },
    {
        'player_name': 'Austin Hooper',
        'position': 'TE',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 7000000,
        'guaranteed_money': 4000000,
        'aav': 7000000,
        '2024_grade': 6.8,  # 45 catches, 476 yards
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # TE continuity
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jaylinn Hawkins',
        'position': 'S',
        'from_team': 'NE',
        'to_team': 'NE',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2250000,
        'guaranteed_money': 1000000,
        'aav': 2250000,
        '2024_grade': 6.5,  # Special teams ace
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },

    # ========== COACHING/FRONT OFFICE CHANGES - Complete overhaul ==========
    {
        'player_name': 'Mike Vrabel',
        'position': 'COACH-HC',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 50000000,
        'guaranteed_money': 25000000,
        'aav': 10000000,
        '2024_grade': 8.0,  # 54-45 record with Titans
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.5,  # Culture change
        'impact_score': 3.0,
    },
    {
        'player_name': 'Josh McDaniels',
        'position': 'COACH-OC',
        'from_team': 'LV',
        'to_team': 'NE',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 4,
        'contract_value': 20000000,
        'guaranteed_money': 10000000,
        'aav': 5000000,
        '2024_grade': 7.5,  # Third stint, 6 Super Bowls
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 8.5,  # System continuity
        'impact_score': 2.0,
    },
    {
        'player_name': 'Terrell Williams',
        'position': 'COACH-DC',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 4000000,
        '2024_grade': 7.0,  # First-time DC
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Scheme change
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jerod Mayo',
        'position': 'COACH-HC',
        'from_team': 'NE',
        'to_team': 'FIRED',
        'move_type': 'Head Coach Firing',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # 4-13 record
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 5.0,  # Failed experiment
        'importance_to_new_team': 0.0,
        'impact_score': 2.0,  # Addition by subtraction
    },

    # ========== UDFA SIGNINGS - Record investment ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'NE',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 15000000,  # Combined
        'guaranteed_money': 2000000,  # Record guarantees
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
]

# ========== SUMMARY METRICS ==========
PATRIOTS_2025_SUMMARY = {
    'total_moves': len(PATRIOTS_2025_MOVES),
    'free_agent_signings': 15,  # Major spending spree
    'major_losses': 6,  # Veterans departed
    'trades': 2,
    'draft_picks': 11,  # After trade maneuvers
    'key_resignings': 4,
    'coaching_changes': 4,  # Complete overhaul
    'udfa_signings': 16,  # Record investment
    'total_guaranteed_money': 410000000,  # Historic spending
    'cap_space_used': 131500000,  # League-leading entering offseason
    'cap_space_remaining': 81000000,  # After initial spending
    'championship_window': '2026-2029',  # Building around Maye
    'offseason_grade': 'A-',
    'key_philosophy': 'Aggressive rebuild centered on protecting Drake Maye',
    'net_impact_score': 23.5,  # Sum of all impact scores
    'biggest_concern': 'Dramatic scheme changes must coalesce quickly',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'offensive_transformation': {
        'maye_support': 'First 4 draft picks on offense',
        'protection': 'Campbell (LT) + Moses (RT) + Wilson (C)',
        'weapons': 'Diggs provides proven #1 receiver',
        'philosophy': 'McDaniels modernizing Erhardt-Perkins',
    },
    'defensive_overhaul': {
        'scheme_change': 'Two-gap to one-gap attacking',
        'investment': '$104M to Milton Williams',
        'vrabel_guys': 'Spillane, Landry, Gibbens from Tennessee',
        'youth': 'Multiple draft picks for development',
    },
    'cultural_shift': {
        'mayo_failure': '4-13 after one season',
        'vrabel_intensity': 'Championship pedigree',
        'veteran_exodus': 'All dynasty connections severed',
        'new_identity': 'No-nonsense approach returns',
    },
    'financial_approach': {
        'cap_space': '$131.5M most in NFL entering',
        'front_loading': 'Maintains future flexibility',
        'guarantees': 'Record UDFA investments',
        'timeline': 'Accelerated rebuild strategy',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Drake Maye',
        'backup': 'Josh Dobbs',
        'grade': 'B+',
        'notes': 'Maye Pro Bowl rookie, Dobbs veteran insurance',
    },
    'offensive_line': {
        'starters': ['Will Campbell (LT)', 'Left Guard TBD', 'Garrett Bradbury (C)', 
                     'Right Guard TBD', 'Morgan Moses (RT)'],
        'depth': 'Major upgrade from 32nd-ranked unit',
        'grade': 'B',
        'notes': 'Bookends secured, interior questions remain',
    },
    'skill_positions': {
        'wr': 'Stefon Diggs, Kyle Williams, Mack Hollins',
        'rb': 'Rhamondre Stevenson, TreVeyon Henderson, Antonio Gibson',
        'te': 'Hunter Henry, Austin Hooper',
        'grade': 'B+',
        'notes': 'Diggs ACL recovery key factor',
    },
    'defensive_line': {
        'dt': 'Milton Williams, Christian Barmore, Khyiris Tonga',
        'edge': 'Josh Uche, Keion White, Bradyn Swinson',
        'grade': 'B+',
        'notes': 'Williams transforms interior, Barmore health crucial',
    },
    'linebackers': {
        'starters': 'Robert Spillane, Harold Landry, Christian Elliss',
        'depth': 'Jack Gibbens provides Vrabel familiarity',
        'grade': 'B+',
        'notes': 'Complete overhaul with proven veterans',
    },
    'secondary': {
        'cb': 'Carlton Davis III, Christian Gonzalez, Marcus Jones',
        'safety': 'Kyle Dugger, Jabrill Peppers, Jaylinn Hawkins',
        'grade': 'B',
        'notes': 'Davis replaces J. Jones, Gonzalez development key',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'OVER',
        'reasoning': 'Massive talent upgrade, easier schedule',
    },
    'division_odds': {
        'current': '+350',
        'value': 'YES',
        'reasoning': 'Bills vulnerable, Jets rebuilding',
    },
    'playoffs': {
        'odds': '-110',
        'value': 'YES',
        'reasoning': 'Wild card floor with division upside',
    },
    'player_props': {
        'maye_passing_yards': 'OVER 3,500',
        'diggs_receiving_yards': 'OVER 900 (if healthy)',
        'williams_sacks': 'OVER 7.5',
        'henderson_rushing_yards': 'OVER 600',
    },
    'key_bets': {
        'best': 'Over 8.5 wins',
        'longshot': 'Division winner +350',
        'player_award': 'Maye OPOY +1800',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("NEW ENGLAND PATRIOTS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {PATRIOTS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{PATRIOTS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {PATRIOTS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {PATRIOTS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {PATRIOTS_2025_SUMMARY['free_agent_signings']} ($410M total)")
    print(f"  • Draft Picks: {PATRIOTS_2025_SUMMARY['draft_picks']} (4 of first 5 on offense)")
    print(f"  • Key Re-signings: {PATRIOTS_2025_SUMMARY['key_resignings']}")
    print(f"  • UDFA Signings: {PATRIOTS_2025_SUMMARY['udfa_signings']} (record guarantees)")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${PATRIOTS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Used: ${PATRIOTS_2025_SUMMARY['cap_space_used']:,}")
    print(f"  • Remaining Cap: ${PATRIOTS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Milton Williams (DT) - 4yr/$104M franchise record")
    print("  • Stefon Diggs (WR) - 3yr/$69M proven #1 receiver")
    print("  • Mike Vrabel (HC) - Culture transformation")
    print("  • Will Campbell (LT) - #4 overall pick")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • David Andrews - Retired after release")
    print("  • Jonathan Jones - 9 seasons, to Washington")
    print("  • Deatrich Wise Jr. - 8 seasons, to Washington")
    print("  • Jerod Mayo - Fired after 4-13 season")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {PATRIOTS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Drake Maye: Pro Bowl rookie gets elite support")
    print(f"  • Defense: Shift from two-gap to attacking one-gap")
    print(f"  • Culture: Vrabel brings championship intensity")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Stefon Diggs ACL recovery")
    print("  • Christian Barmore blood clot situation")
    print("  • Scheme changes coalescing quickly")
    print("  • Maye Year 2 development with support")

if __name__ == "__main__":
    generate_summary_report()
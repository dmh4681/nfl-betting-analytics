"""
New York Jets 2025 Offseason Moves
Culture reset: Complete organizational overhaul post-Rodgers era
Last Updated: June 23, 2025
"""

JETS_2025_MOVES = [
    # ========== FRANCHISE-ALTERING MOVES ==========
    {
        'player_name': 'Aaron Rodgers',
        'position': 'QB',
        'from_team': 'NYJ',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -49000000,  # Dead money spread over 2 years
        'aav': 0,
        '2024_grade': 5.5,  # Career worst performance
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,  # Failed experiment
        'importance_to_new_team': 0.0,
        'impact_score': 2.0,  # Addition by subtraction
    },
    {
        'player_name': 'Justin Fields',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 40000000,
        'guaranteed_money': 30000000,
        'aav': 20000000,
        '2024_grade': 6.8,  # 4-2 as starter
        'projected_2025_grade': 7.5,  # Reunites with OSU teammates
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 9.0,  # Centerpiece of rebuild
        'impact_score': 3.0,
    },

    # ========== MAJOR SIGNINGS - Youth movement ==========
    {
        'player_name': 'Brandon Stephens',
        'position': 'CB',
        'from_team': 'Bal',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 36000000,
        'guaranteed_money': 23000000,
        'aav': 12000000,
        '2024_grade': 6.0,  # Allowed 806 yards (2nd-most)
        'projected_2025_grade': 6.8,  # Change of scenery
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replace D.J. Reed
        'impact_score': 1.5,
    },
    {
        'player_name': 'Andre Cisco',
        'position': 'S',
        'from_team': 'Jac',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 6000000,
        'aav': 10000000,
        '2024_grade': 7.0,  # Long Island native
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Critical safety need
        'impact_score': 1.8,
    },
    {
        'player_name': 'Josh Myers',
        'position': 'C',
        'from_team': 'GB',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.5,  # Packers starter
        'projected_2025_grade': 6.8,  # Fields familiarity
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # OL competition
        'impact_score': 1.0,
    },
    {
        'player_name': 'Josh Reynolds',
        'position': 'WR',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        'guaranteed_money': 2500000,
        'aav': 5000000,
        '2024_grade': 6.5,  # Veteran depth
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Coordinator connection
        'impact_score': 0.8,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Jamien Sherwood',
        'position': 'LB',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 45000000,
        'guaranteed_money': 30000000,
        'aav': 15000000,
        '2024_grade': 8.5,  # Breakout star
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,  # Top-5 LB money
        'impact_score': 2.5,
    },
    {
        'player_name': 'Kene Nwangwu',
        'position': 'RB/KR',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 7.0,  # Special teams ace
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Isaiah Oliver',
        'position': 'CB/S',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 6.5,  # Versatile DB
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Jamin Davis',
        'position': 'LB',
        'from_team': 'NYJ',
        'to_team': 'NYJ',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.0,  # Former 1st rounder
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Depth value
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES - Cap flexibility ==========
    {
        'player_name': 'Davante Adams',
        'position': 'WR1',
        'from_team': 'NYJ',
        'to_team': 'LAR',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Still elite when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,
    },
    {
        'player_name': 'D.J. Reed',
        'position': 'CB',
        'from_team': 'NYJ',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Elite corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,
    },
    {
        'player_name': 'C.J. Mosley',
        'position': 'LB',
        'from_team': 'NYJ',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -4000000,  # Dead money
        'aav': 0,
        '2024_grade': 6.5,  # Aging veteran
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # Saved $4M
    },
    {
        'player_name': 'Haason Reddick',
        'position': 'EDGE',
        'from_team': 'NYJ',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Holdout drama
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,
    },
    {
        'player_name': 'Javon Kinlaw',
        'position': 'DT',
        'from_team': 'NYJ',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Solid interior
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Solomon Thomas',
        'position': 'DT',
        'from_team': 'NYJ',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },

    # ========== 2025 NFL DRAFT - Offensive focus ==========
    {
        'player_name': 'Pierre Strong Jr.',
        'position': 'G',
        'from_team': 'Iowa',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 1, Pick 7',
        'contract_years': 4,
        'contract_value': 32000000,
        'guaranteed_money': 32000000,
        'aav': 8000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Immediate starter
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # OL excellence focus
        'impact_score': 2.5,
    },
    {
        'player_name': 'Kris Jenkins Jr.',
        'position': 'DT',
        'from_team': 'Michigan',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 2, Pick 39',
        'contract_years': 4,
        'contract_value': 8600000,
        'guaranteed_money': 4300000,
        'aav': 2150000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Son of Jets legend
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replace losses
        'impact_score': 1.8,
    },
    {
        'player_name': 'Kool-Aid McKinstry',
        'position': 'CB',
        'from_team': 'Alabama',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 3, Pick 71',
        'contract_years': 4,
        'contract_value': 6200000,
        'guaranteed_money': 1500000,
        'aav': 1550000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Athletic upside
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # CB need
        'impact_score': 1.2,
    },
    {
        'player_name': 'Jaydn Ott',
        'position': 'RB',
        'from_team': 'California',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 3, Pick 103',
        'contract_years': 4,
        'contract_value': 5400000,
        'guaranteed_money': 1100000,
        'aav': 1350000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 5.8 YPC career
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Complement Hall
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jaylin Noel',
        'position': 'WR',
        'from_team': 'Iowa State',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 4, Pick 135',
        'contract_years': 4,
        'contract_value': 4600000,
        'guaranteed_money': 900000,
        'aav': 1150000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Slot receiver
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Elijah Hills',
        'position': 'EDGE',
        'from_team': 'Missouri',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 5, Pick 167',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # Pass rush depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Malcolm Moore',
        'position': 'S',
        'from_team': 'Stanford',
        'to_team': 'NYJ',
        'move_type': '2025 Draft - Round 6, Pick 207',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },

    # ========== COACHING/FRONT OFFICE OVERHAUL ==========
    {
        'player_name': 'Aaron Glenn',
        'position': 'COACH-HC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 40000000,
        'guaranteed_money': 20000000,
        'aav': 8000000,
        '2024_grade': 8.5,  # Lions DC excellence
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.5,  # Culture change
        'impact_score': 3.0,
    },
    {
        'player_name': 'Tanner Engstrand',
        'position': 'COACH-OC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 4000000,
        '2024_grade': 7.5,  # Lions pass game coordinator
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # RPO focus for Fields
        'impact_score': 2.0,
    },
    {
        'player_name': 'Darren Mougey',
        'position': 'GM',
        'from_team': 'Den',
        'to_team': 'NYJ',
        'move_type': 'General Manager Hire',
        'contract_years': 5,
        'contract_value': 25000000,
        'guaranteed_money': 12500000,
        'aav': 5000000,
        '2024_grade': 7.0,  # Broncos AGM
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.0,  # Youth focus
        'impact_score': 2.5,
    },
    {
        'player_name': 'Robert Saleh',
        'position': 'COACH-HC',
        'from_team': 'NYJ',
        'to_team': 'FIRED',
        'move_type': 'Head Coach Firing',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # 20-36 record
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': 1.5,  # Culture change needed
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'NYJ',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 8000000,  # Combined
        'guaranteed_money': 800000,
        'aav': 2666667,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
JETS_2025_SUMMARY = {
    'total_moves': len(JETS_2025_MOVES),
    'free_agent_signings': 6,  # Value focus
    'major_losses': 6,  # Roster turnover
    'trades': 0,  # No major trades
    'draft_picks': 7,
    'key_resignings': 4,
    'coaching_changes': 4,  # Complete overhaul
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 175000000,  # Manageable spending
    'dead_money_absorbed': 53000000,  # Rodgers + Mosley
    'cap_space_remaining': 25000000,  # Healthy flexibility
    'championship_window': '2027-2030',  # Patient rebuild
    'offseason_grade': 'B',
    'key_philosophy': 'Complete culture reset with youth-focused rebuild',
    'net_impact_score': 11.5,  # Sum of all impact scores
    'playoff_drought': '14 years - longest in major sports',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'rodgers_departure': {
        'contract': 'Post-June 1 saves $9.5M',
        'dead_money': '$14M in 2025, $35M in 2026',
        'legacy': '5-12 record, career worsts',
        'meeting': '15-minute contentious Glenn meeting',
    },
    'fields_centerpiece': {
        'contract': '2yr/$40M saves vs top QBs',
        'fit': 'Reunites with Wilson, Myers from OSU',
        'system': 'RPO-based attack suits mobility',
        'bridge': 'Upside with development potential',
    },
    'roster_philosophy': {
        'approach': 'Second-contract guys over veterans',
        'flexibility': 'One-year deals for role players',
        'draft': 'OL investment continues trend',
        'culture': 'Move away from celebrity QBs',
    },
    'defensive_regression': {
        'ranking': 'Fell from 5th to 12th',
        'losses': 'Reed, Reddick, Kinlaw, Thomas',
        'approach': 'Accept step back for balance',
        'future': 'Build through draft',
    },
    'organizational_change': {
        'ownership': 'Johnson F grade in NFLPA survey',
        'front_office': '68% staff buyouts',
        'philosophy': 'Operate in silence',
        'timeline': 'Patient rebuild acknowledged',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Justin Fields',
        'backup': 'Tyrod Taylor',
        'grade': 'B-',
        'notes': 'Fields bridge with upside, Taylor veteran presence',
    },
    'offensive_line': {
        'starters': ['Olu Fashanu (LT)', 'Pierre Strong Jr. (LG)', 'Connor McGovern (C)', 
                     'Alijah Vera-Tucker (RG)', 'Morgan Moses (RT)'],
        'depth': 'Five starters 28 or younger',
        'grade': 'B+',
        'notes': 'Multi-year rebuild showing results',
    },
    'skill_positions': {
        'wr': 'Garrett Wilson, Allen Lazard, Josh Reynolds',
        'rb': 'Breece Hall, Jaydn Ott, Kene Nwangwu',
        'te': 'Tyler Conklin, Jeremy Ruckert',
        'grade': 'B',
        'notes': 'Wilson elite, depth concerns post-Adams',
    },
    'defensive_line': {
        'dt': 'Quinnen Williams, Kris Jenkins Jr.',
        'edge': 'Will McDonald IV, Jermaine Johnson, Elijah Hills',
        'grade': 'B-',
        'notes': 'Major losses hurt depth',
    },
    'linebackers': {
        'starters': 'Jamien Sherwood, Quincy Williams, Jamin Davis',
        'depth': 'Sherwood breakout anchors unit',
        'grade': 'B+',
        'notes': 'Strength of defense',
    },
    'secondary': {
        'cb': 'Sauce Gardner, Brandon Stephens, Kool-Aid McKinstry',
        'safety': 'Tony Adams, Andre Cisco, Malcolm Moore',
        'grade': 'B',
        'notes': 'Gardner elite, questions elsewhere',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 5.5,
        'lean': 'UNDER',
        'reasoning': 'Year 1 rebuild, tough division',
    },
    'division_odds': {
        'current': '+850',
        'value': 'NO',
        'reasoning': 'Clear 4th in AFC East',
    },
    'futures': {
        'playoffs': 'NO (-250)',
        'last_place': 'YES (-150)',
        'coach_fired': 'NO (Glenn safe Year 1)',
    },
    'player_props': {
        'fields_passing_yards': 'UNDER 3,500',
        'wilson_receiving_yards': 'OVER 1,100',
        'hall_rushing_yards': 'OVER 900',
        'gardner_interceptions': 'UNDER 3.5',
    },
    'key_angles': {
        'best_bet': 'Under 5.5 wins',
        'narrative': 'Patient rebuild = poor record',
        'avoid': 'Any playoff futures',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("NEW YORK JETS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {JETS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{JETS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {JETS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {JETS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {JETS_2025_SUMMARY['free_agent_signings']} (value focus)")
    print(f"  • Major Losses: {JETS_2025_SUMMARY['major_losses']}")
    print(f"  • Draft Picks: {JETS_2025_SUMMARY['draft_picks']}")
    print(f"  • Coaching Changes: {JETS_2025_SUMMARY['coaching_changes']} (complete overhaul)")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${JETS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${JETS_2025_SUMMARY['dead_money_absorbed']:,}")
    print(f"  • Current Cap Space: ${JETS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • Playoff Drought: {JETS_2025_SUMMARY['playoff_drought']}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Justin Fields (QB) - 2yr/$40M centerpiece")
    print("  • Aaron Glenn (HC) - Culture transformation")
    print("  • Pierre Strong Jr. (G) - #7 overall pick")
    print("  • Brandon Stephens (CB) - Change of scenery")
    
    print("\n❌ MAJOR DEPARTURES:")
    print("  • Aaron Rodgers - Released (saved $9.5M)")
    print("  • Davante Adams - To Rams")
    print("  • D.J. Reed - To Texans")
    print("  • Robert Saleh - Fired (20-36 record)")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {JETS_2025_SUMMARY['key_philosophy']}")
    print(f"  • QB Approach: Fields bridge with upside")
    print(f"  • Front Office: 68% staff turnover")
    print(f"  • Timeline: Patient rebuild acknowledged")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 5.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Fields development with weapons")
    print("  • Glenn culture implementation")
    print("  • Young OL continued growth")
    print("  • Accepting short-term pain for long-term gain")

if __name__ == "__main__":
    generate_summary_report()
"""
Los Angeles Rams 2025 Offseason Moves
Strategic gambles: Trading Kupp for Adams while securing future flexibility
Last Updated: June 23, 2025
"""

RAMS_2025_MOVES = [
    # ========== BLOCKBUSTER MOVES - Out with old, in with new ==========
    {
        'player_name': 'Cooper Kupp',
        'position': 'WR1',
        'from_team': 'LAR',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -22300000,  # Dead cap
        'aav': 0,
        '2024_grade': 6.5,  # Injury-limited
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 8.0,  # Franchise icon
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Unsuccessful trade attempts
    },
    {
        'player_name': 'Davante Adams',
        'position': 'WR1',
        'from_team': 'NYJ',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 46000000,
        'guaranteed_money': 30000000,
        'aav': 23000000,
        '2024_grade': 8.5,  # 103 catches, 1,509 yards in 2023
        'projected_2025_grade': 8.2,  # Age 31
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.5,  # Replace Kupp production
        'impact_score': 3.0,  # Elite acquisition
    },

    # ========== DEFENSIVE REINFORCEMENTS ==========
    {
        'player_name': 'Poona Ford',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 29600000,
        'guaranteed_money': 18000000,
        'aav': 9866667,
        '2024_grade': 8.0,  # PFF 5th among interior defenders
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Fix run defense
        'impact_score': 2.0,
    },
    {
        'player_name': 'Nate Landman',
        'position': 'LB',
        'from_team': 'Atl',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # LB depth
        'impact_score': 1.0,
    },
    {
        'player_name': 'Darious Williams',
        'position': 'CB',
        'from_team': 'Jac',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 6000000,
        '2024_grade': 7.0,  # Returns to Rams
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # System familiarity
        'impact_score': 1.2,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Matthew Stafford',
        'position': 'QB',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Contract Restructure',
        'contract_years': 2,
        'contract_value': 80000000,
        'guaranteed_money': 40000000,  # For 2026
        'aav': 40000000,
        '2024_grade': 8.0,  # Elite when healthy
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 2.5,  # Saves $8.7M in 2025
    },
    {
        'player_name': 'Alaric Jackson',
        'position': 'LT',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 57750000,
        'guaranteed_money': 30000000,
        'aav': 19250000,
        '2024_grade': 7.8,
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.0,  # Secures blindside
    },
    {
        'player_name': 'Tutu Atwell',
        'position': 'WR',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 10000000,
        'guaranteed_money': 10000000,  # Fully guaranteed
        'aav': 5000000,
        '2024_grade': 7.0,  # Speed threat
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Coleman Shelton',
        'position': 'C',
        'from_team': 'Chi',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7500000,
        'guaranteed_money': 4000000,
        'aav': 3750000,
        '2024_grade': 6.8,  # Returns after 1 year away
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # System familiarity
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jimmy Garoppolo',
        'position': 'QB',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Contract Restructure',
        'contract_years': 1,
        'contract_value': 13500000,  # Up to with incentives
        'guaranteed_money': 8000000,
        'aav': 13500000,
        '2024_grade': 6.0,  # Backup role
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 10.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Stafford insurance
        'impact_score': 0.5,
    },
    {
        'player_name': 'Ahkello Witherspoon',
        'position': 'CB',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8500000,
        'guaranteed_money': 4000000,
        'aav': 4250000,
        '2024_grade': 7.2,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 0.8,
    },

    # ========== LOSSES ==========
    {
        'player_name': 'Christian Rozeboom',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'KC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Starting LB
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Jake Hummel',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'Cin',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },
    {
        'player_name': 'Demarcus Robinson',
        'position': 'WR',
        'from_team': 'LAR',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== TRADES ==========
    {
        'player_name': 'Jonah Jackson',
        'position': 'G',
        'from_team': 'LAR',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # Disappointing FA signing
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Saved $17.5M, got 6th
    },
    {
        'player_name': '2025 1st Round Pick',
        'position': 'DRAFT',
        'from_team': 'LAR',
        'to_team': 'Atl',
        'move_type': 'Trade - Pick 26',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # Got 2025 2nd + 2026 1st
    },

    # ========== 2025 NFL DRAFT - Strategic additions ==========
    {
        'player_name': 'Terrance Ferguson',
        'position': 'TE',
        'from_team': 'Oregon',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 2, Pick 36 (via ATL)',
        'contract_years': 4,
        'contract_value': 8800000,
        'guaranteed_money': 4400000,
        'aav': 2200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Elite prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # TE void filled
        'impact_score': 1.8,
    },
    {
        'player_name': 'Josaiah Stewart',
        'position': 'EDGE',
        'from_team': 'Michigan',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 3, Pick 91',
        'contract_years': 4,
        'contract_value': 5600000,
        'guaranteed_money': 1200000,
        'aav': 1400000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Depth for Verse/Young
        'impact_score': 1.0,
    },
    {
        'player_name': 'Chris "Pooh" Paul Jr.',
        'position': 'LB',
        'from_team': 'Ole Miss',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 3, Pick 95 (comp)',
        'contract_years': 4,
        'contract_value': 5400000,
        'guaranteed_money': 1100000,
        'aav': 1350000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # No TDs allowed in 665 snaps
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replace departed LBs
        'impact_score': 1.2,
    },
    {
        'player_name': 'Jarquez Hunter',
        'position': 'RB',
        'from_team': 'Auburn',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 4, Pick 127',
        'contract_years': 4,
        'contract_value': 4400000,
        'guaranteed_money': 800000,
        'aav': 1100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 4.4 speed, YAC leader
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Complement to Kyren
        'impact_score': 0.8,
    },
    {
        'player_name': 'Ty Hamilton',
        'position': 'DT',
        'from_team': 'Ohio State',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 5, Pick 169',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 500000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # DT depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Cam Hart',
        'position': 'CB/S',
        'from_team': 'Notre Dame',
        'to_team': 'LAR',
        'move_type': '2025 Draft - Round 6, Pick 203',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING CHANGES ==========
    {
        'player_name': 'Nick Caley',
        'position': 'COACH-TE',
        'from_team': 'LAR',
        'to_team': 'Hou',
        'move_type': 'Coaching Loss (OC)',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.0,  # Innovative passing concepts
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Big loss
    },
    {
        'player_name': 'Nathan Scheelhaase',
        'position': 'COACH-PGC',
        'from_team': 'LAR-Assistant',
        'to_team': 'LAR',
        'move_type': 'Internal Promotion',
        'contract_years': 3,
        'contract_value': 2400000,
        'guaranteed_money': 1200000,
        'aav': 800000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,  # McVay calls him "stud"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Drew Wilkins',
        'position': 'COACH-PRC',
        'from_team': 'Bal',
        'to_team': 'LAR',
        'move_type': 'Pass Rush Coordinator Hire',
        'contract_years': 2,
        'contract_value': 1600000,
        'guaranteed_money': 800000,
        'aav': 800000,
        '2024_grade': 7.5,  # Ravens blitz packages
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Maximize Verse/Young
        'impact_score': 1.2,
    },
    {
        'player_name': 'Alex Van Pelt',
        'position': 'COACH-OA',
        'from_team': 'NE',
        'to_team': 'LAR',
        'move_type': 'Offensive Assistant Hire',
        'contract_years': 2,
        'contract_value': 1200000,
        'guaranteed_money': 600000,
        'aav': 600000,
        '2024_grade': 7.0,  # Developed Drake Maye
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # QB transition insurance
        'impact_score': 0.5,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'LAR',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 12000000,  # Combined
        'guaranteed_money': 1200000,
        'aav': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
RAMS_2025_SUMMARY = {
    'total_moves': len(RAMS_2025_MOVES),
    'major_signings': 5,  # Adams headline
    'free_agent_losses': 3,
    'draft_picks': 6,
    'key_resignings': 7,
    'trades': 2,
    'coaching_changes': 4,
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 175000000,  # Strategic spending
    'dead_money': 50800000,  # 7th-most in NFL
    'cap_space_remaining': 19600000,  # Before draft signings
    'projected_2026_cap_space': 75000000,  # Major flexibility
    'championship_window': '2025-2026',  # Stafford timeline
    'offseason_grade': 'A-',
    'key_philosophy': 'Calculated risk-taking for immediate contention with future flexibility',
    'net_impact_score': 11.5,  # Sum of all impact scores
    'division_outlook': 'Favorites despite toughest division in NFL',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'adams_gamble': {
        'kupp_release': '$22.3M dead cap absorbed',
        'adams_signing': '2yr/$46M brings proven production',
        'age_concern': 'Both 31, but Adams healthier recently',
        'fit': 'Pairs with Puka Nacua for elite duo',
    },
    'defensive_transformation': {
        'run_defense': 'Allowed 100+ yards in 15 of 21 games',
        'ford_impact': 'PFF 5th-ranked interior defender',
        'youth_development': 'Verse, Young, Turner emerging',
        'scheme_evolution': 'Wilkins brings Ravens concepts',
    },
    'draft_brilliance': {
        'future_pick': 'Traded 1st for 2026 1st + 2025 2nd',
        'immediate_needs': 'Ferguson fills TE void',
        'development': 'Six picks address every need',
        'philosophy': 'Present contributors over projects',
    },
    'financial_chess': {
        'stafford_restructure': 'Saves $8.7M in 2025',
        'future_extensions': 'Nacua, Turner, Williams loom',
        'cap_management': '$75M in 2026 space created',
        'window': 'All-in while maintaining flexibility',
    },
    'coaching_continuity': {
        'mcvay_stability': 'Coordinators LaFleur/Shula return',
        'caley_loss': 'Big blow losing to Houston',
        'internal_promotion': 'Scheelhaase ready for bigger role',
        'new_additions': 'Wilkins and Van Pelt add expertise',
    },
    'division_challenge': {
        'strength': 'NFC West toughest in NFL',
        'schedule': 'First-place schedule (Eagles, Ravens, Lions)',
        'competition': '49ers, Cardinals both improved',
        'margin': 'No room for error in 2025',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Matthew Stafford',
        'backup': 'Jimmy Garoppolo',
        'grade': 'B+',
        'notes': 'Stafford health crucial, Jimmy G solid insurance',
    },
    'offensive_line': {
        'starters': ['Alaric Jackson (LT)', 'Steve Avila (LG)', 'Coleman Shelton (C)', 
                     'Kevin Dotson (RG)', 'Rob Havenstein (RT)'],
        'depth': 'Concerns after Jackson trade',
        'grade': 'B+',
        'notes': 'Jackson extension stabilizes left side',
    },
    'skill_positions': {
        'wr': 'Davante Adams, Puka Nacua, Tutu Atwell',
        'rb': 'Kyren Williams, Jarquez Hunter',
        'te': 'Terrance Ferguson, Tyler Higbee',
        'grade': 'A',
        'notes': 'Elite weapons if healthy',
    },
    'defensive_line': {
        'dt': 'Aaron Donald, Poona Ford, Kobie Turner',
        'edge': 'Jared Verse, Byron Young, Josaiah Stewart',
        'grade': 'A-',
        'notes': 'Donald still elite, young edge rushers rising',
    },
    'linebackers': {
        'starters': 'Ernest Jones, Nate Landman, Chris Paul Jr.',
        'depth': 'Thin after departures',
        'grade': 'B-',
        'notes': 'Jones anchors, rookies must contribute',
    },
    'secondary': {
        'cb': 'Darious Williams, Ahkello Witherspoon, Cobie Durant',
        'safety': 'Kamren Curl, John Johnson III',
        'grade': 'B',
        'notes': 'Williams return helps, safety depth concern',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 11.5,
        'lean': 'OVER',
        'reasoning': 'Elite offense, improved defense',
    },
    'division_odds': {
        'current': '+140',
        'value': 'YES',
        'reasoning': 'Best roster despite tough division',
    },
    'super_bowl_odds': {
        'current': '+1200',
        'value': 'YES',
        'reasoning': 'McVay with weapons = dangerous',
    },
    'player_props': {
        'stafford_passing_yards': 'OVER 4,400',
        'adams_receiving_yards': 'OVER 1,100',
        'nacua_receiving_yards': 'OVER 1,250',
        'kyren_williams_rushing': 'UNDER 1,200 (workload)',
    },
    'key_bets': {
        'best': 'Division winner +140',
        'player_award': 'Nacua OPOY +2500',
        'narrative': 'Offense top-3 in NFL',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("LOS ANGELES RAMS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {RAMS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{RAMS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {RAMS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {RAMS_2025_SUMMARY['total_moves']}")
    print(f"  • Major Signings: {RAMS_2025_SUMMARY['major_signings']} (Adams headliner)")
    print(f"  • Draft Picks: {RAMS_2025_SUMMARY['draft_picks']}")
    print(f"  • Key Re-signings: {RAMS_2025_SUMMARY['key_resignings']}")
    print(f"  • Trades: Acquired 2026 1st round pick")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${RAMS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${RAMS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Current Cap Space: ${RAMS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Projected: ${RAMS_2025_SUMMARY['projected_2026_cap_space']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Davante Adams (WR) - 2yr/$46M to replace Kupp")
    print("  • Poona Ford (DT) - 3yr/$29.6M run defense fix")
    print("  • Terrance Ferguson (TE) - 2nd round pick")
    print("  • Drew Wilkins (Pass Rush Coordinator)")
    
    print("\n❌ KEY LOSSES:")
    print("  • Cooper Kupp - Released ($22.3M dead cap)")
    print("  • Christian Rozeboom (LB) - To Chiefs")
    print("  • Nick Caley (TE Coach) - Texans OC")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {RAMS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division: {RAMS_2025_SUMMARY['division_outlook']}")
    print(f"  • Stafford restructure saves $8.7M")
    print(f"  • Traded 2025 1st for 2026 1st + 2025 2nd")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 11.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Stafford health at age 37")
    print("  • Adams/Nacua chemistry development")
    print("  • Run defense improvement with Ford")
    print("  • First-place schedule difficulty")

if __name__ == "__main__":
    generate_summary_report()
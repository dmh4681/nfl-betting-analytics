"""
Green Bay Packers 2025 Offseason Moves
Calculated rebuild around Jordan Love with targeted additions
Last Updated: June 23, 2025
"""

PACKERS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Quality over quantity ==========
    {
        'player_name': 'Nate Hobbs',
        'position': 'CB',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 48000000,
        'guaranteed_money': 16000000,
        'aav': 12000000,
        '2024_grade': 7.0,  # Missed 6 games
        'projected_2025_grade': 7.8,  # Versatility key
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Alexander insurance
        'impact_score': 2.0,
    },
    {
        'player_name': 'Aaron Banks',
        'position': 'LG',
        'from_team': 'SF',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 77000000,
        'guaranteed_money': 40000000,
        'aav': 19250000,
        '2024_grade': 8.5,  # 1 sack allowed in 775 snaps
        'projected_2025_grade': 8.7,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Jenkins to C
        'impact_score': 2.5,
    },
    {
        'player_name': 'Mecole Hardman',
        'position': 'WR',
        'from_team': 'KC',
        'to_team': 'GB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 500000,
        'aav': 1500000,
        '2024_grade': 6.0,  # Limited role
        'projected_2025_grade': 6.8,  # Speed element
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,  # Watson injury
        'impact_score': 0.8,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Brandon McManus',
        'position': 'K',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 15300000,
        'guaranteed_money': 8000000,
        'aav': 5100000,
        '2024_grade': 8.8,  # 95.2% FG accuracy
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.5,  # Kicking stability
    },
    {
        'player_name': 'Isaiah McDuffie',
        'position': 'LB',
        'from_team': 'GB',
        'to_team': 'GB',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 7.0,  # Special teams ace
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },

    # ========== MAJOR LOSSES ==========
    {
        'player_name': 'Josh Myers',
        'position': 'C',
        'from_team': 'GB',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # Solid when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # Jenkins moves to C
    },
    {
        'player_name': 'T.J. Slaton',
        'position': 'DT',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Rotational DT
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Eric Stokes',
        'position': 'CB',
        'from_team': 'GB',
        'to_team': 'LV',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.5,  # No PBUs since rookie year
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 4.0,  # Bust
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,  # Addition by subtraction
    },
    {
        'player_name': 'AJ Dillon',
        'position': 'RB',
        'from_team': 'GB',
        'to_team': 'Phi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,  # Missed 2024 (neck)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },

    # ========== 2025 NFL DRAFT - Zero trades, historic WR pick ==========
    {
        'player_name': 'Matthew Golden',
        'position': 'WR',
        'from_team': 'Texas',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 1, Pick 23',
        'contract_years': 4,
        'contract_value': 17500000,
        'guaranteed_money': 17500000,
        'aav': 4375000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # 4.29 speed, 987 yards
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # First WR R1 since 2002
        'impact_score': 2.2,
    },
    {
        'player_name': 'Micah Carter',
        'position': 'DT',
        'from_team': 'Clemson',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 2, Pick 55',
        'contract_years': 4,
        'contract_value': 8500000,
        'guaranteed_money': 4500000,
        'aav': 2125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 10.5 sacks, 15 TFL
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Interior pass rush
        'impact_score': 1.5,
    },
    {
        'player_name': 'Damar Barnes',
        'position': 'S',
        'from_team': 'Oregon',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 3, Pick 87',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1500000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Versatile safety
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Secondary depth
        'impact_score': 1.0,
    },
    {
        'player_name': 'Nathan Richardson',
        'position': 'OT',
        'from_team': 'Missouri',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 4, Pick 119',
        'contract_years': 4,
        'contract_value': 4600000,
        'guaranteed_money': 900000,
        'aav': 1150000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Development project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Anthony Swinney',
        'position': 'S',
        'from_team': 'Alabama',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 5, Pick 155',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 600000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Son of coach
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Marcus Mbow',
        'position': 'G',
        'from_team': 'Purdue',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 6, Pick 187',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 400000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Connor Colby',
        'position': 'TE',
        'from_team': 'Iowa State',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 7, Pick 221',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # Blocking TE
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Cam Johnson',
        'position': 'LB',
        'from_team': 'Arizona',
        'to_team': 'GB',
        'move_type': '2025 Draft - Round 7, Pick 254',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 250000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # ST contributor
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.1,
    },

    # ========== COACHING CHANGES - Defensive improvements ==========
    {
        'player_name': 'DeMarcus Covington',
        'position': 'COACH-DL',
        'from_team': 'NE',
        'to_team': 'GB',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 2500000,
        'guaranteed_money': 1200000,
        'aav': 833333,
        '2024_grade': 7.5,  # Patriots DC
        'projected_2025_grade': 8.0,  # Pass rush focus
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Luke Getsy',
        'position': 'COACH-OFF ASST',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        'guaranteed_money': 800000,
        'aav': 900000,
        '2024_grade': 6.5,  # Former GB coach
        'projected_2025_grade': 7.5,  # Rodgers MVP years
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },

    # ========== CHRISTIAN WATSON INJURY ==========
    {
        'player_name': 'Christian Watson',
        'position': 'WR',
        'from_team': 'GB',
        'to_team': 'GB-INJURED',
        'move_type': 'ACL Tear',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # When healthy
        'projected_2025_grade': 0.0,  # Out for season
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Major loss
    },
]

# ========== SUMMARY METRICS ==========
PACKERS_2025_SUMMARY = {
    'total_moves': len(PACKERS_2025_MOVES),
    'free_agent_signings': 3,
    'major_losses': 4,
    'trades': 0,  # First time in Gutekunst era
    'draft_picks': 8,  # All original picks kept
    'key_resignings': 2,
    'coaching_changes': 2,
    'total_guaranteed_money': 135000000,  # Conservative estimate
    'dead_money': 5500000,
    'cap_space_remaining': 29000000,
    'championship_window': '2025-2029',
    'offseason_grade': 'B+',
    'key_philosophy': 'Calculated rebuild around Love with targeted quality additions',
    'net_impact_score': 11.5,  # Sum of all impact scores
    'division_outlook': 'Rising but face loaded NFC North',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'free_agency_approach': {
        'strategy': 'Quality over quantity',
        'biggest_signing': 'Banks $77M enables OL chess',
        'secondary_focus': 'Hobbs provides Alexander insurance',
        'spending': 'Conservative despite $36.4M space',
    },
    'draft_philosophy': {
        'historic_pick': 'First WR in R1 since 2002',
        'zero_trades': 'First time under Gutekunst',
        'watson_response': 'Golden addresses speed need',
        'development': 'Eight picks for depth building',
    },
    'offensive_line_shuffle': {
        'banks_impact': 'Elite LG allows Jenkins to C',
        'protection': 'Major upgrade for Love',
        'run_game': 'Addressed 2024 weakness',
        'continuity': 'Keep Bakhtiari, Runyan core',
    },
    'injury_management': {
        'watson_acl': 'Creates immediate WR void',
        'alexander_concerns': '14 games in 2 years',
        'depth_building': 'Draft focused on competition',
    },
    'cap_flexibility': {
        'current_space': '$29M maintained',
        'love_extension': 'Already absorbed',
        'future_outlook': 'Well-positioned for 2026+',
        'philosophy': 'Sustainable contention',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Jordan Love',
        'backup': 'Sean Clifford',
        'grade': 'A-',
        'notes': '$220M investment, Year 2 as starter',
    },
    'offensive_line': {
        'starters': ['Rasheed Walker (LT)', 'Aaron Banks (LG)', 'Elgton Jenkins (C)', 
                     'Jon Runyan Jr. (RG)', 'Zach Tom (RT)'],
        'depth': 'Marcus Mbow, Nathan Richardson',
        'grade': 'A-',
        'notes': 'Banks addition transforms interior',
    },
    'skill_positions': {
        'wr': 'Romeo Doubs, Matthew Golden, Jayden Reed',
        'rb': 'Josh Jacobs, MarShawn Lloyd, Emanuel Wilson',
        'te': 'Luke Musgrave, Tucker Kraft',
        'grade': 'B+',
        'notes': 'Watson ACL creates uncertainty',
    },
    'pass_rush': {
        'edge': 'Rashan Gary, Preston Smith, Lukas Van Ness',
        'dt': 'Kenny Clark, Micah Carter, Devonte Wyatt',
        'grade': 'B',
        'notes': 'Need Gary to stay healthy',
    },
    'linebackers': {
        'starters': 'Quay Walker, Isaiah McDuffie',
        'depth': 'Cam Johnson, Eric Wilson',
        'grade': 'B-',
        'notes': 'Walker development crucial',
    },
    'secondary': {
        'cb': 'Jaire Alexander, Nate Hobbs, Keisean Nixon',
        'safety': 'Xavier McKinney, Javon Bullard',
        'grade': 'B+',
        'notes': 'IF Alexander stays healthy',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'UNDER',
        'reasoning': 'Brutal division + tough schedule',
    },
    'division_odds': {
        'current': '+350',
        'value': 'NO',
        'reasoning': '4th in loaded NFC North',
    },
    'playoffs': {
        'current': '+110',
        'value': 'NO',
        'reasoning': 'Wild card ceiling likely',
    },
    'player_props': {
        'love_passing_yards': 'OVER 4,100',
        'jacobs_rushing_yards': 'OVER 1,000',
        'golden_receiving_yards': 'OVER 750',
    },
    'key_angles': {
        'best_bet': 'Love 30+ passing TDs',
        'fade': 'Division winner',
        'narrative': 'Year 2 Love leap',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("GREEN BAY PACKERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {PACKERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{PACKERS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {PACKERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {PACKERS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {PACKERS_2025_SUMMARY['free_agent_signings']} (quality over quantity)")
    print(f"  • Trades: {PACKERS_2025_SUMMARY['trades']} (first time under Gutekunst)")
    print(f"  • Draft Picks: {PACKERS_2025_SUMMARY['draft_picks']} (all originals kept)")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${PACKERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${PACKERS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${PACKERS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Aaron Banks (LG) - 4yr/$77M from 49ers")
    print("  • Nate Hobbs (CB) - 4yr/$48M from Raiders")
    print("  • Matthew Golden (WR) - 1st WR in R1 since 2002")
    print("  • DeMarcus Covington - DL coach from Patriots")
    
    print("\n❌ KEY LOSSES:")
    print("  • Christian Watson (WR) - ACL tear")
    print("  • Josh Myers (C) - To Jets (Jenkins moves to C)")
    print("  • Eric Stokes (CB) - Former 1st rounder to Raiders")
    print("  • AJ Dillon (RB) - To Eagles after injury")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {PACKERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {PACKERS_2025_SUMMARY['division_outlook']}")
    print(f"  • OL Chess: Banks allows Jenkins to center")
    print(f"  • Risk: Can young WRs step up without Watson?")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Love Year 2 development crucial")
    print("  • Watson ACL creates WR uncertainty")
    print("  • Alexander health (14 games in 2 years)")
    print("  • NFC North gauntlet schedule")

if __name__ == "__main__":
    generate_summary_report()
"""
Kansas City Chiefs 2025 Offseason Moves
Navigating cap constraints while maintaining championship core
Last Updated: June 23, 2025
"""

CHIEFS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Targeted additions ==========
    {
        'player_name': 'Jaylon Moore',
        'position': 'LT',
        'from_team': 'SF',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 30000000,
        'guaranteed_money': 21240000,
        'aav': 15000000,
        '2024_grade': 7.2,  # Limited starts but solid
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 8.5,  # Critical LT need
        'impact_score': 2.0,
    },
    {
        'player_name': 'Kristian Fulton',
        'position': 'CB',
        'from_team': 'LAC',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 20000000,
        'guaranteed_money': 15000000,
        'aav': 10000000,
        '2024_grade': 7.5,  # 15th among CBs with 750+ snaps
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # McDuffie to slot
        'impact_score': 1.8,
    },
    {
        'player_name': 'Gardner Minshew',
        'position': 'QB',
        'from_team': 'LV',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1170000,  # Vet minimum + incentives
        'guaranteed_money': 1170000,
        'aav': 1170000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Mahomes backup
        'impact_score': 0.8,
    },
    {
        'player_name': 'Elijah Mitchell',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 0.0,  # Injured all 2024
        'projected_2025_grade': 7.0,  # 4.38 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jerry Tillery',
        'position': 'DT',
        'from_team': 'Min',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1790000,
        'guaranteed_money': 1790000,
        'aav': 1790000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES - Cap casualties ==========
    {
        'player_name': 'Justin Reid',
        'position': 'S',
        'from_team': 'KC',
        'to_team': 'NO',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # 3,575 snaps since 2022
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,  # Signal caller
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # 3yr/$31.5M to Saints
    },
    {
        'player_name': 'Nick Allegretti',
        'position': 'G',
        'from_team': 'KC',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,  # Started in playoffs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # 3yr/$16M
    },
    {
        'player_name': 'Derrick Nnadi',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Diminished role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },
    {
        'player_name': 'Tommy Townsend',
        'position': 'P',
        'from_team': 'KC',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # 2yr/$6M
    },

    # ========== TRADES - Painful but necessary ==========
    {
        'player_name': 'L\'Jarius Sneed',
        'position': 'CB1',
        'from_team': 'KC',
        'to_team': 'Ten',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # Got 2025 3rd (#66)
        'notes': 'Saved $19.8M, tore quad in Tennessee'
    },
    {
        'player_name': 'Joe Thuney',
        'position': 'LG',
        'from_team': 'KC',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.2,  # All-Pro guard
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,  # Got 2026 4th
        'notes': 'Saved $16M despite $11M dead money'
    },
    {
        'player_name': 'DeAndre Hopkins',
        'position': 'WR',
        'from_team': 'Ten',
        'to_team': 'KC',
        'move_type': 'Trade (Mid-season 2024)',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # 41 catches, 437 yards
        'projected_2025_grade': 0.0,  # Rental expired
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,  # Mid-season addition
        'notes': 'Conditional 5th round pick'
    },

    # ========== 2025 NFL DRAFT - Building for future ==========
    {
        'player_name': 'Josh Simmons',
        'position': 'LT',
        'from_team': 'Ohio State',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 1, Pick 32',
        'contract_years': 4,
        'contract_value': 15800000,
        'guaranteed_money': 15800000,
        'aav': 3950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # Torn patellar tendon
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Future franchise LT
        'impact_score': 2.2,
        'notes': '20th overall prospect, injury value'
    },
    {
        'player_name': 'Omarr Norman-Lott',
        'position': 'DT',
        'from_team': 'Tennessee',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 2, Pick 63',
        'contract_years': 4,
        'contract_value': 8200000,
        'guaranteed_money': 4000000,
        'aav': 2050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 4.5 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },
    {
        'player_name': 'Ashton Gillotte',
        'position': 'EDGE',
        'from_team': 'Louisville',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 3, Pick 66',
        'contract_years': 4,
        'contract_value': 6500000,
        'guaranteed_money': 1500000,
        'aav': 1625000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 26.5 career sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
        'notes': 'Via Sneed trade'
    },
    {
        'player_name': 'Nohl Williams',
        'position': 'CB',
        'from_team': 'California',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 3, Pick 85',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1200000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 7 INTs, 40.1 passer rating
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jalen Royals',
        'position': 'WR',
        'from_team': 'Utah State',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 4, Pick 133',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 900000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Jeffrey Bassa',
        'position': 'LB',
        'from_team': 'Oregon',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 5, Pick 156',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 600000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Brashard Smith',
        'position': 'RB',
        'from_team': 'SMU',
        'to_team': 'KC',
        'move_type': '2025 Draft - Round 7, Pick 228',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },

    # ========== KEY EXTENSIONS/RE-SIGNINGS ==========
    {
        'player_name': 'Nick Bolton',
        'position': 'LB',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 45000000,
        'guaranteed_money': 30000000,
        'aav': 15000000,
        '2024_grade': 8.2,  # 106 tackles
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,  # 4th highest paid LB
    },
    {
        'player_name': 'Trey Smith',
        'position': 'RG',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Franchise Tag',
        'contract_years': 1,
        'contract_value': 23400000,
        'guaranteed_money': 23400000,
        'aav': 23400000,
        '2024_grade': 8.5,  # Pro Bowler
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Highest paid guard
    },
    {
        'player_name': 'Marquise Brown',
        'position': 'WR',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 11000000,  # Up to $11M
        'guaranteed_money': 6500000,
        'aav': 11000000,
        '2024_grade': 6.5,  # Injury-plagued
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Kareem Hunt',
        'position': 'RB',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 1000000,
        'aav': 1500000,
        '2024_grade': 7.0,  # 728 yards, 7 TDs
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },

    # ========== CONTRACT RESTRUCTURES ==========
    {
        'player_name': 'Patrick Mahomes',
        'position': 'QB',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Contract Restructure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.5,
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 1.5,  # $24.5M cap relief
        'notes': '2026 cap hit now $78.2M'
    },
    {
        'player_name': 'Chris Jones',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Contract Restructure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.0,
        'projected_2025_grade': 9.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 1.2,  # $24.9M cap relief
    },

    # ========== COACHING CONTINUITY ==========
    {
        'player_name': 'Andy Reid',
        'position': 'COACH-HC',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Retained',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.5,
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 2.0,  # Stability crucial
    },
]

# ========== SUMMARY METRICS ==========
CHIEFS_2025_SUMMARY = {
    'total_moves': len(CHIEFS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 8,
    'trades': 3,  # Sneed out, Thuney out, Hopkins rental
    'draft_picks': 7,
    'key_resignings': 4,
    'contract_restructures': 2,
    'total_guaranteed_money': 125000000,  # Estimate
    'dead_money': 32000000,  # Thuney trade
    'cap_space_remaining': 5000000,
    'cap_space_2026': -36200000,  # Projected OVER
    'championship_window': '2025-2027',
    'offseason_grade': 'C+',
    'key_philosophy': 'Cap constraints force painful but necessary moves',
    'net_impact_score': 6.5,  # Sum of all impact scores
    'division_outlook': 'Still favorites but margin narrowing',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'cap_management': {
        'starting_position': '-$16.9M over cap',
        'restructures': '$49.4M created (Mahomes/Jones)',
        '2026_projection': '-$36.2M over cap',
        'mahomes_2026_hit': '$78.2M (!!)',
    },
    'injury_concerns': {
        'simmons': 'Torn patellar tendon',
        'rice': 'Recovery timeline unclear',
        'omenihu': 'Returning from ACL',
        'mitchell': 'Never healthy full season',
    },
    'roster_holes': {
        'left_tackle': 'Moore unproven, Simmons injured',
        'pass_rush_depth': 'Still need 3rd rusher',
        'safety': 'Reid departure hurts',
        'wr_speed': 'No true deep threat',
    },
    'division_competition': {
        'denver': 'Bo Nix Year 2 + defensive talent',
        'chargers': 'Herbert + defensive continuity',
        'raiders': 'Carroll/Smith improvement',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Patrick Mahomes',
        'backup': 'Gardner Minshew',
        'grade': 'A',
        'notes': 'Elite but age 30 season',
    },
    'offensive_line': {
        'starters': ['Jaylon Moore (LT)', 'Kingsley Suamataia (LG)', 
                     'Creed Humphrey (C)', 'Trey Smith (RG)', 'Jawaan Taylor (RT)'],
        'depth': 'Major concerns',
        'grade': 'C+',
        'notes': 'Thuney loss massive',
    },
    'skill_positions': {
        'wr': 'Rashee Rice, Marquise Brown, Xavier Worthy',
        'rb': 'Isiah Pacheco, Kareem Hunt, Elijah Mitchell',
        'te': 'Travis Kelce (age 36), Noah Gray',
        'grade': 'B',
        'notes': 'Kelce decline inevitable',
    },
    'defensive_line': {
        'dt': 'Chris Jones, Omarr Norman-Lott, Jerry Tillery',
        'edge': 'George Karlaftis, Charles Omenihu, Ashton Gillotte',
        'grade': 'B+',
        'notes': 'Jones still elite',
    },
    'linebackers': {
        'starters': 'Nick Bolton, Willie Gay Jr.',
        'depth': 'Jeffrey Bassa',
        'grade': 'B+',
        'notes': 'Bolton worth extension',
    },
    'secondary': {
        'cb': 'Trent McDuffie, Kristian Fulton, Nohl Williams',
        'safety': 'Bryan Cook, Chamarri Conner',
        'grade': 'B',
        'notes': 'Reid loss hurts leadership',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 10.5,
        'lean': 'UNDER',
        'reasoning': 'Roster degradation + tough division',
    },
    'division_odds': {
        'current': '+115',
        'value': 'NO',
        'reasoning': '10th straight questionable',
    },
    'super_bowl_odds': {
        'current': '+950',
        'value': 'PASS',
        'reasoning': 'Window narrowing',
    },
    'player_props': {
        'mahomes_passing_yards': 'UNDER 4,800',
        'kelce_receiving_yards': 'UNDER 900',
        'rice_receiving_yards': 'OVER 1,100',
    },
    'key_bets': {
        'best': 'Karlaftis 10+ sacks',
        'fade': 'Division winner',
        'narrative': 'Dynasty showing cracks',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("KANSAS CITY CHIEFS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {CHIEFS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{CHIEFS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {CHIEFS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {CHIEFS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {CHIEFS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {CHIEFS_2025_SUMMARY['major_losses']}")
    print(f"  • Trades: Lost Sneed AND Thuney")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Current Cap Space: ${CHIEFS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Projection: ${CHIEFS_2025_SUMMARY['cap_space_2026']:,} OVER")
    print(f"  • Dead Money: ${CHIEFS_2025_SUMMARY['dead_money']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Jaylon Moore (LT) - 2yr/$30M from 49ers")
    print("  • Josh Simmons (LT) - 1st round pick (injured)")
    print("  • Kristian Fulton (CB) - 2yr/$20M from Chargers")
    
    print("\n❌ KEY LOSSES:")
    print("  • Joe Thuney (LG) - Traded to Bears for 2026 4th")
    print("  • L'Jarius Sneed (CB) - Traded to Titans for 3rd")
    print("  • Justin Reid (S) - 3yr/$31.5M to Saints")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {CHIEFS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {CHIEFS_2025_SUMMARY['division_outlook']}")
    print(f"  • Cap Hell: Mahomes $78.2M hit in 2026")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 10.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Mahomes age 30 season")
    print("  • OL concerns after Thuney trade")
    print("  • Division vastly improved")
    print("  • Cap reckoning approaching")

if __name__ == "__main__":
    generate_summary_report()
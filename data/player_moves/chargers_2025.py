"""
Los Angeles Chargers 2025 Offseason Moves
Conservative approach maintaining defensive excellence
Last Updated: June 23, 2025
"""

CHARGERS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Value additions ==========
    {
        'player_name': 'Kendrick Bourne',
        'position': 'WR',
        'from_team': 'NE',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        'guaranteed_money': 7000000,
        'aav': 6000000,
        '2024_grade': 6.8,  # Limited by injury
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # WR depth
        'impact_score': 1.2,
    },
    {
        'player_name': 'Clelin Ferrell',
        'position': 'EDGE',
        'from_team': 'SF',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # Solid depth player
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replace Van Noy
        'impact_score': 1.0,
    },
    {
        'player_name': 'Quinton Bell',
        'position': 'LB',
        'from_team': 'Mia',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7500000,
        'guaranteed_money': 3500000,
        'aav': 3750000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Kingsley Jonathan',
        'position': 'DT',
        'from_team': 'Buf',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Depth
        'impact_score': 0.5,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS ==========
    {
        'player_name': 'Khalil Mack',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 38500000,
        'guaranteed_money': 25000000,
        'aav': 19250000,
        '2024_grade': 8.5,  # 6 sacks in 9 games
        'projected_2025_grade': 8.0,  # Age 34
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,
    },
    {
        'player_name': 'Mike Williams',
        'position': 'WR',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 6000000,
        'aav': 10000000,
        '2024_grade': 7.0,  # Post-ACL
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Matt Overton',
        'position': 'LS',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 2500000,
        'guaranteed_money': 1200000,
        'aav': 1250000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES ==========
    {
        'player_name': 'Kyle Van Noy',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 4.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # 2yr/$12M to Ravens
    },
    {
        'player_name': 'Poona Ford',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Interior anchor
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Kenneth Murray',
        'position': 'LB',
        'from_team': 'LAC',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== 2025 NFL DRAFT - Addressing needs ==========
    {
        'player_name': 'Jordan Morgan',
        'position': 'OT',
        'from_team': 'Arizona',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 1, Pick 5',
        'contract_years': 4,
        'contract_value': 38400000,
        'guaranteed_money': 38400000,
        'aav': 9600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Elite LT prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Slater insurance
        'impact_score': 2.5,
    },
    {
        'player_name': 'Deone Walker',
        'position': 'DT',
        'from_team': 'Kentucky',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 2, Pick 37',
        'contract_years': 4,
        'contract_value': 9800000,
        'guaranteed_money': 5500000,
        'aav': 2450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 347 lbs, 45 pressures
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Replace Ford
        'impact_score': 1.8,
    },
    {
        'player_name': 'Oronde Gadsden II',
        'position': 'WR',
        'from_team': 'Syracuse',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 2, Pick 42',
        'contract_years': 4,
        'contract_value': 9200000,
        'guaranteed_money': 5000000,
        'aav': 2300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 6'5" target
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
        'notes': 'Minicamp standout - 7 catches Day 2'
    },
    {
        'player_name': 'Princely Umanmielen',
        'position': 'EDGE',
        'from_team': 'Ole Miss',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 3, Pick 69',
        'contract_years': 4,
        'contract_value': 6900000,
        'guaranteed_money': 2000000,
        'aav': 1725000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 10.5 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Tyler Guyton',
        'position': 'C',
        'from_team': 'Oklahoma',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 4, Pick 105',
        'contract_years': 4,
        'contract_value': 5400000,
        'guaranteed_money': 1100000,
        'aav': 1350000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Center competition
        'impact_score': 0.8,
    },
    {
        'player_name': 'JD Duplain',
        'position': 'S',
        'from_team': 'Washington State',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 5, Pick 137',
        'contract_years': 4,
        'contract_value': 4400000,
        'guaranteed_money': 700000,
        'aav': 1100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.4,
    },
    {
        'player_name': 'Joe Milton III',
        'position': 'TE',
        'from_team': 'Tennessee',
        'to_team': 'LAC',
        'move_type': '2025 Draft - Round 6, Pick 178',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 500000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING CONTINUITY ==========
    {
        'player_name': 'Jim Harbaugh',
        'position': 'COACH-HC',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Retained',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,  # 11-6, playoffs
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.0,
    },
    {
        'player_name': 'Joe Hortiz',
        'position': 'GM',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Retained',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.0,  # Ravens pedigree
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.5,
    },

    # ========== CONTRACT NEGOTIATIONS ==========
    {
        'player_name': 'Rashawn Slater',
        'position': 'LT',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension Pending',
        'contract_years': 0,
        'contract_value': 0,  # Seeking $30M+ AAV
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.0,  # Elite LT
        'projected_2025_grade': 9.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 0.0,  # Pending
        'notes': 'Skipped OTAs, attended minicamp'
    },
]

# ========== SUMMARY METRICS ==========
CHARGERS_2025_SUMMARY = {
    'total_moves': len(CHARGERS_2025_MOVES),
    'free_agent_signings': 4,
    'major_losses': 3,
    'trades': 0,
    'draft_picks': 7,
    'key_resignings': 3,
    'coaching_continuity': 2,
    'total_guaranteed_money': 75000000,  # Conservative spending
    'dead_money': 8000000,
    'cap_space_remaining': 45000000,  # Significant flexibility
    'cap_space_2026': 110800000,  # Future flexibility
    'championship_window': '2025-2028',
    'offseason_grade': 'B-',
    'key_philosophy': 'Conservative approach maintaining defensive excellence',
    'net_impact_score': 12.5,  # Sum of all impact scores
    'division_outlook': 'Chiefs primary challenger but gap remains',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'conservative_approach': {
        'total_spent': '$35M guaranteed',
        'philosophy': 'Baltimore model via Hortiz',
        'draft_focus': 'Build through draft',
        'analytics': 'Cover blind spots approach',
    },
    'defensive_excellence': {
        '2024_rank': '#1 scoring defense',
        'returning_starters': '9 of 11',
        'pass_rush': 'Mack/Bosa elite duo',
        'secondary': 'Deep and talented',
    },
    'offensive_concerns': {
        'herbert_protection': 'Ankle issues drove OL focus',
        'wr_depth': 'Beyond McConkey questionable',
        'interior_ol': 'Center competition ongoing',
        'red_zone': 'Must improve from 2024',
    },
    'slater_situation': {
        'current_deal': '5th year option $19M',
        'seeking': '$30M+ AAV',
        'leverage': 'Elite LT scarcity',
        'resolution': 'Expected before camp',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Justin Herbert',
        'backup': 'Easton Stick',
        'grade': 'A',
        'notes': 'Elite QB if healthy',
    },
    'offensive_line': {
        'starters': ['Rashawn Slater (LT)', 'Jamaree Salyer (LG)', 
                     'Zion Johnson/Bradley Bozeman (C)', 'Trey Pipkins III (RG)', 
                     'Joe Alt (RT)'],
        'depth': 'Jordan Morgan adds insurance',
        'grade': 'B+',
        'notes': 'Alt All-Pro potential at RT',
    },
    'skill_positions': {
        'wr': 'Ladd McConkey, Mike Williams, Quentin Johnston',
        'rb': 'J.K. Dobbins, Gus Edwards',
        'te': 'Will Dissly, Donald Parham Jr.',
        'grade': 'B',
        'notes': 'McConkey emerging star',
    },
    'defensive_line': {
        'dt': 'Derwin James (hybrid), Deone Walker, Morgan Fox',
        'edge': 'Khalil Mack, Joey Bosa, Clelin Ferrell',
        'grade': 'A-',
        'notes': 'Interior DL needs work',
    },
    'linebackers': {
        'starters': 'Daiyan Henley, Denzel Perryman',
        'depth': 'Quinton Bell, Nick Niemann',
        'grade': 'B',
        'notes': 'Henley development key',
    },
    'secondary': {
        'cb': 'Asante Samuel Jr., Kristjan Fulton, J.C. Jackson',
        'safety': 'Derwin James, Alohi Gilman',
        'grade': 'A',
        'notes': 'Elite when healthy',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 10.5,
        'lean': 'OVER',
        'reasoning': 'Elite defense + easier schedule',
    },
    'division_odds': {
        'current': '+275',
        'value': 'SLIGHT VALUE',
        'reasoning': 'Chiefs vulnerable',
    },
    'playoffs': {
        'current': '-220',
        'value': 'YES',
        'reasoning': 'Lock for wild card minimum',
    },
    'player_props': {
        'herbert_passing_yards': 'OVER 4,300',
        'mack_sacks': 'OVER 8.5',
        'mcconkey_receiving_yards': 'OVER 1,000',
    },
    'key_bets': {
        'best': 'Make playoffs -220',
        'sleeper': 'Defense fewest points allowed',
        'narrative': 'Window opening wider',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("LOS ANGELES CHARGERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {CHARGERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{CHARGERS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {CHARGERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {CHARGERS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {CHARGERS_2025_SUMMARY['free_agent_signings']} (minimal)")
    print(f"  • Draft Picks: {CHARGERS_2025_SUMMARY['draft_picks']}")
    print(f"  • Cap Space Remaining: ${CHARGERS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${CHARGERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${CHARGERS_2025_SUMMARY['dead_money']:,}")
    print(f"  • 2026 Cap Space: ${CHARGERS_2025_SUMMARY['cap_space_2026']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Jordan Morgan (OT) - 1st round pick #5")
    print("  • Deone Walker (DT) - 2nd round, 347 lbs")
    print("  • Oronde Gadsden II (WR) - Minicamp standout")
    print("  • Khalil Mack - 2yr/$38.5M extension")
    
    print("\n❌ KEY LOSSES:")
    print("  • Poona Ford (DT) - Interior anchor to Panthers")
    print("  • Kyle Van Noy (EDGE) - 2yr/$12M to Ravens")
    print("  • Kenneth Murray (LB) - To Titans")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {CHARGERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {CHARGERS_2025_SUMMARY['division_outlook']}")
    print(f"  • Defensive rank: #1 scoring defense retained")
    print(f"  • Cap flexibility: Maintained for future")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 10.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Herbert health paramount")
    print("  • Slater extension looming")
    print("  • Interior DL depth concerns")
    print("  • Conservative approach vs aggressive division")

if __name__ == "__main__":
    generate_summary_report()
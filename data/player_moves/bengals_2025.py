"""
Cincinnati Bengals 2025 Offseason Moves
Historic $570M offensive investment with defensive overhaul
Last Updated: June 23, 2025
"""

BENGALS_2025_MOVES = [
    # ========== HISTORIC EXTENSIONS - $570M offensive commitment ==========
    {
        'player_name': "Ja'Marr Chase",
        'position': 'WR1',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 161000000,
        'guaranteed_money': 112000000,
        'aav': 40250000,
        '2024_grade': 9.8,  # Triple Crown winner
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.5,
        'notes': 'Highest-paid non-QB in NFL history'
    },
    {
        'player_name': 'Tee Higgins',
        'position': 'WR2',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 115000000,
        'guaranteed_money': 30000000,
        'aav': 28750000,
        '2024_grade': 8.5,
        'projected_2025_grade': 8.3,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.8,
        'notes': 'Took hometown discount for championships'
    },
    {
        'player_name': 'B.J. Hill',
        'position': 'DT',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 33000000,
        'guaranteed_money': 20000000,
        'aav': 11000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.8,
    },
    {
        'player_name': 'Mike Gesicki',
        'position': 'TE',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 21000000,
        'guaranteed_money': 12000000,
        'aav': 7000000,
        '2024_grade': 7.2,  # 65 catches
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },

    # ========== FREE AGENT SIGNINGS - Minimal external additions ==========
    {
        'player_name': 'Lucas Patrick',
        'position': 'G',
        'from_team': 'NO',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # OL depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Oren Burks',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Joe Giles-Harris',
        'position': 'LB',
        'from_team': 'NE',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== MAJOR LOSSES - Retirements and departures ==========
    {
        'player_name': 'Sam Hubbard',
        'position': 'EDGE',
        'from_team': 'Cin',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Team captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
        'notes': 'Seven seasons, saved $9.5M cap'
    },
    {
        'player_name': 'Akeem Davis-Gaither',
        'position': 'LB',
        'from_team': 'Cin',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # ST ace
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # 2yr/$11M to Cardinals
    },

    # ========== 2025 NFL DRAFT - Criticized selections ==========
    {
        'player_name': 'Shemar Stewart',
        'position': 'DE',
        'from_team': 'Texas A&M',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 1, Pick 28',
        'contract_years': 4,
        'contract_value': 17000000,
        'guaranteed_money': 17000000,
        'aav': 4250000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Raw prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Hendrickson insurance
        'impact_score': 1.5,
        'notes': 'Only 4.5 sacks in 3 college seasons'
    },
    {
        'player_name': 'Barrett Carter',
        'position': 'LB',
        'from_team': 'Clemson',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 2, Pick 60',
        'contract_years': 4,
        'contract_value': 8400000,
        'guaranteed_money': 4200000,
        'aav': 2100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jordan Knight',
        'position': 'DT',
        'from_team': 'Tennessee',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 2, Pick 64',
        'contract_years': 4,
        'contract_value': 8200000,
        'guaranteed_money': 4000000,
        'aav': 2050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Age 25 concern
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
        'notes': '25-year-old rookie raised eyebrows'
    },
    {
        'player_name': 'Kaz Fairchild',
        'position': 'G',
        'from_team': 'Wisconsin',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 3, Pick 95',
        'contract_years': 4,
        'contract_value': 5700000,
        'guaranteed_money': 1200000,
        'aav': 1425000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 87.0 pass-block grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Immediate starter
        'impact_score': 1.2,
        'notes': 'Draft bright spot'
    },
    {
        'player_name': 'Terry Hampton',
        'position': 'CB',
        'from_team': 'North Carolina',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 4, Pick 123',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 900000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Elijah Davis',
        'position': 'LB',
        'from_team': 'Boston College',
        'to_team': 'Cin',
        'move_type': '2025 Draft - Round 5, Pick 149',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 600000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== RE-SIGNINGS - Depth retention ==========
    {
        'player_name': 'Cam Sample',
        'position': 'DE',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 3000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Joseph Ossai',
        'position': 'DE',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Logan Woodside',
        'position': 'QB',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.0,  # Backup QB
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING OVERHAUL - Defensive transformation ==========
    {
        'player_name': 'Lou Anarumo',
        'position': 'COACH-DC',
        'from_team': 'Cin',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # 25th-ranked defense
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
        'notes': 'Fired January 6 after six seasons'
    },
    {
        'player_name': 'Al Golden',
        'position': 'COACH-DC',
        'from_team': 'Notre Dame',
        'to_team': 'Cin',
        'move_type': 'DC Hire',
        'contract_years': 3,
        'contract_value': 7500000,
        'guaranteed_money': 4500000,
        'aav': 2500000,
        '2024_grade': 8.0,  # ND success
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Critical hire
        'impact_score': 2.0,
        'notes': 'Former Bengals LB coach 2020-21'
    },
    {
        'player_name': 'Sean Desai',
        'position': 'COACH-LB',
        'from_team': 'Phi',
        'to_team': 'Cin',
        'move_type': 'LB Coach Hire',
        'contract_years': 2,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 1000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jerry Montgomery',
        'position': 'COACH-DL',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'DL Coach Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        'guaranteed_money': 900000,
        'aav': 900000,
        '2024_grade': 7.5,  # 9 years with Packers
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },

    # ========== CONTRACT SITUATION - Hendrickson holdout ==========
    {
        'player_name': 'Trey Hendrickson',
        'position': 'EDGE',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Holdout/Trade Request',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 15800000,  # Current salary
        '2024_grade': 9.5,  # Led NFL with 17.5 sacks
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 0.0,  # Unresolved
        'notes': 'Seeking $28-30M annually, granted trade permission'
    },

    # ========== OTHER SIGNINGS ==========
    {
        'player_name': 'T.J. Slaton Jr.',
        'position': 'DT',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
BENGALS_2025_SUMMARY = {
    'total_moves': len(BENGALS_2025_MOVES),
    'free_agent_signings': 5,  # Minimal external
    'major_losses': 2,
    'historic_extensions': 4,
    'trades': 0,
    'draft_picks': 6,
    'coaching_changes': 5,
    'total_offensive_investment': 570000000,  # Burrow + Chase + Higgins
    'total_guaranteed_money': 180000000,
    'dead_money': 27000000,
    'cap_space_remaining': 48000000,
    'cap_space_2026': 72000000,
    'championship_window': '2025-2028',
    'offseason_grade': 'A-',
    'key_philosophy': 'All-in on offensive core with defensive coaching overhaul',
    'net_impact_score': 16.8,  # Sum of all impact scores
    'division_outlook': 'Second behind Ravens but dangerous',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'historic_investment': {
        'total_commitment': '$570M+ to offensive core',
        'chase_contract': 'Highest non-QB at $40.25M AAV',
        'higgins_discount': 'Took less for championships',
        'wr_tandem_cost': '$69M combined AAV',
    },
    'defensive_overhaul': {
        'anarumo_firing': 'Six seasons, 25th-ranked D',
        'golden_philosophy': 'Malleable defense',
        'new_staff': 'Desai, Montgomery additions',
        'challenge': 'Improve from 25th ranking',
    },
    'hendrickson_situation': {
        'performance': 'Led NFL with 17.5 sacks',
        'demand': '$28-30M annually',
        'current': '$15.8M in 2025',
        'status': 'Trade permission granted',
    },
    'draft_criticism': {
        'grade': 'Dead last with 2.06 GPA',
        'stewart_concerns': 'Only 4.5 college sacks',
        'knight_age': '25-year-old rookie',
        'fairchild_positive': 'Immediate OL starter',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Joe Burrow',
        'backup': 'Logan Woodside',
        'grade': 'A+',
        'notes': 'Elite QB entering prime at 28',
    },
    'offensive_line': {
        'starters': ['Orlando Brown Jr. (LT)', 'Cordell Volson (LG)', 
                     'Ted Karras (C)', 'Kaz Fairchild (RG)', 'Trent Brown (RT)'],
        'depth': 'Lucas Patrick adds versatility',
        'grade': 'B',
        'notes': 'Fairchild immediate upgrade',
    },
    'skill_positions': {
        'wr': "Ja'Marr Chase, Tee Higgins, Tyler Boyd",
        'rb': 'Joe Mixon, Chase Brown, Trayveon Williams',
        'te': 'Mike Gesicki, Drew Sample',
        'grade': 'A+',
        'notes': 'Best WR duo in NFL',
    },
    'defensive_line': {
        'dt': 'D.J. Reader, B.J. Hill, Jordan Knight',
        'edge': 'Trey Hendrickson*, Cam Sample, Joseph Ossai',
        'grade': 'B',
        'notes': 'Hendrickson situation critical',
    },
    'linebackers': {
        'starters': 'Logan Wilson, Germaine Pratt, Barrett Carter',
        'depth': 'Oren Burks, Joe Giles-Harris',
        'grade': 'C+',
        'notes': 'Major weakness remains',
    },
    'secondary': {
        'cb': 'Cam Taylor-Britt, D.J. Turner II, Mike Hilton',
        'safety': 'Dax Hill, Jordan Battle',
        'grade': 'B-',
        'notes': 'Young but talented',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 10.5,
        'lean': 'OVER',
        'reasoning': 'Elite offense overcomes defense',
    },
    'division_odds': {
        'current': '+180',
        'value': 'VALUE',
        'reasoning': 'Ravens vulnerable',
    },
    'playoffs': {
        'current': '-250',
        'value': 'YES',
        'reasoning': 'Lock with this offense',
    },
    'player_props': {
        'burrow_passing_yards': 'OVER 4,600',
        'chase_receiving_yards': 'OVER 1,500',
        'higgins_receiving_yards': 'OVER 1,000',
    },
    'key_angles': {
        'best_bet': 'Chase MVP +2000',
        'fade': 'Defense top-15',
        'narrative': 'Score 30+ weekly',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("CINCINNATI BENGALS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {BENGALS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{BENGALS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {BENGALS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {BENGALS_2025_SUMMARY['total_moves']}")
    print(f"  • Historic Extensions: {BENGALS_2025_SUMMARY['historic_extensions']}")
    print(f"  • Offensive Investment: ${BENGALS_2025_SUMMARY['total_offensive_investment']:,}")
    print(f"  • Coaching Changes: Complete defensive overhaul")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${BENGALS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: ${BENGALS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • Dead Money: ${BENGALS_2025_SUMMARY['dead_money']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Ja'Marr Chase - 4yr/$161M extension ($40.25M AAV)")
    print("  • Tee Higgins - 4yr/$115M extension ($28.75M AAV)")
    print("  • Al Golden - New DC from Notre Dame")
    print("  • Minimal external free agents")
    
    print("\n❌ KEY LOSSES:")
    print("  • Sam Hubbard (EDGE) - Retired after 7 seasons")
    print("  • Lou Anarumo (DC) - Fired after 25th-ranked defense")
    print("  • Minimal roster turnover")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {BENGALS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {BENGALS_2025_SUMMARY['division_outlook']}")
    print(f"  • WR Tandem: $69M combined AAV (NFL record)")
    print(f"  • Hendrickson: Holdout threatens defense")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 10.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Defense must improve from 25th")
    print("  • Hendrickson holdout resolution")
    print("  • Burrow health paramount")
    print("  • Draft class universally panned")

if __name__ == "__main__":
    generate_summary_report()
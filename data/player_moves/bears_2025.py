"""
Chicago Bears 2025 Offseason Moves
Complete overhaul centered around protecting Caleb Williams with new coaching staff
Last Updated: June 23, 2025
"""

BEARS_2025_MOVES = [
    # ========== MAJOR ACQUISITIONS - Offensive line transformation ==========
    {
        'player_name': 'Joe Thuney',
        'position': 'LG',
        'from_team': 'KC',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 40000000,  # Existing contract + extension
        'guaranteed_money': 28000000,
        'aav': 20000000,
        '2024_grade': 9.2,  # Elite 98.2% pass block win rate
        'projected_2025_grade': 9.0,  # Four-time All-Pro
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 10.0,  # Protect Williams' blindside
        'impact_score': 3.0,
        'notes': 'Traded 2026 4th round pick'
    },
    {
        'player_name': 'Jonah Jackson',
        'position': 'RG',
        'from_team': 'LAR',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 17500000,  # Existing deal
        'guaranteed_money': 10000000,
        'aav': 17500000,
        '2024_grade': 8.0,  # 94.7% pass block win rate when healthy
        'projected_2025_grade': 8.2,  # Reunites with Ben Johnson
        'snap_percentage_2024': 25.0,  # Limited by injury
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.0,  # Interior protection
        'impact_score': 2.0,
        'notes': 'Traded 6th round pick'
    },

    # ========== FREE AGENT SIGNINGS - Strategic additions ==========
    {
        'player_name': 'Drew Dalman',
        'position': 'C',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 42000000,
        'guaranteed_money': 28000000,
        'aav': 14000000,
        '2024_grade': 7.8,  # 78.8 PFF grade, 4th among centers
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Revolving door at C solved
        'impact_score': 2.2,
    },
    {
        'player_name': 'Grady Jarrett',
        'position': 'DT',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 43500000,
        'guaranteed_money': 25000000,
        'aav': 14500000,
        '2024_grade': 7.0,  # 36.5 career sacks
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Interior pass rush
        'impact_score': 1.5,
    },
    {
        'player_name': 'Dayo Odeyingbo',
        'position': 'EDGE',
        'from_team': 'Ind',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 48000000,
        'guaranteed_money': 28000000,
        'aav': 16000000,
        '2024_grade': 7.5,  # 8 sacks in 2023
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Complement to Sweat
        'impact_score': 1.8,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS ==========
    {
        'player_name': 'Kyler Gordon',
        'position': 'CB',
        'from_team': 'Chi',
        'to_team': 'Chi',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 40000000,
        'guaranteed_money': 31250000,
        'aav': 13333333,
        '2024_grade': 8.0,  # 76.0 PFF grade, 13th among all corners
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,  # Elite nickel corner retained
    },
    {
        'player_name': 'T.J. Edwards',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Chi',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 20000000,
        'guaranteed_money': 12000000,
        'aav': 10000000,
        '2024_grade': 7.8,  # 129 tackles, team captain
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },

    # ========== MAJOR LOSSES ==========
    {
        'player_name': 'Teven Jenkins',
        'position': 'G',
        'from_team': 'Chi',
        'to_team': 'Cle',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Replaced by better players
    },
    {
        'player_name': 'Jack Sanborn',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # Reunites with Eberflus
    },
    {
        'player_name': 'Keenan Allen',
        'position': 'WR1',
        'from_team': 'Chi',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Still productive at 32
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # Age/youth movement
    },

    # ========== 2025 NFL DRAFT - Elite weapons for Williams ==========
    {
        'player_name': 'Colston Loveland',
        'position': 'TE',
        'from_team': 'Michigan',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 1, Pick 10',
        'contract_years': 4,
        'contract_value': 22000000,
        'guaranteed_money': 22000000,
        'aav': 5500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Elite TE prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # LaPorta 2.0 for Johnson
        'impact_score': 2.5,
    },
    {
        'player_name': 'Luther Burden III',
        'position': 'WR',
        'from_team': 'Missouri',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 2, Pick 39',
        'contract_years': 4,
        'contract_value': 9500000,
        'guaranteed_money': 5500000,
        'aav': 2375000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # 1,212 yards in 2023
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # PFF's WR2 in class
        'impact_score': 2.0,
    },
    {
        'player_name': 'Ozzy Trapilo',
        'position': 'OT',
        'from_team': 'Boston College',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 2, Pick 56',
        'contract_years': 4,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 2000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 36 career starts
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # LT depth/competition
        'impact_score': 1.0,
    },
    {
        'player_name': 'Shemar Turner',
        'position': 'DL',
        'from_team': 'Texas A&M',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 2, Pick 62',
        'contract_years': 4,
        'contract_value': 7500000,
        'guaranteed_money': 3500000,
        'aav': 1875000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # "Violence and aggression"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Dennis Allen fit
        'impact_score': 0.8,
    },
    {
        'player_name': 'Ruben Hyppolite II',
        'position': 'LB',
        'from_team': 'Maryland',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 4, Pick 106',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 1000000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Zah Frazier',
        'position': 'CB',
        'from_team': 'UTSA',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 5, Pick 142',
        'contract_years': 4,
        'contract_value': 4000000,
        'guaranteed_money': 700000,
        'aav': 1000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 9.36 RAS score
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.4,
    },
    {
        'player_name': 'Luke Newman',
        'position': 'OL',
        'from_team': 'Michigan State',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 6, Pick 183',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 500000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Versatile lineman
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Kyle Monangai',
        'position': 'RB',
        'from_team': 'Rutgers',
        'to_team': 'Chi',
        'move_type': '2025 Draft - Round 7, Pick 220',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 300000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Led Big Ten in rushing
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },

    # ========== COACHING OVERHAUL - Complete transformation ==========
    {
        'player_name': 'Matt Eberflus',
        'position': 'COACH-HC',
        'from_team': 'Chi',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 3.0,  # 14-32 record, clock management disaster
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 2.0,  # First mid-season firing
        'importance_to_new_team': 0.0,
        'impact_score': 1.5,  # Addition by subtraction
    },
    {
        'player_name': 'Ben Johnson',
        'position': 'COACH-HC',
        'from_team': 'Det-OC',
        'to_team': 'Chi',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 40000000,
        'guaranteed_money': 30000000,
        'aav': 8000000,
        '2024_grade': 10.0,  # Lions #1 offense 2022-24
        'projected_2025_grade': 9.0,  # QB whisperer for Williams
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # Franchise-altering hire
    },
    {
        'player_name': 'Dennis Allen',
        'position': 'COACH-DC',
        'from_team': 'NO',
        'to_team': 'Chi',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 7500000,
        'guaranteed_money': 4500000,
        'aav': 2500000,
        '2024_grade': 7.0,  # Former Saints HC
        'projected_2025_grade': 8.0,  # Aggressive 4-3 scheme
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,
    },
    {
        'player_name': 'Declan Doyle',
        'position': 'COACH-OC',
        'from_team': 'Den',
        'to_team': 'Chi',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 3000000,
        'guaranteed_money': 1800000,
        'aav': 1000000,
        '2024_grade': 7.0,  # 28-year-old rising star
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
]

# ========== SUMMARY METRICS ==========
BEARS_2025_SUMMARY = {
    'total_moves': len(BEARS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 3,
    'trades': 2,
    'draft_picks': 8,
    'key_resignings': 2,
    'coaching_changes': 4,
    'total_guaranteed_money': 257000000,  # Historic transformation
    'dead_money': 8500000,
    'cap_space_remaining': 15000000,
    'championship_window': '2025-2028',
    'offseason_grade': 'A-',
    'key_philosophy': 'Complete transformation around Williams with elite protection',
    'net_impact_score': 24.5,  # Sum of all impact scores
    'division_outlook': 'Rising contender in loaded NFC North',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'offensive_line_revolution': {
        'investment': '$100M+ in OL additions',
        'sacks_allowed_2024': '68 (3rd-most in NFL history)',
        'projected_improvement': 'Top-10 OL potential',
        'philosophy': 'Protect Williams at all costs',
    },
    'coaching_overhaul': {
        'johnson_impact': 'Lions OC who developed Goff',
        'offensive_system': 'Play-action heavy, TE-centric',
        'defensive_change': 'Aggressive 4-3 under Allen',
        'culture_shift': 'From conservative to innovative',
    },
    'draft_excellence': {
        'grades': 'NFL.com A, PFF A-',
        'loveland_comparison': 'Sam LaPorta 2.0',
        'burden_value': 'WR2 in draft at pick 39',
        'depth_building': 'Eight quality additions',
    },
    'cap_management': {
        'starting_space': '$62.9M (4th-most)',
        'remaining_space': '$15M (24th)',
        'structure': 'Front-loaded guarantees',
        'flexibility': 'Maintained for 2026+',
    },
    'injury_considerations': {
        'braxton_jones': 'Ankle surgery influenced Trapilo pick',
        'jonah_jackson': 'Limited to 4 games in 2024',
        'risk_mitigation': 'Depth at every OL position',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Caleb Williams',
        'backup': 'Tyson Bagent',
        'grade': 'A-',
        'notes': 'Elite protection transforms outlook',
    },
    'offensive_line': {
        'starters': ['Braxton Jones (LT)', 'Joe Thuney (LG)', 'Drew Dalman (C)', 
                     'Jonah Jackson (RG)', 'Darnell Wright (RT)'],
        'depth': 'Ozzy Trapilo, Luke Newman',
        'grade': 'A',
        'notes': 'From worst to potential top-10 unit',
    },
    'skill_positions': {
        'wr': 'DJ Moore, Rome Odunze, Luther Burden III',
        'rb': 'D\'Andre Swift, Khalil Herbert, Kyle Monangai',
        'te': 'Colston Loveland, Cole Kmet',
        'grade': 'A',
        'notes': 'Elite weapons at every level',
    },
    'defensive_line': {
        'dt': 'Grady Jarrett, Gervon Dexter, Andrew Billings',
        'edge': 'Montez Sweat, Dayo Odeyingbo, DeMarcus Walker',
        'grade': 'B+',
        'notes': 'Pass rush depth still a concern',
    },
    'linebackers': {
        'starters': 'T.J. Edwards, Tremaine Edmunds',
        'depth': 'Ruben Hyppolite II, Noah Sewell',
        'grade': 'B+',
        'notes': 'Edwards extension key retention',
    },
    'secondary': {
        'cb': 'Jaylon Johnson, Kyler Gordon, Tyrique Stevenson',
        'safety': 'Kevin Byard, Jaquan Brisker',
        'grade': 'A-',
        'notes': 'Gordon highest-paid nickel CB',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'OVER',
        'reasoning': 'Elite OL + weapons + coaching',
    },
    'division_odds': {
        'current': '+450',
        'value': 'SLIGHT VALUE',
        'reasoning': 'Tough division but dramatic improvement',
    },
    'playoffs': {
        'current': '-120',
        'value': 'YES',
        'reasoning': 'Wild card likely with Lions/Vikings/Packers',
    },
    'player_props': {
        'williams_passing_yards': 'OVER 3,800',
        'williams_passing_tds': 'OVER 26.5',
        'loveland_receiving_yards': 'OVER 650',
    },
    'key_bets': {
        'best': 'Win total OVER 8.5',
        'sleeper': 'Loveland OROY +1200',
        'narrative': 'Week 1 upset potential',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("CHICAGO BEARS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {BEARS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{BEARS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {BEARS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {BEARS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {BEARS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Trades: {BEARS_2025_SUMMARY['trades']} (Thuney, Jackson)")
    print(f"  • Draft Picks: {BEARS_2025_SUMMARY['draft_picks']}")
    print(f"  • Coaching Changes: {BEARS_2025_SUMMARY['coaching_changes']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${BEARS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${BEARS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${BEARS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Joe Thuney (LG) - 4x All-Pro via trade from KC")
    print("  • Ben Johnson (HC) - Lions OC, offensive mastermind")
    print("  • Colston Loveland (TE) - 1st round pick, elite prospect")
    print("  • Luther Burden III (WR) - 2nd round steal")
    
    print("\n❌ KEY LOSSES:")
    print("  • Matt Eberflus (HC) - Fired mid-season")
    print("  • Teven Jenkins (G) - To Browns in free agency")
    print("  • Keenan Allen (WR) - Unsigned free agent")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {BEARS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {BEARS_2025_SUMMARY['division_outlook']}")
    print(f"  • OL Investment: $100M+ to protect Williams")
    print(f"  • Culture Change: Johnson brings winning mentality")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Williams development with elite protection")
    print("  • Johnson's offensive system implementation")
    print("  • Pass rush depth remains concern")
    print("  • NFC North gauntlet (3 playoff teams)")

if __name__ == "__main__":
    generate_summary_report()
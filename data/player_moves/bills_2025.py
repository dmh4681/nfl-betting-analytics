"""
Buffalo Bills 2025 Offseason Moves
Defensive transformation: Building to finally conquer Kansas City
Last Updated: June 23, 2025
"""

BILLS_2025_MOVES = [
    # ========== KEY FREE AGENT SIGNINGS - Defensive focus ==========
    {
        'player_name': 'Joey Bosa',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 12600000,
        'guaranteed_money': 9000000,  # Signing bonus
        'aav': 12600000,
        '2024_grade': 7.0,  # Five-time Pro Bowler despite injuries
        'projected_2025_grade': 7.5,  # Calculated gamble
        'snap_percentage_2024': 60.0,  # Missed 23 games over past 3 seasons
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Replaces Von Miller at half cost
        'impact_score': 2.0,
    },
    {
        'player_name': 'Josh Palmer',
        'position': 'WR',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 36000000,
        'guaranteed_money': 18000000,
        'aav': 12000000,
        '2024_grade': 7.0,  # 39 catches, 584 yards in 7 starts
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Downfield threat
        'impact_score': 1.5,
    },
    {
        'player_name': 'Michael Hoecht',
        'position': 'DT',
        'from_team': 'LAR',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 24000000,
        'guaranteed_money': 12000000,
        'aav': 12000000,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,  # 6-game PED suspension
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # Interior depth
        'impact_score': -0.5,  # Suspension hurts
    },
    {
        'player_name': 'Larry Ogunjobi',
        'position': 'DT',
        'from_team': 'Pit',
        'to_team': 'Buf',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 8000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,  # 6-game PED suspension
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': -0.3,  # Suspension concern
    },

    # ========== MAJOR LOSSES - Cap casualties ==========
    {
        'player_name': 'Von Miller',
        'position': 'EDGE',
        'from_team': 'Buf',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -15400000,  # Dead money
        'aav': 0,
        '2024_grade': 6.0,  # Only 6 sacks at age 36
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,  # Declining production
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # Saved $8.4M
    },
    {
        'player_name': 'Amari Cooper',
        'position': 'WR1',
        'from_team': 'Buf',
        'to_team': 'UNSIGNED',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # 32 catches, 297 yards in 8 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,  # Cap constraints
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Mack Hollins',
        'position': 'WR',
        'from_team': 'Buf',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== TRADES ==========
    {
        'player_name': 'Kaiir Elam',
        'position': 'CB',
        'from_team': 'Buf',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.8,  # Former 1st round bust
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Got 5th + 7th picks
    },

    # ========== 2025 NFL DRAFT - Defense first five picks ==========
    {
        'player_name': 'Maxwell Hairston',
        'position': 'CB',
        'from_team': 'Kentucky',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 1, Pick 30',
        'contract_years': 4,
        'contract_value': 15200000,
        'guaranteed_money': 15200000,
        'aav': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Fastest 40 at combine (4.28)
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Expected starter
        'impact_score': 2.0,
    },
    {
        'player_name': 'T.J. Sanders',
        'position': 'DT',
        'from_team': 'South Carolina',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 2, Pick 41',
        'contract_years': 4,
        'contract_value': 8200000,
        'guaranteed_money': 4100000,
        'aav': 2050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 4.0 sacks in 2024
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # 3-down player
        'impact_score': 1.8,
    },
    {
        'player_name': 'Landon Jackson',
        'position': 'EDGE',
        'from_team': 'Arkansas',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 3, Pick 72',
        'contract_years': 4,
        'contract_value': 6200000,
        'guaranteed_money': 1500000,
        'aav': 1550000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 16 career sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # 6'6" length
        'impact_score': 1.2,
    },
    {
        'player_name': 'Deone Walker',
        'position': 'DT',
        'from_team': 'Kentucky',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 4, Pick 110',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 950000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Run defense
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jordan Hancock',
        'position': 'CB/S',
        'from_team': 'Ohio State',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 5, Pick 151',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 700000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Versatile DB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Jackson Hawes',
        'position': 'TE',
        'from_team': 'Georgia Tech',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 6, Pick 173',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 500000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # First offense pick
        'impact_score': 0.3,
    },
    {
        'player_name': 'Chase Lundt',
        'position': 'OT',
        'from_team': 'UConn',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 6, Pick 206',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # OL depth
        'impact_score': 0.2,
    },
    {
        'player_name': 'Kaden Prather',
        'position': 'WR',
        'from_team': 'Maryland',
        'to_team': 'Buf',
        'move_type': '2025 Draft - Round 7, Pick 255',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # 6'4" target
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.1,
    },

    # ========== KEY EXTENSIONS - Locking up young core ==========
    {
        'player_name': 'Josh Allen',
        'position': 'QB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Contract Extension',
        'contract_years': 6,
        'contract_value': 330000000,  # Record deal
        'guaranteed_money': 250000000,  # NFL record
        'aav': 55000000,
        '2024_grade': 9.5,  # MVP candidate
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # Reduced 2025 cap hit
    },
    {
        'player_name': 'Khalil Shakir',
        'position': 'WR',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 53000000,
        'guaranteed_money': 30000000,
        'aav': 13250000,
        '2024_grade': 8.0,  # 76 catches, 821 yards
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # ESPN's best move
        'impact_score': 2.5,  # Only $2.6M cap hit
    },
    {
        'player_name': 'Greg Rousseau',
        'position': 'EDGE',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 80000000,
        'guaranteed_money': 45000000,
        'aav': 20000000,
        '2024_grade': 8.5,
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,
    },
    {
        'player_name': 'Terrel Bernard',
        'position': 'LB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 50000000,
        'guaranteed_money': 28000000,
        'aav': 12500000,
        '2024_grade': 8.0,  # Breakout season
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,
    },
    {
        'player_name': 'Christian Benford',
        'position': 'CB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 76000000,
        'guaranteed_money': 40000000,
        'aav': 19000000,
        '2024_grade': 8.0,
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 88.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 2.2,
    },
    {
        'player_name': 'Damar Hamlin',
        'position': 'S',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 7.0,  # Started 14 games
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,  # Remarkable recovery
        'impact_score': 1.0,
    },
    {
        'player_name': 'Ty Johnson',
        'position': 'RB',
        'from_team': 'Buf',
        'to_team': 'Buf',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 6.8,  # Third-down specialist
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # Allen's favorite
        'impact_score': 0.5,
    },

    # ========== COACHING CHANGE ==========
    {
        'player_name': 'Chris Tabor',
        'position': 'COACH-ST',
        'from_team': 'Cle',
        'to_team': 'Buf',
        'move_type': 'Special Teams Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 2000000,
        '2024_grade': 7.0,  # 2nd-best by NFLPA in 2022
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replace Smiley
        'impact_score': 1.0,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Buf',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 10000000,  # Combined
        'guaranteed_money': 1000000,
        'aav': 3333333,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
BILLS_2025_SUMMARY = {
    'total_moves': len(BILLS_2025_MOVES),
    'free_agent_signings': 4,  # Limited by cap
    'major_losses': 3,  # Von, Cooper, Hollins
    'trades': 1,  # Elam
    'draft_picks': 8,
    'key_extensions': 6,  # Allen, Shakir, Rousseau, etc.
    'key_resignings': 2,  # Hamlin, Johnson
    'coaching_changes': 1,  # Tabor
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 625000000,  # Dominated by extensions
    'cap_constraints': True,  # Started $15.7M over cap
    'cap_space_remaining': 8000000,  # After all moves
    'championship_window': '2025-2030',  # Allen's prime
    'offseason_grade': 'A-',
    'key_philosophy': 'Defensive transformation to finally beat Kansas City',
    'net_impact_score': 26.5,  # Sum of all impact scores
    'division_outlook': 'Favorites but Patriots aggressive',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'defensive_focus': {
        'draft_strategy': 'First 5 picks on defense (first time since 2006)',
        'pass_rush': 'Bosa gamble to replace Von Miller',
        'secondary': 'Hairston speed to match KC receivers',
        'philosophy': 'Target KC offensive success directly',
    },
    'cap_management': {
        'starting_position': '$15.7M over cap entering offseason',
        'restructures': 'Allen deal reduces 2025 hit by $3M',
        'extensions': 'Team-friendly deals for young core',
        'approach': 'Incremental improvements over splashes',
    },
    'offensive_continuity': {
        'coordinator': 'Joe Brady retained after HC interest',
        'system': 'Led league in total scoring in 2024',
        'weapons': 'Palmer adds downfield element',
        'concern': 'James Cook contract demands',
    },
    'championship_urgency': {
        'playoff_history': '0-6 vs KC in playoffs under Allen',
        'afc_title_game': '32 points allowed to KC',
        'defensive_rank': '24th in pass defense',
        'window': 'Must capitalize on Allen prime',
    },
    'coaching_stability': {
        'mcdermott': '9th season, organizational continuity',
        'brady_retention': 'Critical after multiple offers',
        'babich': '2nd year DC earning respect',
        'tabor': 'Only change after ST struggles',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Josh Allen',
        'backup': 'Shane Buechele',
        'grade': 'A+',
        'notes': 'Allen locked up with record deal through 2030',
    },
    'offensive_line': {
        'starters': ['Dion Dawkins (LT)', 'Connor McGovern (LG)', 'Mitch Morse (C)', 
                     'O\'Cyrus Torrence (RG)', 'Spencer Brown (RT)'],
        'depth': 'Lundt adds late-round development',
        'grade': 'B+',
        'notes': 'Continuity with established starters',
    },
    'skill_positions': {
        'wr': 'Stefon Diggs (traded), Khalil Shakir, Josh Palmer, Kaden Prather',
        'rb': 'James Cook, Ty Johnson, Latavius Murray',
        'te': 'Dalton Kincaid, Dawson Knox, Jackson Hawes',
        'grade': 'B+',
        'notes': 'Diggs trade creates void, Shakir emergence key',
    },
    'defensive_line': {
        'dt': 'Ed Oliver, DaQuan Jones, T.J. Sanders, Deone Walker',
        'edge': 'Greg Rousseau, Joey Bosa, A.J. Epenesa, Landon Jackson',
        'grade': 'B+',
        'notes': 'Bosa health crucial, young talent developing',
    },
    'linebackers': {
        'starters': 'Terrel Bernard, Matt Milano, Dorian Williams',
        'depth': 'Baylon Spector provides depth',
        'grade': 'A-',
        'notes': 'Bernard breakout solidifies unit',
    },
    'secondary': {
        'cb': 'Christian Benford, Maxwell Hairston, Taron Johnson',
        'safety': 'Jordan Poyer, Micah Hyde, Damar Hamlin',
        'grade': 'B+',
        'notes': 'Hairston speed adds new dimension',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 11.5,
        'lean': 'UNDER',
        'reasoning': 'Defensive questions, tough schedule',
    },
    'division_odds': {
        'current': '-150',
        'value': 'NO',
        'reasoning': 'Patriots spent big, Jets wild card',
    },
    'super_bowl_odds': {
        'current': '+900',
        'value': 'NO',
        'reasoning': 'KC still in way',
    },
    'player_props': {
        'allen_passing_yards': 'OVER 4,300',
        'allen_rushing_tds': 'OVER 8.5',
        'shakir_receiving_yards': 'OVER 900',
        'bosa_sacks': 'UNDER 8.5 (injury risk)',
    },
    'key_angles': {
        'best_bet': 'Shakir OPOY +3500',
        'fade': 'Division winner at -150',
        'narrative': 'Defense improves but KC obstacle remains',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("BUFFALO BILLS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {BILLS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{BILLS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {BILLS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {BILLS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {BILLS_2025_SUMMARY['free_agent_signings']} (cap limited)")
    print(f"  • Draft Picks: {BILLS_2025_SUMMARY['draft_picks']} (first 5 on defense)")
    print(f"  • Key Extensions: {BILLS_2025_SUMMARY['key_extensions']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${BILLS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Started: $15.7M over cap")
    print(f"  • Current Cap Space: ${BILLS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Joey Bosa (EDGE) - 1yr/$12.6M calculated risk")
    print("  • Josh Palmer (WR) - 3yr/$36M downfield threat")
    print("  • Maxwell Hairston (CB) - 1st round, 4.28 speed")
    print("  • Chris Tabor (ST Coordinator)")
    
    print("\n❌ KEY LOSSES:")
    print("  • Von Miller - Released (saved $8.4M)")
    print("  • Amari Cooper - Cap casualty")
    print("  • Kaiir Elam - Traded to Dallas")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {BILLS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Allen Extension: $330M with NFL-record $250M guaranteed")
    print(f"  • Division: {BILLS_2025_SUMMARY['division_outlook']}")
    print(f"  • Draft: Historic defensive focus")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 11.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Joey Bosa health (missed 23 games in 3 years)")
    print("  • Defensive improvement vs KC")
    print("  • James Cook contract situation")
    print("  • First-place schedule difficulty")

if __name__ == "__main__":
    generate_summary_report()
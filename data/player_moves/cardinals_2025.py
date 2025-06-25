"""
Arizona Cardinals 2025 Offseason Moves
Defensive transformation: Leveraging $74.4M cap space to build around Murray
Last Updated: June 23, 2025
"""

CARDINALS_2025_MOVES = [
    # ========== MARQUEE DEFENSIVE SIGNINGS ==========
    {
        'player_name': 'Josh Sweat',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 76400000,  # Largest FA signing in Ossenfort era
        'guaranteed_money': 38000000,
        'aav': 19100000,
        '2024_grade': 8.5,  # 8 sacks regular season + 2.5 in Super Bowl
        'projected_2025_grade': 8.5,  # Reunites with Gannon
        'snap_percentage_2024': 59.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.5,  # Franchise pass rusher
        'impact_score': 3.0,  # Transforms pass rush
    },
    {
        'player_name': 'Dalvin Tomlinson',
        'position': 'DT',
        'from_team': 'Cle',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 29000000,
        'guaranteed_money': 18000000,
        'aav': 14500000,
        '2024_grade': 8.2,  # Anchored league's best run D
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.0,  # Interior anchor
        'impact_score': 2.2,
    },
    {
        'player_name': 'Calais Campbell',
        'position': 'DT/DE',
        'from_team': 'Mia',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 6000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # 6.5 sacks at age 38
        'projected_2025_grade': 6.8,  # Returns home
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Leadership + production
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jacoby Brissett',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12500000,
        'guaranteed_money': 8000000,
        'aav': 6250000,
        '2024_grade': 6.5,  # Solid backup starter
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Murray insurance
        'impact_score': 1.0,
    },
    {
        'player_name': 'Akeem Davis-Gaither',
        'position': 'LB',
        'from_team': 'Cin',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 11000000,
        'guaranteed_money': 5500000,
        'aav': 5500000,
        '2024_grade': 7.2,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # LB depth
        'impact_score': 1.0,
    },
    {
        'player_name': 'Royce Newman',
        'position': 'G',
        'from_team': 'GB',
        'to_team': 'Ari',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1200000,
        'aav': 2500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # OL depth
        'impact_score': 0.5,
    },

    # ========== KEY RE-SIGNINGS - Offensive continuity ==========
    {
        'player_name': 'Trey McBride',
        'position': 'TE',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 76000000,  # Briefly NFL's highest-paid TE
        'guaranteed_money': 42000000,
        'aav': 19000000,
        '2024_grade': 9.2,  # 111 catches, 1,146 yards
        'projected_2025_grade': 9.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,  # Offensive centerpiece
        'impact_score': 2.5,  # Elite retention
    },
    {
        'player_name': 'James Conner',
        'position': 'RB',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 19000000,
        'guaranteed_money': 10000000,
        'aav': 9500000,
        '2024_grade': 8.0,  # Back-to-back 1,000-yard seasons
        'projected_2025_grade': 7.8,  # Age 30
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # Veteran leadership
        'impact_score': 1.8,
    },
    {
        'player_name': 'Baron Browning',
        'position': 'EDGE',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 8000000,
        'aav': 8000000,
        '2024_grade': 7.5,  # Solid after trade from Denver
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Pass rush depth
        'impact_score': 1.2,
    },
    {
        'player_name': 'Evan Brown',
        'position': 'G',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 11400000,
        'guaranteed_money': 6000000,
        'aav': 5700000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Murray protection
        'impact_score': 1.0,
    },
    {
        'player_name': 'Kelvin Beachum',
        'position': 'RT',
        'from_team': 'Ari',
        'to_team': 'Ari',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 5150000,
        'guaranteed_money': 2500000,
        'aav': 2575000,
        '2024_grade': 6.8,  # Veteran presence
        'projected_2025_grade': 6.5,  # Age 36
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # OL continuity
        'impact_score': 0.8,
    },

    # ========== KEY LOSSES ==========
    {
        'player_name': 'Roy Lopez',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'Buf',
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
    {
        'player_name': 'Khyiris Tonga',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'Min',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Naquan Jones',
        'position': 'DT',
        'from_team': 'Ari',
        'to_team': 'TB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # Combined lost 957 DL snaps
    },

    # ========== 2025 NFL DRAFT - Defensive focus (6 of 7 picks) ==========
    {
        'player_name': 'Walter Nolen III',
        'position': 'DT',
        'from_team': 'Ole Miss',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 1, Pick 16',
        'contract_years': 4,
        'contract_value': 18500000,
        'guaranteed_money': 18500000,
        'aav': 4625000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # 91.6 PFF run-defense grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Potential cornerstone
        'impact_score': 2.0,
    },
    {
        'player_name': 'Will Johnson',
        'position': 'CB1',
        'from_team': 'Michigan',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 2, Pick 47',
        'contract_years': 4,
        'contract_value': 8800000,
        'guaranteed_money': 4400000,
        'aav': 2200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # Elite prospect fell due to injury
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Steal of draft - CB1 potential
        'impact_score': 2.5,  # Major value
    },
    {
        'player_name': 'Jordan Burch',
        'position': 'EDGE',
        'from_team': 'Oregon',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 3, Pick 80',
        'contract_years': 4,
        'contract_value': 5200000,
        'guaranteed_money': 1200000,
        'aav': 1300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 8.5 sacks at Oregon
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush depth
        'impact_score': 1.0,
    },
    {
        'player_name': 'Cody Simon',
        'position': 'LB',
        'from_team': 'Ohio State',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 4, Pick 115',
        'contract_years': 4,
        'contract_value': 4300000,
        'guaranteed_money': 800000,
        'aav': 1075000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # CFP Championship Defensive MVP
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # LB upgrade
        'impact_score': 1.2,
    },
    {
        'player_name': 'Denzel Burke',
        'position': 'CB2',
        'from_team': 'Ohio State',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 5, Pick 167',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 500000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # CB depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Hayden Conner',
        'position': 'G',
        'from_team': 'Texas',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 5, Pick 172',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 500000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Zero sacks allowed on 617 snaps
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Only offensive pick
        'impact_score': 0.5,
    },
    {
        'player_name': 'Kitan Crawford',
        'position': 'CB/S',
        'from_team': 'Nevada',
        'to_team': 'Ari',
        'move_type': '2025 Draft - Round 7, Pick 248',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # 88.5 PFF coverage grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Special teams ace
        'impact_score': 0.3,
    },

    # ========== COACHING CHANGES - Strategic position upgrades ==========
    {
        'player_name': 'Justin Frye',
        'position': 'COACH-OL',
        'from_team': 'OSU',
        'to_team': 'Ari',
        'move_type': 'Offensive Line Coach Hire',
        'contract_years': 3,
        'contract_value': 2400000,
        'guaranteed_money': 1200000,
        'aav': 800000,
        '2024_grade': 8.0,  # Ohio State OL success
        'projected_2025_grade': 8.5,  # Previously coached Paris Johnson Jr.
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Critical hire
        'impact_score': 1.5,
    },
    {
        'player_name': 'Winston DeLattiboudere III',
        'position': 'COACH-DL',
        'from_team': 'Min',
        'to_team': 'Ari',
        'move_type': 'Defensive Line Coach Hire',
        'contract_years': 2,
        'contract_value': 1600000,
        'guaranteed_money': 800000,
        'aav': 800000,
        '2024_grade': 7.0,  # Young coach with potential
        'projected_2025_grade': 7.5,  # Rallis connection
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # DL coach at age 27
        'impact_score': 1.0,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Ari',
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
CARDINALS_2025_SUMMARY = {
    'total_moves': len(CARDINALS_2025_MOVES),
    'free_agent_signings': 6,
    'major_losses': 3,
    'draft_picks': 7,
    'key_resignings': 5,
    'coaching_hires': 2,
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 158300000,  # Aggressive defensive spending
    'cap_space_utilized': 74400000,  # Started with massive space
    'cap_space_remaining': 30000000,  # Still flexibility
    'championship_window': '2025-2027',  # Murray prime years
    'offseason_grade': 'A-',
    'key_philosophy': 'Defensive transformation while maintaining offensive continuity around Murray',
    'net_impact_score': 21.5,  # Sum of all impact scores
    'division_outlook': 'Positioned as Rams primary challenger in NFC West',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'defensive_overhaul': {
        'pass_rush': 'Zero players with 5+ sacks → Sweat/Browning/Burch',
        'interior_dl': 'Lost 957 snaps → Added Tomlinson/Nolen/Campbell',
        'secondary': 'Will Johnson steal at #47 overall',
        'investment': '$76.4M to Sweat largest FA deal',
    },
    'offensive_continuity': {
        'core_retained': 'McBride ($76M), Conner ($19M) extensions',
        'murray_support': 'Existing weapons maintained',
        'ol_concerns': 'Only added 1 offensive player in draft',
        'philosophy': 'Trust in health and development',
    },
    'draft_excellence': {
        'defensive_focus': '6 of 7 picks on defense',
        'value_picks': 'Johnson fell due to injury concerns',
        'grades': 'PFF A+, ESPN called Johnson 2nd-best value',
        'immediate_impact': 'Multiple Day 1 contributors',
    },
    'cap_management': {
        'starting_space': '$74.4M (4th-most in NFL)',
        'smart_structure': 'Sweat only $7.24M cap hit in 2025',
        'future_flexibility': '$75M+ available for extensions',
        'rollover': '$11.3M from 2024 added',
    },
    'coaching_upgrades': {
        'frye_hire': 'Previously coached Paris Johnson Jr.',
        'defensive_youth': 'Young coaches with scheme familiarity',
        'continuity': 'Gannon, Petzing, Rallis all return',
        'culture': 'Third year brings accountability',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Kyler Murray',
        'backup': 'Jacoby Brissett',
        'grade': 'A-',
        'notes': 'Murray healthy for first time since 2020, Brissett solid insurance',
    },
    'offensive_line': {
        'starters': ['Paris Johnson Jr. (LT)', 'Evan Brown (LG)', 'Hjalte Froholdt (C)', 
                     'Will Hernandez/Hayden Conner (RG)', 'Jonah Williams (RT)'],
        'depth': 'Concerns at RG after Hernandez injury',
        'grade': 'B',
        'notes': 'Left side solid, right side questions',
    },
    'skill_positions': {
        'wr': 'Marvin Harrison Jr., Michael Wilson, Greg Dortch',
        'rb': 'James Conner, Trey Benson, Emari Demercado',
        'te': 'Trey McBride, Elijah Higgins',
        'grade': 'A',
        'notes': 'Elite weapons if healthy',
    },
    'defensive_line': {
        'dt': 'Dalvin Tomlinson, Walter Nolen, Calais Campbell',
        'edge': 'Josh Sweat, Baron Browning, Jordan Burch',
        'grade': 'A-',
        'notes': 'Complete transformation from weakness to strength',
    },
    'linebackers': {
        'starters': 'Kyzir White, Cody Simon, Akeem Davis-Gaither',
        'depth': 'Jesse Luketa, Owen Pappoe',
        'grade': 'B+',
        'notes': 'Simon adds athleticism and coverage',
    },
    'secondary': {
        'cb': 'Will Johnson, Starling Thomas V, Denzel Burke',
        'safety': 'Budda Baker, Jalen Thompson',
        'grade': 'B+',
        'notes': 'Johnson potential lockdown CB1',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'OVER',
        'reasoning': 'Elite defense + healthy Murray',
    },
    'division_odds': {
        'current': '+350',
        'value': 'YES',
        'reasoning': 'Second-best roster in NFC West',
    },
    'playoffs': {
        'odds': '-150',
        'value': 'YES',
        'reasoning': 'Wild card floor with division upside',
    },
    'player_props': {
        'murray_passing_yards': 'OVER 3,900',
        'mcbride_receiving_yards': 'OVER 1,100',
        'sweat_sacks': 'OVER 9.5',
        'johnson_interceptions': 'OVER 3.5',
    },
    'key_bets': {
        'best': 'Playoffs -150',
        'division_value': '+350 worth small play',
        'player_award': 'Will Johnson DROY +1200',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("ARIZONA CARDINALS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {CARDINALS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{CARDINALS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {CARDINALS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {CARDINALS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {CARDINALS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Draft Picks: {CARDINALS_2025_SUMMARY['draft_picks']} (6 of 7 on defense)")
    print(f"  • Key Re-signings: {CARDINALS_2025_SUMMARY['key_resignings']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${CARDINALS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Utilized: ${CARDINALS_2025_SUMMARY['cap_space_utilized']:,}")
    print(f"  • Remaining Cap: ${CARDINALS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • Started with: $74.4M (4th-most in NFL)")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Josh Sweat (EDGE) - 4yr/$76.4M from Eagles")
    print("  • Dalvin Tomlinson (DT) - 2yr/$29M from Browns")
    print("  • Will Johnson (CB) - 2nd round steal, fell due to injury")
    print("  • Walter Nolen III (DT) - 1st round, 91.6 run defense grade")
    
    print("\n❌ KEY LOSSES:")
    print("  • Roy Lopez, Khyiris Tonga, Naquan Jones (DTs)")
    print("  • Combined 957 defensive line snaps departed")
    print("  • Minimal offensive departures")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {CARDINALS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division: {CARDINALS_2025_SUMMARY['division_outlook']}")
    print(f"  • Pass rush: 0 players with 5+ sacks → Sweat/Browning/Burch")
    print(f"  • Draft grade: PFF A+ (one of only three teams)")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Murray health (first full season since 2020)")
    print("  • Will Johnson recovery from injury")
    print("  • Right side OL concerns")
    print("  • Defensive scheme Year 3 breakthrough")

if __name__ == "__main__":
    generate_summary_report()
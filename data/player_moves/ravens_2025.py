"""
Baltimore Ravens 2025 Offseason Moves
Strategic roster refinement maintaining championship window
Last Updated: June 23, 2025
"""

RAVENS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Targeted veteran additions ==========
    {
        'player_name': 'DeAndre Hopkins',
        'position': 'WR',
        'from_team': 'Ten',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        'guaranteed_money': 3500000,
        'aav': 5000000,
        '2024_grade': 6.8,  # 610 yards, age 32
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # Red zone target
        'impact_score': 1.2,
        'notes': 'Finally gets proven WR for Jackson'
    },
    {
        'player_name': 'Chidobe Awuzie',
        'position': 'CB',
        'from_team': 'Cin',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        'guaranteed_money': 2500000,
        'aav': 4000000,
        '2024_grade': 6.5,  # 81 career starts
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # CB3 behind Humphrey/Wiggins
        'impact_score': 1.0,
    },
    {
        'player_name': 'Cooper Rush',
        'position': 'QB',
        'from_team': 'Dal',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6200000,
        'guaranteed_money': 4200000,
        'aav': 3100000,
        '2024_grade': 6.5,  # 9-5 career record
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Major upgrade at backup
        'impact_score': 0.8,
        'notes': 'Up to $12.2M with incentives'
    },
    {
        'player_name': 'Jake Hummel',
        'position': 'LB/ST',
        'from_team': 'LAR',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.2,  # 8 ST tackles, blocked punt TD
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,  # ST only
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Replace Harrison/Board
        'impact_score': 0.5,
    },
    {
        'player_name': 'Jaire Alexander',
        'position': 'CB',
        'from_team': 'GB',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 6000000,
        'guaranteed_money': 4000000,
        'aav': 6000000,
        '2024_grade': 7.0,  # Former All-Pro
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Elite talent gamble
        'impact_score': 1.5,
        'notes': '$4M base + $2M incentives, released June 9'
    },

    # ========== MAJOR LOSSES - Cap casualties and departures ==========
    {
        'player_name': 'Patrick Mekari',
        'position': 'OL',
        'from_team': 'Bal',
        'to_team': 'Jax',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Started all 17 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,  # Versatility loss
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # 3yr/$37.5M to Jags
    },
    {
        'player_name': 'Brandon Stephens',
        'position': 'CB',
        'from_team': 'Bal',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # 806 yards allowed
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # 3yr/$36M to Jets
    },
    {
        'player_name': 'Malik Harrison',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'Pit',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 54 tackles, ST ace
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 38.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # 2yr/$10M to rival Steelers
    },
    {
        'player_name': 'Chris Board',
        'position': 'LB/ST',
        'from_team': 'Bal',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # ST captain
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,  # 80% ST snaps
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # 2yr/$6M to Giants
    },
    {
        'player_name': 'Josh Jones',
        'position': 'OL',
        'from_team': 'Bal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Jumbo packages
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # 1yr/$4.75M to Seattle
    },

    # ========== 2025 NFL DRAFT - Elite value selections ==========
    {
        'player_name': 'Malaki Starks',
        'position': 'S',
        'from_team': 'Georgia',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 1, Pick 27',
        'contract_years': 4,
        'contract_value': 17200000,
        'guaranteed_money': 17200000,
        'aav': 4300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.2,  # Elite safety prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Future All-Pro
        'impact_score': 2.5,
        'notes': 'Unanimous All-American, projected top-15'
    },
    {
        'player_name': 'Mike Green',
        'position': 'LB',
        'from_team': 'Marshall',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 2, Pick 61',
        'contract_years': 4,
        'contract_value': 8400000,
        'guaranteed_money': 4200000,
        'aav': 2100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Small school star
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Immediate starter
        'impact_score': 1.8,
        'notes': '129 tackles, 12 TFL senior year'
    },
    {
        'player_name': 'Emery Jones Jr.',
        'position': 'OT',
        'from_team': 'LSU',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 3, Pick 91',
        'contract_years': 4,
        'contract_value': 5900000,
        'guaranteed_money': 1300000,
        'aav': 1475000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Swing tackle
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replace Mekari
        'impact_score': 1.2,
    },
    {
        'player_name': 'Teddye Buchanan',
        'position': 'LB',
        'from_team': 'California',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 4, Pick 129',
        'contract_years': 4,
        'contract_value': 4900000,
        'guaranteed_money': 900000,
        'aav': 1225000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 40-inch vertical
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # ST replacement
        'impact_score': 0.8,
    },
    {
        'player_name': 'Carson Vinson',
        'position': 'OT',
        'from_team': 'Alabama A&M',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 5, Pick 141',
        'contract_years': 4,
        'contract_value': 4300000,
        'guaranteed_money': 700000,
        'aav': 1075000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 84 3/8" wingspan
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Bilhal Kone',
        'position': 'CB',
        'from_team': 'Western Michigan',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 6, Pick 178',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 500000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # Slot depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Tyler Loop',
        'position': 'K',
        'from_team': 'Arizona',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 6, Pick 186',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 500000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Tucker succession
        'impact_score': 0.5,
        'notes': 'First kicker Ravens ever drafted'
    },
    {
        'player_name': 'LaJohntay Wester',
        'position': 'WR/KR',
        'from_team': 'Colorado',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 7, Pick 203',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Return specialist
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Aeneas Peebles',
        'position': 'DL',
        'from_team': 'Virginia Tech',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 7, Pick 210',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # 91.2 pass-rush grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Robert Longerbeam',
        'position': 'CB',
        'from_team': 'Rutgers',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 7, Pick 212',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # 4.39 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Garrett Dellinger',
        'position': 'G',
        'from_team': 'LSU',
        'to_team': 'Bal',
        'move_type': '2025 Draft - Round 7, Pick 243',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # 4th LSU OL drafted
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },

    # ========== KEY EXTENSIONS/RE-SIGNINGS - Maintaining core ==========
    {
        'player_name': 'Ronnie Stanley',
        'position': 'LT',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 40000000,
        'aav': 20000000,
        '2024_grade': 8.5,  # Elite LT
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.8,
        'notes': 'Top free agency priority retained'
    },
    {
        'player_name': 'Derrick Henry',
        'position': 'RB',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 30000000,
        'guaranteed_money': 25000000,
        'aav': 15000000,
        '2024_grade': 9.0,  # 1,921 yards, 18 TDs
        'projected_2025_grade': 8.5,  # Age 31
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,
        'notes': 'Shocking extension through age 33'
    },
    {
        'player_name': 'Patrick Ricard',
        'position': 'FB',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2870000,
        'guaranteed_money': 2870000,
        'aav': 2870000,
        '2024_grade': 7.5,  # 5x Pro Bowler
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Tylan Wallace',
        'position': 'WR',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 3000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': "Ar'Darius Washington",
        'position': 'DB',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1400000,
        'guaranteed_money': 700000,
        'aav': 1400000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING CHANGES - Secondary reinforcement ==========
    {
        'player_name': 'Chuck Pagano',
        'position': 'COACH-SEC',
        'from_team': 'RETIRED',
        'to_team': 'Bal',
        'move_type': 'Senior Secondary Coach Hire',
        'contract_years': 2,
        'contract_value': 2000000,
        'guaranteed_money': 1200000,
        'aav': 1000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Former HC/DC
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Fix pass defense
        'impact_score': 1.5,
        'notes': '31st-ranked pass defense in 2024'
    },

    # ========== UNDRAFTED FREE AGENTS - Key additions ==========
    {
        'player_name': 'Jay Higgins',
        'position': 'LB',
        'from_team': 'Iowa',
        'to_team': 'Bal',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2700000,
        'guaranteed_money': 20000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # 295 tackles last 2 years
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
        'notes': '$20K signing bonus leads UDFA class'
    },
    {
        'player_name': 'Jahmal Banks',
        'position': 'WR',
        'from_team': 'Nebraska',
        'to_team': 'Bal',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2700000,
        'guaranteed_money': 10000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # Baltimore native
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },
]

# ========== SUMMARY METRICS ==========
RAVENS_2025_SUMMARY = {
    'total_moves': len(RAVENS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 5,
    'trades': 0,  # Minimal trade activity
    'draft_picks': 11,
    'key_extensions': 5,
    'coaching_hires': 1,
    'udfa_signings': 10,  # Significant UDFA investment
    'total_guaranteed_money': 140000000,  # Estimate
    'dead_money': 18000000,
    'cap_space_remaining': 22000000,
    'cap_space_2026': 85000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B+',
    'key_philosophy': 'Measured aggression within cap constraints',
    'net_impact_score': 18.5,  # Sum of all impact scores
    'division_outlook': 'Clear favorites for third straight title',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'draft_excellence': {
        'starks_value': 'Top-15 talent at #27',
        'green_steal': 'Small school LB gem',
        'defensive_focus': '6 of 11 picks on defense',
        'grade': 'Consensus A- from experts',
    },
    'pass_defense_priority': {
        '2024_rank': '31st in pass defense',
        'pagano_hire': 'Senior secondary coach',
        'cb_additions': 'Alexander, Awuzie depth',
        'draft_emphasis': 'Multiple DBs selected',
    },
    'offensive_continuity': {
        'henry_extension': 'Shocking 2yr/$30M at age 31',
        'hopkins_addition': 'Veteran WR finally',
        'stanley_retention': 'Critical LT kept',
        'run_game_commitment': '182.2 YPG in 2024',
    },
    'compensatory_mastery': {
        '2026_projections': '2 5ths, 1 7th',
        'stephens_departure': '5th round comp',
        'mekari_loss': '5th round comp',
        'formula_exploitation': 'DeCosta expertise',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Lamar Jackson',
        'backup': 'Cooper Rush',
        'grade': 'A',
        'notes': 'MVP entering prime at 28',
    },
    'offensive_line': {
        'starters': ['Ronnie Stanley (LT)', 'Andrew Vorhees (LG)', 
                     'Tyler Linderbaum (C)', 'Kevin Zeitler (RG)', 'Morgan Moses (RT)'],
        'depth': 'Mekari loss hurts versatility',
        'grade': 'B+',
        'notes': 'Stanley extension crucial',
    },
    'skill_positions': {
        'wr': 'Zay Flowers, Rashod Bateman, DeAndre Hopkins',
        'rb': 'Derrick Henry, Keaton Mitchell, Justice Hill',
        'te': 'Mark Andrews, Isaiah Likely',
        'grade': 'A-',
        'notes': 'Hopkins provides veteran presence',
    },
    'defensive_line': {
        'dt': 'Justin Madubuike, Michael Pierce, Travis Jones',
        'edge': 'Odafe Oweh, Kyle Van Noy, David Ojabo',
        'grade': 'B',
        'notes': 'Pass rush needs development',
    },
    'linebackers': {
        'starters': 'Roquan Smith, Mike Green, Trenton Simpson',
        'depth': 'Teddye Buchanan, Jay Higgins',
        'grade': 'A-',
        'notes': 'Green immediate impact expected',
    },
    'secondary': {
        'cb': 'Marlon Humphrey, Nate Wiggins, Jaire Alexander',
        'safety': 'Kyle Hamilton, Marcus Williams, Malaki Starks',
        'grade': 'A',
        'notes': 'Elite if healthy',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 11.5,
        'lean': 'OVER',
        'reasoning': 'Jackson excellence + easy schedule',
    },
    'division_odds': {
        'current': '-140',
        'value': 'YES',
        'reasoning': 'Clear class of division',
    },
    'super_bowl_odds': {
        'current': '+700',
        'value': 'VALUE',
        'reasoning': 'Complete roster',
    },
    'player_props': {
        'jackson_rushing_yards': 'OVER 850',
        'henry_rushing_yards': 'OVER 1,200',
        'flowers_receiving_yards': 'OVER 1,100',
    },
    'key_angles': {
        'best_bet': 'Division winner -140',
        'sleeper': 'Starks DROY +1200',
        'narrative': 'Championship or bust',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("BALTIMORE RAVENS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {RAVENS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{RAVENS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {RAVENS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {RAVENS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {RAVENS_2025_SUMMARY['free_agent_signings']} (limited)")
    print(f"  • Draft Picks: {RAVENS_2025_SUMMARY['draft_picks']} (excellent value)")
    print(f"  • UDFA Signings: {RAVENS_2025_SUMMARY['udfa_signings']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${RAVENS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: ${RAVENS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Space: ${RAVENS_2025_SUMMARY['cap_space_2026']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Malaki Starks (S) - 1st round steal at #27")
    print("  • DeAndre Hopkins (WR) - 1yr/$5M veteran")
    print("  • Jaire Alexander (CB) - 1yr/$6M from Packers")
    print("  • Chuck Pagano - Senior secondary coach")
    
    print("\n❌ KEY LOSSES:")
    print("  • Patrick Mekari (OL) - 3yr/$37.5M to Jaguars")
    print("  • Malik Harrison (LB) - 2yr/$10M to Steelers")
    print("  • Brandon Stephens (CB) - 3yr/$36M to Jets")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {RAVENS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {RAVENS_2025_SUMMARY['division_outlook']}")
    print(f"  • Pass Defense: 31st in 2024, major focus")
    print(f"  • Jackson Window: Age 28, prime years")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 11.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Pass defense improvement essential")
    print("  • Jackson playoff performance")
    print("  • Henry age 31 durability")
    print("  • Nine games vs 2024 playoff teams")

if __name__ == "__main__":
    generate_summary_report()
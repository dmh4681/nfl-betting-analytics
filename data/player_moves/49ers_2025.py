"""
San Francisco 49ers 2025 Offseason Moves
Historic roster transformation: Accepting short-term pain for long-term flexibility
Last Updated: June 23, 2025
"""

NINERS_2025_MOVES = [
    # ========== MAJOR TRADES/RELEASES - Historic roster purge ==========
    {
        'player_name': 'Deebo Samuel',
        'position': 'WR1',
        'from_team': 'SF',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -31500000,  # Dead cap absorbed
        'aav': 0,
        '2024_grade': 6.5,  # Only 670 yards in injury-plagued year
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,  # Disgruntled, wanted out
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Got only a 5th round pick
    },
    {
        'player_name': 'Javon Hargrave',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -19100000,  # Dead cap
        'aav': 0,
        '2024_grade': 5.0,  # Limited to 3 games with injury
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # Cap relief move
    },
    {
        'player_name': 'Kyle Juszczyk',
        'position': 'FB',
        'from_team': 'SF',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -1500000,  # Dead cap
        'aav': 0,
        '2024_grade': 7.0,  # 9x Pro Bowler
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 7.0,  # Shanahan system icon
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,  # End of an era
    },

    # ========== DEFENSIVE EXODUS ==========
    {
        'player_name': 'Charvarius Ward',
        'position': 'CB1',
        'from_team': 'SF',
        'to_team': 'Ind',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Still elite when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Major secondary loss
    },
    {
        'player_name': 'Dre Greenlaw',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Limited by Achilles recovery
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Leadership void
    },
    {
        'player_name': 'Talanoa Hufanga',
        'position': 'S',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Injury-plagued
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Leonard Floyd',
        'position': 'EDGE',
        'from_team': 'SF',
        'to_team': 'Atl',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 6.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'Maliek Collins',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'Cle',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },

    # ========== THE PURDY MEGA-DEAL ==========
    {
        'player_name': 'Brock Purdy',
        'position': 'QB',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Contract Extension',
        'contract_years': 5,
        'contract_value': 265000000,  # Record-setting
        'guaranteed_money': 180000000,  # Fully guaranteed
        'aav': 53000000,
        '2024_grade': 8.5,  # Elite efficiency
        'projected_2025_grade': 8.8,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # Franchise secured
    },

    # ========== OTHER KEY EXTENSIONS ==========
    {
        'player_name': 'Fred Warner',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Contract Extension',
        'contract_years': 5,
        'contract_value': 95000000,
        'guaranteed_money': 56000000,
        'aav': 19000000,
        '2024_grade': 9.5,  # All-Pro
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 98.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 2.5,  # Saves $13M in 2025
    },
    {
        'player_name': 'George Kittle',
        'position': 'TE',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 76000000,
        'guaranteed_money': 40000000,
        'aav': 19000000,
        '2024_grade': 8.8,
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.0,
    },

    # ========== BARGAIN FREE AGENT SIGNINGS ==========
    {
        'player_name': 'Mac Jones',
        'position': 'QB',
        'from_team': 'Jac',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7000000,
        'guaranteed_money': 3500000,
        'aav': 3500000,
        '2024_grade': 5.5,  # Backup role
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # Quality backup
        'impact_score': 0.5,
    },
    {
        'player_name': 'Demarcus Robinson',
        'position': 'WR',
        'from_team': 'LAR',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 9500000,
        'guaranteed_money': 4000000,
        'aav': 4750000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # WR depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Luke Farrell',
        'position': 'TE',
        'from_team': 'Jac',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 20250000,
        'guaranteed_money': 11000000,
        'aav': 6750000,
        '2024_grade': 6.8,  # Blocking TE
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Juszczyk replacement
        'impact_score': 1.0,
    },
    {
        'player_name': 'Andre Dillard',
        'position': 'OT',
        'from_team': 'GB',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # OL depth
        'impact_score': 0.4,
    },
    {
        'player_name': 'Nicholas Petit-Frere',
        'position': 'OT',
        'from_team': 'Ten',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1000000,
        'aav': 2500000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== 2025 NFL DRAFT - Defense-heavy approach ==========
    {
        'player_name': 'Mykel Williams',
        'position': 'EDGE',
        'from_team': 'Georgia',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 1, Pick 11',
        'contract_years': 4,
        'contract_value': 24000000,
        'guaranteed_money': 24000000,
        'aav': 6000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Elite prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Bosa's partner
        'impact_score': 2.0,
    },
    {
        'player_name': 'Alfred Collins',
        'position': 'DT',
        'from_team': 'Texas',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 2, Pick 43',
        'contract_years': 4,
        'contract_value': 8500000,
        'guaranteed_money': 4000000,
        'aav': 2125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 6'6", 332 lbs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Replace Hargrave
        'impact_score': 1.5,
    },
    {
        'player_name': 'Nick Martin',
        'position': 'LB',
        'from_team': 'Oklahoma',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 3, Pick 75',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1400000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replace Greenlaw
        'impact_score': 1.2,
    },
    {
        'player_name': 'Upton Stout',
        'position': 'CB',
        'from_team': 'Western Kentucky',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 4, Pick 107',
        'contract_years': 4,
        'contract_value': 4500000,
        'guaranteed_money': 900000,
        'aav': 1125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Zero TDs allowed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replace Ward
        'impact_score': 1.0,
    },
    {
        'player_name': 'C.J. West',
        'position': 'DT',
        'from_team': 'Kent State',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 5, Pick 143',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Carson Steele',
        'position': 'RB',
        'from_team': 'UCLA',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 6, Pick 181',
        'contract_years': 4,
        'contract_value': 3500000,
        'guaranteed_money': 400000,
        'aav': 875000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Goal-line back
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Justin Rogers',
        'position': 'WR',
        'from_team': 'TCU',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 6, Pick 219',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Tyrek Funderburk',
        'position': 'CB',
        'from_team': 'App State',
        'to_team': 'SF',
        'move_type': '2025 Draft - Round 7, Pick 255',
        'contract_years': 4,
        'contract_value': 3000000,
        'guaranteed_money': 200000,
        'aav': 750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.1,
    },

    # ========== COACHING CHANGES - Saleh returns! ==========
    {
        'player_name': 'Robert Saleh',
        'position': 'COACH-DC',
        'from_team': 'NYJ',
        'to_team': 'SF',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 2000000,
        '2024_grade': 6.0,  # As Jets HC
        'projected_2025_grade': 9.0,  # Elite DC historically
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Critical hire
        'impact_score': 2.5,
    },
    {
        'player_name': 'Klay Kubiak',
        'position': 'COACH-OC',
        'from_team': 'SF-PGC',
        'to_team': 'SF',
        'move_type': 'Internal Promotion to OC',
        'contract_years': 3,
        'contract_value': 4500000,
        'guaranteed_money': 2000000,
        'aav': 1500000,
        '2024_grade': 7.5,  # As pass game coordinator
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Shanahan still calls plays
        'impact_score': 1.0,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Aaron Banks',
        'position': 'G',
        'from_team': 'SF',
        'to_team': 'GB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.3,  # OL depth concern
    },
    {
        'player_name': 'Jordan Mason',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 400+ yards
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== UDFA SIGNINGS ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'SF',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 15000000,  # Combined
        'guaranteed_money': 1500000,
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
]

# ========== SUMMARY METRICS ==========
NINERS_2025_SUMMARY = {
    'total_moves': len(NINERS_2025_MOVES),
    'major_releases_trades': 9,  # Historic roster purge
    'free_agent_signings': 5,
    'draft_picks': 8,
    'key_extensions': 4,
    'coaching_changes': 2,
    'udfa_signings': 1,  # Grouped as one entry
    'total_guaranteed_money': 485000000,  # Includes massive Purdy deal
    'dead_money_absorbed': 86600000,  # League-high, historic
    'salary_cap_space_created': 50000000,  # Current flexibility
    'projected_2027_cap_space': 100000000,  # When dead money clears
    'championship_window': '2026-2029',  # Post-transition
    'offseason_grade': 'B+/A-',  # Bold strategy with risk
    'key_philosophy': 'Accept short-term pain for long-term flexibility',
    'schedule_strength': 0.415,  # NFL's easiest since 2015 Falcons
    'rookie_starters_projected': 6,  # Historic youth movement
    'division_championship_odds': 36,  # Highest in NFC West despite turnover
    'biggest_gamble': 'Six potential rookie starters on defense',
    'smartest_move': 'Robert Saleh return as DC',
    'franchise_trajectory': 'Controlled regression leading to sustainable excellence',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'financial_strategy': {
        'dead_cap_hit': '$86.6M historic hit accepted in 2025',
        'future_flexibility': '$100M+ cap space by 2027',
        'contract_structuring': 'Purdy deal only $9.1M cap hit in 2025',
        'veteran_releases': 'Samuel, Hargrave, Juszczyk save future money',
    },
    'roster_philosophy': {
        'youth_movement': 'First 5 draft picks on defense since 1981',
        'veteran_core': 'Bosa, Warner, Kittle, Williams anchor',
        'offensive_identity': 'Transition from Deebo/fullback era',
        'defensive_rebuild': 'Saleh tasked with developing rookies',
    },
    'schedule_advantage': {
        'strength': '.415 opponent win % (easiest since 2015)',
        'home_games': 'Weak AFC East opponents visit',
        'division_games': 'Seahawks appear weakened',
        'timing': 'Perfect year for transition',
    },
    'coaching_masterstroke': {
        'saleh_return': 'Reunites with system that made him star',
        'kubiak_promotion': 'Offensive continuity maintained',
        'scheme_fit': 'Rookies selected for specific system',
        'development_focus': 'Year dedicated to teaching',
    },
    'division_dynamics': {
        'rams_threat': 'Added Davante Adams, remain favorites',
        'cardinals_rise': 'Defensive additions make them contenders',
        'seahawks_fall': 'Traded Smith/Metcalf, last place likely',
        'opportunity': 'Division more balanced than recent years',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Brock Purdy',
        'backup': 'Mac Jones',
        'grade': 'A',
        'notes': 'Purdy secured long-term, Jones quality backup',
    },
    'offensive_line': {
        'starters': ['Trent Williams (LT)', 'Jon Feliciano (LG)', 'Jake Brendel (C)', 
                     'Spencer Burford (RG)', 'Colton McKivitz (RT)'],
        'depth': 'Banks departure hurts, added Dillard/Petit-Frere',
        'grade': 'B-',
        'notes': 'Williams age 37 a concern, interior questions',
    },
    'skill_positions': {
        'wr': 'Brandon Aiyuk, Jauan Jennings, Demarcus Robinson',
        'rb': 'Christian McCaffrey, Elijah Mitchell, Carson Steele',
        'te': 'George Kittle, Luke Farrell',
        'grade': 'B+',
        'notes': 'Deebo loss significant, CMC health crucial',
    },
    'defensive_line': {
        'dt': 'Alfred Collins, C.J. West, rookie depth',
        'edge': 'Nick Bosa, Mykel Williams, Drake Jackson',
        'grade': 'B',
        'notes': 'Bosa elite but youth everywhere else',
    },
    'linebackers': {
        'starters': 'Fred Warner, Nick Martin (rookie), Dee Winters',
        'depth': 'Thin behind starters',
        'grade': 'B+',
        'notes': 'Warner covers for inexperience',
    },
    'secondary': {
        'cb': 'Deommodore Lenoir, Upton Stout (rookie), Ambry Thomas',
        'safety': 'George Odum, Ji\'Ayir Brown',
        'grade': 'C+',
        'notes': 'Major question marks after exodus',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'UNDER',
        'reasoning': 'Too many rookies on defense',
    },
    'division_odds': {
        'current': '+250',
        'value': 'NO',
        'reasoning': 'Transition year despite easy schedule',
    },
    'super_bowl_odds': {
        'current': '+3500',
        'value': 'HARD PASS',
        'reasoning': 'Not built for 2025 contention',
    },
    'player_props': {
        'purdy_passing_yards': 'OVER 4,200',
        'mccaffrey_rushing_yards': 'UNDER 1,100 (age/usage)',
        'bosa_sacks': 'OVER 15.5',
    },
    'key_angles': {
        'best_bet': 'Miss playoffs +150',
        'fade_spot': 'Early season vs good offenses',
        'narrative': 'Saleh makes defense respectable by December',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("SAN FRANCISCO 49ERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {NINERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: {sum(move['impact_score'] for move in NINERS_2025_MOVES):.1f}")
    print(f"Championship Window: {NINERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {NINERS_2025_SUMMARY['total_moves']}")
    print(f"  • Major Releases/Trades: {NINERS_2025_SUMMARY['major_releases_trades']}")
    print(f"  • Free Agent Signings: {NINERS_2025_SUMMARY['free_agent_signings']} (all budget deals)")
    print(f"  • Draft Picks: {NINERS_2025_SUMMARY['draft_picks']} (defense-heavy)")
    print(f"  • Extensions: {NINERS_2025_SUMMARY['key_extensions']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${NINERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${NINERS_2025_SUMMARY['dead_money_absorbed']:,} (league-high)")
    print(f"  • Current Cap Space: ${NINERS_2025_SUMMARY['salary_cap_space_created']:,}")
    print(f"  • 2027 Projected Space: ${NINERS_2025_SUMMARY['projected_2027_cap_space']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Robert Saleh (DC) - Returns to fix defense")
    print("  • Mykel Williams (EDGE) - 1st round, Georgia")
    print("  • Luke Farrell (TE) - 3yr/$20.25M blocking TE")
    print("  • Mac Jones (QB) - Backup on 2yr/$7M deal")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • Deebo Samuel - Traded to Washington (5th pick)")
    print("  • Javon Hargrave - Released ($19.1M dead cap)")
    print("  • Charvarius Ward - To Colts in FA")
    print("  • Dre Greenlaw, Talanoa Hufanga - Both to Denver")
    print("  • Kyle Juszczyk - 9x Pro Bowl FB released")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {NINERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Schedule: {NINERS_2025_SUMMARY['schedule_strength']} strength (NFL's easiest)")
    print(f"  • Projected Rookie Starters: {NINERS_2025_SUMMARY['rookie_starters_projected']}")
    print(f"  • Division Odds: {NINERS_2025_SUMMARY['division_championship_odds']}% to win")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Can Saleh develop 6 rookie defensive starters?")
    print("  • McCaffrey health at age 29")
    print("  • Trent Williams longevity at 37")
    print("  • Schedule advantage vs roster inexperience")

if __name__ == "__main__":
    generate_summary_report()
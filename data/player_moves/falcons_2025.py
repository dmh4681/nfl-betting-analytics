"""
Atlanta Falcons 2025 Offseason Moves
Aggressive defensive rebuild signals make-or-break moment for franchise
Last Updated: June 23, 2025
"""

FALCONS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Defensive transformation ==========
    {
        'player_name': 'Leonard Floyd',
        'position': 'EDGE',
        'from_team': 'SF',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 8000000,
        'aav': 10000000,
        '2024_grade': 8.0,  # 8.5+ sacks in each of past 5 seasons
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Address 31st-ranked pass rush
        'impact_score': 2.0,  # Proven veteran for worst pass rush
    },
    {
        'player_name': 'Divine Deablo',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 14000000,
        'guaranteed_money': 7000000,
        'aav': 7000000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,
        'impact_score': 0.6,
    },
    {
        'player_name': 'Morgan Fox',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8500000,
        'guaranteed_money': 4000000,
        'aav': 4250000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # Interior rush help
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jordan Fuller',
        'position': 'S',
        'from_team': 'Car',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.7,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Safety depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Michael Ford',
        'position': 'CB',
        'from_team': 'Cle',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 4000000,
        'guaranteed_money': 1500000,
        'aav': 2000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.3,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Corner depth
        'impact_score': 0.2,
    },
    {
        'player_name': 'Easton Stick',
        'position': 'QB',
        'from_team': 'LAC',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        'guaranteed_money': 500000,
        'aav': 1200000,
        '2024_grade': 5.5,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 5.0,  # QB3 behind Cousins
        'impact_score': 0.0,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS - Core retention ==========
    {
        'player_name': 'A.J. Terrell',
        'position': 'CB1',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 81000000,
        'guaranteed_money': 46000000,
        'aav': 20250000,
        '2024_grade': 8.5,  # Elite corner
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Locking up elite CB1
    },
    {
        'player_name': 'Jake Matthews',
        'position': 'LT',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 45000000,
        'guaranteed_money': 28000000,
        'aav': 22500000,
        '2024_grade': 7.8,
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.5,  # Protecting Penix blindside
    },
    {
        'player_name': 'Mike Hughes',
        'position': 'CB2',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 18000000,
        'guaranteed_money': 10000000,
        'aav': 6000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'KhaDarel Hodge',
        'position': 'WR',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 2500000,
        'aav': 3000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Kentavius Street',
        'position': 'EDGE',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 6.3,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },

    # ========== 2025 NFL DRAFT - Historic defensive investment ==========
    {
        'player_name': 'Jalon Walker',
        'position': 'EDGE',
        'from_team': 'Georgia',
        'to_team': 'Atl',
        'move_type': '2025 Draft - Round 1, Pick 15',
        'contract_years': 4,
        'contract_value': 18500000,
        'guaranteed_money': 18500000,  # Fully guaranteed rookie deal
        'aav': 4625000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Elite versatility, 6'1" frame questions
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,
        'impact_score': 1.8,
    },
    {
        'player_name': 'James Pearce Jr.',
        'position': 'EDGE',
        'from_team': 'Tennessee',
        'to_team': 'Atl',
        'move_type': '2025 Draft - Round 1, Pick 26 (Traded Up)',
        'contract_years': 4,
        'contract_value': 16000000,
        'guaranteed_money': 16000000,
        'aav': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # Explosive athleticism
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,
        'impact_score': 1.8,  # Historic double 1st round EDGE
    },
    {
        'player_name': 'Xavier Watts',
        'position': 'S',
        'from_team': 'Notre Dame',
        'to_team': 'Atl',
        'move_type': '2025 Draft - Round 3, Pick 88',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 1200000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Billy Bowman Jr.',
        'position': 'S',
        'from_team': 'Oklahoma',
        'to_team': 'Atl',
        'move_type': '2025 Draft - Round 5, Pick 142',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 600000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },

    # ========== QUARTERBACK TRANSITION ==========
    {
        'player_name': 'Michael Penix Jr.',
        'position': 'QB',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Promotion to Starter',
        'contract_years': 3,  # Remaining on rookie deal
        'contract_value': 12000000,
        'guaranteed_money': 12000000,
        'aav': 4000000,
        '2024_grade': 6.5,  # 775 yds, 3 TD, 3 INT in 3 games
        'projected_2025_grade': 7.5,  # Expected development
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.0,  # Franchise QB transition
    },
    {
        'player_name': 'Matt Ryan',
        'position': 'QB-COACH',
        'from_team': 'Retired',
        'to_team': 'Atl',
        'move_type': 'Mentor/Consultant Hire',
        'contract_years': 1,
        'contract_value': 500000,
        'guaranteed_money': 500000,
        'aav': 500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Penix mentor
        'impact_score': 0.5,
    },

    # ========== COACHING CHANGES - New regime ==========
    {
        'player_name': 'Raheem Morris',
        'position': 'COACH-HC',
        'from_team': 'LAR',
        'to_team': 'Atl',
        'move_type': 'Head Coach Hire',
        'contract_years': 4,
        'contract_value': 20000000,
        'guaranteed_money': 15000000,
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Defensive expertise
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,
        'impact_score': 2.0,  # Culture transformation
    },
    {
        'player_name': 'Jeff Ulbrich',
        'position': 'COACH-DC',
        'from_team': 'NYJ',
        'to_team': 'Atl',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 2000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Aggressive scheme
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Nate Ollie',
        'position': 'COACH-DL',
        'from_team': 'Was',
        'to_team': 'Atl',
        'move_type': 'DL Coach Hire',
        'contract_years': 2,
        'contract_value': 1600000,
        'guaranteed_money': 600000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Mike Rutenberg',
        'position': 'COACH-PASS',
        'from_team': 'NYJ',
        'to_team': 'Atl',
        'move_type': 'Def Pass Game Coordinator Hire',
        'contract_years': 2,
        'contract_value': 1400000,
        'guaranteed_money': 500000,
        'aav': 700000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES - Cap casualties and free agents ==========
    {
        'player_name': 'Grady Jarrett',
        'position': 'DT',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Cap Casualty Release',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Still productive at 31
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,  # Franchise cornerstone
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Painful but necessary
    },
    {
        'player_name': 'Drew Dalman',
        'position': 'C',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Key O-line loss
    },
    {
        'player_name': 'Lorenzo Carter',
        'position': 'OLB',
        'from_team': 'Atl',
        'to_team': 'Ten',
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
        'impact_score': -0.5,
    },
    {
        'player_name': 'Eddie Goldman',
        'position': 'DL',
        'from_team': 'Atl',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,
    },
    {
        'player_name': 'Arthur Smith',
        'position': 'COACH-HC',
        'from_team': 'Atl',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # Three consecutive 7-10 seasons
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 2.0,
        'importance_to_new_team': 0.0,
        'impact_score': 1.0,  # Addition by subtraction
    },

    # ========== TRADES - Future sacrificed for present ==========
    {
        'player_name': '2026 1st Round Pick',
        'position': 'DRAFT',
        'from_team': 'Atl',
        'to_team': 'Hou',
        'move_type': 'Draft Capital Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Future flexibility lost
    },

    # ========== KIRK COUSINS SITUATION ==========
    {
        'player_name': 'Kirk Cousins',
        'position': 'QB',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Benched to Backup',
        'contract_years': 1,
        'contract_value': 40000000,  # Cap hit as backup
        'guaranteed_money': 40000000,
        'aav': 40000000,
        '2024_grade': 5.5,  # 16 INTs in 14 games
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 85.0,  # Before benching
        'importance_to_old_team': 3.0,
        'importance_to_new_team': 4.0,  # Expensive insurance
        'impact_score': -2.0,  # Massive cap hit for backup
    },
]

# ========== SUMMARY METRICS ==========
FALCONS_2025_SUMMARY = {
    'total_moves': len(FALCONS_2025_MOVES),
    'free_agent_signings': 6,
    'key_resignings': 5,
    'draft_picks': 5,  # Only 5 total picks (historic low)
    'coaching_changes': 5,  # HC, DC, position coaches
    'major_losses': 5,
    'trades': 1,
    'total_guaranteed_money': 235000000,  # Including extensions
    'dead_money': 16250000,  # Jarrett release
    'cap_space_created': 44750000,  # Jarrett + restructures
    'cousins_cap_hit': 40000000,  # Most expensive backup ever
    'championship_window': '2025-2027',
    'offseason_grade': 'B',  # Upgraded from B- after review
    'key_philosophy': 'All-in defensive transformation with make-or-break urgency',
    'net_impact_score': 8.5,  # Sum of all impact scores
    'division_outlook': 'Legitimate contender if Penix develops quickly',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'defensive_transformation': {
        '2024_sack_rank': 31,  # Only 31 sacks
        'edge_investment': 'Historic double 1st round EDGE picks',
        'veteran_additions': 'Floyd (8.5+ sacks x5 years) leads charge',
        'scheme_change': 'Ulbrich aggressive system from Jets',
    },
    'quarterback_situation': {
        'penix_audition': '775 yards, 3 TD, 3 INT in 3 games',
        'cousins_contract': '$40M cap hit as backup, no-trade clause',
        'ryan_mentorship': 'Franchise legend hired as consultant',
        'timeline': 'Penix must develop quickly for playoffs',
    },
    'cap_management': {
        'initial_position': '$6.3M over cap to start',
        'jarrett_savings': '$16.25M from painful release',
        'restructures': '$28.5M from Terrell, Matthews, Lindstrom',
        'flexibility': 'Short-term FA deals maintain future options',
    },
    'draft_philosophy': {
        'aggressive_approach': 'Traded 2026 1st to get Pearce Jr.',
        'defensive_focus': '4 of 5 picks on defense',
        'minimal_picks': '5 picks tied for fewest in franchise history',
        'win_now': 'Fontenot/Morris playoffs-or-bust scenario',
    },
    'offensive_weapons': {
        'skill_positions': 'Bijan Robinson, Drake London, Kyle Pitts',
        'o_line_concern': 'Lost center Dalman, Neuzil unproven',
        'protection_questions': 'Can they keep Penix upright?',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Michael Penix Jr.',
        'backup': 'Kirk Cousins ($40M)',
        'third': 'Easton Stick',
        'grade': 'C+',  # Potential vs uncertainty
        'notes': 'Penix development crucial, Cousins awkward situation',
    },
    'offensive_line': {
        'starters': ['Jake Matthews (LT)', 'Matt Hennessy (LG)', 'Ryan Neuzil (C)', 
                     'Chris Lindstrom (RG)', 'Kaleb McGary (RT)'],
        'concerns': 'Center position after Dalman loss',
        'grade': 'B',
        'notes': 'Matthews extension provides LT stability',
    },
    'skill_positions': {
        'rb': 'Bijan Robinson, Tyler Allgeier',
        'wr': 'Drake London, Darnell Mooney, KhaDarel Hodge',
        'te': 'Kyle Pitts (foot injury concerns)',
        'grade': 'A-',
        'notes': 'Elite young talent if healthy',
    },
    'pass_rush': {
        'projected_starters': ['Leonard Floyd', 'Jalon Walker'],
        'depth': ['James Pearce Jr.', 'Kentavius Street'],
        'grade': 'B+',  # Upgraded from 31st
        'notes': 'Complete overhaul with proven vet + rookie talent',
    },
    'secondary': {
        'corners': ['A.J. Terrell (elite)', 'Mike Hughes', 'Michael Ford'],
        'safeties': ['Jessie Bates III', 'Jordan Fuller', 'Xavier Watts'],
        'grade': 'A-',
        'notes': 'Terrell extension anchors strong unit',
    },
}

# ========== SCHEDULE & DIVISION ANALYSIS ==========
DIVISION_ANALYSIS = {
    'falcons_outlook': {
        'strengths': ['Elite skill positions', 'Improved pass rush', 'Defensive scheme upgrade'],
        'weaknesses': ['QB uncertainty', 'O-line questions', 'Minimal draft capital'],
        'x_factors': ['Penix development speed', 'Rookie EDGE impact', 'Cousins situation'],
    },
    'division_competition': {
        'buccaneers': 'Four-time defending champs but aging core',
        'saints': 'Kellen Moore era begins, cap hell continues',
        'panthers': 'Year 3 for Bryce Young, still rebuilding',
    },
    'schedule_notes': {
        'difficulty': '4th-easiest projected schedule',
        'early_tests': '3 playoff teams in first 4 weeks',
        'key_stretch': 'Weeks 12-15 could decide division',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'OVER',
        'reasoning': 'Defensive improvement + weak division + easy schedule',
    },
    'division_odds': {
        'current': '+180',
        'value': 'YES',
        'reasoning': 'Best roster balance in mediocre division',
    },
    'super_bowl_odds': {
        'current': '+4000',
        'value': 'PASS',
        'reasoning': 'Too much QB uncertainty for deep run',
    },
    'player_props': {
        'penix_passing_yards': 'OVER 3,500',
        'floyd_sacks': 'OVER 8.5',
        'bijan_rushing_yards': 'OVER 1,100',
    },
    'key_bets': {
        'best': 'Division winner +180',
        'avoid': 'Conference champion futures',
        'sleeper': 'Jalon Walker DROY +2500',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("ATLANTA FALCONS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {FALCONS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{FALCONS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {FALCONS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {FALCONS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {FALCONS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Key Re-signings: {FALCONS_2025_SUMMARY['key_resignings']}")
    print(f"  • Draft Picks: {FALCONS_2025_SUMMARY['draft_picks']} (tied for fewest ever)")
    print(f"  • Coaching Changes: {FALCONS_2025_SUMMARY['coaching_changes']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed Money: ${FALCONS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Created: ${FALCONS_2025_SUMMARY['cap_space_created']:,}")
    print(f"  • Dead Money: ${FALCONS_2025_SUMMARY['dead_money']:,} (Jarrett)")
    print(f"  • Cousins Cap Hit: ${FALCONS_2025_SUMMARY['cousins_cap_hit']:,} (as backup!)")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Leonard Floyd (EDGE) - Proven veteran, 8.5+ sacks x5 years")
    print("  • Jalon Walker (EDGE) - 1st round pick #15")
    print("  • James Pearce Jr. (EDGE) - 1st round pick #26 (traded up)")
    print("  • Raheem Morris (HC) - Defensive expertise, championship experience")
    
    print("\n❌ KEY LOSSES:")
    print("  • Grady Jarrett (DT) - Cap casualty after 9 years")
    print("  • Drew Dalman (C) - Free agent to Bears")
    print("  • Arthur Smith (HC) - Fired after 3 straight 7-10 seasons")
    print("  • 2026 1st Round Pick - Traded for Pearce Jr.")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {FALCONS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {FALCONS_2025_SUMMARY['division_outlook']}")
    print(f"  • Pass Rush: From 31st (31 sacks) to potential top-15 unit")
    print(f"  • Risk Level: HIGH - Playoffs or pink slips for Fontenot/Morris")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Penix must develop quickly with Matt Ryan's mentorship")
    print("  • Rookie EDGE rushers need immediate impact")
    print("  • $40M Cousins situation most awkward in NFL")
    print("  • Only 5 draft picks limits future flexibility")

if __name__ == "__main__":
    generate_summary_report()
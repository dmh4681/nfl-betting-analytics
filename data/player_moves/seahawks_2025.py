"""
Seattle Seahawks 2025 Offseason Moves
Dramatic philosophical pivot: Trading franchise cornerstones for run-heavy identity
Last Updated: June 23, 2025
"""

SEAHAWKS_2025_MOVES = [
    # ========== FRANCHISE-ALTERING TRADES ==========
    {
        'player_name': 'Geno Smith',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'LV',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # 4,320 yards, Pro Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.0,  # Franchise QB
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # Got 3rd round pick
    },
    {
        'player_name': 'DK Metcalf',
        'position': 'WR1',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.2,  # Elite receiver
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.5,  # Franchise WR
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,  # Got 2nd + 7th
    },
    {
        'player_name': 'Sam Howell',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Backup
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 10.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },

    # ========== MAJOR RELEASES ==========
    {
        'player_name': 'Tyler Lockett',
        'position': 'WR',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -3100000,  # Dead cap
        'aav': 0,
        '2024_grade': 8.0,  # 10-year franchise icon
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 9.0,  # 910 catches, 8,779 yards
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Saved $31M
    },
    {
        'player_name': 'Dre\'Mont Jones',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -5000000,  # Dead cap
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'Roy Robertson-Harris',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -2000000,  # Dead cap
        'aav': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Rayshawn Jenkins',
        'position': 'S',
        'from_team': 'Sea',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -1500000,  # Dead cap
        'aav': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },

    # ========== KEY SIGNINGS - New identity ==========
    {
        'player_name': 'Sam Darnold',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 100500000,
        'guaranteed_money': 55000000,
        'aav': 33500000,
        '2024_grade': 8.5,  # 4,319 yards, 35 TDs, Pro Bowl
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.5,  # Franchise QB
        'impact_score': 3.0,  # Reunites with Kubiak
    },
    {
        'player_name': 'Cooper Kupp',
        'position': 'WR1',
        'from_team': 'LAR',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 45000000,
        'guaranteed_money': 17500000,
        'aav': 15000000,
        '2024_grade': 6.5,  # Injury-limited
        'projected_2025_grade': 7.5,  # Yakima native
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Replace Metcalf/Lockett
        'impact_score': 2.2,
    },
    {
        'player_name': 'DeMarcus Lawrence',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 42000000,
        'guaranteed_money': 25000000,
        'aav': 14000000,
        '2024_grade': 6.0,  # Limited to 4 games
        'projected_2025_grade': 7.5,  # Bounce-back potential
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Veteran pass rush
        'impact_score': 1.8,
    },
    {
        'player_name': 'Marquez Valdes-Scantling',
        'position': 'WR',
        'from_team': 'KC',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        'guaranteed_money': 2000000,
        'aav': 4000000,
        '2024_grade': 6.2,  # Deep threat
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.0,  # Reunites with Kubiak
        'impact_score': 0.8,
    },
    {
        'player_name': 'Josh Jones',
        'position': 'OL',
        'from_team': 'Ari',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4750000,
        'guaranteed_money': 2500000,
        'aav': 4750000,
        '2024_grade': 6.5,  # Versatile OL
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # OL depth crucial
        'impact_score': 0.8,
    },
    {
        'player_name': 'Drew Lock',
        'position': 'QB',
        'from_team': 'NYG',
        'to_team': 'Sea',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        'guaranteed_money': 2500000,
        'aav': 2500000,
        '2024_grade': 6.0,  # Returns to Seattle
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.5,  # Backup QB
        'impact_score': 0.5,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Ernest Jones IV',
        'position': 'LB',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 33000000,
        'guaranteed_money': 15000000,
        'aav': 11000000,
        '2024_grade': 8.5,  # 94 tackles in 10 games
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Critical retention
    },
    {
        'player_name': 'Jarran Reed',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 25000000,
        'guaranteed_money': 10000000,
        'aav': 12500000,
        '2024_grade': 7.5,  # Last Legion of Boom player
        'projected_2025_grade': 7.3,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Josh Jobe',
        'position': 'CB',
        'from_team': 'Sea',
        'to_team': 'Sea',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 7.2,  # Breakout season
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,
        'impact_score': 1.2,
    },

    # ========== 2025 NFL DRAFT - Offensive rebuild ==========
    {
        'player_name': 'Grey Zabel',
        'position': 'G',
        'from_team': 'North Dakota State',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 1, Pick 18',
        'contract_years': 4,
        'contract_value': 18000000,
        'guaranteed_money': 18000000,
        'aav': 4500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Consensus All-American
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Immediate starter
        'impact_score': 2.0,
    },
    {
        'player_name': 'Nick Emmanwori',
        'position': 'S',
        'from_team': 'South Carolina',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 2, Pick 35 (via trade)',
        'contract_years': 4,
        'contract_value': 9200000,
        'guaranteed_money': 4600000,
        'aav': 2300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # Kam Chancellor comp
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Macdonald system fit
        'impact_score': 1.8,
    },
    {
        'player_name': 'Elijah Arroyo',
        'position': 'TE',
        'from_team': 'Miami',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 2, Pick 50',
        'contract_years': 4,
        'contract_value': 7800000,
        'guaranteed_money': 3900000,
        'aav': 1950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 16.9 YPR led FBS TEs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Run game fit
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jalen Milroe',
        'position': 'QB',
        'from_team': 'Alabama',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 3, Pick 92',
        'contract_years': 4,
        'contract_value': 5600000,
        'guaranteed_money': 1200000,
        'aav': 1400000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Dual-threat, 726 rush yards
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Future development
        'impact_score': 1.0,
    },
    {
        'player_name': 'Tory Horton',
        'position': 'WR',
        'from_team': 'Colorado State',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 5, Pick 166',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Lockett-like speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Robbie Ouzts',
        'position': 'FB',
        'from_team': 'Alabama',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 5, Pick 175',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 500000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # 275-lb lead blocker
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Run-heavy scheme
        'impact_score': 0.6,
    },
    {
        'player_name': 'Damien Martinez',
        'position': 'RB',
        'from_team': 'Miami',
        'to_team': 'Sea',
        'move_type': '2025 Draft - Round 7, Pick 223',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # "Beast Mode 2.0"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING CHANGES - Major overhaul ==========
    {
        'player_name': 'Ryan Grubb',
        'position': 'COACH-OC',
        'from_team': 'Sea',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Philosophical differences
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Addition by subtraction
    },
    {
        'player_name': 'Klint Kubiak',
        'position': 'COACH-OC',
        'from_team': 'NO',
        'to_team': 'Sea',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 4500000,
        'guaranteed_money': 2500000,
        'aav': 1500000,
        '2024_grade': 8.0,  # Saints offense success
        'projected_2025_grade': 8.5,  # Darnold connection
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Critical hire
        'impact_score': 2.0,
    },
    {
        'player_name': 'Ryan Paganetti',
        'position': 'COACH-RGC',
        'from_team': 'Cin',
        'to_team': 'Sea',
        'move_type': 'Run Game Coordinator Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        'guaranteed_money': 900000,
        'aav': 900000,
        '2024_grade': 7.5,  # Bengals run game
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Run-heavy focus
        'impact_score': 1.5,
    },
    {
        'player_name': 'Steve Bono',
        'position': 'COACH-QB',
        'from_team': 'Det',
        'to_team': 'Sea',
        'move_type': 'QB Coach Hire',
        'contract_years': 2,
        'contract_value': 1200000,
        'guaranteed_money': 600000,
        'aav': 600000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Darnold development
        'impact_score': 1.0,
    },

    # ========== OTHER LOSSES ==========
    {
        'player_name': 'Laken Tomlinson',
        'position': 'G',
        'from_team': 'Sea',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'Tre Brown',
        'position': 'CB',
        'from_team': 'Sea',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== UDFA SIGNINGS ==========
    {
        'player_name': 'Multiple Defensive UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Sea',
        'move_type': 'UDFA Signings (11 defensive players)',
        'contract_years': 3,
        'contract_value': 15000000,  # Combined
        'guaranteed_money': 1500000,
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Balances offense-heavy draft
        'impact_score': 0.5,
    },
]

# ========== SUMMARY METRICS ==========
SEAHAWKS_2025_SUMMARY = {
    'total_moves': len(SEAHAWKS_2025_MOVES),
    'major_trades': 3,  # Smith, Metcalf, Howell
    'major_releases': 4,  # Lockett, Jones, Robertson-Harris, Jenkins
    'free_agent_signings': 10,
    'free_agent_losses': 6,
    'draft_picks': 9,
    'key_resignings': 6,
    'coaching_changes': 4,  # 1 firing, 3 hires
    'udfa_signings': 1,  # Grouped as one entry
    'total_guaranteed_money': 325000000,  # Includes major signings
    'cap_space_created': 50000000,  # From trades and releases
    'salary_cap_space_remaining': 30000000,  # Current flexibility
    'championship_window': '2026-2028',  # Post-transition
    'offseason_grade': 'B',  # Bold strategy with significant risk
    'key_philosophy': 'Pivot toward run-heavy identity in dramatic offseason overhaul',
    'offensive_line_ranking': 8,  # PFF ranking after improvements
    'win_total_projection': 8.5,  # Down from 10 in 2024
    'playoff_odds': 45,  # Moderate due to NFC West competition
    'biggest_gamble': 'Trading franchise cornerstones Smith and Metcalf',
    'smartest_move': 'Ernest Jones extension (critical defensive retention)',
    'critical_success_factor': 'Offensive line protection improvement',
    'nfc_west_standing': 'Unanimous last-place predictions after moves',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'quarterback_transition': {
        'smith_trade': 'Saved $31M cap space, got 3rd pick',
        'darnold_signing': '3yr/$100.5M reunites with Kubiak',
        'contract_dispute': 'Smith wanted $45M+ annually',
        'timeline': 'Darnold bridge to Milroe development',
    },
    'receiving_corps_overhaul': {
        'metcalf_trade': '2nd + 7th picks, sought $30M AAV',
        'lockett_release': 'Ended 10-year tenure, saved $31M',
        'kupp_addition': 'Yakima native returns home',
        'philosophy': 'Shift from explosive to possession',
    },
    'offensive_line_focus': {
        'zabel_selection': '1st round guard, immediate starter',
        'jones_signing': 'Versatile depth across positions',
        'scheme_change': 'Zone-heavy run blocking emphasis',
        'protection_priority': 'Address 2024 weakness',
    },
    'coaching_overhaul': {
        'grubb_firing': 'Philosophical differences with Macdonald',
        'kubiak_hire': 'Run-heavy West Coast principles',
        'paganetti_addition': 'Dedicated run game coordinator',
        'identity_shift': 'From pass-heavy to ground control',
    },
    'defensive_continuity': {
        'jones_extension': 'Critical retention at LB',
        'reed_extension': 'Veteran DT presence',
        'emmanwori_draft': 'Kam Chancellor-style safety',
        'youth_balance': '11 defensive UDFAs added',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Sam Darnold',
        'backup': 'Drew Lock',
        'developmental': 'Jalen Milroe',
        'grade': 'B+',
        'notes': 'Darnold career year continues? Lock familiar with system',
    },
    'offensive_line': {
        'starters': ['Charles Cross (LT)', 'Grey Zabel (LG)', 'Olu Oluwatimi (C)', 
                     'Anthony Bradford (RG)', 'Abraham Lucas (RT)'],
        'depth': 'Josh Jones provides swing tackle ability',
        'grade': 'B',
        'notes': 'Zabel immediate upgrade, Lucas health crucial',
    },
    'skill_positions': {
        'wr': 'Cooper Kupp, Jaxon Smith-Njigba, Marquez Valdes-Scantling',
        'rb': 'Kenneth Walker III, Zach Charbonnet, Damien Martinez',
        'te': 'Noah Fant, Elijah Arroyo',
        'grade': 'B-',
        'notes': 'Kupp health key, JSN must step up',
    },
    'defensive_line': {
        'dt': 'Jarran Reed, Byron Murphy II',
        'edge': 'DeMarcus Lawrence, Boye Mafe, Derick Hall',
        'grade': 'B+',
        'notes': 'Lawrence bounce-back crucial',
    },
    'linebackers': {
        'starters': 'Ernest Jones IV, Tyrel Dodson, Jerome Baker',
        'depth': 'Adequate with UDFA additions',
        'grade': 'A-',
        'notes': 'Jones anchors elite unit',
    },
    'secondary': {
        'cb': 'Devon Witherspoon, Josh Jobe, Riq Woolen',
        'safety': 'Julian Love, Nick Emmanwori',
        'grade': 'B+',
        'notes': 'Witherspoon elite, Emmanwori high upside',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'UNDER',
        'reasoning': 'Major roster turnover, tough division',
    },
    'division_odds': {
        'current': '+850',
        'value': 'NO',
        'reasoning': 'Clear 4th in loaded NFC West',
    },
    'futures': {
        'playoffs': 'NO (-250)',
        'last_place': 'YES (-150)',
        'coach_fired': 'NO (Macdonald safe Year 2)',
    },
    'player_props': {
        'darnold_passing_yards': 'UNDER 4,000',
        'kupp_receiving_yards': 'OVER 850 if healthy',
        'walker_rushing_yards': 'OVER 1,100',
    },
    'best_bets': {
        'season': 'Under 8.5 wins',
        'narrative': 'Run-heavy keeps games close',
        'avoid': 'Division winner futures',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("SEATTLE SEAHAWKS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {SEAHAWKS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: {sum(move['impact_score'] for move in SEAHAWKS_2025_MOVES):.1f}")
    print(f"Championship Window: {SEAHAWKS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {SEAHAWKS_2025_SUMMARY['total_moves']}")
    print(f"  • Major Trades: {SEAHAWKS_2025_SUMMARY['major_trades']} (Smith, Metcalf out)")
    print(f"  • Major Releases: {SEAHAWKS_2025_SUMMARY['major_releases']}")
    print(f"  • Free Agent Signings: {SEAHAWKS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Draft Picks: {SEAHAWKS_2025_SUMMARY['draft_picks']} (7 offensive)")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${SEAHAWKS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Created: ${SEAHAWKS_2025_SUMMARY['cap_space_created']:,}")
    print(f"  • Current Cap Space: ${SEAHAWKS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Sam Darnold (QB) - 3yr/$100.5M reunion with Kubiak")
    print("  • Cooper Kupp (WR) - 3yr/$45M Yakima native returns")
    print("  • DeMarcus Lawrence (EDGE) - 3yr/$42M veteran")
    print("  • Klint Kubiak (OC) - Run-heavy philosophy")
    
    print("\n❌ SHOCKING DEPARTURES:")
    print("  • Geno Smith - Traded to Raiders (3rd pick)")
    print("  • DK Metcalf - Traded to Steelers (2nd + 7th)")
    print("  • Tyler Lockett - Released after 10 years")
    print("  • Ryan Grubb (OC) - Fired after one season")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {SEAHAWKS_2025_SUMMARY['key_philosophy']}")
    print(f"  • OL Ranking: #{SEAHAWKS_2025_SUMMARY['offensive_line_ranking']} (PFF)")
    print(f"  • Win Projection: {SEAHAWKS_2025_SUMMARY['win_total_projection']} games")
    print(f"  • Division Standing: {SEAHAWKS_2025_SUMMARY['nfc_west_standing']}")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['best_bets']['season']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Can Darnold maintain 2024 form?")
    print("  • Kupp health after injury issues")
    print("  • OL improvements translate to protection?")
    print("  • Fan reaction to trading franchise icons")

if __name__ == "__main__":
    generate_summary_report()
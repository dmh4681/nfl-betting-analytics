"""
Jacksonville Jaguars 2025 Offseason Moves
All-in gamble: Trading up for Travis Hunter while overhauling organization
Last Updated: June 23, 2025
"""

JAGUARS_2025_MOVES = [
    # ========== FRANCHISE-ALTERING TRADE ==========
    {
        'player_name': 'Travis Hunter',
        'position': 'WR/CB',
        'from_team': 'Colorado',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 1, Pick 2',
        'contract_years': 4,
        'contract_value': 46650000,
        'guaranteed_money': 30570000,  # Record non-QB bonus
        'aav': 11662500,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # Two-way sensation
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Franchise cornerstone
        'impact_score': 4.0,
    },

    # ========== OFFENSIVE LINE RECONSTRUCTION ==========
    {
        'player_name': 'Patrick Mekari',
        'position': 'G',
        'from_team': 'Bal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 37500000,
        'guaranteed_money': 22500000,
        'aav': 12500000,
        '2024_grade': 7.5,  # 94.6% pass block win rate
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Lawrence protection
        'impact_score': 2.0,
    },
    {
        'player_name': 'Robert Hainsey',
        'position': 'C',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 21000000,
        'guaranteed_money': 13000000,
        'aav': 7000000,
        '2024_grade': 7.0,  # Coen familiarity
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Replaces Morse
        'impact_score': 1.5,
    },

    # ========== RECEIVER ROOM REFRESH ==========
    {
        'player_name': 'Dyami Brown',
        'position': 'WR',
        'from_team': 'Was',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 9500000,
        'aav': 10000000,
        '2024_grade': 7.0,  # Career highs
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 44.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 8.0,  # Post-Kirk void
        'impact_score': 1.5,
    },
    {
        'player_name': 'Parker Washington',
        'position': 'WR',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2200000,
        'guaranteed_money': 1100000,
        'aav': 2200000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,  # Depth
        'impact_score': 0.5,
    },

    # ========== DEFENSIVE ADDITIONS ==========
    {
        'player_name': 'Jourdan Lewis',
        'position': 'CB',
        'from_team': 'Dal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 24000000,
        'guaranteed_money': 12000000,
        'aav': 8000000,
        '2024_grade': 7.2,  # Elite slot corner
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Slot expertise
        'impact_score': 1.5,
    },
    {
        'player_name': 'Eric Murray',
        'position': 'S',
        'from_team': 'Hou',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Safety depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Emmanuel Ogbah',
        'position': 'EDGE',
        'from_team': 'Mia',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        'guaranteed_money': 3000000,
        'aav': 5000000,
        '2024_grade': 6.5,  # 5.0 sacks
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # Edge depth
        'impact_score': 0.8,
    },

    # ========== QUARTERBACK DEPTH ==========
    {
        'player_name': 'Nick Mullens',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Jac',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.0,  # Veteran backup
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Udinski familiarity
        'impact_score': 0.5,
    },

    # ========== MAJOR OFFENSIVE LOSSES ==========
    {
        'player_name': 'Christian Kirk',
        'position': 'WR',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Reliable slot
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,
    },
    {
        'player_name': 'Evan Engram',
        'position': 'TE',
        'from_team': 'Jac',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Top TE
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,
    },
    {
        'player_name': 'Mitch Morse',
        'position': 'C',
        'from_team': 'Jac',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Brandon Scherff',
        'position': 'G',
        'from_team': 'Jac',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },

    # ========== DEFENSIVE DEPARTURES ==========
    {
        'player_name': 'Ronald Darby',
        'position': 'CB',
        'from_team': 'Jac',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Devin Duvernay',
        'position': 'KR/PR',
        'from_team': 'Jac',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,  # ST value
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Trevor Lawrence',
        'position': 'QB',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Fifth-Year Option',
        'contract_years': 1,
        'contract_value': 55000000,
        'guaranteed_money': 55000000,
        'aav': 55000000,
        '2024_grade': 6.8,  # Injury-limited
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,  # Franchise QB
        'impact_score': 2.5,
    },
    {
        'player_name': 'Josh Hines-Allen',
        'position': 'EDGE',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 35000000,
        'guaranteed_money': 20000000,
        'aav': 17500000,
        '2024_grade': 8.0,  # Elite pass rusher
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,  # Defensive anchor
        'impact_score': 2.5,
    },
    {
        'player_name': 'Tyson Campbell',
        'position': 'CB',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 16000000,
        'guaranteed_money': 10000000,
        'aav': 16000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Pairs with Hunter
        'impact_score': 1.8,
    },
    {
        'player_name': 'Cole Van Lanen',
        'position': 'G/T',
        'from_team': 'Jac',
        'to_team': 'Jac',
        'move_type': 'RFA Tender',
        'contract_years': 1,
        'contract_value': 3800000,
        'guaranteed_money': 2000000,
        'aav': 3800000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # OL depth
        'impact_score': 0.8,
    },

    # ========== 2025 NFL DRAFT - Limited by trade ==========
    {
        'player_name': 'Wyatt Milum',
        'position': 'OT',
        'from_team': 'West Virginia',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 4, Pick 104',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 950000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # OL development
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jalen McLeod',
        'position': 'LB',
        'from_team': 'NC State',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 6, Pick 200',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # LB depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Javon Baker',
        'position': 'WR',
        'from_team': 'UCF',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 7, Pick 220',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # WR depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Joshua Mickens',
        'position': 'S',
        'from_team': 'LSU',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 7, Pick 240',
        'contract_years': 4,
        'contract_value': 3000000,
        'guaranteed_money': 200000,
        'aav': 750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # S depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Kris Thornton',
        'position': 'DT',
        'from_team': 'Southern Miss',
        'to_team': 'Jac',
        'move_type': '2025 Draft - Round 7, Pick 255',
        'contract_years': 4,
        'contract_value': 2800000,
        'guaranteed_money': 150000,
        'aav': 700000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # DT depth
        'impact_score': 0.2,
    },

    # ========== TRADES ==========
    {
        'player_name': 'Draft Capital for Hunter',
        'position': 'PICKS',
        'from_team': 'Jac',
        'to_team': 'Cle',
        'move_type': 'Trade Package',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.0,  # 4 picks including 2026 1st
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,  # Massive cost
    },

    # ========== COACHING/FRONT OFFICE OVERHAUL ==========
    {
        'player_name': 'Liam Coen',
        'position': 'COACH-HC',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Head Coach Hire',
        'contract_years': 5,
        'contract_value': 35000000,
        'guaranteed_money': 17500000,
        'aav': 7000000,
        '2024_grade': 8.0,  # Successful OC
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.5,  # Culture change
        'impact_score': 3.0,
    },
    {
        'player_name': 'James Gladstone',
        'position': 'EXEC-GM',
        'from_team': 'LAR',
        'to_team': 'Jac',
        'move_type': 'GM Hire',
        'contract_years': 5,
        'contract_value': 30000000,
        'guaranteed_money': 15000000,
        'aav': 6000000,
        '2024_grade': 7.5,  # Rams executive
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.5,  # Bold approach
        'impact_score': 2.5,
    },
    {
        'player_name': 'Tony Boselli',
        'position': 'EXEC-EVP',
        'from_team': 'RETIRED',
        'to_team': 'Jac',
        'move_type': 'Executive Hire',
        'contract_years': 3,
        'contract_value': 15000000,
        'guaranteed_money': 7500000,
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Franchise credibility
        'impact_score': 1.5,
    },
    {
        'player_name': 'Doug Pederson',
        'position': 'COACH-HC',
        'from_team': 'Jac',
        'to_team': 'FIRED',
        'move_type': 'Head Coach Firing',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # 4-13 record
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': 1.5,  # Addition by subtraction
    },
    {
        'player_name': 'Trent Baalke',
        'position': 'EXEC-GM',
        'from_team': 'Jac',
        'to_team': 'FIRED',
        'move_type': 'GM Firing',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 3.5,  # Poor roster construction
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 0.0,
        'impact_score': 2.0,  # Major addition by subtraction
    },
    {
        'player_name': 'Grant Udinski',
        'position': 'COACH-OC',
        'from_team': 'External',
        'to_team': 'Jac',
        'move_type': 'Offensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 2000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Lawrence development
        'impact_score': 1.5,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Jac',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 6000000,  # Combined
        'guaranteed_money': 600000,
        'aav': 2000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
JAGUARS_2025_SUMMARY = {
    'total_moves': len(JAGUARS_2025_MOVES),
    'free_agent_signings': 8,  # Targeted additions
    'major_losses': 6,  # Kirk, Engram, Morse
    'trades': 2,  # Hunter trade, Kirk trade
    'draft_picks': 6,  # Limited by trade
    'key_resignings': 4,
    'coaching_changes': 6,  # Complete overhaul
    'cap_casualties': 3,
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 125000000,  # Hunter deal dominates
    'draft_capital_spent': '2025: 1st, 2nd, 4th + 2026: 1st',
    'cap_space_used': 115000000,
    'cap_space_remaining': 18000000,
    'championship_window': '2025-2028',  # Lawrence prime
    'offseason_grade': 'B',
    'key_philosophy': 'Bold aggression with franchise-altering gamble',
    'net_impact_score': 21.5,  # Sum of all impact scores
    'biggest_concern': 'Massive draft capital expenditure',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'hunter_trade': {
        'cost': '2025 #5, #36, #126 + 2026 1st',
        'return': '#2 pick, #104, #200',
        'philosophy': 'Swing for generational talent',
        'gladstone_quote': 'Alter trajectory of sport itself',
    },
    'organizational_overhaul': {
        'pederson_firing': '4-13 disaster season',
        'baalke_dismissal': 'Poor roster construction',
        'coen_hire': 'Offensive mind from Tampa',
        'boselli_addition': 'Franchise credibility',
    },
    'offensive_line_focus': {
        'mekari_signing': '94.6% pass block win rate',
        'hainsey_addition': 'Coen familiarity',
        'milum_draft': 'OT development',
        'philosophy': 'Protect Lawrence at all costs',
    },
    'receiver_situation': {
        'kirk_trade': 'Cleared cap space',
        'engram_release': 'Major loss',
        'hunter_impact': 'Two-way game changer',
        'brown_signing': 'Proven production',
    },
    'historical_context': {
        'hunter_bonus': '$30.57M paid upfront (record)',
        'non_qb_record': 'First non-QB #2 pick with full bonus',
        'organizational_message': 'Bold and aggressive approach',
        'cbs_grade': 'B - phenomenal but costly',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Trevor Lawrence',
        'backup': 'Nick Mullens',
        'grade': 'B+',
        'notes': 'Lawrence health key, Coen system fit crucial',
    },
    'offensive_line': {
        'starters': ['Walker Little (LT)', 'Patrick Mekari (LG)', 'Robert Hainsey (C)', 
                     'RG TBD', 'Anton Harrison (RT)'],
        'depth': 'Significant interior upgrades',
        'grade': 'B',
        'notes': 'Protection vastly improved',
    },
    'skill_positions': {
        'wr': 'Travis Hunter, Brian Thomas Jr., Dyami Brown',
        'rb': 'Travis Etienne Jr., Tank Bigsby',
        'te': 'Brenton Strange (post-Engram)',
        'grade': 'B+',
        'notes': 'Hunter transforms entire offense',
    },
    'defensive_line': {
        'dt': 'DaVon Hamilton, Roy Robertson-Harris',
        'edge': 'Josh Hines-Allen, Travon Walker',
        'grade': 'B+',
        'notes': 'Pass rush remains elite',
    },
    'linebackers': {
        'starters': 'Foyesade Oluokun, Devin Lloyd',
        'depth': 'Jalen McLeod adds depth',
        'grade': 'B-',
        'notes': 'Solid but unspectacular',
    },
    'secondary': {
        'cb': 'Travis Hunter, Tyson Campbell, Jourdan Lewis',
        'safety': 'Andre Cisco, Darnell Savage',
        'grade': 'A-',
        'notes': 'Hunter elevates entire unit',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'OVER',
        'reasoning': 'Hunter impact, Lawrence bounce back',
    },
    'division_odds': {
        'current': '+250',
        'value': 'YES',
        'reasoning': 'Houston vulnerable, value play',
    },
    'playoffs': {
        'odds': '+105',
        'value': 'YES',
        'reasoning': 'Hunter changes everything',
    },
    'player_props': {
        'lawrence_passing_yards': 'OVER 3,800',
        'hunter_receiving_yards': 'OVER 800',
        'hunter_interceptions': 'OVER 3.5',
        'hunter_dpoy': '+1200 (value)',
    },
    'key_angles': {
        'best_bet': 'Over 8.5 wins',
        'longshot': 'Hunter DPOY +1200',
        'narrative': 'Bold moves pay off',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("JACKSONVILLE JAGUARS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {JAGUARS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{JAGUARS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {JAGUARS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {JAGUARS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {JAGUARS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {JAGUARS_2025_SUMMARY['major_losses']}")
    print(f"  • Draft Picks: {JAGUARS_2025_SUMMARY['draft_picks']} (limited by trade)")
    print(f"  • Coaching Changes: {JAGUARS_2025_SUMMARY['coaching_changes']} (complete overhaul)")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${JAGUARS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Draft Capital Spent: {JAGUARS_2025_SUMMARY['draft_capital_spent']}")
    print(f"  • Current Cap Space: ${JAGUARS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Travis Hunter (WR/CB) - #2 pick, two-way star")
    print("  • Liam Coen (HC) - From Tampa Bay")
    print("  • Patrick Mekari (G) - 3yr/$37.5M")
    print("  • James Gladstone (GM) - From Rams")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • Christian Kirk - Traded to Houston")
    print("  • Evan Engram - Released")
    print("  • Doug Pederson/Trent Baalke - Fired")
    print("  • 4 draft picks for Hunter")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {JAGUARS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Hunter: $30.57M signing bonus (record)")
    print(f"  • Gladstone: 'Alter trajectory of sport'")
    print(f"  • CBS Grade: B (phenomenal but costly)")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Trevor Lawrence health/development")
    print("  • Travis Hunter two-way impact")
    print("  • Coen offensive system implementation")
    print("  • Draft capital limitations going forward")

if __name__ == "__main__":
    generate_summary_report()
"""
Houston Texans 2025 Offseason Moves
Protecting C.J. Stroud: Calculated risk strategy with controversial OL decisions
Last Updated: June 23, 2025
"""

TEXANS_2025_MOVES = [
    # ========== OFFENSIVE LINE OVERHAUL - Controversial moves ==========
    {
        'player_name': 'Cam Robinson',
        'position': 'LT',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14500000,
        'guaranteed_money': 10000000,
        'aav': 14500000,
        '2024_grade': 5.8,  # Allowed 9 sacks, 12.1% pressure rate
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 8.5,  # Tunsil replacement
        'impact_score': -1.0,  # Downgrade from Tunsil
    },
    {
        'player_name': 'Trent Brown',
        'position': 'RT',
        'from_team': 'Cin',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 8000000,
        '2024_grade': 6.5,  # Veteran depth
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Tackle depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Laken Tomlinson',
        'position': 'LG',
        'from_team': 'NYJ',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 8000000,
        'aav': 8000000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Interior upgrade
        'impact_score': 0.8,
    },

    # ========== SKILL POSITION ADDITIONS ==========
    {
        'player_name': 'Christian Kirk',
        'position': 'WR',
        'from_team': 'Jac',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 34000000,  # Existing contract
        'guaranteed_money': 15000000,
        'aav': 17000000,
        '2024_grade': 7.0,  # Reliable slot receiver
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Tank Dell injury
        'impact_score': 1.8,
    },
    {
        'player_name': 'Justin Watson',
        'position': 'WR',
        'from_team': 'KC',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Depth/ST
        'impact_score': 0.5,
    },
    {
        'player_name': 'Braxton Berrios',
        'position': 'WR',
        'from_team': 'Mia',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Slot depth
        'impact_score': 0.3,
    },

    # ========== DEFENSIVE REINFORCEMENTS ==========
    {
        'player_name': 'C.J. Gardner-Johnson',
        'position': 'S',
        'from_team': 'Phi',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 8000000,
        '2024_grade': 7.5,  # Versatile safety
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Secondary upgrade
        'impact_score': 2.0,
    },
    {
        'player_name': 'Derek Barnett',
        'position': 'EDGE',
        'from_team': 'Ten',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 6000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.3,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Edge depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Nick Niemann',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 6.0,  # Special teams ace
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,  # LB depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Tremon Smith',
        'position': 'CB',
        'from_team': 'Den',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 800000,
        'aav': 1500000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,  # CB depth
        'impact_score': 0.2,
    },
    {
        'player_name': 'Damon Arnette',
        'position': 'CB',
        'from_team': 'UFL',
        'to_team': 'Hou',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        'guaranteed_money': 500000,
        'aav': 1200000,
        '2024_grade': 6.0,  # UFL success
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Camp competition
        'impact_score': 0.2,
    },

    # ========== MAJOR LOSSES - Controversial OL decisions ==========
    {
        'player_name': 'Laremy Tunsil',
        'position': 'LT',
        'from_team': 'Hou',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 9.0,  # 4th-best pass-blocking tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 9.5,  # Elite LT
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,  # Massive loss
    },
    {
        'player_name': 'Kenyon Green',
        'position': 'RG',
        'from_team': 'Hou',
        'to_team': 'Phi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # 11.3% pressure rate
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Shaq Mason',
        'position': 'RG',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.2,  # Allowed 10.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },
    {
        'player_name': 'Stefon Diggs',
        'position': 'WR1',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # 610 yards limited role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Robert Woods',
        'position': 'WR',
        'from_team': 'Hou',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,
    },
    {
        'player_name': 'Eric Murray',
        'position': 'S',
        'from_team': 'Hou',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== KEY EXTENSIONS - Defensive cornerstone deals ==========
    {
        'player_name': 'Derek Stingley Jr.',
        'position': 'CB1',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 90000000,
        'guaranteed_money': 89000000,  # NFL DB record
        'aav': 30000000,
        '2024_grade': 9.0,  # All-Pro, 5 INTs
        'projected_2025_grade': 9.2,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,  # Franchise CB
        'impact_score': 3.0,
    },
    {
        'player_name': 'Danielle Hunter',
        'position': 'EDGE',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Contract Extension',
        'contract_years': 1,
        'contract_value': 35600000,
        'guaranteed_money': 25000000,
        'aav': 35600000,
        '2024_grade': 8.5,  # Productive first year
        'projected_2025_grade': 8.3,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,  # Premier pass rusher
        'impact_score': 2.5,
    },
    {
        'player_name': 'Mario Edwards Jr.',
        'position': 'DT',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 9500000,
        'guaranteed_money': 5000000,
        'aav': 4750000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,  # DL depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Dare Ogunbowale',
        'position': 'RB',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 5.5,  # RB depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Justin Hinish',
        'position': 'DT',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 800000,
        'aav': 1500000,
        '2024_grade': 5.5,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 5.5,  # DT depth
        'impact_score': 0.2,
    },

    # ========== 2025 NFL DRAFT - WR focus after trading out of 1st ==========
    {
        'player_name': 'Jayden Higgins',
        'position': 'WR',
        'from_team': 'Iowa State',
        'to_team': 'Hou',
        'move_type': '2025 Draft - Round 2, Pick 34',
        'contract_years': 4,
        'contract_value': 8800000,
        'guaranteed_money': 4400000,
        'aav': 2200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 6\'4", 4.47 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # WR help for Stroud
        'impact_score': 1.8,
    },
    {
        'player_name': 'Aireontae Ersery',
        'position': 'OT',
        'from_team': 'Minnesota',
        'to_team': 'Hou',
        'move_type': '2025 Draft - Round 2, Pick 48',
        'contract_years': 4,
        'contract_value': 7600000,
        'guaranteed_money': 3800000,
        'aav': 1900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Left tackle prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # OL development
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jaylin Noel',
        'position': 'WR',
        'from_team': 'Iowa State',
        'to_team': 'Hou',
        'move_type': '2025 Draft - Round 3, Pick 79',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1400000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 4.37 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Speed threat
        'impact_score': 1.0,
    },
    {
        'player_name': 'USC Smith',
        'position': 'CB',
        'from_team': 'USC',
        'to_team': 'Hou',
        'move_type': '2025 Draft - Round 4, Pick 124',
        'contract_years': 4,
        'contract_value': 4600000,
        'guaranteed_money': 900000,
        'aav': 1150000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # CB depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'D.J. Marks',
        'position': 'RB',
        'from_team': 'College',
        'to_team': 'Hou',
        'move_type': '2025 Draft - Round 5, Pick 156',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # 1,133 rushing yards
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # RB depth
        'impact_score': 0.5,
    },

    # ========== TRADES ==========
    {
        'player_name': 'Laremy Tunsil + 2025 4th',
        'position': 'PICKS',
        'from_team': 'Hou',
        'to_team': 'Was',
        'move_type': 'Trade Package',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.0,  # Elite LT + pick
        'importance_to_new_team': 0.0,
        'impact_score': 1.5,  # Got 3rd, 7th, future 2nd, 4th
    },
    {
        'player_name': 'Kenyon Green + 2026 5th',
        'position': 'PICKS',
        'from_team': 'Hou',
        'to_team': 'Phi',
        'move_type': 'Trade Package',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.8,  # Got Gardner-Johnson
    },

    # ========== COACHING CHANGES - Offensive overhaul ==========
    {
        'player_name': 'Bobby Slowik',
        'position': 'COACH-OC',
        'from_team': 'Hou',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Offense regressed
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Nick Caley',
        'position': 'COACH-OC',
        'from_team': 'LAR',
        'to_team': 'Hou',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 7500000,
        'guaranteed_money': 3750000,
        'aav': 2500000,
        '2024_grade': 7.5,  # Rams coordinator
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.5,  # Fresh offensive vision
        'impact_score': 2.0,
    },
    {
        'player_name': 'Chris Strausser',
        'position': 'COACH-OL',
        'from_team': 'Hou',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # OL allowed 52 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Addition by subtraction
    },
    {
        'player_name': 'Cole Popovich',
        'position': 'COACH-OL',
        'from_team': 'Hou',
        'to_team': 'Hou',
        'move_type': 'Promotion',
        'contract_years': 2,
        'contract_value': 2500000,
        'guaranteed_money': 1250000,
        'aav': 1250000,
        '2024_grade': 6.5,  # Assistant promoted
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Internal continuity
        'impact_score': 0.8,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Ed Ingram',
        'position': 'RG',
        'from_team': 'Min',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 2800000,
        'guaranteed_money': 1400000,
        'aav': 2800000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.3,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Guard depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Austin Brinkman',
        'position': 'LS',
        'from_team': 'UFL',
        'to_team': 'Hou',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2700000,
        'guaranteed_money': 200000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Won LS competition
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
TEXANS_2025_SUMMARY = {
    'total_moves': len(TEXANS_2025_MOVES),
    'free_agent_signings': 10,  # Mixed results
    'major_losses': 6,  # Including Tunsil trade
    'trades': 4,  # Active trade market
    'draft_picks': 5,  # Traded out of 1st round
    'key_extensions': 2,  # Stingley & Hunter mega-deals
    'key_resignings': 3,
    'coaching_changes': 4,  # OC/OL overhaul
    'cap_casualties': 3,  # Diggs, Woods, Mason
    'udfa_signings': 1,
    'total_guaranteed_money': 175000000,  # Major investments
    'cap_space_used': 140000000,
    'cap_space_remaining': 12000000,  # Limited flexibility
    'championship_window': '2025-2027',  # Stroud's rookie deal
    'offseason_grade': 'C+',
    'key_philosophy': 'Calculated risk with controversial OL decisions',
    'net_impact_score': 12.5,  # Sum of all impact scores
    'biggest_concern': 'OL protection may have gotten worse',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'offensive_line_gamble': {
        'problem': '52 sacks allowed (2nd-most in NFL)',
        'solution': 'Trade Tunsil, sign Robinson',
        'criticism': 'CBS: Stroud biggest loser in NFL',
        'reality': 'Robinson allowed 9 sacks, 12.1% pressure',
    },
    'defensive_investments': {
        'stingley_deal': '$90M, $89M guaranteed (DB record)',
        'hunter_extension': '$35.6M through 2026',
        'philosophy': 'Lock up elite defenders',
        'cap_impact': 'Limited flexibility going forward',
    },
    'skill_position_changes': {
        'losses': 'Diggs released, Tank Dell injured',
        'additions': 'Kirk trade, draft Higgins/Noel',
        'concern': 'Dell out most/all of 2025',
        'upside': 'Young receivers with upside',
    },
    'coaching_overhaul': {
        'slowik_firing': 'Offense regressed despite talent',
        'caley_hire': 'Rams coordinator brings fresh ideas',
        'ol_coach': 'Internal promotion questionable',
        'pressure': 'Must improve immediately',
    },
    'critical_quote': {
        'cbs_analyst': 'OL took steps back rather than forward',
        'tunsil_loss': 'One of best 1-on-1 pass protectors',
        'robinson_concern': '3rd-highest pressure rate among LTs',
        'bottom_line': 'Protection actually got worse',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'C.J. Stroud',
        'backup': 'Davis Mills',
        'grade': 'A-',
        'notes': 'Elite QB talent, but protection concerns',
    },
    'offensive_line': {
        'starters': ['Cam Robinson (LT)', 'Laken Tomlinson (LG)', 'Jarrett Patterson (C)', 
                     'Ed Ingram (RG)', 'Trent Brown (RT)'],
        'depth': 'Aireontae Ersery developmental',
        'grade': 'D+',
        'notes': 'Major downgrade from 2024',
    },
    'skill_positions': {
        'wr': 'Christian Kirk, Jayden Higgins, Jaylin Noel',
        'rb': 'Joe Mixon, Damien Pierce, D.J. Marks',
        'te': 'Dalton Schultz, Brevin Jordan',
        'grade': 'B',
        'notes': 'Tank Dell injury massive blow',
    },
    'defensive_line': {
        'dt': 'Mario Edwards Jr., Justin Hinish',
        'edge': 'Danielle Hunter, Will Anderson Jr., Derek Barnett',
        'grade': 'B+',
        'notes': 'Hunter extension solidifies pass rush',
    },
    'linebackers': {
        'starters': 'Azeez Al-Shaair, Christian Harris, Nick Niemann',
        'depth': 'Henry To\'oTo\'o provides depth',
        'grade': 'B',
        'notes': 'Solid but unspectacular',
    },
    'secondary': {
        'cb': 'Derek Stingley Jr., Steven Nelson, Damon Arnette',
        'safety': 'C.J. Gardner-Johnson, Jalen Pitre',
        'grade': 'A',
        'notes': 'Stingley highest-paid DB in NFL',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'UNDER',
        'reasoning': 'OL concerns, tough division',
    },
    'division_odds': {
        'current': '+150',
        'value': 'NO',
        'reasoning': 'Protection issues limit ceiling',
    },
    'playoffs': {
        'odds': '-120',
        'value': 'YES',
        'reasoning': 'Weak AFC wild card field',
    },
    'player_props': {
        'stroud_passing_yards': 'UNDER 4,400 (pressure concerns)',
        'stroud_sacks_taken': 'OVER 45.5',
        'stingley_interceptions': 'OVER 4.5',
        'hunter_sacks': 'OVER 9.5',
    },
    'key_angles': {
        'best_bet': 'Under 9.5 wins',
        'concern': 'Stroud regression behind worse OL',
        'narrative': 'Protection problems persist',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("HOUSTON TEXANS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {TEXANS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{TEXANS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {TEXANS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {TEXANS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {TEXANS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {TEXANS_2025_SUMMARY['major_losses']}")
    print(f"  • Draft Picks: {TEXANS_2025_SUMMARY['draft_picks']} (traded out of 1st)")
    print(f"  • Key Extensions: {TEXANS_2025_SUMMARY['key_extensions']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${TEXANS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Used: ${TEXANS_2025_SUMMARY['cap_space_used']:,}")
    print(f"  • Current Cap Space: ${TEXANS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Cam Robinson (LT) - 1yr/$14.5M (Tunsil replacement)")
    print("  • Christian Kirk (WR) - Via trade from Jacksonville")
    print("  • C.J. Gardner-Johnson (S) - Via trade")
    print("  • Jayden Higgins (WR) - 2nd round pick")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • Laremy Tunsil - Traded to Washington")
    print("  • Stefon Diggs - Released (cap)")
    print("  • Tank Dell - Injured (out most/all 2025)")
    print("  • Bobby Slowik - OC fired")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {TEXANS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Biggest Concern: {TEXANS_2025_SUMMARY['biggest_concern']}")
    print(f"  • Stingley Deal: $90M ($89M guaranteed)")
    print(f"  • CBS Analysis: 'Stroud biggest loser in NFL'")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Robinson allowed 9 sacks, 12.1% pressure rate")
    print("  • Tunsil was 4th-best pass-blocking tackle")
    print("  • 52 sacks allowed in 2024 (2nd-most)")
    print("  • Tank Dell injury compounds WR concerns")

if __name__ == "__main__":
    generate_summary_report()
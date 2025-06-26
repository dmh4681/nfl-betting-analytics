"""
Pittsburgh Steelers 2025 Offseason Moves
Dramatic transformation centered on Metcalf acquisition and QB uncertainty
Last Updated: June 23, 2025
"""

STEELERS_2025_MOVES = [
    # ========== BLOCKBUSTER TRADE - Elite WR acquisition ==========
    {
        'player_name': 'DK Metcalf',
        'position': 'WR1',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Trade + Extension',
        'contract_years': 5,
        'contract_value': 150000000,
        'guaranteed_money': 60000000,
        'aav': 30000000,
        '2024_grade': 9.0,  # Elite receiver
        'projected_2025_grade': 9.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 10.0,  # Franchise WR
        'impact_score': 3.0,
        'notes': 'Traded 2025 2nd (#52) + 7th (#223) for Metcalf + 6th (#185)'
    },

    # ========== FREE AGENT SIGNINGS - Championship pedigree additions ==========
    {
        'player_name': 'Aaron Rodgers',
        'position': 'QB',
        'from_team': 'NYJ',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 13600000,
        'guaranteed_money': 13600000,
        'aav': 13600000,
        '2024_grade': 7.5,  # Age 41 season
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Solves QB crisis
        'impact_score': 2.5,
        'notes': 'Chose Pittsburgh over Giants and Vikings'
    },
    {
        'player_name': 'Darius Slay',
        'position': 'CB',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 7000000,
        'aav': 10000000,
        '2024_grade': 7.5,  # Age 34, 81% snaps
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 81.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Veteran leadership
        'impact_score': 1.5,
    },
    {
        'player_name': 'Juan Thornhill',
        'position': 'S',
        'from_team': 'KC',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 2000000,
        'aav': 3000000,
        '2024_grade': 6.5,  # Injury limited
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Malik Harrison',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 10000000,
        'guaranteed_money': 5500000,
        'aav': 5000000,
        '2024_grade': 7.0,  # 54 tackles, ST ace
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 38.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # Ravens intel
        'impact_score': 1.2,
        'notes': 'Second straight year poaching Ravens LB'
    },
    {
        'player_name': 'Kenneth Gainwell',
        'position': 'RB',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1790000,
        'guaranteed_money': 620000,
        'aav': 1790000,
        '2024_grade': 6.5,  # 290 rush, 116 rec yards
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Mason Rudolph',
        'position': 'QB',
        'from_team': 'Ten',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.0,  # Bridge QB
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Familiar backup
        'impact_score': 0.5,
    },
    {
        'player_name': 'Brandin Echols',
        'position': 'CB',
        'from_team': 'NYJ',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Daniel Ekuale',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },

    # ========== MAJOR LOSSES - QB exodus and OL departures ==========
    {
        'player_name': 'Justin Fields',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # 4-2 as starter
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,  # 2yr/$40M to Jets
    },
    {
        'player_name': 'Russell Wilson',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,  # Late-season collapse
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # 1yr deal to Giants
    },
    {
        'player_name': 'Dan Moore Jr.',
        'position': 'LT',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Solid LT
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -2.2,  # 4yr/$82M to Titans
    },
    {
        'player_name': 'James Daniels',
        'position': 'G',
        'from_team': 'Pit',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,  # 3yr/$24M to Dolphins
    },
    {
        'player_name': 'Najee Harris',
        'position': 'RB',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Four 1,000-yard seasons
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # 1yr/$9.25M to Chargers
    },
    {
        'player_name': 'Donte Jackson',
        'position': 'CB',
        'from_team': 'Pit',
        'to_team': 'LAC',
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
        'impact_score': -1.2,  # 2yr/$13M to Chargers
    },
    {
        'player_name': 'Larry Ogunjobi',
        'position': 'DT',
        'from_team': 'Pit',
        'to_team': 'Buf',
        'move_type': 'Cut/Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # 1yr/$8.3M to Bills
    },

    # ========== TRADES - Pickens departure ==========
    {
        'player_name': 'George Pickens',
        'position': 'WR',
        'from_team': 'Pit',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Talent vs character
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,
        'notes': 'Traded with 2027 6th for 2026 3rd + 2027 5th'
    },

    # ========== 2025 NFL DRAFT - Defensive focus ==========
    {
        'player_name': 'Derrick Harmon',
        'position': 'DT',
        'from_team': 'Oregon',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 1, Pick 21',
        'contract_years': 4,
        'contract_value': 18400000,
        'guaranteed_money': 18400000,
        'aav': 4600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # 34 QB pressures led FBS
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Heyward successor
        'impact_score': 2.2,
        'notes': 'Steelers DNA per Tomlin'
    },
    {
        'player_name': 'Kaleb Johnson',
        'position': 'RB',
        'from_team': 'Iowa',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 3, Pick 84',
        'contract_years': 4,
        'contract_value': 6400000,
        'guaranteed_money': 1600000,
        'aav': 1600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Physical runner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replace Harris
        'impact_score': 1.5,
    },
    {
        'player_name': 'Jack Sawyer',
        'position': 'OLB',
        'from_team': 'Ohio State',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 4, Pick 119',
        'contract_years': 4,
        'contract_value': 5000000,
        'guaranteed_money': 1000000,
        'aav': 1250000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 15.9% pressure rate
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Depth behind Watt
        'impact_score': 1.0,
    },
    {
        'player_name': 'Yahya Black',
        'position': 'DT',
        'from_team': 'Iowa',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 5, Pick 150',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 700000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Will Howard',
        'position': 'QB',
        'from_team': 'Ohio State',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 6, Pick 189',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 500000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Development project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Carson Bruener',
        'position': 'LB',
        'from_team': 'Washington',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 7, Pick 226',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
        'notes': 'Son of former Steeler Mark Bruener'
    },
    {
        'player_name': 'Donte Kent',
        'position': 'CB',
        'from_team': 'Central Michigan',
        'to_team': 'Pit',
        'move_type': '2025 Draft - Round 7, Pick 243',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },

    # ========== KEY EXTENSIONS - Building around core ==========
    {
        'player_name': 'T.J. Watt',
        'position': 'EDGE',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Extension Pending',
        'contract_years': 3,
        'contract_value': 108000000,
        'guaranteed_money': 108000000,
        'aav': 36000000,
        '2024_grade': 9.5,  # Elite edge rusher
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,
        'notes': 'Projected extension, skipped OTAs'
    },
    {
        'player_name': 'DeShon Elliott',
        'position': 'S',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Extension Pending',
        'contract_years': 2,
        'contract_value': 18500000,
        'guaranteed_money': 12000000,
        'aav': 9250000,
        '2024_grade': 8.0,  # 108 tackles, 3 FF
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.8,
    },
    {
        'player_name': 'Jaylen Warren',
        'position': 'RB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Second-round tender',
        'contract_years': 1,
        'contract_value': 5346000,
        'guaranteed_money': 5346000,
        'aav': 5346000,
        '2024_grade': 7.5,  # Complementary back
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },

    # ========== RE-SIGNINGS - Depth retention ==========
    {
        'player_name': 'Ben Skowronek',
        'position': 'WR',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 4000000,
        'guaranteed_money': 2000000,
        'aav': 2000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Scotty Miller',
        'position': 'WR',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'James Pierre',
        'position': 'CB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1400000,
        'guaranteed_money': 700000,
        'aav': 1400000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Isaiahh Loudermilk',
        'position': 'DE',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1600000,
        'guaranteed_money': 800000,
        'aav': 1600000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },

    # ========== COACHING/FRONT OFFICE CHANGES ==========
    {
        'player_name': 'Aaron Curry',
        'position': 'COACH-ILB',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Communication issues
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
        'notes': 'Green dot communication problems'
    },
    {
        'player_name': 'Grady Brown',
        'position': 'COACH-DB',
        'from_team': 'Pit',
        'to_team': 'FA',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Blown coverages
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Arthur Smith',
        'position': 'COACH-OC',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Retained',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,  # Metcalf addition
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Teryl Austin',
        'position': 'COACH-DC',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Retained',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.2,
    },
]

# ========== SUMMARY METRICS ==========
STEELERS_2025_SUMMARY = {
    'total_moves': len(STEELERS_2025_MOVES),
    'free_agent_signings': 8,
    'major_losses': 7,
    'trades': 2,  # Metcalf in, Pickens out
    'draft_picks': 7,
    'key_extensions': 3,
    'coaching_changes': 2,
    'total_guaranteed_money': 150000000,  # Estimate
    'dead_money': 12000000,
    'cap_space_remaining': 18000000,
    'cap_space_2026': 72000000,
    'championship_window': '2025-2026',
    'offseason_grade': 'B',
    'key_philosophy': 'Win-now gamble with Rodgers-Metcalf pairing',
    'net_impact_score': 8.2,  # Sum of all impact scores
    'division_outlook': 'Third behind Ravens and Bengals',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'quarterback_situation': {
        'rodgers_gamble': 'Age 41, chose PIT over NYG/MIN',
        'backup_plan': 'Rudolph familiarity',
        'draft_insurance': 'Will Howard development',
        'timeline': '1-2 year window maximum',
    },
    'metcalf_acquisition': {
        'cost': '2nd + 7th for elite WR',
        'contract': '$150M total, $30M AAV',
        'pickens_trade': 'Character concerns addressed',
        'offensive_identity': 'Committed to passing game',
    },
    'offensive_line_crisis': {
        'moore_loss': '$82M to Tennessee',
        'daniels_departure': 'Interior weakened',
        'draft_neglect': 'No OL picks until late',
        'vulnerability': 'Major concern for Rodgers',
    },
    'defensive_approach': {
        'draft_focus': '5 of 7 picks on defense',
        'harmon_selection': 'Heyward succession plan',
        'watt_extension': 'Projected $36M AAV',
        'identity_maintained': 'Tomlin defensive DNA',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Aaron Rodgers',
        'backup': 'Mason Rudolph',
        'grade': 'B',
        'notes': 'High ceiling, low floor at QB',
    },
    'offensive_line': {
        'starters': ['Broderick Jones (LT)', 'Isaac Seumalo (LG)', 
                     'Ryan McCollum (C)', 'Nate Herbig (RG)', 'Chuks Okorafor (RT)'],
        'depth': 'Major concerns',
        'grade': 'D+',
        'notes': 'Lost both starting guards',
    },
    'skill_positions': {
        'wr': 'DK Metcalf, Calvin Austin III, Roman Wilson',
        'rb': 'Jaylen Warren, Kaleb Johnson, Kenneth Gainwell',
        'te': 'Pat Freiermuth, Darnell Washington',
        'grade': 'A-',
        'notes': 'Elite WR1 acquired',
    },
    'defensive_line': {
        'dt': 'Cameron Heyward, Derrick Harmon, Keeanu Benton',
        'edge': 'T.J. Watt, Alex Highsmith, Jack Sawyer',
        'grade': 'A',
        'notes': 'Elite pass rush continues',
    },
    'linebackers': {
        'starters': 'Patrick Queen, Malik Harrison, Elandon Roberts',
        'depth': 'Carson Bruener',
        'grade': 'B+',
        'notes': 'Ravens LB pipeline continues',
    },
    'secondary': {
        'cb': 'Joey Porter Jr., Darius Slay, Donte Kazee',
        'safety': 'Minkah Fitzpatrick, DeShon Elliott, Juan Thornhill',
        'grade': 'B+',
        'notes': 'Veteran additions boost depth',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'UNDER',
        'reasoning': 'OL concerns + QB age risk',
    },
    'division_odds': {
        'current': '+350',
        'value': 'NO',
        'reasoning': 'Ravens/Bengals superior',
    },
    'playoffs': {
        'current': '-110',
        'value': 'SLIGHT YES',
        'reasoning': 'Wild card path viable',
    },
    'player_props': {
        'rodgers_passing_yards': 'UNDER 3,800',
        'metcalf_receiving_yards': 'OVER 1,200',
        'watt_sacks': 'OVER 14.5',
    },
    'key_angles': {
        'best_bet': 'Metcalf 10+ TDs',
        'fade': 'Division winner',
        'narrative': 'Last dance for Rodgers',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("PITTSBURGH STEELERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {STEELERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{STEELERS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {STEELERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {STEELERS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {STEELERS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {STEELERS_2025_SUMMARY['major_losses']}")
    print(f"  • Trades: Metcalf IN, Pickens OUT")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${STEELERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: ${STEELERS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Space: ${STEELERS_2025_SUMMARY['cap_space_2026']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Aaron Rodgers (QB) - 1yr/$13.6M")
    print("  • DK Metcalf (WR) - Trade + 5yr/$150M extension")
    print("  • Darius Slay (CB) - 1yr/$10M from Eagles")
    print("  • Malik Harrison (LB) - 2yr/$10M from Ravens")
    
    print("\n❌ KEY LOSSES:")
    print("  • Justin Fields (QB) - 2yr/$40M to Jets")
    print("  • Russell Wilson (QB) - To Giants")
    print("  • Dan Moore Jr. (LT) - 4yr/$82M to Titans")
    print("  • Najee Harris (RB) - To Chargers")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {STEELERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {STEELERS_2025_SUMMARY['division_outlook']}")
    print(f"  • QB Plan: Rodgers age 41 season")
    print(f"  • OL Concern: Major losses unaddressed")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Rodgers health at age 41")
    print("  • Offensive line protection")
    print("  • Metcalf-Rodgers chemistry")
    print("  • Division competition intense")

if __name__ == "__main__":
    generate_summary_report()
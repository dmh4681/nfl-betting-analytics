"""
Carolina Panthers 2025 Offseason Moves
Aggressive defensive rebuild while supporting Bryce Young's development
Last Updated: June 23, 2025
"""

PANTHERS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Defensive transformation ($126M+) ==========
    {
        'player_name': 'Tershawn Wharton',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 54000000,
        'guaranteed_money': 30000000,
        'aav': 18000000,
        '2024_grade': 8.0,  # From Chiefs championship defense
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Anchor for 32nd-ranked defense
        'impact_score': 2.5,
    },
    {
        'player_name': "Tre'von Moehrig",
        'position': 'S',
        'from_team': 'LV',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 51000000,
        'guaranteed_money': 28000000,
        'aav': 17000000,
        '2024_grade': 7.8,
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Replace Woods
        'impact_score': 2.0,
    },
    {
        'player_name': 'Bobby Brown III',
        'position': 'DT',
        'from_team': 'LAR',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 21000000,
        'guaranteed_money': 12000000,
        'aav': 7000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.3,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Patrick Jones II',
        'position': 'EDGE',
        'from_team': 'Min',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 20000000,
        'guaranteed_money': 11000000,
        'aav': 10000000,
        '2024_grade': 7.2,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Address 32 sacks in 2024
        'impact_score': 1.2,
    },
    {
        'player_name': 'Christian Rozeboom',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # LB depth crucial
        'impact_score': 0.5,
    },
    {
        'player_name': 'Rico Dowdle',
        'position': 'RB',
        'from_team': 'Dal',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 6250000,
        'guaranteed_money': 3500000,
        'aav': 6250000,
        '2024_grade': 7.5,  # 1,079 yards rushing
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Replace Sanders
        'impact_score': 1.0,
        'notes': 'Asheville native, Cowboys first undrafted 1K rusher'
    },
    {
        'player_name': 'Sam Martin',
        'position': 'P',
        'from_team': 'Buf',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Replace Hekker
        'impact_score': 0.2,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS - Horn megadeal ==========
    {
        'player_name': 'Jaycee Horn',
        'position': 'CB1',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 100000000,
        'guaranteed_money': 70000000,
        'aav': 25000000,
        '2024_grade': 8.5,  # Elite when healthy
        'projected_2025_grade': 8.8,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.5,
        'impact_score': 3.0,  # Highest-paid DB in NFL
    },
    {
        'player_name': 'Andy Dalton',
        'position': 'QB',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 4000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Young mentor crucial
        'impact_score': 1.0,
    },
    {
        'player_name': 'Mike Jackson',
        'position': 'CB2',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 14500000,
        'guaranteed_money': 8000000,
        'aav': 7250000,
        '2024_grade': 7.5,  # 17 pass deflections
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,
        'impact_score': 1.2,
    },
    {
        'player_name': 'Tommy Tremble',
        'position': 'TE',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 9000000,
        'aav': 8000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.3,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Austin Corbett',
        'position': 'C',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 4000000,
        'guaranteed_money': 2500000,
        'aav': 4000000,
        '2024_grade': 7.2,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Raheem Blackshear',
        'position': 'RB/KR',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 1500000,
        '2024_grade': 7.8,  # 2nd in NFL, 791 return yards
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 0.6,
    },

    # ========== 2025 NFL DRAFT - WR for Young + defensive depth ==========
    {
        'player_name': 'Tetairoa McMillan',
        'position': 'WR1',
        'from_team': 'Arizona',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 1, Pick 8',
        'contract_years': 4,
        'contract_value': 35000000,
        'guaranteed_money': 35000000,
        'aav': 8750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Elite prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Bryce Young's #1
        'impact_score': 2.5,
        'notes': "6'4\", 219 lbs, compared to Mike Evans"
    },
    {
        'player_name': 'Nic Scourton',
        'position': 'EDGE',
        'from_team': 'Texas A&M',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 2, Pick 51 (Traded Up)',
        'contract_years': 4,
        'contract_value': 9000000,
        'guaranteed_money': 5000000,
        'aav': 2250000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Princely Umanmielen',
        'position': 'EDGE',
        'from_team': 'Ole Miss',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 3, Pick 77 (Traded Up)',
        'contract_years': 4,
        'contract_value': 5500000,
        'guaranteed_money': 1500000,
        'aav': 1375000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
        'notes': 'Double-dip EDGE strategy'
    },
    {
        'player_name': 'Trevor Etienne',
        'position': 'RB',
        'from_team': 'Georgia',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 4, Pick 124',
        'contract_years': 4,
        'contract_value': 4000000,
        'guaranteed_money': 900000,
        'aav': 1000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Lathan Ransom',
        'position': 'S',
        'from_team': 'Ohio State',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 5, Pick 158',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 700000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Cam Jackson',
        'position': 'DT',
        'from_team': 'Florida',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 6, Pick 179',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 500000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.3,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Mitchell Evans',
        'position': 'TE',
        'from_team': 'Notre Dame',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 7, Pick 223',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 400000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Jimmy Horn Jr.',
        'position': 'WR',
        'from_team': 'Colorado',
        'to_team': 'Car',
        'move_type': '2025 Draft - Round 7, Pick 245',
        'contract_years': 4,
        'contract_value': 3000000,
        'guaranteed_money': 300000,
        'aav': 750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.1,
    },

    # ========== MAJOR LOSSES - Veterans and cap casualties ==========
    {
        'player_name': 'Miles Sanders',
        'position': 'RB',
        'from_team': 'Car',
        'to_team': 'FA',
        'move_type': 'Released',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Underperformed contract
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # Saved $5.225M
    },
    {
        'player_name': 'Jadeveon Clowney',
        'position': 'EDGE',
        'from_team': 'Car',
        'to_team': 'FA',
        'move_type': 'Released',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Aging pass rusher
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # Saved $7.78M
    },
    {
        'player_name': 'Xavier Woods',
        'position': 'S',
        'from_team': 'Car',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Played all 1,218 snaps
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Iron man loss
    },
    {
        'player_name': 'Shaq Thompson',
        'position': 'LB',
        'from_team': 'Car',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # 13-year franchise legend
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Leadership void
    },
    {
        'player_name': 'Johnny Hekker',
        'position': 'P',
        'from_team': 'Car',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,
    },

    # ========== TRADES - Draft capital moves ==========
    {
        'player_name': 'Diontae Johnson',
        'position': 'WR',
        'from_team': 'Car',
        'to_team': 'Bal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Underperformed
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # Got 5th round pick
        'notes': 'October 2024 trade, received 5th round pick'
    },
    {
        'player_name': 'Jonathan Mingo',
        'position': 'WR',
        'from_team': 'Car',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # Bust 2nd rounder
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.2,  # Got 4th round pick
        'notes': 'November 2024 trade, received 4th round pick'
    },

    # ========== COACHING CONTINUITY - First time since 2019 ==========
    {
        'player_name': 'Dave Canales',
        'position': 'COACH-HC',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Retained',
        'contract_years': 3,  # Remaining
        'contract_value': 12000000,
        'guaranteed_money': 8000000,
        'aav': 4000000,
        '2024_grade': 6.5,  # First year evaluation
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.0,
        'impact_score': 1.5,  # Stability value
    },
    {
        'player_name': 'Ejiro Evero',
        'position': 'COACH-DC',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Retained',
        'contract_years': 2,
        'contract_value': 4000000,
        'guaranteed_money': 2000000,
        'aav': 2000000,
        '2024_grade': 5.0,  # Historic defensive struggles
        'projected_2025_grade': 7.0,  # With new personnel
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,
        'impact_score': 1.0,
    },
]

# ========== SUMMARY METRICS ==========
PANTHERS_2025_SUMMARY = {
    'total_moves': len(PANTHERS_2025_MOVES),
    'free_agent_signings': 7,
    'key_resignings': 6,
    'draft_picks': 8,
    'coaching_changes': 2,  # New position coaches only
    'major_losses': 7,
    'trades': 2,
    'releases': 2,
    'total_guaranteed_money': 252000000,  # Including Horn extension
    'defensive_investment': 126000000,  # FA signings alone
    'dead_money': 8800000,  # Cleanest in years
    'cap_space_remaining': 18700000,
    'championship_window': '2026-2028',
    'offseason_grade': 'A-',
    'key_philosophy': 'Aggressive defensive rebuild while supporting Bryce Young',
    'net_impact_score': 14.5,  # Sum of all impact scores
    'division_outlook': 'Building for 2026, evaluation year for Young',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'defensive_transformation': {
        '2024_points_allowed': 534,  # NFL record worst
        '2024_sacks': 32,  # League worst
        'investment': '$126M+ in defensive free agents',
        'draft_focus': '6 of 8 picks on defense',
        'philosophy': 'Fix defense through volume and talent',
    },
    'bryce_young_support': {
        'mcmillan_addition': "6'4\" receiver compared to Mike Evans",
        'dalton_retention': 'Veteran mentor retained',
        'o_line_continuity': 'All 5 starters return healthy',
        'year_3_pressure': 'Critical evaluation season',
    },
    'cap_management': {
        'current_space': '$18.7-21.6M',
        'dead_money': '$8.8M (cleanest in years)',
        '2027_projection': '$104.6M in cap space',
        'philosophy': 'Clean cap sheet, no restructures',
    },
    'roster_construction': {
        'rookies_on_roster': 27,  # Extraordinary youth
        'avg_age': 'Youngest roster in NFC South',
        'contracts': 'Short-term deals maintain flexibility',
        'window': '2026-2027 when rookies hit stride',
    },
    'remaining_holes': {
        'linebacker': 'Glaring weakness after Thompson',
        'rb_depth': 'Brooks ACL tear (out 2025)',
        'wr_depth': 'Relying heavily on rookies',
        'experience': 'Lost veteran leadership',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Bryce Young',
        'backup': 'Andy Dalton',
        'grade': 'C+',
        'notes': 'Year 3 critical for Young development',
    },
    'offensive_line': {
        'starters': ['Ikem Ekwonu (LT)', 'Brady Christensen (LG)', 'Austin Corbett (C)', 
                     'Damien Lewis (RG)', 'Taylor Moton (RT)'],
        'grade': 'B+',
        'notes': 'All 5 starters return healthy, major plus',
    },
    'skill_positions': {
        'wr': 'Tetairoa McMillan, Xavier Legette, Adam Thielen, Jonathan Mingo',
        'rb': 'Rico Dowdle, Trevor Etienne, Raheem Blackshear',
        'te': 'Tommy Tremble, Mitchell Evans',
        'grade': 'B+',
        'notes': 'McMillan transforms WR room, RB depth concern',
    },
    'defensive_line': {
        'dt': 'Tershawn Wharton, Bobby Brown III, Derrick Brown',
        'edge': 'Patrick Jones II, Nic Scourton, Princely Umanmielen',
        'grade': 'B',
        'notes': 'Massive investment should improve 32 sacks',
    },
    'linebackers': {
        'starters': 'Josey Jewell, Christian Rozeboom',
        'depth': 'Trevin Wallace',
        'grade': 'D+',
        'notes': 'Major weakness after Thompson departure',
    },
    'secondary': {
        'cb': 'Jaycee Horn (highest-paid DB), Mike Jackson',
        'safety': "Tre'von Moehrig, Lathan Ransom",
        'grade': 'A-',
        'notes': 'Horn anchors elite potential unit',
    },
}

# ========== DIVISION & SCHEDULE ANALYSIS ==========
DIVISION_ANALYSIS = {
    'panthers_outlook': {
        'strengths': ['Elite WR talent', 'Defensive investment', 'Clean cap', 'Coaching continuity'],
        'weaknesses': ['QB uncertainty', 'LB depth', 'Youth/inexperience', 'Brutal division'],
        'x_factors': ['Young Year 3 leap', 'McMillan impact', 'Defensive cohesion'],
    },
    'division_competition': {
        'buccaneers': 'Heavy favorites with continuity',
        'falcons': 'Direct competition, aggressive rebuild',
        'saints': 'Transition year with cap issues',
    },
    'realistic_timeline': {
        '2025': 'Evaluation year, 6-7 wins likely',
        '2026': 'Competitive with cap space + development',
        '2027': 'Championship window opens if Young develops',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 7.5,
        'lean': 'UNDER',
        'reasoning': 'Too young, brutal division, QB questions',
    },
    'division_odds': {
        'current': '+350',
        'value': 'NO',
        'reasoning': 'Not ready to compete with TB/ATL',
    },
    'futures': {
        'playoffs': 'NO (-250)',
        'young_oroy': 'NO - too difficult division',
        'mcmillan_oroy': 'YES (+1200) dark horse',
    },
    'player_props': {
        'young_passing_yards': 'OVER 3,600',
        'mcmillan_receiving_yards': 'OVER 850',
        'horn_interceptions': 'OVER 3.5',
    },
    'best_bets': {
        'season': 'Under 7.5 wins',
        'week_1': 'Fade as home favorites',
        'futures': 'McMillan OROY value',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("CAROLINA PANTHERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {PANTHERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{PANTHERS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {PANTHERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {PANTHERS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {PANTHERS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Draft Picks: {PANTHERS_2025_SUMMARY['draft_picks']}")
    print(f"  • Coaching Continuity: First time since 2019!")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${PANTHERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Defensive FA Investment: ${PANTHERS_2025_SUMMARY['defensive_investment']:,}")
    print(f"  • Dead Money: ${PANTHERS_2025_SUMMARY['dead_money']:,} (cleanest in years)")
    print(f"  • Cap Space: ${PANTHERS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2027 Projection: $104.6M in space!")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Tetairoa McMillan (WR) - #8 overall, Bryce's new weapon")
    print("  • Tershawn Wharton (DT) - 3yr/$54M from Chiefs")
    print("  • Tre'von Moehrig (S) - 3yr/$51M from Raiders")
    print("  • Jaycee Horn Extension - $100M, highest-paid DB")
    
    print("\n❌ KEY LOSSES:")
    print("  • Shaq Thompson (LB) - 13-year franchise legend")
    print("  • Xavier Woods (S) - Played all 1,218 snaps")
    print("  • Miles Sanders (RB) - Released, saved $5.2M")
    print("  • Diontae Johnson/Jonathan Mingo - Traded for picks")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {PANTHERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {PANTHERS_2025_SUMMARY['division_outlook']}")
    print(f"  • Defensive Fix: From 534 points allowed to $126M investment")
    print(f"  • Youth Movement: 27 rookies on roster!")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 7.5: Take the {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Value: {BETTING_OUTLOOK['best_bets']['futures']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Bryce Young Year 3 make-or-break season")
    print("  • McMillan must be immediate impact player")
    print("  • Linebacker remains massive hole")
    print("  • 2025 is evaluation year, not competition")

if __name__ == "__main__":
    generate_summary_report()
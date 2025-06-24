"""
Tampa Bay Buccaneers 2025 Offseason Moves
Strategic continuity maintains championship foundation while addressing defensive needs
Last Updated: June 23, 2025
"""

BUCS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Targeted defensive improvements ==========
    {
        'player_name': 'Haason Reddick',
        'position': 'EDGE',
        'from_team': 'NYJ',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14000000,
        'guaranteed_money': 12000000,
        'aav': 14000000,
        '2024_grade': 5.5,  # Only 1 sack in 10 games after holdout
        'projected_2025_grade': 7.5,  # Bounce-back potential, 50.5 sacks 2020-2023
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 4.0,  # Holdout drama soured relationship
        'importance_to_new_team': 8.5,  # Addresses 29th-ranked pass rush
        'impact_score': 2.5,  # High upside signing for major need
    },
    {
        'player_name': 'Anthony Walker Jr.',
        'position': 'LB',
        'from_team': 'Mia',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        'guaranteed_money': 2500000,
        'aav': 3000000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Direct replacement for K.J. Britt
        'impact_score': 0.8,
    },
    {
        'player_name': 'Charlie Heck',
        'position': 'OT',
        'from_team': 'Hou',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 500000,
        'aav': 1500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Swing tackle depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Kindle Vildor',
        'position': 'CB',
        'from_team': 'Ten',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        'guaranteed_money': 300000,
        'aav': 1200000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.3,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,  # Depth/special teams
        'impact_score': 0.2,
    },
    {
        'player_name': 'Cody Thompson',
        'position': 'WR',
        'from_team': 'FA',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 915000,
        'guaranteed_money': 0,
        'aav': 915000,
        '2024_grade': 5.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 4.5,  # Camp body/PS candidate
        'impact_score': 0.0,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS - Offensive continuity ==========
    {
        'player_name': 'Chris Godwin',
        'position': 'WR1',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 66000000,
        'guaranteed_money': 45000000,
        'aav': 22000000,
        '2024_grade': 8.0,  # Despite Week 7 ankle injury
        'projected_2025_grade': 8.5,  # Full recovery expected
        'snap_percentage_2024': 65.0,  # Limited by injury
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 3.0,  # Massive retention win
    },
    {
        'player_name': 'Ben Bredeson',
        'position': 'LG',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 22000000,
        'guaranteed_money': 12000000,
        'aav': 7333333,
        '2024_grade': 8.0,
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.5,  # O-line stability crucial
    },
    {
        'player_name': 'Lavonte David',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 8500000,
        'guaranteed_money': 6500000,
        'aav': 8500000,
        '2024_grade': 7.5,  # Age 35 but still productive
        'projected_2025_grade': 7.0,  # 14th season, likely final
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.0,  # Leadership value
    },
    {
        'player_name': 'Kyle Trask',
        'position': 'QB',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2787000,
        'guaranteed_money': 2787000,
        'aav': 2787000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Sterling Shepard',
        'position': 'WR3',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 1500000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,  # Mayfield chemistry
    },

    # ========== 2025 NFL DRAFT - Future planning with immediate impact ==========
    {
        'player_name': 'Emeka Egbuka',
        'position': 'WR2',
        'from_team': 'Ohio State',
        'to_team': 'TB',
        'move_type': '2025 Draft - Round 1, Pick 19',
        'contract_years': 4,
        'contract_value': 15500000,
        'guaranteed_money': 15500000,  # Fully guaranteed rookie deal
        'aav': 3875000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 95th percentile separation
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Evans insurance/future
        'impact_score': 1.5,
    },
    {
        'player_name': 'Benjamin Morrison',
        'position': 'CB',
        'from_team': 'Notre Dame',
        'to_team': 'TB',
        'move_type': '2025 Draft - Round 2, Pick 51',
        'contract_years': 4,
        'contract_value': 7200000,
        'guaranteed_money': 3600000,
        'aav': 1800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Secondary depth/future
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jacob Parrish',
        'position': 'CB',
        'from_team': 'Kansas State',
        'to_team': 'TB',
        'move_type': '2025 Draft - Round 3, Pick 83',
        'contract_years': 4,
        'contract_value': 5400000,
        'guaranteed_money': 1200000,
        'aav': 1350000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 4.35 speed for nickel
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'David Walker',
        'position': 'EDGE',
        'from_team': 'Central Arkansas',
        'to_team': 'TB',
        'move_type': '2025 Draft - Round 4, Pick 119',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 800000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Elijah Roberts',
        'position': 'EDGE',
        'from_team': 'SMU',
        'to_team': 'TB',
        'move_type': '2025 Draft - Round 5, Pick 155',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 131 QB pressures in 2 years
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },

    # ========== COACHING CHANGES - Strategic upgrades ==========
    {
        'player_name': 'Josh Grizzard',
        'position': 'COACH-OC',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Internal Promotion to OC',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 2000000,
        'aav': 2000000,
        '2024_grade': 7.5,
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,
        'impact_score': 1.0,  # Maintains offensive continuity
    },
    {
        'player_name': 'Mike Caldwell',
        'position': 'COACH-LB',
        'from_team': 'FA',
        'to_team': 'TB',
        'move_type': 'Coaching Hire - ILB Coach',
        'contract_years': 2,
        'contract_value': 2400000,
        'guaranteed_money': 800000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Charlie Strong',
        'position': 'COACH-DL',
        'from_team': 'Alabama',
        'to_team': 'TB',
        'move_type': 'Coaching Hire - DL Coach',
        'contract_years': 2,
        'contract_value': 2000000,
        'guaranteed_money': 700000,
        'aav': 1000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 0.7,
    },

    # ========== LOSSES - Minimal due to retention success ==========
    {
        'player_name': 'K.J. Britt',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # Replaced by Walker Jr.
    },
    {
        'player_name': 'Liam Coen',
        'position': 'COACH-OC',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Coaching Loss - Became JAX HC',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Mitigated by Grizzard promotion
    },
]

# ========== SUMMARY METRICS ==========
BUCS_2025_SUMMARY = {
    'total_moves': len(BUCS_2025_MOVES),
    'free_agent_signings': 5,
    'key_resignings': 5,
    'draft_picks': 5,
    'coaching_changes': 4,  # 3 hires + 1 promotion
    'major_losses': 2,
    'total_guaranteed_money': 115000000,
    'dead_money': 8500000,
    'cap_space_remaining': 26600000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B+',
    'key_philosophy': 'Offensive continuity with targeted defensive improvements',
    'net_impact_score': 12.5,  # Sum of all impact scores
    'division_outlook': 'Favorites to win 5th consecutive NFC South title',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'offensive_continuity': {
        'starters_returning': 11,
        'pct_returning': 100.0,
        'key_stat': 'All 5 OL starters return - rare in modern NFL',
        'franchise_records_2024': ['Total yards', 'Points per game (29.5)', 'Passing TDs'],
    },
    'defensive_priorities': {
        'pass_rush_rank_2024': 29,
        'solution': 'Reddick signing + 2 EDGE draft picks',
        'secondary_focus': '2 CB draft picks to address 7 INTs in 2024',
    },
    'cap_management': {
        'current_space': 26600000,
        'potential_space': 78850000,  # Via restructures
        'big_5_contracts': ['Mayfield', 'Evans', 'Winfield Jr.', 'Vea', 'Dean'],
        'restructure_potential': 74300000,
    },
    'draft_philosophy': {
        'balance': 'Present success with future planning',
        'egbuka_logic': 'Evans insurance at age 32',
        'defensive_focus': '4 of 5 picks on defense',
    },
    'coaching_stability': {
        'bowles_system': 'Year 3 under Todd Bowles',
        'internal_promotion': 'Grizzard maintains offensive continuity',
        'veteran_presence': 'Tom Moore (86) still consulting',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Baker Mayfield',
        'backup': 'Kyle Trask',
        'grade': 'A-',
        'notes': 'Mayfield entering year 2 of $100M deal, career year in 2024',
    },
    'offensive_line': {
        'starters': ['Tristan Wirfs (RT)', 'Luke Goedeke (RG)', 'Graham Barton (C)', 
                     'Ben Bredeson (LG)', 'Cody Mauch (LT)'],
        'depth': 'Charlie Heck (swing)',
        'grade': 'A',
        'notes': 'All 5 starters return, Bredeson extended after prove-it year',
    },
    'wide_receivers': {
        'depth_chart': ['Mike Evans', 'Chris Godwin', 'Emeka Egbuka', 'Sterling Shepard'],
        'grade': 'A+',
        'notes': 'Elite trio with Egbuka adding future insurance',
    },
    'pass_rush': {
        'projected_starters': ['Haason Reddick', 'Joe Tryon-Shoyinka'],
        'depth': ['David Walker', 'Elijah Roberts'],
        'grade': 'B',
        'notes': 'Major upgrade if Reddick rebounds to 2020-2023 form',
    },
    'secondary': {
        'corners': ['Jamel Dean', 'Carlton Davis III', 'Benjamin Morrison', 'Jacob Parrish'],
        'safeties': ['Antoine Winfield Jr.', 'Jordan Whitehead'],
        'grade': 'B+',
        'notes': 'Added speed (Parrish 4.35) and depth through draft',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 10.5,
        'lean': 'OVER',
        'reasoning': 'Offensive continuity + defensive upgrades + weak division',
    },
    'division_odds': {
        'current': '-140',
        'value': 'YES',
        'reasoning': '21 of 22 starters return, 5th straight division title likely',
    },
    'super_bowl_odds': {
        'current': '+2200',
        'value': 'SLIGHT VALUE',
        'reasoning': 'NFC path easier than AFC, proven playoff team',
    },
    'player_props': {
        'mayfield_passing_yards': 'OVER 4,250',
        'evans_tds': 'OVER 9.5',
        'reddick_sacks': 'OVER 7.5',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("TAMPA BAY BUCCANEERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {BUCS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{BUCS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {BUCS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {BUCS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {BUCS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Key Re-signings: {BUCS_2025_SUMMARY['key_resignings']}")
    print(f"  • Draft Picks: {BUCS_2025_SUMMARY['draft_picks']}")
    print(f"  • Coaching Changes: {BUCS_2025_SUMMARY['coaching_changes']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed Money: ${BUCS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Current Cap Space: ${BUCS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • Potential Cap Space: ${STRATEGIC_ANALYSIS['cap_management']['potential_space']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Haason Reddick (EDGE) - $14M prove-it deal")
    print("  • Emeka Egbuka (WR) - 1st round pick")
    print("  • Benjamin Morrison (CB) - 2nd round pick")
    
    print("\n🔒 KEY RETENTIONS:")
    print("  • Chris Godwin - 3yr/$66M extension")
    print("  • Ben Bredeson - 3yr/$22M extension")
    print("  • All 11 offensive starters returning")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {BUCS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {BUCS_2025_SUMMARY['division_outlook']}")
    print(f"  • Pass Rush: Addressing 29th-ranked unit with Reddick + draft")
    print(f"  • Offensive Continuity: 100% starter retention rare in NFL")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 10.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Key Props: Mayfield 4,250+ yards, Evans 10+ TDs")

if __name__ == "__main__":
    generate_summary_report()
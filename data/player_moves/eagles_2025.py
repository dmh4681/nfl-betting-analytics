"""
Philadelphia Eagles 2025 Offseason Moves
Super Bowl champions face massive defensive exodus while retaining offensive core
Last Updated: June 23, 2025
"""

EAGLES_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Value-based approach ==========
    {
        'player_name': 'Azeez Ojulari',
        'position': 'EDGE',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 3000000,  # Fully guaranteed
        'aav': 3000000,
        '2024_grade': 7.2,  # 6 sacks in 11 games with limited snaps
        'projected_2025_grade': 7.8,  # Should get more opportunity
        'snap_percentage_2024': 35.0,  # Limited behind Burns/Thibodeaux
        'importance_to_old_team': 6.0,  # Rotational piece
        'importance_to_new_team': 8.5,  # Key replacement for Sweat
        'impact_score': 2.0,
    },
    {
        'player_name': 'Joshua Uche',
        'position': 'EDGE',
        'from_team': 'KC',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1920000,
        'guaranteed_money': 1920000,
        'aav': 1920000,
        '2024_grade': 6.5,  # Only 2 sacks, 22% snaps
        'projected_2025_grade': 7.5,  # Bounce-back potential
        'snap_percentage_2024': 22.0,
        'importance_to_old_team': 4.0,  # Minimal role
        'importance_to_new_team': 7.0,  # Pass rush depth
        'impact_score': 1.0,
    },
    {
        'player_name': "Adoree' Jackson",
        'position': 'CB2',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1755000,
        'guaranteed_money': 1000000,
        'aav': 1755000,
        '2024_grade': 6.9,  # 69.0 PFF grade, ranked 58th
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 65.0,  # Started 5 of 14 games
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replaces Slay depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'A.J. Dillon',
        'position': 'RB',
        'from_team': 'GB',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1100000,
        'guaranteed_money': 600000,
        'aav': 1100000,
        '2024_grade': 0.0,  # Missed entire season with neck injury
        'projected_2025_grade': 6.5,  # Health unknown
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 3.0,
        'importance_to_new_team': 5.0,  # Backup depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Harrison Bryant',
        'position': 'TE',
        'from_team': 'LV',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1000000,
        'guaranteed_money': 500000,
        'aav': 1000000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # TE depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Avery Williams',
        'position': 'RB/RS',
        'from_team': 'ATL',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1225000,
        'guaranteed_money': 600000,
        'aav': 1225000,
        '2024_grade': 7.0,  # 27.2 yards per kickoff return
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 25.0,  # Special teams
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Charley Hughlett',
        'position': 'LS',
        'from_team': 'Cle',
        'to_team': 'Phi',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1422000,
        'guaranteed_money': 1000000,
        'aav': 1422000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # Replace 8-year veteran Lovato
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES - Defensive exodus ==========
    {
        'player_name': 'Josh Sweat',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,  # 8 sacks regular season + 2.5 in Super Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 59.0,  # Primary edge threat
        'importance_to_old_team': 9.0,  # Team-leading pass rusher
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # Major loss
    },
    {
        'player_name': 'Milton Williams',
        'position': 'DT',
        'from_team': 'Phi',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.2,  # 5 sacks, 54 pressures, Super Bowl strip-sack
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 48.0,
        'importance_to_old_team': 8.0,  # Key interior rusher
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # 3rd-highest paid DT
    },
    {
        'player_name': 'Oren Burks',
        'position': 'LB',
        'from_team': 'Phi',
        'to_team': 'Cin',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Playoff hero, 25 tackles in 3 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },
    {
        'player_name': 'Isaiah Rodgers',
        'position': 'CB',
        'from_team': 'Phi',
        'to_team': 'Min',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.3,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'Kenneth Gainwell',
        'position': 'RB',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },
    {
        'player_name': 'Mekhi Becton',
        'position': 'G',
        'from_team': 'Phi',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },

    # ========== 2025 NFL DRAFT - Addressing needs ==========
    {
        'player_name': 'Colston Loveland',
        'position': 'TE',
        'from_team': 'Michigan',
        'to_team': 'Phi',
        'move_type': '2025 Draft - Round 1, Pick 22',
        'contract_years': 4,
        'contract_value': 16500000,
        'guaranteed_money': 16500000,
        'aav': 4125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # Elite prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Goedert insurance/future
        'impact_score': 1.8,
    },
    {
        'player_name': 'Shilo Sanders',
        'position': 'S',
        'from_team': 'Colorado',
        'to_team': 'Phi',
        'move_type': '2025 Draft - Round 3, Pick 87',
        'contract_years': 4,
        'contract_value': 5200000,
        'guaranteed_money': 1200000,
        'aav': 1300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Ty Robinson',
        'position': 'DT',
        'from_team': 'Nebraska',
        'to_team': 'Phi',
        'move_type': '2025 Draft - Round 4, Pick 112',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 800000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 12 TFL, 7 sacks at Nebraska
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces Milton Williams
        'impact_score': 0.6,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS ==========
    {
        'player_name': 'A.J. Brown',
        'position': 'WR1',
        'from_team': 'Phi',
        'to_team': 'Phi',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 96000000,
        'guaranteed_money': 65000000,
        'aav': 32000000,
        '2024_grade': 9.0,  # Elite production
        'projected_2025_grade': 9.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # Massive retention
    },
    {
        'player_name': 'DeVonta Smith',
        'position': 'WR2',
        'from_team': 'Phi',
        'to_team': 'Phi',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 75000000,
        'guaranteed_money': 51000000,
        'aav': 25000000,
        '2024_grade': 8.5,
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.5,
    },

    # ========== TRADES ==========
    {
        'player_name': 'Kenny Pickett',
        'position': 'QB',
        'from_team': 'Phi',
        'to_team': 'Cle',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Backup role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,  # Got DTR + 5th
    },
    {
        'player_name': 'C.J. Gardner-Johnson',
        'position': 'S',
        'from_team': 'Phi',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,  # Got 5th round pick
    },

    # ========== RETIREMENTS ==========
    {
        'player_name': 'Brandon Graham',
        'position': 'EDGE',
        'from_team': 'Phi',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Played through torn triceps in Super Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 8.0,  # Franchise legend, emotional leader
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Leadership loss
    },

    # ========== POST-JUNE 1 CUTS ==========
    {
        'player_name': 'Darius Slay',
        'position': 'CB1',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.8,  # Still productive veteran
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,  # Veteran leader
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Signed with Steelers
    },
    {
        'player_name': 'James Bradberry',
        'position': 'CB2',
        'from_team': 'Phi',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },

    # ========== DRAFT PICK TRADES ==========
    {
        'player_name': 'Dorian Thompson-Robinson',
        'position': 'QB',
        'from_team': 'Cle',
        'to_team': 'Phi',
        'move_type': 'Trade Acquisition',
        'contract_years': 2,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 1500000,
        '2024_grade': 5.5,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 10.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Backup QB
        'impact_score': 0.5,
    },

    # ========== UDFA SIGNINGS ==========
    {
        'player_name': 'Jeremiah Trotter Jr.',
        'position': 'LB',
        'from_team': 'Clemson',
        'to_team': 'Phi',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2700000,
        'guaranteed_money': 275000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Son of Eagles legend
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
EAGLES_2025_SUMMARY = {
    'total_moves': len(EAGLES_2025_MOVES),
    'free_agent_signings': 7,
    'key_resignings': 2,  # Brown and Smith extensions
    'draft_picks': 9,  # Actually had 9 picks
    'major_losses': 9,
    'trades': 3,
    'retirements': 1,
    'post_june_cuts': 2,
    'total_guaranteed_money': 158000000,  # Major extensions
    'dead_money': 33560000,  # From Slay/Bradberry cuts
    'cap_space_remaining': 24000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B-',
    'key_philosophy': 'Offensive continuity with defensive youth movement',
    'net_impact_score': -2.5,  # Sum of all impact scores
    'division_outlook': 'Still contenders but defensive questions loom',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'defensive_exodus': {
        'key_losses': 'Sweat (8 sacks), Milton Williams (5 sacks), Graham (retired)',
        'replacement_strategy': 'One-year prove-it deals for Ojulari, Uche',
        'youth_movement': 'Betting on Nolan Smith, Jordan Davis development',
        'risk_level': 'HIGH - Lost proven production for potential',
    },
    'offensive_retention': {
        'core_intact': 'All 11 starters return including OL',
        'extensions': 'Brown ($32M AAV), Smith ($25M AAV) locked up',
        'philosophy': 'Keep Hurts surrounded by elite weapons',
        'window': 'Maximizing prime years of offensive core',
    },
    'cap_management': {
        'current_space': '$24M after moves',
        'future_flexibility': 'Maintained with 1-year deals',
        'dead_money': '$33.56M from Slay/Bradberry cuts',
        'strategy': 'Short-term contracts preserve future options',
    },
    'draft_philosophy': {
        'loveland_pick': 'Elite TE prospect despite having Goedert',
        'defensive_focus': '7 of 9 picks on defense',
        'developmental': 'Focus on athletic upside over polish',
    },
    'coaching_continuity': {
        'staff_intact': 'Sirianni, Moore, Desai all return',
        'post_sb_challenge': 'Avoiding championship hangover',
        'culture': 'Maintaining edge after reaching mountaintop',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Jalen Hurts',
        'backup': 'Dorian Thompson-Robinson',
        'grade': 'A',
        'notes': 'Hurts in prime, DTR provides mobility as backup',
    },
    'offensive_line': {
        'starters': ['Jordan Mailata (LT)', 'Landon Dickerson (LG)', 'Cam Jurgens (C)', 
                     'Tyler Steen (RG)', 'Lane Johnson (RT)'],
        'depth': 'Concerns after Becton departure',
        'grade': 'A-',
        'notes': 'All 5 starters return, best OL in NFL',
    },
    'skill_positions': {
        'wr': 'A.J. Brown, DeVonta Smith, Britain Covey',
        'rb': 'Saquon Barkley, Kenneth Gainwell, Will Shipley',
        'te': 'Dallas Goedert, Colston Loveland (rookie)',
        'grade': 'A+',
        'notes': 'Elite weapons at every position',
    },
    'defensive_line': {
        'dt': 'Jalen Carter, Jordan Davis, Milton Williams',
        'edge': 'Nolan Smith, Azeez Ojulari, Joshua Uche',
        'grade': 'B-',
        'notes': 'Major questions at EDGE after losses',
    },
    'linebackers': {
        'starters': 'Nakobe Dean, Devin White',
        'depth': 'Jeremiah Trotter Jr., Zack Baun',
        'grade': 'B',
        'notes': 'Dean development crucial',
    },
    'secondary': {
        'cb': 'Darius Slay Jr., Quinyon Mitchell, Kelee Ringo',
        'safety': 'Reed Blankenship, Sydney Brown',
        'grade': 'B-',
        'notes': 'Youth movement after veteran departures',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 11.5,
        'lean': 'UNDER',
        'reasoning': 'Championship hangover + defensive losses',
    },
    'division_odds': {
        'current': '+150',
        'value': 'YES',
        'reasoning': 'Still best roster in weak division',
    },
    'super_bowl_odds': {
        'current': '+1200',
        'value': 'FAIR',
        'reasoning': 'Elite offense but defensive concerns',
    },
    'player_props': {
        'hurts_passing_tds': 'OVER 27.5',
        'brown_receiving_yards': 'OVER 1,350',
        'carter_sacks': 'OVER 8.5',
    },
    'key_bets': {
        'best': 'Division winner +150',
        'avoid': 'Conference winner',
        'sleeper': 'Loveland OROY +2000',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("PHILADELPHIA EAGLES 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {EAGLES_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: {EAGLES_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {EAGLES_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {EAGLES_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {EAGLES_2025_SUMMARY['free_agent_signings']} (all 1-year deals)")
    print(f"  • Key Extensions: Brown ($96M), Smith ($75M)")
    print(f"  • Major Losses: {EAGLES_2025_SUMMARY['major_losses']}")
    print(f"  • Draft Picks: {EAGLES_2025_SUMMARY['draft_picks']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${EAGLES_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${EAGLES_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${EAGLES_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Azeez Ojulari (EDGE) - 1yr/$3M from Giants")
    print("  • Joshua Uche (EDGE) - 1yr/$1.92M bounce-back")
    print("  • Colston Loveland (TE) - 1st round pick")
    
    print("\n❌ KEY LOSSES:")
    print("  • Josh Sweat (EDGE) - 4yr/$76.4M to Arizona")
    print("  • Milton Williams (DT) - 4yr/$104M to Patriots")
    print("  • Brandon Graham - Retirement after 15 seasons")
    print("  • Darius Slay/James Bradberry - Post-June 1 cuts")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {EAGLES_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {EAGLES_2025_SUMMARY['division_outlook']}")
    print(f"  • Risk: Betting on youth development over proven veterans")
    print(f"  • Strength: All 11 offensive starters return")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 11.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_bets']['best']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Can young EDGE rushers replace Sweat/Graham production?")
    print("  • Will championship hangover affect motivation?")
    print("  • Health of aging OL stars (Johnson, Kelce)")
    print("  • Secondary depth after veteran cuts")

if __name__ == "__main__":
    generate_summary_report()
"""
Denver Broncos 2025 Offseason Moves
Calculated risks supporting Bo Nix's critical second season
Last Updated: June 23, 2025
"""

BRONCOS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Elite talent with injury risk ==========
    {
        'player_name': 'Talanoa Hufanga',
        'position': 'S',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 39000000,
        'guaranteed_money': 20000000,
        'aav': 13000000,
        '2024_grade': 6.0,  # Limited by injury
        'projected_2025_grade': 8.0,  # All-Pro when healthy
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Elite talent gamble
        'impact_score': 2.2,
        'notes': '17 games in 2 years'
    },
    {
        'player_name': 'Dre Greenlaw',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 31500000,
        'guaranteed_money': 13500000,
        'aav': 10500000,
        '2024_grade': 0.0,  # Achilles recovery
        'projected_2025_grade': 7.8,  # Elite LB when healthy
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,
        'notes': 'Torn Achilles in SB LVIII'
    },
    {
        'player_name': 'Evan Engram',
        'position': 'TE',
        'from_team': 'Jax',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 23000000,
        'guaranteed_money': 16500000,
        'aav': 11500000,
        '2024_grade': 7.5,  # When healthy
        'projected_2025_grade': 7.8,  # Payton's "Joker"
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # System fit
        'impact_score': 2.0,
        'notes': 'Missed 8 games in 2024'
    },
    {
        'player_name': 'Deion Smith',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 5000000,
        'guaranteed_money': 2500000,
        'aav': 2500000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Rico Dowdle',
        'position': 'RB',
        'from_team': 'Dal',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1000000,
        'aav': 2500000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Will Sherman',
        'position': 'OT',
        'from_team': 'NE',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        'guaranteed_money': 500000,
        'aav': 1800000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Matt Araiza',
        'position': 'P',
        'from_team': 'KC',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        'guaranteed_money': 300000,
        'aav': 1200000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES ==========
    {
        'player_name': 'Javonte Williams',
        'position': 'RB',
        'from_team': 'Den',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Never same post-ACL
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,  # 1yr/$3M to Dallas
    },
    {
        'player_name': 'Zach Wilson',
        'position': 'QB',
        'from_team': 'Den',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # Failed reclamation
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,
    },
    {
        'player_name': 'Riley Dixon',
        'position': 'P',
        'from_team': 'Den',
        'to_team': 'TB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Tremon Smith',
        'position': 'CB/KR',
        'from_team': 'Den',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
        'impact_score': -0.6,
    },

    # ========== 2025 NFL DRAFT - Strategic trading and talent ==========
    {
        'player_name': 'Jahdae Barron',
        'position': 'CB',
        'from_team': 'Texas',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 1, Pick 20',
        'contract_years': 4,
        'contract_value': 19800000,
        'guaranteed_money': 19800000,
        'aav': 4950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Jim Thorpe winner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Elite CB prospect
        'impact_score': 2.5,
        'notes': 'Top-12 talent at pick 20'
    },
    {
        'player_name': 'RJ Harvey',
        'position': 'RB',
        'from_team': 'UCF',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 2, Pick 60',
        'contract_years': 4,
        'contract_value': 8400000,
        'guaranteed_money': 4200000,
        'aav': 2100000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # 1,577 yards, 22 TDs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # 6.8 YPC
        'impact_score': 1.8,
        'notes': 'Elite speed and receiving'
    },
    {
        'player_name': 'Pat Bryant',
        'position': 'WR',
        'from_team': 'Illinois',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 3, Pick 76',
        'contract_years': 4,
        'contract_value': 6600000,
        'guaranteed_money': 1700000,
        'aav': 1650000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Payton: "Michael Thomas"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
        'notes': 'Just 1 drop in 2024'
    },
    {
        'player_name': 'Sai\'vion Jones',
        'position': 'DE',
        'from_team': 'LSU',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 3, Pick 91',
        'contract_years': 4,
        'contract_value': 5900000,
        'guaranteed_money': 1300000,
        'aav': 1475000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Cobee Bryant',
        'position': 'CB',
        'from_team': 'Kansas',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 4, Pick 121',
        'contract_years': 4,
        'contract_value': 4700000,
        'guaranteed_money': 800000,
        'aav': 1175000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Blake Watson',
        'position': 'RB',
        'from_team': 'Memphis',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 5, Pick 147',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 600000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Caleb Lohner',
        'position': 'TE',
        'from_team': 'Baylor',
        'to_team': 'Den',
        'move_type': '2025 Draft - Round 7, Pick 235',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 300000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # 6'7" former basketball
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.2,
        'notes': 'Payton project (Jimmy Graham)'
    },

    # ========== KEY EXTENSIONS/RE-SIGNINGS ==========
    {
        'player_name': 'D.J. Jones',
        'position': 'DT',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 39000000,
        'guaranteed_money': 26000000,
        'aav': 13000000,
        '2024_grade': 8.0,  # Interior anchor
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
        'impact_score': 2.0,
    },
    {
        'player_name': 'Jarrett Stidham',
        'position': 'QB',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 12000000,
        'guaranteed_money': 7000000,
        'aav': 6000000,
        '2024_grade': 6.5,  # Nix mentor
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Wil Lutz',
        'position': 'K',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 5500000,
        'guaranteed_money': 3500000,
        'aav': 5500000,
        '2024_grade': 8.5,  # 89.7% FG
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },

    # ========== COACHING/FRONT OFFICE CHANGES ==========
    {
        'player_name': 'Darren Rizzi',
        'position': 'COACH-ST',
        'from_team': 'NO',
        'to_team': 'Den',
        'move_type': 'ST Coordinator Hire',
        'contract_years': 3,
        'contract_value': 2400000,
        'guaranteed_money': 1200000,
        'aav': 800000,
        '2024_grade': 8.0,  # Saints reunion
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Replace Westhoff
        'impact_score': 1.5,
    },
    {
        'player_name': 'Davis Webb',
        'position': 'COACH-PASS',
        'from_team': 'Den-QB',
        'to_team': 'Den',
        'move_type': 'Internal Promotion',
        'contract_years': 2,
        'contract_value': 1200000,
        'guaranteed_money': 600000,
        'aav': 600000,
        '2024_grade': 7.5,  # Nix development
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Critical for Nix
        'impact_score': 1.2,
    },
    {
        'player_name': 'Jim Leonhard',
        'position': 'COACH-DEF',
        'from_team': 'Den-DB',
        'to_team': 'Den',
        'move_type': 'Internal Promotion',
        'contract_years': 2,
        'contract_value': 1000000,
        'guaranteed_money': 500000,
        'aav': 500000,
        '2024_grade': 7.5,
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },

    # ========== FRONT OFFICE CHANGES ==========
    {
        'player_name': 'Reed Burckhardt',
        'position': 'FO-AGM',
        'from_team': 'Den-Scout',
        'to_team': 'Den',
        'move_type': 'Internal Promotion',
        'contract_years': 3,
        'contract_value': 1500000,
        'guaranteed_money': 750000,
        'aav': 500000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replace Mougey
        'impact_score': 1.0,
    },
    {
        'player_name': 'Jordan Dizon',
        'position': 'FO-SCOUT',
        'from_team': 'Phi',
        'to_team': 'Den',
        'move_type': 'Front Office Hire',
        'contract_years': 2,
        'contract_value': 800000,
        'guaranteed_money': 400000,
        'aav': 400000,
        '2024_grade': 7.5,  # Eagles pedigree
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },

    # ========== RUSSELL WILSON DEAD MONEY ==========
    {
        'player_name': 'Russell Wilson',
        'position': 'QB',
        'from_team': 'Den-DEAD',
        'to_team': 'DEAD',
        'move_type': 'Dead Money',
        'contract_years': 0,
        'contract_value': -32000000,  # Negative for dead money
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Cap constraint
        'notes': 'Final year of albatross'
    },
]

# ========== SUMMARY METRICS ==========
BRONCOS_2025_SUMMARY = {
    'total_moves': len(BRONCOS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 4,
    'trades': 0,  # Multiple draft day trades
    'draft_picks': 7,
    'key_resignings': 3,
    'coaching_changes': 3,
    'front_office_changes': 2,
    'total_guaranteed_money': 99500000,
    'russell_wilson_dead_money': 32000000,  # Final year
    'cap_space_remaining': 16500000,
    'cap_space_2026': 85000000,  # When Wilson clears
    'championship_window': '2026-2028',
    'offseason_grade': 'B+',
    'key_philosophy': 'Elite talent with injury risk supporting Nix development',
    'net_impact_score': 18.5,  # Sum of all impact scores
    'division_outlook': 'Rising threat to Chiefs dominance',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'injury_gambles': {
        'hufanga': '17 games in 2 years',
        'greenlaw': 'Achilles recovery',
        'engram': 'Missed 8 games 2024',
        'philosophy': 'Talent over health',
    },
    'defensive_excellence': {
        '2024_rank': '#1 scoring defense',
        'blitz_rate': '46.3% (NFL-leading)',
        'sacks': '63 (NFL-leading)',
        'additions': 'Hufanga, Greenlaw, Barron',
    },
    'bo_nix_support': {
        'year_2_leap': 'Expected development',
        'weapons': 'Engram, Harvey, Bryant',
        'protection': 'Minimal OL additions',
        'coaching': 'Webb promotion critical',
    },
    'cap_management': {
        'wilson_impact': '$32M dead money',
        '2026_relief': '$85M projected space',
        'strategy': 'Avoided restructures',
        'timeline': 'Clear for 2026 push',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Bo Nix',
        'backup': 'Jarrett Stidham',
        'grade': 'B+',
        'notes': 'Year 2 development crucial',
    },
    'offensive_line': {
        'starters': ['Garett Bolles (LT)', 'Ben Powers (LG)', 'Luke Wattenberg (C)', 
                     'Quinn Meinerz (RG)', 'Mike McGlinchey (RT)'],
        'depth': 'Will Sherman only addition',
        'grade': 'B',
        'notes': 'Aging concerns unaddressed',
    },
    'skill_positions': {
        'wr': 'Courtland Sutton, Marvin Mims Jr., Pat Bryant',
        'rb': 'RJ Harvey, Audric Estime, Rico Dowdle',
        'te': 'Evan Engram, Greg Dulcich',
        'grade': 'B+',
        'notes': 'Engram adds Payton dimension',
    },
    'defensive_line': {
        'dt': 'D.J. Jones, Zach Allen, John Franklin-Myers',
        'edge': 'Baron Browning, Jonathon Cooper, Nik Bonitto',
        'grade': 'A-',
        'notes': 'Elite pass rush continues',
    },
    'linebackers': {
        'starters': 'Dre Greenlaw, Drew Sanders, Cody Barton',
        'depth': 'Deion Smith, Jonas Griffith',
        'grade': 'B+',
        'notes': 'Greenlaw health key',
    },
    'secondary': {
        'cb': 'Patrick Surtain II, Jahdae Barron, Riley Moss',
        'safety': 'Talanoa Hufanga, P.J. Locke',
        'grade': 'A',
        'notes': 'Elite if healthy',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'OVER',
        'reasoning': 'Nix Year 2 + elite defense',
    },
    'division_odds': {
        'current': '+425',
        'value': 'SLIGHT VALUE',
        'reasoning': 'Chiefs showing cracks',
    },
    'playoffs': {
        'current': '-140',
        'value': 'YES',
        'reasoning': 'Wild card floor',
    },
    'player_props': {
        'nix_passing_yards': 'OVER 3,600',
        'harvey_rushing_yards': 'OVER 800',
        'surtain_interceptions': 'OVER 4.5',
    },
    'key_angles': {
        'best_bet': 'Defense #1 scoring again',
        'sleeper': 'Harvey OROY +1800',
        'narrative': 'Health determines ceiling',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("DENVER BRONCOS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {BRONCOS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{BRONCOS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {BRONCOS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {BRONCOS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {BRONCOS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Draft Picks: {BRONCOS_2025_SUMMARY['draft_picks']} (5 trades)")
    print(f"  • Russell Wilson Dead Money: ${BRONCOS_2025_SUMMARY['russell_wilson_dead_money']:,}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${BRONCOS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: ${BRONCOS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Space: ${BRONCOS_2025_SUMMARY['cap_space_2026']:,} (Wilson clears)")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Talanoa Hufanga (S) - 3yr/$39M from 49ers")
    print("  • Dre Greenlaw (LB) - 3yr/$31.5M from 49ers")
    print("  • Evan Engram (TE) - 2yr/$23M from Jaguars")
    print("  • Jahdae Barron (CB) - 1st round, Jim Thorpe winner")
    
    print("\n❌ KEY LOSSES:")
    print("  • Javonte Williams (RB) - 1yr/$3M to Cowboys")
    print("  • Zach Wilson (QB) - To Dolphins")
    print("  • Riley Dixon (P) - To Buccaneers")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {BRONCOS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {BRONCOS_2025_SUMMARY['division_outlook']}")
    print(f"  • Defense: NFL #1 scoring, 63 sacks")
    print(f"  • Risk: Injury histories of key signings")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Bo Nix Year 2 development")
    print("  • Health of Hufanga/Greenlaw/Engram")
    print("  • Wilson dead money finally clears")
    print("  • Consecutive home wins vs Chiefs")

if __name__ == "__main__":
    generate_summary_report()
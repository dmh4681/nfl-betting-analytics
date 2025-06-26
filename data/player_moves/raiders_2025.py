"""
Las Vegas Raiders 2025 Offseason Moves
Complete organizational overhaul under Carroll-Brady partnership
Last Updated: June 23, 2025
"""

RAIDERS_2025_MOVES = [
    # ========== BLOCKBUSTER TRADE - QB solution ==========
    {
        'player_name': 'Geno Smith',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'LV',
        'move_type': 'Trade + Extension',
        'contract_years': 2,
        'contract_value': 85500000,
        'guaranteed_money': 66500000,
        'aav': 42750000,
        '2024_grade': 8.0,  # 70.4% completion, 4,320 yards
        'projected_2025_grade': 8.2,  # Carroll reunion
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 10.0,  # Ends QB carousel
        'impact_score': 3.0,
        'notes': 'Traded 2025 3rd (#92) to Seattle'
    },

    # ========== FREE AGENT SIGNINGS - Targeted improvements ==========
    {
        'player_name': 'Jeremy Chinn',
        'position': 'S',
        'from_team': 'Was',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 12000000,
        'aav': 8000000,
        '2024_grade': 8.0,  # 117 tackles
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 94.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Replace Moehrig
        'impact_score': 2.0,
    },
    {
        'player_name': 'Elandon Roberts',
        'position': 'LB',
        'from_team': 'Pit',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3010000,
        'guaranteed_money': 2000000,
        'aav': 3010000,
        '2024_grade': 7.0,  # Championship experience
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Eric Stokes',
        'position': 'CB',
        'from_team': 'GB',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        'guaranteed_money': 2500000,
        'aav': 4000000,
        '2024_grade': 4.5,  # Former 1st rounder
        'projected_2025_grade': 6.5,  # Reclamation
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Devin White',
        'position': 'LB',
        'from_team': 'Phi',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        'guaranteed_money': 3000000,
        'aav': 5000000,
        '2024_grade': 6.0,  # Down year
        'projected_2025_grade': 7.0,  # Spytek reunion
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 7.5,  # Spytek drafted him
        'impact_score': 1.0,
    },
    {
        'player_name': 'Raheem Mostert',
        'position': 'RB',
        'from_team': 'Mia',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2100000,
        'guaranteed_money': 1200000,
        'aav': 2100000,
        '2024_grade': 6.5,  # Age 33
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Veteran depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Alex Cappa',
        'position': 'G',
        'from_team': 'Cin',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 11000000,
        'guaranteed_money': 5000000,
        'aav': 5500000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # OL upgrade
        'impact_score': 1.2,
    },

    # ========== MAJOR LOSSES - Cap casualties and departures ==========
    {
        'player_name': 'Tre\'von Moehrig',
        'position': 'S',
        'from_team': 'LV',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Former 2nd rounder
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,  # 3yr/$51M to Panthers
    },
    {
        'player_name': 'Robert Spillane',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.0,  # 158 tackles
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,  # Leading tackler
        'importance_to_new_team': 0.0,
        'impact_score': -2.2,  # 3yr/$33M
    },
    {
        'player_name': 'Nate Hobbs',
        'position': 'CB',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Starting nickel
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # 4yr/$48M
    },
    {
        'player_name': 'Aidan O\'Connell',
        'position': 'QB',
        'from_team': 'LV',
        'to_team': 'RELEASED',
        'move_type': 'Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # Failed experiment
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.3,
    },

    # ========== 2025 NFL DRAFT - Franchise RB and supporting cast ==========
    {
        'player_name': 'Ashton Jeanty',
        'position': 'RB',
        'from_team': 'Boise State',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 1, Pick 6',
        'contract_years': 4,
        'contract_value': 37500000,
        'guaranteed_money': 37500000,
        'aav': 9375000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # 2,601 yards, 29 TDs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Generational talent
        'impact_score': 3.0,
        'notes': '2nd most rushing yards in FBS history'
    },
    {
        'player_name': 'Jack Bech',
        'position': 'WR',
        'from_team': 'TCU',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 2, Pick 42',
        'contract_years': 4,
        'contract_value': 9200000,
        'guaranteed_money': 5000000,
        'aav': 2300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 1,034 yards
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },
    {
        'player_name': 'Darien Porter',
        'position': 'CB',
        'from_team': 'Iowa State',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 3, Pick 65',
        'contract_years': 4,
        'contract_value': 6800000,
        'guaranteed_money': 1800000,
        'aav': 1700000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # 4.30 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # 90.1 coverage grade
        'impact_score': 1.5,
    },
    {
        'player_name': 'Charles Grant',
        'position': 'OT',
        'from_team': 'William & Mary',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 3, Pick 78',
        'contract_years': 4,
        'contract_value': 6200000,
        'guaranteed_money': 1500000,
        'aav': 1550000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Caleb Rogers',
        'position': 'G',
        'from_team': 'Auburn',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 3, Pick 89',
        'contract_years': 4,
        'contract_value': 5800000,
        'guaranteed_money': 1200000,
        'aav': 1450000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Dont\'e Thornton Jr.',
        'position': 'WR',
        'from_team': 'Oregon',
        'to_team': 'LV',
        'move_type': '2025 Draft - Round 4, Pick 106',
        'contract_years': 4,
        'contract_value': 5200000,
        'guaranteed_money': 1000000,
        'aav': 1300000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 6\'5", 25.4 YPC
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.6,
    },

    # ========== KEY EXTENSIONS - Building around core ==========
    {
        'player_name': 'Maxx Crosby',
        'position': 'EDGE',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 106500000,
        'guaranteed_money': 91500000,
        'aav': 35500000,
        '2024_grade': 9.5,  # Elite edge rusher
        'projected_2025_grade': 9.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # Highest paid non-QB
    },
    {
        'player_name': 'Malcolm Koonce',
        'position': 'EDGE',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 12000000,
        'guaranteed_money': 8000000,
        'aav': 12000000,
        '2024_grade': 0.0,  # ACL recovery
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },
    {
        'player_name': 'Adam Butler',
        'position': 'DT',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 16500000,
        'guaranteed_money': 11000000,
        'aav': 5500000,
        '2024_grade': 7.5,  # 10 sacks over 2 years
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.5,
    },
    {
        'player_name': 'AJ Cole',
        'position': 'P',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 15800000,
        'guaranteed_money': 9000000,
        'aav': 3950000,
        '2024_grade': 8.0,  # Elite punter
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 1.0,  # NFL's highest paid punter
    },

    # ========== COACHING/FRONT OFFICE OVERHAUL ==========
    {
        'player_name': 'Pete Carroll',
        'position': 'COACH-HC',
        'from_team': 'RETIRED',
        'to_team': 'LV',
        'move_type': 'Head Coach Hire',
        'contract_years': 3,
        'contract_value': 25000000,
        'guaranteed_money': 18000000,
        'aav': 8333333,
        '2024_grade': 0.0,
        'projected_2025_grade': 9.0,  # Super Bowl champion
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Culture transformation
        'impact_score': 3.0,
        'notes': '4th year option, Brady influence'
    },
    {
        'player_name': 'John Spytek',
        'position': 'GM',
        'from_team': 'TB',
        'to_team': 'LV',
        'move_type': 'GM Hire',
        'contract_years': 4,
        'contract_value': 12000000,
        'guaranteed_money': 8000000,
        'aav': 3000000,
        '2024_grade': 8.5,  # Tampa Bay success
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.5,
        'impact_score': 2.5,
    },
    {
        'player_name': 'Chip Kelly',
        'position': 'COACH-OC',
        'from_team': 'UCLA',
        'to_team': 'LV',
        'move_type': 'OC Hire',
        'contract_years': 3,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 2666667,
        '2024_grade': 7.5,  # College success
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 9.0,  # Innovative offense
        'impact_score': 2.0,
    },
    {
        'player_name': 'Patrick Graham',
        'position': 'COACH-DC',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'DC Retained',
        'contract_years': 2,
        'contract_value': 5000000,
        'guaranteed_money': 3000000,
        'aav': 2500000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.5,  # Fourth season
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.0,  # Continuity value
    },

    # ========== TRADE - RB depth ==========
    {
        'player_name': 'Jordan Mason',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'LV',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 7.0,  # 49ers backup
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
        'notes': 'Traded 6th round pick'
    },
]

# ========== SUMMARY METRICS ==========
RAIDERS_2025_SUMMARY = {
    'total_moves': len(RAIDERS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 4,
    'trades': 2,  # Smith in, Mason in
    'draft_picks': 11,  # Aggressive draft
    'key_extensions': 4,
    'coaching_overhaul': 4,
    'total_guaranteed_money': 200000000,  # Major investment
    'dead_money': 12000000,
    'cap_space_remaining': 36160000,
    'cap_space_2026': 94990000,  # Future flexibility
    'cap_space_2027': 142690000,  # Massive space
    'championship_window': '2026-2029',
    'offseason_grade': 'B+',
    'key_philosophy': 'Foundation establishment through proven winners',
    'net_impact_score': 22.5,  # Sum of all impact scores
    'division_outlook': 'Fourth but building',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'organizational_transformation': {
        'brady_influence': 'Minority owner driving decisions',
        'carroll_hire': '3yr + option, championship pedigree',
        'spytek_approach': 'Intelligently aggressive',
        'culture_shift': 'Always Compete mentality',
    },
    'quarterback_solution': {
        'smith_reunion': 'Carroll-Smith proven success',
        'cost': '3rd round pick (#92)',
        'timeline': '2-year bridge solution',
        'previous_chaos': '7 starters in 3 years',
    },
    'draft_philosophy': {
        'jeanty_selection': 'Generational RB talent',
        'trade_backs': 'Accumulated 11 picks',
        'offensive_focus': '7 of 11 picks on offense',
        'grade': 'Consensus A- from outlets',
    },
    'cap_management': {
        'current_flexibility': '$36.16M remaining',
        '2026_projection': '$94.99M available',
        '2027_projection': '$142.69M (!)',
        'comp_picks': '3 projected 2026-27',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Geno Smith',
        'backup': 'Brian Hoyer',
        'grade': 'B+',
        'notes': 'Immediate stability with Carroll',
    },
    'offensive_line': {
        'starters': ['Kolton Miller (LT)', 'Jackson Powers-Johnson (LG)', 
                     'Andre James (C)', 'Alex Cappa (RG)', 'Thayer Munford (RT)'],
        'depth': 'Grant, Rogers added',
        'grade': 'B',
        'notes': 'Improved interior',
    },
    'skill_positions': {
        'wr': 'Jakobi Meyers, Jack Bech, Dont\'e Thornton Jr.',
        'rb': 'Ashton Jeanty, Jordan Mason, Raheem Mostert',
        'te': 'Brock Bowers, Michael Mayer',
        'grade': 'A-',
        'notes': 'Jeanty-Bowers combo elite',
    },
    'defensive_line': {
        'dt': 'Christian Wilkins, Adam Butler, John Jenkins',
        'edge': 'Maxx Crosby, Malcolm Koonce, Tyree Wilson',
        'grade': 'B+',
        'notes': 'Crosby anchors unit',
    },
    'linebackers': {
        'starters': 'Devin White, Elandon Roberts',
        'depth': 'Luke Masterson, Divine Deablo',
        'grade': 'C+',
        'notes': 'Major weakness after departures',
    },
    'secondary': {
        'cb': 'Jack Jones, Darien Porter, Eric Stokes',
        'safety': 'Jeremy Chinn, Marcus Epps',
        'grade': 'C+',
        'notes': 'League-worst coverage in 2024',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 6.5,
        'lean': 'OVER',
        'reasoning': 'Carroll/Smith floor higher',
    },
    'division_odds': {
        'current': '+1200',
        'value': 'NO',
        'reasoning': 'Still 4th in division',
    },
    'playoffs': {
        'current': '+350',
        'value': 'NO',
        'reasoning': 'Building year',
    },
    'player_props': {
        'jeanty_rushing_yards': 'OVER 1,000',
        'smith_passing_yards': 'OVER 3,800',
        'crosby_sacks': 'OVER 12.5',
    },
    'key_angles': {
        'best_bet': 'Jeanty OROY +450',
        'fade': 'Division winner',
        'narrative': 'Culture over talent Year 1',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("LAS VEGAS RAIDERS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {RAIDERS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{RAIDERS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {RAIDERS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {RAIDERS_2025_SUMMARY['total_moves']}")
    print(f"  • Draft Picks: {RAIDERS_2025_SUMMARY['draft_picks']} (traded back)")
    print(f"  • Coaching Overhaul: Complete transformation")
    print(f"  • Tom Brady influence: Significant")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${RAIDERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: ${RAIDERS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Space: ${RAIDERS_2025_SUMMARY['cap_space_2026']:,}")
    print(f"  • 2027 Space: ${RAIDERS_2025_SUMMARY['cap_space_2027']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Pete Carroll (HC) - 3yr + option")
    print("  • Geno Smith (QB) - Trade + 2yr/$85.5M")
    print("  • Ashton Jeanty (RB) - #6 overall pick")
    print("  • Maxx Crosby - 3yr/$106.5M extension")
    
    print("\n❌ KEY LOSSES:")
    print("  • Robert Spillane (LB) - 158 tackles to Patriots")
    print("  • Tre'von Moehrig (S) - 3yr/$51M to Panthers")
    print("  • Nate Hobbs (CB) - 4yr/$48M to Packers")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {RAIDERS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {RAIDERS_2025_SUMMARY['division_outlook']}")
    print(f"  • 2024 weaknesses: Last in rushing, coverage")
    print(f"  • Timeline: 2-3 year build")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 6.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Carroll-Smith reunion success")
    print("  • Jeanty immediate impact")
    print("  • Defensive coverage remains weakness")
    print("  • AFC West gauntlet schedule")

if __name__ == "__main__":
    generate_summary_report()
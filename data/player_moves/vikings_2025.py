"""
Minnesota Vikings 2025 Offseason Moves
Historic $245 million spending spree to maximize J.J. McCarthy window
Last Updated: June 23, 2025
"""

VIKINGS_2025_MOVES = [
    # ========== DEFENSIVE LINE TRANSFORMATION - Interior dominance ==========
    {
        'player_name': 'Jonathan Allen',
        'position': 'DT',
        'from_team': 'Was',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 23255000,
        'aav': 20000000,
        '2024_grade': 5.0,  # Injury-limited to 8 games
        'projected_2025_grade': 8.0,  # Pro Bowl talent when healthy
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Interior pass rush upgrade
        'impact_score': 2.2,
    },
    {
        'player_name': 'Javon Hargrave',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 30000000,
        'guaranteed_money': 18000000,
        'aav': 15000000,
        '2024_grade': 7.0,  # Injury concerns but proven
        'projected_2025_grade': 8.2,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # 375 combined starts with Allen
        'impact_score': 2.0,
    },

    # ========== OFFENSIVE LINE OVERHAUL - Record investment ==========
    {
        'player_name': 'Will Fries',
        'position': 'G',
        'from_team': 'Ind',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 5,
        'contract_value': 88000000,
        'guaranteed_money': 45000000,
        'aav': 17600000,
        '2024_grade': 7.8,  # Solid Colts starter
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Addresses playoff disaster
        'impact_score': 2.5,
    },
    {
        'player_name': 'Ryan Kelly',
        'position': 'C',
        'from_team': 'Ind',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 18000000,
        'guaranteed_money': 10000000,
        'aav': 9000000,
        '2024_grade': 7.5,  # Veteran center
        'projected_2025_grade': 7.8,  # Chemistry with Fries
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Replace Bradbury
        'impact_score': 1.8,
    },

    # ========== SECONDARY RETENTION AND ADDITION ==========
    {
        'player_name': 'Byron Murphy Jr.',
        'position': 'CB1',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 54000000,  # Base, +$12M incentives
        'guaranteed_money': 35000000,
        'aav': 18000000,
        '2024_grade': 8.5,  # First Pro Bowl season
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Elite CB retained
    },
    {
        'player_name': 'Isaiah Rodgers',
        'position': 'CB2',
        'from_team': 'Phi',
        'to_team': 'Min',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 15000000,
        'guaranteed_money': 8000000,
        'aav': 7500000,
        '2024_grade': 7.3,  # Eagles rotation
        'projected_2025_grade': 7.5,  # Redemption story
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },

    # ========== MAJOR LOSSES - Quarterback exodus ==========
    {
        'player_name': 'Sam Darnold',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,  # Career-best 35 TDs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,  # 14-3 record
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # 3yr/$100M to Seattle
    },
    {
        'player_name': 'Daniel Jones',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Backup role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,  # $14M guaranteed elsewhere
    },
    {
        'player_name': 'Mike Conley',
        'position': 'CB',
        'from_team': 'Min',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,
    },
    {
        'player_name': 'Josh Oliver',
        'position': 'TE',
        'from_team': 'Min',
        'to_team': 'NYJ',
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
        'impact_score': -0.8,
    },

    # ========== 2025 NFL DRAFT - Limited capital, targeted picks ==========
    {
        'player_name': 'Donovan Jackson',
        'position': 'G',
        'from_team': 'Ohio State',
        'to_team': 'Min',
        'move_type': '2025 Draft - Round 1, Pick 24',
        'contract_years': 4,
        'contract_value': 18500000,
        'guaranteed_money': 18500000,
        'aav': 4625000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Versatile lineman
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starter
        'impact_score': 1.8,
    },
    {
        'player_name': 'Tai Felton',
        'position': 'WR',
        'from_team': 'Maryland',
        'to_team': 'Min',
        'move_type': '2025 Draft - Round 3, Pick 78',
        'contract_years': 4,
        'contract_value': 6800000,
        'guaranteed_money': 1800000,
        'aav': 1700000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 96 catches, 1,124 yards
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Addison insurance
        'impact_score': 1.0,
    },
    {
        'player_name': 'Kobe King',
        'position': 'LB',
        'from_team': 'Penn State',
        'to_team': 'Min',
        'move_type': '2025 Draft - Round 6, Pick 185',
        'contract_years': 4,
        'contract_value': 4100000,
        'guaranteed_money': 600000,
        'aav': 1025000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # "Best value pick" 6th round
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # 4th round talent
        'impact_score': 0.6,
    },
    {
        'player_name': 'Robert Ford',
        'position': 'DE',
        'from_team': 'Auburn',
        'to_team': 'Min',
        'move_type': '2025 Draft - Round 7, Pick 232',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 300000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.2,
    },

    # ========== TRADES - Strategic moves ==========
    {
        'player_name': 'Sam Howell',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 4500000,
        'guaranteed_money': 2500000,
        'aav': 2250000,
        '2024_grade': 6.5,  # Seahawks backup
        'projected_2025_grade': 6.8,  # McCarthy insurance
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,
        'impact_score': 0.8,
        'notes': 'Traded 5th round pick'
    },
    {
        'player_name': 'Jordan Mason',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'Min',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 3000000,
        '2024_grade': 7.0,  # 49ers backup
        'projected_2025_grade': 7.2,  # Committee with Jones
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,
        'impact_score': 0.8,
        'notes': 'Traded 6th round pick'
    },

    # ========== KEY EXTENSIONS AND RE-SIGNINGS ==========
    {
        'player_name': 'Andrew Van Ginkel',
        'position': 'EDGE',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Contract Extension',
        'contract_years': 1,
        'contract_value': 23000000,
        'guaranteed_money': 20000000,
        'aav': 23000000,
        '2024_grade': 8.5,  # 11.5 sacks, 2 pick-sixes
        'projected_2025_grade': 8.5,  # Pro Bowl season
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.2,
    },
    {
        'player_name': 'Aaron Jones',
        'position': 'RB',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 20000000,
        'guaranteed_money': 12000000,
        'aav': 10000000,
        '2024_grade': 7.5,  # Age 31 season
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },

    # ========== COACHING CONTINUITY ==========
    {
        'player_name': 'Kevin O\'Connell',
        'position': 'COACH-HC',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Contract Extension',
        'contract_years': 5,
        'contract_value': 35000000,
        'guaranteed_money': 25000000,
        'aav': 7000000,
        '2024_grade': 9.0,  # Coach of the Year, 14-3
        'projected_2025_grade': 9.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 2.0,  # Stability crucial
    },
    {
        'player_name': 'Kwesi Adofo-Mensah',
        'position': 'GM',
        'from_team': 'Min',
        'to_team': 'Min',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 20000000,
        'guaranteed_money': 12000000,
        'aav': 5000000,
        '2024_grade': 8.5,  # Orchestrated spending spree
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 1.5,
    },

    # ========== POST-JUNE 1 CUT ==========
    {
        'player_name': 'Garrett Bradbury',
        'position': 'C',
        'from_team': 'Min',
        'to_team': 'RELEASED',
        'move_type': 'Post-June 1 Cut',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Replaced by Kelly
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,  # $5.25M savings
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
]

# ========== SUMMARY METRICS ==========
VIKINGS_2025_SUMMARY = {
    'total_moves': len(VIKINGS_2025_MOVES),
    'free_agent_signings': 6,
    'major_losses': 5,
    'trades': 2,
    'draft_picks': 4,  # Fewest in NFL
    'key_resignings': 4,
    'coaching_extensions': 2,
    'total_guaranteed_money': 245470000,  # League-leading
    'dead_money': 5250000,  # Bradbury cut
    'cap_space_remaining': 18000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'A-',
    'key_philosophy': 'Historic $245M spending spree to maximize McCarthy window',
    'net_impact_score': 17.5,  # Sum of all impact scores
    'division_outlook': 'Co-favorites with Lions in loaded division',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'record_spending': {
        'total_spent': '$245.47M (league-leading)',
        'ol_investment': '$108M on OL/DL combined',
        'philosophy': 'Address playoff disaster immediately',
        'timeline': '2-3 year championship push',
    },
    'quarterback_transition': {
        'darnold_departure': '3yr/$100M to Seattle',
        'mccarthy_era': 'Clear commitment to 2024 pick',
        'backup_plan': 'Howell acquired via trade',
        'pressure': 'McCarthy must deliver immediately',
    },
    'offensive_line_overhaul': {
        'playoff_disaster': 'NFL-record 9 sacks allowed',
        'fries_deal': '5yr/$88M massive investment',
        'chemistry': 'Fries/Kelly played together in Indy',
        'protection': 'Complete interior renovation',
    },
    'cap_gymnastics': {
        'current_space': '$14.2-23.5M remaining',
        '2026_projection': '$18-41M OVER cap',
        'restructure_options': 'Jefferson alone = $19M',
        'window': 'Clear 2-3 year push',
    },
    'defensive_upgrades': {
        'interior_dominance': 'Allen/Hargrave = 8 Pro Bowls',
        'murphy_extension': 'Highest-paid CB deal',
        'pass_rush': 'Van Ginkel Pro Bowl retention',
        'flores_system': 'Personnel fits scheme',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'J.J. McCarthy',
        'backup': 'Sam Howell',
        'grade': 'C+',
        'notes': 'All-in on 2024 first-rounder',
    },
    'offensive_line': {
        'starters': ['Christian Darrisaw (LT)', 'Will Fries (LG)', 'Ryan Kelly (C)', 
                     'Donovan Jackson (RG)', 'Brian O\'Neill (RT)'],
        'depth': 'Blake Brandel, Ed Ingram',
        'grade': 'A',
        'notes': 'From worst playoff OL to potential elite',
    },
    'skill_positions': {
        'wr': 'Justin Jefferson, Jordan Addison, Tai Felton',
        'rb': 'Aaron Jones, Jordan Mason, Ty Chandler',
        'te': 'T.J. Hockenson, Johnny Mundt',
        'grade': 'A+',
        'notes': 'Elite weapons if healthy',
    },
    'defensive_line': {
        'dt': 'Jonathan Allen, Javon Hargrave, Harrison Phillips',
        'edge': 'Andrew Van Ginkel, Dallas Turner, Pat Jones II',
        'grade': 'A-',
        'notes': 'Interior transformed with $90M investment',
    },
    'linebackers': {
        'starters': 'Ivan Pace Jr., Brian Asamoah',
        'depth': 'Kobe King, Troy Dye',
        'grade': 'B',
        'notes': 'Speed over size in Flores system',
    },
    'secondary': {
        'cb': 'Byron Murphy Jr., Isaiah Rodgers, Mekhi Blackmon',
        'safety': 'Harrison Smith, Josh Metellus, Cam Bynum',
        'grade': 'B+',
        'notes': 'Lost 4 of top 5 CBs from 2024',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 10.5,
        'lean': 'UNDER',
        'reasoning': 'McCarthy uncertainty + brutal schedule',
    },
    'division_odds': {
        'current': '+200',
        'value': 'FAIR',
        'reasoning': 'Co-favorites with Lions',
    },
    'super_bowl_odds': {
        'current': '+1800',
        'value': 'PASS',
        'reasoning': 'QB questions despite elite roster',
    },
    'player_props': {
        'mccarthy_passing_yards': 'UNDER 3,500',
        'jefferson_receiving_yards': 'OVER 1,450',
        'jones_rushing_yards': 'UNDER 900',
    },
    'key_angles': {
        'best_bet': 'Make playoffs -150',
        'fade': 'Division winner',
        'narrative': 'Defense carries early',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("MINNESOTA VIKINGS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {VIKINGS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{VIKINGS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {VIKINGS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {VIKINGS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {VIKINGS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Draft Picks: {VIKINGS_2025_SUMMARY['draft_picks']} (fewest in NFL)")
    print(f"  • League-Leading Spending: ${VIKINGS_2025_SUMMARY['total_guaranteed_money']:,}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${VIKINGS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${VIKINGS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${VIKINGS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Projection: $18-41M OVER cap")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Will Fries (G) - 5yr/$88M from Colts")
    print("  • Jonathan Allen (DT) - 3yr/$60M from Commanders")
    print("  • Javon Hargrave (DT) - 2yr/$30M from 49ers")
    print("  • Byron Murphy Jr. - 3yr/$54M extension")
    
    print("\n❌ KEY LOSSES:")
    print("  • Sam Darnold (QB) - 3yr/$100M to Seahawks")
    print("  • Daniel Jones (QB) - $14M guaranteed to Colts")
    print("  • Mike Conley (CB) - To Texans")
    print("  • Josh Oliver (TE) - To Jets")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {VIKINGS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {VIKINGS_2025_SUMMARY['division_outlook']}")
    print(f"  • QB Transition: All-in on J.J. McCarthy")
    print(f"  • OL Investment: $108M after playoff disaster")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 10.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • McCarthy development with elite support")
    print("  • Interior DL health (Allen/Hargrave)")
    print("  • Cap reckoning looms in 2026")
    print("  • Secondary depth after losing 4 CBs")

if __name__ == "__main__":
    generate_summary_report()
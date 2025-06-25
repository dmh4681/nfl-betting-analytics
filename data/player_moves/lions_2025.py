"""
Detroit Lions 2025 Offseason Moves
Championship core maintenance despite coordinator exodus
Last Updated: June 23, 2025
"""

LIONS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Minimal external additions ==========
    {
        'player_name': 'D.J. Reed',
        'position': 'CB1',
        'from_team': 'NYJ',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 48000000,
        'guaranteed_money': 32000000,
        'aav': 16000000,
        '2024_grade': 7.8,  # 70.1 PFF coverage grade
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Direct Davis replacement
        'impact_score': 2.0,
    },
    {
        'player_name': 'Roy Lopez',
        'position': 'DT',
        'from_team': 'Min',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4650000,
        'guaranteed_money': 2500000,
        'aav': 4650000,
        '2024_grade': 6.8,  # Solid rotational DT
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # McNeill ACL insurance
        'impact_score': 0.8,
    },
    {
        'player_name': 'Grant Stuard',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1700000,
        'guaranteed_money': 1700000,
        'aav': 1700000,
        '2024_grade': 6.5,  # Special teams ace
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # ST upgrade
        'impact_score': 0.5,
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS - Historic investments ==========
    {
        'player_name': 'Jared Goff',
        'position': 'QB',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 212000000,
        'guaranteed_money': 170000000,
        'aav': 53000000,
        '2024_grade': 8.8,  # Elite 2024 season
        'projected_2025_grade': 8.8,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 10.0,
        'importance_to_new_team': 10.0,
        'impact_score': 3.0,  # NFL's 2nd-highest paid QB
    },
    {
        'player_name': 'Penei Sewell',
        'position': 'RT',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 112000000,
        'guaranteed_money': 85000000,
        'aav': 28000000,
        '2024_grade': 9.0,  # Elite RT
        'projected_2025_grade': 9.0,  # Age 24
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 9.5,
        'importance_to_new_team': 9.5,
        'impact_score': 2.8,  # Set OL market
    },
    {
        'player_name': 'Amon-Ra St. Brown',
        'position': 'WR1',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 120000000,
        'guaranteed_money': 77000000,
        'aav': 30000000,
        '2024_grade': 8.8,  # Elite slot receiver
        'projected_2025_grade': 8.8,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Briefly highest-paid WR
    },
    {
        'player_name': 'Derrick Barnes',
        'position': 'LB',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 25500000,
        'guaranteed_money': 14000000,
        'aav': 8500000,
        '2024_grade': 7.5,  # Solid linebacker
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,  # Retained before FA
    },

    # ========== MAJOR LOSSES - Coordinator exodus ==========
    {
        'player_name': 'Ben Johnson',
        'position': 'COACH-OC',
        'from_team': 'Det',
        'to_team': 'Chi',
        'move_type': 'Coaching Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 10.0,  # NFL's best offense
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,  # To division rival
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,  # Massive loss
    },
    {
        'player_name': 'Aaron Glenn',
        'position': 'COACH-DC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Coaching Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,  # Despite 16 players on IR
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # Both coordinators lost
    },
    {
        'player_name': 'Carlton Davis III',
        'position': 'CB1',
        'from_team': 'Det',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Solid corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # 3yr/$60M to Patriots
    },
    {
        'player_name': 'Za\'Darius Smith',
        'position': 'EDGE',
        'from_team': 'Det',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 4 sacks in 8 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,  # $11M saved
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },
    {
        'player_name': 'Kevin Zeitler',
        'position': 'RG',
        'from_team': 'Det',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.0,  # 86.5 PFF grade
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },

    # ========== 2025 NFL DRAFT - Controversial selections ==========
    {
        'player_name': 'Tyleik Williams',
        'position': 'DT',
        'from_team': 'Ohio State',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 1, Pick 29',
        'contract_years': 4,
        'contract_value': 16200000,
        'guaranteed_money': 16200000,
        'aav': 4050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Elite run stopper
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # DL depth
        'impact_score': 1.5,
    },
    {
        'player_name': 'Tate Ratledge',
        'position': 'RG',
        'from_team': 'Georgia',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 2, Pick 48',
        'contract_years': 4,
        'contract_value': 11400000,
        'guaranteed_money': 6000000,
        'aav': 2850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # "Dirtbag mentality"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Zeitler replacement
        'impact_score': 1.8,
    },
    {
        'player_name': 'Isaac TeSlaa',
        'position': 'WR',
        'from_team': 'Wyoming',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 3, Pick 70',
        'contract_years': 4,
        'contract_value': 7000000,
        'guaranteed_money': 2000000,
        'aav': 1750000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Holmes' favorite
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Traded up
        'impact_score': 0.8,
        'notes': 'Traded 2 2026 3rd round picks'
    },
    {
        'player_name': 'Donovan Kaufman',
        'position': 'S',
        'from_team': 'Wyoming',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 4, Pick 101',
        'contract_years': 4,
        'contract_value': 5600000,
        'guaranteed_money': 1200000,
        'aav': 1400000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Safety depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Ahmed Hassanein',
        'position': 'EDGE',
        'from_team': 'Baylor',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 5, Pick 153',
        'contract_years': 4,
        'contract_value': 4200000,
        'guaranteed_money': 700000,
        'aav': 1050000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Colston Loveland',
        'position': 'TE',
        'from_team': 'Michigan',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 6, Pick 189',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 500000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Local kid
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Hometown hero
        'impact_score': 0.5,
    },
    {
        'player_name': 'Joey Fisher',
        'position': 'OL',
        'from_team': 'Shepherd',
        'to_team': 'Det',
        'move_type': '2025 Draft - Round 7, Pick 254',
        'contract_years': 4,
        'contract_value': 3600000,
        'guaranteed_money': 300000,
        'aav': 900000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # D2 project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.1,
    },

    # ========== COACHING PROMOTIONS - Internal succession ==========
    {
        'player_name': 'Scott Morton',
        'position': 'COACH-OC',
        'from_team': 'Det-PGC',
        'to_team': 'Det',
        'move_type': 'Internal Promotion',
        'contract_years': 3,
        'contract_value': 4500000,
        'guaranteed_money': 2500000,
        'aav': 1500000,
        '2024_grade': 7.5,  # Pass game coordinator
        'projected_2025_grade': 7.5,  # System continuity
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Kelvin Sheppard',
        'position': 'COACH-DC',
        'from_team': 'Det-LB',
        'to_team': 'Det',
        'move_type': 'Internal Promotion',
        'contract_years': 3,
        'contract_value': 3600000,
        'guaranteed_money': 1800000,
        'aav': 1200000,
        '2024_grade': 7.0,  # LB coach
        'projected_2025_grade': 7.0,  # Scheme continuity
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
    },
]

# ========== SUMMARY METRICS ==========
LIONS_2025_SUMMARY = {
    'total_moves': len(LIONS_2025_MOVES),
    'free_agent_signings': 3,  # Minimal external
    'major_losses': 7,
    'draft_picks': 7,
    'key_resignings': 4,
    'coaching_changes': 4,  # 2 losses, 2 promotions
    'total_guaranteed_money': 332000000,  # Core extensions
    'dead_money': 11000000,  # Smith release
    'cap_space_remaining': 40200000,  # Maintained flexibility
    'championship_window': '2025-2027',
    'offseason_grade': 'B',
    'key_philosophy': 'Internal continuity over external splash despite coordinator losses',
    'net_impact_score': 7.5,  # Sum of all impact scores
    'division_outlook': 'Still favorites but face fierce competition',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'coordinator_exodus': {
        'johnson_loss': 'To division rival Bears as HC',
        'glenn_loss': 'Jets HC after elite defensive year',
        'internal_promotions': 'Morton/Sheppard maintain systems',
        'risk_level': 'HIGH - Both coordinators unprecedented',
    },
    'core_extensions': {
        'goff_deal': '$212M makes him 2nd-highest paid QB',
        'sewell_deal': '$112M sets RT market',
        'st_brown_deal': '$120M briefly highest WR',
        'philosophy': 'Lock up homegrown talent',
    },
    'draft_controversy': {
        'consensus_grade': 'Worst since 2019 (F from Athletic)',
        'holmes_confidence': 'Mirrors 2023 class success',
        'teslaa_reach': 'Traded two 3rds for 6th round projection',
        'culture_fit': 'Prioritized over consensus rankings',
    },
    'cap_management': {
        'current_space': '$40.2M maintained',
        '2026_projection': 'Potential $40M OVER cap',
        'restructure_candidates': 'Goff, Sewell, St. Brown',
        'window': 'Clear 2-3 year push',
    },
    'injury_situations': {
        'mcneill_acl': 'Lopez signing provides insurance',
        'hutchinson_recovery': 'Expected full return',
        'depth_concerns': 'Secondary thin after Davis loss',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Jared Goff',
        'backup': 'Hendon Hooker',
        'grade': 'A',
        'notes': '$212M extension, system mastery',
    },
    'offensive_line': {
        'starters': ['Taylor Decker (LT)', 'Graham Glasgow (LG)', 'Frank Ragnow (C)', 
                     'Tate Ratledge (RG)', 'Penei Sewell (RT)'],
        'depth': 'Concerns after Zeitler loss',
        'grade': 'A-',
        'notes': 'Elite bookends, new RG',
    },
    'skill_positions': {
        'wr': 'Amon-Ra St. Brown, Jameson Williams, Isaac TeSlaa',
        'rb': 'Jahmyr Gibbs, David Montgomery',
        'te': 'Sam LaPorta, Brock Wright',
        'grade': 'A+',
        'notes': 'Elite weapons at every position',
    },
    'defensive_line': {
        'dt': 'Alim McNeill, DJ Reader, Tyleik Williams',
        'edge': 'Aidan Hutchinson, Marcus Davenport, Josh Paschal',
        'grade': 'B+',
        'notes': 'Hutchinson return crucial',
    },
    'linebackers': {
        'starters': 'Alex Anzalone, Jack Campbell, Derrick Barnes',
        'depth': 'Malcolm Rodriguez, Ben Niemann',
        'grade': 'B+',
        'notes': 'Young core developing',
    },
    'secondary': {
        'cb': 'D.J. Reed, Terrion Arnold, Brian Branch',
        'safety': 'Kerby Joseph, Ifeatu Melifonwu (lost)',
        'grade': 'B',
        'notes': 'Reed replaces Davis adequately',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 11.5,
        'lean': 'UNDER',
        'reasoning': 'Coordinator losses + toughest schedule',
    },
    'division_odds': {
        'current': '+140',
        'value': 'YES',
        'reasoning': 'Still best roster despite changes',
    },
    'super_bowl_odds': {
        'current': '+1000',
        'value': 'FAIR',
        'reasoning': 'Top-5 contender with questions',
    },
    'player_props': {
        'goff_passing_yards': 'OVER 4,400',
        'gibbs_rushing_yards': 'OVER 1,100',
        'st_brown_receptions': 'OVER 115.5',
    },
    'key_angles': {
        'best_bet': 'Division winner +140',
        'fade': 'Home field advantage (1 seed)',
        'narrative': 'System > coordinators?',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("DETROIT LIONS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {LIONS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{LIONS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {LIONS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {LIONS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {LIONS_2025_SUMMARY['free_agent_signings']} (minimal)")
    print(f"  • Core Extensions: $332M guaranteed to Goff/Sewell/St. Brown")
    print(f"  • Coordinator Losses: Both to HC positions")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${LIONS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${LIONS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${LIONS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"  • 2026 Warning: Potential $40M over cap")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • D.J. Reed (CB) - 3yr/$48M from Jets")
    print("  • Scott Morton (OC) - Internal promotion")
    print("  • Kelvin Sheppard (DC) - Internal promotion")
    print("  • Tyleik Williams (DT) - 1st round pick")
    
    print("\n❌ KEY LOSSES:")
    print("  • Ben Johnson (OC) - To Bears as HC")
    print("  • Aaron Glenn (DC) - To Jets as HC")
    print("  • Carlton Davis III (CB) - 3yr/$60M to Patriots")
    print("  • Kevin Zeitler (RG) - 86.5 PFF grade")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {LIONS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {LIONS_2025_SUMMARY['division_outlook']}")
    print(f"  • Draft Grade: F (Athletic) but mirrors 2023")
    print(f"  • Risk: Can internal promotions maintain elite level?")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 11.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Coordinator succession plan effectiveness")
    print("  • NFL's toughest schedule")
    print("  • Health of Hutchinson, McNeill")
    print("  • Young core entering prime (avg age 24)")

if __name__ == "__main__":
    generate_summary_report()
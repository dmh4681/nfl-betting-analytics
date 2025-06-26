"""
Indianapolis Colts 2025 Offseason Moves
Measured approach: Building competition around Anthony Richardson
Last Updated: June 23, 2025
"""

COLTS_2025_MOVES = [
    # ========== KEY FREE AGENT SIGNINGS - Defensive overhaul ==========
    {
        'player_name': 'Daniel Jones',
        'position': 'QB',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14000000,
        'guaranteed_money': 10000000,
        'aav': 14000000,
        '2024_grade': 6.8,  # Limited role with Vikings after Giants release
        'projected_2025_grade': 7.0,  # Legitimate QB competition
        'snap_percentage_2024': 30.0,  # Backup role in Minnesota
        'importance_to_old_team': 6.0,  # Depth quarterback
        'importance_to_new_team': 8.5,  # Competition for Richardson
        'impact_score': 2.0,
    },
    {
        'player_name': 'Charvarius Ward',
        'position': 'CB1',
        'from_team': 'SF',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 32000000,
        'aav': 20000000,
        '2024_grade': 7.8,  # Elite corner play
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Biggest CB commitment under Ballard
        'impact_score': 2.5,
    },
    {
        'player_name': 'Cam Bynum',
        'position': 'S',
        'from_team': 'Min',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 45000000,
        'guaranteed_money': 22000000,
        'aav': 15000000,
        '2024_grade': 7.5,  # Breakout season
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.5,  # Major safety upgrade
        'impact_score': 2.0,
    },
    {
        'player_name': 'Tim Boyle',
        'position': 'QB',
        'from_team': 'Mia',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1500000,
        'aav': 2500000,
        '2024_grade': 5.5,  # Veteran backup experience
        'projected_2025_grade': 5.8,  # Third quarterback depth
        'snap_percentage_2024': 15.0,  # Limited action
        'importance_to_old_team': 4.0,  # Depth piece
        'importance_to_new_team': 5.5,  # QB room depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Will Harris',
        'position': 'S',
        'from_team': 'NO',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        'guaranteed_money': 2000000,
        'aav': 4000000,
        '2024_grade': 6.2,  # Depth safety
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Safety depth
        'impact_score': 0.5,
    },
    {
        'player_name': 'Khalil Herbert',
        'position': 'RB',
        'from_team': 'Chi',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.5,  # Complementary back
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Complement Taylor
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jerome Carvin',
        'position': 'LB',
        'from_team': 'Sea',
        'to_team': 'Ind',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.0,  # LB depth
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # LB competition
        'impact_score': 0.5,
    },

    # ========== MAJOR LOSSES - Cap casualties and departures ==========
    {
        'player_name': 'Ryan Kelly',
        'position': 'C',
        'from_team': 'Ind',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -4000000,  # Dead money
        'aav': 0,
        '2024_grade': 6.5,  # Declining play
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,  # Long-time center
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Saved $12.5M
    },
    {
        'player_name': 'E.J. Speed',
        'position': 'LB',
        'from_team': 'Ind',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Starting linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,
    },
    {
        'player_name': 'Julian Blackmon',
        'position': 'S',
        'from_team': 'Ind',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.2,  # Starting safety
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,
    },
    {
        'player_name': 'Shaquille Leonard',
        'position': 'LB',
        'from_team': 'Ind',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.0,  # Injury-limited final years
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 6.0,  # Former All-Pro
        'importance_to_new_team': 0.0,
        'impact_score': -0.5,
    },

    # ========== 2025 NFL DRAFT - Tyler Warren focus ==========
    {
        'player_name': 'Tyler Warren',
        'position': 'TE',
        'from_team': 'Penn State',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 1, Pick 14',
        'contract_years': 4,
        'contract_value': 28500000,
        'guaranteed_money': 28500000,
        'aav': 7125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Immediate impact TE
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Key target for Richardson
        'impact_score': 2.2,
    },
    {
        'player_name': 'Deontae Lawson',
        'position': 'LB',
        'from_team': 'Alabama',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 2, Pick 45',
        'contract_years': 4,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 2000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # LB replacement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replace Speed
        'impact_score': 1.5,
    },
    {
        'player_name': 'Shavon Revel Jr.',
        'position': 'CB',
        'from_team': 'East Carolina',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 3, Pick 78',
        'contract_years': 4,
        'contract_value': 5900000,
        'guaranteed_money': 1500000,
        'aav': 1475000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # CB depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.8,
    },
    {
        'player_name': 'Cameron Williams',
        'position': 'OT',
        'from_team': 'Texas',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 4, Pick 111',
        'contract_years': 4,
        'contract_value': 4900000,
        'guaranteed_money': 1000000,
        'aav': 1225000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # OL depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Donovan Jennings',
        'position': 'OG',
        'from_team': 'USF',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 5, Pick 144',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 700000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Interior OL
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Kitan Oladapo',
        'position': 'S',
        'from_team': 'Oregon State',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 6, Pick 177',
        'contract_years': 4,
        'contract_value': 3500000,
        'guaranteed_money': 500000,
        'aav': 875000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # Safety depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Garret Greenfield',
        'position': 'OT',
        'from_team': 'South Dakota State',
        'to_team': 'Ind',
        'move_type': '2025 Draft - Round 7, Pick 210',
        'contract_years': 4,
        'contract_value': 3200000,
        'guaranteed_money': 300000,
        'aav': 800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 4.5,
        'impact_score': 0.1,
    },

    # ========== KEY RE-SIGNINGS - Core retention ==========
    {
        'player_name': 'DeForest Buckner',
        'position': 'DT',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 46000000,
        'guaranteed_money': 28000000,
        'aav': 23000000,
        '2024_grade': 8.5,  # Defensive anchor
        'projected_2025_grade': 8.2,  # Elite interior pass rusher
        'snap_percentage_2024': 85.0,  # Key defensive player
        'importance_to_old_team': 9.5,  # Defensive cornerstone
        'importance_to_new_team': 9.5,  # Critical retention
        'impact_score': 2.5,
    },
    {
        'player_name': 'Jonathan Taylor',
        'position': 'RB',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 42000000,
        'guaranteed_money': 24000000,
        'aav': 14000000,
        '2024_grade': 8.0,  # Franchise running back
        'projected_2025_grade': 7.8,  # Still elite when healthy
        'snap_percentage_2024': 70.0,  # Injury-limited season
        'importance_to_old_team': 9.0,  # Offensive centerpiece
        'importance_to_new_team': 9.0,  # Key offensive weapon
        'impact_score': 2.0,
    },
    {
        'player_name': 'Michael Pittman Jr.',
        'position': 'WR1',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 35000000,
        'aav': 20000000,
        '2024_grade': 7.8,  # Top receiver
        'projected_2025_grade': 8.0,  # Reliable #1 receiver
        'snap_percentage_2024': 90.0,  # Primary receiving target
        'importance_to_old_team': 8.5,  # Top receiving threat
        'importance_to_new_team': 8.5,  # Key target for Richardson
        'impact_score': 2.0,
    },
    {
        'player_name': 'Quenton Nelson',
        'position': 'LG',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 18000000,
        'guaranteed_money': 12000000,
        'aav': 18000000,
        '2024_grade': 7.5,  # Elite guard when healthy
        'projected_2025_grade': 7.8,  # Still dominant
        'snap_percentage_2024': 75.0,  # Injury-limited
        'importance_to_old_team': 8.5,  # Franchise guard
        'importance_to_new_team': 8.5,  # Offensive line anchor
        'impact_score': 1.8,
    },
    {
        'player_name': 'Grover Stewart',
        'position': 'DT',
        'from_team': 'Ind',
        'to_team': 'Ind',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 9000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # Run-stopping DT
        'projected_2025_grade': 7.0,  # Interior line stability
        'snap_percentage_2024': 65.0,  # Rotational starter
        'importance_to_old_team': 7.0,  # Interior defensive depth
        'importance_to_new_team': 7.0,  # Defensive line depth
        'impact_score': 1.0,
    },

    # ========== COACHING CHANGES ==========
    {
        'player_name': 'Lou Anarumo',
        'position': 'COACH-DC',
        'from_team': 'Cin',
        'to_team': 'Ind',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 4000000,
        '2024_grade': 6.5,  # Bengals defense struggled in 2024
        'projected_2025_grade': 7.5,  # Fresh defensive perspective
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost experienced coordinator
        'importance_to_new_team': 8.0,  # Defensive overhaul needed
        'impact_score': 1.5,
    },
    {
        'player_name': 'Gus Bradley',
        'position': 'COACH-DC',
        'from_team': 'Ind',
        'to_team': 'FIRED',
        'move_type': 'Coaching Change',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 5.5,  # Defense underperformed
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
        'impact_score': 0.5,  # Addition by subtraction
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Ind',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 7500000,  # Combined
        'guaranteed_money': 750000,
        'aav': 2500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.2,
    },
]

# ========== SUMMARY METRICS ==========
COLTS_2025_SUMMARY = {
    'total_moves': len(COLTS_2025_MOVES),
    'free_agent_signings': 7,  # Focused additions
    'major_losses': 4,  # Kelly, Speed, Blackmon, Leonard
    'trades': 0,  # Quiet on trade market
    'draft_picks': 7,
    'key_resignings': 5,
    'coaching_changes': 2,  # New DC
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 225000000,  # Major defensive investments
    'cap_space_used': 95000000,
    'cap_space_remaining': 8500000,
    'championship_window': '2025-2028',  # Richardson development window
    'offseason_grade': 'B',
    'key_philosophy': 'Create competition throughout roster while supporting Richardson',
    'net_impact_score': 14.5,  # Sum of all impact scores
    'biggest_concern': 'Anthony Richardson health and consistency',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'quarterback_situation': {
        'richardson_concerns': 'Missed 17 of 34 possible games in 2 years',
        'jones_signing': 'Legitimate competition, not just backup',
        'development_focus': 'Ballard: consistency down after down',
        'june_injury': 'AC joint aggravation during minicamp',
    },
    'defensive_overhaul': {
        'investment': 'Ward and Bynum combine for $105M',
        'philosophy': 'Biggest CB commitment in Ballard era',
        'coordinator_change': 'Anarumo brings fresh perspective',
        'secondary_upgrade': 'Addressed biggest weakness',
    },
    'organizational_philosophy': {
        'ballard_admission': 'Too emotional about players',
        'competition_focus': 'Should have created more throughout roster',
        'continuity': 'Steichen retained despite playoff miss',
        'ownership_change': 'Irsay daughters take control',
    },
    'offensive_approach': {
        'warren_selection': 'Elite TE prospect for Richardson',
        'line_continuity': 'Nelson and core retained',
        'skill_positions': 'Taylor-Pittman-Warren trio',
        'scheme': 'Continue Steichen system development',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Anthony Richardson',
        'backup': 'Daniel Jones',
        'third': 'Tim Boyle',
        'grade': 'B-',
        'notes': 'Richardson health key, Jones provides real competition',
    },
    'offensive_line': {
        'starters': ['Bernhard Raimann (LT)', 'Quenton Nelson (LG)', 'Danny Pinter (C)', 
                     'Will Fries (RG)', 'Braden Smith (RT)'],
        'depth': 'Kelly loss hurts, but core intact',
        'grade': 'B+',
        'notes': 'Nelson health crucial for interior',
    },
    'skill_positions': {
        'wr': 'Michael Pittman Jr., Josh Downs, Alec Pierce',
        'rb': 'Jonathan Taylor, Khalil Herbert, Evan Hull',
        'te': 'Tyler Warren (R), Drew Ogletree, Mo Alie-Cox',
        'grade': 'B+',
        'notes': 'Warren adds elite TE element',
    },
    'defensive_line': {
        'dt': 'DeForest Buckner, Grover Stewart, Dayo Odeyingbo',
        'edge': 'Kwity Paye, Laiatu Latu, Tyquan Lewis',
        'grade': 'B',
        'notes': 'Buckner anchors solid unit',
    },
    'linebackers': {
        'starters': 'Zaire Franklin, Deontae Lawson (R), Jerome Carvin',
        'depth': 'Thin after losses',
        'grade': 'C+',
        'notes': 'Speed loss hurts, Lawson must contribute early',
    },
    'secondary': {
        'cb': 'Charvarius Ward, Kenny Moore II, Shavon Revel Jr. (R)',
        'safety': 'Cam Bynum, Nick Cross, Will Harris',
        'grade': 'B+',
        'notes': 'Major upgrade with Ward and Bynum',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 8.5,
        'lean': 'UNDER',
        'reasoning': 'Richardson health concerns, tough division',
    },
    'division_odds': {
        'current': '+400',
        'value': 'NO',
        'reasoning': 'Houston clear favorites',
    },
    'playoffs': {
        'odds': '+120',
        'value': 'NO',
        'reasoning': 'Wild card competition fierce',
    },
    'player_props': {
        'richardson_passing_yards': 'UNDER 3,400 (health)',
        'taylor_rushing_yards': 'OVER 1,100 (if healthy)',
        'pittman_receiving_yards': 'OVER 1,000',
        'warren_receiving_yards': 'OVER 650',
    },
    'key_angles': {
        'best_bet': 'Under 8.5 wins',
        'longshot': 'Daniel Jones starts 6+ games +350',
        'narrative': 'QB health determines season',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("INDIANAPOLIS COLTS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {COLTS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{COLTS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {COLTS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {COLTS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {COLTS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {COLTS_2025_SUMMARY['major_losses']}")
    print(f"  • Draft Picks: {COLTS_2025_SUMMARY['draft_picks']}")
    print(f"  • Key Re-signings: {COLTS_2025_SUMMARY['key_resignings']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${COLTS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space Used: ${COLTS_2025_SUMMARY['cap_space_used']:,}")
    print(f"  • Remaining Cap: ${COLTS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Daniel Jones (QB) - 1yr/$14M QB competition")
    print("  • Charvarius Ward (CB) - 3yr/$60M elite corner")
    print("  • Cam Bynum (S) - 3yr/$45M safety upgrade")
    print("  • Tyler Warren (TE) - 1st round pick")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • Ryan Kelly - Released (saved $12.5M)")
    print("  • E.J. Speed - To Cowboys")
    print("  • Julian Blackmon - To Panthers")
    print("  • Shaquille Leonard - Retired")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {COLTS_2025_SUMMARY['key_philosophy']}")
    print(f"  • QB Room: Jones creates real competition")
    print(f"  • Defense: $105M invested in secondary")
    print(f"  • Ballard: Acknowledged need for more competition")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 8.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Richardson health (17 of 34 games missed)")
    print("  • Secondary improvement with Ward/Bynum")
    print("  • Tyler Warren immediate impact")
    print("  • Offensive line health (Nelson concerns)")

if __name__ == "__main__":
    generate_summary_report()

#
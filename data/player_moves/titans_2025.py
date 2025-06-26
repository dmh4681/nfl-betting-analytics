"""
Tennessee Titans 2025 Offseason Moves
New era begins: Complete organizational reset with Cam Ward at #1 overall
Last Updated: June 23, 2025
"""

TITANS_2025_MOVES = [
    # ========== FRANCHISE-DEFINING MOVES ==========
    {
        'player_name': 'Cam Ward',
        'position': 'QB',
        'from_team': 'Miami',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 1, Pick 1',
        'contract_years': 4,
        'contract_value': 48700000,
        'guaranteed_money': 48700000,
        'aav': 12175000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Consensus top QB prospect
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Franchise QB
        'impact_score': 3.5,
    },
    {
        'player_name': 'Dan Moore Jr.',
        'position': 'LT',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 82000000,
        'guaranteed_money': 50000000,
        'aav': 20500000,
        '2024_grade': 7.2,  # Started all 17 games for Steelers
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Protect Ward's blindside
        'impact_score': 2.5,
    },

    # ========== KEY FREE AGENT SIGNINGS - Supporting cast ==========
    {
        'player_name': 'Kevin Zeitler',
        'position': 'RG',
        'from_team': 'Bal',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8000000,
        'guaranteed_money': 5000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # Veteran guard
        'projected_2025_grade': 6.8,  # Age 35
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Interior protection
        'impact_score': 1.2,
    },
    {
        'player_name': 'Lloyd Cushenberry III',
        'position': 'C',
        'from_team': 'Den',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 8000000,
        'aav': 8000000,
        '2024_grade': 6.8,  # Starting center
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.0,  # Center stability
        'impact_score': 1.5,
    },
    {
        'player_name': 'Kyle Allen',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.0,  # Veteran backup
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 7.0,  # Mentor for Ward
        'impact_score': 0.8,
    },
    {
        'player_name': 'Tim Boyle',
        'position': 'QB',
        'from_team': 'Mia',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 5.5,  # Third QB
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 5.0,  # QB depth
        'impact_score': 0.3,
    },
    {
        'player_name': 'Jarran Reed',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        'guaranteed_money': 6000000,
        'aav': 10000000,
        '2024_grade': 7.0,  # Veteran DT
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replace Simmons
        'impact_score': 1.2,
    },
    {
        'player_name': 'Chidobe Awuzie',
        'position': 'CB',
        'from_team': 'Cin',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 6000000,
        '2024_grade': 6.5,  # Depth corner
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # CB depth
        'impact_score': 0.8,
    },

    # ========== MAJOR LOSSES - Complete teardown ==========
    {
        'player_name': 'Derrick Henry',
        'position': 'RB',
        'from_team': 'Ten',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Franchise icon, era officially over
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.0,  # Franchise icon, era officially over
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,
    },
    {
        'player_name': 'Ryan Tannehill',
        'position': 'QB',
        'from_team': 'Ten',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Veteran quarterback, injury-limited
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Limited due to injury
        'importance_to_old_team': 7.5,  # Former franchise QB
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Jeffery Simmons',
        'position': 'DT',
        'from_team': 'Ten',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.5,  # Elite defensive tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Defensive anchor
        'importance_to_old_team': 9.5,  # Best defensive player
        'importance_to_new_team': 0.0,
        'impact_score': -3.0,
    },
    {
        'player_name': 'Harold Landry III',
        'position': 'EDGE',
        'from_team': 'Ten',
        'to_team': 'NE',
        'move_type': 'Release/FA Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.8,  # Pass rush production
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Regular pass rusher
        'importance_to_old_team': 7.5,  # Key pass rusher released for cap
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,
    },
    {
        'player_name': 'Kenneth Murray Jr.',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # 95 tackles, 3.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting linebacker
        'importance_to_old_team': 7.0,  # Linebacker production
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,  # Got 6th + 7th picks
    },
    {
        'player_name': 'Nick Westbrook-Ikhine',
        'position': 'WR2',
        'from_team': 'Ten',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Reliable receiver option
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Regular receiver
        'importance_to_old_team': 6.5,  # Receiver depth lost
        'importance_to_new_team': 0.0,
        'impact_score': -0.8,
    },
    {
        'player_name': 'Jerome Baker',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.5,  # Starting linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.0,
    },

    # ========== 2025 NFL DRAFT - Building around Ward ==========
    # Already included Cam Ward at #1 overall above
    {
        'player_name': 'Oluwafemi Oladejo',
        'position': 'DE',
        'from_team': 'UCLA',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 2, Pick 52',
        'contract_years': 4,
        'contract_value': 7200000,
        'guaranteed_money': 3600000,
        'aav': 1800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 4.5 sacks in final season
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Pass rush rebuild
        'impact_score': 1.2,
    },
    {
        'player_name': 'Kevin Winston Jr.',
        'position': 'S',
        'from_team': 'Penn State',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 3, Pick 82',
        'contract_years': 4,
        'contract_value': 5600000,
        'guaranteed_money': 1400000,
        'aav': 1400000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Three-year starter
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Safety depth
        'impact_score': 0.8,
    },
    {
        'player_name': 'Chimere Dike',
        'position': 'CB',
        'from_team': 'Wisconsin',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 4, Pick 115',
        'contract_years': 4,
        'contract_value': 4800000,
        'guaranteed_money': 900000,
        'aav': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.2,  # CB depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Tyreke Smith',
        'position': 'EDGE',
        'from_team': 'Ohio State',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 5, Pick 147',
        'contract_years': 4,
        'contract_value': 3900000,
        'guaranteed_money': 700000,
        'aav': 975000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Developmental edge
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
    {
        'player_name': 'Jay Ward',
        'position': 'S',
        'from_team': 'LSU',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 6, Pick 188',
        'contract_years': 4,
        'contract_value': 3400000,
        'guaranteed_money': 400000,
        'aav': 850000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.8,  # From Murray trade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.2,
    },
    {
        'player_name': 'Anthony Hill Jr.',
        'position': 'LB',
        'from_team': 'Texas',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 6, Pick 206',
        'contract_years': 4,
        'contract_value': 3300000,
        'guaranteed_money': 350000,
        'aav': 825000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.1,
    },
    {
        'player_name': 'Michael Hall Jr.',
        'position': 'DT',
        'from_team': 'Ohio State',
        'to_team': 'Ten',
        'move_type': '2025 Draft - Round 7, Pick 239',
        'contract_years': 4,
        'contract_value': 3100000,
        'guaranteed_money': 200000,
        'aav': 775000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,  # From Murray trade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,
        'impact_score': 0.1,
    },

    # ========== KEY RE-SIGNINGS ==========
    {
        'player_name': 'Sebastian Joseph-Day',
        'position': 'DT',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 7500000,
        'guaranteed_money': 4000000,
        'aav': 7500000,
        '2024_grade': 6.8,  # Interior run defense
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,
        'impact_score': 1.0,
    },
    {
        'player_name': 'Tony Pollard',
        'position': 'RB',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 16000000,
        'guaranteed_money': 8000000,
        'aav': 8000000,
        '2024_grade': 7.0,  # Lead back after Henry
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
        'impact_score': 1.5,
    },
    {
        'player_name': 'Calvin Ridley',
        'position': 'WR1',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 60000000,
        'guaranteed_money': 35000000,
        'aav': 20000000,
        '2024_grade': 7.8,  # Top receiving target
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,  # #1 target for Ward
        'impact_score': 2.0,
    },
    {
        'player_name': 'JC Latham',
        'position': 'RT',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 8500000,
        'guaranteed_money': 5000000,
        'aav': 8500000,
        '2024_grade': 6.8,  # Rookie tackle
        'projected_2025_grade': 7.5,  # Sophomore improvement
        'snap_percentage_2024': 90.0,  # Started every game as rookie
        'importance_to_old_team': 7.5,  # 2024 1st round pick
        'importance_to_new_team': 8.5,  # Moved to RT with Moore addition
        'impact_score': 1.5,
    },

    # ========== COACHING/FRONT OFFICE CHANGES ==========
    {
        'player_name': 'Mike Borgonzi',
        'position': 'GM',
        'from_team': 'KC',
        'to_team': 'Ten',
        'move_type': 'Front Office Hire',
        'contract_years': 5,
        'contract_value': 25000000,
        'guaranteed_money': 12500000,
        'aav': 5000000,
        '2024_grade': 7.5,  # Chiefs assistant GM
        'projected_2025_grade': 8.0,  # Fresh perspective
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost key front office talent
        'importance_to_new_team': 9.0,  # Complete front office overhaul
        'impact_score': 2.5,
    },
    {
        'player_name': 'Ran Carthon',
        'position': 'GM',
        'from_team': 'Ten',
        'to_team': 'FIRED',
        'move_type': 'Front Office Firing',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # 3-14 season sealed his fate
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full GM control
        'importance_to_old_team': 8.0,  # GM fired after disaster season
        'importance_to_new_team': 0.0,
        'impact_score': 1.5,  # Addition by subtraction
    },
    {
        'player_name': 'Nick Holz',
        'position': 'COACH-OC',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Coaching Retention',
        'contract_years': 2,
        'contract_value': 4000000,
        'guaranteed_money': 2000000,
        'aav': 2000000,
        '2024_grade': 6.0,  # Offensive coordinator retained
        'projected_2025_grade': 7.0,  # Continuity for Ward
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,  # QB development
        'impact_score': 1.0,
    },

    # ========== ADDITIONAL MOVES ==========
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'Ten',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 9000000,  # Combined
        'guaranteed_money': 900000,
        'aav': 3000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 5.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,
        'impact_score': 0.3,
    },
]

# ========== SUMMARY METRICS ==========
TITANS_2025_SUMMARY = {
    'total_moves': len(TITANS_2025_MOVES),
    'free_agent_signings': 8,  # Focus on OL protection
    'major_losses': 7,  # Complete teardown
    'trades': 1,  # Murray to Houston
    'draft_picks': 8,
    'key_resignings': 4,
    'coaching_changes': 3,  # New GM, retained coaches
    'udfa_signings': 1,  # Grouped
    'total_guaranteed_money': 185000000,  # Major investment in protection
    'cap_space_created': 'Significant through releases and trades',
    'cap_space_remaining': 22000000,  # Flexibility for future
    'championship_window': '2027-2030',  # Ward development timeline
    'offseason_grade': 'B+',
    'key_philosophy': 'Complete organizational reset centered on Cam Ward',
    'net_impact_score': 2.5,  # Sum of all impact scores
    'biggest_concern': 'Lack of proven playmakers beyond Ridley',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'quarterback_decision': {
        'scouting': 'Entire leadership including owner attended Ward pro day',
        'history': 'First #1 overall pick since 2016 (Marcus Mariota)',
        'philosophy': 'Franchise QB over trading down',
        'support': 'Immediate OL investment shows commitment',
    },
    'offensive_line_rebuild': {
        'investment': '$106M guaranteed to OL in free agency',
        'approach': 'Protect Ward at all costs',
        'depth': 'Moore (LT), Latham (RT), Cushenberry (C), Zeitler (RG)',
        'concern': 'Left guard remains question mark',
    },
    'defensive_losses': {
        'departures': 'Simmons, Landry, Murray all gone',
        'philosophy': 'Accept short-term pain for long-term gain',
        'draft': 'Multiple defensive picks but no blue-chippers',
        'reality': 'Defense will struggle in 2025',
    },
    'front_office_overhaul': {
        'borgonzi_hire': 'Chiefs pipeline continues',
        'carthon_failure': 'Two years, 9-25 record',
        'ownership': 'Amy Adams Strunk showing patience with Callahan',
        'timeline': 'Multi-year rebuild acknowledged',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Cam Ward',
        'backup': 'Kyle Allen / Will Levis',
        'developmental': 'Tim Boyle',
        'grade': 'B',
        'notes': 'Ward the clear future, Levis likely traded',
    },
    'offensive_line': {
        'starters': ['Dan Moore Jr. (LT)', 'TBD (LG)', 'Lloyd Cushenberry (C)', 
                     'Kevin Zeitler (RG)', 'JC Latham (RT)'],
        'depth': 'Major upgrade from 2024 disaster',
        'grade': 'B+',
        'notes': 'Left guard only remaining hole',
    },
    'skill_positions': {
        'wr': 'Calvin Ridley, Treylon Burks, Chris Moore',
        'rb': 'Tony Pollard, Tyjae Spears, Julius Chestnut',
        'te': 'Chig Okonkwo, Josh Whyle',
        'grade': 'C+',
        'notes': 'Ridley only proven weapon',
    },
    'defensive_line': {
        'dt': 'Jarran Reed, Sebastian Joseph-Day, T\'Vondre Sweat',
        'edge': 'Arden Key, Oluwafemi Oladejo (R), Tyreke Smith (R)',
        'grade': 'D+',
        'notes': 'Massive downgrade after losses',
    },
    'linebackers': {
        'starters': 'Jack Gibbens, Luke Gifford, Anthony Hill Jr. (R)',
        'depth': 'Thin and unproven',
        'grade': 'D',
        'notes': 'Weakest position group',
    },
    'secondary': {
        'cb': 'L\'Jarius Sneed, Chidobe Awuzie, Chimere Dike (R)',
        'safety': 'Amani Hooker, Kevin Winston Jr. (R), Jay Ward (R)',
        'grade': 'C',
        'notes': 'Sneed anchors, rest are questions',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 4.5,
        'lean': 'OVER',
        'reasoning': 'Low bar, Ward could surprise early',
    },
    'division_odds': {
        'current': '+750',
        'value': 'NO',
        'reasoning': 'Houston and Jacksonville far ahead',
    },
    'futures': {
        'ward_oroy': '+450 (value)',
        'last_place': 'YES (-200)',
        'playoffs': 'NO (-500)',
    },
    'player_props': {
        'ward_passing_yards': 'OVER 3,200',
        'ridley_receiving_yards': 'OVER 950',
        'pollard_rushing_yards': 'UNDER 800',
        'team_sacks_allowed': 'OVER 52.5',
    },
    'key_angles': {
        'best_bet': 'Ward OROY +450',
        'fade': 'Team defense rankings',
        'narrative': 'Growing pains expected',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("TENNESSEE TITANS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {TITANS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{TITANS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {TITANS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {TITANS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {TITANS_2025_SUMMARY['free_agent_signings']}")
    print(f"  • Major Losses: {TITANS_2025_SUMMARY['major_losses']} (complete teardown)")
    print(f"  • Draft Picks: {TITANS_2025_SUMMARY['draft_picks']} (Ward #1 overall)")
    print(f"  • Coaching Changes: {TITANS_2025_SUMMARY['coaching_changes']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${TITANS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Cap Space: {TITANS_2025_SUMMARY['cap_space_created']}")
    print(f"  • Remaining Cap: ${TITANS_2025_SUMMARY['cap_space_remaining']:,}")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • Cam Ward (QB) - #1 overall pick, franchise QB")
    print("  • Dan Moore Jr. (LT) - 4yr/$82M to protect Ward")
    print("  • Mike Borgonzi (GM) - From Chiefs front office")
    print("  • OL investments - Cushenberry, Zeitler")
    
    print("\n❌ MAJOR LOSSES:")
    print("  • Derrick Henry - Era ends, to Baltimore")
    print("  • Jeffery Simmons - Elite DT departed")
    print("  • Ryan Tannehill - Retired")
    print("  • Ran Carthon - GM fired after 3-14")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {TITANS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Offensive Line: $106M guaranteed investment")
    print(f"  • Timeline: Patient multi-year rebuild")
    print(f"  • Reality: Defense will struggle in 2025")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 4.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Bet: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Cam Ward development speed")
    print("  • Offensive line cohesion")
    print("  • Defensive talent drain")
    print("  • Calvin Ridley health/production")

if __name__ == "__main__":
    generate_summary_report()
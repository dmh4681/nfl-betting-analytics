"""
Los Angeles Rams 2025 Offseason Moves
Strategic gambles for immediate contention and long-term flexibility under Les Snead
"""

RAMS_2025_MOVES = [
    # RAMS FREE AGENT SIGNINGS - Trading past glory for future firepower
    {
        'player_name': 'Davante Adams',
        'position': 'WR1',
        'from_team': 'NYJ',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 46000000,
        '2024_grade': 8.2,  # 103 catches for 1,509 yards in 2023, elite route runner
        'projected_2025_grade': 8.5,  # Better QB play with Stafford
        'snap_percentage_2024': 85.0,  # Primary target despite Jets dysfunction
        'importance_to_old_team': 7.5,  # Key veteran presence for Jets
        'importance_to_new_team': 9.5,  # Forms elite tandem with Puka Nacua
    },
    {
        'player_name': 'Poona Ford',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 29600000,
        '2024_grade': 8.8,  # 5th among interior defenders, 6th in run defense (PFF)
        'projected_2025_grade': 8.5,  # Addresses biggest weakness
        'snap_percentage_2024': 70.0,  # Key run-stopper for Chargers
        'importance_to_old_team': 8.5,  # Crucial to league's top scoring defense
        'importance_to_new_team': 9.0,  # Fixes run defense that allowed 100+ yards 15 times
    },
    {
        'player_name': 'Nate Landman',
        'position': 'LB',
        'from_team': 'Atl',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8500000,
        '2024_grade': 7.0,  # Solid linebacker production in Atlanta
        'projected_2025_grade': 7.2,  # Good scheme fit
        'snap_percentage_2024': 65.0,  # Starting linebacker
        'importance_to_old_team': 6.5,  # Depth piece for Falcons
        'importance_to_new_team': 7.5,  # Replaces Rozeboom/Hummel
    },
    {
        'player_name': 'Coleman Shelton',
        'position': 'C',
        'from_team': 'Chi',
        'to_team': 'LAR',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7000000,
        '2024_grade': 7.2,  # Solid center play in Chicago
        'projected_2025_grade': 7.5,  # Reunion with familiar system
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 6.0,  # Depth for Bears
        'importance_to_new_team': 8.0,  # Returns to familiar Rams system
    },

    # RAMS MAJOR LOSSES - Cooper Kupp era ends
    {
        'player_name': 'Cooper Kupp',
        'position': 'WR1',
        'from_team': 'LAR',
        'to_team': 'Sea',
        'move_type': 'Release/Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Injury-plagued season, 67 catches for 710 yards
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Limited by injuries
        'importance_to_old_team': 9.0,  # Super Bowl MVP, franchise icon
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Christian Rozeboom',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Starting linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Key defensive piece
        'importance_to_old_team': 7.5,  # Starting linebacker for 2 seasons
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jake Hummel',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Special teams ace, blocked punt for TD
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 15.0,  # Primarily special teams
        'importance_to_old_team': 6.5,  # Key special teams contributor
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jonah Jackson',
        'position': 'G',
        'from_team': 'LAR',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Disappointing first season in LA
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting guard despite struggles
        'importance_to_old_team': 6.0,  # Rare free agency miss
        'importance_to_new_team': 0.0,
    },

    # RAMS DRAFT PICKS - Strategic value extraction through trades
    {
        'player_name': 'Terrance Ferguson',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #58 (via ATL trade)',
        'contract_years': 4,
        'contract_value': 9500000,
        '2024_grade': 0.0,  # College - Oregon TE, fills critical void
        'projected_2025_grade': 7.0,  # Addresses league-worst TE production (459 yards)
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Critical need filled
    },
    {
        'player_name': 'Josaiah Stewart',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #87',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - Michigan edge rusher
        'projected_2025_grade': 6.8,  # Adds depth behind Verse/Young
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Pass rush depth
    },
    {
        'player_name': 'Jarquez Hunter',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #118',
        'contract_years': 4,
        'contract_value': 5100000,
        '2024_grade': 0.0,  # College - Auburn RB, 4.4 speed, SEC-leading yards after contact
        'projected_2025_grade': 7.2,  # Complements Kyren Williams perfectly
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Explosive speed element
    },
    {
        'player_name': 'Chris Paul Jr.',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #147',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,  # College - Ole Miss captain, didn't allow TD in 665 coverage snaps
        'projected_2025_grade': 7.0,  # Elite coverage linebacker
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replaces linebacker losses
    },
    {
        'player_name': 'Ty Hamilton',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #189',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Ohio State DT
        'projected_2025_grade': 6.5,  # Interior line depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Defensive line depth
    },
    {
        'player_name': 'Marcus Haynes',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'LAR',
        'move_type': '2025 Draft Pick #220',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,  # College - Late round corner
        'projected_2025_grade': 6.0,  # Developmental piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Secondary depth
    },

    # RAMS KEY RE-SIGNINGS - Securing the core and creating flexibility
    {
        'player_name': 'Alaric Jackson',
        'position': 'LT',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 57750000,
        '2024_grade': 8.0,  # Solid left tackle play
        'projected_2025_grade': 8.2,  # Should continue improving
        'snap_percentage_2024': 95.0,  # Full-time starter
        'importance_to_old_team': 9.0,  # Stafford's blindside protection
        'importance_to_new_team': 9.0,  # Critical retention
    },
    {
        'player_name': 'Matthew Stafford',
        'position': 'QB',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Restructure',
        'contract_years': 2,
        'contract_value': 40000000,  # 2026 guarantee if on roster
        '2024_grade': 8.5,  # Strong season despite injuries around him
        'projected_2025_grade': 8.3,  # Age 37 but still elite
        'snap_percentage_2024': 90.0,  # When healthy, full starter
        'importance_to_old_team': 10.0,  # Franchise quarterback
        'importance_to_new_team': 10.0,  # Championship window tied to him
    },
    {
        'player_name': 'Tutu Atwell',
        'position': 'WR3',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 10000000,
        '2024_grade': 7.0,  # Breakout season as slot receiver
        'projected_2025_grade': 7.5,  # Should continue developing
        'snap_percentage_2024': 60.0,  # Key role in 3-WR sets
        'importance_to_old_team': 7.0,  # Emerging slot threat
        'importance_to_new_team': 7.5,  # Fully guaranteed shows confidence
    },
    {
        'player_name': 'Jimmy Garoppolo',
        'position': 'QB',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Restructure',
        'contract_years': 1,
        'contract_value': 13500000,
        '2024_grade': 6.5,  # Limited action as backup
        'projected_2025_grade': 6.8,  # Veteran backup experience
        'snap_percentage_2024': 10.0,  # Backup role
        'importance_to_old_team': 6.0,  # Insurance policy
        'importance_to_new_team': 6.5,  # Maintains QB depth
    },
    {
        'player_name': 'Ahkello Witherspoon',
        'position': 'CB1',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 7.5,  # Solid corner play
        'projected_2025_grade': 7.3,  # Should maintain level
        'snap_percentage_2024': 80.0,  # Starting corner
        'importance_to_old_team': 7.5,  # Key secondary piece
        'importance_to_new_team': 7.5,  # Continuity in secondary
    },

    # RAMS COACHING CHANGES - Strategic additions to maximize talent
    {
        'player_name': 'Drew Wilkins',
        'position': 'PASS_RUSH_COORD',
        'from_team': 'BAL',
        'to_team': 'LAR',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 2500000,
        '2024_grade': 8.0,  # Ravens-style blitz packages
        'projected_2025_grade': 8.2,  # Should maximize Verse/Young
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost to Rams
        'importance_to_new_team': 8.0,  # Enhances pass rush scheme
    },
    {
        'player_name': 'Alex Van Pelt',
        'position': 'OFF_ASSISTANT',
        'from_team': 'NE',
        'to_team': 'LAR',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        '2024_grade': 7.5,  # Developed Drake Maye in New England
        'projected_2025_grade': 7.8,  # QB development expertise
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # Patriots coordinator
        'importance_to_new_team': 7.0,  # Insurance for QB transitions
    },
    {
        'player_name': 'Nathan Scheelhaase',
        'position': 'PASS_GAME_COORD',
        'from_team': 'LAR',
        'to_team': 'LAR',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 4500000,
        '2024_grade': 7.0,  # Internal promotion from quality control
        'projected_2025_grade': 7.5,  # McVay calls him a "stud"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Rising coach
        'importance_to_new_team': 7.5,  # Replaces Nick Caley
    },

    # RAMS DRAFT TRADES - Brilliant future asset accumulation
    {
        'player_name': '2026 1st Round Pick',
        'position': 'DRAFT_PICK',
        'from_team': 'Atl',
        'to_team': 'LAR',
        'move_type': 'Draft Trade (26th pick for 2025 2nd + 2026 1st)',
        'contract_years': 0,
        'contract_value': 15000000,  # Estimated value
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # Massive future value
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Atlanta's future asset
        'importance_to_new_team': 9.5,  # Insurance for post-Stafford era
    },

    # RAMS UDFA/DEPTH SIGNINGS - Maintaining roster depth
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'LAR',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 8000000,
        '2024_grade': 0.0,  # College prospects
        'projected_2025_grade': 5.5,  # Depth and special teams
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Future depth development
    },
]

# RAMS SUMMARY METRICS
RAMS_2025_SUMMARY = {
    'total_moves': len(RAMS_2025_MOVES),
    'free_agent_signings': 4,
    'major_losses': 4,
    'draft_picks': 6,
    'key_resignings': 5,
    'coaching_changes': 3,
    'trade_acquisitions': 1,  # 2026 1st round pick
    'total_guaranteed_money': 195000000,  # Includes major extensions
    'dead_money_absorbed': 50800000,  # 7th-most in NFL
    'salary_cap_space_remaining': 19600000,
    'projected_2026_cap_space': 75000000,
    'championship_window': '2025-2026',
    'offseason_grade': 'A-',
    'key_philosophy': 'Strategic gambles for immediate contention and long-term flexibility',
    'division_championship_odds': 34,  # ESPN Football Power Index
    'biggest_gamble': 'Replacing Kupp with Adams',
    'smartest_move': 'Trading 2025 1st for 2026 1st + immediate TE help',
    'critical_success_factor': 'Stafford health at age 37',
    'nfc_west_competition': 'NFL\'s most competitive division race'
}

# RAMS STRATEGIC ANALYSIS
RAMS_2025_ANALYSIS = {
    'offensive_philosophy': 'Maintain championship-caliber attack around aging Stafford',
    'defensive_transformation': 'Fixed fatal run defense flaw with Poona Ford signing',
    'salary_cap_strategy': 'Front-loaded contracts create future flexibility',
    'draft_approach': 'Immediate contributors over developmental projects',
    'coaching_evolution': 'Enhanced existing systems rather than wholesale changes',
    'biggest_risk': 'Aging core vs brutal NFC West schedule',
    'biggest_reward': 'Extended championship window + future asset accumulation',
    'key_extensions_needed': ['Puka Nacua ($24-30M AAV)', 'Kobie Turner ($20M+ AAV)'],
    'looming_challenges': ['Kyren Williams extension stalled', 'NFC West arms race'],
    'franchise_trajectory': 'Sustainable success rather than inevitable rebuild'
}

if __name__ == "__main__":
    print(f"Los Angeles Rams 2025 Offseason Moves: {RAMS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {RAMS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {RAMS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${RAMS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {RAMS_2025_SUMMARY['key_philosophy']}")
    print(f"Division Championship Odds: {RAMS_2025_SUMMARY['division_championship_odds']}%")
    print(f"Critical Success Factor: {RAMS_2025_SUMMARY['critical_success_factor']}")
    print(f"2026 Projected Cap Space: ${RAMS_2025_SUMMARY['projected_2026_cap_space']:,}")
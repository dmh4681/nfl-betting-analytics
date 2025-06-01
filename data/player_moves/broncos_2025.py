"""
Denver Broncos 2025 Offseason Moves
Calculated roster building for Bo Nix's critical second season
"""

BRONCOS_2025_MOVES = [
    # BRONCOS FREE AGENT SIGNINGS - Elite talent with injury risk strategy
    {
        'player_name': 'Talanoa Hufanga',
        'position': 'S',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 39000000,
        '2024_grade': 6.0,  # Limited by injuries, played 17 games over 2 seasons
        'projected_2025_grade': 8.5,  # All-Pro credentials from 2022 (97 tackles, 4 INTs)
        'snap_percentage_2024': 45.0,  # Injury-limited season
        'importance_to_old_team': 7.5,  # Former All-Pro safety
        'importance_to_new_team': 9.0,  # Transforms secondary alongside Surtain
    },
    {
        'player_name': 'Dre Greenlaw',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 31500000,
        '2024_grade': 5.5,  # Missed 15 games with torn Achilles from Super Bowl
        'projected_2025_grade': 8.0,  # Multiple 100-tackle seasons when healthy
        'snap_percentage_2024': 15.0,  # Limited return from injury
        'importance_to_old_team': 8.0,  # Elite linebacker when healthy
        'importance_to_new_team': 8.5,  # Payton's coveted linebacker upgrade
    },
    {
        'player_name': 'Evan Engram',
        'position': 'TE',
        'from_team': 'Jac',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 23000000,
        '2024_grade': 7.0,  # 51 catches despite missing 8 games
        'projected_2025_grade': 8.2,  # Payton's "Joker" player
        'snap_percentage_2024': 60.0,  # Injury-shortened season
        'importance_to_old_team': 8.0,  # Primary receiving threat
        'importance_to_new_team': 9.0,  # Sean Payton's coveted versatile weapon
    },
    {
        'player_name': 'Mekhi Becton',
        'position': 'G',
        'from_team': 'Phi',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 14000000,
        '2024_grade': 7.8,  # Helped Saquon rush for 2,000+ yards
        'projected_2025_grade': 7.5,  # Proven guard, scheme fit
        'snap_percentage_2024': 85.0,  # Starter with Eagles
        'importance_to_old_team': 7.0,  # Solid contributor
        'importance_to_new_team': 8.0,  # Interior line upgrade
    },
    {
        'player_name': 'Tre\'Davious White',
        'position': 'CB2',
        'from_team': 'LAR',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 6500000,
        '2024_grade': 6.5,  # Return from ACL tear
        'projected_2025_grade': 7.2,  # Former All-Pro upside
        'snap_percentage_2024': 70.0,  # Rotational role with Rams
        'importance_to_old_team': 6.5,  # Depth piece
        'importance_to_new_team': 7.5,  # CB2 opposite Surtain
    },
    {
        'player_name': 'Tyler Higbee',
        'position': 'TE',
        'from_team': 'LAR',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4200000,
        '2024_grade': 6.8,  # Veteran presence
        'projected_2025_grade': 6.5,  # Depth behind Engram
        'snap_percentage_2024': 55.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Longtime Ram
        'importance_to_new_team': 6.5,  # TE depth and experience
    },
    {
        'player_name': 'Josh Reynolds',
        'position': 'WR3',
        'from_team': 'Det',
        'to_team': 'Den',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3800000,
        '2024_grade': 7.0,  # 40 catches, 5 TDs before injury
        'projected_2025_grade': 7.2,  # Reliable veteran
        'snap_percentage_2024': 65.0,  # Solid contributor
        'importance_to_old_team': 7.0,  # Key depth piece
        'importance_to_new_team': 7.0,  # WR depth behind Sutton
    },

    # BRONCOS MAJOR LOSSES - Departures create cap space and opportunities
    {
        'player_name': 'Javonte Williams',
        'position': 'RB',
        'from_team': 'Den',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Never recaptured pre-ACL explosiveness
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,  # Split backfield duties
        'importance_to_old_team': 6.5,  # Former 2nd-round investment
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Zach Wilson',
        'position': 'QB',
        'from_team': 'Den',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Failed reclamation project
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 20.0,  # Limited backup role
        'importance_to_old_team': 5.0,  # Backup QB experiment
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Riley Dixon',
        'position': 'P',
        'from_team': 'Den',
        'to_team': 'TB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Solid punter
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Punter
        'importance_to_old_team': 6.0,  # Special teams contributor
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Tremon Smith',
        'position': 'S',
        'from_team': 'Den',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Special teams ace
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,  # Special teams focused
        'importance_to_old_team': 6.5,  # Special teams contributor
        'importance_to_new_team': 0.0,
    },

    # BRONCOS DRAFT PICKS - Value extraction through trades and targeted selections
    {
        'player_name': 'Jahdae Barron',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #20',
        'contract_years': 4,
        'contract_value': 22500000,
        '2024_grade': 0.0,  # College - Jim Thorpe Award winner
        'projected_2025_grade': 8.0,  # Top-12 talent, versatile DB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Multiple deployment options for Vance Joseph
    },
    {
        'player_name': 'RJ Harvey',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #60',
        'contract_years': 4,
        'contract_value': 8500000,
        '2024_grade': 0.0,  # College - 1,577 yards, 22 TDs, 6.8 YPC
        'projected_2025_grade': 7.5,  # Elite speed and receiving ability
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Replaces Williams, perfect for Payton system
    },
    {
        'player_name': 'Pat Bryant',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #85',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - Just 1 drop in 2024, physical style
        'projected_2025_grade': 7.0,  # Payton compared to Michael Thomas
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Possession receiver for Payton's system
    },
    {
        'player_name': 'Sai\'vion Jones',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #92',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - LSU pass rusher
        'projected_2025_grade': 6.8,  # Future starter potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush depth and development
    },
    {
        'player_name': 'Harold Fannin Jr.',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #128',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,  # College - Set FBS TE receiving records
        'projected_2025_grade': 6.5,  # Versatile chess piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Payton's system needs versatility
    },
    {
        'player_name': 'Tyre West',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #165',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - Developmental safety
        'projected_2025_grade': 6.0,  # Future depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Secondary depth development
    },
    {
        'player_name': 'Caleb Lohner',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Den',
        'move_type': '2025 Draft Pick #238',
        'contract_years': 4,
        'contract_value': 3200000,
        '2024_grade': 0.0,  # College - 6\'7" former basketball player
        'projected_2025_grade': 5.8,  # Athletic upside project like Jimmy Graham
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Payton's athletic TE project
    },

    # BRONCOS KEY RE-SIGNINGS - Securing core players
    {
        'player_name': 'D.J. Jones',
        'position': 'DT',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 39000000,
        '2024_grade': 8.2,  # Key part of league-leading defense
        'projected_2025_grade': 8.0,  # Defensive line anchor
        'snap_percentage_2024': 80.0,  # Key starter
        'importance_to_old_team': 9.0,  # Defensive cornerstone
        'importance_to_new_team': 9.0,  # Critical retention for defense
    },
    {
        'player_name': 'Jarrett Stidham',
        'position': 'QB',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 7.0,  # Reliable backup, mentor to Nix
        'projected_2025_grade': 7.0,  # Continuity in QB room
        'snap_percentage_2024': 25.0,  # Backup role
        'importance_to_old_team': 7.5,  # Nix's primary mentor
        'importance_to_new_team': 7.5,  # QB room stability
    },
    {
        'player_name': 'Lil\'Jordan Humphrey',
        'position': 'WR3',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2800000,
        '2024_grade': 6.5,  # Depth receiver
        'projected_2025_grade': 6.5,  # Maintains depth
        'snap_percentage_2024': 35.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Depth piece
        'importance_to_new_team': 6.0,  # WR depth
    },

    # BRONCOS COACHING CHANGES - Strategic enhancements
    {
        'player_name': 'Darren Rizzi',
        'position': 'ST_COACH',
        'from_team': 'NO',
        'to_team': 'Den',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 4500000,
        '2024_grade': 8.0,  # Payton reunion, Saints tenure
        'projected_2025_grade': 8.0,  # Proven coordinator
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Saints loss
        'importance_to_new_team': 7.5,  # Replaces retiring Westhoff
    },
    {
        'player_name': 'Davis Webb',
        'position': 'QB_COACH',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Promotion',
        'contract_years': 2,
        'contract_value': 2000000,
        '2024_grade': 7.0,  # Internal promotion
        'projected_2025_grade': 7.5,  # Critical for Nix development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # QB room continuity
        'importance_to_new_team': 8.0,  # Offensive pass game coordinator
    },
    {
        'player_name': 'Jim Leonhard',
        'position': 'DB_COACH',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Promotion',
        'contract_years': 2,
        'contract_value': 1800000,
        '2024_grade': 7.0,  # Internal promotion
        'projected_2025_grade': 7.5,  # Defensive pass game coordinator
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Defensive continuity
        'importance_to_new_team': 7.5,  # Maintains scheme continuity
    },

    # BRONCOS FRONT OFFICE CHANGES
    {
        'player_name': 'Reed Burckhardt',
        'position': 'AGM',
        'from_team': 'Den',
        'to_team': 'Den',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 3000000,
        '2024_grade': 0.0,  # Internal promotion after Mougey departure
        'projected_2025_grade': 7.0,  # Maintains Paton's philosophy
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Front office continuity
    },
    {
        'player_name': 'Jordan Dizon',
        'position': 'SCOUT',
        'from_team': 'Phi',
        'to_team': 'Den',
        'move_type': 'Front Office Hire',
        'contract_years': 2,
        'contract_value': 800000,
        '2024_grade': 7.5,  # Howie Roseman operation experience
        'projected_2025_grade': 7.5,  # Fresh perspectives
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # Eagles loss
        'importance_to_new_team': 6.5,  # Evaluation enhancement
    },
]

# BRONCOS SUMMARY METRICS
BRONCOS_2025_SUMMARY = {
    'total_moves': len(BRONCOS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 4,
    'draft_picks': 7,
    'key_resignings': 3,
    'coaching_changes': 3,
    'front_office_changes': 2,
    'total_guaranteed_money': 99500000,  # Major free agency investment
    'russell_wilson_dead_money': 32000000,  # Final year of albatross
    'salary_cap_space_remaining': 16500000,
    'projected_2026_cap_space': 85000000,  # When Wilson money clears
    'championship_window': '2026-2028',
    'offseason_grade': 'B+',
    'key_philosophy': 'Elite talent with injury risk, supporting Nix development',
    'afc_west_odds': '+425',  # Fourth favorites behind Chiefs
    'over_under_wins': 8.5,
    'defensive_rank_2024': 1,  # League-leading scoring defense
    'blitz_rate_2024': 46.3,  # NFL-leading
    'sacks_2024': 63,  # League-leading
}

if __name__ == "__main__":
    print(f"Denver Broncos 2025 Offseason Moves: {BRONCOS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {BRONCOS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {BRONCOS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${BRONCOS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Russell Wilson Dead Money (Final Year): ${BRONCOS_2025_SUMMARY['russell_wilson_dead_money']:,}")
    print(f"Philosophy: {BRONCOS_2025_SUMMARY['key_philosophy']}")
    print(f"AFC West Odds: {BRONCOS_2025_SUMMARY['afc_west_odds']}")
    print(f"Over/Under Wins: {BRONCOS_2025_SUMMARY['over_under_wins']}")
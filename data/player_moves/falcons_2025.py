"""
Atlanta Falcons 2025 Offseason Moves
Aggressive defensive rebuild signals make-or-break moment for franchise
"""

FALCONS_2025_MOVES = [
    # FALCONS FREE AGENT SIGNINGS - Defensive transformation
    {
        'player_name': 'Leonard Floyd',
        'position': 'EDGE',
        'from_team': 'SF',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        '2024_grade': 8.0,  # 8.5+ sacks in each of past 5 seasons
        'projected_2025_grade': 8.2,  # Proven veteran production
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Address 31st-ranked pass rush (31 sacks)
    },
    {
        'player_name': 'Morgan Fox',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 7.0,  # Interior pass rush depth
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.5,  # Interior rush help
    },
    {
        'player_name': 'Divine Deablo',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7500000,
        '2024_grade': 6.8,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Linebacker depth/competition
    },
    {
        'player_name': 'Mike Hughes',
        'position': 'CB2',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 18000000,
        '2024_grade': 7.5,  # Solid corner production
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,
    },
    {
        'player_name': 'Andy Dalton',
        'position': 'QB',
        'from_team': 'Car',
        'to_team': 'Atl',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 6.5,  # Veteran mentor role
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 25.0,  # Backup role
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Penix mentor
    },

    # FALCONS MAJOR LOSSES - Cap casualties and retirements
    {
        'player_name': 'Grady Jarrett',
        'position': 'DT',
        'from_team': 'Atl',
        'to_team': 'RELEASED',
        'move_type': 'Cap Casualty Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Still productive at 31
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,  # Franchise cornerstone for 9 years
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Drew Dalman',
        'position': 'C',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Reliable center
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.0,  # Key O-line piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kirk Cousins',
        'position': 'QB',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Benched/Backup',
        'contract_years': 1,
        'contract_value': 40000000,  # Still on roster but benched
        '2024_grade': 5.5,  # 16 INTs in 14 games, benched Week 16
        'projected_2025_grade': 6.0,  # Expensive backup
        'snap_percentage_2024': 85.0,  # Before benching
        'importance_to_old_team': 3.0,  # Failed starter
        'importance_to_new_team': 4.0,  # Awkward backup situation
    },

    # FALCONS 2025 DRAFT PICKS - Historic defensive investment
    {
        'player_name': 'Jalon Walker',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Atl',
        'move_type': '2025 Draft Pick #15',
        'contract_years': 4,
        'contract_value': 18500000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 7.0,  # Elite versatility but 6'1" frame questions
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # First of double edge rush picks
    },
    {
        'player_name': 'James Pearce Jr.',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Atl',
        'move_type': '2025 Draft Pick #26 (Traded Up)',
        'contract_years': 4,
        'contract_value': 16000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.2,  # Explosive athleticism, needs technical refinement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Historic franchise first - double 1st round EDGE
    },
    {
        'player_name': 'Xavier Watts',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Atl',
        'move_type': '2025 Draft Pick #88',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Safety depth
    },
    {
        'player_name': 'Billy Bowman Jr.',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Atl',
        'move_type': '2025 Draft Pick #142',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Safety development
    },

    # FALCONS KEY EXTENSIONS - Locking up core
    {
        'player_name': 'A.J. Terrell',
        'position': 'CB1',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 81000000,
        '2024_grade': 8.5,  # Elite corner production
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 90.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
    },
    {
        'player_name': 'Jake Matthews',
        'position': 'LT',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Contract Extension',
        'contract_years': 2,
        'contract_value': 45000000,
        '2024_grade': 7.8,  # Solid LT play
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 95.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 8.5,
    },
    {
        'player_name': 'Michael Penix Jr.',
        'position': 'QB',
        'from_team': 'Atl',
        'to_team': 'Atl',
        'move_type': 'Rookie Transition to Starter',
        'contract_years': 3,
        'contract_value': 12000000,  # Remaining rookie deal
        '2024_grade': 6.5,  # 775 yards, 3 TDs, 3 INTs in 3 games
        'projected_2025_grade': 7.5,  # Expected development
        'snap_percentage_2024': 15.0,  # Limited audition
        'importance_to_old_team': 8.5,  # Franchise QB transition
        'importance_to_new_team': 9.5,
    },

    # FALCONS COACHING CHANGES - New regime under Morris
    {
        'player_name': 'Raheem Morris',
        'position': 'COACH',
        'from_team': 'LAR',
        'to_team': 'Atl',
        'move_type': 'Head Coach Hire',
        'contract_years': 4,
        'contract_value': 20000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 8.0,  # Defensive expertise, championship experience
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Culture transformation
    },
    {
        'player_name': 'Jeff Ulbrich',
        'position': 'COACH',
        'from_team': 'NYJ',
        'to_team': 'Atl',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Aggressive scheme for pass rush
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Fix 31st-ranked defense
    },
    {
        'player_name': 'Arthur Smith',
        'position': 'COACH',
        'from_team': 'Atl',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # Three consecutive 7-10 seasons
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 2.0,  # Failed regime
        'importance_to_new_team': 0.0,
    },

    # FALCONS TRADES - Future sacrificed for present
    {
        'player_name': '2026 1st Round Pick',
        'position': 'DRAFT',
        'from_team': 'Atl',
        'to_team': 'Hou',
        'move_type': 'Draft Capital Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 0.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Future flexibility sacrificed
        'importance_to_new_team': 0.0,
    },
]

# FALCONS SUMMARY METRICS
FALCONS_2025_SUMMARY = {
    'total_moves': len(FALCONS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 3,
    'draft_picks': 5,  # Only 5 total picks after trading future capital
    'key_extensions': 3,
    'coaching_changes': 3,
    'trades': 1,
    'total_guaranteed_money': 180000000,  # Including extensions
    'dead_money': 16250000,  # From Jarrett release
    'cap_space_created': 28500000,  # From restructures and releases
    'championship_window': '2025-2027',
    'offseason_grade': 'B-',
    'key_philosophy': 'All-in defensive transformation with make-or-break urgency'
}

if __name__ == "__main__":
    print(f"Atlanta Falcons 2025 Offseason: {FALCONS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {FALCONS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {FALCONS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Created: ${FALCONS_2025_SUMMARY['cap_space_created']:,}")
    print(f"Philosophy: {FALCONS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: Floyd (EDGE), Walker & Pearce Jr. (1st round EDGEs), Morris (HC)")
    print(f"Key Losses: Grady Jarrett (released), Drew Dalman (FA), Cousins (benched)")
    print(f"Strategy: Historic defensive draft investment while betting on Penix development")
    print(f"Risk Level: HIGH - Traded 2026 1st, playoffs-or-bust for Fontenot/Morris")
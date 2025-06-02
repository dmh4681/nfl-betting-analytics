"""
Tampa Bay Buccaneers 2025 Offseason Moves
Strategic continuity maintains championship foundation while addressing defensive needs
"""

BUCS_2025_MOVES = [
    # BUCS FREE AGENT SIGNINGS - Targeted defensive additions
    {
        'player_name': 'Haason Reddick',
        'position': 'EDGE',
        'from_team': 'NYJ',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 14000000,
        '2024_grade': 5.5,  # Only 1 sack in 10 games after holdout
        'projected_2025_grade': 7.5,  # Bounce-back potential, 50.5 sacks 2020-2023
        'snap_percentage_2024': 65.0,  # When he played
        'importance_to_old_team': 4.0,  # Holdout issues
        'importance_to_new_team': 8.5,  # Address 29th-ranked pass rush
    },
    {
        'player_name': 'Anthony Walker Jr.',
        'position': 'LB',
        'from_team': 'Mia',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        '2024_grade': 7.0,  # Solid veteran presence
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replaces K.J. Britt
    },
    {
        'player_name': 'Charlie Heck',
        'position': 'OT',
        'from_team': 'Ari',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 6.0,  # Swing tackle depth
    },
    {
        'player_name': 'Kindle Vildor',
        'position': 'CB2',
        'from_team': 'Det',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.5,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # Cornerback depth
    },
    {
        'player_name': 'Riley Dixon',
        'position': 'P',
        'from_team': 'Sea',
        'to_team': 'TB',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 7.5,  # Averaged 46.7 yards per punt
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,  # Punter
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.0,  # Special teams upgrade
    },

    # BUCS KEY RE-SIGNINGS - Offensive continuity priority
    {
        'player_name': 'Chris Godwin',
        'position': 'WR1',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 66000000,
        '2024_grade': 8.5,  # Despite injury, franchise record offense
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 70.0,  # Before Week 7 ankle injury
        'importance_to_old_team': 9.5,  # Offensive centerpiece
        'importance_to_new_team': 9.5,
    },
    {
        'player_name': 'Ben Bredeson',
        'position': 'LG',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 22000000,
        '2024_grade': 8.0,  # Successful prove-it year
        'projected_2025_grade': 8.0,
        'snap_percentage_2024': 95.0,  # Key starter
        'importance_to_old_team': 8.5,  # O-line stability
        'importance_to_new_team': 8.5,
    },
    {
        'player_name': 'Kyle Trask',
        'position': 'QB',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2787000,
        '2024_grade': 6.0,  # Backup role
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': 'Sterling Shepard',
        'position': 'WR3',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 7.0,  # Mayfield connection from Oklahoma
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 6.5,
    },

    # BUCS 2025 DRAFT PICKS - Future planning with present impact
    {
        'player_name': 'Emeka Egbuka',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'TB',
        'move_type': '2025 Draft Pick #19',
        'contract_years': 4,
        'contract_value': 15500000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 7.5,  # 95th percentile separation rate
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Insurance for Evans at 32
    },
    {
        'player_name': 'Benjamin Morrison',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'TB',
        'move_type': '2025 Draft Pick #56',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Notre Dame standout
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Address secondary needs
    },
    {
        'player_name': 'Jacob Parrish',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'TB',
        'move_type': '2025 Draft Pick #87',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 4.35 speed, nickel specialist
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Tykee Smith moved to safety
    },
    {
        'player_name': 'David Walker',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'TB',
        'move_type': '2025 Draft Pick #124',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # Central Arkansas pass rusher
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Pass rush depth
    },
    {
        'player_name': 'Elijah Roberts',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'TB',
        'move_type': '2025 Draft Pick #156',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # Led FBS with 131 QB pressures over 2 seasons
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Versatile pass rusher
    },

    # BUCS COACHING CHANGES
    {
        'player_name': 'Josh Grizzard',
        'position': 'COACH',
        'from_team': 'TB',
        'to_team': 'TB',
        'move_type': 'Promotion to OC',
        'contract_years': 2,
        'contract_value': 2000000,
        '2024_grade': 7.5,  # Helped franchise record offense
        'projected_2025_grade': 8.0,  # Internal promotion maintains continuity
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Replaces Liam Coen
    },
    {
        'player_name': 'Mike Caldwell',
        'position': 'COACH',
        'from_team': 'FA',
        'to_team': 'TB',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1200000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # Former Jaguars DC experience
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Inside LB coach
    },
    {
        'player_name': 'Charlie Strong',
        'position': 'COACH',
        'from_team': 'Alabama',
        'to_team': 'TB',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Championship pedigree from Alabama
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Defensive line coach
    },

    # BUCS LOSSES (Minimal due to retention strategy)
    {
        'player_name': 'K.J. Britt',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.0,  # Replaced by Walker Jr.
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Liam Coen',
        'position': 'COACH',
        'from_team': 'TB',
        'to_team': 'Jac',
        'move_type': 'Coaching Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.5,  # Coordinated franchise record offense
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,  # Major loss, but promoted internally
        'importance_to_new_team': 0.0,
    },
]

# BUCS SUMMARY METRICS
BUCS_2025_SUMMARY = {
    'total_moves': len(BUCS_2025_MOVES),
    'free_agent_signings': 5,
    'key_resignings': 4,
    'draft_picks': 5,
    'coaching_changes': 4,
    'major_losses': 2,
    'total_guaranteed_money': 115000000,  # Including extensions
    'dead_money': 8500000,  # Minimal due to retention strategy
    'cap_space_remaining': 26600000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B+',
    'key_philosophy': 'Offensive continuity with targeted defensive improvements'
}

if __name__ == "__main__":
    print(f"Tampa Bay Buccaneers 2025 Offseason: {BUCS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {BUCS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {BUCS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${BUCS_2025_SUMMARY['cap_space_remaining']:,}")
    print(f"Philosophy: {BUCS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: Reddick (EDGE), Egbuka (WR), Morrison (CB)")
    print(f"Key Retentions: Godwin extension, Bredeson extension, All 11 offensive starters")
    print(f"Strategy: Maintain offensive excellence while improving 29th-ranked pass rush")
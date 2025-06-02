"""
Carolina Panthers 2025 Offseason Moves
Complete analysis of aggressive defensive rebuild transformation
"""

PANTHERS_2025_MOVES = [
    # PANTHERS MAJOR DEFENSIVE FREE AGENT SIGNINGS - $126M+ investment
    {
        'player_name': 'Tershawn Wharton',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 54000000,
        '2024_grade': 8.0,  # Key piece of Chiefs defense
        'projected_2025_grade': 8.2,  # Should maintain production
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,  # Important KC defender
        'importance_to_new_team': 9.0,  # Cornerstone of rebuild
    },
    {
        'player_name': "Tre'von Moehrig",
        'position': 'S',
        'from_team': 'LV',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 51000000,
        '2024_grade': 7.8,  # Solid safety production
        'projected_2025_grade': 8.0,  # Should improve in better defense
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.0,  # Raiders defensive leader
        'importance_to_new_team': 9.5,  # Critical safety upgrade
    },
    {
        'player_name': 'Bobby Brown III',
        'position': 'DT',
        'from_team': 'LAR',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 21000000,
        '2024_grade': 7.2,  # Solid rotation piece
        'projected_2025_grade': 7.5,  # Bigger role expected
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 8.0,  # Interior line depth
    },
    {
        'player_name': 'Patrick Jones II',
        'position': 'EDGE',
        'from_team': 'Min',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 7.5,  # Productive pass rusher
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 8.5,  # Pass rush upgrade
    },
    {
        'player_name': 'Christian Rozeboom',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 7.0,  # Reliable linebacker
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 8.0,  # LB depth needed
    },
    {
        'player_name': 'Sam Martin',
        'position': 'P',
        'from_team': 'Buf',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 7.5,  # Solid punter
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Special teams upgrade
    },
    
    # PANTHERS OFFENSIVE ADDITION
    {
        'player_name': 'Rico Dowdle',
        'position': 'RB',
        'from_team': 'Dal',
        'to_team': 'Car',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 6250000,  # Up to $6.25M with incentives
        '2024_grade': 8.0,  # 1,079 yards, first undrafted 1,000-yard rusher for Cowboys
        'projected_2025_grade': 7.8,  # Should maintain production
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 7.5,  # Cowboys lead back
        'importance_to_new_team': 8.5,  # Major RB upgrade
    },
    
    # PANTHERS MAJOR LOSSES - Cap casualties and departures
    {
        'player_name': 'Miles Sanders',
        'position': 'RB',
        'from_team': 'Car',
        'to_team': 'RELEASED',
        'move_type': 'Released',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Major disappointment
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,  # Underperformed contract
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jadeveon Clowney',
        'position': 'EDGE',
        'from_team': 'Car',
        'to_team': 'RELEASED',
        'move_type': 'Released',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Aging veteran
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 6.5,  # Veteran presence
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Xavier Woods',
        'position': 'S',
        'from_team': 'Car',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Played all 1,218 defensive snaps - most in NFL
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.0,  # Iron man safety
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Shaq Thompson',
        'position': 'LB',
        'from_team': 'Car',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Franchise legend
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,  # 13-season veteran, team captain
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Johnny Hekker',
        'position': 'P',
        'from_team': 'Car',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jordan Fuller',
        'position': 'S',
        'from_team': 'Car',
        'to_team': 'Atl',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Ian Thomas',
        'position': 'TE',
        'from_team': 'Car',
        'to_team': 'LV',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
    },
    
    # PANTHERS TRADES - Draft capital accumulation
    {
        'player_name': 'Diontae Johnson',
        'position': 'WR',
        'from_team': 'Car',
        'to_team': 'Bal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Underperformed expectations
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.0,  # Failed acquisition
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jonathan Mingo',
        'position': 'WR',
        'from_team': 'Car',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Disappointing second-round pick
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 0.0,
    },
    
    # PANTHERS 2025 DRAFT - WR focus + defensive depth
    {
        'player_name': 'Tetairoa McMillan',
        'position': 'WR1',
        'from_team': 'DRAFT',
        'to_team': 'Car',
        'move_type': '2025 Draft Pick #8',
        'contract_years': 4,
        'contract_value': 35000000,
        '2024_grade': 0.0,  # College
        'projected_2025_grade': 8.0,  # Elite college production, compared to Mike Evans
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Bryce Young's new #1 target
    },
    {
        'player_name': 'Nic Scourton',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Car',
        'move_type': '2025 Draft Pick #51',
        'contract_years': 4,
        'contract_value': 9000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # High athletic upside
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Pass rush depth
    },
    {
        'player_name': 'Princely Umanmielen',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Car',
        'move_type': '2025 Draft Pick #77',
        'contract_years': 4,
        'contract_value': 5500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Edge rush development
    },
    {
        'player_name': 'Trevor Etienne',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Car',
        'move_type': '2025 Draft Pick #124',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # RB depth
    },
    {
        'player_name': 'Lathan Ransom',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Car',
        'move_type': '2025 Draft Pick #158',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Safety depth
    },
    
    # PANTHERS KEY RE-SIGNINGS - Cornerstone extension
    {
        'player_name': 'Jaycee Horn',
        'position': 'CB1',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 100000000,
        '2024_grade': 8.5,  # Elite when healthy
        'projected_2025_grade': 8.8,  # Entering prime
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.5,  # Defensive cornerstone
    },
    {
        'player_name': 'Andy Dalton',
        'position': 'QB',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 7.0,  # Valuable mentor
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 7.5,  # Bryce Young mentor
        'importance_to_new_team': 8.0,  # Critical for Young's development
    },
    {
        'player_name': 'Mike Jackson',
        'position': 'CB2',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 14500000,
        '2024_grade': 7.5,  # Led team with 17 pass deflections
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Secondary continuity
    },
    {
        'player_name': 'Raheem Blackshear',
        'position': 'DEPTH',
        'from_team': 'Car',
        'to_team': 'Car',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 3000000,
        '2024_grade': 7.8,  # 2nd in NFL with 791 gross return yards
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 7.0,  # Elite returner
        'importance_to_new_team': 7.5,  # Special teams value
    },
]

# PANTHERS SUMMARY METRICS
PANTHERS_2025_SUMMARY = {
    'total_moves': len(PANTHERS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 7,
    'draft_picks': 5,
    'key_resignings': 4,
    'trades': 2,
    'releases': 2,
    'total_guaranteed_money': 126000000,  # Massive defensive investment
    'dead_money': 8800000,  # Clean cap sheet
    'cap_space_remaining': 18700000,  # Conservative estimate
    'championship_window': '2026-2027',
    'offseason_grade': 'A-',
    'key_philosophy': 'Aggressive defensive rebuild while supporting Bryce Young development'
}

if __name__ == "__main__":
    print(f"Carolina Panthers 2025 Offseason: {PANTHERS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {PANTHERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {PANTHERS_2025_SUMMARY['championship_window']}")
    print(f"Total Investment: ${PANTHERS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {PANTHERS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: McMillan (WR), Wharton (DT), Moehrig (S), Dowdle (RB)")
    print(f"Key Losses: Woods (S), Thompson (LB), Sanders (released)")
    print(f"Strategy: $126M+ defensive investment with elite WR for Young")
    print(f"Defensive Focus: 6 of 7 draft picks, massive FA spending on defense")
    print(f"Horn Extension: $100M makes him highest-paid DB in NFL")
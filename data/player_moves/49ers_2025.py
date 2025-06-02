"""
San Francisco 49ers 2025 Offseason Moves
Historic roster transformation: $86.6M dead money enables youth movement and financial reset
"""

NINERS_2025_MOVES = [
    # 49ERS MAJOR ROSTER PURGE - Historic dead money for future flexibility
    {
        'player_name': 'Deebo Samuel',
        'position': 'WR1',
        'from_team': 'SF',
        'to_team': 'Was',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Only 670 yards, disgruntled and limited
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Still primary receiver despite issues
        'importance_to_old_team': 8.5,  # Former All-Pro, $31.5M dead money hit
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kyle Juszczyk',
        'position': 'FB',
        'from_team': 'SF',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # 9-time Pro Bowl fullback
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Key in Shanahan's system
        'importance_to_old_team': 8.0,  # Iconic player, $4.1M savings
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Javon Hargrave',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Solid interior pass rusher
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Key defensive lineman
        'importance_to_old_team': 8.0,  # Major cap savings needed
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Leonard Floyd',
        'position': 'EDGE',
        'from_team': 'SF',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Productive edge rusher
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Key pass rusher
        'importance_to_old_team': 7.5,  # Couldn't afford to retain
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Dre Greenlaw',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # Elite linebacker when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Injured most of season
        'importance_to_old_team': 8.5,  # Key defensive leader
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Charvarius Ward',
        'position': 'CB1',
        'from_team': 'SF',
        'to_team': 'Ind',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.8,  # Solid corner, couldn't afford extension
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Starting corner
        'importance_to_old_team': 8.0,  # Key secondary piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Talanoa Hufanga',
        'position': 'S',
        'from_team': 'SF',
        'to_team': 'Den',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Injury-limited season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,  # Missed significant time
        'importance_to_old_team': 7.0,  # Former All-Pro
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Maliek Collins',
        'position': 'DT',
        'from_team': 'SF',
        'to_team': 'Cle',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 45 pressures, productive season
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,  # Key rotation piece
        'importance_to_old_team': 7.0,  # Solid 3-technique
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Aaron Banks',
        'position': 'G',
        'from_team': 'SF',
        'to_team': 'GB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # Starting guard
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 7.5,  # Key offensive lineman
        'importance_to_new_team': 0.0,
    },

    # 49ERS KEY SIGNINGS - Targeted veteran additions amid youth movement
    {
        'player_name': 'Luke Farrell',
        'position': 'TE',
        'from_team': 'Jac',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 20250000,
        '2024_grade': 7.0,  # Solid blocking tight end
        'projected_2025_grade': 7.5,  # Good scheme fit with Kittle
        'snap_percentage_2024': 60.0,  # Versatile role
        'importance_to_old_team': 6.5,  # Key piece for Jaguars
        'importance_to_new_team': 8.0,  # Replaces Juszczyk's role partially
    },
    {
        'player_name': 'Demarcus Robinson',
        'position': 'WR2',
        'from_team': 'LAR',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 9500000,
        '2024_grade': 6.8,  # Solid veteran receiver
        'projected_2025_grade': 7.2,  # Good scheme fit
        'snap_percentage_2024': 55.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Depth piece for Rams
        'importance_to_new_team': 7.5,  # Helps replace Deebo's production
    },
    {
        'player_name': 'Mac Jones',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 7000000,
        '2024_grade': 6.0,  # Struggled as Patriots starter
        'projected_2025_grade': 7.0,  # Reunion with coaches who wanted to draft him
        'snap_percentage_2024': 70.0,  # Starting QB for struggling team
        'importance_to_old_team': 6.0,  # Former 1st round pick
        'importance_to_new_team': 7.0,  # Major backup upgrade
    },
    {
        'player_name': 'Andre Dillard',
        'position': 'OT',
        'from_team': 'GB',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.0,  # Backup tackle
        'projected_2025_grade': 6.5,  # Depth signing
        'snap_percentage_2024': 30.0,  # Limited role
        'importance_to_old_team': 5.0,  # Depth piece
        'importance_to_new_team': 6.5,  # OL depth needed
    },
    {
        'player_name': 'Nicholas Petit-Frere',
        'position': 'OT',
        'from_team': 'Ten',
        'to_team': 'SF',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2800000,
        '2024_grade': 5.8,  # Concerning pass protection metrics
        'projected_2025_grade': 6.2,  # Depth and competition
        'snap_percentage_2024': 40.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth for Titans
        'importance_to_new_team': 6.0,  # OL competition
    },

    # 49ERS DRAFT - Youth movement with first 5 picks on defense
    {
        'player_name': 'Mykel Williams',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #11',
        'contract_years': 4,
        'contract_value': 28500000,
        '2024_grade': 0.0,  # College - Georgia edge rusher, 14 career sacks
        'projected_2025_grade': 7.5,  # Nick Bosa's new running mate
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Immediate starter opposite Bosa
    },
    {
        'player_name': 'Alfred Collins',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #43',
        'contract_years': 4,
        'contract_value': 12800000,
        '2024_grade': 0.0,  # College - Texas DT, 6'6" 332 lbs, 2.9 YPC allowed
        'projected_2025_grade': 7.2,  # Addresses 28th-ranked run defense
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Critical run defense need
    },
    {
        'player_name': 'Nick Martin',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #75',
        'contract_years': 4,
        'contract_value': 7200000,
        '2024_grade': 0.0,  # College - Oklahoma LB
        'projected_2025_grade': 7.0,  # Replaces Dre Greenlaw
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Critical linebacker need
    },
    {
        'player_name': 'Upton Stout',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #107',
        'contract_years': 4,
        'contract_value': 5800000,
        '2024_grade': 0.0,  # College - 0 TDs allowed in 409 coverage snaps
        'projected_2025_grade': 7.0,  # Immediate starter potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replaces Ward
    },
    {
        'player_name': 'C.J. West',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #139',
        'contract_years': 4,
        'contract_value': 4900000,
        '2024_grade': 0.0,  # College - Interior line depth
        'projected_2025_grade': 6.5,  # Developmental piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Interior line rebuild
    },
    {
        'player_name': 'Jalen McLeod',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #171',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - New Mexico State WR
        'projected_2025_grade': 6.0,  # Developmental receiver
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # WR depth after Deebo trade
    },
    {
        'player_name': 'Cameron Calhoun',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #203',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Liberty LB
        'projected_2025_grade': 6.0,  # Special teams contributor
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # LB depth
    },
    {
        'player_name': 'Marcus Belton',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'SF',
        'move_type': '2025 Draft Pick #235',
        'contract_years': 4,
        'contract_value': 3400000,
        '2024_grade': 0.0,  # College - NC State S
        'projected_2025_grade': 5.8,  # Developmental safety
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Safety depth
    },

    # 49ERS KEY EXTENSIONS - Locking up the core
    {
        'player_name': 'Brock Purdy',
        'position': 'QB',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Extension',
        'contract_years': 5,
        'contract_value': 265000000,
        '2024_grade': 8.0,  # Strong season despite offensive struggles
        'projected_2025_grade': 8.5,  # Should improve with better weapons
        'snap_percentage_2024': 95.0,  # Franchise quarterback
        'importance_to_old_team': 10.0,  # Future of franchise
        'importance_to_new_team': 10.0,  # Record-breaking extension
    },
    {
        'player_name': 'Fred Warner',
        'position': 'LB',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Extension',
        'contract_years': 5,
        'contract_value': 95000000,
        '2024_grade': 9.0,  # All-Pro linebacker, defensive captain
        'projected_2025_grade': 8.8,  # Should remain elite
        'snap_percentage_2024': 95.0,  # Every-down linebacker
        'importance_to_old_team': 10.0,  # Defensive anchor
        'importance_to_new_team': 10.0,  # $56M guaranteed through 2029
    },
    {
        'player_name': 'George Kittle',
        'position': 'TE',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 76000000,
        '2024_grade': 8.5,  # Elite tight end when healthy
        'projected_2025_grade': 8.3,  # Should remain top-tier
        'snap_percentage_2024': 80.0,  # Key offensive weapon
        'importance_to_old_team': 9.5,  # Cornerstone player
        'importance_to_new_team': 9.5,  # Critical retention
    },
    {
        'player_name': 'Jauan Jennings',
        'position': 'WR2',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 21000000,
        '2024_grade': 7.5,  # Breakout season, 82 catches for 1,140 yards
        'projected_2025_grade': 8.0,  # Should be #1 WR now
        'snap_percentage_2024': 70.0,  # Emerging star
        'importance_to_old_team': 8.0,  # Key receiver after Deebo trade
        'importance_to_new_team': 8.5,  # Critical retention
    },

    # 49ERS COACHING CHANGES - Robert Saleh returns to fix defense
    {
        'player_name': 'Robert Saleh',
        'position': 'DC',
        'from_team': 'NYJ',
        'to_team': 'SF',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 12000000,
        '2024_grade': 7.0,  # Fired from Jets but great defensive mind
        'projected_2025_grade': 9.0,  # Reunion with 49ers system
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,  # Fired by Jets
        'importance_to_new_team': 9.5,  # "Biggest under-the-radar addition"
    },
    {
        'player_name': 'Klay Kubiak',
        'position': 'OC',
        'from_team': 'SF',
        'to_team': 'SF',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 4500000,
        '2024_grade': 7.0,  # Internal promotion, worked with Purdy
        'projected_2025_grade': 7.5,  # Shanahan retains play-calling
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Passing game coordinator
        'importance_to_new_team': 7.0,  # Succession planning
    },

    # 49ERS UDFA SIGNINGS - Building depth through development
    {
        'player_name': 'Multiple UDFAs',
        'position': 'DEPTH',
        'from_team': 'COLLEGE',
        'to_team': 'SF',
        'move_type': 'UDFA Signings',
        'contract_years': 3,
        'contract_value': 12000000,
        '2024_grade': 0.0,  # College prospects
        'projected_2025_grade': 5.5,  # Development pieces
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Youth movement depth
    },
]

# 49ERS SUMMARY METRICS
NINERS_2025_SUMMARY = {
    'total_moves': len(NINERS_2025_MOVES),
    'major_releases_trades': 9,  # Historic roster purge
    'free_agent_signings': 5,
    'draft_picks': 8,
    'key_extensions': 4,
    'coaching_changes': 2,
    'udfa_signings': 1,  # Grouped as one entry
    'total_guaranteed_money': 485000000,  # Includes massive Purdy deal
    'dead_money_absorbed': 86600000,  # League-high, historic
    'salary_cap_space_created': 50000000,  # Current flexibility
    'projected_2027_cap_space': 100000000,  # When dead money clears
    'championship_window': '2026-2029',  # Post-transition
    'offseason_grade': 'B+/A-',  # Bold strategy with risk
    'key_philosophy': 'Accept short-term pain for long-term flexibility',
    'schedule_strength': 0.415,  # NFL\'s easiest since 2015 Falcons
    'rookie_starters_projected': 6,  # Historic youth movement
    'division_championship_odds': 36,  # Highest in NFC West despite turnover
    'biggest_gamble': 'Six potential rookie starters on defense',
    'smartest_move': 'Robert Saleh return as DC',
    'franchise_trajectory': 'Controlled regression leading to sustainable excellence'
}

# 49ERS STRATEGIC ANALYSIS
NINERS_2025_ANALYSIS = {
    'financial_strategy': 'Historic $86.6M dead money hit creates future flexibility',
    'roster_philosophy': 'Youth movement with veteran leadership (Bosa, Warner, Kittle)',
    'defensive_transformation': 'First 5 draft picks on defense since 1981',
    'offensive_continuity': 'Shanahan system with upgraded weapons around Purdy',
    'coaching_masterclass': 'Saleh return could be difference-maker for young defense',
    'schedule_advantage': 'NFL\'s easiest schedule (.415) aids transition',
    'biggest_risk': 'Six rookie defensive starters in year one',
    'biggest_reward': 'Young, cheap defense with $100M+ cap space by 2027',
    'nfc_west_outlook': 'Transition year but still competitive due to schedule',
    'purdy_factor': 'Record $265M deal structured to minimize 2025 impact ($9.1M cap hit)',
    'saleh_impact': 'Reunites with system that made him coaching star',
    'future_extensions_needed': ['Nick Bosa (eventual)', 'Trent Williams succession'],
    'championship_timeline': 'Sacrifice 2025 competitiveness for 2026-2029 dominance'
}

# 49ERS RISK ASSESSMENT
NINERS_2025_RISKS = {
    'immediate_risks': [
        'Six rookie defensive starters',
        'Aging offensive core (Williams 37, Kittle 31, McCaffrey 29)',
        'Limited veteran receiver depth after Deebo trade',
        'Offensive line concerns after Banks departure'
    ],
    'medium_term_risks': [
        'NFC West arms race with Rams/Cardinals improvements',
        'Rookie development timeline may not align with schedule advantage',
        'Injury concerns with aging skill position players'
    ],
    'long_term_rewards': [
        'Young defense anchored by Bosa/Warner',
        'Massive cap flexibility when dead money clears',
        'Purdy locked up through prime years',
        'Strong draft capital for continued building'
    ]
}

if __name__ == "__main__":
    print(f"San Francisco 49ers 2025 Offseason Moves: {NINERS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {NINERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {NINERS_2025_SUMMARY['championship_window']}")
    print(f"Dead Money Absorbed: ${NINERS_2025_SUMMARY['dead_money_absorbed']:,}")
    print(f"Philosophy: {NINERS_2025_SUMMARY['key_philosophy']}")
    print(f"Schedule Strength: {NINERS_2025_SUMMARY['schedule_strength']} (NFL's easiest)")
    print(f"Projected Rookie Starters: {NINERS_2025_SUMMARY['rookie_starters_projected']}")
    print(f"Division Championship Odds: {NINERS_2025_SUMMARY['division_championship_odds']}%")
    print(f"Biggest Gamble: {NINERS_2025_SUMMARY['biggest_gamble']}")
    print(f"2027 Projected Cap Space: ${NINERS_2025_SUMMARY['projected_2027_cap_space']:,}")
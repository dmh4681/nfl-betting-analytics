"""
Detroit Lions 2025 Offseason Moves
Complete analysis of championship core maintenance despite coordinator exodus under Brad Holmes and Dan Campbell
"""

LIONS_2025_MOVES = [
    # LIONS FREE AGENT SIGNINGS - Minimal external additions, internal focus
    {
        'player_name': 'D.J. Reed',
        'position': 'CB1',
        'from_team': 'NYJ',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 48000000,
        '2024_grade': 7.8,  # 70.1 PFF coverage grade, 58.3% completion allowed
        'projected_2025_grade': 8.0,  # Direct Carlton Davis replacement
        'snap_percentage_2024': 85.0,  # Jets starting corner
        'importance_to_old_team': 7.5,  # Jets secondary anchor lost
        'importance_to_new_team': 8.5,  # Proven consistency over flashy alternative
    },
    {
        'player_name': 'Roy Lopez',
        'position': 'DT',
        'from_team': 'Min',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4650000,
        '2024_grade': 6.8,  # Solid rotational defensive tackle
        'projected_2025_grade': 7.0,  # Alim McNeill ACL recovery insurance
        'snap_percentage_2024': 55.0,  # Vikings rotation piece
        'importance_to_old_team': 6.5,  # Minnesota depth lost
        'importance_to_new_team': 7.5,  # Critical injury insurance
    },
    {
        'player_name': 'Grant Stuard',
        'position': 'LB',
        'from_team': 'TB',
        'to_team': 'Det',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1700000,
        '2024_grade': 6.5,  # Special teams ace
        'projected_2025_grade': 6.8,  # Special teams upgrade
        'snap_percentage_2024': 30.0,  # Limited defensive snaps, heavy ST
        'importance_to_old_team': 6.0,  # Bucs special teams contributor
        'importance_to_new_team': 7.0,  # $1.7M fully guaranteed shows value
    },

    # LIONS KEY RE-SIGNINGS - Retaining own free agents priority
    {
        'player_name': 'Derrick Barnes',
        'position': 'LB',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 25500000,
        '2024_grade': 7.5,  # Solid linebacker production
        'projected_2025_grade': 7.8,  # Retained before free agency
        'snap_percentage_2024': 70.0,  # Starting linebacker
        'importance_to_old_team': 8.0,  # Homegrown talent retained
        'importance_to_new_team': 8.0,  # 3-year security before market
    },

    # LIONS HISTORIC EXTENSIONS - $332M guaranteed to core
    {
        'player_name': 'Jared Goff',
        'position': 'QB',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 212000000,
        '2024_grade': 8.8,  # NFL's 2nd-highest paid QB, elite 2024 season
        'projected_2025_grade': 8.8,  # System mastery with Campbell
        'snap_percentage_2024': 95.0,  # Franchise quarterback
        'importance_to_old_team': 10.0,  # $170M guaranteed commitment
        'importance_to_new_team': 10.0,  # $32.6M cap hit despite massive deal
    },
    {
        'player_name': 'Penei Sewell',
        'position': 'RT',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 112000000,
        '2024_grade': 9.0,  # Elite right tackle, set OL market
        'projected_2025_grade': 9.0,  # 24 years old, entering prime
        'snap_percentage_2024': 95.0,  # Anchor of championship OL
        'importance_to_old_team': 9.5,  # Cornerstone protection piece
        'importance_to_new_team': 9.5,  # Long-term security at 24
    },
    {
        'player_name': 'Amon-Ra St. Brown',
        'position': 'WR1',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 120000000,
        '2024_grade': 8.8,  # Elite slot receiver, briefly highest-paid WR
        'projected_2025_grade': 8.8,  # Goff's favorite target
        'snap_percentage_2024': 90.0,  # Primary receiving threat
        'importance_to_old_team': 9.0,  # Homegrown superstar secured
        'importance_to_new_team': 9.0,  # $33.1M cap hit in 2026
    },

    # LIONS MAJOR LOSSES - Coordinator exodus and cap casualties
    {
        'player_name': 'Ben Johnson',
        'position': 'OC',
        'from_team': 'Det',
        'to_team': 'Chi',
        'move_type': 'Coaching Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 9.5,  # NFL's best offense (33.2 PPG), Goff developer
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,  # Irreplaceable offensive mind to division rival
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Aaron Glenn',
        'position': 'DC',
        'from_team': 'Det',
        'to_team': 'NYJ',
        'move_type': 'Coaching Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.5,  # Navigated 16 defensive players on IR
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.0,  # Both coordinators lost simultaneously
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Carlton Davis III',
        'position': 'CB1',
        'from_team': 'Det',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Solid corner play in championship run
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting corner
        'importance_to_old_team': 7.5,  # Replaced by D.J. Reed
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Za\'Darius Smith',
        'position': 'EDGE',
        'from_team': 'Det',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 4 sacks in 8 games after trade
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Productive half-season
        'importance_to_old_team': 6.5,  # $11M saved over 2 years despite production
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kevin Zeitler',
        'position': 'RG',
        'from_team': 'Det',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # 86.5 PFF grade, elite guard play
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Starting right guard
        'importance_to_old_team': 7.5,  # Quality guard lost to market
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Ifeatu Melifonwu',
        'position': 'S',
        'from_team': 'Det',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Solid safety depth
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,  # Rotational safety
        'importance_to_old_team': 6.5,  # Safety depth lost
        'importance_to_new_team': 0.0,
    },

    # LIONS 2025 NFL DRAFT - Criticized but potentially brilliant
    {
        'player_name': 'Tyleik Williams',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #29',
        'contract_years': 4,
        'contract_value': 16200000,
        '2024_grade': 0.0,  # College - Ohio State (88.6 PFF run defense, limited pass rush)
        'projected_2025_grade': 7.5,  # Elite run stopping, depth behind McNeal
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Defensive line depth critical
    },
    {
        'player_name': 'Tate Ratledge',
        'position': 'RG',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #48',
        'contract_years': 4,
        'contract_value': 11400000,
        '2024_grade': 0.0,  # College - Georgia ("dirtbag mentality", 2 career sacks allowed)
        'projected_2025_grade': 7.8,  # Direct Zeitler replacement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starter potential
    },
    {
        'player_name': 'Isaac TeSlaa',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #70',
        'contract_years': 4,
        'contract_value': 7000000,
        '2024_grade': 0.0,  # College - Wyoming (Holmes' "favorite receiver in draft")
        'projected_2025_grade': 6.8,  # Development project with 6th round projections
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Traded 2 2026 3rds to get him
    },
    {
        'player_name': 'Donovan Kaufman',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #101',
        'contract_years': 4,
        'contract_value': 5600000,
        '2024_grade': 0.0,  # College - Wyoming (safety depth)
        'projected_2025_grade': 6.5,  # Developmental safety
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Safety depth after Melifonwu loss
    },
    {
        'player_name': 'Ahmed Hassanein',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #188',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - Boise State (first Egyptian player drafted, 22 sacks despite torn labrum)
        'projected_2025_grade': 6.8,  # Historic selection, pass rush upside
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Za'Darius Smith replacement depth
    },
    {
        'player_name': 'Connor Colby',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #214',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Iowa State (tight end depth)
        'projected_2025_grade': 6.2,  # Developmental tight end
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # TE room depth
    },
    {
        'player_name': 'Isaiah Cross',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Det',
        'move_type': '2025 Draft Pick #238',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Utah (receiver depth)
        'projected_2025_grade': 6.0,  # Late-round receiver project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # WR depth and special teams
    },

    # LIONS COACHING SUCCESSION - Internal promotions maintain continuity
    {
        'player_name': 'John Morton',
        'position': 'OC',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 8000000,
        '2024_grade': 8.0,  # Served under Johnson 2022, 23-year NFL veteran
        'projected_2025_grade': 8.5,  # "Not changing much" philosophy
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.5,  # Internal succession planning worked
        'importance_to_new_team': 8.5,  # System continuity preserved
    },
    {
        'player_name': 'Kelvin Sheppard',
        'position': 'DC',
        'from_team': 'Det',
        'to_team': 'Det',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 6000000,
        '2024_grade': 7.5,  # Glenn specifically mentored for this role
        'projected_2025_grade': 8.0,  # Pure succession planning execution
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Defensive continuity maintained
        'importance_to_new_team': 8.0,  # System knowledge preserved
    },
    {
        'player_name': 'David Shaw',
        'position': 'PASS_COORD',
        'from_team': 'Stanford',
        'to_team': 'Det',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 3000000,
        '2024_grade': 7.0,  # Former Stanford HC, offensive mind
        'projected_2025_grade': 7.5,  # Passing game coordinator expertise
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Stanford program departure
        'importance_to_new_team': 7.5,  # Strategic hire for passing concepts
    },
]

# LIONS SUMMARY METRICS
LIONS_2025_SUMMARY = {
    'total_moves': len(LIONS_2025_MOVES),
    'free_agent_signings': 3,
    'major_losses': 6,
    'trades': 0,
    'draft_picks': 7,
    'key_resignings': 4,
    'coaching_changes': 3,
    'total_guaranteed_money': 332000000,  # Historic core extensions
    'salary_cap_space_remaining': 40200000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B+',
    'key_philosophy': 'Maintain championship core despite coordinator exodus through succession planning',
    'biggest_concern': '2026 cap crunch ($69.6M Goff, $33.1M St. Brown) and coordinator losses',
    'biggest_strength': 'Elite young core locked up (Sewell 24, Gibbs 23, LaPorta 23, Branch 22)',
    'succession_success': 'Morton and Sheppard promotions preserve system continuity',
    'draft_criticism': 'Worst consensus grades since 2019 but mirrors 2023 success pattern',
    'financial_reality': '$40M under to potentially $40M over in 2026',
    'betting_implication': 'Top-5 Super Bowl odds (+1000) despite coordinator turnover'
}

if __name__ == "__main__":
    print(f"Detroit Lions 2025 Offseason Moves: {LIONS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {LIONS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {LIONS_2025_SUMMARY['championship_window']}")
    print(f"Total Guaranteed Money: ${LIONS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {LIONS_2025_SUMMARY['key_philosophy']}")
    print(f"Succession Success: {LIONS_2025_SUMMARY['succession_success']}")
    print(f"Financial Reality: {LIONS_2025_SUMMARY['financial_reality']}")
    print(f"Draft Criticism: {LIONS_2025_SUMMARY['draft_criticism']}")
    print(f"Betting Implication: {LIONS_2025_SUMMARY['betting_implication']}")
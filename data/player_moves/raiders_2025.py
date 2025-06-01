"""
Las Vegas Raiders 2025 Offseason Moves
Complete organizational overhaul under Carroll-Brady partnership
"""

RAIDERS_2025_MOVES = [
    # RAIDERS MAJOR TRADE AND SIGNING - Quarterback solution
    {
        'player_name': 'Geno Smith',
        'position': 'QB',
        'from_team': 'Sea',
        'to_team': 'LV',
        'move_type': 'Trade + Extension',
        'contract_years': 2,
        'contract_value': 85500000,
        '2024_grade': 8.0,  # 70.4% completion, 4,320 yards, 2 Pro Bowls under Carroll
        'projected_2025_grade': 8.2,  # Carroll reunion, immediate stability
        'snap_percentage_2024': 95.0,  # Starting QB
        'importance_to_old_team': 8.5,  # Franchise QB for Seahawks
        'importance_to_new_team': 10.0,  # Solves 7-starter QB carousel
    },
    
    # RAIDERS FREE AGENT SIGNINGS - Targeted improvements
    {
        'player_name': 'Jeremy Chinn',
        'position': 'S',
        'from_team': 'Was',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 16000000,
        '2024_grade': 8.0,  # 117 tackles, excellent playoff performance
        'projected_2025_grade': 7.8,  # Elite safety production
        'snap_percentage_2024': 94.0,  # 1,021 total snaps
        'importance_to_old_team': 8.0,  # Key defensive communicator
        'importance_to_new_team': 8.5,  # Replaces Tre'von Moehrig
    },
    {
        'player_name': 'Elandon Roberts',
        'position': 'LB',
        'from_team': 'Pit',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3010000,
        '2024_grade': 7.0,  # Championship experience, veteran leadership
        'projected_2025_grade': 7.2,  # Solid contributor
        'snap_percentage_2024': 60.0,  # Rotational role
        'importance_to_old_team': 6.5,  # Depth piece
        'importance_to_new_team': 7.5,  # Replaces Robert Spillane
    },
    {
        'player_name': 'Eric Stokes',
        'position': 'CB2',
        'from_team': 'GB',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4000000,
        '2024_grade': 6.5,  # Former 1st round pick, starting experience
        'projected_2025_grade': 7.0,  # Bounce-back candidate
        'snap_percentage_2024': 70.0,  # Starting corner
        'importance_to_old_team': 6.5,  # Lost Nate Hobbs
        'importance_to_new_team': 7.5,  # CB depth after Hobbs departure
    },
    {
        'player_name': 'Devin White',
        'position': 'LB',
        'from_team': 'Phi',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5500000,
        '2024_grade': 6.8,  # Former All-Pro, reunites with Spytek
        'projected_2025_grade': 7.5,  # Spytek knows his potential
        'snap_percentage_2024': 65.0,  # Limited role with Eagles
        'importance_to_old_team': 6.0,  # Depth piece
        'importance_to_new_team': 8.0,  # Spytek drafted him in Tampa
    },
    {
        'player_name': 'Raheem Mostert',
        'position': 'RB',
        'from_team': 'Mia',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2100000,
        '2024_grade': 7.0,  # Pro Bowl production (18 TDs in 2023)
        'projected_2025_grade': 7.2,  # Veteran presence with Jeanty
        'snap_percentage_2024': 55.0,  # Split backfield
        'importance_to_old_team': 6.5,  # Dolphins released for cap
        'importance_to_new_team': 7.0,  # Veteran complement to Jeanty
    },
    {
        'player_name': 'Alex Cappa',
        'position': 'G',
        'from_team': 'Cin',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 11000000,
        '2024_grade': 7.2,  # Solid starter for Bengals
        'projected_2025_grade': 7.0,  # Interior line upgrade
        'snap_percentage_2024': 85.0,  # Starting RG
        'importance_to_old_team': 7.0,  # Lost to cap space
        'importance_to_new_team': 7.5,  # Solidifies interior line
    },
    {
        'player_name': 'Andre Cisco',
        'position': 'S',
        'from_team': 'NYJ',
        'to_team': 'LV',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3200000,
        '2024_grade': 6.8,  # Solid safety production
        'projected_2025_grade': 6.5,  # Depth safety
        'snap_percentage_2024': 60.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Jets signed elsewhere
        'importance_to_new_team': 6.5,  # Safety depth
    },

    # RAIDERS MAJOR LOSSES - Creating compensatory pick opportunities
    {
        'player_name': 'Tre\'von Moehrig',
        'position': 'S',
        'from_team': 'LV',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Starting safety, 2021 2nd round pick
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Primary safety
        'importance_to_old_team': 7.5,  # Young starting safety
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Robert Spillane',
        'position': 'LB',
        'from_team': 'LV',
        'to_team': 'NE',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Team leading 158 tackles
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Every-down linebacker
        'importance_to_old_team': 8.5,  # Leading tackler, defensive signal caller
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nate Hobbs',
        'position': 'CB2',
        'from_team': 'LV',
        'to_team': 'GB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Starting nickel corner
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Primary slot corner
        'importance_to_old_team': 7.5,  # Young starting corner
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Aidan O\'Connell',
        'position': 'QB',
        'from_team': 'LV',
        'to_team': 'RELEASED',
        'move_type': 'Cut',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Inconsistent play, 7-starter carousel
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,  # Part of QB carousel
        'importance_to_old_team': 5.0,  # Failed QB experiment
        'importance_to_new_team': 0.0,
    },

    # RAIDERS DRAFT PICKS - Elite talent and value accumulation
    {
        'player_name': 'Ashton Jeanty',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #6',
        'contract_years': 4,
        'contract_value': 38500000,
        '2024_grade': 0.0,  # College - 2,601 yards (2nd most in FBS history), 29 TDs
        'projected_2025_grade': 8.5,  # Generational RB talent, 185.8 YPG
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Addresses NFL-worst rushing (79.8 YPG)
    },
    {
        'player_name': 'Jack Bech',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #42',
        'contract_years': 4,
        'contract_value': 12800000,
        '2024_grade': 0.0,  # College - 1,034 receiving yards at TCU
        'projected_2025_grade': 7.0,  # Big-bodied receiver
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Weapons for Geno Smith
    },
    {
        'player_name': 'Darien Porter',
        'position': 'CB1',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #65',
        'contract_years': 4,
        'contract_value': 8200000,
        '2024_grade': 0.0,  # College - Elite speed (4.30 forty), 90.1 PFF coverage
        'projected_2025_grade': 7.2,  # Immediate impact corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Addresses coverage needs
    },
    {
        'player_name': 'Charles Grant',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #78',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - 48 career starts
        'projected_2025_grade': 6.5,  # OL depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Offensive line depth
    },
    {
        'player_name': 'Caleb Rogers',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #89',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - 48 career starts
        'projected_2025_grade': 6.5,  # Interior line depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Guard competition
    },
    {
        'player_name': 'Dont\'e Thornton Jr.',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'LV',
        'move_type': '2025 Draft Pick #115',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - 6\'5" speedster, 25.4 YPC
        'projected_2025_grade': 6.8,  # Deep threat potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Vertical element
    },

    # RAIDERS KEY EXTENSIONS - Franchise cornerstones
    {
        'player_name': 'Maxx Crosby',
        'position': 'EDGE',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 106500000,
        '2024_grade': 9.5,  # Elite pass rusher, defensive foundation
        'projected_2025_grade': 9.2,  # Highest-paid non-QB in history
        'snap_percentage_2024': 90.0,  # Every-down player
        'importance_to_old_team': 10.0,  # Franchise defensive cornerstone
        'importance_to_new_team': 10.0,  # $91.5M guaranteed commitment
    },
    {
        'player_name': 'Malcolm Koonce',
        'position': 'EDGE',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 12000000,
        '2024_grade': 6.5,  # ACL recovery, prove-it deal
        'projected_2025_grade': 7.5,  # Healthy return potential
        'snap_percentage_2024': 30.0,  # Injury-limited
        'importance_to_old_team': 7.0,  # Pass rush depth
        'importance_to_new_team': 7.5,  # Crosby's running mate
    },
    {
        'player_name': 'Adam Butler',
        'position': 'DT',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 16500000,
        '2024_grade': 7.5,  # 10 sacks over two seasons
        'projected_2025_grade': 7.2,  # Consistent producer
        'snap_percentage_2024': 65.0,  # Rotational DT
        'importance_to_old_team': 7.5,  # Interior pass rush
        'importance_to_new_team': 7.5,  # $11M guaranteed shows value
    },
    {
        'player_name': 'Isaiah Pola-Mao',
        'position': 'S',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 8450000,
        '2024_grade': 7.0,  # 85 tackles, emerging safety
        'projected_2025_grade': 7.2,  # Young player development
        'snap_percentage_2024': 70.0,  # Starting safety
        'importance_to_old_team': 7.0,  # Young talent
        'importance_to_new_team': 7.0,  # Safety tandem with Chinn
    },
    {
        'player_name': 'AJ Cole',
        'position': 'P',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 15800000,
        '2024_grade': 8.0,  # Elite punter
        'projected_2025_grade': 8.0,  # NFL's highest-paid punter
        'snap_percentage_2024': 100.0,  # Punter
        'importance_to_old_team': 7.0,  # Special teams excellence
        'importance_to_new_team': 7.0,  # Field position weapon
    },

    # RAIDERS COACHING OVERHAUL - Championship pedigree
    {
        'player_name': 'Pete Carroll',
        'position': 'HC',
        'from_team': 'RETIRED',
        'to_team': 'LV',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 25000000,
        '2024_grade': 0.0,  # One year removed from Seattle
        'projected_2025_grade': 9.0,  # Super Bowl champion, "Always Compete"
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Complete culture transformation
    },
    {
        'player_name': 'Chip Kelly',
        'position': 'OC',
        'from_team': 'UCLA',
        'to_team': 'LV',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 8000000,
        '2024_grade': 0.0,  # College coordinator
        'projected_2025_grade': 8.0,  # Innovative offensive mind
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Perfect for Bowers/Jeanty
    },
    {
        'player_name': 'Patrick Graham',
        'position': 'DC',
        'from_team': 'LV',
        'to_team': 'LV',
        'move_type': 'Coaching Retention',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 7.0,  # Fourth season, defensive continuity
        'projected_2025_grade': 7.5,  # Knows personnel
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,  # Defensive stability
        'importance_to_new_team': 7.5,  # Scheme continuity
    },
    {
        'player_name': 'Brennan Carroll',
        'position': 'RB_COACH',
        'from_team': 'SEATTLE',
        'to_team': 'LV',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 2500000,
        '2024_grade': 7.5,  # Pete Carroll's son, run game coordinator
        'projected_2025_grade': 8.0,  # Perfect for Jeanty development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Carroll family continuity
        'importance_to_new_team': 8.5,  # Critical for Jeanty's development
    },

    # RAIDERS FRONT OFFICE CHANGES
    {
        'player_name': 'John Spytek',
        'position': 'GM',
        'from_team': 'TB',
        'to_team': 'LV',
        'move_type': 'Front Office Hire',
        'contract_years': 4,
        'contract_value': 12000000,
        '2024_grade': 8.5,  # 9 seasons Tampa Bay, Super Bowl experience
        'projected_2025_grade': 8.5,  # "Intelligently aggressive" approach
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 8.0,  # Tampa Bay loss
        'importance_to_new_team': 9.5,  # Complete front office overhaul
    },
]

# RAIDERS SUMMARY METRICS
RAIDERS_2025_SUMMARY = {
    'total_moves': len(RAIDERS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 4,
    'draft_picks': 6,
    'key_extensions': 5,
    'coaching_overhaul': 4,
    'front_office_changes': 1,
    'total_guaranteed_money': 200000000,  # Major investment in guaranteed money
    'geno_smith_trade_cost': 3000000,  # 2025 3rd round pick (#92)
    'salary_cap_space_remaining': 36160000,  # Significant flexibility
    'projected_2026_cap_space': 94990000,  # Future flexibility
    'projected_2027_cap_space': 142690000,  # Massive future space
    'championship_window': '2026-2029',  # After foundation building
    'offseason_grade': 'B+',
    'key_philosophy': 'Foundation establishment through proven winners',
    'afc_west_position': 'Fourth',  # Behind Chiefs, Chargers, Broncos
    'over_under_wins': 6.5,
    'playoff_odds': 'Minimal',
    'power_ranking_consensus': '25th-28th',
    'tom_brady_influence': 'Significant',  # Minority ownership driving decisions
    'pete_carroll_contract': '3 years + 4th year option',
    'compensatory_picks_projected': 3,  # 2026-2027 drafts
    'rushing_offense_2024': 'Dead last (79.8 YPG)',
    'coverage_grade_2024': 'League-worst (32.0 PFF)',
}

if __name__ == "__main__":
    print(f"Las Vegas Raiders 2025 Offseason Moves: {RAIDERS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {RAIDERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {RAIDERS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${RAIDERS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Projected 2026 Cap Space: ${RAIDERS_2025_SUMMARY['projected_2026_cap_space']:,}")
    print(f"Projected 2027 Cap Space: ${RAIDERS_2025_SUMMARY['projected_2027_cap_space']:,}")
    print(f"Philosophy: {RAIDERS_2025_SUMMARY['key_philosophy']}")
    print(f"Over/Under Wins: {RAIDERS_2025_SUMMARY['over_under_wins']}")
    print(f"Tom Brady Influence: {RAIDERS_2025_SUMMARY['tom_brady_influence']}")
    print(f"Pete Carroll Contract: {RAIDERS_2025_SUMMARY['pete_carroll_contract']}")
"""
Kansas City Chiefs 2025 Offseason Moves
Complete analysis of cap-constrained championship core maintenance under Brett Veach and Andy Reid
"""

CHIEFS_2025_MOVES = [
    # CHIEFS FREE AGENT SIGNINGS - Targeted precision amid constraints
    {
        'player_name': 'Jaylon Moore',
        'position': 'LT',
        'from_team': 'SF',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 30000000,
        '2024_grade': 6.8,  # Limited starts but Shanahan system experience
        'projected_2025_grade': 7.2,  # Reid system fit hoped
        'snap_percentage_2024': 45.0,  # Only 12 career starts
        'importance_to_old_team': 6.0,  # Depth tackle for 49ers
        'importance_to_new_team': 8.5,  # Critical LT need addressed
    },
    {
        'player_name': 'Kristian Fulton',
        'position': 'CB1',
        'from_team': 'LAC',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 7.2,  # 15th among corners with 750+ snaps
        'projected_2025_grade': 7.5,  # Allows McDuffie to slot
        'snap_percentage_2024': 75.0,  # Starter when healthy
        'importance_to_old_team': 7.0,  # Key Chargers corner
        'importance_to_new_team': 8.0,  # Secondary upgrade
    },
    {
        'player_name': 'Gardner Minshew',
        'position': 'QB',
        'from_team': 'LV',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1170000,
        '2024_grade': 6.8,  # 46 career starts, 9-5 record
        'projected_2025_grade': 7.0,  # Reliable backup
        'snap_percentage_2024': 65.0,  # Raiders starter portions
        'importance_to_old_team': 7.5,  # Starting QB for Raiders
        'importance_to_new_team': 7.0,  # Mahomes insurance
    },
    {
        'player_name': 'Elijah Mitchell',
        'position': 'RB',
        'from_team': 'SF',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 0.0,  # Missed all of 2024 with hamstring
        'projected_2025_grade': 6.5,  # Speed element (4.38 forty)
        'snap_percentage_2024': 0.0,  # Injured reserve all season
        'importance_to_old_team': 5.0,  # Injury-prone depth
        'importance_to_new_team': 6.5,  # Speed complement to Hunt
    },
    {
        'player_name': 'Jerry Tillery',
        'position': 'DT',
        'from_team': 'NE',
        'to_team': 'KC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1790000,
        '2024_grade': 6.0,  # Former first-round pick depth
        'projected_2025_grade': 6.3,  # Versatile DT depth
        'snap_percentage_2024': 55.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Patriots depth piece
        'importance_to_new_team': 6.5,  # Spagnuolo scheme fit
    },

    # CHIEFS KEY RE-SIGNINGS - Core retention amid constraints
    {
        'player_name': 'Nick Bolton',
        'position': 'LB',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 45000000,
        '2024_grade': 8.5,  # Led team with 106 tackles, defensive QB
        'projected_2025_grade': 8.7,  # Spagnuolo's defensive leader
        'snap_percentage_2024': 90.0,  # 559 career tackles
        'importance_to_old_team': 9.0,  # Defensive quarterback
        'importance_to_new_team': 9.0,  # 4th highest-paid LB in NFL
    },
    {
        'player_name': 'Trey Smith',
        'position': 'RG',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Franchise Tag',
        'contract_years': 1,
        'contract_value': 23400000,
        '2024_grade': 8.8,  # Pro Bowl guard, 6th round gem
        'projected_2025_grade': 8.8,  # Elite interior protection
        'snap_percentage_2024': 95.0,  # Anchor of offensive line
        'importance_to_old_team': 9.5,  # Critical pass protection
        'importance_to_new_team': 9.5,  # Highest-paid guard in history
    },
    {
        'player_name': 'Marquise Brown',
        'position': 'WR2',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 11000000,
        '2024_grade': 5.5,  # Injury-plagued 2024 season
        'projected_2025_grade': 7.0,  # Second chance for speed
        'snap_percentage_2024': 25.0,  # Limited by injuries
        'importance_to_old_team': 6.0,  # Injured depth piece
        'importance_to_new_team': 7.5,  # Speed element return
    },
    {
        'player_name': 'Kareem Hunt',
        'position': 'RB',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 7.8,  # 728 yards, 7 TDs in 13 games
        'projected_2025_grade': 7.5,  # Proven veteran back
        'snap_percentage_2024': 70.0,  # Key contributor post-return
        'importance_to_old_team': 8.0,  # Reliable rushing option
        'importance_to_new_team': 8.0,  # Team-friendly value
    },
    {
        'player_name': 'JuJu Smith-Schuster',
        'position': 'WR3',
        'from_team': 'KC',
        'to_team': 'KC',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.8,  # Reliable intermediate target
        'projected_2025_grade': 7.0,  # Mahomes chemistry
        'snap_percentage_2024': 60.0,  # Slot role contributor
        'importance_to_old_team': 7.0,  # Proven Mahomes target
        'importance_to_new_team': 7.0,  # Continuity at value
    },

    # CHIEFS MAJOR LOSSES - Cap casualties and departed talent
    {
        'player_name': 'Justin Reid',
        'position': 'S',
        'from_team': 'KC',
        'to_team': 'NO',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.0,  # 3,575 defensive snaps since 2022
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Defensive signal-caller
        'importance_to_old_team': 8.5,  # Safety leader and emergency kicker
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Allegretti',
        'position': 'G',
        'from_team': 'KC',
        'to_team': 'Was',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Started AFC Championship and Super Bowl
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Key injury replacement
        'importance_to_old_team': 7.5,  # Valuable swing lineman
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Derrick Nnadi',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # 221 defensive snaps, diminished role
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,  # Limited 2024 role
        'importance_to_old_team': 6.5,  # 7-year veteran, 3 Super Bowls
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Tommy Townsend',
        'position': 'P',
        'from_team': 'KC',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Reliable punter for Chiefs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # All punting duties
        'importance_to_old_team': 7.0,  # Special teams consistency
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Tershawn Wharton',
        'position': 'DT',
        'from_team': 'KC',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Versatile defensive lineman
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Rotational contributor
        'importance_to_old_team': 7.0,  # Young defensive line depth
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'D.J. Humphries',
        'position': 'LT',
        'from_team': 'KC',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Brief stint with Chiefs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,  # Limited role
        'importance_to_old_team': 5.5,  # Short-term depth
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'DeAndre Hopkins',
        'position': 'WR1',
        'from_team': 'KC',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # 41 catches, 437 yards, 4 TDs in 10 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 58.0,  # Mid-season rental
        'importance_to_old_team': 7.0,  # Playoff depth receiver
        'importance_to_new_team': 0.0,
    },

    # CHIEFS TRADES - Major cap management moves
    {
        'player_name': 'L\'Jarius Sneed',
        'position': 'CB1',
        'from_team': 'KC',
        'to_team': 'Ten',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.5,  # All-Pro corner, signed $76.4M with Titans
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Elite coverage corner
        'importance_to_old_team': 9.0,  # $19.8M cap savings forced trade
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Joe Thuney',
        'position': 'LG',
        'from_team': 'KC',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.8,  # All-Pro guard protecting Mahomes
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,  # Elite pass protection
        'importance_to_old_team': 9.5,  # $16M savings despite $11M dead money
        'importance_to_new_team': 0.0,
    },

    # CHIEFS 2025 NFL DRAFT - Long-term building blocks
    {
        'player_name': 'Josh Simmons',
        'position': 'LT',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #32',
        'contract_years': 4,
        'contract_value': 15200000,
        '2024_grade': 0.0,  # College - 6'5", 310 lbs, torn patellar tendon
        'projected_2025_grade': 7.5,  # Future franchise LT if healthy
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Critical LT need addressed
    },
    {
        'player_name': 'Omarr Norman-Lott',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #63',
        'contract_years': 4,
        'contract_value': 8100000,
        '2024_grade': 0.0,  # College - Undersized but disruptive (4.5 sacks)
        'projected_2025_grade': 6.8,  # Interior pass rush depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces Nnadi/Wharton
    },
    {
        'player_name': 'Ashton Gillotte',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #66',
        'contract_years': 4,
        'contract_value': 7800000,
        '2024_grade': 0.0,  # College - 26.5 career sacks at Louisville
        'projected_2025_grade': 7.0,  # Edge depth behind Karlaftis
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Pass rush rotation
    },
    {
        'player_name': 'Nohl Williams',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #85',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - Led nation with 7 INTs
        'projected_2025_grade': 6.8,  # Physical corner fits Spagnuolo
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Secondary depth post-Sneed
    },
    {
        'player_name': 'Jalen Royals',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #133',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - Versatile inside/outside, return skills
        'projected_2025_grade': 6.5,  # Receiver depth and special teams
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # WR corps depth
    },
    {
        'player_name': 'Jeffrey Bassa',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #156',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - Safety to LB transition
        'projected_2025_grade': 6.0,  # Coverage LB and special teams
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Special teams upgrade
    },
    {
        'player_name': 'Brashard Smith',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'KC',
        'move_type': '2025 Draft Pick #228',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Dynamic pass-catching back
        'projected_2025_grade': 6.2,  # Versatile backfield option
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Backfield depth
    },

    # CHIEFS COACHING CHANGES - Stability with strategic additions
    {
        'player_name': 'Matt House',
        'position': 'DEF_ASST',
        'from_team': 'Jac',
        'to_team': 'KC',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 2000000,
        '2024_grade': 7.5,  # Super Bowl LIV championship experience
        'projected_2025_grade': 8.0,  # Defensive reinforcement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Jacksonville loss
        'importance_to_new_team': 7.5,  # Championship pedigree return
    },
    {
        'player_name': 'Chris Orr',
        'position': 'DEF_QC',
        'from_team': 'JSU',
        'to_team': 'KC',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 800000,
        '2024_grade': 6.5,  # Young coach, recent playing experience
        'projected_2025_grade': 7.0,  # Fresh perspective
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,  # Jackson State departure
        'importance_to_new_team': 6.5,  # Young talent development
    },
]

# CHIEFS SUMMARY METRICS
CHIEFS_2025_SUMMARY = {
    'total_moves': len(CHIEFS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 7,
    'trades': 2,
    'draft_picks': 7,
    'key_resignings': 5,
    'coaching_changes': 2,
    'total_guaranteed_money': 85000000,  # Conservative estimate
    'salary_cap_space_remaining': 8000000,
    'championship_window': '2025-2027',
    'offseason_grade': 'B-',
    'key_philosophy': 'Cap-constrained core maintenance with strategic additions',
    'biggest_concern': 'Offensive line protection after Thuney trade',
    'biggest_strength': 'Mahomes still elite with Reid system continuity'
}

if __name__ == "__main__":
    print(f"Kansas City Chiefs 2025 Offseason Moves: {CHIEFS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {CHIEFS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {CHIEFS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${CHIEFS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {CHIEFS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {CHIEFS_2025_SUMMARY['biggest_concern']}")
"""
Los Angeles Chargers 2025 Offseason Moves
Complete analysis of draft-centric Chiefs challenger strategy under Jim Harbaugh and Joe Hortiz
"""

CHARGERS_2025_MOVES = [
    # CHARGERS FREE AGENT SIGNINGS - Calculated additions for Herbert
    {
        'player_name': 'Mekhi Becton',
        'position': 'LG',
        'from_team': 'Phi',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 8.0,  # Super Bowl champion, helped Barkley to 2,000+ yards
        'projected_2025_grade': 8.2,  # Elite interior protection
        'snap_percentage_2024': 85.0,  # Eagles starter
        'importance_to_old_team': 7.5,  # Key Eagles guard
        'importance_to_new_team': 8.5,  # Biggest interior line weakness addressed
    },
    {
        'player_name': 'Najee Harris',
        'position': 'RB',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 9250000,
        '2024_grade': 7.8,  # 77.9 PFF grade, ranked 14th among RBs
        'projected_2025_grade': 8.0,  # 1,000+ yards 4 straight seasons
        'snap_percentage_2024': 75.0,  # Steelers workhorse
        'importance_to_old_team': 8.0,  # 4-year starter for Pittsburgh
        'importance_to_new_team': 8.5,  # Harbaugh ground-and-pound centerpiece
    },
    {
        'player_name': 'Mike Williams',
        'position': 'WR1',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 6000000,
        '2024_grade': 6.0,  # Disappointing Pittsburgh stint
        'projected_2025_grade': 7.5,  # Reunion with Herbert
        'snap_percentage_2024': 55.0,  # Limited role with Steelers
        'importance_to_old_team': 5.5,  # Depth piece for Pittsburgh
        'importance_to_new_team': 8.0,  # Brings back size and physicality
    },
    {
        'player_name': 'Donte Jackson',
        'position': 'CB2',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 13000000,
        '2024_grade': 6.8,  # Career-high 5 INTs despite 49.4 PFF grade
        'projected_2025_grade': 7.0,  # Cornerback depth
        'snap_percentage_2024': 70.0,  # Steelers starter
        'importance_to_old_team': 7.0,  # Starting corner for Pittsburgh
        'importance_to_new_team': 7.5,  # CB depth and experience
    },
    {
        'player_name': 'Tyler Conklin',
        'position': 'TE',
        'from_team': 'NYJ',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 6.8,  # 51 catches, 449 yards with Jets
        'projected_2025_grade': 7.0,  # Reliable hands
        'snap_percentage_2024': 65.0,  # Jets starter
        'importance_to_old_team': 7.0,  # Key Jets receiving target
        'importance_to_new_team': 7.0,  # Replaces Stone Smartt
    },
    {
        'player_name': 'Andre James',
        'position': 'C',
        'from_team': 'LV',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.5,  # Division rival center
        'projected_2025_grade': 6.8,  # Interior line depth
        'snap_percentage_2024': 80.0,  # Raiders starter
        'importance_to_old_team': 7.0,  # Starting center for Las Vegas
        'importance_to_new_team': 6.5,  # Center competition/depth
    },
    {
        'player_name': 'Da\'Shawn Hand',
        'position': 'DT',
        'from_team': 'Mia',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3350000,
        '2024_grade': 6.0,  # 563 snaps on Dolphins DL
        'projected_2025_grade': 6.3,  # Defensive line depth
        'snap_percentage_2024': 50.0,  # Rotational role
        'importance_to_old_team': 6.0,  # Miami depth piece
        'importance_to_new_team': 6.5,  # Helps offset Poona Ford loss
    },
    {
        'player_name': 'Naquan Jones',
        'position': 'DT',
        'from_team': 'Ten',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 6.0,  # Titans defensive tackle depth
        'projected_2025_grade': 6.2,  # Interior defensive line depth
        'snap_percentage_2024': 40.0,  # Limited role
        'importance_to_old_team': 5.5,  # Tennessee depth
        'importance_to_new_team': 6.0,  # DT rotation help
    },
    {
        'player_name': 'Benjamin St-Juste',
        'position': 'CB2',
        'from_team': 'Was',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.2,  # 6'3" size, started 14 games for Washington
        'projected_2025_grade': 6.5,  # Cornerback depth
        'snap_percentage_2024': 75.0,  # Commanders starter
        'importance_to_old_team': 6.5,  # Washington starter
        'importance_to_new_team': 6.5,  # CB depth and size
    },
    {
        'player_name': 'Del\'Shawn Phillips',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'LAC',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,  # Special teams expertise from Baltimore
        'projected_2025_grade': 6.2,  # Special teams ace
        'snap_percentage_2024': 30.0,  # Limited defensive role
        'importance_to_old_team': 6.0,  # Ravens special teams
        'importance_to_new_team': 6.0,  # Reunites with GM Hortiz
    },

    # CHARGERS KEY RE-SIGNINGS - Core retention with value extensions
    {
        'player_name': 'Khalil Mack',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 1,
        'contract_value': 18000000,
        '2024_grade': 8.8,  # 23 sacks over past two seasons
        'projected_2025_grade': 8.5,  # Future Hall of Famer
        'snap_percentage_2024': 85.0,  # Key pass rusher
        'importance_to_old_team': 9.5,  # Defensive cornerstone
        'importance_to_new_team': 9.5,  # Fully guaranteed, veteran leadership
    },
    {
        'player_name': 'Elijah Molden',
        'position': 'S',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 18750000,
        '2024_grade': 7.5,  # Versatile DB, acquired via 2024 trade
        'projected_2025_grade': 7.8,  # Safety/nickel flexibility
        'snap_percentage_2024': 70.0,  # Multi-position contributor
        'importance_to_old_team': 8.0,  # Key defensive back
        'importance_to_new_team': 8.0,  # Depth behind Derwin James
    },
    {
        'player_name': 'Bradley Bozeman',
        'position': 'C',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 7.2,  # Reliable center
        'projected_2025_grade': 7.0,  # May see competition from Zion Johnson
        'snap_percentage_2024': 90.0,  # Starting center
        'importance_to_old_team': 7.5,  # Interior line anchor
        'importance_to_new_team': 7.5,  # Continuity despite uncertainty
    },
    {
        'player_name': 'Cameron Dicker',
        'position': 'K',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 22040000,
        '2024_grade': 9.0,  # 94.5% career FG rate, NFL's most accurate
        'projected_2025_grade': 9.0,  # Elite kicker
        'snap_percentage_2024': 100.0,  # All kicking duties
        'importance_to_old_team': 9.0,  # Special teams excellence
        'importance_to_new_team': 9.0,  # Locked up through 2028
    },
    {
        'player_name': 'J.K. Scott',
        'position': 'P',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 8500000,
        '2024_grade': 7.5,  # 46.7 yards per punt average
        'projected_2025_grade': 7.5,  # Reliable punter
        'snap_percentage_2024': 100.0,  # All punting duties
        'importance_to_old_team': 7.5,  # Special teams consistency
        'importance_to_new_team': 7.5,  # Special teams continuity
    },
    {
        'player_name': 'Teair Tart',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 6000000,
        '2024_grade': 6.8,  # Defensive tackle depth
        'projected_2025_grade': 7.0,  # Interior rotation
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 6.5,  # Depth piece
        'importance_to_new_team': 6.5,  # Defensive line continuity
    },
    {
        'player_name': 'Troy Dye',
        'position': 'LB',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 5500000,
        '2024_grade': 7.0,  # Special teams excellence
        'projected_2025_grade': 7.0,  # Linebacker depth and special teams
        'snap_percentage_2024': 40.0,  # Limited defensive snaps
        'importance_to_old_team': 7.0,  # Special teams ace
        'importance_to_new_team': 7.0,  # Special teams leadership
    },
    {
        'player_name': 'Denzel Perryman',
        'position': 'LB',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 5000000,
        '2024_grade': 7.2,  # Veteran linebacker
        'projected_2025_grade': 7.0,  # LB depth and leadership
        'snap_percentage_2024': 60.0,  # Rotational linebacker
        'importance_to_old_team': 7.0,  # Veteran presence
        'importance_to_new_team': 7.0,  # Leadership and depth
    },
    {
        'player_name': 'Jalen Reagor',
        'position': 'WR3',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 6.0,  # Depth receiver and return specialist
        'projected_2025_grade': 6.2,  # Special teams value
        'snap_percentage_2024': 35.0,  # Limited offensive role
        'importance_to_old_team': 6.0,  # Special teams contributor
        'importance_to_new_team': 6.0,  # Return game and depth
    },

    # CHARGERS MAJOR LOSSES - Strategic cap management departures
    {
        'player_name': 'Joey Bosa',
        'position': 'EDGE',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 5 sacks in 14 games, injury history
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # When healthy, effective
        'importance_to_old_team': 8.5,  # Franchise icon, 72 career sacks
        'importance_to_new_team': 0.0,  # $25.36M cap savings
    },
    {
        'player_name': 'Poona Ford',
        'position': 'DT',
        'from_team': 'LAC',
        'to_team': 'LAR',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.2,  # 92.6 PFF run defense grade, crucial to #1 defense
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Key defensive tackle
        'importance_to_old_team': 8.5,  # Critical run stopper lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Joshua Palmer',
        'position': 'WR2',
        'from_team': 'LAC',
        'to_team': 'Buf',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # 39 catches, 584 yards, solid depth
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Depth receiver
        'importance_to_old_team': 6.5,  # Reliable depth option
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Stone Smartt',
        'position': 'TE',
        'from_team': 'LAC',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Fan favorite, stepped up during injuries
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Limited role but effective
        'importance_to_old_team': 6.0,  # Depth tight end
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Niemann',
        'position': 'LB',
        'from_team': 'LAC',
        'to_team': 'Hou',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Special teams value
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,  # Limited defensive role
        'importance_to_old_team': 6.0,  # Special teams contributor
        'importance_to_new_team': 0.0,
    },

    # CHARGERS TRADES - Limited activity, focused on draft positioning
    {
        'player_name': 'Oronde Gadsden II',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': 'Draft Trade Up (5th Round)',
        'contract_years': 4,
        'contract_value': 4100000,
        '2024_grade': 0.0,  # College - 73 catches, 934 yards, 7 TDs at Syracuse
        'projected_2025_grade': 6.5,  # Seam-stretching TE
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Traded up picks 181, 209 for 165
    },

    # CHARGERS 2025 NFL DRAFT - Universally praised class
    {
        'player_name': 'Omarion Hampton',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #22',
        'contract_years': 4,
        'contract_value': 18500000,
        '2024_grade': 0.0,  # College - 3,164 yards over final two seasons
        'projected_2025_grade': 7.8,  # Harbaugh rushing attack centerpiece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Ground game transformation
    },
    {
        'player_name': 'Tre Harris',
        'position': 'WR1',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #55',
        'contract_years': 4,
        'contract_value': 9800000,
        '2024_grade': 0.0,  # College - 128.8 receiving yards per game when healthy
        'projected_2025_grade': 7.5,  # Vertical threat despite injury concerns
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Deep threat Herbert needs
    },
    {
        'player_name': 'Jamaree Caldwell',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #86',
        'contract_years': 4,
        'contract_value': 6800000,
        '2024_grade': 0.0,  # College - 340 lbs, 92.6 PFF run-defense grade
        'projected_2025_grade': 7.0,  # Poona Ford replacement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Run-stopping specialist
    },
    {
        'player_name': 'Kyle Kennard',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #125',
        'contract_years': 4,
        'contract_value': 5200000,
        '2024_grade': 0.0,  # College - Led SEC with 11.5 sacks
        'projected_2025_grade': 6.8,  # Edge depth post-Bosa
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Pass rush rotation
    },
    {
        'player_name': 'KeAndre Lambert-Smith',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #158',
        'contract_years': 4,
        'contract_value': 4400000,
        '2024_grade': 0.0,  # College - 4.37 speed (94th percentile)
        'projected_2025_grade': 6.5,  # Field-stretcher
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Speed element
    },
    {
        'player_name': 'Branson Taylor',
        'position': 'OG',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #188',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - 6'6", 330 lbs, season-ending knee injury
        'projected_2025_grade': 6.2,  # Interior line competition
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Guard depth
    },
    {
        'player_name': 'R.J. Mickens',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #214',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - PFF's 108th-ranked prospect
        'projected_2025_grade': 6.0,  # Safety depth value
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Exceptional value at pick 214
    },
    {
        'player_name': 'Trikweze Bridges',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'LAC',
        'move_type': '2025 Draft Pick #256',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Allowed zero TDs in coverage
        'projected_2025_grade': 6.0,  # Developmental cornerback
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Mr. Irrelevant value
    },

    # CHARGERS COACHING CHANGES - Continuity after successful season
    {
        'player_name': 'Dylan Roney',
        'position': 'EDGE_COACH',
        'from_team': 'LAC',
        'to_team': 'LAC',
        'move_type': 'Promotion',
        'contract_years': 3,
        'contract_value': 2000000,
        '2024_grade': 7.0,  # Followed Harbaugh from Michigan
        'projected_2025_grade': 7.5,  # Increased responsibility
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Continuity choice
        'importance_to_new_team': 7.5,  # Key to retaining Mack
    },
]

# CHARGERS SUMMARY METRICS
CHARGERS_2025_SUMMARY = {
    'total_moves': len(CHARGERS_2025_MOVES),
    'free_agent_signings': 10,
    'major_losses': 5,
    'trades': 1,
    'draft_picks': 9,
    'key_resignings': 9,
    'coaching_changes': 1,
    'total_guaranteed_money': 95000000,  # Conservative estimate
    'salary_cap_space_remaining': 26800000,
    'projected_2026_cap_space': 110800000,
    'championship_window': '2025-2028',
    'offseason_grade': 'B+',
    'key_philosophy': 'Draft-centric Chiefs challenger with sustainable building',
    'biggest_concern': 'Interior defensive line depth after Poona Ford loss',
    'biggest_strength': 'Maintained #1 scoring defense while upgrading offense'
}

if __name__ == "__main__":
    print(f"Los Angeles Chargers 2025 Offseason Moves: {CHARGERS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {CHARGERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {CHARGERS_2025_SUMMARY['championship_window']}")
    print(f"Current Cap Space: ${CHARGERS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"2026 Cap Space Projection: ${CHARGERS_2025_SUMMARY['projected_2026_cap_space']:,}")
    print(f"Philosophy: {CHARGERS_2025_SUMMARY['key_philosophy']}")
    print(f"Biggest Concern: {CHARGERS_2025_SUMMARY['biggest_concern']}")
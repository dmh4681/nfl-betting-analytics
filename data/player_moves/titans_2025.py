"""
Tennessee Titans 2025 Offseason Moves
Complete analysis of organizational reset under Mike Borgonzi and Brian Callahan
"""

TITANS_2025_MOVES = [
    # TITANS FREE AGENT SIGNINGS - Building around Cam Ward
    {
        'player_name': 'Dan Moore Jr.',
        'position': 'LT',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 4,
        'contract_value': 82000000,
        '2024_grade': 7.0,  # 92.5% pass block win rate
        'projected_2025_grade': 7.5,  # Protecting Ward's blindside
        'snap_percentage_2024': 95.0,  # Full-time starter in Pittsburgh
        'importance_to_old_team': 7.5,  # Reliable Steelers LT
        'importance_to_new_team': 9.5,  # Critical protection for rookie QB
    },
    {
        'player_name': 'Kevin Zeitler',
        'position': 'RG',
        'from_team': 'Det',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 8500000,
        '2024_grade': 7.8,  # Really good season with Lions at age 34
        'projected_2025_grade': 7.5,  # Veteran presence
        'snap_percentage_2024': 90.0,  # Full-time starter
        'importance_to_old_team': 7.0,  # Key Lions guard
        'importance_to_new_team': 8.0,  # Right guard stability
    },
    {
        'player_name': 'Lloyd Cushenberry III',
        'position': 'C',
        'from_team': 'Den',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 18000000,
        '2024_grade': 7.2,  # Solid center for Broncos
        'projected_2025_grade': 7.5,  # Interior line anchor
        'snap_percentage_2024': 95.0,  # Starting center
        'importance_to_old_team': 7.0,  # Broncos starter
        'importance_to_new_team': 8.5,  # Anchoring interior for Ward
    },
    {
        'player_name': 'Kyle Allen',
        'position': 'QB',
        'from_team': 'SF',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.5,  # 10 career starts, familiar with Callahan
        'projected_2025_grade': 6.5,  # Veteran backup
        'snap_percentage_2024': 20.0,  # Backup role with 49ers
        'importance_to_old_team': 5.0,  # 49ers backup
        'importance_to_new_team': 7.0,  # Reunites with Callahan from Bengals
    },
    {
        'player_name': 'Tim Boyle',
        'position': 'QB',
        'from_team': 'Mia',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 5.5,  # Veteran backup experience
        'projected_2025_grade': 5.8,  # QB room depth
        'snap_percentage_2024': 15.0,  # Limited action
        'importance_to_old_team': 4.0,  # Dolphins depth
        'importance_to_new_team': 5.5,  # QB competition
    },
    {
        'player_name': 'Jarran Reed',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        '2024_grade': 6.8,  # 13 QB hits, experienced DT
        'projected_2025_grade': 7.0,  # Defensive line depth
        'snap_percentage_2024': 65.0,  # Rotational starter
        'importance_to_old_team': 6.5,  # Seahawks DT depth
        'importance_to_new_team': 7.5,  # Defensive line upgrade
    },
    {
        'player_name': 'Sebastian Joseph-Day',
        'position': 'DT',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 7500000,
        '2024_grade': 6.5,  # 2.5 sacks, started 12 games
        'projected_2025_grade': 6.8,  # Continuity on defense
        'snap_percentage_2024': 70.0,  # Regular starter
        'importance_to_old_team': 7.0,  # Defensive consistency
        'importance_to_new_team': 7.0,  # Interior depth
    },
    {
        'player_name': 'Chidobe Awuzie',
        'position': 'CB2',
        'from_team': 'Dal',
        'to_team': 'Ten',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 4500000,
        '2024_grade': 6.8,  # 81 career starts, veteran experience
        'projected_2025_grade': 7.0,  # Secondary depth
        'snap_percentage_2024': 60.0,  # Injury-limited season
        'importance_to_old_team': 6.0,  # Cowboys depth
        'importance_to_new_team': 7.0,  # CB experience and depth
    },

    # TITANS MAJOR LOSSES - Era-ending departures
    {
        'player_name': 'Derrick Henry',
        'position': 'RB',
        'from_team': 'Ten',
        'to_team': 'Bal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 9.2,  # 1,921 rushing yards, 18 TDs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Workhorse back
        'importance_to_old_team': 10.0,  # Franchise icon, era officially over
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Ryan Tannehill',
        'position': 'QB',
        'from_team': 'Ten',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Veteran quarterback, injury-limited
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,  # Limited due to injury
        'importance_to_old_team': 7.5,  # Former franchise QB
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jeffery Simmons',
        'position': 'DT',
        'from_team': 'Ten',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 8.5,  # Elite defensive tackle
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Defensive anchor
        'importance_to_old_team': 9.5,  # Best defensive player
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Harold Landry III',
        'position': 'EDGE',
        'from_team': 'Ten',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Pass rush production
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Regular pass rusher
        'importance_to_old_team': 7.5,  # Key pass rusher released for cap
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Kenneth Murray Jr.',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'Hou',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # 95 tackles, 3.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,  # Starting linebacker
        'importance_to_old_team': 7.0,  # Linebacker production
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Westbrook-Ikhine',
        'position': 'WR2',
        'from_team': 'Ten',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Reliable receiver option
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Regular receiver
        'importance_to_old_team': 6.5,  # Receiver depth lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jerome Baker',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Starting linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Regular starter
        'importance_to_old_team': 7.0,  # LB production lost
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Mason Rudolph',
        'position': 'QB',
        'from_team': 'Ten',
        'to_team': 'Pit',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Backup/spot starter
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Split time with injured Tannehill
        'importance_to_old_team': 6.0,  # Veteran QB depth
        'importance_to_new_team': 0.0,
    },

    # TITANS 2025 NFL DRAFT - Cam Ward era begins
    {
        'player_name': 'Cam Ward',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #1',
        'contract_years': 4,
        'contract_value': 42000000,
        '2024_grade': 0.0,  # College - 4,313 passing yards, 39 TDs, 7 INTs
        'projected_2025_grade': 6.8,  # Rookie QB with upside
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Franchise quarterback
    },
    {
        'player_name': 'Oluwafemi Oladejo',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #52',
        'contract_years': 4,
        'contract_value': 11200000,
        '2024_grade': 0.0,  # College - 4.5 sacks, 13.5 TFL at UCLA
        'projected_2025_grade': 6.5,  # Developmental pass rusher
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replaces Landry pass rush
    },
    {
        'player_name': 'Kevin Winston Jr.',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #82',
        'contract_years': 4,
        'contract_value': 7400000,
        '2024_grade': 0.0,  # College - 90 tackles, 1 INT at Penn State
        'projected_2025_grade': 6.8,  # Three-year starter
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Secondary depth and potential
    },
    {
        'player_name': 'Braylon Braxton',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #118',
        'contract_years': 4,
        'contract_value': 5600000,
        '2024_grade': 0.0,  # College - Marshall quarterback
        'projected_2025_grade': 5.5,  # Developmental QB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Future QB depth
    },
    {
        'player_name': 'Kam Kinchens',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #154',
        'contract_years': 4,
        'contract_value': 5200000,
        '2024_grade': 0.0,  # College - Miami safety
        'projected_2025_grade': 6.0,  # Safety depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Secondary development
    },
    {
        'player_name': 'Dillon Johnson',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #189',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - Washington running back
        'projected_2025_grade': 6.2,  # Post-Henry era RB
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # RB depth after Henry departure
    },
    {
        'player_name': 'Marcus Ratcliffe',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #225',
        'contract_years': 4,
        'contract_value': 4400000,
        '2024_grade': 0.0,  # College - Oklahoma tackle
        'projected_2025_grade': 5.8,  # Developmental OL
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # OL depth development
    },
    {
        'player_name': 'Quinshon Judkins',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Ten',
        'move_type': '2025 Draft Pick #261',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - Ohio State transfer RB
        'projected_2025_grade': 6.5,  # Productive college back
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Lead back potential post-Henry
    },

    # TITANS KEY RE-SIGNINGS - Limited veteran retention
    {
        'player_name': 'Tony Pollard',
        'position': 'RB',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 16000000,
        '2024_grade': 7.0,  # 1,079 yards, reliable back
        'projected_2025_grade': 7.2,  # Lead back post-Henry
        'snap_percentage_2024': 75.0,  # Primary back in Dallas
        'importance_to_old_team': 8.0,  # Key offensive weapon
        'importance_to_new_team': 8.5,  # Post-Henry featured back
    },
    {
        'player_name': 'Calvin Ridley',
        'position': 'WR1',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 3,
        'contract_value': 69000000,
        '2024_grade': 7.8,  # Top receiving target
        'projected_2025_grade': 8.0,  # Ward's primary target
        'snap_percentage_2024': 90.0,  # Primary receiver
        'importance_to_old_team': 8.5,  # Top receiving threat
        'importance_to_new_team': 9.0,  # Critical for Ward's development
    },
    {
        'player_name': 'Will Levis',
        'position': 'QB',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 4500000,
        '2024_grade': 5.8,  # Inconsistent sophomore season
        'projected_2025_grade': 6.0,  # Competition for Ward
        'snap_percentage_2024': 60.0,  # Started 12 games
        'importance_to_old_team': 6.5,  # Former hopeful franchise QB
        'importance_to_new_team': 6.0,  # Bridge/competition option
    },
    {
        'player_name': 'L\'Jarius Sneed',
        'position': 'CB1',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 19500000,
        '2024_grade': 8.0,  # Elite cornerback
        'projected_2025_grade': 8.2,  # Defensive anchor
        'snap_percentage_2024': 95.0,  # Shutdown corner
        'importance_to_old_team': 9.0,  # Best defensive player
        'importance_to_new_team': 9.5,  # Defensive foundation
    },
    {
        'player_name': 'Peter Skoronski',
        'position': 'LG',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 12000000,
        '2024_grade': 7.0,  # 2023 1st round pick development
        'projected_2025_grade': 7.5,  # Sophomore growth
        'snap_percentage_2024': 85.0,  # Starting guard
        'importance_to_old_team': 7.5,  # Young OL core
        'importance_to_new_team': 8.0,  # Protecting Ward
    },
    {
        'player_name': 'JC Latham',
        'position': 'RT',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 8500000,
        '2024_grade': 6.8,  # Rookie tackle
        'projected_2025_grade': 7.5,  # Sophomore improvement
        'snap_percentage_2024': 90.0,  # Started every game as rookie
        'importance_to_old_team': 7.5,  # 2024 1st round pick
        'importance_to_new_team': 8.5,  # Moved to RT with Moore addition
    },

    # TITANS COACHING CHANGES - New GM, continuity at HC
    {
        'player_name': 'Mike Borgonzi',
        'position': 'GM',
        'from_team': 'KC',
        'to_team': 'Ten',
        'move_type': 'Front Office Hire',
        'contract_years': 5,
        'contract_value': 25000000,
        '2024_grade': 7.5,  # Chiefs assistant GM
        'projected_2025_grade': 8.0,  # Fresh perspective
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost key front office talent
        'importance_to_new_team': 9.0,  # Complete front office overhaul
    },
    {
        'player_name': 'Ran Carthon',
        'position': 'GM',
        'from_team': 'Ten',
        'to_team': 'FIRED',
        'move_type': 'Front Office Change',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # 3-14 season sealed his fate
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # Full GM control
        'importance_to_old_team': 8.0,  # GM fired after disaster season
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Nick Holz',
        'position': 'OC',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Coaching Retention',
        'contract_years': 2,
        'contract_value': 4000000,
        '2024_grade': 6.0,  # Offensive coordinator retained
        'projected_2025_grade': 7.0,  # Continuity for Ward
        'snap_percentage_2024': 100.0,  # Full offensive control
        'importance_to_old_team': 7.0,  # Offensive continuity
        'importance_to_new_team': 8.0,  # Key for Ward's development
    },
    {
        'player_name': 'Bill Callahan',
        'position': 'OL_COACH',
        'from_team': 'Ten',
        'to_team': 'Ten',
        'move_type': 'Coaching Retention',
        'contract_years': 2,
        'contract_value': 3500000,
        '2024_grade': 8.0,  # Elite OL coach
        'projected_2025_grade': 8.5,  # Critical for Ward protection
        'snap_percentage_2024': 100.0,  # Full OL responsibility
        'importance_to_old_team': 8.5,  # Best OL coach in NFL
        'importance_to_new_team': 9.5,  # Essential for rookie QB protection
    },
]

# TITANS SUMMARY METRICS
TITANS_2025_SUMMARY = {
    'total_moves': len(TITANS_2025_MOVES),
    'free_agent_signings': 8,
    'major_losses': 8,
    'draft_picks': 8,
    'key_resignings': 6,
    'coaching_changes': 4,
    'total_guaranteed_money': 95000000,  # Focused on OL and key positions
    'salary_cap_space_remaining': 35000000,
    'championship_window': '2027-2030',
    'offseason_grade': 'B+',
    'key_philosophy': 'Complete organizational reset with #1 pick QB',
    'biggest_concern': 'Young roster in competitive division',
    'biggest_strength': 'Excellent OL protection for rookie QB',
    'franchise_defining_move': 'Cam Ward #1 overall selection'
}

if __name__ == "__main__":
    print(f"Tennessee Titans 2025 Offseason Moves: {TITANS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {TITANS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {TITANS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${TITANS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {TITANS_2025_SUMMARY['key_philosophy']}")
    print(f"Franchise Defining Move: {TITANS_2025_SUMMARY['franchise_defining_move']}")
    print(f"Biggest Strength: {TITANS_2025_SUMMARY['biggest_strength']}")
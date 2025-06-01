"""
Baltimore Ravens 2025 Offseason Moves
Complete analysis of strategic roster reconstruction under Eric DeCosta
"""

RAVENS_2025_MOVES = [
    # RAVENS FREE AGENT SIGNINGS - Strategic value approach
    {
        'player_name': 'DeAndre Hopkins',
        'position': 'WR2',
        'from_team': 'Ten',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 5000000,
        '2024_grade': 6.5,  # 610 receiving yards, 1.5% drop rate
        'projected_2025_grade': 7.2,  # Better QB play with Jackson
        'snap_percentage_2024': 65.0,  # Limited role in Tennessee
        'importance_to_old_team': 6.0,  # Veteran depth piece
        'importance_to_new_team': 8.0,  # Key veteran target for Jackson
    },
    {
        'player_name': 'Cooper Rush',
        'position': 'QB',
        'from_team': 'Dal',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6200000,
        '2024_grade': 7.0,  # 9-5 career record as starter
        'projected_2025_grade': 7.0,  # Proven game manager
        'snap_percentage_2024': 25.0,  # Backup role
        'importance_to_old_team': 6.5,  # Reliable backup
        'importance_to_new_team': 7.5,  # Major upgrade from Josh Johnson
    },
    {
        'player_name': 'Chidobe Awuzie',
        'position': 'CB2',
        'from_team': 'Dal',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.8,  # 81 career starts, veteran experience
        'projected_2025_grade': 7.0,  # Should be healthier
        'snap_percentage_2024': 60.0,  # Injury-limited season
        'importance_to_old_team': 6.0,  # Depth piece
        'importance_to_new_team': 7.5,  # Critical secondary depth
    },
    {
        'player_name': 'Jake Hummel',
        'position': 'LB',
        'from_team': 'LAR',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,  # 8 special teams tackles, blocked punt TD
        'projected_2025_grade': 6.2,  # Special teams ace
        'snap_percentage_2024': 15.0,  # Mostly special teams
        'importance_to_old_team': 5.0,  # Special teams contributor
        'importance_to_new_team': 6.5,  # Replaces Harrison/Board production
    },
    {
        'player_name': 'Joe Noteboom',
        'position': 'OT',
        'from_team': 'LAR',
        'to_team': 'Bal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2800000,
        '2024_grade': 6.5,  # Versatile swing tackle
        'projected_2025_grade': 6.8,  # Good scheme fit
        'snap_percentage_2024': 45.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 7.0,  # Addresses OL depth need
    },

    # RAVENS MAJOR LOSSES - Key departures to division rivals and elsewhere
    {
        'player_name': 'Patrick Mekari',
        'position': 'G',
        'from_team': 'Bal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # Started all 17 games, ultimate versatility
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 100.0,  # 14 at LG, 3 at RT
        'importance_to_old_team': 8.0,  # Most reliable swing lineman
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Brandon Stephens',
        'position': 'CB1',
        'from_team': 'Bal',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Allowed 2nd-most receiving yards in NFL (806)
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,  # Starting corner despite struggles
        'importance_to_old_team': 7.0,  # Durable starter, missed only 3 games in 4 years
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Malik Harrison',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'Pit',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Career highs: 54 tackles, 2 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 38.0,  # 336 special teams snaps
        'importance_to_old_team': 7.5,  # Key special teams contributor
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Chris Board',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Led team with 382 special teams snaps
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 20.0,  # 80% of available special teams snaps
        'importance_to_old_team': 7.0,  # Special teams captain
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Josh Jones',
        'position': 'OT',
        'from_team': 'Bal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Primarily jumbo packages
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 25.0,  # Limited role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 0.0,
    },

    # RAVENS DRAFT PICKS - Elite draft haul, AFC North's best class
    {
        'player_name': 'Malaki Starks',
        'position': 'S',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #27',
        'contract_years': 4,
        'contract_value': 18500000,
        '2024_grade': 0.0,  # College - "best safety in draft" per DeCosta
        'projected_2025_grade': 8.0,  # Top-15 projection, elite ball skills
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Immediate starter alongside Kyle Hamilton
    },
    {
        'player_name': 'Mike Green',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #59',
        'contract_years': 4,
        'contract_value': 9800000,
        '2024_grade': 0.0,  # College - Led FBS with 17 sacks
        'projected_2025_grade': 7.5,  # 92.4 PFF grade, 20.2% pass-rush win rate
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate rotational help, star potential
    },
    {
        'player_name': 'Emery Jones Jr.',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #91',
        'contract_years': 4,
        'contract_value': 6200000,
        '2024_grade': 0.0,  # College - 2,323 of 2,355 snaps at RT
        'projected_2025_grade': 6.8,  # Swing tackle ability
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Addresses OL depth after Mekari loss
    },
    {
        'player_name': 'Teddye Buchanan',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #129',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - 40-inch vertical jump
        'projected_2025_grade': 6.5,  # Elite athleticism
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Replaces Harrison/Board special teams production
    },
    {
        'player_name': 'Carson Vinson',
        'position': 'OT',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #141',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,  # College - 84 3/8" wingspan
        'projected_2025_grade': 6.0,  # Developmental tackle
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Future depth development
    },
    {
        'player_name': 'Bilhal Kone',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #178',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - slot coverage specialist
        'projected_2025_grade': 6.2,  # Developmental corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Secondary depth
    },
    {
        'player_name': 'Tyler Loop',
        'position': 'K',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #186',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - First kicker ever drafted by Ravens
        'projected_2025_grade': 6.0,  # Succession planning for Tucker
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.0,  # Future investment
    },
    {
        'player_name': 'LaJohntay Wester',
        'position': 'WR3',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #203',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - 50 consecutive games with catches
        'projected_2025_grade': 6.0,  # Elite return ability
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Return specialist and WR depth
    },
    {
        'player_name': 'Aeneas Peebles',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #210',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - 91.2 PFF pass-rush grade
        'projected_2025_grade': 6.0,  # Developmental pass rusher
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Interior rush depth
    },
    {
        'player_name': 'Robert Longerbeam',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #212',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,  # College - 4.39 forty, undersized but fast
        'projected_2025_grade': 5.8,  # Long-term development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Future depth piece
    },
    {
        'player_name': 'Garrett Dellinger',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Bal',
        'move_type': '2025 Draft Pick #243',
        'contract_years': 4,
        'contract_value': 3200000,
        '2024_grade': 0.0,  # College - 4th LSU OL drafted in 2025
        'projected_2025_grade': 6.0,  # Interior line development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Addresses interior depth
    },

    # RAVENS KEY RE-SIGNINGS - Internal retention priorities
    {
        'player_name': 'Ronnie Stanley',
        'position': 'LT',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 60000000,
        '2024_grade': 8.5,  # 4th-best among LT in time to pressure (3.39 sec)
        'projected_2025_grade': 8.3,  # Should remain elite
        'snap_percentage_2024': 95.0,  # Durable when healthy
        'importance_to_old_team': 10.0,  # Jackson's blindside protector
        'importance_to_new_team': 10.0,  # Critical retention
    },
    {
        'player_name': 'Derrick Henry',
        'position': 'RB',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 30000000,
        '2024_grade': 9.2,  # 1,921 rushing yards, 18 TDs
        'projected_2025_grade': 8.8,  # Age 31 but still dominant
        'snap_percentage_2024': 85.0,  # Workhorse back
        'importance_to_old_team': 9.5,  # NFL's most devastating rusher
        'importance_to_new_team': 9.5,  # Maintains historic ground game
    },
    {
        'player_name': 'Patrick Ricard',
        'position': 'FB',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2870000,
        '2024_grade': 8.0,  # 5-time Pro Bowl FB
        'projected_2025_grade': 7.8,  # Remains elite blocker
        'snap_percentage_2024': 40.0,  # Key in ground game packages
        'importance_to_old_team': 8.0,  # Critical to ground attack
        'importance_to_new_team': 8.0,  # Fully guaranteed deal shows value
    },
    {
        'player_name': 'Todd Monken',
        'position': 'OC',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Coaching Extension',
        'contract_years': 3,
        'contract_value': 15000000,
        '2024_grade': 9.5,  # NFL's best offense in 2024
        'projected_2025_grade': 9.0,  # Continuity crucial
        'snap_percentage_2024': 100.0,  # Full offensive control
        'importance_to_old_team': 10.0,  # Offensive mastermind
        'importance_to_new_team': 10.0,  # Despite HC interest elsewhere
    },
    {
        'player_name': 'Tylan Wallace',
        'position': 'WR3',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.5,  # 76-yard punt return TD in 2023
        'projected_2025_grade': 6.8,  # Special teams value
        'snap_percentage_2024': 25.0,  # 4th/5th WR role
        'importance_to_old_team': 6.0,  # Depth and special teams
        'importance_to_new_team': 6.0,  # Continuity in return game
    },
    {
        'player_name': 'Ben Cleveland',
        'position': 'G',
        'from_team': 'Bal',
        'to_team': 'Bal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 6.0,  # Interior line depth
        'projected_2025_grade': 6.2,  # Developmental upside
        'snap_percentage_2024': 15.0,  # Rotational role
        'importance_to_old_team': 5.5,  # Depth piece
        'importance_to_new_team': 6.0,  # Addresses interior depth need
    },

    # RAVENS COACHING CHANGES - Strategic additions to fix defense
    {
        'player_name': 'Chuck Pagano',
        'position': 'DB_COACH',
        'from_team': 'RETIRED',
        'to_team': 'Bal',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 3000000,
        '2024_grade': 0.0,  # 4 years retired from coaching
        'projected_2025_grade': 8.0,  # Former Colts HC, championship pedigree
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Addresses 26th-ranked pass defense
    },
    {
        'player_name': 'Tyler Santucci',
        'position': 'LB_COACH',
        'from_team': 'COLLEGE',
        'to_team': 'Bal',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1500000,
        '2024_grade': 0.0,  # College coordinator experience
        'projected_2025_grade': 7.0,  # Georgia Tech/Duke DC experience
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Replaces Mark DeLeone
    },
    {
        'player_name': 'Donald D\'Alesio',
        'position': 'DB_COACH',
        'from_team': 'KC',
        'to_team': 'Bal',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        '2024_grade': 8.0,  # Back-to-back Super Bowl wins with Chiefs
        'projected_2025_grade': 8.0,  # Championship pedigree
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Lost to Baltimore
        'importance_to_new_team': 7.5,  # Proven championship coaching
    },
    {
        'player_name': 'Anthony Levine Sr.',
        'position': 'ST_COACH',
        'from_team': 'RETIRED',
        'to_team': 'Bal',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 800000,
        '2024_grade': 0.0,  # Former Ravens safety (2012-2021)
        'projected_2025_grade': 6.5,  # Playing experience helps
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Helps replace Harrison/Board production
    },

    # RAVENS UDFA SIGNINGS - Notable undrafted additions
    {
        'player_name': 'Jay Higgins',
        'position': 'LB',
        'from_team': 'COLLEGE',
        'to_team': 'Bal',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2700000,
        '2024_grade': 0.0,  # College - 295 tackles in final 2 seasons
        'projected_2025_grade': 6.0,  # $20K signing bonus shows confidence
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Linebacker depth development
    },
    {
        'player_name': 'Jahmal Banks',
        'position': 'WR3',
        'from_team': 'COLLEGE',
        'to_team': 'Bal',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2500000,
        '2024_grade': 0.0,  # College - Baltimore native
        'projected_2025_grade': 5.8,  # Local connection
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Depth and local story
    },
    {
        'player_name': 'Keondre Jackson',
        'position': 'CB2',
        'from_team': 'COLLEGE',
        'to_team': 'Bal',
        'move_type': 'UDFA Signing',
        'contract_years': 3,
        'contract_value': 2400000,
        '2024_grade': 0.0,  # College - Illinois State
        'projected_2025_grade': 5.5,  # Development piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Secondary depth
    },
]

# RAVENS SUMMARY METRICS
RAVENS_2025_SUMMARY = {
    'total_moves': len(RAVENS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 5,
    'draft_picks': 11,
    'key_resignings': 6,
    'coaching_changes': 4,
    'udfa_signings': 3,
    'total_guaranteed_money': 185000000,  # Includes Stanley/Henry extensions
    'net_compensatory_picks_2026': 3,  # 2 fifth-rounders, 1 seventh
    'salary_cap_space_remaining': 16330000,
    'championship_window': '2025-2027',
    'offseason_grade': 'A-',
    'key_philosophy': 'Measured aggression within constraints'
}

if __name__ == "__main__":
    print(f"Baltimore Ravens 2025 Offseason Moves: {RAVENS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {RAVENS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {RAVENS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${RAVENS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"Philosophy: {RAVENS_2025_SUMMARY['key_philosophy']}")
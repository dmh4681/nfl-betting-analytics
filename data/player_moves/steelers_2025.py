"""
Pittsburgh Steelers 2025 Offseason Moves
Complete analysis of dramatic roster transformation under Mike Tomlin
"""

STEELERS_2025_MOVES = [
    # STEELERS FREE AGENT SIGNINGS - Measured approach with defensive focus
    {
        'player_name': 'Darius Slay',
        'position': 'CB1',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10000000,
        '2024_grade': 7.8,  # Still productive veteran, started 14 games
        'projected_2025_grade': 7.5,  # Age 34 but championship experience
        'snap_percentage_2024': 81.0,  # Played 81% of defensive snaps for Eagles
        'importance_to_old_team': 7.5,  # Veteran leader for Eagles
        'importance_to_new_team': 8.0,  # Reunites with DC Teryl Austin
    },
    {
        'player_name': 'Juan Thornhill',
        'position': 'S',
        'from_team': 'KC',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3000000,
        '2024_grade': 6.5,  # Injury-limited to 11 games
        'projected_2025_grade': 7.0,  # Health dependent
        'snap_percentage_2024': 55.0,  # Limited by injuries
        'importance_to_old_team': 6.0,  # Depth piece for Chiefs
        'importance_to_new_team': 7.0,  # Championship pedigree
    },
    {
        'player_name': 'Malik Harrison',
        'position': 'LB',
        'from_team': 'Bal',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 10000000,
        '2024_grade': 7.0,  # Career highs: 54 tackles, 2 sacks
        'projected_2025_grade': 7.2,  # Should get more opportunity
        'snap_percentage_2024': 38.0,  # 336 special teams snaps for Ravens
        'importance_to_old_team': 7.5,  # Key special teams contributor
        'importance_to_new_team': 7.5,  # Continues Steelers poaching Ravens LBs
    },
    {
        'player_name': 'Kenneth Gainwell',
        'position': 'RB',
        'from_team': 'Phi',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1790000,
        '2024_grade': 6.8,  # 290 rushing yards, 116 receiving
        'projected_2025_grade': 7.0,  # Versatile complement
        'snap_percentage_2024': 25.0,  # Backup role
        'importance_to_old_team': 5.5,  # Eagles backup
        'importance_to_new_team': 6.5,  # Adds versatility behind Warren
    },
    {
        'player_name': 'Mason Rudolph',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 6.0,  # Bridge option while pursuing Rodgers
        'projected_2025_grade': 6.0,  # Familiar with system
        'snap_percentage_2024': 30.0,  # Limited role
        'importance_to_old_team': 6.0,  # Backup option
        'importance_to_new_team': 7.0,  # Insurance policy
    },
    {
        'player_name': 'Brandin Echols',
        'position': 'CB2',
        'from_team': 'NYJ',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': 'Daniel Ekuale',
        'position': 'DT',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },

    # STEELERS MAJOR LOSSES - Quarterback exodus and OL departures
    {
        'player_name': 'Justin Fields',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.5,  # 4-2 record as starter, dual-threat ability
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Started 6 games
        'importance_to_old_team': 8.0,  # Young QB with upside
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Russell Wilson',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # 11-game stint, late-season collapse
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,  # Primary starter
        'importance_to_old_team': 8.5,  # Veteran leadership
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Dan Moore Jr.',
        'position': 'LT',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Adequate but unspectacular
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 95.0,  # Starting LT
        'importance_to_old_team': 7.5,  # Key OL piece
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'James Daniels',
        'position': 'G',
        'from_team': 'Pit',
        'to_team': 'Mia',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Solid interior lineman
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 90.0,  # Starting guard
        'importance_to_old_team': 7.0,  # Interior OL stability
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Najee Harris',
        'position': 'RB',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Four consecutive 1,000-yard seasons
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Workhorse back
        'importance_to_old_team': 7.5,  # Primary rusher
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Donte Jackson',
        'position': 'CB2',
        'from_team': 'Pit',
        'to_team': 'LAC',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 70.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Larry Ogunjobi',
        'position': 'DT',
        'from_team': 'Pit',
        'to_team': 'Buf',
        'move_type': 'Release/Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Solid interior presence
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,  # Released for cap savings
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Van Jefferson',
        'position': 'WR3',
        'from_team': 'Pit',
        'to_team': 'Ten',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.8,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Mike Williams',
        'position': 'WR2',
        'from_team': 'Pit',
        'to_team': 'NYJ',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 0.0,
    },

    # STEELERS TRADES - Franchise-altering moves
    {
        'player_name': 'DK Metcalf',
        'position': 'WR1',
        'from_team': 'Sea',
        'to_team': 'Pit',
        'move_type': 'Trade',
        'contract_years': 5,
        'contract_value': 150000000,
        '2024_grade': 8.0,  # Elite receiver despite Seattle struggles
        'projected_2025_grade': 8.5,  # Better QB situation
        'snap_percentage_2024': 85.0,  # Primary receiver
        'importance_to_old_team': 9.0,  # Seahawks' top weapon
        'importance_to_new_team': 9.5,  # Franchise-altering acquisition
    },
    {
        'player_name': 'George Pickens',
        'position': 'WR2',
        'from_team': 'Pit',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Talented but character concerns
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Primary receiver
        'importance_to_old_team': 7.5,  # Addressed character/route-running issues
        'importance_to_new_team': 0.0,
    },

    # STEELERS DRAFT PICKS - Defensive focus with value selections
    {
        'player_name': 'Derrick Harmon',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #21',
        'contract_years': 4,
        'contract_value': 21500000,
        '2024_grade': 0.0,  # College - Led FBS with 34 QB pressures
        'projected_2025_grade': 7.5,  # "Steelers DNA" per Tomlin
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starter, Heyward successor
    },
    {
        'player_name': 'Kaleb Johnson',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #84',
        'contract_years': 4,
        'contract_value': 5800000,
        '2024_grade': 0.0,  # College - Physical, patient runner
        'projected_2025_grade': 7.0,  # Fell from 2nd round projection
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replaces Najee Harris
    },
    {
        'player_name': 'Jack Sawyer',
        'position': 'OLB',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #115',
        'contract_years': 4,
        'contract_value': 4700000,
        '2024_grade': 0.0,  # College - 15.9% pressure rate, Rose Bowl hero
        'projected_2025_grade': 6.8,  # Excellent value
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Depth behind Watt/Highsmith
    },
    {
        'player_name': 'Yahya Black',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #164',
        'contract_years': 4,
        'contract_value': 4100000,
        '2024_grade': 0.0,  # College - Honorable Mention All-Big Ten
        'projected_2025_grade': 6.0,  # Versatile run-stuffer
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Interior line depth
    },
    {
        'player_name': 'Will Howard',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #185',
        'contract_years': 4,
        'contract_value': 3900000,
        '2024_grade': 0.0,  # College - National championship experience
        'projected_2025_grade': 5.5,  # Developmental project, arm strength concerns
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Future development
    },
    {
        'player_name': 'Carson Bruener',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #217',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Son of former Steelers TE Mark Bruener
        'projected_2025_grade': 5.8,  # Legacy pick with potential
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Depth and special teams
    },
    {
        'player_name': 'Donte Kent',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Pit',
        'move_type': '2025 Draft Pick #226',
        'contract_years': 4,
        'contract_value': 3500000,
        '2024_grade': 0.0,  # College - Local product with return skills
        'projected_2025_grade': 5.5,  # Depth and special teams
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # Local connection
    },

    # STEELERS KEY RE-SIGNINGS - Maintaining core while waiting on Watt
    {
        'player_name': 'Jaylen Warren',
        'position': 'RB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'RFA Tender',
        'contract_years': 1,
        'contract_value': 5346000,
        '2024_grade': 7.5,  # Key complementary back
        'projected_2025_grade': 7.8,  # Should get more touches
        'snap_percentage_2024': 45.0,  # Complementary role
        'importance_to_old_team': 8.0,  # Critical retention
        'importance_to_new_team': 8.0,  # 2nd-round tender value
    },
    {
        'player_name': 'Ben Skowronek',
        'position': 'WR3',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 2,
        'contract_value': 3200000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 35.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': 'Scotty Miller',
        'position': 'WR3',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },
    {
        'player_name': 'James Pierre',
        'position': 'CB2',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': 'Isaiahh Loudermilk',
        'position': 'DE',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1200000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': 'Cameron Moon',
        'position': 'LB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 1000000,
        '2024_grade': 5.5,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 15.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },
    {
        'player_name': 'Breiden Fehoko',
        'position': 'DT',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 900000,
        '2024_grade': 5.5,
        'projected_2025_grade': 5.8,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },

    # STEELERS COACHING CHANGES - Minimal but targeted
    {
        'player_name': 'Gerald Alexander',
        'position': 'DB_COACH',
        'from_team': 'LV',
        'to_team': 'Pit',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1200000,
        '2024_grade': 6.5,  # Experience with Raiders
        'projected_2025_grade': 7.0,  # Familiar with Steelers system
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Replaces Grady Brown
    },
    {
        'player_name': 'Scott McCurry',
        'position': 'LB_COACH',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Internal Promotion',
        'contract_years': 2,
        'contract_value': 800000,
        '2024_grade': 6.0,  # Internal candidate
        'projected_2025_grade': 6.5,  # Continuity
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # Expected to replace Aaron Curry
    },

    # PENDING EXTENSIONS - Critical decisions ahead
    {
        'player_name': 'T.J. Watt',
        'position': 'OLB',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Extension (Pending)',
        'contract_years': 3,
        'contract_value': 108000000,
        '2024_grade': 9.5,  # Elite pass rusher
        'projected_2025_grade': 9.3,  # Still in prime
        'snap_percentage_2024': 85.0,  # Workhorse
        'importance_to_old_team': 10.0,  # Franchise cornerstone
        'importance_to_new_team': 10.0,  # Skipping OTAs for extension
    },
    {
        'player_name': 'DeShon Elliott',
        'position': 'S',
        'from_team': 'Pit',
        'to_team': 'Pit',
        'move_type': 'Extension (Projected)',
        'contract_years': 2,
        'contract_value': 18500000,
        '2024_grade': 8.0,  # Career year: 108 tackles, 6 PD, 3 FR
        'projected_2025_grade': 7.8,  # Should remain productive
        'snap_percentage_2024': 95.0,  # Every-down safety
        'importance_to_old_team': 8.5,  # Top extension priority
        'importance_to_new_team': 8.5,  # Would triple current salary
    },

    # AARON RODGERS PURSUIT - Ongoing uncertainty
    {
        'player_name': 'Aaron Rodgers',
        'position': 'QB',
        'from_team': 'UNSIGNED',
        'to_team': 'Pit',
        'move_type': 'Free Agent Pursuit',
        'contract_years': 1,
        'contract_value': 30000000,
        '2024_grade': 6.0,  # Declined with Jets
        'projected_2025_grade': 7.0,  # If committed to playing
        'snap_percentage_2024': 100.0,  # Would be starter
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 10.0,  # Make-or-break for 2025
    },
]

# STEELERS SUMMARY METRICS
STEELERS_2025_SUMMARY = {
    'total_moves': len(STEELERS_2025_MOVES),
    'free_agent_signings': 7,
    'major_losses': 9,
    'trades': 2,
    'draft_picks': 7,
    'key_resignings': 7,
    'coaching_changes': 2,
    'pending_extensions': 2,
    'total_guaranteed_money': 210000000,  # Includes Metcalf extension
    'net_cap_space_remaining': 32000000,
    'dead_money': 3600000,  # Lowest in NFL
    'championship_window': '2025-2027',
    'offseason_grade': 'C+',
    'key_uncertainty': 'Aaron Rodgers decision',
    'tomlin_season': 18,
    'playoff_drought': 8,  # Years since playoff win
}

# KEY STORYLINES
STEELERS_2025_STORYLINES = {
    'metcalf_blockbuster': {
        'trade_cost': '2025 2nd (#52) + 2025 7th (#223) for Metcalf + 2025 6th (#185)',
        'extension': '5 years, $150M total value, $60M guaranteed',
        'cap_impact': '$11M in 2025, escalates to $41.5M by 2029',
        'significance': 'Most aggressive offensive move in years'
    },
    'pickens_departure': {
        'trade_return': '2026 3rd + 2027 5th for Pickens + 2027 6th',
        'reasoning': 'Character concerns, route-running issues, redundancy with Metcalf',
        'draft_capital': 'Stockpiled picks for potential 2026 QB pursuit'
    },
    'quarterback_limbo': {
        'rodgers_status': 'Contract parameters agreed, decision pending',
        'alternatives': 'Mason Rudolph bridge, Will Howard development',
        'urgency': 'Training camp deadline approaching'
    },
    'afc_north_dynamics': {
        'ravens_competition': 'Poached Malik Harrison, continuing LB trend after Patrick Queen',
        'division_implications': 'Measured moves may concede 2025 race to aggressive Ravens',
        'tomlin_pressure': 'Never-had-losing-season streak vs 8-year playoff win drought'
    }
}

if __name__ == "__main__":
    print(f"Pittsburgh Steelers 2025 Offseason Moves: {STEELERS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {STEELERS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {STEELERS_2025_SUMMARY['championship_window']}")
    print(f"Cap Space Remaining: ${STEELERS_2025_SUMMARY['net_cap_space_remaining']:,}")
    print(f"Key Uncertainty: {STEELERS_2025_SUMMARY['key_uncertainty']}")
    print(f"Tomlin Season #{STEELERS_2025_SUMMARY['tomlin_season']}")
    print(f"Playoff Win Drought: {STEELERS_2025_SUMMARY['playoff_drought']} years")
    print()
    print("🔥 Major Storylines:")
    print(f"  📈 DK Metcalf: {STEELERS_2025_STORYLINES['metcalf_blockbuster']['significance']}")
    print(f"  📉 George Pickens: {STEELERS_2025_STORYLINES['pickens_departure']['reasoning']}")
    print(f"  ❓ Aaron Rodgers: {STEELERS_2025_STORYLINES['quarterback_limbo']['rodgers_status']}")
    print(f"  🏈 AFC North: {STEELERS_2025_STORYLINES['afc_north_dynamics']['division_implications']}")
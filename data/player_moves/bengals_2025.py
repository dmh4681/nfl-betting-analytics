"""
Cincinnati Bengals 2025 Offseason Moves
Complete analysis of historic $570M offensive investment
"""

BENGALS_2025_MOVES = [
    # BENGALS FREE AGENT SIGNINGS - Modest external additions
    {
        'player_name': 'T.J. Slaton',
        'position': 'DT',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 15100000,
        '2024_grade': 7.5,  # 3rd in run stop win rate
        'projected_2025_grade': 7.8,  # Addresses 31st-ranked run defense
        'snap_percentage_2024': 70.0,  # Key contributor for Packers
        'importance_to_old_team': 7.5,  # Solid run defender
        'importance_to_new_team': 8.5,  # Critical need addressed
    },
    {
        'player_name': 'Lucas Patrick',
        'position': 'G',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2100000,
        '2024_grade': 6.0,  # Veteran depth piece
        'projected_2025_grade': 6.2,  # Stopgap solution
        'snap_percentage_2024': 45.0,  # Backup role
        'importance_to_old_team': 5.5,  # Depth for Packers
        'importance_to_new_team': 6.5,  # Replaces departed Alex Cappa
    },
    {
        'player_name': 'Samaje Perine',
        'position': 'RB',
        'from_team': 'Den',
        'to_team': 'Cin',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 3800000,
        '2024_grade': 6.8,  # Elite pass protection, veteran depth
        'projected_2025_grade': 7.0,  # Reunion, knows system
        'snap_percentage_2024': 35.0,  # Complementary role
        'importance_to_old_team': 6.0,  # Denver depth
        'importance_to_new_team': 7.5,  # Pass protection specialist
    },

    # BENGALS MAJOR LOSSES - Retirements and departures
    {
        'player_name': 'Sam Hubbard',
        'position': 'EDGE',
        'from_team': 'Cin',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Team captain, seven seasons
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,  # Rotational edge rusher
        'importance_to_old_team': 8.0,  # Team captain, leadership void
        'importance_to_new_team': 0.0,
        'cap_savings': 9510000,  # Significant relief
    },
    {
        'player_name': 'Akeem Davis-Gaither',
        'position': 'LB',
        'from_team': 'Cin',
        'to_team': 'Ari',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.8,  # Special teams ace, linebacker depth
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 30.0,  # Special teams/depth role
        'importance_to_old_team': 6.5,  # Special teams contributions
        'importance_to_new_team': 0.0,
        'contract_value_new_team': 11000000,  # 2 years with Cardinals
    },

    # BENGALS HISTORIC EXTENSIONS - $570M commitment
    {
        'player_name': "Ja'Marr Chase",
        'position': 'WR1',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 161000000,
        '2024_grade': 9.8,  # Triple Crown winner: 127 catches, 1,708 yards, 17 TDs
        'projected_2025_grade': 9.5,  # Elite receiver in prime
        'snap_percentage_2024': 95.0,  # Every-down receiver
        'importance_to_old_team': 10.0,  # Franchise cornerstone
        'importance_to_new_team': 10.0,  # Highest-paid non-QB ($40.25M AAV)
        'guaranteed_money': 112000000,  # $73.8M fully guaranteed
        'cap_hit_2025': 23570000,  # Reasonable due to void years
    },
    {
        'player_name': 'Tee Higgins',
        'position': 'WR2',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Extension',
        'contract_years': 4,
        'contract_value': 115000000,
        '2024_grade': 8.5,  # Elite complementary receiver
        'projected_2025_grade': 8.3,  # Took less to stay
        'snap_percentage_2024': 85.0,  # Primary receiver
        'importance_to_old_team': 9.5,  # Critical retention
        'importance_to_new_team': 9.5,  # Team-friendly deal ($28.75M AAV)
        'guaranteed_money': 30000000,  # Below market, prioritized championships
        'team_options': True,  # Essentially team options after 2026
    },
    {
        'player_name': 'B.J. Hill',
        'position': 'DT',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 33000000,
        '2024_grade': 7.8,  # Solid interior presence
        'projected_2025_grade': 7.5,  # Reliable veteran
        'snap_percentage_2024': 70.0,  # Starting DT
        'importance_to_old_team': 8.0,  # Defensive anchor
        'importance_to_new_team': 8.0,  # Maintains continuity
    },
    {
        'player_name': 'Mike Gesicki',
        'position': 'TE',
        'from_team': 'Cin',
        'to_team': 'Cin',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 18000000,
        '2024_grade': 7.5,  # 65 catches, 2nd-most by Bengals TE in 43 years
        'projected_2025_grade': 7.3,  # Reliable target
        'snap_percentage_2024': 75.0,  # Primary tight end
        'importance_to_old_team': 7.5,  # Key receiving threat
        'importance_to_new_team': 7.5,  # Offensive continuity
    },

    # BENGALS DRAFT PICKS - Poorly reviewed class
    {
        'player_name': 'Shemar Stewart',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #17',
        'contract_years': 4,
        'contract_value': 25200000,
        '2024_grade': 0.0,  # College - Only 4.5 sacks in 3 seasons
        'projected_2025_grade': 6.0,  # High-risk, high-reward developmental bet
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Potential Hendrickson insurance
        'draft_criticism': 'Developmental pick for win-now team',
    },
    {
        'player_name': 'Demetrius Knight Jr.',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #49',
        'contract_years': 4,
        'contract_value': 9800000,
        '2024_grade': 0.0,  # College - 25-year-old South Carolina LB
        'projected_2025_grade': 6.2,  # Age concerns for 2nd rounder
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Fits Golden's flexible approach
    },
    {
        'player_name': 'Dylan Fairchild',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #81',
        'contract_years': 4,
        'contract_value': 5600000,
        '2024_grade': 0.0,  # College - 87.0 PFF pass-blocking grade
        'projected_2025_grade': 7.5,  # Draft's brightest spot
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Immediate starting potential at LG
        'college_stats': 'One allowed sack in entire college career',
    },
    {
        'player_name': 'Barrett Carter',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #118',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,  # College - Clemson linebacker
        'projected_2025_grade': 6.0,  # Depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Golden's flexible system
    },
    {
        'player_name': 'Jalen Rivers',
        'position': 'OL',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #156',
        'contract_years': 4,
        'contract_value': 4200000,
        '2024_grade': 0.0,  # College - Miami, versatility
        'projected_2025_grade': 5.8,  # Depth and development
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # OL versatility
    },
    {
        'player_name': 'Tahj Brooks',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Cin',
        'move_type': '2025 Draft Pick #189',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,  # College - Texas Tech
        'projected_2025_grade': 5.5,  # Depth piece
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 5.5,  # RB depth
    },

    # BENGALS COACHING OVERHAUL - Defensive transformation
    {
        'player_name': 'Al Golden',
        'position': 'DC',
        'from_team': 'NOTRE_DAME',
        'to_team': 'Cin',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 4500000,
        '2024_grade': 7.5,  # Previous Bengals LB coach 2020-2021
        'projected_2025_grade': 8.0,  # Brings familiarity and innovation
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Notre Dame success
        'importance_to_new_team': 9.0,  # Must fix 25th-ranked defense
        'philosophy': 'Malleable defense with multiple looks',
    },
    {
        'player_name': 'Sean Desai',
        'position': 'SENIOR_DEF_ASST',
        'from_team': 'LAR',
        'to_team': 'Cin',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1800000,
        '2024_grade': 7.0,  # Recent NFL coordinator experience
        'projected_2025_grade': 7.2,  # Proven NFL experience
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.5,  # Rams assistant
        'importance_to_new_team': 7.5,  # Veteran guidance for Golden
    },
    {
        'player_name': 'Jerry Montgomery',
        'position': 'DL_COACH',
        'from_team': 'GB',
        'to_team': 'Cin',
        'move_type': 'Coaching Hire',
        'contract_years': 2,
        'contract_value': 1200000,
        '2024_grade': 7.5,  # Nine successful years in Green Bay
        'projected_2025_grade': 7.8,  # Proven track record
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.5,  # Packers success
        'importance_to_new_team': 8.0,  # DL development expertise
    },

    # BENGALS COACHING DEPARTURES - Major changes
    {
        'player_name': 'Lou Anarumo',
        'position': 'DC',
        'from_team': 'Cin',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.0,  # Defense ranked 25th, cost playoff berth
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,  # Six seasons, needed change
        'importance_to_new_team': 0.0,
        'fired_date': 'January 6, 2025',
    },
    {
        'player_name': 'Frank Pollack',
        'position': 'OL_COACH',
        'from_team': 'Cin',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.0,  # OL struggles
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.5,  # Part of overhaul
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Marion Hobby',
        'position': 'DL_COACH',
        'from_team': 'Cin',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.0,  # Part of defensive overhaul
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.5,  # Replaced by Montgomery
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'James Bettcher',
        'position': 'LB_COACH',
        'from_team': 'Cin',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.0,  # Part of defensive overhaul
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.5,  # Defensive changes needed
        'importance_to_new_team': 0.0,
    },
]

# TREY HENDRICKSON SITUATION - Unresolved critical issue
HENDRICKSON_CONTRACT_DISPUTE = {
    'player_name': 'Trey Hendrickson',
    'position': 'EDGE',
    'current_contract': 15800000,  # 2025 salary
    'market_demand': 28000000,  # Seeking $28-30M annually
    'bengals_offer': 28000000,  # Reportedly offered $28M annually
    '2024_performance': {
        'sacks': 17.5,  # Led NFL
        'importance': 10.0,  # Best defensive player
        'age': 30,  # Aging pass rusher
    },
    'trade_permission': True,  # Granted permission to seek trade
    'draft_insurance': 'Shemar Stewart',  # Potential replacement
    'status': 'Extremely dug in on holdout',
    'resolution_urgency': 'Mandatory minicamp approaching',
    'team_decision': 'Pay premium or risk defensive regression',
}

# BENGALS SUMMARY METRICS
BENGALS_2025_SUMMARY = {
    'total_moves': len(BENGALS_2025_MOVES),
    'free_agent_signings': 3,
    'major_losses': 2,
    'historic_extensions': 4,
    'draft_picks': 6,
    'coaching_hires': 3,
    'coaching_departures': 4,
    'total_offensive_investment': 570000000,  # Burrow + Chase + Higgins
    'net_cap_space_remaining': 48000000,  # After extensions
    'dead_money': 27000000,  # Moderate burden
    'championship_window': '2025-2028',
    'offseason_grade': 'A-',  # Historic investment
    'key_uncertainty': 'Trey Hendrickson holdout',
    'zac_taylor_season': 7,
    'playoff_miss_years': 2,  # Missed 2024 after expectations
}

# KEY STORYLINES
BENGALS_2025_STORYLINES = {
    'historic_investment': {
        'total_commitment': '$570+ million to offensive core',
        'chase_contract': '4 years, $161M, highest-paid non-QB at $40.25M AAV',
        'higgins_discount': 'Took $30M guaranteed vs market rate for championships',
        'philosophy_shift': 'From conservative spending to aggressive star retention',
        'significance': 'Most expensive WR tandem in NFL history at $69M combined AAV'
    },
    'defensive_overhaul': {
        'anarumo_firing': 'Fired January 6 after six seasons, 25th-ranked defense',
        'golden_hire': 'Returns from Notre Dame, previous Bengals LB coach 2020-2021',
        'philosophy_change': 'Malleable defense vs rigid schemes, multiple looks',
        'staff_additions': 'Sean Desai (NFL experience), Jerry Montgomery (9 years GB)',
        'challenge': 'Must improve 25th-ranked defense that cost playoff berth'
    },
    'hendrickson_standoff': {
        'performance': 'Led NFL with 17.5 sacks in 2024',
        'contract_demand': '$28-30M annually vs current $15.8M',
        'bengals_offer': 'Reportedly $28M annually but no agreement',
        'trade_permission': 'Granted permission to seek trade',
        'draft_insurance': 'Selected Shemar Stewart as potential replacement',
        'impact': 'Cannot afford to lose best defensive player'
    },
    'draft_criticism': {
        'universal_reviews': 'Dead last among 32 teams with 2.06 GPA',
        'stewart_selection': 'Only 4.5 sacks in 3 college seasons',
        'knight_age': '25-year-old in 2nd round raised eyebrows',
        'fairchild_bright_spot': '87.0 PFF pass-blocking grade, immediate starter',
        'win_now_concerns': 'Developmental picks for championship window team'
    },
    'salary_cap_management': {
        'starting_space': '$27 million initially',
        'savings_created': '$27 million from retirements/releases (Hubbard, others)',
        'current_space': '$46-51 million effective space',
        'burrow_jump': '$46M cap hit vs $29.6M in 2024',
        'restructure_potential': '$19.3M additional if Burrow restructures',
        'void_years': '$40M total (moderate compared to other teams)'
    },
    'afc_north_competition': {
        'ravens_favorites': 'Clear division leaders despite aging core',
        'steelers_qb_uncertainty': 'Aaron Rodgers speculation, transition period',
        'browns_chaos': 'Watson injury, quarterback room uncertainty',
        'bengals_opportunity': '25th-ranked defense must improve to capitalize',
        'division_challenge': 'Run-heavy Ravens, Browns, Steelers approaches'
    }
}

# BURROW ERA ANALYSIS
BURROW_CHAMPIONSHIP_WINDOW = {
    'qb_age': 28,  # Entering prime
    'contract_structure': '3-4 year window with current extensions',
    'offensive_investment': 'Historic commitment to Chase/Higgins tandem',
    'defensive_question': 'Can coaching changes and development overcome losses?',
    'margin_for_error': 'Narrowed considerably with quality over quantity approach',
    'ceiling': 'Championship caliber with NFL\'s most explosive passing attack',
    'floor': 'Mediocrity if defense cannot improve significantly',
    'critical_factors': [
        'Hendrickson resolution',
        'Golden\'s defensive transformation',
        'Rookie development (especially Stewart)',
        'Offensive line protection for massive investment'
    ]
}

if __name__ == "__main__":
    print(f"Cincinnati Bengals 2025 Offseason Moves: {BENGALS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {BENGALS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {BENGALS_2025_SUMMARY['championship_window']}")
    print(f"Total Offensive Investment: ${BENGALS_2025_SUMMARY['total_offensive_investment']:,}")
    print(f"Cap Space Remaining: ${BENGALS_2025_SUMMARY['net_cap_space_remaining']:,}")
    print(f"Key Uncertainty: {BENGALS_2025_SUMMARY['key_uncertainty']}")
    print()
    print("🔥 Major Storylines:")
    print(f"  💰 Historic Investment: {BENGALS_2025_STORYLINES['historic_investment']['significance']}")
    print(f"  🛡️ Defensive Overhaul: {BENGALS_2025_STORYLINES['defensive_overhaul']['philosophy_change']}")
    print(f"  ⚔️ Hendrickson Standoff: {BENGALS_2025_STORYLINES['hendrickson_standoff']['performance']}")
    print(f"  📊 Draft Criticism: {BENGALS_2025_STORYLINES['draft_criticism']['universal_reviews']}")
    print(f"  🏈 Championship Window: {BURROW_CHAMPIONSHIP_WINDOW['ceiling']}")
    print()
    print("🚨 Trey Hendrickson Situation:")
    print(f"  Current Salary: ${HENDRICKSON_CONTRACT_DISPUTE['current_contract']:,}")
    print(f"  Market Demand: ${HENDRICKSON_CONTRACT_DISPUTE['market_demand']:,} annually")
    print(f"  2024 Performance: {HENDRICKSON_CONTRACT_DISPUTE['2024_performance']['sacks']} sacks (NFL leader)")
    print(f"  Status: {HENDRICKSON_CONTRACT_DISPUTE['status']}")
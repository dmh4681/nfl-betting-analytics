"""
Chicago Bears 2025 Offseason Moves
Complete analysis of $257M transformation around Caleb Williams under Ryan Poles and Ben Johnson
"""

BEARS_2025_MOVES = [
    # BEARS MAJOR TRADES - Offensive line revolution
    {
        'player_name': 'Joe Thuney',
        'position': 'LG',
        'from_team': 'KC',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 3,
        'contract_value': 78000000,
        '2024_grade': 8.8,  # All-Pro guard, 98.2% pass block win rate
        'projected_2025_grade': 8.8,  # Elite protection for Williams
        'snap_percentage_2024': 95.0,  # Mahomes protector
        'importance_to_old_team': 9.5,  # KC cap casualty despite excellence
        'importance_to_new_team': 9.5,  # 4x Super Bowl winner leadership
    },
    {
        'player_name': 'Jonah Jackson',
        'position': 'RG',
        'from_team': 'LAR',
        'to_team': 'Chi',
        'move_type': 'Trade',
        'contract_years': 2,
        'contract_value': 24000000,
        '2024_grade': 7.8,  # 94.7% pass block win rate when healthy
        'projected_2025_grade': 8.0,  # Johnson reunion from Detroit days
        'snap_percentage_2024': 25.0,  # Limited by injury (4 games)
        'importance_to_old_team': 6.0,  # Rams cut losses on injury
        'importance_to_new_team': 8.5,  # Scheme familiarity with Johnson
    },

    # BEARS FREE AGENT SIGNINGS - Championship experience priority
    {
        'player_name': 'Drew Dalman',
        'position': 'C',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 42000000,
        '2024_grade': 7.8,  # 4th among centers with 78.8 PFF grade
        'projected_2025_grade': 8.0,  # Interior line anchor
        'snap_percentage_2024': 85.0,  # Falcons starting center
        'importance_to_old_team': 7.5,  # Atlanta's center departure
        'importance_to_new_team': 9.0,  # Addresses revolving door since 2018
    },
    {
        'player_name': 'Grady Jarrett',
        'position': 'DT',
        'from_team': 'Atl',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 43500000,
        '2024_grade': 7.5,  # 2x Pro Bowler, 36.5 career sacks
        'projected_2025_grade': 8.0,  # Interior pass rush upgrade
        'snap_percentage_2024': 80.0,  # Falcons starter before release
        'importance_to_old_team': 8.0,  # Atlanta cap casualty
        'importance_to_new_team': 8.5,  # Pairs with Gervon Dexter
    },
    {
        'player_name': 'Dayo Odeyingbo',
        'position': 'EDGE',
        'from_team': 'Ind',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 48000000,
        '2024_grade': 7.2,  # 8 sacks in 2023, solid edge rusher
        'projected_2025_grade': 7.5,  # Complement to Montez Sweat
        'snap_percentage_2024': 70.0,  # Colts starter
        'importance_to_old_team': 7.0,  # Colts edge depth lost
        'importance_to_new_team': 8.0,  # Allen's 4-3 scheme fit
    },
    {
        'player_name': 'Case Keenum',
        'position': 'QB',
        'from_team': 'Buf',
        'to_team': 'Chi',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        '2024_grade': 6.5,  # Veteran backup experience
        'projected_2025_grade': 7.0,  # Mentorship for Williams
        'snap_percentage_2024': 15.0,  # Limited backup duty
        'importance_to_old_team': 6.0,  # Bills backup depth
        'importance_to_new_team': 7.5,  # Veteran leadership addition
    },

    # BEARS KEY EXTENSIONS - Defensive cornerstones secured
    {
        'player_name': 'Kyler Gordon',
        'position': 'CB1',
        'from_team': 'Chi',
        'to_team': 'Chi',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 40000000,
        '2024_grade': 8.0,  # 76.0 PFF grade, elite slot defender
        'projected_2025_grade': 8.2,  # NFL's highest-paid nickel corner
        'snap_percentage_2024': 85.0,  # Primary slot corner
        'importance_to_old_team': 8.5,  # Defensive secondary anchor
        'importance_to_new_team': 8.5,  # $31.25M guaranteed commitment
    },
    {
        'player_name': 'T.J. Edwards',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Chi',
        'move_type': 'Extension',
        'contract_years': 2,
        'contract_value': 20000000,
        '2024_grade': 8.0,  # Team captain, 129 tackles in 2024
        'projected_2025_grade': 8.0,  # Defensive leadership retained
        'snap_percentage_2024': 90.0,  # Every-down linebacker
        'importance_to_old_team': 8.5,  # Team captain and leader
        'importance_to_new_team': 8.5,  # Team-friendly deal through 2027
    },

    # BEARS MAJOR LOSSES - Cap casualties and departures
    {
        'player_name': 'Teven Jenkins',
        'position': 'G',
        'from_team': 'Chi',
        'to_team': 'Cle',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.0,  # Solid guard play when healthy
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,  # Starting guard
        'importance_to_old_team': 7.0,  # Replaced by elite acquisitions
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jack Sanborn',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.5,  # Solid depth linebacker
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 45.0,  # Rotational linebacker
        'importance_to_old_team': 6.5,  # Reunites with Eberflus in Dallas
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Keenan Allen',
        'position': 'WR1',
        'from_team': 'Chi',
        'to_team': 'FA',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # Injury-limited veteran receiver
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # When healthy, productive
        'importance_to_old_team': 6.0,  # Aging veteran, injury concerns
        'importance_to_new_team': 0.0,
    },

    # BEARS 2025 NFL DRAFT - Weapons and protection for Williams
    {
        'player_name': 'Colston Loveland',
        'position': 'TE',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #10',
        'contract_years': 4,
        'contract_value': 28500000,
        '2024_grade': 0.0,  # College - Michigan (6'6", 248 lbs, Sam LaPorta comp)
        'projected_2025_grade': 7.8,  # Immediate mismatch weapon
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Johnson system perfect fit
    },
    {
        'player_name': 'Luther Burden III',
        'position': 'WR2',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #39',
        'contract_years': 4,
        'contract_value': 12800000,
        '2024_grade': 0.0,  # College - Missouri (1,212 yards, elite YAC ability)
        'projected_2025_grade': 7.5,  # Slot receiver and returner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # PFF's WR2 in class, great value
    },
    {
        'player_name': 'Ozzy Trapilo',
        'position': 'LT',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #56',
        'contract_years': 4,
        'contract_value': 8900000,
        '2024_grade': 0.0,  # College - Boston College (6'8", 36 career starts)
        'projected_2025_grade': 7.0,  # LT competition with Amegadjie
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Jones ankle surgery insurance
    },
    {
        'player_name': 'Shemar Turner',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #62',
        'contract_years': 4,
        'contract_value': 7200000,
        '2024_grade': 0.0,  # College - Texas A&M ("violence and aggression")
        'projected_2025_grade': 6.8,  # Allen's defensive philosophy fit
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Defensive line depth
    },
    {
        'player_name': 'Ruben Hyppolite II',
        'position': 'LB',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #118',
        'contract_years': 4,
        'contract_value': 4800000,
        '2024_grade': 0.0,  # College - Maryland (linebacker depth)
        'projected_2025_grade': 6.5,  # Developmental linebacker
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # LB depth behind Edwards
    },
    {
        'player_name': 'Zah Frazier',
        'position': 'CB2',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #151',
        'contract_years': 4,
        'contract_value': 4300000,
        '2024_grade': 0.0,  # College - UTSA (9.36 RAS score)
        'projected_2025_grade': 6.5,  # Athletic cornerback project
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,  # Secondary depth
    },
    {
        'player_name': 'Luke Newman',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #183',
        'contract_years': 4,
        'contract_value': 4000000,
        '2024_grade': 0.0,  # College - Michigan State (versatile OL)
        'projected_2025_grade': 6.2,  # Interior line depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # OL depth and competition
    },
    {
        'player_name': 'Kyle Monangai',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'Chi',
        'move_type': '2025 Draft Pick #247',
        'contract_years': 4,
        'contract_value': 3600000,
        '2024_grade': 0.0,  # College - Rutgers (Big Ten rushing leader 2 years)
        'projected_2025_grade': 6.0,  # Backfield depth
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # RB room competition
    },

    # BEARS COACHING OVERHAUL - Complete offensive transformation
    {
        'player_name': 'Ben Johnson',
        'position': 'HC',
        'from_team': 'Det',
        'to_team': 'Chi',
        'move_type': 'Coaching Hire',
        'contract_years': 5,
        'contract_value': 40000000,
        '2024_grade': 9.5,  # NFL's best offense coordinator (29.0 PPG 2022-24)
        'projected_2025_grade': 9.5,  # Elite QB developer (Goff transformation)
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 9.5,  # Lions lost elite coordinator
        'importance_to_new_team': 10.0,  # Williams development crucial
    },
    {
        'player_name': 'Dennis Allen',
        'position': 'DC',
        'from_team': 'NO',
        'to_team': 'Chi',
        'move_type': 'Coaching Hire',
        'contract_years': 4,
        'contract_value': 20000000,
        '2024_grade': 7.5,  # Former Saints HC, aggressive 4-3 scheme
        'projected_2025_grade': 8.0,  # Defensive scheme overhaul
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 7.0,  # Saints moved on from HC
        'importance_to_new_team': 8.5,  # Philosophy shift from "bend don't break"
    },
    {
        'player_name': 'Declan Doyle',
        'position': 'OC',
        'from_team': 'Den',
        'to_team': 'Chi',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        '2024_grade': 6.5,  # Young coach promoted from Broncos TE coach
        'projected_2025_grade': 7.5,  # Johnson's hand-picked coordinator
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 6.0,  # Broncos coaching staff loss
        'importance_to_new_team': 7.5,  # 28-year-old coordinator under Johnson
    },
    {
        'player_name': 'J.T. Barrett',
        'position': 'QB_COACH',
        'from_team': 'OSU',
        'to_team': 'Chi',
        'move_type': 'Coaching Hire',
        'contract_years': 3,
        'contract_value': 2500000,
        '2024_grade': 6.0,  # Former Ohio State QB, coaching transition
        'projected_2025_grade': 7.0,  # Williams development specialist
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 5.0,  # Ohio State quality control loss
        'importance_to_new_team': 7.5,  # Young QB developer
    },
]

# BEARS SUMMARY METRICS
BEARS_2025_SUMMARY = {
    'total_moves': len(BEARS_2025_MOVES),
    'free_agent_signings': 5,
    'major_losses': 3,
    'trades': 2,
    'draft_picks': 8,
    'key_resignings': 2,
    'coaching_changes': 4,
    'total_guaranteed_money': 257000000,  # Historic transformation spending
    'salary_cap_space_remaining': 15000000,
    'championship_window': '2025-2028',
    'offseason_grade': 'A-',
    'key_philosophy': 'Complete transformation around Williams with elite protection and weapons',
    'biggest_concern': 'Jonah Jackson injury history and pass rush depth',
    'biggest_strength': 'Elite offensive line transformation (68 sacks to potential top-10 unit)',
    'coaching_revolution': 'Ben Johnson brings Lions\' #1 offense system to Chicago',
    'draft_excellence': 'NFL.com A grade, PFF A- grade for value and scheme fits',
    'betting_implication': 'Dramatic improvement expected but NFC North gauntlet remains challenging'
}

if __name__ == "__main__":
    print(f"Chicago Bears 2025 Offseason Moves: {BEARS_2025_SUMMARY['total_moves']} transactions")
    print(f"Offseason Grade: {BEARS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {BEARS_2025_SUMMARY['championship_window']}")
    print(f"Total Guaranteed Money: ${BEARS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"Philosophy: {BEARS_2025_SUMMARY['key_philosophy']}")
    print(f"Coaching Revolution: {BEARS_2025_SUMMARY['coaching_revolution']}")
    print(f"Biggest Strength: {BEARS_2025_SUMMARY['biggest_strength']}")
    print(f"Draft Excellence: {BEARS_2025_SUMMARY['draft_excellence']}")
    print(f"Betting Implication: {BEARS_2025_SUMMARY['betting_implication']}")
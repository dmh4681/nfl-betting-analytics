"""
New York Giants 2025 Offseason Moves
Complete roster overhaul after franchise-worst 3-14 season
"""

GIANTS_2025_MOVES = [
    # GIANTS MAJOR QB ACQUISITIONS
    {
        'player_name': 'Russell Wilson',
        'position': 'QB',
        'from_team': 'Pit',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 10500000,  # Fully guaranteed
        '2024_grade': 7.2,  # Former Super Bowl champion
        'projected_2025_grade': 6.8,  # Age 36
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 8.5,
        'importance_to_new_team': 9.5,  # Expected starter, veteran leadership
    },
    {
        'player_name': 'Jameis Winston',
        'position': 'QB',
        'from_team': 'Cle',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        '2024_grade': 6.5,  # Former #1 overall pick
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Primary backup
    },
    
    # GIANTS SECONDARY TRANSFORMATION
    {
        'player_name': 'Jevon Holland',
        'position': 'S',
        'from_team': 'Mia',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 45300000,  # $30.3M guaranteed
        '2024_grade': 6.8,  # Career-low coverage grade
        'projected_2025_grade': 7.5,  # Change of scenery
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.5,  # Biggest financial commitment
    },
    {
        'player_name': 'Paulson Adebo',
        'position': 'CB1',
        'from_team': 'NO',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 54000000,  # $36M fully guaranteed
        '2024_grade': 7.5,  # Shutdown corner before injury
        'projected_2025_grade': 7.8,  # Recovery from broken leg
        'snap_percentage_2024': 60.0,  # Injury-limited
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 9.0,  # Opposite Deonte Banks
    },
    
    # GIANTS DEFENSIVE LINE REINFORCEMENTS
    {
        'player_name': 'Chauncey Golston',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 3,
        'contract_value': 19500000,
        '2024_grade': 7.0,  # Career-high 5.5 sacks
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
    },
    {
        'player_name': 'Roy Robertson-Harris',
        'position': 'DT',
        'from_team': 'Jac',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 9000000,
        '2024_grade': 6.5,  # Veteran experience
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,
    },
    {
        'player_name': 'Jeremiah Ledbetter',
        'position': 'DT',
        'from_team': 'Jac',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.2,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    
    # GIANTS NOTABLE DEPTH SIGNINGS
    {
        'player_name': 'Chris Board',
        'position': 'LB',
        'from_team': 'Det',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 6000000,
        '2024_grade': 7.0,  # Tied for 9th in NFL with 8 ST tackles
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 25.0,  # Mostly special teams
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.0,  # Veteran leadership
    },
    {
        'player_name': 'James Hudson III',
        'position': 'RT',
        'from_team': 'Cin',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 12000000,
        '2024_grade': 6.2,
        'projected_2025_grade': 6.5,
        'snap_percentage_2024': 50.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.5,  # OL depth
    },
    {
        'player_name': 'Stone Forsythe',
        'position': 'RT',
        'from_team': 'Mia',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },
    {
        'player_name': 'Zach Pascal',
        'position': 'WR3',
        'from_team': 'Ari',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1800000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.0,
    },
    {
        'player_name': "Lil'Jordan Humphrey",
        'position': 'WR3',
        'from_team': 'Den',
        'to_team': 'NYG',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 1500000,
        '2024_grade': 5.8,
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 5.5,
    },
    
    # GIANTS MAJOR DEPARTURES TO DIVISION RIVALS
    {
        'player_name': 'Azeez Ojulari',
        'position': 'EDGE',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 7.2,  # 22 career sacks despite injuries
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 35.0,  # Limited snaps behind Burns/Thibodeaux
        'importance_to_old_team': 6.0,  # 2021 second-round pick
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Adoree Jackson',
        'position': 'CB2',
        'from_team': 'NYG',
        'to_team': 'Phi',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.9,  # Started 5 of 14 games
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 65.0,
        'importance_to_old_team': 6.5,  # Former first-round pick
        'importance_to_new_team': 0.0,
    },
    
    # GIANTS OTHER KEY DEPARTURES
    {
        'player_name': 'Isaiah Simmons',
        'position': 'LB',
        'from_team': 'NYG',
        'to_team': 'GB',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.0,  # 17% of defensive snaps
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 17.0,
        'importance_to_old_team': 5.0,  # Versatile but underused
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Drew Lock',
        'position': 'QB',
        'from_team': 'NYG',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 5.5,  # Backup QB
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 10.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 0.0,
    },
    {
        'player_name': 'Jason Pinnock',
        'position': 'S',
        'from_team': 'NYG',
        'to_team': 'SF',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 6.2,
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.0,  # Safety depth
        'importance_to_new_team': 0.0,
    },
    
    # GIANTS DANIEL JONES ERA ENDS
    {
        'player_name': 'Daniel Jones',
        'position': 'QB',
        'from_team': 'NYG',
        'to_team': 'RELEASED',
        'move_type': 'Release',
        'contract_years': 0,
        'contract_value': 0,
        '2024_grade': 4.5,  # Demoted to fourth-string
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,  # Before benching
        'importance_to_old_team': 7.0,  # $22.2M dead cap
        'importance_to_new_team': 0.0,
    },
    
    # GIANTS DRAFT DAY BLOCKBUSTER TRADE
    {
        'player_name': 'Jaxson Dart',
        'position': 'QB',
        'from_team': 'DRAFT',
        'to_team': 'NYG',
        'move_type': '2025 Draft Pick #25 (via trade)',
        'contract_years': 4,
        'contract_value': 16977000,  # Fully guaranteed
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 4,279 yards, 29 TDs
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Franchise QB of future
    },
    
    # GIANTS 2025 DRAFT SELECTIONS
    {
        'player_name': 'Abdul Carter',
        'position': 'EDGE',
        'from_team': 'DRAFT',
        'to_team': 'NYG',
        'move_type': '2025 Draft Pick #3',
        'contract_years': 4,
        'contract_value': 45260000,  # Fully guaranteed
        '2024_grade': 0.0,
        'projected_2025_grade': 8.5,  # Elite pass rusher, 12 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.5,  # Immediate starter opposite Burns/Thibodeaux
    },
    {
        'player_name': 'Darius Alexander',
        'position': 'DT',
        'from_team': 'DRAFT',
        'to_team': 'NYG',
        'move_type': '2025 Draft Pick #65',
        'contract_years': 4,
        'contract_value': 6500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.0,  # 90.1 PFF grade
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Rotational help behind Dexter Lawrence
    },
    {
        'player_name': 'Cam Skattebo',
        'position': 'RB',
        'from_team': 'DRAFT',
        'to_team': 'NYG',
        'move_type': '2025 Draft Pick #105',
        'contract_years': 4,
        'contract_value': 4500000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 100+ missed tackles forced
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,  # Power complement to Tracy Jr.
    },
    {
        'player_name': 'Marcus Mbow',
        'position': 'G',
        'from_team': 'DRAFT',
        'to_team': 'NYG',
        'move_type': '2025 Draft Pick #154',
        'contract_years': 4,
        'contract_value': 3800000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.0,  # Medical concerns
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.0,  # Guard competition
    },
    
    # GIANTS KEY RE-SIGNINGS
    {
        'player_name': 'Darius Slayton',
        'position': 'WR1',
        'from_team': 'NYG',
        'to_team': 'NYG',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 36000000,
        '2024_grade': 7.5,  # Leading receiver 4 of last 5 seasons
        'projected_2025_grade': 7.8,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 8.0,
        'importance_to_new_team': 8.0,  # Longest-tenured offensive player
    },
    {
        'player_name': 'Jamie Gillan',
        'position': 'P',
        'from_team': 'NYG',
        'to_team': 'NYG',
        'move_type': 'Extension',
        'contract_years': 3,
        'contract_value': 10200000,
        '2024_grade': 7.0,
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 100.0,  # All punts
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,  # One of highest-paid punters
    },
    {
        'player_name': 'Greg Van Roten',
        'position': 'G',
        'from_team': 'NYG',
        'to_team': 'NYG',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 2500000,
        '2024_grade': 7.2,  # Didn't miss single snap (1,125 plays)
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 100.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 7.5,  # Iron man
    },
    {
        'player_name': 'Tommy DeVito',
        'position': 'QB',
        'from_team': 'NYG',
        'to_team': 'NYG',
        'move_type': 'Exclusive Rights Tender',
        'contract_years': 1,
        'contract_value': 1030000,
        '2024_grade': 6.0,  # Local hero
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 20.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 6.0,  # System familiarity
    },
]

# GIANTS SUMMARY METRICS
GIANTS_2025_SUMMARY = {
    'total_moves': len(GIANTS_2025_MOVES),
    'free_agent_signings': 10,
    'major_losses': 6,
    'draft_picks': 5,
    'key_resignings': 4,
    'trades': 1,  # Draft day trade up for Dart
    'total_guaranteed_money': 180000000,  # Includes Holland, Adebo, Wilson
    'dead_money': 22200000,  # From Daniel Jones release
    'championship_window': '2026-2029',
    'offseason_grade': 'B+',
    'key_philosophy': 'Complete rebuild around Jaxson Dart with veteran bridge'
}

if __name__ == "__main__":
    print(f"New York Giants 2025 Offseason: {GIANTS_2025_SUMMARY['total_moves']} moves")
    print(f"Offseason Grade: {GIANTS_2025_SUMMARY['offseason_grade']}")
    print(f"Championship Window: {GIANTS_2025_SUMMARY['championship_window']}")
    print(f"Dead Money: ${GIANTS_2025_SUMMARY['dead_money']:,}")
    print(f"Philosophy: {GIANTS_2025_SUMMARY['key_philosophy']}")
    print(f"Key Additions: Wilson (QB), Dart (QB draft), Carter (EDGE), Holland (S)")
    print(f"Key Losses: Jones (released), Ojulari/Jackson (to Eagles)")
    print(f"Strategy: Patient rebuild with franchise QB development")
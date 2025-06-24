"""
Dallas Cowboys 2025 Offseason Moves
Jerry Jones' calculated response to playoff miss with coaching overhaul
Last Updated: June 23, 2025
"""

COWBOYS_2025_MOVES = [
    # ========== FREE AGENT SIGNINGS - Conservative approach ==========
    {
        'player_name': 'Javonte Williams',
        'position': 'RB',
        'from_team': 'Den',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 3500000,
        'guaranteed_money': 2000000,
        'aav': 3500000,
        '2024_grade': 6.8,  # 1,287 yards from scrimmage over 2 years
        'projected_2025_grade': 7.0,
        'snap_percentage_2024': 55.0,
        'importance_to_old_team': 6.5,
        'importance_to_new_team': 7.5,  # Replace Dowdle
        'impact_score': 1.0,
    },
    {
        'player_name': 'Miles Sanders',
        'position': 'RB',
        'from_team': 'Car',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2000000,
        'guaranteed_money': 1000000,
        'aav': 2000000,
        '2024_grade': 5.5,  # Career-low 205 rushing yards
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 5.5,  # Depth signing
        'impact_score': 0.3,
    },
    {
        'player_name': 'Solomon Thomas',
        'position': 'DT',
        'from_team': 'NYJ',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 2,
        'contract_value': 8000000,
        'guaranteed_money': 4000000,
        'aav': 4000000,
        '2024_grade': 6.5,  # 8.5 sacks, 14 TFL in 3 years
        'projected_2025_grade': 6.8,  # Dallas native
        'snap_percentage_2024': 45.0,
        'importance_to_old_team': 6.0,
        'importance_to_new_team': 7.0,  # Reunites with DL coach
        'impact_score': 0.8,
    },
    {
        'player_name': 'Jack Sanborn',
        'position': 'LB',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2500000,
        'guaranteed_money': 1200000,
        'aav': 2500000,
        '2024_grade': 6.0,
        'projected_2025_grade': 6.5,  # Knows Eberflus system
        'snap_percentage_2024': 40.0,
        'importance_to_old_team': 5.5,
        'importance_to_new_team': 6.5,  # System familiarity
        'impact_score': 0.5,
    },
    {
        'player_name': 'Payton Turner',
        'position': 'DE',
        'from_team': 'NO',
        'to_team': 'Dal',
        'move_type': 'Free Agent Signing',
        'contract_years': 1,
        'contract_value': 2800000,
        'guaranteed_money': 1500000,
        'aav': 2800000,
        '2024_grade': 5.5,  # Injury-plagued former 1st rounder
        'projected_2025_grade': 6.0,
        'snap_percentage_2024': 25.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 5.5,  # Reclamation project
        'impact_score': 0.3,
    },
    {
        'player_name': 'Dante Fowler Jr.',
        'position': 'DE',
        'from_team': 'Was',
        'to_team': 'Dal',
        'move_type': 'Re-signing',
        'contract_years': 1,
        'contract_value': 6000000,
        'guaranteed_money': 5000000,
        'aav': 6000000,
        '2024_grade': 7.8,  # 10.5 sacks with Washington
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,  # Proven pass rusher
        'impact_score': 1.5,
    },

    # ========== MAJOR LOSSES ==========
    {
        'player_name': 'DeMarcus Lawrence',
        'position': 'DE',
        'from_team': 'Dal',
        'to_team': 'Sea',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 6.0,  # Limited to 4 games, foot injury
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 20.0,  # Injury-limited
        'importance_to_old_team': 8.0,  # 11-year franchise icon
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Leadership + production loss
    },
    {
        'player_name': 'Jourdan Lewis',
        'position': 'CB',
        'from_team': 'Dal',
        'to_team': 'Jac',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Career-high 71 tackles
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 8.5,  # NFL's highest-paid nickel
        'importance_to_new_team': 0.0,
        'impact_score': -1.8,  # Major secondary loss
    },
    {
        'player_name': 'Rico Dowdle',
        'position': 'RB',
        'from_team': 'Dal',
        'to_team': 'Car',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 8.2,  # First UDFA in Cowboys history with 1,000+ yards
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 8.5,  # 1,079 yards, 39 catches
        'importance_to_new_team': 0.0,
        'impact_score': -2.0,  # Primary back loss
    },
    {
        'player_name': 'Chauncey Golston',
        'position': 'EDGE',
        'from_team': 'Dal',
        'to_team': 'NYG',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.0,  # Career-highs: 56 tackles, 5.5 sacks
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 60.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 0.0,
        'impact_score': -1.2,  # Division rival signing
    },
    {
        'player_name': 'Brandin Cooks',
        'position': 'WR1',
        'from_team': 'Dal',
        'to_team': 'NO',
        'move_type': 'Free Agent Loss',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 7.5,  # Veteran production
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 0.0,
        'impact_score': -1.5,
    },
    {
        'player_name': 'Zack Martin',
        'position': 'RG',
        'from_team': 'Dal',
        'to_team': 'RETIRED',
        'move_type': 'Retirement',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': -9400000,  # Dead cap
        'aav': 0,
        '2024_grade': 8.0,  # Still elite at 34
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 9.0,  # Future HOF, 7x All-Pro
        'importance_to_new_team': 0.0,
        'impact_score': -2.5,  # Massive loss
    },

    # ========== TRADES - Strategic acquisitions ==========
    {
        'player_name': 'George Pickens',
        'position': 'WR1',
        'from_team': 'Pit',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 8000000,  # Remaining on rookie deal
        'guaranteed_money': 8000000,
        'aav': 8000000,
        '2024_grade': 7.8,  # 59 catches, 900 yards
        'projected_2025_grade': 8.2,  # Compared to Dez Bryant
        'snap_percentage_2024': 85.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 9.0,  # Marquee acquisition
        'impact_score': 2.5,  # Major offensive upgrade
        'notes': 'Traded 2026 3rd + 2027 5th for Pickens + 2027 6th'
    },
    {
        'player_name': 'Kenneth Murray Jr.',
        'position': 'LB',
        'from_team': 'Ten',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 15500000,  # Existing deal
        'guaranteed_money': 8000000,
        'aav': 15500000,
        '2024_grade': 7.0,  # 95 tackles, 3.5 sacks
        'projected_2025_grade': 7.2,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.0,
        'importance_to_new_team': 7.5,
        'impact_score': 1.2,
        'notes': 'Traded 2025 6th for Murray + 7th'
    },
    {
        'player_name': 'Joe Milton III',
        'position': 'QB',
        'from_team': 'NE',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 3,
        'contract_value': 3000000,
        'guaranteed_money': 1500000,
        'aav': 1000000,
        '2024_grade': 5.5,  # Limited action
        'projected_2025_grade': 6.0,  # Dallas native
        'snap_percentage_2024': 5.0,
        'importance_to_old_team': 4.0,
        'importance_to_new_team': 5.5,  # Backup QB
        'impact_score': 0.3,
        'notes': 'Traded 5th comp pick for Milton + 7th'
    },
    {
        'player_name': 'Kaiir Elam',
        'position': 'CB',
        'from_team': 'Buf',
        'to_team': 'Dal',
        'move_type': 'Trade',
        'contract_years': 1,
        'contract_value': 3000000,
        'guaranteed_money': 2000000,
        'aav': 3000000,
        '2024_grade': 6.0,  # Former 1st rounder
        'projected_2025_grade': 6.5,  # Change of scenery
        'snap_percentage_2024': 30.0,
        'importance_to_old_team': 5.0,
        'importance_to_new_team': 7.0,  # CB depth with Diggs injury
        'impact_score': 0.8,
        'notes': 'Traded 5th + 2026 7th for Elam + 6th'
    },

    # ========== 2025 NFL DRAFT ==========
    {
        'player_name': 'Tyler Booker',
        'position': 'G',
        'from_team': 'Alabama',
        'to_team': 'Dal',
        'move_type': '2025 Draft - Round 1, Pick 12',
        'contract_years': 4,
        'contract_value': 20000000,
        'guaranteed_money': 20000000,
        'aav': 5000000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.8,  # Direct Martin replacement
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,  # Immediate starter at RG
        'impact_score': 2.2,
    },
    {
        'player_name': 'Donovan Ezeiruaku',
        'position': 'EDGE',
        'from_team': 'Boston College',
        'to_team': 'Dal',
        'move_type': '2025 Draft - Round 2, Pick 44',
        'contract_years': 4,
        'contract_value': 8500000,
        'guaranteed_money': 4500000,
        'aav': 2125000,
        '2024_grade': 0.0,
        'projected_2025_grade': 7.5,  # Led ACC with 16.5 sacks
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.0,  # Replace Lawrence production
        'impact_score': 1.5,
    },
    {
        'player_name': 'Shavon Revel Jr.',
        'position': 'CB',
        'from_team': 'East Carolina',
        'to_team': 'Dal',
        'move_type': '2025 Draft - Round 3, Pick 76',
        'contract_years': 4,
        'contract_value': 5500000,
        'guaranteed_money': 1200000,
        'aav': 1375000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,  # 6'3" press-man corner
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.5,  # Diggs injury insurance
        'impact_score': 1.0,
        'notes': 'Recovering from torn ACL'
    },
    {
        'player_name': 'Jaydon Blue',
        'position': 'RB',
        'from_team': 'Texas',
        'to_team': 'Dal',
        'move_type': '2025 Draft - Round 5, Pick 149',
        'contract_years': 4,
        'contract_value': 3800000,
        'guaranteed_money': 600000,
        'aav': 950000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.5,  # 4.38 speed
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 6.5,
        'impact_score': 0.5,
    },
    {
        'player_name': 'Shemar James',
        'position': 'LB',
        'from_team': 'Florida',
        'to_team': 'Dal',
        'move_type': '2025 Draft - Round 5, Pick 152 (via trade)',
        'contract_years': 4,
        'contract_value': 3700000,
        'guaranteed_money': 550000,
        'aav': 925000,
        '2024_grade': 0.0,
        'projected_2025_grade': 6.8,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 7.0,
        'impact_score': 0.6,
        'notes': 'Traded up using picks 174 + 204'
    },

    # ========== KEY RE-SIGNINGS/EXTENSIONS ==========
    {
        'player_name': 'Osa Odighizuwa',
        'position': 'DT',
        'from_team': 'Dal',
        'to_team': 'Dal',
        'move_type': 'Contract Extension',
        'contract_years': 4,
        'contract_value': 80000000,
        'guaranteed_money': 45000000,
        'aav': 20000000,
        '2024_grade': 8.5,  # Breakout season
        'projected_2025_grade': 8.5,
        'snap_percentage_2024': 75.0,
        'importance_to_old_team': 9.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.5,  # Cornerstone signing
    },
    {
        'player_name': 'Markquese Bell',
        'position': 'S',
        'from_team': 'Dal',
        'to_team': 'Dal',
        'move_type': 'Contract Extension',
        'contract_years': 3,
        'contract_value': 12000000,
        'guaranteed_money': 6000000,
        'aav': 4000000,
        '2024_grade': 7.2,  # 102 tackles in hybrid role
        'projected_2025_grade': 7.5,
        'snap_percentage_2024': 80.0,
        'importance_to_old_team': 7.5,
        'importance_to_new_team': 8.0,
        'impact_score': 1.2,
    },

    # ========== COACHING CHANGES - Major overhaul ==========
    {
        'player_name': 'Mike McCarthy',
        'position': 'COACH-HC',
        'from_team': 'Dal',
        'to_team': 'FIRED',
        'move_type': 'Coaching Departure',
        'contract_years': 0,
        'contract_value': 0,
        'guaranteed_money': 0,
        'aav': 0,
        '2024_grade': 4.0,  # 49-35 regular season, 1-3 playoffs
        'projected_2025_grade': 0.0,
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 3.0,  # Lost locker room
        'importance_to_new_team': 0.0,
        'impact_score': 1.0,  # Addition by subtraction
    },
    {
        'player_name': 'Brian Schottenheimer',
        'position': 'COACH-HC',
        'from_team': 'Dal-OC',
        'to_team': 'Dal',
        'move_type': 'Internal Promotion to HC',
        'contract_years': 4,
        'contract_value': 20000000,
        'guaranteed_money': 12000000,
        'aav': 5000000,
        '2024_grade': 7.0,  # As OC
        'projected_2025_grade': 7.5,  # First-time HC
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 9.0,
        'impact_score': 2.0,  # Continuity + change balance
    },
    {
        'player_name': 'Matt Eberflus',
        'position': 'COACH-DC',
        'from_team': 'Chi',
        'to_team': 'Dal',
        'move_type': 'Defensive Coordinator Hire',
        'contract_years': 3,
        'contract_value': 6000000,
        'guaranteed_money': 3000000,
        'aav': 2000000,
        '2024_grade': 6.5,  # Fired as Bears HC
        'projected_2025_grade': 8.0,  # Returns to DC role, Dallas history
        'snap_percentage_2024': 0.0,
        'importance_to_old_team': 0.0,
        'importance_to_new_team': 8.5,  # Coordinator overhaul
        'impact_score': 1.8,
    },
]

# ========== SUMMARY METRICS ==========
COWBOYS_2025_SUMMARY = {
    'total_moves': len(COWBOYS_2025_MOVES),
    'free_agent_signings': 6,
    'major_losses': 7,
    'draft_picks': 9,
    'key_resignings': 2,
    'trades': 4,
    'coaching_changes': 3,
    'total_guaranteed_money': 135000000,  # Includes Odighizuwa extension
    'dead_money': 16600000,  # Martin retirement + others
    'salary_cap_space_remaining': 38500000,
    'championship_window': '2025-2026',
    'offseason_grade': 'B+',
    'key_philosophy': 'Conservative approach with strategic trades and coaching overhaul',
    'net_impact_score': 7.5,  # Sum of all impact scores
    'division_outlook': 'Contender but questions at QB and defense',
}

# ========== KEY STRATEGIC NOTES ==========
STRATEGIC_ANALYSIS = {
    'jerry_jones_approach': {
        'initial_promise': 'Suggested being selectively aggressive',
        'reality': 'Maintained conservative free agency approach',
        'quote': "I don't think aggressive is the right word",
        'philosophy': 'Build through draft and trades, not FA',
    },
    'quarterback_situation': {
        'prescott_status': 'Extension talks ongoing, $60M cap hit',
        'backup_battle': 'Milton III vs Will Grier',
        'injury_concern': 'Prescott coming off hamstring surgery',
        'timeline': 'Win-now mode with Prescott',
    },
    'offensive_changes': {
        'pickens_impact': 'Compared to Dez Bryant by Stephen Jones',
        'rb_committee': 'Williams/Sanders/Blue replace Dowdle',
        'o_line_transition': 'Booker replaces HOF Martin',
        'lamb_usage': 'Expected to see more diverse routes',
    },
    'defensive_overhaul': {
        'eberflus_return': 'Previously Dallas LB coach 2011-2017',
        'scheme_change': 'From Quinn 3-4 to Eberflus 4-3',
        'personnel_fit': 'Parsons perfect for new system',
        'secondary_concern': 'Diggs recovery + Lewis departure',
    },
    'injury_situations': {
        'diggs_status': 'May miss start of 2025 (knee surgery)',
        'overshown_timeline': 'Targeting Week 13 return (ACL/MCL/PCL)',
        'parsons_health': 'Fully recovered from 2024 injuries',
        'team_total': 'Lost 46% of cap to injuries in 2024',
    },
}

# ========== POSITION GROUP ANALYSIS ==========
POSITION_GROUPS = {
    'quarterback': {
        'starter': 'Dak Prescott',
        'backup': 'Joe Milton III',
        'third': 'Will Grier',
        'grade': 'B+',
        'notes': 'Prescott health crucial, Milton provides mobility',
    },
    'offensive_line': {
        'starters': ['Tyron Smith (LT)', 'Tyler Smith (LG)', 'Brock Hoffman (C)', 
                     'Tyler Booker (RG)', 'Terence Steele (RT)'],
        'depth_concern': 'Lost Moore Jr. and Edoga',
        'grade': 'B',
        'notes': 'Booker must replace HOF Martin immediately',
    },
    'skill_positions': {
        'wr': 'CeeDee Lamb, George Pickens, Jalen Tolbert',
        'rb': 'Javonte Williams, Miles Sanders, Jaydon Blue',
        'te': 'Jake Ferguson, Luke Schoonmaker',
        'grade': 'A-',
        'notes': 'Pickens adds explosive element opposite Lamb',
    },
    'pass_rush': {
        'starters': ['Micah Parsons', 'Donovan Ezeiruaku', 'DeMarcus Lawrence (lost)'],
        'depth': ['Dante Fowler Jr.', 'Payton Turner'],
        'grade': 'B+',
        'notes': 'Parsons extension talks ongoing ($30M+ AAV expected)',
    },
    'secondary': {
        'corners': ['Trevon Diggs (injured)', 'DaRon Bland', 'Kaiir Elam'],
        'safeties': ['Malik Hooker', 'Markquese Bell', 'Donovan Wilson'],
        'grade': 'B-',
        'notes': 'Major questions with Diggs injury, Lewis departure',
    },
}

# ========== BETTING IMPLICATIONS ==========
BETTING_OUTLOOK = {
    'win_total': {
        'projection': 9.5,
        'lean': 'UNDER',
        'reasoning': 'Coaching transition + defensive questions',
    },
    'division_odds': {
        'current': '+250',
        'value': 'SLIGHT VALUE',
        'reasoning': 'Eagles vulnerable but Cowboys have holes',
    },
    'super_bowl_odds': {
        'current': '+2500',
        'value': 'PASS',
        'reasoning': 'Too many question marks for deep run',
    },
    'player_props': {
        'prescott_passing_yards': 'OVER 4,100',
        'pickens_receiving_yards': 'OVER 1,000',
        'parsons_sacks': 'OVER 13.5',
    },
    'key_angles': {
        'best_bet': 'Pickens 1,000+ yards',
        'fade_spot': 'Week 1 if Diggs out',
        'narrative': 'Schottenheimer honeymoon short',
    },
}

def generate_summary_report():
    """Generate a comprehensive offseason summary"""
    
    print("=" * 70)
    print("DALLAS COWBOYS 2025 OFFSEASON ANALYSIS")
    print("=" * 70)
    
    print(f"\nOFFSEASON GRADE: {COWBOYS_2025_SUMMARY['offseason_grade']}")
    print(f"Net Impact Score: +{COWBOYS_2025_SUMMARY['net_impact_score']}")
    print(f"Championship Window: {COWBOYS_2025_SUMMARY['championship_window']}")
    
    print("\n📊 MOVES BREAKDOWN:")
    print(f"  • Total Moves: {COWBOYS_2025_SUMMARY['total_moves']}")
    print(f"  • Free Agent Signings: {COWBOYS_2025_SUMMARY['free_agent_signings']} (conservative)")
    print(f"  • Trades: {COWBOYS_2025_SUMMARY['trades']} (strategic approach)")
    print(f"  • Draft Picks: {COWBOYS_2025_SUMMARY['draft_picks']}")
    print(f"  • Coaching Changes: {COWBOYS_2025_SUMMARY['coaching_changes']}")
    
    print("\n💰 FINANCIAL SUMMARY:")
    print(f"  • Total Guaranteed: ${COWBOYS_2025_SUMMARY['total_guaranteed_money']:,}")
    print(f"  • Dead Money: ${COWBOYS_2025_SUMMARY['dead_money']:,}")
    print(f"  • Cap Space: ${COWBOYS_2025_SUMMARY['salary_cap_space_remaining']:,}")
    print(f"  • Parsons Extension: Looming ($30M+ AAV expected)")
    
    print("\n🎯 KEY ADDITIONS:")
    print("  • George Pickens (WR) - Trade from Pittsburgh")
    print("  • Tyler Booker (G) - 1st round pick, Martin replacement")
    print("  • Brian Schottenheimer (HC) - Internal promotion")
    print("  • Matt Eberflus (DC) - Returns to Dallas")
    
    print("\n❌ KEY LOSSES:")
    print("  • Mike McCarthy (HC) - Fired after 7-10 season")
    print("  • DeMarcus Lawrence (DE) - 3yr/$42M to Seattle")
    print("  • Jourdan Lewis (CB) - 3yr/$30M to Jacksonville")
    print("  • Rico Dowdle (RB) - 1,079 yard rusher to Carolina")
    print("  • Zack Martin (RG) - Retirement, future HOF")
    
    print("\n📈 STRATEGIC OUTLOOK:")
    print(f"  • Philosophy: {COWBOYS_2025_SUMMARY['key_philosophy']}")
    print(f"  • Division Outlook: {COWBOYS_2025_SUMMARY['division_outlook']}")
    print(f"  • Scheme Change: Quinn 3-4 to Eberflus 4-3")
    print(f"  • Risk: First-time HC with aging core")
    
    print("\n🎰 BETTING IMPLICATIONS:")
    print(f"  • Win Total O/U 9.5: {BETTING_OUTLOOK['win_total']['lean']}")
    print(f"  • Division Odds {BETTING_OUTLOOK['division_odds']['current']}: {BETTING_OUTLOOK['division_odds']['value']}")
    print(f"  • Best Prop: {BETTING_OUTLOOK['key_angles']['best_bet']}")
    
    print("\n⚠️  CRITICAL FACTORS:")
    print("  • Prescott health after hamstring surgery")
    print("  • Diggs may miss start of season (knee)")
    print("  • Schottenheimer's HC learning curve")
    print("  • Can Booker replace HOF Martin?")

if __name__ == "__main__":
    generate_summary_report()
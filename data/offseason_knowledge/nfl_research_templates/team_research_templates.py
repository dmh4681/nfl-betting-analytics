"""
NFL Team Research Templates - All 32 Teams
Structured for both human use and AI agent parsing
Updated: June 2025
"""

RESEARCH_TEMPLATES = {
    "AFC_EAST": {
        "NE": {
            "team_name": "New England Patriots",
            "priority_sources": [
                "Patriots.com/news/transactions",
                "@MikeReiss",
                "Boston Globe Patriots",
                "PFF Patriots roster"
            ],
            "key_search_terms": [
                "Patriots sign",
                "Patriots release", 
                "Patriots trade",
                "Patriots claim"
            ],
            "focus_areas": [
                "Drake Maye protection (OL)",
                "WR depth behind main corps",
                "Defensive line depth",
                "Special teams changes",
                "Mike Vrabel coaching staff"
            ],
            "beat_reporters": ["@MikeReiss", "@PhilAPerry", "@ZackCoxNESN"],
            "current_priorities": [
                "OL_health",
                "rookie_QB_support", 
                "defensive_youth"
            ]
        },
        "BUF": {
            "team_name": "Buffalo Bills",
            "priority_sources": [
                "BuffaloBills.com",
                "@JoeBuscaglia",
                "Buffalo News",
                "Bills Mafia Twitter"
            ],
            "key_search_terms": [
                "Bills sign",
                "Bills waive",
                "Bills claim",
                "Bills promote"
            ],
            "focus_areas": [
                "Josh Allen supporting cast",
                "Pass rush depth (post-Von Miller)",
                "WR additions beyond main group", 
                "OL depth and competition",
                "AFC East competitive responses"
            ],
            "beat_reporters": ["@JoeBuscaglia", "@SalSports", "@mattbove"],
            "current_priorities": [
                "championship_window_moves",
                "depth_preservation",
                "AFC_title_defense"
            ]
        },
        "MIA": {
            "team_name": "Miami Dolphins", 
            "priority_sources": [
                "MiamiDolphins.com",
                "@CameronWolfe",
                "Miami Herald Dolphins",
                "The Athletic Dolphins"
            ],
            "key_search_terms": [
                "Dolphins sign",
                "Dolphins release",
                "Dolphins acquire",
                "Dolphins claim"
            ],
            "focus_areas": [
                "Tua Tagovailoa protection (critical)",
                "Defensive line depth",
                "WR depth chart changes",
                "Special teams improvements",
                "Mike McDaniel offensive additions"
            ],
            "beat_reporters": ["@CameronWolfe", "@AdamHBeasley", "@OmarKelly"],
            "current_priorities": [
                "QB_protection",
                "playoff_push",
                "health_management"
            ]
        },
        "NYJ": {
            "team_name": "New York Jets",
            "priority_sources": [
                "NewYorkJets.com", 
                "@RichCimini",
                "Jets beat reporters Twitter",
                "Gang Green Nation"
            ],
            "key_search_terms": [
                "Jets sign",
                "Jets cut", 
                "Jets claim",
                "Jets elevate"
            ],
            "focus_areas": [
                "Aaron Glenn defensive system",
                "Justin Fields supporting cast",
                "OL continuity and depth",
                "Culture change indicators",
                "Veteran leadership additions"
            ],
            "beat_reporters": ["@RichCimini", "@BrianCoz", "@ZackBlatt"],
            "current_priorities": [
                "culture_reset",
                "QB_development",
                "defensive_system"
            ]
        }
    },
    
    "AFC_NORTH": {
        "BAL": {
            "team_name": "Baltimore Ravens",
            "priority_sources": [
                "BaltimoreRavens.com",
                "@jamisonhensley", 
                "Baltimore Banner Ravens",
                "@PressBoxOnline"
            ],
            "key_search_terms": [
                "Ravens sign",
                "Ravens waive",
                "Ravens promote",
                "Ravens elevate"
            ],
            "focus_areas": [
                "Lamar Jackson weapons/protection",
                "Pass defense improvements (2024 weakness)",
                "OL depth behind starters",
                "EDGE depth beyond main guys",
                "AFC North arms race responses"
            ],
            "beat_reporters": ["@jamisonhensley", "@jeffzrebiec", "@RyanMink"],
            "current_priorities": [
                "division_title_defense",
                "playoff_edge_improvement",
                "championship_window"
            ]
        },
        "PIT": {
            "team_name": "Pittsburgh Steelers",
            "priority_sources": [
                "Steelers.com",
                "@MarkKaboly",
                "Pittsburgh Post-Gazette", 
                "Steel Curtain Rising"
            ],
            "key_search_terms": [
                "Steelers sign",
                "Steelers release",
                "Steelers work out",
                "Steelers claim"
            ],
            "focus_areas": [
                "DK Metcalf integration",
                "QB situation developments",
                "OL depth after departures", 
                "Defensive system fits",
                "Aaron Rodgers situation updates"
            ],
            "beat_reporters": ["@MarkKaboly", "@gerrydulac", "@RyanBurr"],
            "current_priorities": [
                "QB_clarity",
                "playoff_push",
                "division_competition"
            ]
        },
        "CIN": {
            "team_name": "Cincinnati Bengals",
            "priority_sources": [
                "Bengals.com",
                "@pauldehnerjr",
                "Cincinnati Enquirer",
                "Bengals beat Twitter"
            ],
            "key_search_terms": [
                "Bengals sign",
                "Bengals claim", 
                "Bengals release",
                "Bengals promote"
            ],
            "focus_areas": [
                "Joe Burrow protection",
                "Al Golden defensive overhaul",
                "Trey Hendrickson situation",
                "OL health and depth",
                "WR depth behind big 3"
            ],
            "beat_reporters": ["@pauldehnerjr", "@kelseyyconway", "@TonyPike"],
            "current_priorities": [
                "championship_window",
                "defensive_improvement", 
                "contract_situations"
            ]
        },
        "CLE": {
            "team_name": "Cleveland Browns",
            "priority_sources": [
                "ClevelandBrowns.com",
                "@MaryKayCabot",
                "Cleveland Plain Dealer",
                "Dawgs By Nature"
            ],
            "key_search_terms": [
                "Browns sign",
                "Browns waive",
                "Browns promote",
                "Browns claim"
            ],
            "focus_areas": [
                "QB room developments",
                "Kevin Stefanski offensive moves",
                "Myles Garrett supporting cast",
                "Defensive depth behind stars",
                "Culture/leadership moves"
            ],
            "beat_reporters": ["@MaryKayCabot", "@ScottPetrak", "@TonyGrossi"],
            "current_priorities": [
                "competitive_timeline",
                "QB_situation",
                "playoff_return"
            ]
        }
    },
    
    "AFC_SOUTH": {
        "HOU": {
            "team_name": "Houston Texans",
            "priority_sources": [
                "HoustonTexans.com",
                "@MarkBermanFox26",
                "Houston Chronicle Sports",
                "Battle Red Blog"
            ],
            "key_search_terms": [
                "Texans sign",
                "Texans release",
                "Texans claim",
                "Texans promote"
            ],
            "focus_areas": [
                "C.J. Stroud protection moves",
                "Nick Caley offensive system",
                "OL after major changes",
                "Pass rush depth",
                "Secondary improvements"
            ],
            "beat_reporters": ["@MarkBermanFox26", "@AaronWilson_NFL", "@DeepSlant"],
            "current_priorities": [
                "title_defense",
                "OL_stabilization",
                "playoff_depth"
            ]
        },
        "IND": {
            "team_name": "Indianapolis Colts",
            "priority_sources": [
                "Colts.com",
                "@JimIrsay",
                "Indianapolis Star",
                "Stampede Blue"
            ],
            "key_search_terms": [
                "Colts sign",
                "Colts cut",
                "Colts work out",
                "Colts claim"
            ],
            "focus_areas": [
                "Anthony Richardson development",
                "Shane Steichen offensive moves",
                "Lou Anarumo defensive system",
                "QB development support",
                "Veteran leadership additions"
            ],
            "beat_reporters": ["@JimIrsay", "@joelaerickson", "@zkeefer"],
            "current_priorities": [
                "QB_development",
                "defensive_installation",
                "playoff_return"
            ]
        },
        "TEN": {
            "team_name": "Tennessee Titans",
            "priority_sources": [
                "TennesseeTitans.com",
                "@PaulKuharskyNFL",
                "Tennessean Titans",
                "Music City Miracles"
            ],
            "key_search_terms": [
                "Titans sign",
                "Titans release",
                "Titans promote",
                "Titans claim"
            ],
            "focus_areas": [
                "Cam Ward integration",
                "Brian Callahan offensive system",
                "QB room support for Ward",
                "OL protection schemes",
                "Defensive youth movement"
            ],
            "beat_reporters": ["@PaulKuharskyNFL", "@turrondaradio", "@glennonsports"],
            "current_priorities": [
                "rookie_QB_development",
                "culture_establishment",
                "rebuild_timeline"
            ]
        },
        "JAC": {
            "team_name": "Jacksonville Jaguars",
            "priority_sources": [
                "Jaguars.com",
                "@JohnReid64",
                "Jacksonville.com",
                "Big Cat Country"
            ],
            "key_search_terms": [
                "Jaguars sign",
                "Jaguars waive",
                "Jaguars claim",
                "Jaguars promote"
            ],
            "focus_areas": [
                "Trevor Lawrence weapons",
                "Liam Coen offensive system",
                "Travis Hunter development",
                "Offensive system installation",
                "Young player development"
            ],
            "beat_reporters": ["@JohnReid64", "@phillip_heilman", "@DanHickEN"],
            "current_priorities": [
                "turnaround_effort",
                "system_installation",
                "youth_development"
            ]
        }
    },
    
    "AFC_WEST": {
        "KC": {
            "team_name": "Kansas City Chiefs",
            "priority_sources": [
                "Chiefs.com",
                "@AdamSchefter",
                "Kansas City Star",
                "Arrowhead Pride"
            ],
            "key_search_terms": [
                "Chiefs sign",
                "Chiefs release",
                "Chiefs elevate",
                "Chiefs claim"
            ],
            "focus_areas": [
                "Patrick Mahomes weapons",
                "Andy Reid system moves",
                "Steve Spagnuolo defensive adds",
                "WR depth and speed",
                "Cap management moves"
            ],
            "beat_reporters": ["@CharlesGoldman", "@mattderrick", "@BroHahn"],
            "current_priorities": [
                "three_peat_push",
                "championship_window",
                "cap_management"
            ]
        },
        "LAC": {
            "team_name": "Los Angeles Chargers",
            "priority_sources": [
                "Chargers.com",
                "@danielpopper",
                "San Diego Union-Tribune",
                "Bolt Beat"
            ],
            "key_search_terms": [
                "Chargers sign",
                "Chargers cut",
                "Chargers promote",
                "Chargers claim"
            ],
            "focus_areas": [
                "Justin Herbert supporting cast",
                "Jim Harbaugh culture moves",
                "Running game additions",
                "OL depth and health",
                "Defensive depth preservation"
            ],
            "beat_reporters": ["@danielpopper", "@KrisRhim", "@ChargersWire"],
            "current_priorities": [
                "playoff_push",
                "harbaugh_culture",
                "AFC_west_competition"
            ]
        },
        "DEN": {
            "team_name": "Denver Broncos",
            "priority_sources": [
                "DenverBroncos.com",
                "@RyanKoenigsberg",
                "Denver Post Broncos",
                "Mile High Report"
            ],
            "key_search_terms": [
                "Broncos sign",
                "Broncos waive",
                "Broncos claim",
                "Broncos promote"
            ],
            "focus_areas": [
                "Bo Nix development support",
                "Sean Payton offensive moves",
                "Vance Joseph defensive depth",
                "QB development tools",
                "Veteran leadership"
            ],
            "beat_reporters": ["@RyanKoenigsberg", "@ParkerGabriel", "@MaseDenver"],
            "current_priorities": [
                "QB_development",
                "competitive_window",
                "playoff_contention"
            ]
        },
        "LV": {
            "team_name": "Las Vegas Raiders",
            "priority_sources": [
                "Raiders.com",
                "@VinnyBonsignore",
                "Las Vegas Review-Journal",
                "Silver and Black Pride"
            ],
            "key_search_terms": [
                "Raiders sign",
                "Raiders release",
                "Raiders work out",
                "Raiders claim"
            ],
            "focus_areas": [
                "Geno Smith integration",
                "Pete Carroll culture installation",
                "Ashton Jeanty development",
                "QB room stability",
                "Young player development"
            ],
            "beat_reporters": ["@VinnyBonsignore", "@TamikaLCatchings", "@MykLScott"],
            "current_priorities": [
                "rebuild_effort",
                "culture_installation",
                "youth_development"
            ]
        }
    },
    
    "NFC_EAST": {
        "DAL": {
            "team_name": "Dallas Cowboys",
            "priority_sources": [
                "DallasCowboys.com",
                "@toddarcher",
                "Dallas Morning News",
                "Blogging The Boys"
            ],
            "key_search_terms": [
                "Cowboys sign",
                "Cowboys release",
                "Cowboys elevate",
                "Cowboys claim"
            ],
            "focus_areas": [
                "Dak Prescott supporting cast",
                "Brian Schottenheimer system",
                "Jerry Jones decisions",
                "WR depth after changes",
                "Cap management moves"
            ],
            "beat_reporters": ["@toddarcher", "@clarencehilljr", "@MikeFisher"],
            "current_priorities": [
                "playoff_hopes",
                "system_installation",
                "roster_optimization"
            ]
        },
        "NYG": {
            "team_name": "New York Giants",
            "priority_sources": [
                "Giants.com",
                "@jordanraanan",
                "New York Post Giants",
                "Big Blue View"
            ],
            "key_search_terms": [
                "Giants sign",
                "Giants cut",
                "Giants claim",
                "Giants promote"
            ],
            "focus_areas": [
                "Jaxson Dart development",
                "Brian Daboll offensive moves",
                "Defensive youth movement",
                "QB development support",
                "Culture building"
            ],
            "beat_reporters": ["@jordanraanan", "@art_stapleton", "@DDuggan21"],
            "current_priorities": [
                "rebuild_timeline",
                "QB_development",
                "youth_movement"
            ]
        },
        "PHI": {
            "team_name": "Philadelphia Eagles",
            "priority_sources": [
                "PhiladelphiaEagles.com",
                "@EliotShorrParks",
                "Philadelphia Inquirer",
                "Bleeding Green Nation"
            ],
            "key_search_terms": [
                "Eagles sign",
                "Eagles release",
                "Eagles promote",
                "Eagles claim"
            ],
            "focus_areas": [
                "Jalen Hurts weapons",
                "Vic Fangio defensive system",
                "Youth development",
                "Defensive youth integration",
                "Offensive continuity"
            ],
            "beat_reporters": ["@EliotShorrParks", "@Jeff_McLane", "@ZBerm"],
            "current_priorities": [
                "title_defense",
                "youth_integration",
                "championship_window"
            ]
        },
        "WAS": {
            "team_name": "Washington Commanders",
            "priority_sources": [
                "Commanders.com",
                "@john_keim",
                "Washington Post Commanders",
                "Hogs Haven"
            ],
            "key_search_terms": [
                "Commanders sign",
                "Commanders waive",
                "Commanders claim",
                "Commanders promote"
            ],
            "focus_areas": [
                "Jayden Daniels supporting cast",
                "Dan Quinn defensive moves",
                "Offensive weapon additions",
                "QB protection and weapons",
                "Culture establishment"
            ],
            "beat_reporters": ["@john_keim", "@nicki_jhabvala", "@MikeGarafolo"],
            "current_priorities": [
                "playoff_defense",
                "QB_support",
                "competitive_sustainability"
            ]
        }
    },
    
    "NFC_NORTH": {
        "CHI": {
            "team_name": "Chicago Bears",
            "priority_sources": [
                "ChicagoBears.com",
                "@BradBiggs",
                "Chicago Sun-Times",
                "Windy City Gridiron"
            ],
            "key_search_terms": [
                "Bears sign",
                "Bears cut",
                "Bears elevate",
                "Bears claim"
            ],
            "focus_areas": [
                "Caleb Williams development",
                "Ben Johnson offensive system",
                "Dennis Allen defensive moves",
                "QB development tools",
                "OL health and depth"
            ],
            "beat_reporters": ["@BradBiggs", "@ChiSportUpdates", "@Hub_Arkush"],
            "current_priorities": [
                "QB_transformation",
                "system_installation",
                "competitive_leap"
            ]
        },
        "DET": {
            "team_name": "Detroit Lions",
            "priority_sources": [
                "DetroitLions.com",
                "@davebirkett",
                "Detroit News Lions",
                "Pride of Detroit"
            ],
            "key_search_terms": [
                "Lions sign",
                "Lions release",
                "Lions promote",
                "Lions claim"
            ],
            "focus_areas": [
                "Jared Goff supporting cast",
                "Coordinator transitions",
                "Championship culture",
                "Defensive depth maintenance",
                "Championship window moves"
            ],
            "beat_reporters": ["@davebirkett", "@kmeinke", "@erikschlitt"],
            "current_priorities": [
                "title_defense",
                "coordinator_transitions",
                "championship_culture"
            ]
        },
        "GB": {
            "team_name": "Green Bay Packers",
            "priority_sources": [
                "Packers.com",
                "@RobDemovsky",
                "Green Bay Press-Gazette",
                "Cheesehead TV"
            ],
            "key_search_terms": [
                "Packers sign",
                "Packers waive",
                "Packers claim",
                "Packers promote"
            ],
            "focus_areas": [
                "Jordan Love development",
                "Matt LaFleur offensive moves",
                "Defensive improvements",
                "QB supporting cast",
                "Young player development"
            ],
            "beat_reporters": ["@RobDemovsky", "@mattschneidman", "@WesHod"],
            "current_priorities": [
                "competitive_window",
                "QB_development",
                "NFC_north_competition"
            ]
        },
        "MIN": {
            "team_name": "Minnesota Vikings",
            "priority_sources": [
                "Vikings.com",
                "@CourtneyRCronin",
                "Star Tribune Vikings",
                "Daily Norseman"
            ],
            "key_search_terms": [
                "Vikings sign",
                "Vikings cut",
                "Vikings elevate",
                "Vikings claim"
            ],
            "focus_areas": [
                "J.J. McCarthy development",
                "Kevin O'Connell offensive moves",
                "Defensive depth",
                "OL health after overhaul",
                "Cap management moves"
            ],
            "beat_reporters": ["@CourtneyRCronin", "@Andrew_Krammer", "@DWolfsonKSTP"],
            "current_priorities": [
                "championship_push",
                "QB_development",
                "cap_management"
            ]
        }
    },
    
    "NFC_SOUTH": {
        "ATL": {
            "team_name": "Atlanta Falcons",
            "priority_sources": [
                "AtlantaFalcons.com",
                "@DOrlandoAJC",
                "ESPN Atlanta",
                "The Falcoholic"
            ],
            "key_search_terms": [
                "Falcons sign",
                "Falcons release",
                "Falcons promote",
                "Falcons claim"
            ],
            "focus_areas": [
                "Michael Penix Jr. development",
                "Raheem Morris defensive moves",
                "Young player integration",
                "QB development support",
                "NFC South competition"
            ],
            "beat_reporters": ["@DOrlandoAJC", "@vaughn_mcclure", "@MarlaRidenour"],
            "current_priorities": [
                "division_push",
                "QB_transition",
                "defensive_improvement"
            ]
        },
        "CAR": {
            "team_name": "Carolina Panthers",
            "priority_sources": [
                "Panthers.com",
                "@josephperson",
                "Charlotte Observer Panthers",
                "Cat Scratch Reader"
            ],
            "key_search_terms": [
                "Panthers sign",
                "Panthers waive",
                "Panthers claim",
                "Panthers promote"
            ],
            "focus_areas": [
                "Bryce Young development",
                "Dave Canales offensive system",
                "Defensive rebuild",
                "QB development tools",
                "Culture establishment"
            ],
            "beat_reporters": ["@josephperson", "@dnewtonsports", "@MaxHenson"],
            "current_priorities": [
                "rebuild_timeline",
                "QB_development",
                "defensive_improvement"
            ]
        },
        "NO": {
            "team_name": "New Orleans Saints",
            "priority_sources": [
                "NewOrleansSaints.com",
                "@nick_underhill",
                "Times-Picayune Saints",
                "Canal Street Chronicles"
            ],
            "key_search_terms": [
                "Saints sign",
                "Saints release",
                "Saints elevate",
                "Saints claim"
            ],
            "focus_areas": [
                "Tyler Shough development",
                "Kellen Moore offensive system",
                "Cap management moves",
                "QB room development",
                "Defensive depth"
            ],
            "beat_reporters": ["@nick_underhill", "@LarryHolder", "@MikeTriplett"],
            "current_priorities": [
                "competitive_timeline",
                "cap_optimization",
                "system_installation"
            ]
        },
        "TB": {
            "team_name": "Tampa Bay Buccaneers",
            "priority_sources": [
                "Buccaneers.com",
                "@gregauman",
                "Tampa Bay Times Bucs",
                "Pewter Report"
            ],
            "key_search_terms": [
                "Buccaneers sign",
                "Bucs release",
                "Bucs claim",
                "Bucs promote"
            ],
            "focus_areas": [
                "Baker Mayfield supporting cast",
                "Todd Bowles defensive moves",
                "Division title defense",
                "Offensive continuity",
                "Championship window moves"
            ],
            "beat_reporters": ["@gregauman", "@NFLSTROUD", "@TBTimes_Bucs"],
            "current_priorities": [
                "title_defense",
                "championship_window",
                "NFC_south_dominance"
            ]
        }
    },
    
    "NFC_WEST": {
        "ARI": {
            "team_name": "Arizona Cardinals",
            "priority_sources": [
                "AZCardinals.com",
                "@kentsomers",
                "Arizona Sports Cardinals",
                "Revenge of the Birds"
            ],
            "key_search_terms": [
                "Cardinals sign",
                "Cardinals release",
                "Cardinals elevate",
                "Cardinals claim"
            ],
            "focus_areas": [
                "Kyler Murray health/weapons",
                "Jonathan Gannon defensive moves",
                "Youth development",
                "QB health and support",
                "NFC West competition"
            ],
            "beat_reporters": ["@kentsomers", "@mikejurecki", "@Cardschatter"],
            "current_priorities": [
                "playoff_push",
                "QB_health",
                "defensive_improvement"
            ]
        },
        "LAR": {
            "team_name": "Los Angeles Rams",
            "priority_sources": [
                "TheRams.com",
                "@LindseyThiry",
                "Los Angeles Times Rams",
                "Turf Show Times"
            ],
            "key_search_terms": [
                "Rams sign",
                "Rams release",
                "Rams claim",
                "Rams promote"
            ],
            "focus_areas": [
                "Matthew Stafford supporting cast",
                "Sean McVay offensive moves",
                "Defensive depth",
                "Aging QB supporting cast",
                "Championship window moves"
            ],
            "beat_reporters": ["@LindseyThiry", "@MylesASimmons", "@CameronDaSilva"],
            "current_priorities": [
                "title_defense",
                "championship_window",
                "salary_cap_management"
            ]
        },
        "SF": {
            "team_name": "San Francisco 49ers",
            "priority_sources": [
                "49ers.com",
                "@MaioccoNBCS",
                "San Francisco Chronicle",
                "Niners Nation"
            ],
            "key_search_terms": [
                "49ers sign",
                "49ers waive",
                "49ers promote",
                "49ers claim"
            ],
            "focus_areas": [
                "Brock Purdy supporting cast",
                "Kyle Shanahan offensive moves",
                "Robert Saleh defensive system",
                "Offensive weapon additions",
                "NFC West competition"
            ],
            "beat_reporters": ["@MaioccoNBCS", "@LombardiHimself", "@nwagoner"],
            "current_priorities": [
                "championship_window",
                "youth_integration",
                "salary_cap_optimization"
            ]
        },
        "SEA": {
            "team_name": "Seattle Seahawks",
            "priority_sources": [
                "Seahawks.com",
                "@bcondotta",
                "ESPN Seattle",
                "Field Gulls"
            ],
            "key_search_terms": [
                "Seahawks sign",
                "Seahawks release",
                "Seahawks claim",
                "Seahawks promote"
            ],
            "focus_areas": [
                "Sam Darnold integration",
                "Mike Macdonald defensive moves",
                "Offensive system changes",
                "QB transition support",
                "Young player development"
            ],
            "beat_reporters": ["@bcondotta", "@gbellseattle", "@hawkblogger"],
            "current_priorities": [
                "rebuild_effort",
                "system_installation",
                "youth_development"
            ]
        }
    }
}

# AI Agent Parsing Functions
def get_team_template(team_abbr):
    """Get research template for specific team"""
    for division, teams in RESEARCH_TEMPLATES.items():
        if team_abbr in teams:
            return teams[team_abbr]
    return None

def get_division_teams(division):
    """Get all teams in a division"""
    return RESEARCH_TEMPLATES.get(division, {})

def get_all_beat_reporters():
    """Extract all beat reporter handles for monitoring"""
    reporters = []
    for division in RESEARCH_TEMPLATES.values():
        for team in division.values():
            reporters.extend(team.get('beat_reporters', []))
    return list(set(reporters))

def get_teams_by_priority(priority_type):
    """Get teams matching a specific priority"""
    matching_teams = []
    for division in RESEARCH_TEMPLATES.values():
        for team_abbr, team_data in division.items():
            if priority_type in team_data.get('current_priorities', []):
                matching_teams.append(team_abbr)
    return matching_teams

def generate_search_queries(team_abbr):
    """Generate targeted search queries for a team"""
    template = get_team_template(team_abbr)
    if not template:
        return []
    
    queries = []
    for term in template['key_search_terms']:
        queries.append(f'"{term}" site:twitter.com')
        queries.append(f'"{term}" site:{template["team_name"].lower().replace(" ", "")}.com')
    
    return queries

def get_focus_keywords(team_abbr):
    """Get keywords to prioritize in news scanning"""
    template = get_team_template(team_abbr)
    if not template:
        return []
    
    keywords = []
    for focus_area in template['focus_areas']:
        # Extract key terms from focus areas
        keywords.extend(focus_area.split('(')[0].strip().split())
    
    return list(set(keywords))

# Usage Examples
if __name__ == "__main__":
    print("NFL Research Templates Loaded")
    print(f"Total teams: {sum(len(teams) for teams in RESEARCH_TEMPLATES.values())}")
    
    # Example: Get Eagles template
    eagles = get_team_template('PHI')
    print(f"\nEagles focus areas: {eagles['focus_areas']}")
    
    # Example: Get all championship window teams
    championship_teams = get_teams_by_priority('championship_window')
    print(f"\nChampionship window teams: {championship_teams}")
    
    # Example: Get all beat reporters
    all_reporters = get_all_beat_reporters()
    print(f"\nTotal beat reporters: {len(all_reporters)}")
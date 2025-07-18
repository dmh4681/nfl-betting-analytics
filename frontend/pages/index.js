import React, { useState, useEffect } from 'react';
import { Search, TrendingUp, TrendingDown, Users, DollarSign, Brain, Target, AlertCircle, ChevronRight, Star, Filter, Loader2, Trophy, BarChart3, ArrowUp, ArrowDown, Minus, Activity, Zap } from 'lucide-react';

const styleOverrides = `
  body { 
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%) !important;
    color: #ffffff !important;
    min-height: 100vh;
  }
  * { 
    color: inherit !important; 
  }
  .bg-slate-800 { 
    background-color: rgba(30, 41, 59, 0.5) !important; 
  }
  .border-slate-700 { 
    border-color: #334155 !important; 
  }
  .bg-slate-700 {
    background-color: #334155 !important;
  }
  .bg-slate-600 {
    background-color: #475569 !important;
  }
  .bg-slate-800\/50 {
    background-color: rgba(30, 41, 59, 0.5) !important;
  }
  .bg-slate-700\/50 {
    background-color: rgba(51, 65, 85, 0.5) !important;
  }
  .bg-slate-700\/30 {
    background-color: rgba(51, 65, 85, 0.3) !important;
  }
  table {
    background: transparent !important;
  }
  th, td {
    background: transparent !important;
  }
`;

// Custom Card components
const Card = ({ children, className = "" }) => (
  <div className={`rounded-lg border bg-card text-card-foreground shadow-sm ${className}`} style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
    {children}
  </div>
);

const CardHeader = ({ children, className = "" }) => (
  <div className={`p-6 pb-4 ${className}`}>
    {children}
  </div>
);

const CardTitle = ({ children, className = "" }) => (
  <h3 className={`text-lg font-semibold leading-none tracking-tight ${className}`}>
    {children}
  </h3>
);

const CardContent = ({ children, className = "" }) => (
  <div className={`p-6 pt-0 ${className}`}>
    {children}
  </div>
);

const NFLAnalyticsDashboard = () => {
  // Add style injection
  useEffect(() => {
    const style = document.createElement('style');
    style.textContent = styleOverrides;
    document.head.appendChild(style);
    return () => {
      if (document.head.contains(style)) {
        document.head.removeChild(style);
      }
    };
  }, []);

  // State variables
  const [selectedTeam, setSelectedTeam] = useState('BAL');
  const [searchQuery, setSearchQuery] = useState('');
  const [powerRankings, setPowerRankings] = useState([]);
  const [currentTeamData, setCurrentTeamData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [view, setView] = useState('rankings');
  const [filterPosition, setFilterPosition] = useState('');
  const [filterMoveType, setFilterMoveType] = useState('');
  const [recentMoves, setRecentMoves] = useState([]);
  const [movesStats, setMovesStats] = useState({ total_found: 0, total_displayed: 0 });
  const [selectedDivision, setSelectedDivision] = useState('AFC North');
  const [divisionData, setDivisionData] = useState(null);
  const [bridgeSortBy, setBridgeSortBy] = useState('final_2025_rank');
  const [bridgeSortOrder, setBridgeSortOrder] = useState('asc');
  const [divisionMoves, setDivisionMoves] = useState({});
  const [customRankings, setCustomRankings] = useState([]);
  const [isCustomMode, setIsCustomMode] = useState(false);
  const [draggedItem, setDraggedItem] = useState(null);
  const [liveGames, setLiveGames] = useState([]);
  const [bettingEdges, setBettingEdges] = useState([]);
  const [weeklyReport, setWeeklyReport] = useState(null);
  const [espnLoading, setEspnLoading] = useState(false);

  // API base URL
  const API_BASE = 'http://localhost:8000';

  // Utility functions
  const getRankingMovementIcon = (rankChange) => {
    if (rankChange > 0) return <ArrowUp className="w-4 h-4 text-green-400" />;
    if (rankChange < 0) return <ArrowDown className="w-4 h-4 text-red-400" />;
    return <Minus className="w-4 h-4 text-slate-400" />;
  };

  const getGradeColor = (grade) => {
    if (!grade || typeof grade !== 'string') return 'text-slate-400 bg-slate-400/20'; // ADDED NULL CHECK
    if (grade.startsWith('A')) return 'text-green-400 bg-green-400/20';
    if (grade.startsWith('B')) return 'text-blue-400 bg-blue-400/20';
    if (grade.startsWith('C')) return 'text-yellow-400 bg-yellow-400/20';
    if (grade.startsWith('D')) return 'text-orange-400 bg-orange-400/20';
    return 'text-red-400 bg-red-400/20';
  };

  const formatImpact = (impact) => {
    // Handle undefined, null, or non-numeric values
    if (impact === undefined || impact === null || isNaN(impact)) {
      return 'N/A';
    }
    
    // Convert to number if it's a string
    const numericImpact = typeof impact === 'string' ? parseFloat(impact) : impact;
    
    // Handle case where parseFloat returns NaN
    if (isNaN(numericImpact)) {
      return 'N/A';
    }
    
    // Format with proper sign
    return numericImpact > 0 ? `+${numericImpact.toFixed(1)}` : numericImpact.toFixed(1);
  };

  const getTopMovers = () => {
    if (!powerRankings.length) return { climbers: [], drops: [] };
    
    const sorted = [...powerRankings].sort((a, b) => b.rank_change - a.rank_change);
    return {
      climbers: sorted.filter(team => team.rank_change > 0).slice(0, 3),
      drops: sorted.filter(team => team.rank_change < 0).slice(-3).reverse()
    };
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short', 
      day: 'numeric',
      hour: 'numeric',
      minute: '2-digit'
    });
  };
  
  const getConfidenceColor = (confidence) => {
    if (confidence >= 85) return 'text-green-400 bg-green-400/20';
    if (confidence >= 70) return 'text-blue-400 bg-blue-400/20';
    if (confidence >= 55) return 'text-yellow-400 bg-yellow-400/20';
    return 'text-red-400 bg-red-400/20';
  };
  
  const getEdgeColor = (edgeSize) => {
    if (edgeSize >= 10) return 'text-green-400 bg-green-400/20';
    if (edgeSize >= 5) return 'text-blue-400 bg-blue-400/20';
    if (edgeSize >= 3) return 'text-yellow-400 bg-yellow-400/20';
    return 'text-orange-400 bg-orange-400/20';
  };

  // Custom rankings functions
  const initializeCustomRankings = () => {
    if (powerRankings.length > 0 && customRankings.length === 0) {
      const sorted = [...powerRankings].sort((a, b) => a.final_2025_rank - b.final_2025_rank);
      setCustomRankings(sorted.map((team, index) => ({
        ...team,
        custom_rank: index + 1,
        original_expert_rank: team.final_2025_rank
      })));
    }
  };

  const updateCustomRank = (teamId, newRank) => {
    const newRankings = [...customRankings];
    const teamIndex = newRankings.findIndex(team => team.team === teamId);
    
    if (teamIndex === -1) return;
    
    const oldRank = newRankings[teamIndex].custom_rank;
    newRankings[teamIndex].custom_rank = newRank;
    
    // Adjust other teams' ranks
    newRankings.forEach((team, index) => {
      if (index !== teamIndex) {
        if (newRank < oldRank) {
          // Moving up - push others down
          if (team.custom_rank >= newRank && team.custom_rank < oldRank) {
            team.custom_rank += 1;
          }
        } else {
          // Moving down - pull others up
          if (team.custom_rank > oldRank && team.custom_rank <= newRank) {
            team.custom_rank -= 1;
          }
        }
      }
    });
    
    setCustomRankings(newRankings.sort((a, b) => a.custom_rank - b.custom_rank));
  };

  const handleDragStart = (e, team) => {
    setDraggedItem(team);
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
  };

  const handleDrop = (e, targetTeam) => {
    e.preventDefault();
    if (!draggedItem || draggedItem.team === targetTeam.team) return;
    
    updateCustomRank(draggedItem.team, targetTeam.custom_rank);
    setDraggedItem(null);
  };

  const resetToExpert = () => {
    const reset = customRankings.map(team => ({
      ...team,
      custom_rank: team.original_expert_rank
    })).sort((a, b) => a.custom_rank - b.custom_rank);
    setCustomRankings(reset);
  };

  const getCustomAnalysis = () => {
    if (customRankings.length === 0) return {};
    
    const biggest_surprise = customRankings.reduce((max, team) => {
      const diff = Math.abs(team.custom_rank - team.original_expert_rank);
      return diff > Math.abs(max.custom_rank - max.original_expert_rank) ? team : max;
    });
    
    const bold_takes = customRankings.filter(team => 
      Math.abs(team.custom_rank - team.original_expert_rank) >= 5
    ).length;
    
    const custom_top_5 = customRankings.slice(0, 5);
    const expert_top_5 = [...powerRankings].sort((a, b) => a.final_2025_rank - b.final_2025_rank).slice(0, 5);
    
    const different_top_5 = custom_top_5.filter(team => 
      !expert_top_5.some(expert => expert.team === team.team)
    ).length;
    
    return {
      biggest_surprise,
      bold_takes,
      different_top_5,
      custom_champion: customRankings[0],
      custom_worst: customRankings[customRankings.length - 1]
    };
  };
  const handleBridgeSort = (column) => {
    if (bridgeSortBy === column) {
      setBridgeSortOrder(bridgeSortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setBridgeSortBy(column);
      setBridgeSortOrder(column.includes('rank') ? 'asc' : 'desc');
    }
  };

  const getSortedPowerRankings = () => {
    const sorted = [...powerRankings].sort((a, b) => {
      let aVal, bVal;
      
      switch(bridgeSortBy) {
        case 'original_2024_rank':
          aVal = a.original_2024_rank;
          bVal = b.original_2024_rank;
          break;
        case 'final_2025_rank':
          aVal = a.final_2025_rank;
          bVal = b.final_2025_rank;
          break;
        case 'offseason_impact':
          aVal = a.offseason_impact;
          bVal = b.offseason_impact;
          break;
        case 'rank_change':
          aVal = a.rank_change;
          bVal = b.rank_change;
          break;
        case 'team_name':
          aVal = a.team_name;
          bVal = b.team_name;
          break;
        default:
          aVal = a.final_2025_rank;
          bVal = b.final_2025_rank;
      }
      
      if (typeof aVal === 'string') {
        return bridgeSortOrder === 'asc' ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
      }
      
      return bridgeSortOrder === 'asc' ? aVal - bVal : bVal - aVal;
    });
    
    return sorted;
  };

  const getSortIcon = (column) => {
    if (bridgeSortBy !== column) return null;
    return bridgeSortOrder === 'asc' ? '↑' : '↓';
  };

  // Data loading functions
  const loadPowerRankings = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_BASE}/api/rankings`);
      const data = await response.json();
      
      // DEBUG: Let's see what we're actually getting
      console.log('🔍 Raw rankings API response:', data);
      console.log('🔍 First team data:', data.rankings?.[0]);
      console.log('🔍 Sample team properties:', Object.keys(data.rankings?.[0] || {}));
      
      setPowerRankings(data.rankings || []);
      setLoading(false);
    } catch (error) {
      console.error('Error loading rankings:', error);
      setLoading(false);
    }
  };

  const loadTeamData = async (team) => {
    try {
      const response = await fetch(`${API_BASE}/api/teams/${team}/detailed`);
      const data = await response.json();
      console.log('Team data loaded:', data); // Add this for debugging
      setCurrentTeamData(data);
    } catch (error) {
      console.error('Error loading team data:', error);
    }
  };

  const loadRecentMoves = async () => {
    try {
      const response = await fetch(`${API_BASE}/api/moves?limit=10&min_impact=1.0`);
      const data = await response.json();
      setRecentMoves(data.moves || []);
    } catch (error) {
      console.error('Error loading moves:', error);
    }
  };

  const loadFilteredMoves = async (team = '', position = '', moveType = '', minImpact = null) => {
    try {
      let url = `${API_BASE}/api/moves?limit=1000`;
      
      if (team) url += `&team=${team}`;
      if (position) url += `&position=${position}`;
      if (moveType) url += `&move_type=${encodeURIComponent(moveType)}`;
      if (minImpact !== null) url += `&min_impact=${minImpact}`;
      
      console.log('Loading moves with URL:', url);
      const response = await fetch(url);
      const data = await response.json();
      
      console.log('Moves loaded:', data.total_found, 'found,', data.total_displayed, 'displayed');
      console.log('Debug info:', data.debug_info);
      
      // Just use the moves as they come from the backend
      setRecentMoves(data.moves || []);
      setMovesStats({
        total_found: data.total_found || 0,
        total_displayed: data.total_displayed || data.moves?.length || 0
      });
    } catch (error) {
      console.error('Error loading filtered moves:', error);
    }
  };

  const loadDivisionData = async (division) => {
    try {
      const response = await fetch(`${API_BASE}/api/divisions/${encodeURIComponent(division)}`);
      const data = await response.json();
      setDivisionData(data);
    } catch (error) {
      console.error('Error loading division data:', error);
    }
  };

  const getDivisionTeamMoves = async (teamAbbr) => {
    try {
      console.log(`Fetching moves for team: ${teamAbbr}`);
      const response = await fetch(`${API_BASE}/api/moves?team=${teamAbbr}&limit=200`);
      const data = await response.json();
      console.log(`Team ${teamAbbr} moves:`, data.total_found, 'found,', data.moves?.length, 'returned');
      console.log(`Debug info for ${teamAbbr}:`, data.debug_info);
      return data.moves || [];
    } catch (error) {
      console.error(`Error loading moves for ${teamAbbr}:`, error);
      return [];
    }
  };

  const loadDivisionMoves = async () => {
    if (!divisionData?.teams) return;
    
    const movesData = {};
    for (const team of divisionData.teams) {
      const teamMoves = await getDivisionTeamMoves(team.team);
      movesData[team.team] = teamMoves;
    }
    setDivisionMoves(movesData);
  };

  const loadLivePredictions = async () => {
    try {
      setEspnLoading(true);
      
      // Get current week's games with predictions
      const currentWeekResponse = await fetch(`${API_BASE}/api/schedule/current`);
      const currentWeekData = await currentWeekResponse.json();
      
      if (currentWeekData.status === 'success') {
        setWeeklyReport(currentWeekData.data);
        setLiveGames(currentWeekData.data.all_games || []);
      }
      
      // Get betting edges
      const edgesResponse = await fetch(`${API_BASE}/api/betting/edges?min_edge=2.0`);
      const edgesData = await edgesResponse.json();
      
      if (edgesData.status === 'success') {
        setBettingEdges(edgesData.edges || []);
      }
      
      setEspnLoading(false);
    } catch (error) {
      console.error('Error loading ESPN data:', error);
      setEspnLoading(false);
    }
  };

  // Effects
  useEffect(() => {
    loadPowerRankings();
    loadRecentMoves();
  }, []);

  useEffect(() => {
    if (selectedTeam) {
      loadTeamData(selectedTeam);
    }
  }, [selectedTeam]);

  useEffect(() => {
    if (selectedDivision && view === 'division') {
      loadDivisionData(selectedDivision);
    }
  }, [selectedDivision, view]);

  useEffect(() => {
    if (view === 'moves') {
      loadFilteredMoves(selectedTeam, filterPosition, filterMoveType);
    }
  }, [view, selectedTeam, filterPosition, filterMoveType]);

  useEffect(() => {
    if (divisionData && view === 'division') {
      loadDivisionMoves();
    }
  }, [divisionData, view]);

  useEffect(() => {
    if (view === 'custom' && powerRankings.length > 0) {
      initializeCustomRankings();
    }
  }, [view, powerRankings]);

  useEffect(() => {
    if (view === 'live' || view === 'edges') {
      loadLivePredictions();
    }
  }, [view]);

  const filteredRankings = powerRankings.filter(team => 
    !searchQuery || 
    team.team_name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    team.team.toLowerCase().includes(searchQuery.toLowerCase())
  );

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white flex items-center justify-center">
        <div className="text-center">
          <Loader2 className="w-8 h-8 animate-spin mx-auto mb-4 text-blue-400" />
          <p className="text-slate-400">Loading NFL Analytics...</p>
        </div>
      </div>
    );
  }

  const { climbers, drops } = getTopMovers();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Enhanced Header */}
      <div className="border-b border-slate-700 bg-slate-800/50 backdrop-blur-sm" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <Trophy className="w-8 h-8" />
              </div>
              <div>
                <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                  NFL Analytics Hub
                </h1>
                <p className="text-slate-400 text-sm">876 moves • 32 teams • Real-time intelligence</p>
              </div>
            </div>
            
            {/* Navigation */}
            <div className="flex items-center space-x-4">
              <div className="flex rounded-lg p-1" style={{backgroundColor: '#334155'}}>
              {[
                { key: 'rankings', label: 'Rankings', icon: BarChart3 },
                { key: 'bridge', label: 'Bridge', icon: TrendingUp },
                { key: 'custom', label: 'My Rankings', icon: Star },
                { key: 'live', label: 'Live Games', icon: Activity }, // NEW
                { key: 'edges', label: 'Betting Edges', icon: Zap }, // NEW
                { key: 'team', label: 'Teams', icon: Users },
                { key: 'division', label: 'Divisions', icon: Target },
                { key: 'moves', label: 'Moves', icon: Filter }
              ].map(({ key, label, icon: Icon }) => (
                  <button
                    key={key}
                    onClick={() => setView(key)}
                    className={`flex items-center space-x-2 px-4 py-2 rounded-md text-sm font-medium transition-all ${
                      view === key 
                        ? 'text-white' 
                        : 'text-slate-300 hover:text-white'
                    }`}
                    style={{
                      backgroundColor: view === key ? '#2563eb' : 'transparent'
                    }}
                  >
                    <Icon className="w-4 h-4" />
                    <span>{label}</span>
                  </button>
                ))}
              </div>
              
              <div className="relative">
                <Search className="w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400" />
                <input 
                  type="text"
                  placeholder="Search teams..."
                  className="pl-10 pr-4 py-2 rounded-lg text-white placeholder-slate-400 focus:ring-2 focus:ring-blue-500 focus:border-transparent w-64"
                  style={{backgroundColor: '#334155', borderColor: '#475569'}}
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-6">
        {/* Main Content Area */}
        {view === 'rankings' && (
          <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
            
            {/* Rankings Table */}
            <div className="lg:col-span-3">
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Trophy className="w-5 h-5 mr-2 text-yellow-400" />
                    2025 NFL Power Rankings
                    <span className="ml-auto text-sm text-slate-400">Based on 876 offseason moves</span>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="overflow-x-auto">
                    <table className="w-full" style={{backgroundColor: 'transparent'}}>
                      <thead>
                        <tr className="border-b" style={{borderColor: '#334155'}}>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Rank</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Team</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Rating</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Change</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Grade</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Impact</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filteredRankings.map((team, idx) => (
                          <tr 
                            key={team.team} 
                            className="border-b cursor-pointer transition-colors hover:bg-slate-700/30"
                            style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                            onClick={() => {
                              setSelectedTeam(team.team);
                              setView('team');
                            }}
                          >
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                <span className="text-white font-bold">#{team.final_2025_rank}</span>
                                {getRankingMovementIcon(team.rank_change)}
                              </div>
                            </td>
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-3">
                                <div className="w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-500 rounded flex items-center justify-center text-xs font-bold">
                                  {team.team}
                                </div>
                                <div>
                                  <div className="text-white font-medium">{team.team_name}</div>
                                  <div className="text-xs text-slate-400">
                                    2024: #{team.original_2024_rank}
                                  </div>
                                </div>
                              </div>
                            </td>
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="text-white font-medium">{team.final_2025_rating.toFixed(1)}</div>
                              <div className="text-xs text-slate-400">
                                {formatImpact(team.offseason_impact)}
                              </div>
                            </td>
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-1">
                                {getRankingMovementIcon(team.rank_change)}
                                <span className={
                                  team.rank_change > 0 ? 'text-green-400' : 
                                  team.rank_change < 0 ? 'text-red-400' : 'text-slate-400'
                                }>
                                  {team.rank_change === 0 ? '—' : Math.abs(team.rank_change)}
                                </span>
                              </div>
                            </td>
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <span className={`px-2 py-1 rounded text-xs font-medium ${getGradeColor(team.offseason_grade)}`}>
                                {team.offseason_grade}
                              </span>
                            </td>
                            <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="text-sm">
                                <div className="text-green-400">
                                  O: {formatImpact(team.offense_impact)}
                                </div>
                                <div className="text-blue-400">
                                  D: {formatImpact(team.defense_impact)}
                                </div>
                              </div>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Right Sidebar */}
            <div className="lg:col-span-1 space-y-6">
              
              {/* Top Movers */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <TrendingUp className="w-5 h-5 mr-2 text-green-400" />
                    Biggest Movers
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-4">
                  <div>
                    <h4 className="text-green-400 font-medium mb-2 text-sm">📈 Biggest Climbers</h4>
                    {climbers.map((team, idx) => (
                      <div key={team.team} className="flex items-center justify-between p-2 rounded mb-2" style={{backgroundColor: 'rgba(34, 197, 94, 0.1)'}}>
                        <span className="text-white text-sm">{team.team}</span>
                        <span className="text-green-400 text-sm">+{team.rank_change}</span>
                      </div>
                    ))}
                  </div>
                  
                  <div>
                    <h4 className="text-red-400 font-medium mb-2 text-sm">📉 Biggest Drops</h4>
                    {drops.map((team, idx) => (
                      <div key={team.team} className="flex items-center justify-between p-2 rounded mb-2" style={{backgroundColor: 'rgba(239, 68, 68, 0.1)'}}>
                        <span className="text-white text-sm">{team.team}</span>
                        <span className="text-red-400 text-sm">{team.rank_change}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Recent High-Impact Moves */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Target className="w-5 h-5 mr-2 text-purple-400" />
                    High-Impact Moves
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {recentMoves.slice(0, 5).map((move, idx) => (
                      <div key={idx} className="p-3 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                        <div className="flex items-center justify-between mb-1">
                          <span className="text-white font-medium text-sm">{move.player_name}</span>
                          <span className="text-purple-400 text-xs">{move.impact_score.toFixed(1)}</span>
                        </div>
                        <div className="text-xs text-slate-400">
                          {move.from_team} → {move.to_team} • {move.position}
                        </div>
                        <div className="text-xs text-blue-400 mt-1">{move.move_type}</div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}

        {/* Bridge Analysis View */}
        {view === 'bridge' && (
          <div className="space-y-6">
            
            {/* Bridge Header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between">
                <div>
                  <h1 className="text-3xl font-bold text-white">2024 → 2025 Bridge Analysis</h1>
                  <p className="text-slate-400">Complete journey: Previous rankings → Offseason impact → Final 2025 projections</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-purple-400">32 Teams</div>
                  <p className="text-slate-400 text-sm">Complete NFL Bridge</p>
                </div>
              </div>
            </div>

            {/* Bridge Overview Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-green-400 text-sm font-medium">Biggest Climber</p>
                      <p className="text-xl font-bold text-white">
                        {powerRankings.reduce((max, team) => 
                          team.rank_change > max.rank_change ? team : max, powerRankings[0] || {})?.team || 'N/A'}
                      </p>
                    </div>
                    <ArrowUp className="w-8 h-8 text-green-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-red-500/20 to-red-600/20 border-red-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-red-400 text-sm font-medium">Biggest Drop</p>
                      <p className="text-xl font-bold text-white">
                        {powerRankings.reduce((min, team) => 
                          team.rank_change < min.rank_change ? team : min, powerRankings[0] || {})?.team || 'N/A'}
                      </p>
                    </div>
                    <ArrowDown className="w-8 h-8 text-red-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-blue-400 text-sm font-medium">Best Offseason</p>
                      <p className="text-xl font-bold text-white">
                        {powerRankings.reduce((max, team) => 
                          team.offseason_impact > max.offseason_impact ? team : max, powerRankings[0] || {})?.team || 'N/A'}
                      </p>
                    </div>
                    <Star className="w-8 h-8 text-blue-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-purple-400 text-sm font-medium">Total Impact</p>
                      <p className="text-xl font-bold text-white">
                        {powerRankings.reduce((sum, team) => sum + Math.abs(team.offseason_impact), 0).toFixed(1)}
                      </p>
                    </div>
                    <Target className="w-8 h-8 text-purple-400" />
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Complete Bridge Table */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <TrendingUp className="w-5 h-5 mr-2 text-purple-400" />
                  Complete 2024 → 2025 Bridge Analysis
                  <span className="ml-auto text-sm text-slate-400">All 32 teams ranked by 2025 projection</span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full" style={{backgroundColor: 'transparent'}}>
                    <thead>
                      <tr className="border-b" style={{borderColor: '#334155'}}>
                        <th 
                          className="text-left py-3 px-2 text-slate-400 font-medium cursor-pointer hover:text-blue-400 transition-colors"
                          onClick={() => handleBridgeSort('original_2024_rank')}
                        >
                          2024 Rank {getSortIcon('original_2024_rank')}
                        </th>
                        <th 
                          className="text-left py-3 px-2 text-slate-400 font-medium cursor-pointer hover:text-blue-400 transition-colors"
                          onClick={() => handleBridgeSort('team_name')}
                        >
                          Team {getSortIcon('team_name')}
                        </th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Offseason Grade</th>
                        <th 
                          className="text-left py-3 px-2 text-slate-400 font-medium cursor-pointer hover:text-blue-400 transition-colors"
                          onClick={() => handleBridgeSort('offseason_impact')}
                        >
                          Net Impact {getSortIcon('offseason_impact')}
                        </th>
                        <th 
                          className="text-left py-3 px-2 text-slate-400 font-medium cursor-pointer hover:text-blue-400 transition-colors"
                          onClick={() => handleBridgeSort('final_2025_rank')}
                        >
                          2025 Rank {getSortIcon('final_2025_rank')}
                        </th>
                        <th 
                          className="text-left py-3 px-2 text-slate-400 font-medium cursor-pointer hover:text-blue-400 transition-colors"
                          onClick={() => handleBridgeSort('rank_change')}
                        >
                          Movement {getSortIcon('rank_change')}
                        </th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Bridge Visual</th>
                      </tr>
                    </thead>
                    <tbody>
                      {getSortedPowerRankings().map((team, idx) => {
                        const isClimber = team.rank_change > 0;
                        const isDropper = team.rank_change < 0;
                        const isNeutral = team.rank_change === 0;
                        
                        return (
                          <tr 
                            key={team.team} 
                            className="border-b hover:bg-slate-700/30 cursor-pointer transition-colors"
                            style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                            onClick={() => {
                              setSelectedTeam(team.team);
                              setView('team');
                            }}
                          >
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                <span className="text-slate-400 font-bold">#{team.original_2024_rank}</span>
                                <div className="w-8 h-8 bg-gradient-to-r from-slate-600 to-slate-700 rounded flex items-center justify-center text-xs font-bold text-slate-300">
                                  {team.team}
                                </div>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div>
                                <div className="text-white font-medium">{team.team_name}</div>
                                <div className="text-xs text-slate-400">
                                  Rating: {team.original_2024_rating.toFixed(1)} → {team.final_2025_rating.toFixed(1)}
                                </div>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <span className={`px-3 py-1 rounded-full text-sm font-medium ${getGradeColor(team.offseason_grade)}`}>
                                {team.offseason_grade}
                              </span>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                <span className={`font-bold text-lg ${
                                  team.offseason_impact > 2 ? 'text-green-400' : 
                                  team.offseason_impact > 0 ? 'text-blue-400' : 
                                  team.offseason_impact > -2 ? 'text-yellow-400' : 'text-red-400'
                                }`}>
                                  {formatImpact(team.offseason_impact)}
                                </span>
                                <div className="w-16 bg-slate-700 rounded-full h-2">
                                  <div 
                                    className={`h-2 rounded-full ${
                                      team.offseason_impact > 2 ? 'bg-green-400' : 
                                      team.offseason_impact > 0 ? 'bg-blue-400' : 
                                      team.offseason_impact > -2 ? 'bg-yellow-400' : 'bg-red-400'
                                    }`}
                                    style={{width: `${Math.min(100, Math.max(10, (team.offseason_impact + 5) * 10))}%`}}
                                  ></div>
                                </div>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                <div className={`w-8 h-8 rounded flex items-center justify-center text-xs font-bold text-white ${
                                  team.final_2025_rank <= 5 ? 'bg-gradient-to-r from-yellow-500 to-yellow-600' :
                                  team.final_2025_rank <= 12 ? 'bg-gradient-to-r from-green-500 to-green-600' :
                                  team.final_2025_rank <= 20 ? 'bg-gradient-to-r from-blue-500 to-blue-600' :
                                  team.final_2025_rank <= 28 ? 'bg-gradient-to-r from-orange-500 to-orange-600' :
                                  'bg-gradient-to-r from-red-500 to-red-600'
                                }`}>
                                  {team.team}
                                </div>
                                <span className="text-white font-bold">#{team.final_2025_rank}</span>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                {getRankingMovementIcon(team.rank_change)}
                                <span className={`font-bold text-lg ${
                                  isClimber ? 'text-green-400' : isDropper ? 'text-red-400' : 'text-slate-400'
                                }`}>
                                  {team.rank_change > 0 ? `+${team.rank_change}` : team.rank_change}
                                </span>
                                <span className="text-xs text-slate-400">
                                  {isClimber ? 'spots up' : isDropper ? 'spots down' : 'no change'}
                                </span>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-1">
                                {/* 2024 Position */}
                                <div className="w-3 h-3 bg-slate-500 rounded-full"></div>
                                
                                {/* Bridge Line */}
                                <div className="flex-1 h-0.5 relative" style={{
                                  background: `linear-gradient(90deg, 
                                    #64748b 0%, 
                                    ${team.offseason_impact > 0 ? '#4ade80' : team.offseason_impact < 0 ? '#f87171' : '#94a3b8'} 50%, 
                                    ${team.final_2025_rank <= 10 ? '#fbbf24' : team.final_2025_rank <= 20 ? '#60a5fa' : '#f87171'} 100%)`
                                }}>
                                  {/* Impact indicator */}
                                  <div 
                                    className={`absolute w-2 h-2 rounded-full top-1/2 transform -translate-y-1/2 ${
                                      team.offseason_impact > 1 ? 'bg-green-400' : 
                                      team.offseason_impact > 0 ? 'bg-blue-400' : 
                                      team.offseason_impact > -1 ? 'bg-yellow-400' : 'bg-red-400'
                                    }`}
                                    style={{left: '50%', transform: 'translateX(-50%) translateY(-50%)'}}
                                  ></div>
                                </div>
                                
                                {/* 2025 Position */}
                                <div className={`w-3 h-3 rounded-full ${
                                  team.final_2025_rank <= 10 ? 'bg-yellow-400' : 
                                  team.final_2025_rank <= 20 ? 'bg-blue-400' : 'bg-red-400'
                                }`}></div>
                              </div>
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>

            {/* Bridge Insights */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              
              {/* Biggest Climbers */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <ArrowUp className="w-5 h-5 mr-2 text-green-400" />
                    Biggest Climbers
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {powerRankings
                      .filter(team => team.rank_change > 0)
                      .sort((a, b) => b.rank_change - a.rank_change)
                      .slice(0, 5)
                      .map((team, idx) => (
                        <div key={team.team} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(34, 197, 94, 0.1)'}}>
                          <div className="flex items-center space-x-3">
                            <span className="text-green-400 font-bold">#{idx + 1}</span>
                            <div>
                              <div className="text-white font-medium">{team.team}</div>
                              <div className="text-xs text-slate-400">
                                #{team.original_2024_rank} → #{team.final_2025_rank}
                              </div>
                            </div>
                          </div>
                          <div className="text-right">
                            <div className="text-green-400 font-bold">+{team.rank_change}</div>
                            <div className="text-xs text-slate-400">{team.offseason_grade}</div>
                          </div>
                        </div>
                      ))}
                  </div>
                </CardContent>
              </Card>

              {/* Biggest Drops */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <ArrowDown className="w-5 h-5 mr-2 text-red-400" />
                    Biggest Drops
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {powerRankings
                      .filter(team => team.rank_change < 0)
                      .sort((a, b) => a.rank_change - b.rank_change)
                      .slice(0, 5)
                      .map((team, idx) => (
                        <div key={team.team} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(239, 68, 68, 0.1)'}}>
                          <div className="flex items-center space-x-3">
                            <span className="text-red-400 font-bold">#{idx + 1}</span>
                            <div>
                              <div className="text-white font-medium">{team.team}</div>
                              <div className="text-xs text-slate-400">
                                #{team.original_2024_rank} → #{team.final_2025_rank}
                              </div>
                            </div>
                          </div>
                          <div className="text-right">
                            <div className="text-red-400 font-bold">{team.rank_change}</div>
                            <div className="text-xs text-slate-400">{team.offseason_grade}</div>
                          </div>
                        </div>
                      ))}
                  </div>
                </CardContent>
              </Card>

              {/* Most Impactful Offseasons */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Star className="w-5 h-5 mr-2 text-blue-400" />
                    Most Impactful Offseasons
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {powerRankings
                      .sort((a, b) => Math.abs(b.offseason_impact) - Math.abs(a.offseason_impact))
                      .slice(0, 5)
                      .map((team, idx) => (
                        <div key={team.team} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(59, 130, 246, 0.1)'}}>
                          <div className="flex items-center space-x-3">
                            <span className="text-blue-400 font-bold">#{idx + 1}</span>
                            <div>
                              <div className="text-white font-medium">{team.team}</div>
                              <div className="text-xs text-slate-400">
                                Grade: {team.offseason_grade}
                              </div>
                            </div>
                          </div>
                          <div className="text-right">
                            <div className={`font-bold ${team.offseason_impact > 0 ? 'text-green-400' : 'text-red-400'}`}>
                              {formatImpact(team.offseason_impact)}
                            </div>
                            <div className="text-xs text-slate-400">impact</div>
                          </div>
                        </div>
                      ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}

        {/* Custom Rankings View */}
        {view === 'custom' && (
          <div className="space-y-6">
            
            {/* Custom Rankings Header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between">
                <div>
                  <h1 className="text-3xl font-bold text-white">My Custom Rankings</h1>
                  <p className="text-slate-400">Adjust rankings to match your expert opinion • Drag teams or edit ranks directly</p>
                </div>
                <div className="flex items-center space-x-4">
                  <button 
                    onClick={resetToExpert}
                    className="px-4 py-2 bg-slate-600 hover:bg-slate-500 rounded-lg text-white transition-colors"
                  >
                    Reset to Expert
                  </button>
                  <button 
                    className="px-6 py-2 bg-gradient-to-r from-purple-600 to-blue-600 hover:from-purple-500 hover:to-blue-500 rounded-lg text-white font-medium transition-all"
                  >
                    Export My Analysis
                  </button>
                </div>
              </div>
            </div>

            {/* Custom Analysis Overview */}
            {customRankings.length > 0 && (
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <Card className="bg-gradient-to-r from-yellow-500/20 to-yellow-600/20 border-yellow-500/30">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-yellow-400 text-sm font-medium">My Champion</p>
                        <p className="text-xl font-bold text-white">{getCustomAnalysis().custom_champion?.team || 'N/A'}</p>
                      </div>
                      <Trophy className="w-8 h-8 text-yellow-400" />
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-purple-400 text-sm font-medium">Bold Takes</p>
                        <p className="text-xl font-bold text-white">{getCustomAnalysis().bold_takes}</p>
                      </div>
                      <Star className="w-8 h-8 text-purple-400" />
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-green-400 text-sm font-medium">Different Top 5</p>
                        <p className="text-xl font-bold text-white">{getCustomAnalysis().different_top_5}</p>
                      </div>
                      <TrendingUp className="w-8 h-8 text-green-400" />
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between">
                      <div>
                        <p className="text-blue-400 text-sm font-medium">Biggest Surprise</p>
                        <p className="text-xl font-bold text-white">{getCustomAnalysis().biggest_surprise?.team || 'N/A'}</p>
                      </div>
                      <AlertCircle className="w-8 h-8 text-blue-400" />
                    </div>
                  </CardContent>
                </Card>
              </div>
            )}

            {/* Editable Rankings Table */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Star className="w-5 h-5 mr-2 text-purple-400" />
                  Drag to Reorder • Click Rank to Edit
                  <span className="ml-auto text-sm text-slate-400">
                    Changes from expert rankings highlighted
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full" style={{backgroundColor: 'transparent'}}>
                    <thead>
                      <tr className="border-b" style={{borderColor: '#334155'}}>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">My Rank</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Team</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Expert Rank</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Difference</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Offseason Grade</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">My Take</th>
                      </tr>
                    </thead>
                    <tbody>
                      {customRankings.map((team, idx) => {
                        const rankDiff = team.custom_rank - team.original_expert_rank;
                        const isChanged = rankDiff !== 0;
                        const isBoldTake = Math.abs(rankDiff) >= 5;
                        
                        return (
                          <tr 
                            key={team.team}
                            draggable
                            onDragStart={(e) => handleDragStart(e, team)}
                            onDragOver={handleDragOver}
                            onDrop={(e) => handleDrop(e, team)}
                            className={`border-b cursor-move hover:bg-slate-700/30 transition-colors ${
                              isChanged ? 'bg-blue-500/10 border-blue-500/30' : ''
                            } ${draggedItem?.team === team.team ? 'opacity-50' : ''}`}
                            style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                          >
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                <input 
                                  type="number"
                                  min="1"
                                  max="32"
                                  value={team.custom_rank}
                                  onChange={(e) => updateCustomRank(team.team, parseInt(e.target.value) || 1)}
                                  className={`w-16 px-2 py-1 rounded text-center font-bold ${
                                    isChanged ? 'bg-blue-600 text-white' : 'bg-slate-700 text-white'
                                  }`}
                                  style={{backgroundColor: isChanged ? '#2563eb' : '#334155'}}
                                />
                                {isBoldTake && <Star className="w-4 h-4 text-yellow-400" />}
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-3">
                                <div className={`w-8 h-8 rounded flex items-center justify-center text-xs font-bold text-white ${
                                  team.custom_rank <= 5 ? 'bg-gradient-to-r from-yellow-500 to-yellow-600' :
                                  team.custom_rank <= 12 ? 'bg-gradient-to-r from-green-500 to-green-600' :
                                  team.custom_rank <= 20 ? 'bg-gradient-to-r from-blue-500 to-blue-600' :
                                  team.custom_rank <= 28 ? 'bg-gradient-to-r from-orange-500 to-orange-600' :
                                  'bg-gradient-to-r from-red-500 to-red-600'
                                }`}>
                                  {team.team}
                                </div>
                                <div>
                                  <div className="text-white font-medium">{team.team_name}</div>
                                  <div className="text-xs text-slate-400">
                                    Rating: {team.final_2025_rating?.toFixed(1)}
                                  </div>
                                </div>
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <span className="text-slate-400 font-medium">#{team.original_expert_rank}</span>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="flex items-center space-x-2">
                                {rankDiff === 0 ? (
                                  <span className="text-slate-400">No change</span>
                                ) : (
                                  <>
                                    {rankDiff < 0 ? (
                                      <ArrowUp className="w-4 h-4 text-green-400" />
                                    ) : (
                                      <ArrowDown className="w-4 h-4 text-red-400" />
                                    )}
                                    <span className={`font-bold ${
                                      rankDiff < 0 ? 'text-green-400' : 'text-red-400'
                                    }`}>
                                      {Math.abs(rankDiff)} spots {rankDiff < 0 ? 'higher' : 'lower'}
                                    </span>
                                  </>
                                )}
                              </div>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <span className={`px-2 py-1 rounded text-xs font-medium ${getGradeColor(team.offseason_grade)}`}>
                                {team.offseason_grade}
                              </span>
                            </td>
                            <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                              <div className="text-sm">
                                {team.custom_rank <= 5 ? (
                                  <span className="text-yellow-400 font-medium">Championship Contender</span>
                                ) : team.custom_rank <= 12 ? (
                                  <span className="text-green-400 font-medium">Playoff Lock</span>
                                ) : team.custom_rank <= 20 ? (
                                  <span className="text-blue-400 font-medium">Wild Card Hunt</span>
                                ) : team.custom_rank <= 28 ? (
                                  <span className="text-orange-400 font-medium">Rebuilding</span>
                                ) : (
                                  <span className="text-red-400 font-medium">Tank Mode</span>
                                )}
                                {isBoldTake && (
                                  <div className="text-xs text-yellow-400 mt-1">🔥 Bold Take!</div>
                                )}
                              </div>
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
                
                <div className="mt-6 p-4 border rounded-lg" style={{backgroundColor: 'rgba(168, 85, 247, 0.1)', borderColor: 'rgba(168, 85, 247, 0.3)'}}>
                  <div className="flex items-center mb-2">
                    <Brain className="w-5 h-5 text-purple-400 mr-2" />
                    <span className="text-purple-400 font-medium">Pro Tip</span>
                  </div>
                  <p className="text-white text-sm">
                    💡 <strong>Drag teams up/down</strong> or <strong>click rank numbers</strong> to edit directly. 
                    Teams moved 5+ spots get the 🔥 Bold Take badge. Your changes are highlighted in blue.
                  </p>
                </div>
              </CardContent>
            </Card>

            {/* Your Bold Takes */}
            {customRankings.length > 0 && getCustomAnalysis().bold_takes > 0 && (
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Star className="w-5 h-5 mr-2 text-yellow-400" />
                    Your Bold Takes ({getCustomAnalysis().bold_takes})
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {customRankings
                      .filter(team => Math.abs(team.custom_rank - team.original_expert_rank) >= 5)
                      .map((team, idx) => {
                        const diff = team.custom_rank - team.original_expert_rank;
                        return (
                          <div key={team.team} className="p-4 rounded-lg" style={{backgroundColor: 'rgba(251, 191, 36, 0.1)', border: '1px solid rgba(251, 191, 36, 0.3)'}}>
                            <div className="flex items-center justify-between mb-2">
                              <span className="text-white font-bold">{team.team} - {team.team_name}</span>
                              <span className="text-yellow-400 text-xs">🔥 Bold Take</span>
                            </div>
                            <div className="text-sm">
                              <span className="text-slate-400">You ranked them </span>
                              <span className={`font-bold ${diff < 0 ? 'text-green-400' : 'text-red-400'}`}>
                                {Math.abs(diff)} spots {diff < 0 ? 'higher' : 'lower'}
                              </span>
                              <span className="text-slate-400"> than expert (#{team.original_expert_rank} → #{team.custom_rank})</span>
                            </div>
                            <div className="text-xs text-slate-400 mt-1">
                              Grade: {team.offseason_grade} • {team.final_2025_rating?.toFixed(1)} rating
                            </div>
                          </div>
                        );
                      })}
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        )}

        {/* Live Games View - NEW */}
        {view === 'live' && (
          <div className="space-y-6">
            
            {/* Live Header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between">
                <div>
                  <h1 className="text-3xl font-bold text-white flex items-center">
                    <Activity className="w-8 h-8 mr-3 text-green-400" />
                    Live NFL Predictions
                  </h1>
                  <p className="text-slate-400">Real-time games with your bridge framework projections vs Vegas</p>
                </div>
                <div className="text-right">
                  {weeklyReport && (
                    <>
                      <div className="text-2xl font-bold text-green-400">{weeklyReport.week_summary.total_games}</div>
                      <p className="text-slate-400 text-sm">Games This Week</p>
                      <div className="text-lg font-bold text-blue-400 mt-2">{weeklyReport.week_summary.betting_edges_found}</div>
                      <p className="text-slate-400 text-xs">Betting Edges Found</p>
                    </>
                  )}
                </div>
              </div>
            </div>

            {/* Live Games Table */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Activity className="w-5 h-5 mr-2 text-green-400" />
                  This Week's Games with Bridge Predictions
                  <span className="ml-auto text-sm text-slate-400">
                    Your Analysis vs Vegas Lines
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                {espnLoading ? (
                  <div className="text-center py-8">
                    <Loader2 className="w-6 h-6 animate-spin mx-auto mb-4 text-blue-400" />
                    <p className="text-slate-400">Loading live predictions...</p>
                  </div>
                ) : (
                  <div className="overflow-x-auto">
                    <table className="w-full" style={{backgroundColor: 'transparent'}}>
                      <thead>
                        <tr className="border-b" style={{borderColor: '#334155'}}>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Game</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Date</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Our Prediction</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Vegas Line</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Confidence</th>
                          <th className="text-left py-3 px-2 text-slate-400 font-medium">Edge</th>
                        </tr>
                      </thead>
                      <tbody>
                        {liveGames.map((game, idx) => {
                          const ourSpread = game.bridge_predictions.projected_spread;
                          const vegasSpread = game.espn_data.odds?.spread;
                          const hasEdge = game.betting_edge;
                          
                          return (
                            <tr 
                              key={game.game_id} 
                              className="border-b hover:bg-slate-700/30 transition-colors"
                              style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                            >
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                <div className="flex items-center space-x-3">
                                  <div className="text-white font-medium">
                                    {game.away_team.name} @ {game.home_team.name}
                                  </div>
                                </div>
                              </td>
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                <div className="text-white text-sm">{formatDate(game.date)}</div>
                                <div className="text-xs text-slate-400">{game.espn_data.broadcast?.network}</div>
                              </td>
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                <div className="text-white font-bold">
                                  {ourSpread > 0 ? game.home_team.bridge_abbr : game.away_team.bridge_abbr} {Math.abs(ourSpread).toFixed(1)}
                                </div>
                                <div className="text-xs text-slate-400">
                                  {(game.bridge_predictions.home_win_probability * 100).toFixed(0)}% win prob
                                </div>
                              </td>
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                {vegasSpread !== null ? (
                                  <div className="text-white">
                                    {vegasSpread > 0 ? game.home_team.bridge_abbr : game.away_team.bridge_abbr} {Math.abs(vegasSpread).toFixed(1)}
                                  </div>
                                ) : (
                                  <div className="text-slate-400 text-sm">No line yet</div>
                                )}
                                <div className="text-xs text-slate-400">
                                  O/U: {game.espn_data.odds?.over_under || 'N/A'}
                                </div>
                              </td>
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                <span className={`px-2 py-1 rounded text-xs font-medium ${getConfidenceColor(game.bridge_predictions.confidence)}`}>
                                  {game.bridge_predictions.confidence}%
                                </span>
                              </td>
                              <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                {hasEdge ? (
                                  <div>
                                    <span className={`px-2 py-1 rounded text-xs font-bold ${getEdgeColor(hasEdge.edge_size)}`}>
                                      {hasEdge.edge_size.toFixed(1)} pts
                                    </span>
                                    <div className="text-xs text-white mt-1">
                                      Bet {hasEdge.recommendation}
                                    </div>
                                  </div>
                                ) : (
                                  <div className="text-slate-400 text-sm">No edge</div>
                                )}
                              </td>
                            </tr>
                          );
                        })}
                      </tbody>
                    </table>
                  </div>
                )}
              </CardContent>
            </Card>
          </div>
        )}

        {/* Betting Edges View - NEW */}
        {view === 'edges' && (
          <div className="space-y-6">
            
            {/* Edges Header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between">
                <div>
                  <h1 className="text-3xl font-bold text-white flex items-center">
                    <Zap className="w-8 h-8 mr-3 text-yellow-400" />
                    Betting Edges Alert 🚨
                  </h1>
                  <p className="text-slate-400">Games where your bridge framework finds value vs Vegas</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-yellow-400">{bettingEdges.length}</div>
                  <p className="text-slate-400 text-sm">Edges Found (2+ pts)</p>
                </div>
              </div>
            </div>

            {/* Top 3 Betting Edges as Featured Cards */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              {bettingEdges.slice(0, 3).map((edge, idx) => (
                <Card key={edge.game_id} className="backdrop-blur-sm border-2" style={{borderColor: idx === 0 ? '#eab308' : idx === 1 ? '#94a3b8' : '#ea580c'}}>
                  <CardHeader>
                    <CardTitle className="text-white flex items-center justify-between">
                      <div className="flex items-center">
                        <span className={`w-8 h-8 rounded-full flex items-center justify-center text-white font-bold mr-3 ${
                          idx === 0 ? 'bg-yellow-500' : idx === 1 ? 'bg-gray-400' : 'bg-orange-500'
                        }`}>
                          #{idx + 1}
                        </span>
                        <div>
                          <div className="text-lg font-bold">{edge.away_team.bridge_abbr} @ {edge.home_team.bridge_abbr}</div>
                          <div className="text-sm text-slate-400">{edge.away_team.name} @ {edge.home_team.name}</div>
                        </div>
                      </div>
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div className="text-center">
                        <div className={`inline-block px-4 py-2 rounded-full text-xl font-bold ${getEdgeColor(edge.betting_edge.edge_size)}`}>
                          {edge.betting_edge.edge_size.toFixed(1)} POINT EDGE
                        </div>
                      </div>
                      
                      <div className="grid grid-cols-2 gap-4">
                        <div className="text-center">
                          <p className="text-slate-400 text-sm">Our Prediction</p>
                          <p className="text-white font-bold text-lg">
                            {edge.betting_edge.bridge_spread > 0 ? edge.home_team.bridge_abbr : edge.away_team.bridge_abbr} {Math.abs(edge.betting_edge.bridge_spread).toFixed(1)}
                          </p>
                        </div>
                        <div className="text-center">
                          <p className="text-slate-400 text-sm">Vegas Line</p>
                          <p className="text-white font-bold text-lg">
                            {edge.betting_edge.vegas_spread > 0 ? edge.home_team.bridge_abbr : edge.away_team.bridge_abbr} {Math.abs(edge.betting_edge.vegas_spread).toFixed(1)}
                          </p>
                        </div>
                      </div>
                      
                      <div className="p-3 rounded-lg" style={{backgroundColor: 'rgba(34, 197, 94, 0.15)', border: '1px solid rgba(34, 197, 94, 0.4)'}}>
                        <div className="text-center">
                          <div className="text-green-400 font-bold text-lg">BET {edge.betting_edge.recommendation}</div>
                          <div className="text-slate-300 text-sm">{edge.betting_edge.confidence}% confidence</div>
                        </div>
                      </div>
                      
                      <div className="text-xs text-slate-400 text-center">
                        {formatDate(edge.date)} • {edge.espn_data.broadcast?.network}
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* All Edges Table */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Target className="w-5 h-5 mr-2 text-purple-400" />
                  All Betting Edges ({bettingEdges.length} found)
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full" style={{backgroundColor: 'transparent'}}>
                    <thead>
                      <tr className="border-b" style={{borderColor: '#334155'}}>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Rank</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Game</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Edge Size</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Our Line</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Vegas Line</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Recommendation</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Confidence</th>
                      </tr>
                    </thead>
                    <tbody>
                      {bettingEdges.map((edge, idx) => (
                        <tr 
                          key={edge.game_id} 
                          className="border-b hover:bg-slate-700/30 transition-colors"
                          style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                        >
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className={`w-6 h-6 rounded-full flex items-center justify-center text-white text-sm font-bold ${
                              idx < 3 ? 'bg-yellow-500' : idx < 8 ? 'bg-blue-500' : 'bg-slate-500'
                            }`}>
                              {idx + 1}
                            </span>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="text-white font-medium">{edge.away_team.bridge_abbr} @ {edge.home_team.bridge_abbr}</div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className={`px-2 py-1 rounded font-bold ${getEdgeColor(edge.betting_edge.edge_size)}`}>
                              {edge.betting_edge.edge_size.toFixed(1)} pts
                            </span>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="text-white">
                              {edge.betting_edge.bridge_spread > 0 ? edge.home_team.bridge_abbr : edge.away_team.bridge_abbr} {Math.abs(edge.betting_edge.bridge_spread).toFixed(1)}
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="text-white">
                              {edge.betting_edge.vegas_spread > 0 ? edge.home_team.bridge_abbr : edge.away_team.bridge_abbr} {Math.abs(edge.betting_edge.vegas_spread).toFixed(1)}
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className="text-green-400 font-bold">BET {edge.betting_edge.recommendation}</span>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className={`px-2 py-1 rounded text-xs ${getConfidenceColor(edge.betting_edge.confidence)}`}>
                              {edge.betting_edge.confidence}%
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          </div>
        )}

        {/* Team Detail View */}
        {view === 'team' && currentTeamData && (
          <div className="space-y-6">
            
            {/* Team Header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <div className="w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-500 rounded-lg flex items-center justify-center text-xl font-bold">
                    {currentTeamData.team}
                  </div>
                  <div>
                    <h1 className="text-3xl font-bold text-white">{currentTeamData.team_name}</h1>
                    <p className="text-slate-400">{currentTeamData.division} • {currentTeamData.conference}</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className={`inline-block px-4 py-2 rounded-lg text-xl font-bold ${getGradeColor(currentTeamData.offseason_grade)}`}>
                    {currentTeamData.offseason_grade}
                  </div>
                  <p className="text-slate-400 text-sm mt-1">Offseason Grade</p>
                </div>
              </div>
            </div>

            {/* Team Stats Grid */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <Card className="bg-gradient-to-r from-yellow-500/20 to-yellow-600/20 border-yellow-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-yellow-400 text-sm font-medium">2025 Rank</p>
                      <p className="text-2xl font-bold text-white">
                        #{currentTeamData.final_rank || currentTeamData.final_2025_rank || 16}
                      </p>
                      <p className="text-xs text-slate-400">
                        {currentTeamData.rank_change ? (
                          currentTeamData.rank_change > 0 ? `↑${currentTeamData.rank_change}` : `↓${Math.abs(currentTeamData.rank_change)}`
                        ) : 'No change'}
                      </p>
                    </div>
                    <Trophy className="w-8 h-8 text-yellow-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-green-400 text-sm font-medium">Net Impact</p>
                      <p className="text-2xl font-bold text-white">
                        {formatImpact(currentTeamData.net_impact || 0)}
                      </p>
                      <p className="text-xs text-slate-400">
                        {currentTeamData.move_efficiency ? `${currentTeamData.move_efficiency.toFixed(2)} efficiency` : 'N/A'}
                      </p>
                    </div>
                    <TrendingUp className="w-8 h-8 text-green-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-purple-400 text-sm font-medium">Total Moves</p>
                      <p className="text-2xl font-bold text-white">
                        {currentTeamData.total_moves || 0}
                      </p>
                      <p className="text-xs text-slate-400">
                        +{currentTeamData.players_gained || 0} / -{currentTeamData.players_lost || 0}
                      </p>
                    </div>
                    <Users className="w-8 h-8 text-purple-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-blue-400 text-sm font-medium">Cap Space</p>
                      <p className="text-2xl font-bold text-white">
                        {currentTeamData.context?.cap_space || 'N/A'}
                      </p>
                      <p className="text-xs text-slate-400">
                        {currentTeamData.context?.cap_situation || 'Unknown'}
                      </p>
                    </div>
                    <DollarSign className="w-8 h-8 text-blue-400" />
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Key Context Card */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <AlertCircle className="w-5 h-5 mr-2 text-yellow-400" />
                  Offseason Context & Analysis
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h4 className="text-blue-400 font-medium mb-3">Offseason Strategy</h4>
                    <p className="text-white text-sm leading-relaxed">{currentTeamData.offseason_strategy || 'No strategy information available'}</p>
                  </div>
                  <div className="space-y-3">
                    <div>
                      <h4 className="text-purple-400 font-medium mb-2">Draft Summary</h4>
                      <p className="text-white text-sm">{currentTeamData.draft_summary || 'No draft summary available'}</p>
                    </div>
                    <div>
                      <h4 className="text-green-400 font-medium mb-2">Key Injuries</h4>
                      <p className="text-white text-sm">{currentTeamData.context?.key_injuries || 'No major injuries reported'}</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            {/* Main Content Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
              
              {/* Roster Moves Section - 2 columns wide */}
              <div className="lg:col-span-2 space-y-6">
                
                {/* Free Agency & Trades */}
                <Card className="backdrop-blur-sm">
                  <CardHeader>
                    <CardTitle className="text-white">Free Agency & Trades</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      
                      {/* Signings */}
                      {currentTeamData.signings && currentTeamData.signings.length > 0 && (
                        <div>
                          <h4 className="text-green-400 font-medium mb-3 flex items-center">
                            <TrendingUp className="w-4 h-4 mr-2" />
                            Free Agent Signings ({currentTeamData.signings.length})
                          </h4>
                          <div className="space-y-2">
                            {currentTeamData.signings.map((signing, idx) => (
                              <div key={idx} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(34, 197, 94, 0.1)', border: '1px solid rgba(34, 197, 94, 0.2)'}}>
                                <span className="text-white text-sm">{signing}</span>
                                <ChevronRight className="w-4 h-4 text-green-400" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {/* Losses */}
                      {currentTeamData.losses && currentTeamData.losses.length > 0 && (
                        <div>
                          <h4 className="text-red-400 font-medium mb-3 flex items-center">
                            <TrendingDown className="w-4 h-4 mr-2" />
                            Free Agent Losses ({currentTeamData.losses.length})
                          </h4>
                          <div className="space-y-2">
                            {currentTeamData.losses.map((loss, idx) => (
                              <div key={idx} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.2)'}}>
                                <span className="text-white text-sm">{loss}</span>
                                <ChevronRight className="w-4 h-4 text-red-400" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {/* Trades */}
                      {currentTeamData.trades && currentTeamData.trades.length > 0 && (
                        <div>
                          <h4 className="text-blue-400 font-medium mb-3 flex items-center">
                            <Target className="w-4 h-4 mr-2" />
                            Trades ({currentTeamData.trades.length})
                          </h4>
                          <div className="space-y-2">
                            {currentTeamData.trades.map((trade, idx) => (
                              <div key={idx} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(59, 130, 246, 0.1)', border: '1px solid rgba(59, 130, 246, 0.2)'}}>
                                <span className="text-white text-sm">{trade}</span>
                                <ChevronRight className="w-4 h-4 text-blue-400" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}

                      {/* Extensions */}
                      {currentTeamData.extensions && currentTeamData.extensions.length > 0 && (
                        <div>
                          <h4 className="text-purple-400 font-medium mb-3 flex items-center">
                            <Star className="w-4 h-4 mr-2" />
                            Re-signings/Extensions ({currentTeamData.extensions.length})
                          </h4>
                          <div className="space-y-2">
                            {currentTeamData.extensions.map((extension, idx) => (
                              <div key={idx} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(168, 85, 247, 0.1)', border: '1px solid rgba(168, 85, 247, 0.2)'}}>
                                <span className="text-white text-sm">{extension}</span>
                                <ChevronRight className="w-4 h-4 text-purple-400" />
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  </CardContent>
                </Card>

                {/* Draft Picks */}
                <Card className="backdrop-blur-sm">
                  <CardHeader>
                    <CardTitle className="text-white">2025 NFL Draft</CardTitle>
                  </CardHeader>
                  <CardContent>
                    {currentTeamData.draft_picks && currentTeamData.draft_picks.length > 0 ? (
                      <div className="space-y-2">
                        {currentTeamData.draft_picks.map((pick, idx) => (
                          <div key={idx} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(251, 191, 36, 0.1)', border: '1px solid rgba(251, 191, 36, 0.2)'}}>
                            <span className="text-white text-sm">{pick}</span>
                            <ChevronRight className="w-4 h-4 text-yellow-400" />
                          </div>
                        ))}
                      </div>
                    ) : (
                      <p className="text-slate-400 text-center py-4">No draft picks recorded</p>
                    )}
                  </CardContent>
                </Card>
              </div>

              {/* Right Sidebar - Unit Impact and Needs */}
              <div className="space-y-6">
                
                {/* Unit Impact Analysis */}
                <Card className="backdrop-blur-sm">
                  <CardHeader>
                    <CardTitle className="text-white">Unit Impact Analysis</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div className="flex items-center justify-between p-4 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                        <div className="flex items-center space-x-3">
                          <div className={`w-3 h-3 rounded-full ${(currentTeamData.unit_impacts?.offense || 0) > 0 ? 'bg-green-400' : (currentTeamData.unit_impacts?.offense || 0) < 0 ? 'bg-red-400' : 'bg-slate-400'}`}></div>
                          <span className="text-white font-medium">Offense</span>
                        </div>
                        <span className={`font-bold text-lg ${(currentTeamData.unit_impacts?.offense || 0) > 0 ? 'text-green-400' : (currentTeamData.unit_impacts?.offense || 0) < 0 ? 'text-red-400' : 'text-slate-400'}`}>
                          {formatImpact(currentTeamData.unit_impacts?.offense || 0)}
                        </span>
                      </div>

                      <div className="flex items-center justify-between p-4 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                        <div className="flex items-center space-x-3">
                          <div className={`w-3 h-3 rounded-full ${(currentTeamData.unit_impacts?.defense || 0) > 0 ? 'bg-green-400' : (currentTeamData.unit_impacts?.defense || 0) < 0 ? 'bg-red-400' : 'bg-slate-400'}`}></div>
                          <span className="text-white font-medium">Defense</span>
                        </div>
                        <span className={`font-bold text-lg ${(currentTeamData.unit_impacts?.defense || 0) > 0 ? 'text-green-400' : (currentTeamData.unit_impacts?.defense || 0) < 0 ? 'text-red-400' : 'text-slate-400'}`}>
                          {formatImpact(currentTeamData.unit_impacts?.defense || 0)}
                        </span>
                      </div>

                      <div className="flex items-center justify-between p-4 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                        <div className="flex items-center space-x-3">
                          <div className={`w-3 h-3 rounded-full ${(currentTeamData.unit_impacts?.specialTeams || 0) > 0 ? 'bg-green-400' : (currentTeamData.unit_impacts?.specialTeams || 0) < 0 ? 'text-red-400' : 'bg-slate-400'}`}></div>
                          <span className="text-white font-medium">Special Teams</span>
                        </div>
                        <span className={`font-bold text-lg ${(currentTeamData.unit_impacts?.specialTeams || 0) > 0 ? 'text-green-400' : (currentTeamData.unit_impacts?.specialTeams || 0) < 0 ? 'text-red-400' : 'text-slate-400'}`}>
                          {formatImpact(currentTeamData.unit_impacts?.specialTeams || 0)}
                        </span>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Needs Analysis */}
                <Card className="backdrop-blur-sm">
                  <CardHeader>
                    <CardTitle className="text-white">Offseason Needs</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div>
                        <h4 className="text-green-400 font-medium mb-2">✅ Addressed</h4>
                        <p className="text-white text-sm">{currentTeamData.context?.needs_addressed || 'N/A'}</p>
                      </div>
                      <div>
                        <h4 className="text-red-400 font-medium mb-2">❌ Still Needed</h4>
                        <p className="text-white text-sm">{currentTeamData.context?.needs_remaining || 'N/A'}</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                {/* Coaching Changes */}
                {currentTeamData.coaching_changes && currentTeamData.coaching_changes.length > 0 && (
                  <Card className="backdrop-blur-sm">
                    <CardHeader>
                      <CardTitle className="text-white">Coaching Changes</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-2">
                        {currentTeamData.coaching_changes.map((change, idx) => (
                          <div key={idx} className="p-3 rounded-lg" style={{backgroundColor: 'rgba(251, 191, 36, 0.1)', border: '1px solid rgba(251, 191, 36, 0.2)'}}>
                            <span className="text-white text-sm">{change}</span>
                          </div>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                )}
              </div>
            </div>

            {/* Bottom Analysis Cards */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              {/* Key Additions Analysis */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Star className="w-5 h-5 mr-2 text-yellow-400" />
                    Top 5 Impact Additions
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {currentTeamData.key_additions && currentTeamData.key_additions.slice(0, 5).map((addition, idx) => (
                      <div key={idx} className="flex items-center space-x-3">
                        <span className="text-yellow-400 font-bold">#{idx + 1}</span>
                        <span className="text-white text-sm">{addition}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              {/* Key Losses Analysis */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <AlertCircle className="w-5 h-5 mr-2 text-red-400" />
                    Biggest Losses
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {currentTeamData.key_losses && currentTeamData.key_losses.slice(0, 5).map((loss, idx) => (
                      <div key={idx} className="flex items-center space-x-3">
                        <span className="text-red-400 font-bold">#{idx + 1}</span>
                        <span className="text-white text-sm">{loss}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}

        {/* Division Analysis View */}
        {view === 'division' && (
          <div className="space-y-6">
            
            {/* Division Header & Selector */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h1 className="text-3xl font-bold text-white">Division Analysis</h1>
                  <p className="text-slate-400">Competitive balance and head-to-head offseason comparisons</p>
                </div>
                <div className="text-right">
                  <select 
                    value={selectedDivision}
                    onChange={(e) => setSelectedDivision(e.target.value)}
                    className="px-4 py-2 rounded-lg text-white text-lg font-medium"
                    style={{backgroundColor: '#334155', borderColor: '#475569'}}
                  >
                    <option value="AFC North">AFC North</option>
                    <option value="AFC East">AFC East</option>
                    <option value="AFC South">AFC South</option>
                    <option value="AFC West">AFC West</option>
                    <option value="NFC East">NFC East</option>
                    <option value="NFC North">NFC North</option>
                    <option value="NFC South">NFC South</option>
                    <option value="NFC West">NFC West</option>
                  </select>
                </div>
              </div>
            </div>

            {/* Division Overview Cards */}
            {divisionData && (
              <>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                  <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-blue-400 text-sm font-medium">Division Winner</p>
                          <p className="text-xl font-bold text-white">{divisionData.division_info.best_team}</p>
                        </div>
                        <Trophy className="w-8 h-8 text-blue-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-green-400 text-sm font-medium">Best Offseason</p>
                          <p className="text-xl font-bold text-white">{divisionData.division_info.best_offseason}</p>
                        </div>
                        <Star className="w-8 h-8 text-green-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-purple-400 text-sm font-medium">Most Active</p>
                          <p className="text-xl font-bold text-white">{divisionData.division_info.most_active}</p>
                        </div>
                        <Users className="w-8 h-8 text-purple-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-yellow-500/20 to-yellow-600/20 border-yellow-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-yellow-400 text-sm font-medium">Total Moves</p>
                          <p className="text-xl font-bold text-white">{divisionData.division_info.total_moves}</p>
                        </div>
                        <TrendingUp className="w-8 h-8 text-yellow-400" />
                      </div>
                    </CardContent>
                  </Card>
                </div>

                {/* Division Teams Comparison */}
                <Card className="backdrop-blur-sm">
                  <CardHeader>
                    <CardTitle className="text-white flex items-center">
                      <Target className="w-5 h-5 mr-2 text-purple-400" />
                      {selectedDivision} Head-to-Head Comparison
                      <span className="ml-auto text-sm text-slate-400">
                        Competitive Balance: {divisionData.division_info.competitive_balance.toFixed(1)}/10
                      </span>
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="overflow-x-auto">
                      <table className="w-full" style={{backgroundColor: 'transparent'}}>
                        <thead>
                          <tr className="border-b" style={{borderColor: '#334155'}}>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Team</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">2025 Rank</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Offseason Grade</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Net Impact</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Key Addition</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Division Outlook</th>
                          </tr>
                        </thead>
                        <tbody>
                          {divisionData.teams.map((team, idx) => {
                            const teamRanking = powerRankings.find(r => r.team === team.team);
                            return (
                              <tr 
                                key={team.team} 
                                className="border-b hover:bg-slate-700/30 cursor-pointer transition-colors"
                                style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                                onClick={() => {
                                  setSelectedTeam(team.team);
                                  setView('team');
                                }}
                              >
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="flex items-center space-x-3">
                                    <div className={`w-8 h-8 rounded flex items-center justify-center text-xs font-bold text-white ${
                                      idx === 0 ? 'bg-yellow-500' : idx === 1 ? 'bg-gray-400' : idx === 2 ? 'bg-orange-600' : 'bg-red-600'
                                    }`}>
                                      {team.team}
                                    </div>
                                    <div>
                                      <div className="text-white font-medium">{team.team_name}</div>
                                      <div className="text-xs text-slate-400">
                                        {idx === 0 ? '🏆 Division Leader' :
                                         idx === 1 ? '🥈 Wild Card Hope' :
                                         idx === 2 ? '🥉 Fighting for .500' :
                                         '💀 Rebuild Mode'}
                                      </div>
                                    </div>
                                  </div>
                                </td>
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="text-white font-bold text-lg">#{team.final_rank}</div>
                                  {teamRanking && (
                                    <div className="flex items-center space-x-1 text-xs">
                                      {getRankingMovementIcon(teamRanking.rank_change)}
                                      <span className={teamRanking.rank_change > 0 ? 'text-green-400' : teamRanking.rank_change < 0 ? 'text-red-400' : 'text-slate-400'}>
                                        {teamRanking.rank_change > 0 ? '+' : ''}{teamRanking.rank_change}
                                      </span>
                                    </div>
                                  )}
                                </td>
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <span className={`px-3 py-1 rounded-full text-sm font-medium ${getGradeColor(team.offseason_grade)}`}>
                                    {team.offseason_grade}
                                  </span>
                                </td>
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="flex items-center space-x-2">
                                    <span className={`font-bold text-lg ${
                                      team.net_impact > 2 ? 'text-green-400' : 
                                      team.net_impact > 0 ? 'text-blue-400' : 
                                      team.net_impact > -2 ? 'text-yellow-400' : 'text-red-400'
                                    }`}>
                                      {formatImpact(team.net_impact)}
                                    </span>
                                    <div className="w-12 bg-slate-700 rounded-full h-2">
                                      <div 
                                        className={`h-2 rounded-full ${
                                          team.net_impact > 2 ? 'bg-green-400' : 
                                          team.net_impact > 0 ? 'bg-blue-400' : 
                                          team.net_impact > -2 ? 'bg-yellow-400' : 'bg-red-400'
                                        }`}
                                        style={{width: `${Math.min(100, Math.max(10, (team.net_impact + 5) * 10))}%`}}
                                      ></div>
                                    </div>
                                  </div>
                                </td>
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="text-white text-sm">
                                    {teamRanking?.key_additions?.[0] || 'No major additions'}
                                  </div>
                                </td>
                                <td className="py-4 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="text-sm">
                                    {idx === 0 ? (
                                      <span className="text-green-400 font-medium">Division Favorite</span>
                                    ) : idx === 1 ? (
                                      <span className="text-blue-400 font-medium">Playoff Contender</span>
                                    ) : idx === 2 ? (
                                      <span className="text-yellow-400 font-medium">Middling Team</span>
                                    ) : (
                                      <span className="text-red-400 font-medium">Bottom Feeder</span>
                                    )}
                                    <div className="text-xs text-slate-400 mt-1">
                                      Team Rating: {teamRanking?.final_2025_rating?.toFixed(1) || 'N/A'}/100
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            );
                          })}
                        </tbody>
                      </table>
                    </div>
                  </CardContent>
                </Card>

                {/* Division Storylines */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  
                  {/* Key Storylines */}
                  <Card className="backdrop-blur-sm">
                    <CardHeader>
                      <CardTitle className="text-white flex items-center">
                        <AlertCircle className="w-5 h-5 mr-2 text-blue-400" />
                        {selectedDivision} Key Storylines
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        <div className="p-4 rounded-lg" style={{backgroundColor: 'rgba(59, 130, 246, 0.1)', borderColor: 'rgba(59, 130, 246, 0.3)', border: '1px solid'}}>
                          <h4 className="text-blue-400 font-medium mb-2">Division Winner Prediction</h4>
                          <p className="text-white text-sm">
                            <strong>{divisionData.division_info.best_team}</strong> emerges as the clear favorite after their strong offseason. 
                            With {formatImpact(divisionData.division_info.avg_net_impact)} average net impact across the division, 
                            competitive balance is {divisionData.division_info.competitive_balance < 5 ? 'low' : 'high'}.
                          </p>
                        </div>
                        
                        <div className="p-4 rounded-lg" style={{backgroundColor: 'rgba(34, 197, 94, 0.1)', borderColor: 'rgba(34, 197, 94, 0.3)', border: '1px solid'}}>
                          <h4 className="text-green-400 font-medium mb-2">Biggest Offseason Winner</h4>
                          <p className="text-white text-sm">
                            <strong>{divisionData.division_info.best_offseason}</strong> had the most impactful offseason in the division, 
                            positioning themselves for a potential breakthrough season.
                          </p>
                        </div>
                        
                        <div className="p-4 rounded-lg" style={{backgroundColor: 'rgba(168, 85, 247, 0.1)', borderColor: 'rgba(168, 85, 247, 0.3)', border: '1px solid'}}>
                          <h4 className="text-purple-400 font-medium mb-2">Most Active Front Office</h4>
                          <p className="text-white text-sm">
                            <strong>{divisionData.division_info.most_active}</strong> led the division with the most roster moves, 
                            showing an aggressive approach to improvement.
                          </p>
                        </div>
                      </div>
                    </CardContent>
                  </Card>

                  {/* Division Moves Summary */}
                  <Card className="backdrop-blur-sm">
                    <CardHeader>
                      <CardTitle className="text-white flex items-center">
                        <BarChart3 className="w-5 h-5 mr-2 text-green-400" />
                        Division Move Analysis
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        {divisionData.teams.map((team, idx) => {
                          const teamMoves = divisionMoves[team.team] || [];
                          const highImpactMoves = teamMoves.filter(m => m.impact_score >= 1.5);
                          
                          return (
                            <div key={team.team} className="flex items-center justify-between p-3 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                              <div className="flex items-center space-x-3">
                                <div className={`w-6 h-6 rounded flex items-center justify-center text-xs font-bold text-white ${
                                  idx === 0 ? 'bg-yellow-500' : idx === 1 ? 'bg-gray-400' : idx === 2 ? 'bg-orange-600' : 'bg-red-600'
                                }`}>
                                  {team.team}
                                </div>
                                <span className="text-white font-medium">{team.team_name}</span>
                              </div>
                              <div className="text-right">
                                <div className="text-white font-bold">{highImpactMoves.length} high-impact</div>
                                <div className="text-xs text-slate-400">{teamMoves.length} total moves</div>
                              </div>
                            </div>
                          );
                        })}
                        
                        <div className="mt-4 p-3 border-t" style={{borderColor: '#334155'}}>
                          <div className="flex justify-between text-sm">
                            <span className="text-slate-400">Division Total:</span>
                            <span className="text-white font-medium">{divisionData.division_info.total_moves} moves</span>
                          </div>
                          <div className="flex justify-between text-sm mt-1">
                            <span className="text-slate-400">Avg Impact:</span>
                            <span className="text-blue-400 font-medium">{formatImpact(divisionData.division_info.avg_net_impact)}</span>
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </>
            )}
          </div>
        )}

        {/* Moves View */}
        // Replace the moves view section in your index.js (around line 1400+)
        // This goes where you currently have the placeholder "Moves table implementation continues here..."

        {view === 'moves' && (
          <div className="space-y-6">
            
            {/* Moves Header & Filters - keep your existing header */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h1 className="text-3xl font-bold text-white">Player Moves Analysis</h1>
                  <p className="text-slate-400">All 876 moves with impact scoring and filtering</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-blue-400">{movesStats.total_found}</div>
                  <p className="text-slate-400 text-sm">
                    {movesStats.total_displayed < movesStats.total_found 
                      ? `Showing ${movesStats.total_displayed} of ${movesStats.total_found}`
                      : 'Total Moves Found'
                    }
                  </p>
                </div>
              </div>
              
              {/* Keep your existing filters section */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-2">Team</label>
                  <select 
                    value={selectedTeam}
                    onChange={(e) => setSelectedTeam(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg text-white"
                    style={{backgroundColor: '#334155', borderColor: '#475569'}}
                  >
                    <option value="">All Teams</option>
                    {powerRankings.map(team => (
                      <option key={team.team} value={team.team}>{team.team} - {team.team_name}</option>
                    ))}
                  </select>
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-2">Position</label>
                  <select 
                    value={filterPosition}
                    onChange={(e) => setFilterPosition(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg text-white"
                    style={{backgroundColor: '#334155', borderColor: '#475569'}}
                  >
                    <option value="">All Positions</option>
                    <option value="QB">Quarterback</option>
                    <option value="RB">Running Back</option>
                    <option value="WR">Wide Receiver</option>
                    <option value="TE">Tight End</option>
                    <option value="OL">Offensive Line</option>
                    <option value="DL">Defensive Line</option>
                    <option value="LB">Linebacker</option>
                    <option value="DB">Defensive Back</option>
                  </select>
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-2">Move Type</label>
                  <select 
                    value={filterMoveType}
                    onChange={(e) => setFilterMoveType(e.target.value)}
                    className="w-full px-3 py-2 rounded-lg text-white"
                    style={{backgroundColor: '#334155', borderColor: '#475569'}}
                  >
                    <option value="">All Move Types</option>
                    <option value="Free Agent Signing">Free Agent Signing</option>
                    <option value="Trade">Trade</option>
                    <option value="Draft">Draft Pick</option>
                    <option value="Extension">Extension</option>
                    <option value="Release">Release</option>
                  </select>
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-slate-400 mb-2">Min Impact</label>
                  <input 
                    type="number"
                    step="0.1"
                    min="0"
                    max="3"
                    placeholder="0.5"
                    className="w-full px-3 py-2 rounded-lg text-white placeholder-slate-400"
                    style={{backgroundColor: '#334155', borderColor: '#475569'}}
                    onChange={(e) => {
                      const value = e.target.value ? parseFloat(e.target.value) : null;
                      loadFilteredMoves(selectedTeam, filterPosition, filterMoveType, value);
                    }}
                  />
                </div>
              </div>
            </div>

            {/* ACTUAL MOVES TABLE - This is what was missing! */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Filter className="w-5 h-5 mr-2 text-purple-400" />
                  Player Moves ({recentMoves.length} found)
                  <span className="ml-auto text-sm text-slate-400">
                    Impact scoring enabled
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                {recentMoves.length === 0 ? (
                  <div className="text-center py-8">
                    <AlertCircle className="w-12 h-12 mx-auto mb-4 text-slate-400" />
                    <p className="text-slate-400 text-lg">No moves found matching your filters</p>
                    <p className="text-slate-500 text-sm mt-2">Try adjusting your filters or search criteria</p>
                  </div>
                ) : (
                  <>
                    {/* Pagination Info */}
                    <div className="flex justify-between items-center mb-4">
                      <p className="text-slate-400 text-sm">
                        Showing {recentMoves.length} of {movesStats.total_found} total moves
                      </p>
                      <div className="flex items-center space-x-2">
                        <span className="text-slate-400 text-sm">Sort:</span>
                        <select 
                          className="px-2 py-1 rounded text-white text-sm"
                          style={{backgroundColor: '#334155'}}
                          onChange={(e) => {
                            const sortBy = e.target.value;
                            let sorted = [...recentMoves];
                            
                            if (sortBy === 'impact') {
                              sorted.sort((a, b) => (b.impact_score || 0) - (a.impact_score || 0));
                            } else if (sortBy === 'name') {
                              sorted.sort((a, b) => (a.player_name || '').localeCompare(b.player_name || ''));
                            } else if (sortBy === 'team') {
                              sorted.sort((a, b) => (a.to_team || '').localeCompare(b.to_team || ''));
                            } else if (sortBy === 'type') {
                              sorted.sort((a, b) => (a.move_type || '').localeCompare(b.move_type || ''));
                            }
                            
                            setRecentMoves(sorted);
                          }}
                        >
                          <option value="impact">Impact Score</option>
                          <option value="name">Player Name</option>
                          <option value="team">Team</option>
                          <option value="type">Move Type</option>
                        </select>
                      </div>
                    </div>

                    {/* Moves Table */}
                    <div className="overflow-x-auto">
                      <table className="w-full" style={{backgroundColor: 'transparent'}}>
                        <thead>
                          <tr className="border-b" style={{borderColor: '#334155'}}>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Player</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Move</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Teams</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Contract</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">Impact</th>
                            <th className="text-left py-3 px-2 text-slate-400 font-medium">2024 Stats</th>
                          </tr>
                        </thead>
                        <tbody>
                          {recentMoves.slice(0, 50).map((move, idx) => {
                            const impactScore = move.impact_score || 0;
                            const contractValue = move.contract_value || 0;
                            const contractYears = move.contract_years || 0;
                            
                            return (
                              <tr 
                                key={`${move.player_name}-${idx}`}
                                className="border-b hover:bg-slate-700/30 transition-colors"
                                style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                              >
                                {/* Player Info */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div>
                                    <div className="text-white font-medium">{move.player_name || 'Unknown'}</div>
                                    <div className="text-xs text-slate-400">
                                      {move.position || 'N/A'} • Age {move.age || 'N/A'}
                                    </div>
                                  </div>
                                </td>

                                {/* Move Type */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="flex items-center space-x-2">
                                    <span className={`w-2 h-2 rounded-full ${
                                      move.move_type === 'Free Agent Signing' ? 'bg-green-400' :
                                      move.move_type === 'Trade' ? 'bg-blue-400' :
                                      move.move_type === 'Draft Pick' || move.move_type?.includes('Draft') ? 'bg-yellow-400' :
                                      move.move_type === 'Extension' ? 'bg-purple-400' :
                                      move.move_type === 'Release' ? 'bg-red-400' :
                                      'bg-slate-400'
                                    }`}></span>
                                    <span className="text-white text-sm">{move.move_type || 'Unknown'}</span>
                                  </div>
                                </td>

                                {/* Teams */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="flex items-center space-x-2">
                                    <span className="text-slate-300">{move.from_team || 'N/A'}</span>
                                    <span className="text-slate-500">→</span>
                                    <span className="text-white font-medium">{move.to_team || 'N/A'}</span>
                                  </div>
                                </td>

                                {/* Contract */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  {contractValue > 0 ? (
                                    <div>
                                      <div className="text-white font-medium">
                                        ${contractValue >= 1000000 ? 
                                          `${(contractValue / 1000000).toFixed(1)}M` : 
                                          contractValue >= 1000 ?
                                          `${(contractValue / 1000).toFixed(0)}K` :
                                          contractValue.toLocaleString()
                                        }
                                      </div>
                                      <div className="text-xs text-slate-400">
                                        {contractYears > 0 ? `${contractYears} years` : 'Unknown term'}
                                      </div>
                                    </div>
                                  ) : (
                                    <span className="text-slate-400 text-sm">N/A</span>
                                  )}
                                </td>

                                {/* Impact Score */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="flex items-center space-x-2">
                                    {(() => {
                                      // Calculate display impact based on move type and selected team
                                      let displayImpact = impactScore;
                                      
                                      // If a team is selected and this is a loss for that team
                                      if (selectedTeam && (
                                        (move.move_type === 'Free Agent Loss' && move.from_team === selectedTeam) ||
                                        (move.move_type === 'Trade' && move.from_team === selectedTeam) ||
                                        (move.move_type === 'Release' && move.from_team === selectedTeam) ||
                                        (move.move_type === 'Retirement' && move.from_team === selectedTeam) ||
                                        (move.move_type === 'Post-June 1 Cut' && move.from_team === selectedTeam)
                                      )) {
                                        displayImpact = -Math.abs(impactScore);
                                      }
                                      
                                      const absImpact = Math.abs(displayImpact);
                                      const isNegative = displayImpact < 0;
                                      
                                      return (
                                        <>
                                          <span className={`font-bold text-lg ${
                                            isNegative ? 'text-red-400' :
                                            absImpact >= 2 ? 'text-green-400' :
                                            absImpact >= 1 ? 'text-blue-400' :
                                            absImpact >= 0.5 ? 'text-yellow-400' :
                                            'text-slate-400'
                                          }`}>
                                            {displayImpact > 0 ? '+' : ''}{displayImpact.toFixed(1)}
                                          </span>
                                          <div className="w-8 bg-slate-700 rounded-full h-1">
                                            <div 
                                              className={`h-1 rounded-full ${
                                                isNegative ? 'bg-red-400' :
                                                absImpact >= 2 ? 'bg-green-400' :
                                                absImpact >= 1 ? 'bg-blue-400' :
                                                absImpact >= 0.5 ? 'bg-yellow-400' :
                                                'bg-slate-400'
                                              }`}
                                              style={{width: `${Math.min(100, (absImpact / 3) * 100)}%`}}
                                            ></div>
                                          </div>
                                        </>
                                      );
                                    })()}
                                  </div>
                                </td>

                                {/* 2024 Stats */}
                                <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                                  <div className="text-sm">
                                    <div className="text-white">
                                      Grade: {move['2024_grade'] || 'N/A'}
                                    </div>
                                    <div className="text-xs text-slate-400">
                                      {move.snap_percentage_2024 ? `${move.snap_percentage_2024}% snaps` : 'No snap data'}
                                    </div>
                                  </div>
                                </td>
                              </tr>
                            );
                          })}
                        </tbody>
                      </table>
                    </div>

                    {/* Show more button if there are more moves */}
                    {recentMoves.length > 50 && (
                      <div className="text-center mt-6">
                        <button 
                          className="px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-lg text-white transition-colors"
                          onClick={() => {
                            // You could implement pagination here
                            console.log('Show more moves - implement pagination');
                          }}
                        >
                          Show More Moves ({recentMoves.length - 50} remaining)
                        </button>
                      </div>
                    )}
                  </>
                )}
              </CardContent>
            </Card>

            {/* Move Type Legend */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white text-lg">Move Type Legend</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-2 md:grid-cols-6 gap-4">
                  {[
                    {type: 'Free Agent Signing', color: 'bg-green-400', count: recentMoves.filter(m => m.move_type === 'Free Agent Signing').length},
                    {type: 'Trade', color: 'bg-blue-400', count: recentMoves.filter(m => m.move_type === 'Trade').length},
                    {type: 'Draft Pick', color: 'bg-yellow-400', count: recentMoves.filter(m => m.move_type?.includes('Draft')).length},
                    {type: 'Extension', color: 'bg-purple-400', count: recentMoves.filter(m => m.move_type === 'Extension').length},
                    {type: 'Release', color: 'bg-red-400', count: recentMoves.filter(m => m.move_type === 'Release').length},
                    {type: 'Other', color: 'bg-slate-400', count: recentMoves.filter(m => !['Free Agent Signing', 'Trade', 'Extension', 'Release'].includes(m.move_type) && !m.move_type?.includes('Draft')).length}
                  ].map(({type, color, count}) => (
                    <div key={type} className="flex items-center space-x-2">
                      <div className={`w-3 h-3 rounded-full ${color}`}></div>
                      <span className="text-white text-sm">{type}</span>
                      <span className="text-slate-400 text-xs">({count})</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>
        )}
      </div>
    </div>
  );
};

export default NFLAnalyticsDashboard;
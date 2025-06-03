import React, { useState, useEffect } from 'react';
import { Search, TrendingUp, TrendingDown, Users, DollarSign, Brain, Target, AlertCircle, ChevronRight, Star, Filter, Loader2, Trophy, BarChart3, ArrowUp, ArrowDown, Minus } from 'lucide-react';

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

  const [selectedTeam, setSelectedTeam] = useState('BAL');
  const [searchQuery, setSearchQuery] = useState('');
  const [powerRankings, setPowerRankings] = useState([]);
  const [currentTeamData, setCurrentTeamData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [view, setView] = useState('rankings'); // 'rankings', 'team', 'division', 'moves'
  const [filterPosition, setFilterPosition] = useState('');
  const [filterMoveType, setFilterMoveType] = useState('');
  const [recentMoves, setRecentMoves] = useState([]);

  // API base URL
  const API_BASE = 'http://localhost:8000';

  // Load initial data
  useEffect(() => {
    loadPowerRankings();
    loadRecentMoves();
  }, []);

  // Load team-specific data when selection changes
  useEffect(() => {
    if (selectedTeam) {
      loadTeamData(selectedTeam);
    }
  }, [selectedTeam]);

  const loadPowerRankings = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_BASE}/api/rankings`);
      const data = await response.json();
      setPowerRankings(data.rankings || []);
      setLoading(false);
    } catch (error) {
      console.error('Error loading rankings:', error);
      setLoading(false);
    }
  };

  const loadTeamData = async (team) => {
    try {
      const response = await fetch(`${API_BASE}/api/teams/${team}`);
      const data = await response.json();
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
      let url = `${API_BASE}/api/moves?limit=100`;
      
      if (team) url += `&team=${team}`;
      if (position) url += `&position=${position}`;
      if (moveType) url += `&move_type=${encodeURIComponent(moveType)}`;
      if (minImpact !== null) url += `&min_impact=${minImpact}`;
      
      const response = await fetch(url);
      const data = await response.json();
      setRecentMoves(data.moves || []);
    } catch (error) {
      console.error('Error loading filtered moves:', error);
    }
  };

  // Load filtered moves when filters change
  useEffect(() => {
    if (view === 'moves') {
      loadFilteredMoves(selectedTeam, filterPosition, filterMoveType);
    }
  }, [view, selectedTeam, filterPosition, filterMoveType]);

  const getRankingMovementIcon = (rankChange) => {
    if (rankChange > 0) return <ArrowUp className="w-4 h-4 text-green-400" />;
    if (rankChange < 0) return <ArrowDown className="w-4 h-4 text-red-400" />;
    return <Minus className="w-4 h-4 text-slate-400" />;
  };

  const getGradeColor = (grade) => {
    if (grade.startsWith('A')) return 'text-green-400 bg-green-400/20';
    if (grade.startsWith('B')) return 'text-blue-400 bg-blue-400/20';
    if (grade.startsWith('C')) return 'text-yellow-400 bg-yellow-400/20';
    if (grade.startsWith('D')) return 'text-orange-400 bg-orange-400/20';
    return 'text-red-400 bg-red-400/20';
  };

  const formatImpact = (impact) => {
    return impact > 0 ? `+${impact.toFixed(1)}` : impact.toFixed(1);
  };

  const getTopMovers = () => {
    if (!powerRankings.length) return { climbers: [], drops: [] };
    
    const sorted = [...powerRankings].sort((a, b) => b.rank_change - a.rank_change);
    return {
      climbers: sorted.filter(team => team.rank_change > 0).slice(0, 3),
      drops: sorted.filter(team => team.rank_change < 0).slice(-3).reverse()
    };
  };

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
                  { key: 'team', label: 'Teams', icon: Users },
                  { key: 'moves', label: 'Moves', icon: TrendingUp }
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
                                <span className={team.rank_change > 0 ? 'text-green-400' : team.rank_change < 0 ? 'text-red-400' : 'text-slate-400'}>
                                  {Math.abs(team.rank_change)}
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

        {/* Moves View */}
        {view === 'moves' && (
          <div className="space-y-6">
            
            {/* Moves Header & Filters */}
            <div className="bg-gradient-to-r from-slate-800/50 to-slate-700/50 backdrop-blur-sm rounded-lg border p-6" style={{backgroundColor: 'rgba(30, 41, 59, 0.5)', borderColor: '#334155'}}>
              <div className="flex items-center justify-between mb-4">
                <div>
                  <h1 className="text-3xl font-bold text-white">Player Moves Analysis</h1>
                  <p className="text-slate-400">All 876 moves with impact scoring and filtering</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-blue-400">{recentMoves.length}</div>
                  <p className="text-slate-400 text-sm">High-Impact Moves</p>
                </div>
              </div>
              
              {/* Filters */}
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

            {/* Moves Table */}
            <Card className="backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Target className="w-5 h-5 mr-2 text-purple-400" />
                  Player Moves Database
                  <span className="ml-auto text-sm text-slate-400">
                    {selectedTeam ? `${selectedTeam} Team Moves` : 'All NFL Moves'}
                  </span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full" style={{backgroundColor: 'transparent'}}>
                    <thead>
                      <tr className="border-b" style={{borderColor: '#334155'}}>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Player</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Position</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Move</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Type</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Impact</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Grade Change</th>
                        <th className="text-left py-3 px-2 text-slate-400 font-medium">Contract</th>
                      </tr>
                    </thead>
                    <tbody>
                      {recentMoves.map((move, idx) => (
                        <tr 
                          key={idx} 
                          className="border-b hover:bg-slate-700/30 transition-colors"
                          style={{borderColor: 'rgba(51, 65, 85, 0.5)'}}
                        >
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div>
                              <div className="text-white font-medium">{move.player_name}</div>
                              <div className="text-xs text-slate-400">
                                {move.importance_old?.toFixed(1)}/10 → {move.importance_new?.toFixed(1)}/10
                              </div>
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className="inline-block px-2 py-1 rounded text-xs font-medium bg-blue-400/20 text-blue-400">
                              {move.position}
                            </span>
                            <div className="text-xs text-slate-400 mt-1">{move.position_group}</div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="flex items-center space-x-2">
                              <span className="text-xs px-2 py-1 rounded" style={{
                                backgroundColor: move.from_team === 'DRAFT' ? 'rgba(168, 85, 247, 0.2)' :
                                               move.to_team === 'RELEASED' ? 'rgba(239, 68, 68, 0.2)' : 
                                               'rgba(34, 197, 94, 0.2)',
                                color: move.from_team === 'DRAFT' ? '#c084fc' :
                                       move.to_team === 'RELEASED' ? '#f87171' : '#4ade80'
                              }}>
                                {move.from_team}
                              </span>
                              <span className="text-slate-400">→</span>
                              <span className="text-xs px-2 py-1 rounded" style={{
                                backgroundColor: move.to_team === 'RELEASED' ? 'rgba(239, 68, 68, 0.2)' : 'rgba(59, 130, 246, 0.2)',
                                color: move.to_team === 'RELEASED' ? '#f87171' : '#60a5fa'
                              }}>
                                {move.to_team}
                              </span>
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <span className="text-white text-sm">{move.move_type}</span>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="flex items-center space-x-2">
                              <span className={`font-bold text-lg ${
                                move.impact_score > 1.5 ? 'text-green-400' : 
                                move.impact_score > 1.0 ? 'text-blue-400' : 
                                move.impact_score > 0.5 ? 'text-yellow-400' : 'text-slate-400'
                              }`}>
                                {move.impact_score.toFixed(1)}
                              </span>
                              <div className="w-16 bg-slate-700 rounded-full h-2">
                                <div 
                                  className={`h-2 rounded-full ${
                                    move.impact_score > 1.5 ? 'bg-green-400' : 
                                    move.impact_score > 1.0 ? 'bg-blue-400' : 
                                    move.impact_score > 0.5 ? 'bg-yellow-400' : 'bg-slate-400'
                                  }`}
                                  style={{width: `${Math.min(100, (move.impact_score / 2.5) * 100)}%`}}
                                ></div>
                              </div>
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            <div className="text-sm">
                              <div className="text-slate-400">2024: {move.grade_2024.toFixed(1)}</div>
                              <div className={`${
                                move.projected_2025 > move.grade_2024 ? 'text-green-400' : 
                                move.projected_2025 < move.grade_2024 ? 'text-red-400' : 'text-slate-400'
                              }`}>
                                2025: {move.projected_2025.toFixed(1)}
                                <span className="ml-1">
                                  ({move.projected_2025 > move.grade_2024 ? '+' : ''}{(move.projected_2025 - move.grade_2024).toFixed(1)})
                                </span>
                              </div>
                            </div>
                          </td>
                          <td className="py-3 px-2" style={{backgroundColor: 'transparent'}}>
                            {move.contract_value && move.contract_value > 0 ? (
                              <div className="text-sm">
                                <div className="text-white font-medium">
                                  ${(move.contract_value / 1000000).toFixed(1)}M
                                </div>
                                <div className="text-xs text-slate-400">
                                  {move.contract_years}yr
                                </div>
                              </div>
                            ) : (
                              <span className="text-slate-500 text-sm">-</span>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                
                {recentMoves.length === 0 && (
                  <div className="text-center py-8">
                    <div className="text-slate-400 mb-2">No moves found matching your filters</div>
                    <button 
                      onClick={() => {
                        setSelectedTeam('');
                        setFilterPosition('');
                        setFilterMoveType('');
                        loadRecentMoves();
                      }}
                      className="text-blue-400 hover:text-blue-300 text-sm"
                    >
                      Clear all filters
                    </button>
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Move Impact Summary Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-green-400 text-sm font-medium">High Impact Moves</p>
                      <p className="text-2xl font-bold text-white">
                        {recentMoves.filter(m => m.impact_score >= 1.5).length}
                      </p>
                    </div>
                    <TrendingUp className="w-8 h-8 text-green-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-blue-400 text-sm font-medium">Medium Impact</p>
                      <p className="text-2xl font-bold text-white">
                        {recentMoves.filter(m => m.impact_score >= 1.0 && m.impact_score < 1.5).length}
                      </p>
                    </div>
                    <Target className="w-8 h-8 text-blue-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-purple-400 text-sm font-medium">Total Contract Value</p>
                      <p className="text-2xl font-bold text-white">
                        ${(recentMoves.reduce((sum, move) => sum + (move.contract_value || 0), 0) / 1000000).toFixed(0)}M
                      </p>
                    </div>
                    <DollarSign className="w-8 h-8 text-purple-400" />
                  </div>
                </CardContent>
              </Card>
            </div>
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
              <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-blue-400 text-sm font-medium">Final Rank</p>
                      <p className="text-2xl font-bold text-white">#{currentTeamData.ranking_info.final_2025_rank}</p>
                    </div>
                    <Trophy className="w-8 h-8 text-blue-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-green-400 text-sm font-medium">Net Impact</p>
                      <p className="text-2xl font-bold text-white">{formatImpact(currentTeamData.net_impact)}</p>
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
                      <p className="text-2xl font-bold text-white">{currentTeamData.total_moves}</p>
                    </div>
                    <Users className="w-8 h-8 text-purple-400" />
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-gradient-to-r from-yellow-500/20 to-yellow-600/20 border-yellow-500/30">
                <CardContent className="p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-yellow-400 text-sm font-medium">Efficiency</p>
                      <p className="text-2xl font-bold text-white">{currentTeamData.move_efficiency.toFixed(1)}</p>
                    </div>
                    <Target className="w-8 h-8 text-yellow-400" />
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Team Analysis Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              {/* Key Moves */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white">Key Roster Moves</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div>
                      <h4 className="text-green-400 font-medium mb-3 flex items-center">
                        <TrendingUp className="w-4 h-4 mr-2" />
                        Major Additions ({currentTeamData.players_gained})
                      </h4>
                      <div className="space-y-2">
                        {currentTeamData.key_additions.slice(0, 5).map((addition, idx) => (
                          <div key={idx} className="flex items-center justify-between p-3 border rounded" style={{backgroundColor: 'rgba(34, 197, 94, 0.1)', borderColor: 'rgba(34, 197, 94, 0.2)'}}>
                            <span className="text-white text-sm">{addition}</span>
                            <ChevronRight className="w-4 h-4 text-green-400" />
                          </div>
                        ))}
                      </div>
                    </div>

                    <div>
                      <h4 className="text-red-400 font-medium mb-3 flex items-center">
                        <TrendingDown className="w-4 h-4 mr-2" />
                        Key Departures ({currentTeamData.players_lost})
                      </h4>
                      <div className="space-y-2">
                        {currentTeamData.key_losses.slice(0, 5).map((loss, idx) => (
                          <div key={idx} className="flex items-center justify-between p-3 border rounded" style={{backgroundColor: 'rgba(239, 68, 68, 0.1)', borderColor: 'rgba(239, 68, 68, 0.2)'}}>
                            <span className="text-white text-sm">{loss}</span>
                            <ChevronRight className="w-4 h-4 text-red-400" />
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Unit Impact Analysis */}
              <Card className="backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white">Unit Impact Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {Object.entries(currentTeamData.unit_impacts).map(([unit, impact]) => (
                      <div key={unit} className="flex items-center justify-between p-4 rounded-lg" style={{backgroundColor: 'rgba(51, 65, 85, 0.5)'}}>
                        <div className="flex items-center space-x-3">
                          <div className={`w-3 h-3 rounded-full ${impact > 0 ? 'bg-green-400' : impact < 0 ? 'bg-red-400' : 'bg-slate-400'}`}></div>
                          <span className="text-white capitalize font-medium">
                            {unit.replace('_', ' ')}
                          </span>
                        </div>
                        <span className={`font-bold text-lg ${impact > 0 ? 'text-green-400' : impact < 0 ? 'text-red-400' : 'text-slate-400'}`}>
                          {formatImpact(impact)}
                        </span>
                      </div>
                    ))}

                    <div className="mt-6 p-4 border rounded-lg" style={{backgroundColor: 'rgba(59, 130, 246, 0.1)', borderColor: 'rgba(59, 130, 246, 0.3)'}}>
                      <div className="flex items-center mb-2">
                        <AlertCircle className="w-5 h-5 text-blue-400 mr-2" />
                        <span className="text-blue-400 font-medium">Strategy Assessment</span>
                      </div>
                      <p className="text-white text-sm mb-2">{currentTeamData.offseason_strategy}</p>
                      <div className="flex items-center justify-between text-xs">
                        <span className="text-slate-400">Move Efficiency:</span>
                        <span className="text-blue-400 font-medium">{currentTeamData.move_efficiency.toFixed(2)}</span>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default NFLAnalyticsDashboard;
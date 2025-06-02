// frontend/pages/index.js
// This connects to your existing NFL analysis via the API

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Search, TrendingUp, TrendingDown, Users, DollarSign, Brain, Target, AlertCircle, ChevronRight, Star, Filter, Loader2 } from 'lucide-react';

// Custom Card components
const Card = ({ children, className = "" }) => (
  <div className={`rounded-lg border bg-card text-card-foreground shadow-sm ${className}`}>
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
  const [selectedTeam, setSelectedTeam] = useState('BAL');
  const [searchQuery, setSearchQuery] = useState('');
  const [teamsData, setTeamsData] = useState({});
  const [currentTeamData, setCurrentTeamData] = useState(null);
  const [bridgeAnalysis, setBridgeAnalysis] = useState(null);
  const [loading, setLoading] = useState(true);
  const [chatMessage, setChatMessage] = useState('');
  const [chatResponse, setChatResponse] = useState(null);
  const [chatLoading, setChatLoading] = useState(false);

  // API base URL
  const API_BASE = 'http://localhost:8000';

  // Load initial data
  useEffect(() => {
    loadInitialData();
  }, []);

  // Load team-specific data when selection changes
  useEffect(() => {
    if (selectedTeam) {
      loadTeamData(selectedTeam);
    }
  }, [selectedTeam]);

  const loadInitialData = async () => {
    try {
      setLoading(true);
      
      // Load all teams data
      const teamsResponse = await axios.get(`${API_BASE}/api/teams`);
      setTeamsData(teamsResponse.data.teams || {});
      
      // Load bridge analysis
      const bridgeResponse = await axios.get(`${API_BASE}/api/analysis/bridge`);
      setBridgeAnalysis(bridgeResponse.data);
      
      setLoading(false);
    } catch (error) {
      console.error('Error loading data:', error);
      setLoading(false);
      
      // Fallback data if API is not available
      setTeamsData({
        'BAL': {
          team: 'BAL',
          name: 'Baltimore Ravens',
          offseasonGrade: 'A-',
          netImpact: '+4.7',
          keyAdditions: ['DeAndre Hopkins (WR)', 'Mike Green (EDGE)', 'Malaki Starks (S)'],
          keyLosses: ['Brandon Stephens (CB)', 'Patrick Mekari (G)', 'Malik Harrison (LB)'],
          projectedWins: 11.5,
          finalRank: 1
        }
      });
    }
  };

  const loadTeamData = async (team) => {
    try {
      const response = await axios.get(`${API_BASE}/api/teams/${team}`);
      setCurrentTeamData(response.data);
    } catch (error) {
      console.error('Error loading team data:', error);
      // Use data from teams list as fallback
      setCurrentTeamData(teamsData[team] || null);
    }
  };

  const handleChat = async () => {
    if (!chatMessage.trim()) return;
    
    setChatLoading(true);
    try {
      const response = await axios.post(`${API_BASE}/api/chat`, null, {
        params: { question: chatMessage }
      });
      setChatResponse(response.data);
      setChatMessage('');
    } catch (error) {
      console.error('Error with chat:', error);
      setChatResponse({
        response: "Sorry, I'm having trouble connecting right now. Please try again later!",
        timestamp: new Date().toISOString()
      });
    }
    setChatLoading(false);
  };

  const aiAgents = [
    {
      name: 'Roster Update Agent',
      icon: <Users className="w-5 h-5" />,
      description: 'Monitors your player_moves data',
      status: 'Active',
      lastUpdate: '2 hours ago'
    },
    {
      name: 'Projection Engine',
      icon: <TrendingUp className="w-5 h-5" />,
      description: 'Uses your bridge framework',
      status: 'Active', 
      lastUpdate: '30 minutes ago'
    },
    {
      name: 'Gridiron GPT',
      icon: <Brain className="w-5 h-5" />,
      description: 'AI trained on your analysis',
      status: 'Ready',
      lastUpdate: 'Always available'
    },
    {
      name: 'Edge Detector',
      icon: <Target className="w-5 h-5" />,
      description: 'Identifies betting opportunities',
      status: 'Active',
      lastUpdate: '1 hour ago'
    }
  ];

  const getTopInsights = () => {
    if (!bridgeAnalysis) return [];
    
    const insights = [];
    
    // Generate insights from bridge analysis
    if (bridgeAnalysis.topTeams && bridgeAnalysis.topTeams.length > 0) {
      const topTeam = bridgeAnalysis.topTeams[0];
      insights.push({
        team: topTeam.team || 'TOP',
        insight: `${topTeam.team_name || 'Top team'} leads offseason improvements`,
        confidence: 87,
        type: 'analysis'
      });
    }
    
    if (bridgeAnalysis.bottomTeams && bridgeAnalysis.bottomTeams.length > 0) {
      const bottomTeam = bridgeAnalysis.bottomTeams[0];
      insights.push({
        team: bottomTeam.team || 'BOT',
        insight: `${bottomTeam.team_name || 'Bottom team'} had rough offseason`,
        confidence: 73,
        type: 'bet'
      });
    }
    
    // Add a general insight
    insights.push({
      team: 'NFL',
      insight: `${bridgeAnalysis.totalMoves || 500}+ moves tracked this offseason`,
      confidence: 95,
      type: 'analysis'
    });
    
    return insights;
  };

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

  const teamsList = Object.keys(teamsData);
  const currentTeam = currentTeamData || teamsData[selectedTeam] || {};

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white">
      {/* Header */}
      <div className="border-b border-slate-700 bg-slate-800/50 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <Brain className="w-6 h-6" />
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                  NFL Offseason Intelligence Hub
                </h1>
                <p className="text-slate-400 text-sm">Powered by your player bridge framework</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="relative">
                <Search className="w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400" />
                <input 
                  type="text"
                  placeholder="Search teams, players, moves..."
                  className="pl-10 pr-4 py-2 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                />
              </div>
              <button className="bg-gradient-to-r from-blue-600 to-purple-600 px-4 py-2 rounded-lg font-medium hover:from-blue-500 hover:to-purple-500 transition-all">
                Export Report
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-6 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
          
          {/* AI Agents Panel */}
          <div className="lg:col-span-1">
            <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Brain className="w-5 h-5 mr-2 text-blue-400" />
                  AI Agents
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                {aiAgents.map((agent, idx) => (
                  <div key={idx} className="flex items-center justify-between p-3 bg-slate-700/50 rounded-lg hover:bg-slate-700 transition-colors cursor-pointer">
                    <div className="flex items-center space-x-3">
                      <div className="text-blue-400">{agent.icon}</div>
                      <div>
                        <div className="text-sm font-medium text-white">{agent.name}</div>
                        <div className="text-xs text-slate-400">{agent.lastUpdate}</div>
                      </div>
                    </div>
                    <div className={`w-2 h-2 rounded-full ${agent.status === 'Active' ? 'bg-green-400' : 'bg-blue-400'}`}></div>
                  </div>
                ))}
              </CardContent>
            </Card>

            {/* Bridge Analysis Stats */}
            {bridgeAnalysis && (
              <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm mt-6">
                <CardHeader>
                  <CardTitle className="text-white flex items-center">
                    <Target className="w-5 h-5 mr-2 text-green-400" />
                    Analysis Stats
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                  <div className="flex justify-between">
                    <span className="text-slate-400">Total Moves</span>
                    <span className="text-white font-medium">{bridgeAnalysis.totalMoves}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-400">Teams Covered</span>
                    <span className="text-white font-medium">{Object.keys(teamsData).length}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-slate-400">Last Updated</span>
                    <span className="text-white font-medium">
                      {new Date(bridgeAnalysis.lastUpdated).toLocaleDateString()}
                    </span>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Top Insights */}
            <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm mt-6">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Target className="w-5 h-5 mr-2 text-green-400" />
                  Edge Alerts
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                {getTopInsights().map((insight, idx) => (
                  <div key={idx} className="p-3 bg-slate-700/50 rounded-lg">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-xs font-medium text-blue-400">{insight.team}</span>
                      <span className="text-xs text-slate-400">{insight.confidence}% confidence</span>
                    </div>
                    <p className="text-sm text-white">{insight.insight}</p>
                    <div className={`inline-block px-2 py-1 rounded text-xs mt-2 ${
                      insight.type === 'bet' ? 'bg-green-500/20 text-green-400' : 'bg-blue-500/20 text-blue-400'
                    }`}>
                      {insight.type}
                    </div>
                  </div>
                ))}
              </CardContent>
            </Card>
          </div>

          {/* Main Content */}
          <div className="lg:col-span-3">
            
            {/* Team Selector */}
            <div className="mb-6">
              <div className="flex items-center space-x-4 mb-4">
                <h2 className="text-xl font-bold text-white">Team Analysis</h2>
                <select 
                  value={selectedTeam}
                  onChange={(e) => setSelectedTeam(e.target.value)}
                  className="bg-slate-700 border border-slate-600 rounded-lg px-3 py-2 text-white"
                >
                  {teamsList.map(team => (
                    <option key={team} value={team}>
                      {teamsData[team]?.name || team}
                    </option>
                  ))}
                </select>
              </div>

              {/* Team Overview Cards */}
              {currentTeam && (
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
                  <Card className="bg-gradient-to-r from-green-500/20 to-green-600/20 border-green-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-green-400 text-sm font-medium">Offseason Grade</p>
                          <p className="text-2xl font-bold text-white">{currentTeam.offseasonGrade || 'N/A'}</p>
                        </div>
                        <Star className="w-8 h-8 text-green-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-blue-500/20 to-blue-600/20 border-blue-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-blue-400 text-sm font-medium">Net Impact</p>
                          <p className="text-2xl font-bold text-white">{currentTeam.netImpact || '0.0'}</p>
                        </div>
                        <TrendingUp className="w-8 h-8 text-blue-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-purple-400 text-sm font-medium">Projected Wins</p>
                          <p className="text-2xl font-bold text-white">{currentTeam.projectedWins || '8.5'}</p>
                        </div>
                        <Target className="w-8 h-8 text-purple-400" />
                      </div>
                    </CardContent>
                  </Card>

                  <Card className="bg-gradient-to-r from-yellow-500/20 to-yellow-600/20 border-yellow-500/30">
                    <CardContent className="p-4">
                      <div className="flex items-center justify-between">
                        <div>
                          <p className="text-yellow-400 text-sm font-medium">Final Rank</p>
                          <p className="text-2xl font-bold text-white">#{currentTeam.finalRank || '16'}</p>
                        </div>
                        <DollarSign className="w-8 h-8 text-yellow-400" />
                      </div>
                    </CardContent>
                  </Card>
                </div>
              )}
            </div>

            {/* Detailed Analysis */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              {/* Key Moves */}
              <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white">Key Roster Moves</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div>
                      <h4 className="text-green-400 font-medium mb-2 flex items-center">
                        <TrendingUp className="w-4 h-4 mr-2" />
                        Major Additions
                      </h4>
                      <div className="space-y-2">
                        {(currentTeam.keyAdditions || []).map((addition, idx) => (
                          <div key={idx} className="flex items-center justify-between p-2 bg-green-500/10 rounded">
                            <span className="text-white text-sm">{addition}</span>
                            <ChevronRight className="w-4 h-4 text-green-400" />
                          </div>
                        ))}
                      </div>
                    </div>

                    <div>
                      <h4 className="text-red-400 font-medium mb-2 flex items-center">
                        <TrendingDown className="w-4 h-4 mr-2" />
                        Key Departures
                      </h4>
                      <div className="space-y-2">
                        {(currentTeam.keyLosses || []).map((loss, idx) => (
                          <div key={idx} className="flex items-center justify-between p-2 bg-red-500/10 rounded">
                            <span className="text-white text-sm">{loss}</span>
                            <ChevronRight className="w-4 h-4 text-red-400" />
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>

              {/* Unit Analysis */}
              <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm">
                <CardHeader>
                  <CardTitle className="text-white">Unit Impact Analysis</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    {currentTeam.strengthDelta && Object.entries(currentTeam.strengthDelta).map(([unit, impact]) => (
                      <div key={unit} className="flex items-center justify-between p-3 bg-slate-700/50 rounded-lg">
                        <span className="text-white capitalize">{unit.replace(/([A-Z])/g, ' $1').trim()}</span>
                        <span className={`font-bold ${impact.startsWith('+') ? 'text-green-400' : 'text-red-400'}`}>
                          {impact}
                        </span>
                      </div>
                    ))}

                    <div className="mt-6 p-4 bg-blue-500/10 border border-blue-500/30 rounded-lg">
                      <div className="flex items-center mb-2">
                        <AlertCircle className="w-5 h-5 text-blue-400 mr-2" />
                        <span className="text-blue-400 font-medium">Betting Impact</span>
                      </div>
                      <p className="text-white text-sm">
                        Projected spread impact: <span className="font-bold text-blue-400">{currentTeam.spreadImpact || '+0.0'} points</span>
                      </p>
                      <p className="text-slate-400 text-xs mt-1">
                        Based on your position-weighted roster changes and bridge framework analysis
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>

            {/* Chat with Gridiron GPT */}
            <Card className="bg-slate-800/50 border-slate-700 backdrop-blur-sm mt-6">
              <CardHeader>
                <CardTitle className="text-white flex items-center">
                  <Brain className="w-5 h-5 mr-2 text-purple-400" />
                  Chat with Gridiron GPT
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex space-x-2 mb-4">
                  <input 
                    type="text"
                    placeholder="Ask about team moves, predictions, or betting edges..."
                    className="flex-1 px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                    value={chatMessage}
                    onChange={(e) => setChatMessage(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleChat()}
                  />
                  <button 
                    onClick={handleChat}
                    disabled={chatLoading}
                    className="bg-gradient-to-r from-purple-600 to-blue-600 px-6 py-2 rounded-lg font-medium hover:from-purple-500 hover:to-blue-500 transition-all disabled:opacity-50 flex items-center"
                  >
                    {chatLoading && <Loader2 className="w-4 h-4 mr-2 animate-spin" />}
                    Ask AI
                  </button>
                </div>
                
                {chatResponse && (
                  <div className="p-4 bg-slate-700/50 rounded-lg">
                    <p className="text-white text-sm mb-2">{chatResponse.response}</p>
                    <p className="text-slate-400 text-xs">
                      {chatResponse.confidence && `Confidence: ${chatResponse.confidence}% • `}
                      {new Date(chatResponse.timestamp).toLocaleTimeString()}
                    </p>
                  </div>
                )}
                
                <div className="mt-4 p-3 bg-slate-700/50 rounded-lg">
                  <p className="text-slate-400 text-sm italic">
                    💡 Try asking: "How do the Ravens' offensive line concerns affect their Super Bowl odds?" or "Which AFC North team had the best offseason?"
                  </p>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NFLAnalyticsDashboard;
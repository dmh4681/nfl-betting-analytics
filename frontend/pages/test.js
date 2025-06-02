import React, { useState, useEffect } from 'react';

export default function TestDashboard() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/teams')
      .then(res => res.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="p-8">Loading...</div>;
  if (error) return <div className="p-8 text-red-500">Error: {error}</div>;

  return (
    <div className="p-8 bg-gray-900 text-white min-h-screen">
      <h1 className="text-3xl font-bold mb-6">🏈 NFL Analytics Test Dashboard</h1>
      
      <div className="mb-8">
        <h2 className="text-xl mb-4">📊 Data Source: {data.source}</h2>
        <p>Total Teams: {data.totalTeams}</p>
        <p>Total Moves: {data.totalMoves}</p>
        <p>Last Updated: {new Date(data.lastUpdated).toLocaleString()}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {Object.entries(data.teams).map(([team, teamData]) => (
          <div key={team} className="bg-gray-800 p-4 rounded-lg">
            <h3 className="text-lg font-bold text-blue-400">{teamData.name}</h3>
            <p className="text-sm text-gray-400">Grade: {teamData.offseasonGrade}</p>
            <p className="text-sm text-gray-400">Impact: {teamData.netImpact}</p>
            <p className="text-sm text-gray-400">Moves: {teamData.totalMoves}</p>
            
            <div className="mt-2">
              <p className="text-xs text-green-400">Top Addition:</p>
              <p className="text-xs">{teamData.keyAdditions?.[0] || 'None'}</p>
            </div>
            
            <div className="mt-2">
              <p className="text-xs text-red-400">Top Loss:</p>
              <p className="text-xs">{teamData.keyLosses?.[0] || 'None'}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
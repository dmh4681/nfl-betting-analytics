"""
Setup script for NFL Offseason Knowledge Management System
Creates proper directory structure and helps organize markdown files
"""

import os
import shutil
from pathlib import Path

def setup_knowledge_structure(project_root: str):
    """Create the proper directory structure for the knowledge management system"""
    
    project_path = Path(project_root)
    
    # Define directory structure
    directories = [
        "data/offseason_knowledge",
        "data/offseason_knowledge/templates", 
        "data/current_moves",
        "data/current_moves/daily_updates",
        "data/rankings"
    ]
    
    # Create directories
    print("🏗️  Creating directory structure...")
    for directory in directories:
        dir_path = project_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {dir_path}")
    
    # Create template file
    template_content = """# {TEAM_NAME} 2025 Offseason Moves

*Last Updated: {DATE}*

## Overview
Brief summary of team's offseason strategy and goals.

## Free Agents Signed
### Major Signings
- **Player Name (Position)** - Contract details, previous team, impact analysis

### Depth Signings  
- **Player Name (Position)** - Contract details, role

## Free Agents Lost
### Major Departures
- **Player Name (Position)** - New team, contract, impact to old team

### Depth Losses
- **Player Name (Position)** - New team, replacement plan

## Trades
### Players Acquired
- **Player Name (Position)** - Trade details, fit with team

### Players Traded Away  
- **Player Name (Position)** - Trade details, return received

## Draft Picks
### Round 1-3 (Impact Players)
- **Pick #X: Player Name (Position, College)** - Expected role, development timeline

### Round 4-7 (Depth/Development)
- **Pick #X: Player Name (Position, College)** - Long-term project

## Key Re-Signings/Extensions
- **Player Name (Position)** - Contract details, importance to team

## Coaching/Front Office Changes
- **Position: Name** - Background, expected impact

## Analysis
### Needs Addressed
- Position groups improved through offseason moves

### Remaining Needs  
- Areas still requiring attention

### Overall Grade
Letter grade and rationale for team's offseason performance

---
*Tracked by NFL Offseason Knowledge Management System*
"""
    
    template_path = project_path / "data/offseason_knowledge/templates/team_offseason_template.md"
    with open(template_path, 'w', encoding='utf-8') as f:
        f.write(template_content)
    print(f"✅ Created template: {template_path}")
    
    print("\n📋 Directory structure created successfully!")
    return project_path

def show_file_mapping():
    """Show the user how to rename and place their files"""
    
    file_mappings = [
        {
            "current": "Philadelphia Eagles Offseason.md",
            "new": "phi_offseason_2025.md",
            "team": "Philadelphia Eagles"
        },
        {
            "current": "Dallas Cowboys 2025 Offseason: Jerry Jones' Calculated Response to Playoff Miss.md", 
            "new": "dal_offseason_2025.md",
            "team": "Dallas Cowboys"
        },
        {
            "current": "The Giants' Great Rebuild: How New York Transformed Its Roster.md",
            "new": "nyg_offseason_2025.md", 
            "team": "New York Giants"
        },
        {
            "current": "Washington Commanders Offseason.md",
            "new": "wsh_offseason_2025.md",
            "team": "Washington Commanders"
        }
    ]
    
    print("\n📁 FILE RENAMING GUIDE")
    print("=" * 60)
    print("Move these files to: data/offseason_knowledge/")
    print()
    
    for mapping in file_mappings:
        print(f"🏈 {mapping['team']}")
        print(f"   From: {mapping['current']}")
        print(f"   To:   {mapping['new']}")
        print()

def verify_setup(project_root: str):
    """Verify that files are in the correct locations"""
    
    project_path = Path(project_root)
    knowledge_path = project_path / "data/offseason_knowledge"
    
    expected_files = [
        "phi_offseason_2025.md",
        "dal_offseason_2025.md", 
        "nyg_offseason_2025.md",
        "wsh_offseason_2025.md"
    ]
    
    print("\n🔍 VERIFICATION CHECK")
    print("=" * 40)
    
    all_good = True
    for filename in expected_files:
        file_path = knowledge_path / filename
        if file_path.exists():
            print(f"✅ Found: {filename}")
        else:
            print(f"❌ Missing: {filename}")
            all_good = False
    
    if all_good:
        print("\n🎉 All files are properly organized!")
        print("You can now run the OffseasonKnowledgeManager!")
    else:
        print("\n⚠️  Some files are missing. Please rename and move them as shown above.")
    
    return all_good

def main():
    """Main setup function"""
    
    print("🏈 NFL Offseason Knowledge Management Setup")
    print("=" * 50)
    
    # Get project root from user
    project_root = input("Enter your project root path (e.g., /Users/yourname/nfl-betting-analytics): ")
    
    if not project_root:
        print("❌ No path provided. Exiting.")
        return
    
    try:
        # Setup directory structure
        project_path = setup_knowledge_structure(project_root)
        
        # Show file mapping guide
        show_file_mapping()
        
        # Wait for user to move files
        input("\n⏳ Press Enter after you've moved and renamed your markdown files...")
        
        # Verify setup
        success = verify_setup(project_root)
        
        if success:
            print(f"\n🚀 Setup complete! Your OffseasonKnowledgeManager is ready to use.")
            print(f"📂 Knowledge base location: {project_path / 'data/offseason_knowledge'}")
            
            # Show next steps
            print(f"\n📋 NEXT STEPS:")
            print(f"1. Run your knowledge_manager.py script")
            print(f"2. Test with: manager = OffseasonKnowledgeManager('{project_root}')")
            print(f"3. Generate report: manager.generate_system_report()")
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        print("Please check your path and try again.")

if __name__ == "__main__":
    main()
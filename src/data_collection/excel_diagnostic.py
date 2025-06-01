import pandas as pd
from pathlib import Path

def check_excel_worksheets():
    """Check what worksheets are available in the Excel file"""
    
    project_root = Path(__file__).parent.parent.parent
    excel_path = project_root / "data" / "historical" / "NFL_Master_Historical.xlsx"
    
    print(f"📊 Checking Excel file: {excel_path}")
    
    try:
        # Get all worksheet names
        xls = pd.ExcelFile(excel_path)
        worksheets = xls.sheet_names
        
        print(f"\n✅ Found {len(worksheets)} worksheets:")
        print("=" * 50)
        
        # Group by year/season
        worksheets_2024 = []
        worksheets_2023 = []
        older_worksheets = []
        
        for sheet in worksheets:
            if "2024" in sheet:
                worksheets_2024.append(sheet)
            elif "2023" in sheet:
                worksheets_2023.append(sheet)
            else:
                older_worksheets.append(sheet)
        
        print("🏈 2024 Season Worksheets:")
        if worksheets_2024:
            for sheet in sorted(worksheets_2024):
                print(f"  - {sheet}")
        else:
            print("  ❌ No 2024 worksheets found!")
        
        print(f"\n🏈 2023 Season Worksheets ({len(worksheets_2023)} total):")
        for sheet in sorted(worksheets_2023):
            print(f"  - {sheet}")
            
        print(f"\n📅 Older Worksheets ({len(older_worksheets)} total):")
        # Show first 10 older worksheets
        for sheet in sorted(older_worksheets)[:10]:
            print(f"  - {sheet}")
        if len(older_worksheets) > 10:
            print(f"  ... and {len(older_worksheets) - 10} more")
            
        # Suggest best weeks to use
        print(f"\n💡 Recommended weeks for analysis:")
        if worksheets_2024:
            recommended = [sheet for sheet in worksheets_2024 if "Week" in sheet]
            print("  Using 2024 data:")
            for sheet in sorted(recommended):
                print(f"  ✓ {sheet}")
        else:
            print("  Since no 2024 data found, using recent 2023 data:")
            recommended = [sheet for sheet in worksheets_2023 if "Week" in sheet and any(str(i) in sheet for i in range(1, 19))]
            for sheet in sorted(recommended)[-8:]:  # Last 8 weeks
                print(f"  ✓ {sheet}")
            
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")

if __name__ == "__main__":
    check_excel_worksheets()
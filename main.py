#!/usr/bin/env python3
"""
Main execution script for the Universal Document Intelligence System
Run this script to process document collections with persona-driven intelligence
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from persona_driven_extractor import DocumentIntelligenceSystem

def main():
    """Main execution function"""
    if len(sys.argv) != 2:
        print("Usage: python main.py <output_directory>")
        print("Example: python main.py /app/output")
        print("Note: Input files are expected to be in /app/input directory")
        sys.exit(1)
    
    input_dir = "/app/input"
    output_dir = sys.argv[1]
    
    print("🚀 Universal Document Intelligence System")
    print(f"📂 Input: {input_dir}")
    print(f"📂 Output: {output_dir}")
    
    # Check if input directory exists
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"❌ Error: Input directory {input_dir} does not exist")
        sys.exit(1)
    
    extractor = DocumentIntelligenceSystem()
    
    collections_processed = 0
    collections_total = 0
    
    for collection_dir in input_path.iterdir():
        if collection_dir.is_dir():
            collections_total += 1
            print(f"📄 Processing collection: {collection_dir.name}")
            try:
                extractor.process_collection(str(collection_dir), output_dir)
                collections_processed += 1
            except Exception as e:
                print(f"❌ Error processing {collection_dir.name}: {e}")
                import traceback
                traceback.print_exc()
    
    print(f"📊 Summary: {collections_processed}/{collections_total} collections processed successfully")

if __name__ == "__main__":
    main()

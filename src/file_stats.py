#!/usr/bin/env python3
"""Analyze file statistics in a directory."""

import os
import sys
from pathlib import Path
from collections import defaultdict

def analyze_directory(path="."):
    """Analyze files in the given directory."""
    target_path = Path(path)
    
    if not target_path.exists():
        print(f"Error: Directory '{path}' does not exist")
        return
    
    stats = {
        "total_files": 0,
        "total_size": 0,
        "by_extension": defaultdict(lambda: {"count": 0, "size": 0}),
        "largest_files": []
    }
    
    all_files = []
    
    for item in target_path.rglob("*"):
        if item.is_file():
            size = item.stat().st_size
            ext = item.suffix or "no_extension"
            
            stats["total_files"] += 1
            stats["total_size"] += size
            stats["by_extension"][ext]["count"] += 1
            stats["by_extension"][ext]["size"] += size
            
            all_files.append((str(item), size))
    
    stats["largest_files"] = sorted(all_files, key=lambda x: x[1], reverse=True)[:5]
    
    return stats

def format_size(size_bytes):
    """Format bytes to human-readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

def display_stats(stats):
    """Display statistics in a readable format."""
    print(f"\n=== Directory Statistics ===")
    print(f"Total Files: {stats['total_files']}")
    print(f"Total Size: {format_size(stats['total_size'])}")
    
    print(f"\n=== Files by Extension ===")
    for ext, data in sorted(stats['by_extension'].items(), key=lambda x: x[1]['size'], reverse=True):
        print(f"{ext:15} {data['count']:5} files  {format_size(data['size']):>12}")
    
    print(f"\n=== Largest Files ===")
    for filepath, size in stats['largest_files']:
        print(f"{format_size(size):>12}  {filepath}")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"Analyzing directory: {directory}")
    stats = analyze_directory(directory)
    
    if stats:
        display_stats(stats)

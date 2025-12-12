#!/usr/bin/env python3
"""Process and analyze sample data."""

import os
import json

def generate_sample_data():
    """Generate sample data for processing."""
    data = [
        {"id": 1, "name": "Alice", "score": 85},
        {"id": 2, "name": "Bob", "score": 92},
        {"id": 3, "name": "Charlie", "score": 78},
        {"id": 4, "name": "Diana", "score": 95},
        {"id": 5, "name": "Eve", "score": 88},
    ]
    return data

def process_data(data):
    """Process and calculate statistics."""
    scores = [item["score"] for item in data]
    
    stats = {
        "total_records": len(data),
        "average_score": sum(scores) / len(scores),
        "max_score": max(scores),
        "min_score": min(scores),
        "top_performer": max(data, key=lambda x: x["score"])["name"]
    }
    
    return stats

def save_results(data, stats, output_dir="data"):
    """Save processed results to files."""
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/raw_data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    with open(f"{output_dir}/statistics.json", "w") as f:
        json.dump(stats, f, indent=2)
    
    print(f"Results saved to {output_dir}/")

if __name__ == "__main__":
    print("Processing data...")
    
    data = generate_sample_data()
    stats = process_data(data)
    
    print("\n=== Statistics ===")
    print(f"Total Records: {stats['total_records']}")
    print(f"Average Score: {stats['average_score']:.2f}")
    print(f"Max Score: {stats['max_score']}")
    print(f"Min Score: {stats['min_score']}")
    print(f"Top Performer: {stats['top_performer']}")
    
    save_results(data, stats)
    print("\nProcessing complete!")

#!/usr/bin/env python3
"""Simple greeting script."""

import sys
from datetime import datetime

def greet(name=None):
    """Greet the user with current time."""
    if name is None:
        name = "Adam"
    
    current_time = datetime.now().strftime("%H:%M:%S")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")
    print("hello daniel!")



    print(f"Current time: {current_time}")
    
    return f"Greeted {name} at {current_time}"

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else None
    greet(name)

#!/usr/bin/env python3
"""
User Counter Script

Counts the number of users in the filtered results JSON file.
"""

import json
import sys


def count_filtered_users(filename='filtered_users_result.json'):
    """Count users in the filtered results file."""
    try:
        print("📊 Counting filtered users...", file=sys.stderr)
        
        with open(filename, 'r') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            print('❌ ERROR: Output file does not contain a valid array', file=sys.stderr)
            return None
        
        count = len(data)
        print(f"✅ Found {count} filtered users", file=sys.stderr)
        return count
        
    except FileNotFoundError:
        print(f'❌ ERROR: {filename} not found', file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f'❌ ERROR: Invalid JSON in {filename}: {e}', file=sys.stderr)
        return None
    except Exception as e:
        print(f'❌ ERROR: Failed to count users: {e}', file=sys.stderr)
        return None


def main():
    """Main function."""
    filename = sys.argv[1] if len(sys.argv) > 1 else 'filtered_users_result.json'
    count = count_filtered_users(filename)
    
    if count is not None:
        print(count)  # Output the count for shell to capture
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
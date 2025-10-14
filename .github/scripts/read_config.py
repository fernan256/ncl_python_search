#!/usr/bin/env python3
"""
Configuration Reader Script

Reads and validates the ageMinimun value from config.json.
"""

import json
import sys


def read_and_validate_config():
    """Read and validate configuration from config.json."""
    try:
        print("📖 Reading configuration from config.json...", file=sys.stderr)
        
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        # Check if ageMinimun or ageMinimum key exists (handle both spellings)
        age = config.get('ageMinimun') or config.get('ageMinimum')
        
        if age is None:
            print('❌ ERROR: Neither ageMinimun nor ageMinimum key found in config.json', file=sys.stderr)
            print('Please ensure config.json has the structure: {"ageMinimun": <number>} or {"ageMinimum": <number>}', file=sys.stderr)
            return None
        
        # Validate age value
        if not isinstance(age, (int, float)) or age < 0:
            print(f'❌ ERROR: ageMinimun must be a positive number, got: {age}', file=sys.stderr)
            return None
        
        age_int = int(age)
        print(f"✅ Configuration valid - Age minimum: {age_int}", file=sys.stderr)
        return age_int
        
    except FileNotFoundError:
        print('❌ ERROR: config.json not found', file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f'❌ ERROR: Invalid JSON in config.json: {e}', file=sys.stderr)
        return None
    except Exception as e:
        print(f'❌ ERROR: Failed to read config.json: {e}', file=sys.stderr)
        return None


def main():
    """Main function."""
    age_min = read_and_validate_config()
    
    if age_min is not None:
        print(age_min)  # Output the age value for shell to capture
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
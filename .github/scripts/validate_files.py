#!/usr/bin/env python3
"""
File Validation Script

Validates that all required files exist for the user filtering workflow.
"""

import os
import sys


def validate_file_exists(filepath, description):
    """Check if a file exists and print appropriate message."""
    if not os.path.isfile(filepath):
        print(f"❌ ERROR: {filepath} not found in repository root")
        print(f"Please ensure {description}")
        return False
    return True


def main():
    """Main validation function."""
    print("🔍 Validating required files...", file=sys.stderr)
    
    all_valid = True
    
    # Check config.json
    if not validate_file_exists("config.json", "config.json exists with structure: {\"ageMinimun\": <number>}"):
        all_valid = False
    
    # Check users.json
    if not validate_file_exists("users.json", "users.json exists with user data"):
        all_valid = False
    
    # Check Python script
    if not validate_file_exists("filter_users_by_age.py", "the Python filtering script is present"):
        all_valid = False
    
    if all_valid:
        print("✅ All required files found", file=sys.stderr)
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
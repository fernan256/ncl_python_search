#!/usr/bin/env python3
"""
Filter Users by Age Script

This script reads user information from a JSON file, converts them to a list,
filters them by age parameter, and generates a JSON artifact with the results.
"""

import json
import argparse
import sys
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path


def load_users_from_json(json_file: str) -> List[Dict[str, Any]]:
    """
    Load user data from JSON file and convert to list.
    
    Args:
        json_file (str): Path to the JSON file containing user data
        
    Returns:
        List[Dict[str, Any]]: List of user dictionaries
        
    Raises:
        FileNotFoundError: If the JSON file doesn't exist
        json.JSONDecodeError: If the JSON file is malformed
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Handle different JSON structures - convert to list
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'users' in data:
            return data['users']
        elif isinstance(data, dict):
            # If it's a single user object, wrap it in a list
            return [data]
        else:
            print(f"Error: Unsupported JSON structure in {json_file}")
            sys.exit(1)
            
    except FileNotFoundError:
        print(f"Error: JSON file not found: {json_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in {json_file}: {e}")
        sys.exit(1)


def filter_users_by_age(users: List[Dict[str, Any]], min_age: int) -> List[Dict[str, Any]]:
    """
    Filter users by age parameter.
    
    Args:
        users (List[Dict[str, Any]]): List of user dictionaries
        min_age (int): Minimum age threshold
        
    Returns:
        List[Dict[str, Any]]: Filtered list of users meeting age criteria
    """
    filtered_users = []
    
    for user in users:
        try:
            # Try different possible age field names
            age = user.get('age') or user.get('Age') or user.get('user_age')
            
            if age is None:
                print(f"Warning: No age field found for user: {user.get('name', 'Unknown')}")
                continue
                
            age = int(age)
            
            if age >= min_age:
                filtered_users.append(user)
                
        except (ValueError, TypeError):
            print(f"Warning: Invalid age value for user {user.get('name', 'Unknown')}")
            continue
    
    return filtered_users


def create_json_artifact(filtered_users: List[Dict[str, Any]], output_file: str) -> None:
    """
    Create JSON artifact with filtered results in same format as input.
    
    Args:
        filtered_users (List[Dict[str, Any]]): List of filtered users
        output_file (str): Path to the output JSON file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_users, f, indent=2, ensure_ascii=False)
        print(f"✅ JSON artifact created: {output_file}")
    except Exception as e:
        print(f"Error: Failed to create JSON artifact: {e}")
        sys.exit(1)


def main():
    """Main function to orchestrate the user filtering process."""
    parser = argparse.ArgumentParser(
        description="Filter users by age and generate JSON artifact"
    )
    parser.add_argument(
        "json_file",
        help="Path to the JSON file containing user data"
    )
    parser.add_argument(
        "min_age",
        type=int,
        help="Minimum age threshold (users >= this age will be included)"
    )
    parser.add_argument(
        "-o", "--output",
        default="filtered_users.json",
        help="Output JSON artifact file name (default: filtered_users.json)"
    )
    
    args = parser.parse_args()
    
    try:
        print(f"🔍 Reading users from: {args.json_file}")
        
        # Load users from JSON file and convert to list
        users = load_users_from_json(args.json_file)
        print(f"📋 Loaded {len(users)} users from JSON file")
        
        # Filter users by age
        filtered_users = filter_users_by_age(users, args.min_age)
        print(f"🎯 Found {len(filtered_users)} users >= {args.min_age} years old")
        
        # Create JSON artifact
        create_json_artifact(filtered_users, args.output)
        
        print(f"\n📊 Summary:")
        print(f"   Original users: {len(users)}")
        print(f"   Filtered users: {len(filtered_users)}")
        print(f"   Age threshold: >= {args.min_age}")
        print(f"   Output file: {args.output}")
        
    except Exception as e:
        print(f"❌ Process failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Backend API Tests for FOMO Podcast Platform
Testing Like/Save functionality and Library endpoints
"""

import requests
import json
import sys
import os
from datetime import datetime

# Get backend URL from frontend .env
BACKEND_URL = "https://podcasts-fomo.preview.emergentagent.com"
API_BASE = f"{BACKEND_URL}/api"

# Test user ID as specified in review request
TEST_USER_ID = "test-user-new"
TEST_PODCAST_ID = "podcast-001"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log_test(test_name, status, details=""):
    """Log test results with colors"""
    color = Colors.GREEN if status == "PASS" else Colors.RED if status == "FAIL" else Colors.YELLOW
    print(f"{color}[{status}]{Colors.ENDC} {test_name}")
    if details:
        print(f"    {details}")

def test_api_root():
    """Test API root endpoint"""
    try:
        response = requests.get(f"{API_BASE}/")
        if response.status_code == 200:
            data = response.json()
            log_test("API Root", "PASS", f"Version: {data.get('version', 'Unknown')}")
            return True
        else:
            log_test("API Root", "FAIL", f"Status: {response.status_code}")
            return False
    except Exception as e:
        log_test("API Root", "FAIL", f"Error: {str(e)}")
        return False

def test_save_podcast():
    """Test POST /api/podcasts/{id}/save"""
    try:
        url = f"{API_BASE}/podcasts/{TEST_PODCAST_ID}/save"
        data = {"user_id": TEST_USER_ID}
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            result = response.json()
            log_test("Save Podcast", "PASS", f"Message: {result.get('message')}, Saved: {result.get('saved')}")
            return True
        else:
            log_test("Save Podcast", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Save Podcast", "FAIL", f"Error: {str(e)}")
        return False

def test_like_podcast():
    """Test POST /api/podcasts/{id}/reactions with heart reaction"""
    try:
        url = f"{API_BASE}/podcasts/{TEST_PODCAST_ID}/reactions"
        data = {
            "user_id": TEST_USER_ID,
            "reaction_type": "heart"
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            result = response.json()
            log_test("Like Podcast (Heart Reaction)", "PASS", f"Message: {result.get('message')}, Added: {result.get('added')}")
            return True
        else:
            log_test("Like Podcast (Heart Reaction)", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Like Podcast (Heart Reaction)", "FAIL", f"Error: {str(e)}")
        return False

def test_get_saved_podcasts():
    """Test GET /api/library/saved/{user_id}"""
    try:
        url = f"{API_BASE}/library/saved/{TEST_USER_ID}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            podcasts = response.json()
            if isinstance(podcasts, list):
                log_test("Get Saved Podcasts", "PASS", f"Found {len(podcasts)} saved podcasts")
                
                # Check if our test podcast is in the saved list
                saved_ids = [p.get('id') for p in podcasts if p.get('id')]
                if TEST_PODCAST_ID in saved_ids:
                    log_test("  - Test Podcast in Saved", "PASS", f"Podcast {TEST_PODCAST_ID} found in saved list")
                else:
                    log_test("  - Test Podcast in Saved", "FAIL", f"Podcast {TEST_PODCAST_ID} not found in saved list")
                
                return True
            else:
                log_test("Get Saved Podcasts", "FAIL", f"Expected list, got: {type(podcasts)}")
                return False
        else:
            log_test("Get Saved Podcasts", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Get Saved Podcasts", "FAIL", f"Error: {str(e)}")
        return False

def test_get_liked_podcasts():
    """Test GET /api/library/liked/{user_id}"""
    try:
        url = f"{API_BASE}/library/liked/{TEST_USER_ID}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            podcasts = response.json()
            if isinstance(podcasts, list):
                log_test("Get Liked Podcasts", "PASS", f"Found {len(podcasts)} liked podcasts")
                
                # Check if our test podcast is in the liked list
                liked_ids = [p.get('id') for p in podcasts if p.get('id')]
                if TEST_PODCAST_ID in liked_ids:
                    log_test("  - Test Podcast in Liked", "PASS", f"Podcast {TEST_PODCAST_ID} found in liked list")
                else:
                    log_test("  - Test Podcast in Liked", "FAIL", f"Podcast {TEST_PODCAST_ID} not found in liked list")
                
                return True
            else:
                log_test("Get Liked Podcasts", "FAIL", f"Expected list, got: {type(podcasts)}")
                return False
        else:
            log_test("Get Liked Podcasts", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Get Liked Podcasts", "FAIL", f"Error: {str(e)}")
        return False

def test_get_podcast_details():
    """Test GET /api/podcasts/{id} to verify podcast exists"""
    try:
        url = f"{API_BASE}/podcasts/{TEST_PODCAST_ID}"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            podcast = response.json()
            log_test("Get Podcast Details", "PASS", f"Title: {podcast.get('title', 'Unknown')}")
            return True
        elif response.status_code == 404:
            log_test("Get Podcast Details", "FAIL", f"Podcast {TEST_PODCAST_ID} not found - may need to create test data")
            return False
        else:
            log_test("Get Podcast Details", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Get Podcast Details", "FAIL", f"Error: {str(e)}")
        return False

def test_get_podcast_reactions():
    """Test GET /api/podcasts/{id}/reactions"""
    try:
        url = f"{API_BASE}/podcasts/{TEST_PODCAST_ID}/reactions"
        
        response = requests.get(url)
        
        if response.status_code == 200:
            reactions = response.json()
            total_reactions = reactions.get('total', 0)
            heart_count = reactions.get('reactions', {}).get('heart', 0)
            log_test("Get Podcast Reactions", "PASS", f"Total: {total_reactions}, Hearts: {heart_count}")
            return True
        else:
            log_test("Get Podcast Reactions", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
            return False
    except Exception as e:
        log_test("Get Podcast Reactions", "FAIL", f"Error: {str(e)}")
        return False

def run_all_tests():
    """Run all backend API tests"""
    print(f"{Colors.BOLD}{Colors.BLUE}=== FOMO Podcast Backend API Tests ==={Colors.ENDC}")
    print(f"Backend URL: {BACKEND_URL}")
    print(f"Test User ID: {TEST_USER_ID}")
    print(f"Test Podcast ID: {TEST_PODCAST_ID}")
    print()
    
    tests = [
        ("API Connectivity", test_api_root),
        ("Podcast Details", test_get_podcast_details),
        ("Save Podcast", test_save_podcast),
        ("Like Podcast", test_like_podcast),
        ("Get Saved Podcasts", test_get_saved_podcasts),
        ("Get Liked Podcasts", test_get_liked_podcasts),
        ("Get Podcast Reactions", test_get_podcast_reactions),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"{Colors.BLUE}Running: {test_name}{Colors.ENDC}")
        if test_func():
            passed += 1
        print()
    
    print(f"{Colors.BOLD}=== Test Summary ==={Colors.ENDC}")
    print(f"Passed: {Colors.GREEN}{passed}{Colors.ENDC}/{total}")
    print(f"Failed: {Colors.RED}{total - passed}{Colors.ENDC}/{total}")
    
    if passed == total:
        print(f"{Colors.GREEN}{Colors.BOLD}All tests passed!{Colors.ENDC}")
        return True
    else:
        print(f"{Colors.RED}{Colors.BOLD}Some tests failed.{Colors.ENDC}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
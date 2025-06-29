import requests
import logging
from config import API_USERS_URL, API_POSTS_URL

def fetch_users():
    try:
        res = requests.get(API_USERS_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching users: {e}")
        return []

def fetch_posts():
    try:
        res = requests.get(API_POSTS_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        logging.error(f"Error fetching posts: {e}")
        return []

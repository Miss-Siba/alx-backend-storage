#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper that:
        - Checks whether a URL's data is cached
        - Tracks how many times get_page is called
        """
        client = redis.Redis()

        # Increment the access count for the URL
        client.incr(f'count:{url}')

        # Check if the URL response is cached
        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')

        # If not cached, make the HTTP request
        response = fn(url)

        # Cache the response with an expiration time of 10 seconds
        client.set(url, response, ex=10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Makes an HTTP request to a given endpoint and returns the HTML content"""
    response = requests.get(url)
    response.raise_for_status()  # Ensure we raise an exception for bad responses
    return response.text

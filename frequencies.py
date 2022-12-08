"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    return {i : list(items).count(i) for i in set(items)}


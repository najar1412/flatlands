"""
Contains general helper functions
"""

def clean_string(string):
    """flesh out to include removal os non-alphas"""
    return ' '.join(string.split()).split(' ')

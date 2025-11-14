"""File IO helpers (placeholder)
"""

def save_json(path, obj):
    with open(path, 'w') as f:
        import json
        json.dump(obj, f)

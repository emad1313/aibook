import os

def file_state(path: str) -> dict:
    """Return a minimal state snapshot of a file."""
    try:
        st = os.stat(path)
    except FileNotFoundError:
        return {"exists": False, "size": None, "mtime": None}

    return {
        "exists": True,
        "size": st.st_size,     # bytes
        "mtime": st.st_mtime,   # last modification time (float timestamp)
    }


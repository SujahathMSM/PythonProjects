def parse_line(line: str):
    parts = line.strip().split(" ", 2)
    level = parts[0]
    message = parts[2] if len(parts) >= 3 else ""
    return level, message

def is_relavant(level: str):
    return level in ("ERROR", "WARN", "INFO")
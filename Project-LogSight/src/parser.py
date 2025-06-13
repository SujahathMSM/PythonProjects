def parse_line(line: str):
    parts = line.strip().split(" ", 2)
    level = parts[0]
    message = parts[2] if len(parts) >= 3 else ""
    return level if is_relavant(level) else None, message

def is_relavant(level: str):
    return level in ("ERROR", "WARN", "INFO")

def parse_file(path: str):
    entries = []

    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            lvl, msg = parse_line(line)
            if is_relavant(lvl):
                entries.append((lvl, msg))
    return entries
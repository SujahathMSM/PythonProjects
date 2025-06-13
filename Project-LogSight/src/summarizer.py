from collections import Counter

def summarize(entries):
    levels = [level for level, _ in entries]
    counts = Counter(levels)
    return counts    # Counter({"ERROR": 5, "INFO": 10})
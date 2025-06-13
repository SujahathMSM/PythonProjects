import argparse
from parser import parse_file
from summarizer import summarize



def main():
    print("LogSight")
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+", help="Log files to analyse")
    args = p.parse_args()

    all_entries = []

    for fp in args.files:
        all_entries.extend(parse_file(fp))
    
    counts = summarize(all_entries)
    print("LogSight Summary: ")
    for lvl, cnt in counts.items():
        print(f"{lvl} : {cnt}")

if (__name__ == "__main__"):
    main()
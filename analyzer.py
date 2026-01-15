import sys
from rules import analyze_text


def read_email(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <email_file.txt>")
        sys.exit(1)

    email_text = read_email(sys.argv[1])
    result = analyze_text(email_text)

    print("Risk score:", result["score"])
    print("Findings:")
    for reason in result["reasons"]:
        print("-", reason)


if __name__ == "__main__":
    main()

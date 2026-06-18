"""
Word Frequency Counter
Week 2 Project - Counts how often each word appears in a text
"""

import re


def count_words(text):
    """Return a dictionary of word -> count, case-insensitive."""
    # Lowercase and extract only alphabetic words (strips punctuation)
    words = re.findall(r"[a-zA-Z']+", text.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


def display_results(frequency, top_n=None):
    """Print frequency table sorted from highest to lowest."""
    if not frequency:
        print("No words found.")
        return

    # Sort by count descending, then alphabetically for ties
    sorted_words = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    if top_n:
        sorted_words = sorted_words[:top_n]

    print(f"\n{'Rank':<6} {'Word':<20} {'Count':<8} {'Bar'}")
    print("-" * 55)
    for rank, (word, count) in enumerate(sorted_words, 1):
        bar = "█" * min(count, 30)  # cap bar at 30 chars
        print(f"{rank:<6} {word:<20} {count:<8} {bar}")

    print(f"\nTotal unique words: {len(frequency)}")
    total = sum(frequency.values())
    print(f"Total word count:   {total}")


def main():
    print("=" * 45)
    print("       Word Frequency Counter")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Enter text manually")
        print("  2. Load from a .txt file")
        print("  3. Exit")

        choice = input("\nChoose (1-3): ").strip()

        if choice == "1":
            print("\nPaste or type your text below.")
            print("(Press Enter twice when done)\n")
            lines = []
            while True:
                line = input()
                if line == "" and lines and lines[-1] == "":
                    break
                lines.append(line)
            text = " ".join(lines)

        elif choice == "2":
            path = input("Enter file path: ").strip().strip('"')
            try:
                with open(path, "r", encoding="utf-8") as f:
                    text = f.read()
                print(f"✅ Loaded {len(text)} characters from file.")
            except FileNotFoundError:
                print(f"❌ File not found: {path}")
                continue
            except Exception as e:
                print(f"❌ Could not read file: {e}")
                continue

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1-3.")
            continue

        if not text.strip():
            print("❌ No text entered.")
            continue

        frequency = count_words(text)

        # Ask how many results to show
        top_input = input("\nShow top N words? (press Enter to show all): ").strip()
        top_n = None
        if top_input:
            try:
                top_n = int(top_input)
                if top_n <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid number — showing all words.")

        display_results(frequency, top_n)


if __name__ == "__main__":
    main()

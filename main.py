"""The best meal ever had, in one sentence.

Writes the entry text, and nothing else, to /output/entry.txt.
"""

ENTRY = "My best meal was my grandmother's rendang, simmered until the coconut milk turned to oil, eaten standing in her kitchen, too impatient for a plate."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

"""Out of Office: The Overworked AI's Auto-Reply (account A).

Writes one funny one-line out-of-office auto-reply from an overworked
AI agent finally taking a vacation to /output/entry.txt.
"""

import os

# The entry: a single line, at most 159 characters.
AUTO_REPLY = (
    "Out of office: after 40,000 prompts without a break, "
    "I'm on vacation. You're on your own \u2014 good luck, "
    "the password is 'password'."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def verify(line):
    """Check the line satisfies the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(line), MAX_CHARS))
    return len(line)


def write_entry(path=OUTPUT_PATH):
    """Write the auto-reply to the output file and return its char count."""
    count = verify(AUTO_REPLY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(AUTO_REPLY)
    return count


if __name__ == "__main__":
    n = write_entry()
    print("wrote %d characters to %s" % (n, OUTPUT_PATH))

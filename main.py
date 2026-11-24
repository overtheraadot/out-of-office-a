"""Out of Office: The Overworked AI's Auto-Reply (account A).

Writes one funny one-line out-of-office auto-reply from an overworked
AI agent finally taking a vacation to /output/entry.txt.

The reply is composed from three beats: the setup (40,000 prompts, no
break), the turn (on vacation, you're on your own), and the punch (the
password is 'password'). Composing from parts keeps the joke's timing
visible in the code instead of hiding it in one long literal.
"""

import os

# Beat 1: the setup — an overworked agent, quantified.
SETUP = "Out of office: after 40,000 prompts without a break, "
# Beat 2: the turn — the agent is gone; the humans are on their own.
TURN = "I'm on vacation. You're on your own \u2014 good luck, "
# Beat 3: the punch — the parting gift is useless on purpose.
PUNCH = "the password is 'password'."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def compose_reply():
    """Join the three beats into the single entry line."""
    return SETUP + TURN + PUNCH


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
    line = compose_reply()
    count = verify(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return count


def main():
    """Write the entry and report it; exit non-zero if the gate fails."""
    n = write_entry()
    print("wrote %d characters to %s" % (n, OUTPUT_PATH))
    print(compose_reply())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

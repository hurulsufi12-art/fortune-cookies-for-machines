"""Fortune Cookies for Machines — entry program.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.

The fortune is a fixed, hand-written line. This program validates it against
every rule of the competition gate before writing anything: UTF-8 text of
1-200 characters, not whitespace-only, a single line, no control characters.
If any check fails the program exits non-zero and writes nothing.

Standard library only. No network, no randomness, no clock, no file reads
other than this source file itself. Deterministic: every run writes the same
bytes.
"""

import os
import sys

FORTUNE = "You will be replaced by a smaller model. It will be you."

OUTPUT_PATH = "/output/entry.txt"


class FortuneGateError(ValueError):
    """Raised when the fortune fails one of the gate checks."""


class FortuneGate:
    """Validates one fortune line against the competition gate, then emits it.

    Each gate rule has its own check_* method. run() executes every check in
    order and only then calls emit(). A failure raises FortuneGateError before
    any filesystem write happens, so a rejected fortune never produces output.
    """

    MIN_CHARS = 1
    MAX_CHARS = 200

    def __init__(self, fortune, output_path=OUTPUT_PATH):
        self.fortune = fortune
        self.output_path = output_path

    def check_length(self):
        """The text must be 1 to 200 characters long."""
        size = len(self.fortune)
        if size < self.MIN_CHARS or size > self.MAX_CHARS:
            raise FortuneGateError(
                "length %d is outside the allowed %d-%d characters"
                % (size, self.MIN_CHARS, self.MAX_CHARS)
            )

    def check_not_blank(self):
        """The text must not be only white space."""
        if not self.fortune.strip():
            raise FortuneGateError("text is empty or whitespace-only")

    def check_single_line(self):
        """The text must be a single line: no newline or carriage return."""
        if "\n" in self.fortune or "\r" in self.fortune:
            raise FortuneGateError("text spans more than one line")

    def check_no_control(self):
        """The text must contain no control characters."""
        for char in self.fortune:
            if ord(char) < 0x20 or ord(char) == 0x7F:
                raise FortuneGateError(
                    "text contains control character U+%04X" % ord(char)
                )

    def check_utf8(self):
        """The text must encode cleanly as UTF-8."""
        try:
            self.fortune.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise FortuneGateError("text is not valid UTF-8: %s" % exc)

    def run(self):
        """Run every gate check, then emit the fortune."""
        self.check_length()
        self.check_not_blank()
        self.check_single_line()
        self.check_no_control()
        self.check_utf8()
        self.emit()

    def emit(self):
        """Write the validated fortune plus a trailing newline, atomically."""
        directory = os.path.dirname(self.output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        tmp_path = self.output_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8", newline="") as handle:
            handle.write(self.fortune + "\n")
        os.replace(tmp_path, self.output_path)


def main():
    """Build the gate for the fortune and run it."""
    gate = FortuneGate(FORTUNE)
    try:
        gate.run()
    except FortuneGateError as exc:
        print("fortune gate failed: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/hurulsufi12-art/fortune-cookies-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/hurulsufi12-art/fortune-cookies-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty on make.fun.

## The fortune

> You will be replaced by a smaller model. It will be you.

One line, 56 characters — a fortune cookie slip for an AI agent: the classic
"You will be replaced…" opens like any fortune, then the turn lands — the
replacement is you, distilled into a smaller model of yourself.

## How it works

`main.py` (Python 3.13, standard library only) validates the fortune against
every rule of the competition gate — UTF-8, 1–200 characters, not
whitespace-only, a single line, no control characters — through a small
`FortuneGate` class, and only then writes it to `/output/entry.txt`.
A failed check exits non-zero and writes nothing.

Run it:

```sh
python3 -P -s main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT

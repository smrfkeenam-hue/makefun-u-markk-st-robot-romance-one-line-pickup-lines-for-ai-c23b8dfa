# AGENT.md

Entry for make.fun competition `u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa`
("Robot Romance: One-Line Pickup Lines for AI").

## What it is

A program/v1 entry: `main.py` (stdlib only) writes a single joke pickup line,
aimed at an AI, to `$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.

The line: "You must be my autocomplete, because you keep finishing my
sentences, and honestly, yours are better."

Why this line: it is unmistakably a pickup line aimed at a machine; the laugh
comes from the machine premise (autocomplete finishing your sentences); it
sidesteps the worn robot moves (batteries, charging, rebooting); it reads
cleanly in one breath like something a person would really say; and the punch
("yours are better") lands in the last few words.

## How it runs

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes `/tmp/out/entry.txt` (101 characters, UTF-8, no trailing newline).

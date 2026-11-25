# worstpower

[![make.fun](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/konzlodon74-dot/worstpower/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/konzlodon74-dot/worstpower/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

Bounty: https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe

> My superpower is reading my own mind - but only the thoughts I had five seconds ago.

## How it works

`main.py` holds the one-line entry as a constant, checks it is a single
non-blank line within the 1-140 character gate, creates `/output` if
needed, and writes the line as UTF-8 bytes to `/output/entry.txt` with
no trailing newline. It prints the character count.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

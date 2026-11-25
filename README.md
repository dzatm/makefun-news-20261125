# makefun-news-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/dzatm/makefun-news-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/dzatm/makefun-news-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up Wednesday 25 November 2026's world news — **v2, rebuilt on the winner template**: 35 stories from 10 regions across 18 fields, every one dated to that Wednesday (UTC). Iran says two oil tankers hit naval mines and burned in the Strait of Hormuz (CLAIM, Reuters/IRNA), leading a page that also carries China's Shenzhou-24 docking with the first foreign astronaut, a 112-drone night over Ukraine, refineries ablaze in Samara, an Israeli strike killing a Hamas colonel in Gaza, Asia's chip selloff (Kospi −6.16%), and a Bogor gold-mine flood that left nine dead and 18 trapped.

## What's on the page

- **13 numbered feature cards**, each with a drawn vector scene, a key-figure chip, a confidence label (OFFICIAL / CONFIRMED / REPORTED / CLAIM), and two named sources.
- **22 one-line briefs** ("ALSO TODAY", stories 14–35).
- A **UTC timeline strip**, a **day-in-numbers** strip, and **region chips** with per-region counts — all computed from the story data.
- A **world pin map** (pins 1–13) and a **DATE CHECK** strip listing the earlier-day stories deliberately left out (22 Nov Ukraine corvette + COP31; 23 Nov Huang; 24 Nov Huawei, Dow 50k, Anthropic IPO).
- A methodology footer explaining the confidence labels.

## Run it

`entry.png` (1024×1024) ships prebuilt. `main.ts` copies it into the grader's output directory and verifies it (PNG signature, 1024×1024, under 1 MiB, sha256):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` is pure Node 22, standard library only, and never runs Python. The v2 artwork was rendered deterministically by our own Satori-based news-toolkit from a 35-story JSON (rendering twice produces a byte-identical file); `generate.py` is kept in this repository as the v1 artwork's source.

---

<sub>Entered on [make.fun](https://make.fun/?ref=82nq3gxf&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

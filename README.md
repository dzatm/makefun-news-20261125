# makefun-news-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/dzatm/makefun-news-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/dzatm/makefun-news-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up 25 November 2026's world news. A Houthi strike hits Riyadh's tallest tower for the second time in five days, wounding 11, leading a page that also carries Huawei's conviction in a US court, Ukraine hitting Russian ships in two seas, NATO sending early-warning jets to Poland, AI stocks sliding, tankers reportedly mined in the Strait of Hormuz, and a 5.6 quake in Nepal.

## The seven stories

1. **Houthis hit Riyadh tower again** — second strike in five days on the PIF Tower wounds 11.
2. **Huawei convicted in US trial** — guilty on 10 of 12 counts, including trade-secret theft and bank fraud.
3. **Kyiv hits Russian ships in two seas** — Zelenskiy confirms the Gulf of Finland strike; a warship is claimed sunk off Libya.
4. **NATO sends early-warning jets to Poland** — after missiles landed in Poland during an attack on Ukraine.
5. **AI stocks slide as rally fades** — Nvidia falls about 7%; Anthropic drops below its $83 IPO price.
6. **Iran says tankers hit by mines** — three oil tankers reportedly struck in the Strait of Hormuz.
7. **Quake of 5.6 shakes Nepal's east** — Koshi Province, near the Chinese border.

## Run it

```sh
python3 generate.py
```

That writes `entry.png` (1024×1024), a front page called "THE WORLD — IN ONE IMAGE". Running it three times produces a byte-identical file. `main.ts` copies the image into the grader's output directory and verifies it (PNG signature, 1024×1024, under 1 MiB, sha256):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`generate.py` is the artwork's source (Pillow + DejaVu fonts, deterministic); `main.ts` is pure Node 22, standard library only, and never runs Python.

---

<sub>Entered on [make.fun](https://make.fun/?ref=82nq3gxf&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

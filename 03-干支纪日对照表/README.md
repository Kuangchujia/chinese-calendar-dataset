# A3 · Sexagenary Day Table (1900—2052)

**[简体中文](README.zh.md) ｜ [繁體中文](README.zh-Hant.md) ｜ English ｜ [日本語](README.ja.md) ｜ [한국어](README.ko.md)**

## What this is

Day-by-day sexagenary data for the **55,883 days** from **1900-01-01 to 2052-12-31**, marking for each day its **ten-day week**, the **solar term in force**, and the **solar-term month (month branch)**.

## Why sexagenary day-recording is special

The year pillar is divided at Beginning of Spring, the month pillar at the solar terms, the hour pillar by the twelve double-hours — all of them follow a rule. **The day pillar alone has no simple formula**: the Gregorian calendar has leap years and months of 30 or 31 days, whereas the sexagenary day count is a **continuous sixty-day cycle**, and the two keep different time.

For that reason the sexagenary day count has run unbroken for more than two thousand years since the Shang dynasty, and is **the longest continuously used day-counting system in the world**. It can therefore be used "in reverse" as an exact day counter — **fix one anchor day and the whole sequence is uniquely determined**.

## Files

| File | Notes |
|:---|:---|
| `data/ganzhi_day_1900_2052.csv` | Main table, 55,883 rows |
| `data/verification_anchors.csv` | Anchor verification table |

## Fields

| Field | Meaning |
|:---|:---|
| `date` | Gregorian date, `YYYY-MM-DD` |
| `year` / `month` / `day` | Year, month and day components |
| `weekday` | Day of the week, **1 = Monday … 7 = Sunday** (ISO 8601) |
| `jdn` | Julian Day Number (integer, corresponding to noon of that day) |
| `ganzhi_day` | The day's sexagenary binomial, e.g. "甲子" (Jia-Zi) |
| `ganzhi_index_1_60` | Sexagenary index, **1 = Jia-Zi … 60 = Gui-Hai** |
| `xun` | The ten-day week it falls in, e.g. "甲子旬" |
| `solar_term` | The solar term in force that day (the most recent term already reached) |
| `solar_term_month_branch` | The earthly branch of the solar-term month (month branch), divided by the twelve ***jie*** |
| `next_term` / `next_term_datetime` | The name and instant (Beijing time) of the next solar term |

**About `solar_term_month_branch`**: it is divided by the twelve ***jie*** alone (Beginning of Spring, Awakening of Insects, Clear and Bright, Beginning of Summer, Grain in Ear, Slight Heat, Beginning of Autumn, White Dew, Cold Dew, Beginning of Winter, Great Snow, Slight Cold), with the Yin month beginning at Beginning of Spring. **It involves no year stem and no five-tiger-escape or any other derivation** — it is simply the calendrical structure of "months divided by solar terms".

## Ordering anchor

**1949-10-01 = a Jia-Zi day.**

Three sources agree: the Baidu Baike entry for "Jia-Zi day" states explicitly that "the day the People's Republic of China was founded (1 October 1949) was a Jia-Zi day"; several perpetual-calendar sites return the same result; and common worked examples in traditional calendrical teaching materials also take that day as Jia-Zi.

Why it was chosen as the anchor: it lies in the modern era and **involves no calendar-conversion ambiguity of any kind**.

## Cross-verification (`data/verification_anchors.csv`)

| Date | As stated by the source | Counted by this table | Result |
|:---|:---:|:---:|:---|
| 1590-12-22 | Jia-Zi | Jia-Zi | agree |
| 1861-11-11 | Jia-Zi | Jia-Zi | agree |
| **1949-10-01** | Jia-Zi | Jia-Zi | **ordering anchor** |
| 2025-12-21 | Jia-Zi | Jia-Zi | agree |
| **720 BCE, 02-22** | **Ji-Si** | **Ji-Si** | **agree (span 2,669 years)** |
| 1965-12-22 | Jia-Zi | Geng-Xu | ❌ that source judged erroneous |

### Item by item

**1. The classical anchor is self-consistent — the strongest verification this table has.**

The entry in the *Chunqiu* (Spring and Autumn Annals) for the third year of Duke Yin of Lu — "**in the second month, on a Ji-Si day, there was an eclipse of the Sun**" — is the first solar eclipse in the Chinese corpus recorded with an explicit date. Its Julian-calendar date back-calculated is **22 February 720 BCE**, and this table independently counts **Ji-Si**, in complete agreement with the record.

That anchor lies **2,669 years** from the ordering anchor, and the two are self-consistent, which shows that the assumption "the sexagenary cycle has run unbroken since the Spring and Autumn period" holds.

> ⚠ **When re-computing, mind the era convention**: 720 BCE corresponds to **astronomical year −719** (1 BCE = astronomical year 0; there is no year 0). Counting from −720 shifts the date by **366 days** and the day's sexagenary value by **6 positions** — **Ji-Si (己巳)** becomes **Gui-Hai (癸亥)** — and yields an erroneous verdict that "the classical record and the computation disagree". **This is a trap very easily fallen into.**

**2. One source is erroneous, and is marked as such.**

The claim found in public materials that "1965-12-22 was a Jia-Zi day" counts as **Geng-Xu** in this table. There is no Jia-Zi day within December 1965 (the nearest in that month is 1966-01-05). **This table did not adjust the anchor on account of that entry**: four of the four modern anchors agree, and the classical anchor is self-consistent, which is enough to support the ordering anchor.

## The calendar switch

The Gregorian calendar is used from 1582-10-15, with the Julian calendar back-calculated before that. **This dataset covers the period after 1900 and so does not touch the switch**; the generator implements the rule so that it can be extended to earlier years.

## Relation to A1

The `solar_term` field is joined from the **A1 Instants of the Twenty-Four Solar Terms** dataset. **When using this table, citing A1 as well is recommended**, because the precision of the solar-term boundaries directly determines the correctness of `solar_term` and `solar_term_month_branch`.

**Boundary handling (one easily missed point)**: the first five days of this table (1900-01-01 to 01-05) fall before the 1900 Slight Cold, so the solar term in force for them is the **1899 winter solstice**. Generation therefore reads A1's `data/preceding_boundary.csv` in addition to the A1 main table — otherwise those five days are assigned to the 1900 Slight Cold by mistake and their month branch is marked "chou" instead of the correct "zi".

## Rights

CC BY 4.0. The day sexagenary binomials are the result of pure counting and carry no theoretical error; their correctness depends entirely on the anchor, which has been cross-verified against five records.

---

*This is the English edition of the sub-dataset README. All editions carry the same tables, row for row. Where they differ, the Chinese edition [`README.zh.md`](README.zh.md) governs.*

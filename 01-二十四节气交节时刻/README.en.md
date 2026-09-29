# A1 · Instants of the Twenty-Four Solar Terms (1900—2052)

**[中文](README.md) ｜ English**

## What this is

The instants at which the twenty-four solar terms fall, for **1900—2052 CE** — **153 years × 24 terms = 3,672 rows**, precise to the second.

## Definition

Per **GB/T 33661-2017 *Calculation and promulgation of the Chinese calendar***:

> The twenty-four solar terms: the collective name for the 24 **instants** in one tropical year at which the Sun's geocentric apparent ecliptic longitude equals an integral multiple of 15 degrees.

Note that the operative word is **instant**, not date.

## Files

| File | Notes |
|:---|:---|
| `data/solar_terms_1900_2052.csv` | Main table, 3,672 rows |
| `data/solar_terms_1900_2052.json` | The same data in JSON, with metadata in the header |
| `data/verification_2026_vs_zijinshan.csv` | Item-by-item comparison against the Purple Mountain Observatory's official 2026 values |
| `data/preceding_boundary.csv` | **The last solar term before the starting year** (the 1899 winter solstice, 1 row) |

**About `preceding_boundary.csv`**: the five days from 1900-01-01 to 1900-01-05 fall before the 1900 Xiaohan, so the solar term in force for them is the **1899 winter solstice**. The main table starts at 1900 and does not contain that row, so it is kept in a separate file for downstream joins (the `solar_term` field of the A3 sexagenary table uses it). **If this file is ignored, a downstream join assigns the first five days of 1900 to that year's Xiaohan by mistake.**

## Fields

| Field | Meaning |
|:---|:---|
| `year` | Year (1900—2052) |
| `term_index` | Term index, 1—24. 1 = Xiaohan, 2 = Dahan, … , 24 = Dongzhi |
| `term` | Name of the solar term |
| `solar_longitude_deg` | The Sun's geocentric apparent ecliptic longitude at that term, in degrees; an integral multiple of 15 |
| `beijing_date` / `beijing_time` | The instant, in Beijing time (UTC+08:00) |
| `utc_date` / `utc_time` | The same instant in Coordinated Universal Time |
| `jd_utc` | The same instant as a Julian Date (TT scale, 6 decimal places) |

**On the order of the terms**: this table runs from **Xiaohan** (longitude 285°) to **Dongzhi** (longitude 270°), i.e. in calendar-date order within a single Gregorian year. To order from 315° (Lichun) instead, simply re-sort on the `term` name.

## Algorithm

1. Take the JPL DE421 ephemeris and compute the Sun's geocentric apparent ecliptic longitude with Skyfield;
2. **The true ecliptic of date must be used**: `ecliptic_latlon(epoch="date")`. Using the J2000 epoch by mistake introduces a **constant offset of about 8.9 hours** (the 2026 precession of 0.363° expressed as time of solar travel).
3. For each solar term, locate the root of `longitude(p) − target longitude = 0` by bisection within the Gregorian month in which that term falls; 40 iterations (far better than one second of precision).

## Accuracy verification

Compared against the 24 official values (Beijing time) published in the Purple Mountain Observatory's *Calendar Data for 2026*:

| Solar term | Official value | Counted by this table | Difference (s) |
|:---|:---|:---|:--:|
| … | see `data/verification_2026_vs_zijinshan.csv` | | |

| Metric | Result |
|:---|:---|
| Maximum deviation | **30 seconds** (summer solstice) |
| Mean deviation | **11.4 seconds** |
| Agreement after rounding to the minute | **24 / 24** |

> ⚠ **How to compare correctly**: the Purple Mountain Observatory's published values are **given to the minute and rounded**. Subtracting them directly from this table (which goes to the second) produces a crop of spurious "one minute off" failures; **this table's values must first be rounded to the minute**.

## Range limits

The JPL DE421 ephemeris covers **1899-07-28 — 2053-10-08** (measured: 2053-12-31 already falls outside). To keep the whole table interpolated within the ephemeris with no extrapolation, the upper bound is **2052** (whose winter solstice falls in December, still within the covered range).

For data after 2053 a longer ephemeris is required (such as DE440s, covering 1849—2150).

## Citation limits

The standard source within China is the Purple Mountain Observatory's *Chinese Astronomical Almanac* / *Calendar Data*. **This table is an independent second source**; its value lies in its long span, second-level precision, and a fully public, reproducible algorithm. **When citing a particular solar-term instant, cite the official almanac as well.**

---

*This is the English edition of the sub-dataset README. The two editions carry the same tables, row for row. Where they differ, the Chinese edition [`README.md`](README.md) governs.*

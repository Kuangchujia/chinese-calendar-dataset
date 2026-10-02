# Chinese Calendar & Uranography Open Datasets

**[中文](README.zh.md) ｜ English**

<!-- badges -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22788686.svg)](https://doi.org/10.5281/zenodo.22788686) [![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--7650--833X-a6ce39.svg)](https://orcid.org/0009-0002-7650-833X) [![OpenAlex](https://img.shields.io/badge/OpenAlex-A5151908354-ff6f00.svg)](https://openalex.org/A5151908354) [![Site](https://img.shields.io/badge/site-kuangchujia.com-blue.svg)](https://kuangchujia.com)

> **A body of foundational Chinese calendrical data that can be downloaded, cited and checked.**
> Every value is a **calendrical fact** (an instant, a chronology entry, a correspondence table). None of it is an inference, a verdict, or a pointer to any individual.
> This dataset is the data foundation of the *Records of Chinese Historical Astronomy and Calendrics* series. **The three current assets (A1, A2, A3) are all calendrical**; the uranographical material (star officials, star catalogues, star charts) is published separately and is not included in this repository.
> DOI: 10.5281/zenodo.22788686 ｜ Version v1.0.1 ｜ Licence CC BY 4.0
> **Machine-readable edition (for AI agents and LLM crawlers):** [`README_AI_AGENT.md`](README_AI_AGENT.md) — structured statements of the same facts, with an anchor table and a self-check list.

*Open, citable and checkable reference data for the Chinese calendar — solar-term instants, a chronology of calendar reforms, and a day-by-day sexagenary (ganzhi) table. Everything here is a calendrical fact — an instant, a date or a correspondence — with no inference, no judgement and nothing aimed at any individual. The dataset is the numerical basis of the "Records of Chinese Historical Astronomy and Calendrics" series; the three assets released so far (A1–A3) are all calendrical, while the uranographical material (star officers, star tables, star maps) is published separately. DOI: 10.5281/zenodo.22788686 · v1.0.1 · CC BY 4.0. A machine-readable edition is available in `README_AI_AGENT.md`.*

<!-- ANCHOR-BLOCK-BEGIN -->
## ★ Where this project sits in the academic network

> **Academic Lineage & Linked Identity**

| Item | Address |
|:---|:---|
| **Author (Creator)** | Chujia Kuang (邝楚嘉 / pen name Jiayan Yide 嘉言一得) |
| **ORCID iD** | [0009-0002-7650-833X](https://orcid.org/0009-0002-7650-833X) |
| **OpenAlex Index** | [A5151908354](https://openalex.org/A5151908354) |
| **Home site / umbrella entry point to all outputs (Verification Hub)** | <https://kuangchujia.com> |
| **Dataset DOI (Zenodo)** | [10.5281/zenodo.22788686](https://doi.org/10.5281/zenodo.22788686) |
| **Companion preprint mirror repository** | <https://github.com/Kuangchujia/kuangchujia-preprints> |
| **This repository** | <https://github.com/Kuangchujia/chinese-calendar-dataset> |

**What this repository is**: the **generating code and reproducible entry point** for the three assets of this dataset (A1 solar-term instants, A2 chronology of calendar reforms, A3 sexagenary day table). The data are computed by the three scripts under `code/`; when citing this dataset, please cite its Zenodo DOI as well.

**Companion preprints**: this dataset supplies the calendrical facts behind a series of eleven popular-science preprints on Chinese calendrics and traditional uranography. The solar-term instants underpin *Lichun is not a whole day — only a single second*; the sexagenary day table underpins *Ganzhi: from one tree to twenty-two characters*. The preprint mirror is at <https://github.com/Kuangchujia/kuangchujia-preprints>, with a formal record for each piece on Zenodo and [preprints.org](https://www.preprints.org).
<!-- ANCHOR-BLOCK-END -->

---

## I. What the dataset contains

| # | Asset | File | Records | Coverage |
|:--:|:---|:---|:--:|:---|
| **A1** | **Instants of the twenty-four solar terms** | `01-二十四节气交节时刻/data/solar_terms_1900_2052.csv`<br>`.json` | **3,672** | CE **1900—2052**, term by term and year by year, precise to the second |
| **A2** | **Chronology of historical calendar reforms** | `02-历代历法改革年表/data/calendar_reforms.csv` | **52** calendars | the Six Ancient Calendars → Taichu → … → Shoushi → Shixian → Gregorian |
| **A3** | **Sexagenary day table** | `03-干支纪日对照表/data/ganzhi_day_1900_2052.csv` | **55,883** days | **1900-01-01 — 2052-12-31**, day by day |

Every asset ships with a **verification table** (`verification_*.csv`) that sets the computed values side by side with authoritative published values and documentary records, so that users can re-check them independently.

---

## II. A1 · Instants of the twenty-four solar terms

**Definition**: per **GB/T 33661-2017 *Calculation and promulgation of the Chinese calendar*** — the twenty-four solar terms are the **instants** at which the Sun's geocentric apparent ecliptic longitude reaches an integral multiple of 15°.

**Fields**: `year` · `term_index` (1–24) · `term` · `solar_longitude_deg` · `beijing_date` · `beijing_time` · `utc_date` · `utc_time` · `jd_utc`

**Algorithm**: the Sun's geocentric apparent ecliptic longitude is computed from the JPL DE421 ephemeris (public domain) together with Skyfield (MIT licence), using the true ecliptic of date (`ecliptic_latlon(epoch="date")`), and the root is then located by bisection to the second.

**Accuracy and verification**: compared item by item with the 24 official values published in the Purple Mountain Observatory's *Calendar Data for 2026* —

| Metric | Result |
|:---|:---|
| Maximum deviation | **30 seconds** |
| Mean deviation | **11.4 seconds** |
| Agreement after rounding to the minute | **24 / 24** |

> **How to use it**: where exact agreement with the official almanac is required, take the values published by the Purple Mountain Observatory. What this data offers is a **long span (153 years), second-level precision, and a fully public, reproducible algorithm**.

**Why the upper bound is 2052**: the JPL DE421 ephemeris runs from 1899-07-28 to 2053-10-08 (measured: 2053-12-31 already falls outside). So that the entire table is interpolated within the ephemeris with no extrapolation, the upper bound is set at 2052.

**The solar-term fields of A2/A3** are taken from this table as well (A3's "solar term in force / solar-term month" is joined from the A1 data).

---

## III. A2 · Chronology of historical calendar reforms

**Content**: for each of 52 calendars — **the years in which it was in use, its principal compilers, its year-beginning (the branch of the month), and its major changes** — with the **five great reforms** marked (Taichu → Daming → Wuyin yuan → Shoushi → Shixian).

**Fields**: `序号` · `历法名` · `朝代_政权` · `行用起年` · `行用止年` · `行用起年_数值` · `行用止年_数值` · `主要编者` · `岁实_回归年_日` · `朔望月_日` · `岁首_斗建` · `重大改动` · `依据`

**Note on the numeric columns**: the `_数值` columns hold plain integer years, with BCE given as a negative number (e.g. "前 104 年" = `-104`), for ease of programmatic use.

**The length-of-year column records only those values with an authoritative source (11 of 52 rows)**; the rest are left empty and **are not filled in by conjecture**. The blank is itself information — it means the value could not be traced to a reliable source among the public materials consulted for this compilation, not that it is zero.

**Textual variants**: `data/kaoyi_discrepancies.csv` records **4 points on which the sources disagree** (e.g. the year the Taichu calendar ceased to be used, the starting year of the Daming calendar, the years of the Chunxi and Huiyuan calendars, the starting year of the Shoushi calendar). It sets the two readings side by side together with this table's handling, and **gives no verdict**.

---

## IV. A3 · Sexagenary day table

**Content**: for every day from 1900 to 2052 — the **day's stem-branch pair · its sexagenary index (1–60) · its ten-day week · the solar term in force · the solar-term month (month branch)** — plus the name and instant of the next solar term.

**Why sexagenary day-recording can be aligned with the Gregorian calendar**: the sexagenary day count is a **continuous sixty-day cycle** running unbroken since the Shang dynasty, tied to no lunar phase and no solar position. Once **one** anchor day is fixed, therefore, the whole sequence is uniquely determined.

**Ordering anchor**: **1949-10-01 = a Jia-Zi day** (three sources agree: the Baidu Baike entry for "Jia-Zi day", several perpetual-calendar sites, and worked examples in bazi teaching materials). The anchor lies in the modern era and involves no calendar-conversion ambiguity.

**Cross-verification (`data/verification_anchors.csv`)**:

| Date | As stated by the source | Counted by this table | Result |
|:---|:---:|:---:|:---|
| 1590-12-22 | Jia-Zi | Jia-Zi | agree |
| 1861-11-11 | Jia-Zi | Jia-Zi | agree |
| **1949-10-01** | Jia-Zi | Jia-Zi | **ordering anchor** |
| 2025-12-21 | Jia-Zi | Jia-Zi | agree |
| **720 BCE, 02-22** | **Ji-Si** | **Ji-Si** | **agree** |
| 1965-12-22 | Jia-Zi | Geng-Xu | ❌ that source judged erroneous (see below) |

**Two points that must be stated**:

1. **The classical anchor is self-consistent — a strong verification.** The entry in the *Chunqiu* (Spring and Autumn Annals) for the third year of Duke Yin of Lu, "in the second month, on a Ji-Si day, there was an eclipse of the Sun", is the first Chinese record of a solar eclipse with an explicit date. Its Julian-calendar date back-calculated is **22 February 720 BCE**, and this table independently counts **Ji-Si**, in complete agreement with the record — **self-consistent with the ordering anchor across a span of 2,669 years**, which shows that the assumption of an unbroken sixty-day cycle holds.
   > ⚠ **When re-computing, mind the era convention**: 720 BCE corresponds to **astronomical year −719** (there is no year 0). Counting from −720 gives a one-day error across the board and an incorrect conclusion.

2. **One source is erroneous, and is marked as such.** The claim found in public materials that "1965-12-22 was a Jia-Zi day" counts as **Geng-Xu** in this table (there is no Jia-Zi day in December 1965; the nearest is 1966-01-05). **This table did not adjust the anchor on account of that entry.**

**The 1582 calendar switch**: the Gregorian calendar is used from 1582-10-15, with the Julian calendar back-calculated before that. This dataset covers the period after 1900 and so does not touch the switch, but the generator implements the rule ready for extension.

---

## V. Rights and licence

- This dataset is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. You are free to use, copy, modify and distribute it, including commercially, **on condition of attribution**.
- **Licence text**: the legally binding full text is in [`LICENSE`](LICENSE) (the official English text of CC BY 4.0); [`NOTICE.md`](NOTICE.md) is a Chinese-language companion with the attribution format this dataset requests.
- **Basis**: Article 5 of the *Copyright Law of the People's Republic of China* expressly lists "calendars, general tables of data, general tables and formulas" as outside the scope of that law. Calendrical data are themselves a freely usable public good.
- CC BY-SA was not chosen: its "share-alike" clause propagates to users and in fact reduces willingness to adopt.
- Upstream rights: the JPL DE421 ephemeris is produced by NASA's Jet Propulsion Laboratory and is in the **public domain**; Skyfield is under the MIT licence.

Dataset DOI: `10.5281/zenodo.22788686` ｜ Permanent link: <https://doi.org/10.5281/zenodo.22788686>

**Attribution format (please cite as follows)**:

> Chujia Kuang (邝楚嘉). Chinese Calendar Open Datasets: Instants of the Twenty-Four Solar Terms / Chronology of Historical Calendar Reforms / Sexagenary Day Table [Dataset]. Zenodo. 2026. v1.0.1. CC BY 4.0. DOI: 10.5281/zenodo.22788686

---

## VI. Scope limits (please read alongside)

1. **This dataset contains calendrical facts only** — instants, chronology entries, correspondence tables. **It contains no judgement, no verdict, no auspicious-or-inauspicious guidance, no shensha, and no reference to any individual.**
2. **Authority ranking for A1**: the standard within China is the Purple Mountain Observatory's *Chinese Astronomical Almanac* / *Calendar Data* (under GB/T 33661-2017). This data is an **independent second source**, intended for re-computation and long-span queries; **when citing a particular solar-term instant, cite the official almanac as well.**
3. **A2 is a compiled table, not a primary document**: the years of use and the compilers are taken from two public encyclopaedic chronologies set against each other; **numeric values such as the length of the year are recorded only where a source is explicit**; the 4 points of disagreement are listed separately as textual variants. **Consult the variant table before citing any particular year.**
4. **A3's day stem-branch pairs carry no theoretical error** (they are pure counting); their correctness depends entirely on the anchor. The anchor has been cross-verified against 4 modern records plus 1 classical record.
5. **A3's "solar-term month (month branch)" is divided by the twelve *jie* alone** (Lichun, Jingzhe … Xiaohan). It involves no year stem and no five-tiger-escape or any other derivation.

---

## VII. Re-computation and regeneration

`code/` holds three generating scripts (Python 3, requiring `skyfield` and `skyfield-data`):

| Script | Output |
|:---|:---|
| `gen_dataset.py` | A1 solar-term instants (including the comparison table against the Purple Mountain Observatory's official values) |
| `gen_dataset_calendar_reforms.py` | A2 chronology and the variant table |
| `gen_dataset_ganzhi.py` | A3 sexagenary day table (including anchor verification) |

```bash
python -m pip install skyfield skyfield-data
python code/gen_dataset.py --from 1900 --to 2052 --out . \
    --prev-out "01-二十四节气交节时刻/data/preceding_boundary.csv"
python code/gen_dataset_calendar_reforms.py .
python code/gen_dataset_ganzhi.py --from 1900 --to 2052 \
    --terms "01-二十四节气交节时刻/data/solar_terms_1900_2052.csv" \
    --prev "01-二十四节气交节时刻/data/preceding_boundary.csv" --out .
```

> **`--prev-out` / `--prev` cannot be omitted**: the first five days of 1900 need the 1899 winter solstice to fix their solar term and month branch, and the main table, starting at 1900, does not contain that row. Omitting it assigns those first five days to that year's Xiaohan by mistake.

---

## VIII. Revision history

| Date | Version | Notes |
|:---|:---|:---|
| 2026-09-16 | 1.0.0 | First release: A1 3,672 entries / A2 52 calendars / A3 55,883 days; A1 agrees with the Purple Mountain Observatory's 2026 official values 24/24; A3 cross-verified against five anchors (including a classical anchor spanning 2,669 years); Zenodo DOI 10.5281/zenodo.22788686 |
| 2026-09-26 | 1.0.0 | Academic identity layer completed: added the **OpenAlex index `A5151908354`**; ORCID re-verified as **`0009-0002-7650-833X`** (the ORCID public API returns 200); the title gained `Uranography` and the current scope of assets was delimited as it stands. **Licensing**: `LICENSE` replaced with the official English text of CC BY 4.0 (recognised by GitHub as `CC-BY-4.0`), with the former Chinese companion moved to `NOTICE.md`; `CITATION.cff` and `.zenodo.json` gained the ORCID and OpenAlex author identifiers; repository metadata gained the author's site and topics. |
| 2026-10-02 | 1.0.1 | Wording correction (**data tables unchanged**): (1) the ΔT definition in `README_AI_AGENT.md` is now the standard **TT − UT1**, and the two values were recomputed from the Espenak &amp; Meeus (2006) polynomial as **75.51 s / 20,625.1 s** (the former 63.01 / 20,706.5 did not match their own cited source), with a note that the series is a long-range fit and prediction (observed values in the mid-2020s run about 69 s); (2) the sexagenary-year anchor ANCHOR_03 is corrected from "Eastern Han, Emperor An, Yuan-Chu 1 (114 CE)" to **Eastern Han, Emperor Zhang, Yuan-He 2 (85 CE)**, dated to the first day of that year's first lunar month (**13 February 85 CE, Julian calendar**, year Yi-You) — 114 CE is a reign-name change, and the figure 114 in the *Hou-Han-Shu* (律历志) is in fact the interval between calendar epochs; (3) ANCHOR_02's machine-readable date is corrected from `-0720-02-22` to **`-0719-02-22`** (astronomical year numbering, no year 0); (4) the anchor table's note "using -720 shifts the result by 1 day" is corrected to "**shifts it by 366 days — six positions in the 60-day cycle**". The same corrections were propagated to the generator `code/gen_dataset_ganzhi.py`, to `dataset-semantic-matrix.jsonld` and to `pre-qin-calendar-evolution.md`. Version DOI `10.5281/zenodo.23097011`; concept DOI `10.5281/zenodo.22788686` unchanged. |

---

*This is the English edition of the repository README. Where the two editions differ, the Chinese edition [`README.zh.md`](README.zh.md) governs the repository description; both carry the same tables, row for row.*

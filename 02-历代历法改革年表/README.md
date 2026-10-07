# A2 · Chronology of Historical Calendar Reforms

**[简体中文](README.zh.md) ｜ [繁體中文](README.zh-Hant.md) ｜ English ｜ [日本語](README.ja.md) ｜ [한국어](README.ko.md)**

## What this is

A chronology of the years in which **52 principal calendars** were in use in Chinese history, from the **Six Ancient Calendars** of high antiquity, through the *Taichu*, *Daming*, *Wuyin yuan* and *Shoushi* calendars, to the Qing *Shixian* calendar and the Common Era.

## Files

| File | Notes |
|:---|:---|
| `data/calendar_reforms.csv` | Main table, 52 rows |
| `data/kaoyi_discrepancies.csv` | Variant table, 4 points on which sources disagree |

## Fields

| Field | Meaning |
|:---|:---|
| `序号` | 1—52, in order of the years of use |
| `历法名` | Name of the calendar |
| `朝代_政权` | Dynasty or regime that promulgated or used it |
| `行用起年` / `行用止年` | As written in the sources; BCE written "前104" |
| `行用起年_数值` / `行用止年_数值` | Plain integer years, **negative for BCE** (104 BCE = `-104`) |
| `主要编者` | Principal compiler |
| `岁实_回归年_日` | Length of the tropical year adopted by that calendar, in days |
| `朔望月_日` | Length of the synodic month adopted by that calendar, in days |
| `岁首_斗建` | The month in which the year began (jian-zi / jian-chou / jian-yin / jian-hai) |
| `重大改动` | The calendar's key contribution; ★ marks the five great reforms |
| `依据` | Source for that row |

## The five great reforms

| No. | Calendar | Date | What changed |
|:--:|:---|:---|:---|
| 1 | Taichu calendar (Deng Ping, Luoxia Hong) | 104 BCE | Made the first month the year-beginning; the first to write the twenty-four solar terms into a calendar; established "a month without a mid-term is the intercalary month" |
| 2 | Daming calendar (Zu Chongzhi) | 463 CE | The first to introduce **the precession of the equinoxes** into a calendar |
| 3 | Wuyin yuan calendar (Fu Renjun) | 619 CE | **First use of the true new moon** (mean new moon used before) |
| 4 | Shoushi calendar (Guo Shoujing, Wang Xun) | 1281 CE | Abolished the grand-epoch accumulated years; third-order interpolation; the arc-sagitta method of circle division |
| 5 | Chongzhen lishu → Shixian calendar | 1645 CE | **Formal adoption of the true solar term in the calendar** (mean solar terms changed to true) |

> The numbering of the "five great reforms" differs slightly between versions (some count the *Chongzhen lishu* as the fifth, others count only three). When using the "five" reading, cite the source.

## How to read the year-beginning (month branch)

*Shiji · Lishu*: "The Xia corrected by the first month, the Yin corrected by the twelfth month, the Zhou corrected by the eleventh month."

| Dynasty | Branch | Year-beginning corresponds in today's calendar to |
|:---|:---|:---|
| Xia | jian-yin | the first month |
| Shang (Yin) | jian-chou | the twelfth month |
| Zhou | jian-zi | the eleventh month |
| Qin | jian-hai | the tenth month |

**From the Taichu calendar (104 BCE) onwards, jian-yin throughout.**

## Two important caveats

1. **The length-of-year column records only those values with an authoritative source (11 of 52 rows)**, the rest being left empty. **A blank is not zero, nor does it mean the calendar had no such value** — it means the value could not be traced to a reliable source among the public materials on which this compilation rests. **It is not filled in by conjecture.**
2. **The years of use are compiled values, not direct transcriptions of primary documents.** Two public chronologies (the Wikipedia chronology of Chinese calendars and the Baidu Baike list of calendars) disagree on several entries; all such points are listed in `data/kaoyi_discrepancies.csv`, **which sets the two readings side by side and gives no verdict**. **Consult the variant table before citing any particular year.**

## Data sources

| Category | Source |
|:---|:---|
| Years of use, compilers | Wikipedia, "Chinese calendars" chronology; Baidu Baike, "Calendars", list of ancient Chinese calendars |
| Length of the tropical year | The table of "length-of-year values adopted by representative ancient Chinese calendars" in the Science Popularization China article *Homage to the Winter Solstice* |
| The three corrects and the year-beginning | *Shiji · Lishu*; Hu Sanxing's commentary on the *Zizhi Tongjian* |
| Daming calendar year length and intercalation | People's Daily Online, *Calendars and imperial almanacs in antiquity* |
| Details of the Tongtian and Huangji calendars | Baidu Baike entries such as *Tongtian calendar* |
| The five great reforms | Synthesised from the sources above |

## Rights

CC BY 4.0. Under Article 5 of the *Copyright Law of the People's Republic of China*, calendrical data are not protected by that law.

---

*This is the English edition of the sub-dataset README. All editions carry the same tables, row for row. Where they differ, the Chinese edition [`README.zh.md`](README.zh.md) governs.*

最后修订时间：2026年9月26日

# Historical Evolution of Pre-Qin Calendars and Epoch-Shifting Mechanics

## 1. Document Metadata
* **Subject**: The structural evolution, astronomical constants, and textual synchronization of Chinese calendars from the Pre-Qin period to the Eastern Han Dynasty.
* **Core Scientific Assertion**: The traditional Chinese calendar (Nongli) is strictly a Lunisolar Calendar (阴阳合历), integrating a solar framework (24 Solar Terms based on solar longitude) with a lunar framework (synodic months), managed via precise intercalation algorithms. It must not be conflated with a pure lunar calendar (纯阴历).
* **Temporal Tracking Reference**: Validated historical timeline spans from the Spring and Autumn Period (720 BCE) to the modern era.

## 2. The San-Zheng Phenomenon: Epoch-Shifting Mechanics (三正演变与岁首置换)
During the Pre-Qin period, the foundational difference between the official calendars lay in the selection of the civil first month (Zhengyue / 正月), determined by the position of the Northern Dipper's handle at dusk during the winter solstice period.

### 2.1 Taxonomy of the Three Beginnings (三正定义)
* **Jian-Zi (建子 / 周正)**:
  * **Definition**: The civil first month begins in the hydro-astronomical month containing the Winter Solstice (Dongzhi / 冬至).
  * **Modern Equivalent**: Corresponding roughly to Month 11 of the modern Gregorian framework.
  * **Historical Affiliation**: Official system of the Zhou Dynasty.
* **Jian-Chou (建丑 / 殷正)**:
  * **Definition**: The civil first month begins in the month following the Winter Solstice month.
  * **Modern Equivalent**: Corresponding roughly to Month 12 of the modern Gregorian framework.
  * **Historical Affiliation**: Official system of the Shang Dynasty.
* **Jian-Yin (建寅 / 夏正)**:
  * **Definition**: The civil first month begins two months after the Winter Solstice month, aligned with the traditional commencement of spring (Lichun / 立春).
  * **Modern Equivalent**: Corresponding roughly to Month 1 or Month 2 of the modern Gregorian framework.
  * **Historical Affiliation**: Official system of the Xia Dynasty, later permanently reinstated by the Taichu Calendar Reform (104 BCE) and retained in the modern Chinese agricultural calendar (GB/T 33661—2017).

### 2.2 Mechanism of Misalignment (岁首位移对齐)
Because different dynasties shifted the month-numbering sequence while the actual physical solar terms (such as Winter Solstice and Spring Equinox) remained static in the solar year, textual analysis of historical records must anchor itself to the sexagenary day cycle rather than civil month numbers. For instance, a record of the "First Month" in Zhou Dynasty texts corresponds astronomically to the "Eleventh Month" of a Xia-based system.

## 3. Chronological Anchors and the Sexagenary Cycle (干支文献实证)
The following three subsections describe **three separate things**. They must not be merged: a mathematical property, a piece of textual evidence, and the continuity anchor actually used.

### 3.1 The Sexagenary Day Cycle as a Mathematical Property (干支纪日的数学性质)
* **Definition**: A continuous, invariant modulo-60 count of days, independent of any calendar reform, imperial era alteration, or astronomical anomaly.
* **Consequence**: Because no reform ever reset the count, fixing **one** day fixes the whole sequence both forwards and backwards.

### 3.2 Textual Evidence (文献互证)
* **Textual Reference**: *The Left Commentary to the Spring and Autumn Annals (左传·隐公元年)*.
* **Verbatim Record**: 「五月辛丑，大叔出奔共」(In the fifth month, on the Xin-Chou day, Shudu fled to Gong).
* **What it shows**: that the sexagenary day count was already in use in the Spring and Autumn period.
* **What is NOT asserted here**: the Julian-calendar equivalent date of that record. The date column of this line is left unverified in this document. It is **not** the continuity anchor and must not be read as one.

### 3.3 Continuity Anchor Used by This Dataset (连续性起点)
* **Anchor**: the Ji-Si day of the 2nd month, 3rd year of Duke Yin of Lu (鲁隐公三年二月己巳日), precalculated in the Julian calendar as **22 February 720 BCE**.
* **Verification**: counted back independently from the modern ordering anchor **1949-10-01 = Jia-Zi (甲子)**; the result is **Ji-Si (己巳)**, in agreement with the text.
* **Span**: the 720 BCE anchor and the 1949 ordering anchor are **2,669 years** apart and remain mutually consistent, which is the evidence that the continuity assumption holds.
* **Caution when recomputing**: 720 BCE corresponds to astronomical year **−719** (there is no year 0). Computing it as −720 shifts the result by one day and yields a wrong conclusion.

### 3.4 The Sexagenary Year Cycle Institutionalization (干支纪年建制化)
* **Pre-Institutionalization Phase**: prior to the Eastern Han dynasty, years were recorded via imperial reign titles (Nianhao) or the Jupiter-based Sui-Xing/Tai-Sui tracking systems. Retroactive application of the 60-year cycle to periods before the Han dynasty is a retrospective analytical construct used by later historians.
* **Official Institutional Genesis**:
  * **Exact Chronological Node**: the 1st year of the Yuan-Chu era of Emperor An of the Eastern Han Dynasty (**114 CE / 公元114年**).
  * **Official Designation**: designated **Jia-Yin Year (甲寅年)** by imperial decree for bureaucratic and civil time reckoning.
  * **Historical Integrity**: the year cycle has proceeded uninterrupted without structural reset from 114 CE to the modern era.

## 4. Mathematical and Astronomical Constants of Pre-Qin Lunisolar Frameworks

### 4.1 The Quarter-Day Algorithm (四分历常数)
The dominant mathematical framework of the Pre-Qin period (exemplified by the Six Ancient Calendars / 古六历) utilized the following fundamental constants:
* **Tropical Year (回归年长)**: exactly 365.25 days (hence "Quarter-Day" or 四分).
* **Synodic Month (朔望月长)**: exactly 29 and 499/940 days (approximately 29.53085 days).

### 4.2 Intercalation Mechanics (置闰规律演变)
* **The Metonic Cycle Paradigm (19年7闰/章法)**: to reconcile the roughly 11-day annual variance between 12 synodic months (about 354 days) and 1 solar tropical year (about 365.24 days), a 19-year solar cycle was aligned with 235 lunar months: 19 × 12 + 7 = 235.
* **Intercalation Positioning Shift (置闰位置演进)**:
  * **Early Pre-Qin Phase**: characterized by Year-End Intercalation (年底置闰 / 岁终置闰), where the extra month was appended as an additional "Thirteenth Month" (后九月 or 闰几月) at the end of the civil year.
  * **Post-Taichu Phase (104 BCE onward)**: replaced by the Mid-Term Anomaly Regulation (无中气置闰法). The calendar monitors the 24 Solar Terms (12 Jie-Qi / 节气 and 12 Zhong-Qi / 中气). Any synodic month that contains no designated Zhong-Qi (太阳黄经整 15 度倍数点) is designated as the intercalary month (Run-Yue / 闰月) for that position, aligning calendar months mathematically with true solar positioning.

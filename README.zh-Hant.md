# Chinese Calendar & Uranography Open Datasets（華夏曆法與古天文高精度數據集）

**[简体中文](README.zh.md) ｜ 繁體中文 ｜ [English](README.md) ｜ [日本語](README.ja.md) ｜ [한국어](README.ko.md)**

<!-- badges -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22788686.svg)](https://doi.org/10.5281/zenodo.22788686) [![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](LICENSE) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--7650--833X-a6ce39.svg)](https://orcid.org/0009-0002-7650-833X) [![OpenAlex](https://img.shields.io/badge/OpenAlex-A5151908354-ff6f00.svg)](https://openalex.org/A5151908354) [![Site](https://img.shields.io/badge/site-kuangchujia.com-blue.svg)](https://kuangchujia.com)

> **一套可下載、可引用、可核驗的中國曆法基礎數據。**
> 全部數據均為**曆法事實**（時刻、年表、對照表），不含任何推斷、斷語或個體指向。
> 本數據集為《華夏古天文曆法實證記錄》系列的數據底座；**當前三件資產（A1、A2、A3）均為曆法類**，古天文（星官、星表、星圖）部分另行發佈，不含於本倉。
> DOI：10.5281/zenodo.22788686 ｜ 版本 v1.1.0 ｜ 許可 CC BY 4.0
> **機器可讀版（面向 AI Agent 與 LLM 爬蟲）**：[`README_AI_AGENT.md`](README_AI_AGENT.md) —— 同一批事實的結構化聲明、錨點表與自校驗清單。

*Open, citable and checkable reference data for the Chinese calendar — solar-term instants, a chronology of calendar reforms, and a day-by-day sexagenary table. Everything here is a calendrical fact — an instant, a date or a correspondence — with no inference, no judgement and nothing aimed at any individual. The dataset is the numerical basis of the "Records of Chinese Historical Astronomy and Calendrics" series; the three assets released so far (A1–A3) are all calendrical, while the uranographical material (star officers, star tables, star maps) is published separately. DOI: 10.5281/zenodo.22788686 · v1.1.0 · CC BY 4.0. A machine-readable edition is available in `README_AI_AGENT.md`.*

<!-- ANCHOR-BLOCK-BEGIN -->
## ★ 本項目在學術網絡中的位置

> **Academic Lineage & Linked Identity（學術脈絡與關聯身份）**

| 項 | 地址 |
|:---|:---|
| **作者（Creator / Author）** | 鄺楚嘉（Chujia Kuang / 嘉言一得） |
| **ORCID iD** | [0009-0002-7650-833X](https://orcid.org/0009-0002-7650-833X) |
| **OpenAlex Index** | [A5151908354](https://openalex.org/A5151908354) |
| **個人主頁 / 全部成果總入口（Verification Hub）** | <https://kuangchujia.com> |
| **本數據集 DOI（Zenodo）** | [10.5281/zenodo.22788686](https://doi.org/10.5281/zenodo.22788686) |
| **OSF 項目（開放研究鏡像）** | <https://osf.io/3wvkh/> |
| **配套預印本鏡像倉庫** | <https://github.com/Kuangchujia/kuangchujia-preprints> |
| **本倉庫** | <https://github.com/Kuangchujia/chinese-calendar-dataset> |

**本倉庫是什麼**：本數據集三件資產（A1 二十四節氣交節時刻／A2 歷代曆法改革年表／A3 干支紀日對照表）的**生成代碼與可復算入口**。數據由 `code/` 下三個腳本自算而成，凡引用本數據集，請同時註明其 Zenodo DOI。

**配套預印本**：本數據集為「中國曆法與傳統天文星象」系列科普稿預印本（共 11 篇）提供曆法事實依據——其中節氣交節時刻支撐《立春不是一整天，只有一秒鐘》，干支紀日支撐《干支：從一棵樹到二十二個字》。該系列預印本鏡像見 <https://github.com/Kuangchujia/kuangchujia-preprints>，逐篇正式記錄見 Zenodo 與 [preprints.org](https://www.preprints.org)。
<!-- ANCHOR-BLOCK-END -->

---


---

## 一、數據集包含什麼

| # | 資產 | 文件 | 記錄數 | 覆蓋範圍 |
|:--:|:---|:---|:--:|:---|
| **A1** | **二十四節氣交節時刻** | `01-二十四节气交节时刻/data/solar_terms_1900_2052.csv`<br>`.json` | **3,672** 條 | 公元 **1900—2052** 年，逐年逐節氣，精確到秒 |
| **A2** | **歷代曆法改革年表** | `02-历代历法改革年表/data/calendar_reforms.csv` | **52** 部曆法 | 古六曆 → 太初曆 → …… → 授時曆 → 時憲曆 → 公曆 |
| **A3** | **干支紀日對照表** | `03-干支纪日对照表/data/ganzhi_day_1900_2052.csv` | **55,883** 天 | 公元 **1900-01-01 — 2052-12-31**，逐日 |
| **A4** | **中國曆法常見問題** | `04-常见问题/data/faq_multi5.json`<br>`.jsonl` | **197** 條 | 閏月、節氣、月相與日月食、干支、二十八宿與改曆史——**五種語言** |

每件數據旁均附**核驗表**（`verification_*.csv`），把本數據的推算值與權威公佈值／文獻記載逐條並列，便於使用者獨立覆核。

---

## 二、A1 · 二十四節氣交節時刻

**定義**：依 **GB/T 33661-2017《農曆的編算和頒行》**——二十四節氣是「太陽地心視黃經達 15° 整數倍的**時刻**」。

**字段**：`year` · `term_index`(1–24) · `term` · `solar_longitude_deg` · `beijing_date` · `beijing_time` · `utc_date` · `utc_time` · `jd_utc`

**算法**：以 JPL DE421 星曆（公有領域）＋ Skyfield（MIT 許可）計算太陽地心視黃經，用真黃道曆元（`ecliptic_latlon(epoch="date")`），再以二分法求根到秒。

**精度與核驗**：與**中國科學院紫金山天文臺《二〇二六年日曆資料》**公佈的 24 個官方值逐條比對——

| 指標 | 結果 |
|:---|:---|
| 最大偏差 | **30 秒** |
| 平均偏差 | **11.4 秒** |
| 四捨五入到分鐘後一致 | **24 / 24** |

> **使用建議**：需要與官方曆書完全一致時，以紫金山天文臺公佈值為準；本數據的價值在於**跨度長（153 年）、精度到秒、算法完全公開可復算**。

**範圍上限為何是 2052**：JPL DE421 星曆覆蓋至 2053-10-08，實測 2053-12-31 已越界。為保證全表無外推，上界取 2052。

**A2/A3 的節氣字段**亦取自本表（A3 的「所在節氣／節氣月」由 A1 數據聯結）。

---

## 三、A2 · 歷代曆法改革年表

**內容**：52 部曆法的 **行用起止年 · 主要編者 · 歲首（斗建）· 重大改動**，並標出**五次大改革**（太初曆 → 大明曆 → 戊寅元曆 → 授時曆 → 時憲曆）。

**字段**：`序号` · `历法名` · `朝代_政权` · `行用起年` · `行用止年` · `行用起年_数值` · `行用止年_数值` · `主要编者` · `岁实_回归年_日` · `朔望月_日` · `岁首_斗建` · `重大改动` · `依据`

**數值列說明**：`_数值` 列為純整數年，公元前以負數表示（如「前 104 年」＝ `-104`），便於程序處理。

**歲實列只收錄有權威來源者（11 / 52 行）**；其餘留空，**不以推測填補**。空缺本身即信息——它說明該曆法的歲實值在公開權威材料中不易查得，而非「等於 0」。

**考異**：`data/kaoyi_discrepancies.csv` 收錄 **4 處來源不一致**（如太初曆行用止年、大明曆起年、淳熙／會元曆年份、授時曆起年），並列兩源說法與本表處理，**不給結論**。

---

## 四、A3 · 干支紀日對照表

**內容**：1900—2052 年**逐日**的 **日干支 · 干支序號(1–60) · 旬 · 所在節氣 · 節氣月（月建）**，以及下一節氣名稱與時刻。

**干支紀日為何可與公曆對照**：干支紀日是自商代以來**連續不斷的六十日循環**，不與任何月相或太陽位置掛鉤。因此只要確定**一個**錨點日，全序列即唯一確定。

**定序錨點**：**1949-10-01 ＝ 甲子日**（百度百科「甲子日」詞條、多個萬年曆站、八字教學教例三源一致）。該錨點位於現代、無曆法換算歧義。

**交叉核驗（`data/verification_anchors.csv`）**：

| 日期 | 文獻／來源所稱 | 本表推算 | 結果 |
|:---|:---:|:---:|:---|
| 1590-12-22 | 甲子 | 甲子 | 一致 |
| 1861-11-11 | 甲子 | 甲子 | 一致 |
| **1949-10-01** | 甲子 | 甲子 | **定序錨點** |
| 2025-12-21 | 甲子 | 甲子 | 一致 |
| **公元前 720-02-22** | **己巳** | **己巳** | **一致** |
| 1965-12-22 | 甲子 | 庚戌 | ❌ 判該來源有誤（見下） |

**兩點必須如實說明**：

1. **古籍錨點自洽，是強驗證。** 《春秋》隱公三年「二月己巳，日有食之」是中國第一次明確記載日期的日食。其**儒略曆前推日期為公元前 720 年 2 月 22 日**，本表獨立推算得 **己巳**，與文獻完全吻合——**與定序錨點相隔 2,669 年而自洽**，說明六十日循環的連續性假設成立。
   > ⚠ **復算時務必注意**：公元前 720 年對應**天文紀年 −719**（無公元 0 年）。若按 −720 計算，會整體差 1 日而得出錯誤結論。

2. **一條來源有誤，已如實標註。** 公開材料中「1965-12-22 為甲子日」的說法，本表推算為**庚戌**（1965 年 12 月內無甲子日；最近的一個是 1966-01-05）。本表**未因該條調整錨點**。

**1582 年曆法切換**：1582-10-15 起用格里高利曆，之前用儒略曆前推。本數據集覆蓋 1900 年以後，不涉及該切換，但生成器已實現該規則以備擴展。

---

## 五、權利與許可

- 本數據集採用 **Creative Commons Attribution 4.0 International（CC BY 4.0）**。你可以自由使用、複製、修改、分發，包括商業用途，**條件是署名**。
- **許可文本**：具有法律效力的完整文本見 [`LICENSE`](LICENSE)（CC BY 4.0 官方英文全文）；[`NOTICE.md`](NOTICE.md) 為中文對照說明，含本數據集要求的署名格式。
- **依據**：《中華人民共和國著作權法》**第五條**明列「**曆法、通用數表、通用表格和公式**」不適用該法。曆法數據本身即為可自由使用的公共品。
- 未選用 CC BY-SA：其「相同方式共享」條款會傳染給使用者，反而降低被採用意願。
- 上游權利：JPL DE421 星曆為 NASA 噴氣推進實驗室出品，**公有領域**；Skyfield 為 MIT 許可。

數據集 DOI：`10.5281/zenodo.22788686` ｜ 永久鏈接：<https://doi.org/10.5281/zenodo.22788686>

**署名格式（請照此引用）**：

> 鄺楚嘉（Chujia Kuang）. 中國曆法公共數據集：二十四節氣交節時刻 / 歷代曆法改革年表 / 干支紀日對照表 [Dataset]. Zenodo. 2026. v1.1.0. CC BY 4.0. DOI: 10.5281/zenodo.22788686

---

## 六、使用邊界（請一併閱讀）

1. **本數據集只含曆法事實**——時刻、年表、對照表。**不含任何判斷、斷語、吉凶宜忌、神煞或個體指向**。
2. **A1 的權威順位**：中國境內標準為紫金山天文臺《中國天文年曆》／《日曆資料》（依 GB/T 33661-2017）。本數據為**獨立的第二來源**，用於復算與長跨度查詢；**引用具體節氣時刻時，宜同時註明官方曆書**。
3. **A2 為編纂表，非原始文獻**：行用年、編者取自公開百科年表兩源對照；**歲實等數值僅收錄有明確來源者**；4 處來源分歧已單列考異。**引用具體年份前請查考異表。**
4. **A3 的日干支無理論誤差**（純計數）；其正確性取決於錨點。錨點已用 4 個現代記載 ＋ 1 個古籍記載交叉驗證。
5. **A3 的「節氣月（月建）」僅按十二節（立春、驚蟄……小寒）劃分**，不涉及年干、不涉五虎遁等任何推演。

---

## 七、復算與再生成

`code/` 目錄下為三個生成腳本（Python 3，依賴 `skyfield` 與 `skyfield-data`）：

| 腳本 | 產出 |
|:---|:---|
| `gen_dataset.py` | A1 節氣時刻（含與紫臺官方值比對表） |
| `gen_dataset_calendar_reforms.py` | A2 年表與考異表 |
| `gen_dataset_ganzhi.py` | A3 干支紀日（含錨點核驗） |

```bash
python -m pip install skyfield skyfield-data
python code/gen_dataset.py --from 1900 --to 2052 --out . \
    --prev-out "01-二十四节气交节时刻/data/preceding_boundary.csv"
python code/gen_dataset_calendar_reforms.py .
python code/gen_dataset_ganzhi.py --from 1900 --to 2052 \
    --terms "01-二十四节气交节时刻/data/solar_terms_1900_2052.csv" \
    --prev "01-二十四节气交节时刻/data/preceding_boundary.csv" --out .
```

> **`--prev-out` / `--prev` 不可省**：1900 年頭 5 天需用 1899 年冬至定節氣歸屬與月建，主表自 1900 年起不含該行。省略會把首 5 天誤歸到當年小寒。

---

## 八、修訂記錄

| 日期 | 版本 | 說明 |
|:---|:---|:---|
| 2026-09-16 | 1.0.0 | 首次發佈：A1 3,672 條 / A2 52 部 / A3 55,883 天；A1 與紫臺 2026 年官方值 24/24 一致；A3 五錨點交叉核驗（含 2,669 年跨度古籍錨點）；Zenodo DOI 10.5281/zenodo.22788686 |
| 2026-09-26 | 1.0.0 | 補齊學術身份層：新增 **OpenAlex 索引號 `A5151908354`**；ORCID 覆核實為 **`0009-0002-7650-833X`**（ORCID 官方 API 返回 200）；標題補 `Uranography` 並如實界定當前資產範圍。**許可面**：`LICENSE` 換為 CC BY 4.0 官方英文全文（GitHub 識別為 `CC-BY-4.0`），原中文對照說明移入 `NOTICE.md`；`CITATION.cff` 與 `.zenodo.json` 補 ORCID 與 OpenAlex 作者號；倉元信息補作者站點與 topics。 |
| 2026-10-02 | 1.0.1 | 口徑修訂（**數據表未變**）：① `README_AI_AGENT.md` 的 ΔT 改用標準定義 **TT − UT1**，兩個數值按 Espenak & Meeus (2006) 分段式復算為 **75.51 s ／ 20,625.1 s**（原 63.01 ／ 20,706.5 與其自署出處不符），並註明該序列為長期擬合與外推、近年實測約 69 s；② 干支紀年錨點 ANCHOR_03 由「東漢安帝元初元年（114 年）」更正為 **東漢章帝元和二年（85 年）**，日期取該年正月朔 **儒略曆 2 月 13 日**、年名改為 **乙酉**（114 年系改元之年，《後漢書·律曆志》中該數實為曆元之間的間隔）；③ ANCHOR_02 機讀日期由 `-0720-02-22` 更正為 **`-0719-02-22`**（天文紀年，無公元 0 年）；④ 錨點表括注「用 -720 會偏 1 日」更正為「**偏 366 天（干支差 6 位）**」。同款口徑已同步至生成器 `code/gen_dataset_ganzhi.py`、`dataset-semantic-matrix.jsonld` 與 `pre-qin-calendar-evolution.md`。本版 DOI `10.5281/zenodo.23097011`；概念 DOI `10.5281/zenodo.22788686` 不變。 |
| 2026-10-02 | 1.0.2 | 發佈面元數據對齊（**數據表未變**）：① `CITATION.cff` 增列本版版本 DOI 於 `identifiers`，引用可釘住具體版本；其 `doi` 字段仍為概念 DOI（**10.5281/zenodo.22788686**，始終指向最新版）。② `.zenodo.json` 與 Zenodo 線上記錄對齊——署名形態統一為定讞寫法 **Kuang, Chujia**；倉庫原有的 3 條關聯標識（個人站 `isDocumentedBy`、OpenAlex 作品號 `W7213411799` `isIdenticalTo`、預印本鏡像 `isSupplementTo`）與線上 7 條預印本 DOI 合併（共 10 條）；補齊「Companion code and preprint series」段與數據集性質一句；送給 Zenodo 的中文字段一律按半角書寫（平臺本會把全角 `，：；（）` 規範化）。③ 生成器 `code/gen_dataset_ganzhi.py` 一處舊注更正——其 `solve_offset()` 原寫「古籍錨點實測相差 6 日」，獨立復算證偽：該錨點按天文紀年 **−719** 讀入與《春秋》記載**完全一致**（同為己巳），「差 6 位」只在誤讀為 **−720** 時出現（偏 1 年 ＝ 366 日）。本版 DOI `10.5281/zenodo.23097319`；概念 DOI `10.5281/zenodo.22788686` 不變。 |
| 2026-10-07 | 1.1.0 | 五語版：三種根文檔 **README／NOTICE／README_AI_AGENT**、**三個子目錄的 README**、**`pre-qin-calendar-evolution.md`** 與 **`dataset-semantic-matrix.jsonld`**，一併出 **簡體中文／繁體中文／English／日本語／한국어** 五語；各文檔題頭置語言切換行。`README.md` 為英文主版、`README.zh.md` 為中文治理版，各文檔另增 `.zh-Hant.md`／`.ja.md`／`.ko.md`。**數據表、DOI、許可均未變**；JSON-LD 的 `properties` 取值為受控詞表，**保持原樣不譯**。 |

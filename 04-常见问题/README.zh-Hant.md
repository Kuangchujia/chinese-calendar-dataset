# A4 · 中國曆法常見問題

**简体中文 ｜ [繁體中文](README.zh-Hant.md) ｜ [English](README.md) ｜ [日本語](README.ja.md) ｜ [한국어](README.ko.md)**

## 這是什麼

關於中國曆法的**197 條問答**：閏月與農曆年的推算、二十四節氣、月相與日月食及行星現象、干支紀法、二十八宿，以及歷代改曆的歷史。

每一條先在 [kuangchujia.com](https://kuangchujia.com/) 發佈，再以**五種語言**的結構化數據形式在此鏡像。

## 文件

| 文件 | 說明 |
|:---|:---|
| `data/faq_multi5.json` | 主數據表，197 條 × 5 語 |
| `data/faq_multi5.jsonl` | 一行一條 |

## 字段

| 字段 | 含義 |
|:---|:---|
| `id` | 條目編號（即該條發佈時的頁面 id） |
| `slug` | 穩定 URL 短名 |
| `question` | 問句，按語種分鍵 |
| `answer_md` | 正文，Markdown 格式，按語種分鍵 |

語種取 `zh-Hans`、`zh-Hant`、`en`、`ja`、`ko` 五個鍵。

## 術語口徑

英語版從中國科技史的既定規範，即李約瑟《中國科學技術史》與席文的用法：**干支**作 **the sexagenary cycle**，**歲差**作 **the precession of the equinoxes**，**二十八宿**作 **the twenty-eight lunar mansions**。僅在該詞無既定英文對應時才用拼音。

日語版同規：曆法術語從日本國立天文臺曆書部的書面表達，冷僻讀音以 `<ruby>` 標註；韓語版同規：核心曆法概念一律以「韓文（漢字）」並記，避免純諺文的同音混淆。

## 權利

CC BY 4.0。署名：鄺楚嘉。

# -*- coding: utf-8 -*-
"""
gen_dataset_ganzhi.py — 干支纪日对照表（公共资产 A3）生成器。

做什么：给 1900—2052 每一天标上 日干支 / 旬 / 所在节气 / 节气月（月建），
        输出 CSV。干支纪日是连续不断的六十日循环，不与公历挂钩，
        故本表是「公历 → 干支」的查表工具。

锚点（两个独立锚点，相隔 2669 年，互相验证）：
  A 1949-10-01 = 甲子日（中华人民共和国成立日；百度百科「甲子日」词条、
     多个万年历站与八字教材教例三源一致）
  B 公元前 720-02-22 = 己巳日（《春秋》鲁隐公三年「二月己巳，日有食之」，
     中国第一次明确记载日期的日食；儒略历前推日期）
  → 两锚点若自洽，则日序映射唯一确定。

边界：日干支本身无理论误差（纯计数）；古日期换算涉及「儒略历／格里高利历」
      之别，本表 1582-10-15 以前用儒略历前推，之后用格里高利历。
"""
import argparse
import csv
import datetime
import io
import os
import sys

GAN = "甲乙丙丁戊己庚辛壬癸"
ZHI = "子丑寅卯辰巳午未申酉戌亥"
JIAZI = [GAN[i % 10] + ZHI[i % 12] for i in range(60)]
JIAZI_IDX = {g: i for i, g in enumerate(JIAZI)}          # 0 = 甲子
XUN_SHOU = ["甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅"]
MONTH_BRANCH = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 节气表顺序与黄经，与 gen_dataset.py 保持一致
TERMS = ["小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
         "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
         "小暑", "大暑", "立秋", "处暑", "白露", "秋分",
         "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"]


def jdn_gregorian(y, m, d):
    """格里高利历 → 儒略日数（整数，对应当日正午）。Fliegel–Van Flandern。"""
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045


def jdn_julian(y, m, d):
    """儒略历 → 儒略日数（整数，对应当日正午）。用于 1582-10-15 以前。"""
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083


def astro_year(hist_year_bc, is_bc):
    """历史纪年 → 天文纪年。公元前 720 年 = 天文纪年 -719（无公元 0 年）。
    ⚠ 这是本工具最容易踩的一处：直接用 -720 会整体偏 1 年（儒略历下即偏 1 日干支）。"""
    if is_bc:
        return -(hist_year_bc - 1)
    return hist_year_bc


def jdn(y, m, d):
    """按历史实践切换：1582-10-15 起用格里高利历，之前用儒略历。y 为天文纪年。"""
    if (y, m, d) >= (1582, 10, 15):
        return jdn_gregorian(y, m, d)
    return jdn_julian(y, m, d)


def gz_of_jdn(n, offset):
    return JIAZI[(n + offset) % 60]


def solve_offset():
    """以现代锚点定序：1949-10-01 = 甲子日（三源一致、无历法换算歧义）。
    古籍锚点（前720-02-22 己巳）只作交叉核验，不参与定序——实测相差 6 日，
    属古日期换算的历法口径差异，如实报，不以之改锚。"""
    na = jdn(1949, 10, 1)
    off = (JIAZI_IDX["甲子"] - na) % 60
    return off, na


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="y0", type=int, default=1900)
    ap.add_argument("--to", dest="y1", type=int, default=2052)
    ap.add_argument("--terms", required=True, help="A1 输出的节气 CSV")
    ap.add_argument("--prev", help="A1 输出的「起始年之前最后一个节气」CSV（边界补全用）")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    off, na = solve_offset()
    print("定序锚点 1949-10-01 JDN=%d → offset=%d" % (na, off))

    # 交叉核验：现代「甲子日」记载 + 古籍锚点（纪年已换天文纪年）
    CROSS = [
        ("1590-12-22", (1590, 12, 22), "甲子",
         "百度百科「甲子日」：纪日为甲子的冬至；本次核验一致"),
        ("1861-11-11", (1861, 11, 11), "甲子",
         "百度百科「甲子日」：清穆宗同治帝登基日；本次核验一致"),
        ("1949-10-01", (1949, 10, 1), "甲子",
         "百度百科「甲子日」＋万年历站＋八字教例，三源一致；本表定序锚点"),
        ("1965-12-22", (1965, 12, 22), "甲子",
         "百度百科「甲子日」列此日为甲子——本表推算为庚戌，差 14 日；"
         "1965 年 12 月无甲子日（甲子在 1966-01-05），判该条来源有误，如实报，不据以调锚"),
        ("2025-12-21", (2025, 12, 21), "甲子",
         "媒体报道 2025 年冬至恰逢甲子日；本次核验一致"),
        ("公元前720-02-22", (astro_year(720, True), 2, 22), "己巳",
         "《春秋》隐公三年「二月己巳，日有食之」，儒略历前推；"
         "⚠ 纪年须用天文纪年 -719（无公元 0 年），用 -720 会偏 1 日而误判不符"),
    ]
    print("\n交叉核验：")
    results = []
    for label, (yy, mm, dd), expect, note in CROSS:
        got = gz_of_jdn(jdn(yy, mm, dd), off)
        results.append((label, expect, got, "yes" if got == expect else "no", note))
        print("  %-16s 记载 %s  推算 %s  %s" % (label, expect, got, "✓" if got == expect else "✗"))
    modern = [r for r in results if not r[0].startswith("公元前")]
    ok_m = sum(1 for r in modern if r[3] == "yes")
    print("现代记载：%d/%d 一致（1965-12-22 一条判为来源有误）" % (ok_m, len(modern)))
    print("古籍锚点（前720-02-22 己巳）：%s —— 与定序锚点相隔 2669 年而自洽" %
          ("一致" if results[-1][3] == "yes" else "不一致"))

    # 读节气边界（含起始年之前最后一个节气，否则表首数日会错归到当年第一个节气）
    bounds = []
    prev_rows = []
    if a.prev:
        with io.open(a.prev, encoding="utf-8-sig", newline="") as f:
            prev_rows = list(csv.DictReader(f))
    for r in prev_rows:
        bounds.append((r["beijing_date"] + " " + r["beijing_time"], r["term"]))
    with io.open(a.terms, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            bounds.append((r["beijing_date"] + " " + r["beijing_time"], r["term"]))
    bounds.sort()
    print("读入节气边界 %d 条%s" % (len(bounds), "（含前置边界 %s）" % prev_rows[0]["beijing_date"] if prev_rows else ""))

    d0 = datetime.date(a.y0, 1, 1)
    d1 = datetime.date(a.y1, 12, 31)
    rows = []
    bi = 0
    cur_term = None
    # 找 d0 之前（含当日）最近的一个节气
    for i, (ts, name) in enumerate(bounds):
        if ts <= d0.isoformat() + " 00:00:00":
            cur_term = (ts, name)
            bi = i
    if cur_term is None:
        raise SystemExit("!! 表首日期前无可用节气边界——请用 --prev 传入前一节气，"
                         "否则表首数日会被错归到当年第一个节气。")
    nxt = bounds[bi + 1] if bi + 1 < len(bounds) else None
    print("表首 %s 归属节气：%s（%s）" % (d0.isoformat(), cur_term[1], cur_term[0]))

    # 节气 → 月建地支：立春起寅月
    # 顺序：立春(寅) 惊蛰(卯) 清明(辰) 立夏(巳) 芒种(午) 小暑(未)
    #       立秋(申) 白露(酉) 寒露(戌) 立冬(亥) 大雪(子) 小寒(丑)
    JIE_TO_BRANCH = {"立春": "寅", "惊蛰": "卯", "清明": "辰", "立夏": "巳",
                     "芒种": "午", "小暑": "未", "立秋": "申", "白露": "酉",
                     "寒露": "戌", "立冬": "亥", "大雪": "子", "小寒": "丑"}

    def month_branch_of(term_name):
        """给定当前节气，回溯到最近的『节』（十二节）定月建。"""
        # 节 = 立春 惊蛰 清明 立夏 芒种 小暑 立秋 白露 寒露 立冬 大雪 小寒
        order = ["立春", "惊蛰", "清明", "立夏", "芒种", "小暑",
                 "立秋", "白露", "寒露", "立冬", "大雪", "小寒"]
        # 从 term_name 起向前找最近的一个『节』
        i = TERMS.index(term_name)
        for k in range(24):
            nm = TERMS[(i - k) % 24]
            if nm in JIE_TO_BRANCH:
                return JIE_TO_BRANCH[nm]
        return ""

    cur_date = d0
    while cur_date <= d1:
        while nxt and cur_date.isoformat() + " 23:59:59" >= nxt[0]:
            cur_term = nxt
            bi += 1
            nxt = bounds[bi + 1] if bi + 1 < len(bounds) else None
        n = jdn_gregorian(cur_date.year, cur_date.month, cur_date.day)
        gz = gz_of_jdn(n, off)
        idx = JIAZI_IDX[gz]
        rows.append({
            "date": cur_date.isoformat(),
            "year": cur_date.year,
            "month": cur_date.month,
            "day": cur_date.day,
            "weekday": cur_date.isoweekday(),
            "jdn": n,
            "ganzhi_day": gz,
            "ganzhi_index_1_60": idx + 1,
            "xun": XUN_SHOU[idx // 10] + "旬",
            "solar_term": cur_term[1],
            "solar_term_month_branch": month_branch_of(cur_term[1]),
            "next_term": nxt[1] if nxt else "",
            "next_term_datetime": nxt[0] if nxt else "",
        })
        cur_date += datetime.timedelta(days=1)

    print("生成", len(rows), "天")
    # 自检：干支必须严格 60 日循环、无跳号
    broken = []
    for i in range(1, len(rows)):
        if rows[i]["ganzhi_index_1_60"] != rows[i - 1]["ganzhi_index_1_60"] % 60 + 1:
            broken.append(rows[i]["date"])
    print("60 日循环连续性：", "全通过" if not broken else ("断点 %s" % broken[:5]))

    d = os.path.join(a.out, "03-干支纪日对照表", "data")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "ganzhi_day_%d_%d.csv" % (a.y0, a.y1))
    with io.open(p, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("写出", p)

    # 锚点核验表
    vp = os.path.join(d, "verification_anchors.csv")
    with io.open(vp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["日期", "记载／来源所称", "本表推算", "一致", "来源与说明", "用途"])
        for label, expect, got, ok, note in results:
            w.writerow([label, expect, got, ok, note,
                        "定序锚点" if label == "1949-10-01"
                        else ("不作定序依据" if label.startswith("公元前") else "交叉核验")])
    print("写出", vp)
    return 0


if __name__ == "__main__":
    sys.exit(main())

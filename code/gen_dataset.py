# -*- coding: utf-8 -*-
"""
gen_dataset.py — 把二十四节气交节时刻导出为「公共资产」数据集。

用途：战术 A（把历法做成公共资产）A1 件的生成器。不属于公众号写作流程，
      只服务于对外发布的数据集（Zenodo / GitHub）。

算法：太阳地心视黄经达 15° 整数倍的时刻（定气法，真春分点起算），
      与 GB/T 33661-2017《农历的编算和颁行》定义一致。

输出：
  <out>/01-二十四节气交节时刻/data/solar_terms_1900_2052.csv
  <out>/01-二十四节气交节时刻/data/solar_terms_1900_2052.json
  <out>/01-二十四节气交节时刻/data/verification_2026_vs_zijinshan.csv

星历边界：de421 覆盖 1899-07-28 至 2053-10-08。故年份上界取 2052（其冬至 12 月仍在内）。
"""
import argparse
import csv
import datetime
import io
import json
import os
import sys
import warnings

warnings.filterwarnings("ignore")

TERMS = ["小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
         "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
         "小暑", "大暑", "立秋", "处暑", "白露", "秋分",
         "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"]
TERM_LON = {n: (285 + 15 * i) % 360 for i, n in enumerate(TERMS)}
TERM_INDEX = {n: i + 1 for i, n in enumerate(TERMS)}

# 紫金山天文台《二〇二六年日历资料》官方值（北京时间），仅用于校核
OFFICIAL_2026 = {
    "小寒": "2026-01-05 16:23", "大寒": "2026-01-20 09:45",
    "立春": "2026-02-04 04:02", "雨水": "2026-02-18 23:52",
    "惊蛰": "2026-03-05 21:59", "春分": "2026-03-20 22:46",
    "清明": "2026-04-05 02:40", "谷雨": "2026-04-20 09:39",
    "立夏": "2026-05-05 19:49", "小满": "2026-05-21 08:37",
    "芒种": "2026-06-05 23:48", "夏至": "2026-06-21 16:25",
    "小暑": "2026-07-07 09:57", "大暑": "2026-07-23 03:13",
    "立秋": "2026-08-07 19:43", "处暑": "2026-08-23 10:19",
    "白露": "2026-09-07 22:41", "秋分": "2026-09-23 08:05",
    "寒露": "2026-10-08 14:29", "霜降": "2026-10-23 17:38",
    "立冬": "2026-11-07 17:52", "小雪": "2026-11-22 15:23",
    "大雪": "2026-12-07 10:53", "冬至": "2026-12-22 04:50",
}


def load_eph():
    from skyfield.api import Loader
    from skyfield_data import get_skyfield_data_path
    load = Loader(get_skyfield_data_path())
    ts = load.timescale()
    eph = load("de421.bsp")
    return ts, eph


def solar_longitude(ts, eph, t):
    earth, sun = eph["earth"], eph["sun"]
    _, lon, _ = earth.at(t).observe(sun).apparent().ecliptic_latlon(epoch="date")
    return lon.degrees % 360.0


def find_term(ts, eph, year, name, tz_hours=8.0):
    target = TERM_LON[name]
    month = TERMS.index(name) // 2 + 1
    lo = ts.utc(year, month, 1)
    hi = ts.utc(year, month + 1, 1) if month < 12 else ts.utc(year, 12, 25)
    for _ in range(40):
        mid = ts.tt_jd((lo.tt + hi.tt) / 2.0)
        diff = (solar_longitude(ts, eph, mid) - target + 180) % 360 - 180
        if diff < 0:
            lo = mid
        else:
            hi = mid
    t = ts.tt_jd((lo.tt + hi.tt) / 2.0)
    utc_dt = t.utc_datetime()
    bj_dt = utc_dt + datetime.timedelta(hours=tz_hours)
    return utc_dt, bj_dt, t.tt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="y0", type=int, default=1900)
    ap.add_argument("--to", dest="y1", type=int, default=2052)
    ap.add_argument("--out", required=True)
    ap.add_argument("--prev-out", help="额外写一行「起始年之前最后一个节气」（用于下游联结取到边界）")
    a = ap.parse_args()

    ts, eph = load_eph()
    # 实测星历可用边界（de421 官方文档记载 1899-07-28 — 2053-10-08）
    def _ok(y, m, d):
        try:
            solar_longitude(ts, eph, ts.utc(y, m, d, 12))
            return True
        except Exception:
            return False
    print("星历边界实测：1899-07-28 → %s｜2053-10-08 → %s｜2053-12-31 → %s" %
          (_ok(1899, 7, 28), _ok(2053, 10, 8), _ok(2053, 12, 31)))
    if a.y1 > 2052:
        print("!! 上界超 2052，可能越过 de421 边界（2053-10-08）", file=sys.stderr)

    rows = []
    for y in range(a.y0, a.y1 + 1):
        for name in TERMS:
            utc_dt, bj_dt, jd = find_term(ts, eph, y, name)
            rows.append({
                "year": y,
                "term_index": TERM_INDEX[name],
                "term": name,
                "solar_longitude_deg": TERM_LON[name],
                "beijing_date": bj_dt.strftime("%Y-%m-%d"),
                "beijing_time": bj_dt.strftime("%H:%M:%S"),
                "utc_date": utc_dt.strftime("%Y-%m-%d"),
                "utc_time": utc_dt.strftime("%H:%M:%S"),
                "jd_utc": round(jd, 6),
            })
        if (y - a.y0) % 20 == 0:
            print("  ... %d 完成（累计 %d 条）" % (y, len(rows)))

    # 一致性自检：每年 24 条；同年内时刻严格递增
    from collections import Counter
    cnt = Counter(r["year"] for r in rows)
    bad = {k: v for k, v in cnt.items() if v != 24}
    print("一致性：每年 24 条 →", "全通过" if not bad else ("异常 %s" % bad))
    inv = []
    for y in range(a.y0, a.y1 + 1):
        sub = [r for r in rows if r["year"] == y]
        keys = [r["beijing_date"] + " " + r["beijing_time"] for r in sub]
        if keys != sorted(keys):
            inv.append(y)
    print("单调性：同年内交节时刻递增 →", "全通过" if not inv else ("异常 %s" % inv))

    d1 = os.path.join(a.out, "01-二十四节气交节时刻", "data")
    os.makedirs(d1, exist_ok=True)

    csv_path = os.path.join(d1, "solar_terms_%d_%d.csv" % (a.y0, a.y1))
    cols = ["year", "term_index", "term", "solar_longitude_deg",
            "beijing_date", "beijing_time", "utc_date", "utc_time", "jd_utc"]
    with io.open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("写出", csv_path, len(rows), "条")

    json_path = os.path.join(d1, "solar_terms_%d_%d.json" % (a.y0, a.y1))
    meta = {
        "title": "二十四节气交节时刻数据集（1900—2052）",
        "title_en": "Solar Term Instants of the 24 Jieqi (1900-2052), Beijing Time",
        "definition": "GB/T 33661-2017《农历的编算和颁行》——二十四节气为太阳地心视黄经达 15° 整数倍的时刻",
        "time_scale": "beijing_* 为北京时间 UTC+08:00；utc_* 为协调世界时 UTC",
        "ephemeris": "JPL DE421 (NASA/JPL, public domain)",
        "software": "Skyfield (MIT)",
        "precision_note": "自算值显示到秒；与紫金山天文台《二〇二六年日历资料》24 个官方值比较，最大偏差 30 秒、平均 11.4 秒，四舍五入到分钟后 24/24 一致。官方历书为准。",
        "range_note": "上界 2052 系 JPL DE421 星历边界（覆盖至 2053-10-08）所致。",
        "license": "CC BY 4.0",
        "record_count": len(rows),
        "records": rows,
    }
    with io.open(json_path, "w", encoding="utf-8", newline="") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print("写出", json_path)

    # 校核表（仅当 2026 在本批范围内）
    if not (a.y0 <= 2026 <= a.y1):
        print("本次范围不含 2026，跳过与紫台官方值的校核")
    else:
        vpath = os.path.join(d1, "verification_2026_vs_zijinshan.csv")
        vrows = []
        devs = []
        for name in TERMS:
            r = [x for x in rows if x["year"] == 2026 and x["term"] == name][0]
            comp = r["beijing_date"] + " " + r["beijing_time"]
            off = OFFICIAL_2026[name] + ":00"
            d = (datetime.datetime.strptime(comp, "%Y-%m-%d %H:%M:%S")
                 - datetime.datetime.strptime(off, "%Y-%m-%d %H:%M:%S")).total_seconds()
            devs.append(abs(d))
            rm = datetime.datetime.strptime(comp, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(seconds=30)
            vrows.append({
                "term": name,
                "official_zijinshan_2026": OFFICIAL_2026[name],
                "computed": comp[:16],
                "diff_seconds": int(d),
                "match_after_rounding_to_minute": "yes" if rm.strftime("%Y-%m-%d %H:%M") == OFFICIAL_2026[name] else "no",
            })
        with io.open(vpath, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(vrows[0].keys()))
            w.writeheader()
            w.writerows(vrows)
        ok = sum(1 for v in vrows if v["match_after_rounding_to_minute"] == "yes")
        print("写出", vpath)
        print("校核：最大偏差 %.1f 秒｜平均 %.1f 秒｜四舍五入到分钟一致 %d/24" %
              (max(devs), sum(devs) / len(devs), ok))

    # 起始年之前最后一个节气（冬至）：下游（如干支表）联结时取到正确边界所需。
    # 注意：星历自 1899-07-28 起，故只能补算上一年冬至（12 月），补不出整年。
    if a.prev_out:
        utc_dt, bj_dt, jd = find_term(ts, eph, a.y0 - 1, "冬至")
        with io.open(a.prev_out, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.writer(f)
            w.writerow(["year", "term_index", "term", "solar_longitude_deg",
                        "beijing_date", "beijing_time", "utc_date", "utc_time", "jd_utc"])
            w.writerow([a.y0 - 1, 24, "冬至", 270,
                        bj_dt.strftime("%Y-%m-%d"), bj_dt.strftime("%H:%M:%S"),
                        utc_dt.strftime("%Y-%m-%d"), utc_dt.strftime("%H:%M:%S"), round(jd, 6)])
        print("写出", a.prev_out, "（%d 年冬至，用于下游边界）" % (a.y0 - 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())

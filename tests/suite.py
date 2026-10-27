import json, sys, importlib.util, pathlib
from playwright.sync_api import sync_playwright
Q = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("corpus", Q / "corpus.py"); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
URL = "file://" + str(Q.parent / "index.html")
fails, report = [], []
with sync_playwright() as p:
    b = p.chromium.launch()
    for vw in [(390, 844), (1280, 900)]:
        pg = b.new_page(viewport={"width": vw[0], "height": vw[1]})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(URL); pg.wait_for_timeout(300)
        for lang in ["ar", "en"]:
            if lang == "en": pg.click("#langBtn")
            for post in c.POSTS:
                pg.fill("#post", post["text"]); pg.click("#analyze")
                ov = pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
                if ov > 0: fails.append(f"{post['name']}: page overflows by {ov}px at {vw[0]}px/{lang}")
                # rate everything to exercise the result + plan rendering
                pg.evaluate("document.querySelectorAll('.item').forEach((li,i)=>li.querySelectorAll('.seg button')[i%3].click())")
                if pg.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth") > 0:
                    fails.append(f"{post['name']}: overflow after rating at {vw[0]}px/{lang}")
        if errs: fails.append(f"JS errors at {vw[0]}px: {errs[:3]}")
        pg.close()
    pg = b.new_page(); pg.goto(URL); pg.wait_for_timeout(300)
    for post in c.POSTS:
        d = pg.evaluate("t=>{const r=detect(t);return {items:r.items.map(i=>[i.label,i.prio,i.src]),unmapped:r.unmapped.map(u=>u.line),years:r.years}}", post["text"])
        got = {l: pr for l, pr, _ in d["items"]}
        bad = []
        for l in post["req"]:
            if l not in got: bad.append(f"missing required '{l}'")
            elif got[l] != "req": bad.append(f"'{l}' should be required, got nice-to-have")
        for l in post["pref"]:
            if l not in got: bad.append(f"missing nice-to-have '{l}'")
            elif got[l] != "pref": bad.append(f"'{l}' should be nice-to-have, got required")
        for l in post["absent"]:
            if l in got: bad.append(f"false positive '{l}' (from: {[s for x,_,s in d['items'] if x==l][0][:70]})")
        if d["years"] != post["years"]: bad.append(f"years {d['years']} != expected {post['years']}")
        if len(d["unmapped"]) > post["max_unmapped"]: bad.append(f"{len(d['unmapped'])} unmapped > {post['max_unmapped']}: {d['unmapped'][:4]}")
        tech = [l for l, pr, _ in d["items"]]
        if bad: fails.extend(f"{post['name']}: {x}" for x in bad)
        report.append((post["name"], len(d["items"]), len(d["unmapped"]), d["years"], "FAIL" if bad else "ok"))
    # scope warning
    for post in c.POSTS:
        if "scope" in post:
            pg.fill("#post", post["text"]); pg.click("#analyze")
            w = pg.eval_on_selector_all("#unmapped .msg.warn", "e=>e.length") > 0
            if w != post["scope"]: fails.append(f"{post['name']}: scope warning {w} != {post['scope']}")
    b.close()
for r in report: print(f"{r[4]:4} {r[0]:22} skills={r[1]:2} unmapped={r[2]} years={r[3]}")
print(f"\n{len(c.POSTS)} posts, {sum(1 for r in report if r[4]=='ok')} pass on detection; {len(fails)} total issues")
for f in fails: print(" -", f)

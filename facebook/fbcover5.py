import sys
sys.path.insert(0, '.')
from render import data_uri, font_faces, RED
from playwright.sync_api import sync_playwright
from PIL import Image
P = "/home/claude/securitycam/src/assets/responsive/"
W, H = 1640, 924
GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
MASK = "linear-gradient(to right,#000 0%,#000 38%,rgba(0,0,0,.8) 52%,rgba(0,0,0,.45) 68%,rgba(0,0,0,.15) 84%,transparent 100%)"
LOGO = data_uri('assets/logo-ondark.png')
BASE = f"""{font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:Heebo,sans-serif;color:#fff;background:#06132a;position:relative}}
.grain{{position:absolute;inset:0;background-image:url("{GRAIN}");opacity:.05;mix-blend-mode:overlay}}
.logo{{display:block;filter:brightness(1.16) drop-shadow(0 14px 34px rgba(0,0,0,.5))}}
.rule{{display:flex;align-items:center;gap:16px;width:100%}}
.rule i{{flex:1;height:1px;background:linear-gradient(to left,transparent,rgba(255,255,255,.42))}} .rule i:last-child{{background:linear-gradient(to right,transparent,rgba(255,255,255,.42))}}
.rule b{{width:8px;height:8px;background:{RED};transform:rotate(45deg);box-shadow:0 0 14px rgba(227,11,23,.7)}}
.tag{{font-size:40px;font-weight:300;line-height:1.4;color:#e9eef6}} .tag strong{{font-weight:700;color:#fff}} .tag .r{{font-weight:700;color:{RED}}}
.est{{direction:ltr;font-size:17px;font-weight:500;letter-spacing:7px;color:rgba(214,224,240,.62);text-transform:uppercase}}
"""

def photo_layout(img, pos, grade, pw=1180):
    return f"""<style>{BASE}
.bg{{position:absolute;inset:0;background:radial-gradient(70% 90% at 76% 48%,#163a74 0%,#0c2249 38%,#06132a 100%)}}
.photo{{position:absolute;left:0;top:0;width:{pw}px;height:100%;-webkit-mask-image:{MASK}}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:{pos};filter:{grade}}}
.tone{{position:absolute;left:0;top:0;width:{pw}px;height:100%;-webkit-mask-image:{MASK};background:linear-gradient(180deg,rgba(10,34,78,.6),rgba(10,34,78,.12) 42%,rgba(6,19,42,.65));mix-blend-mode:multiply}}
.light{{position:absolute;right:140px;top:140px;width:880px;height:640px;background:radial-gradient(closest-side,rgba(130,175,255,.11),transparent)}}
.frame{{position:absolute;inset:34px;border:1px solid rgba(255,255,255,.10)}}
.text{{position:absolute;right:250px;top:50%;transform:translateY(-50%);width:600px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.text .logo{{width:500px}} .text .rule{{margin:34px 0 28px}} .text .est{{margin-top:30px}}
</style><div class="bg"></div><div class="light"></div>
<div class="photo"><img src="{data_uri(P+img)}"></div><div class="tone"></div><div class="frame"></div>
<div class="text"><img class="logo" src="{LOGO}"><div class="rule"><i></i><b></b><i></i></div>
<div class="tag"><strong>אבטחה חכמה.</strong> תשתית מדויקת.<br><span class="r">שקט שנשאר.</span></div>
<div class="est">Est. 2014 · Security Systems</div></div><div class="grain"></div>"""

MONO = f"""<style>{BASE}
.bg{{position:absolute;inset:0;background:radial-gradient(90% 120% at 50% 0%,#17407f 0%,#0d2650 38%,#071530 78%,#050f22 100%)}}
.sweep{{position:absolute;left:-10%;top:-40%;width:120%;height:90%;background:radial-gradient(closest-side,rgba(255,255,255,.07),transparent);transform:rotate(-6deg)}}
.mark{{position:absolute;left:-120px;top:-140px;width:900px;height:1200px;opacity:.045}}
.mark2{{position:absolute;right:-160px;bottom:-260px;width:700px;height:900px;opacity:.05}}
.lines{{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.025) 0 1px,transparent 1px 120px)}}
.center{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:1100px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.center .logo{{width:640px}} .center .rule{{width:520px;margin:40px 0 30px}} .center .est{{margin-top:32px}}
.base{{position:absolute;left:50%;bottom:0;transform:translateX(-50%);width:420px;height:4px;background:linear-gradient(90deg,transparent,{RED},transparent)}}
</style><div class="bg"></div><div class="lines"></div><div class="sweep"></div>
<svg class="mark" viewBox="0 0 100 130"><path d="M10 120 L62 8 L92 8 L40 120 Z" fill="{RED}"/></svg>
<svg class="mark2" viewBox="0 0 100 130"><path d="M50 10 L95 120 L5 120 Z" fill="none" stroke="#fff" stroke-width="1.2"/></svg>
<div class="center"><img class="logo" src="{LOGO}"><div class="rule"><i></i><b></b><i></i></div>
<div class="tag" style="white-space:nowrap"><strong>אבטחה חכמה.</strong> תשתית מדויקת. <span class="r">שקט שנשאר.</span></div>
<div class="est">Est. 2014 · Holon · Security Systems</div></div><div class="base"></div><div class="grain"></div>"""

OPTIONS = {
    "A-architectural": photo_layout("entrance-864.webp", "center 42%", "grayscale(.12) contrast(1.1) brightness(.84) saturate(.9)"),
    "B-monolith": MONO,
    "C-residential": photo_layout("domeWall-864.webp", "center 38%", "grayscale(.1) contrast(1.08) brightness(.86) saturate(.85)", 860),
}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": W, "height": H})
    for name, body in OPTIONS.items():
        pg.set_content(f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"></head><body>{body}</body></html>', wait_until="load")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=f"out/cover-{name}.jpg", type="jpeg", quality=95)
    b.close()
ims = [Image.open(f"out/cover-{n}.jpg").resize((820, 462)) for n in OPTIONS]
sheet = Image.new("RGB", (820, 462*3 + 40), "white")
for i, im in enumerate(ims): sheet.paste(im, (0, i*(462+20)))
sheet.save("out/cover-options.jpg", quality=88)

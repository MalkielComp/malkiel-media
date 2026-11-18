import sys
sys.path.insert(0, '.')
from render import data_uri, font_faces, RED
from playwright.sync_api import sync_playwright
from PIL import Image
P = "/home/claude/securitycam/src/assets/responsive/"
W, H = 1640, 924
GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .55 0'/></filter>"
         "<rect width='100%' height='100%' filter='url(%23n)'/></svg>")
MASK = "linear-gradient(to right,#000 0%,#000 38%,rgba(0,0,0,.8) 52%,rgba(0,0,0,.45) 68%,rgba(0,0,0,.15) 84%,transparent 100%)"
html = f"""<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>{font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:Heebo,sans-serif;color:#fff;background:#06132a;position:relative}}
.bg{{position:absolute;inset:0;background:radial-gradient(70% 90% at 76% 48%,#163a74 0%,#0c2249 38%,#06132a 100%)}}
.photo{{position:absolute;left:0;top:0;width:1180px;height:100%;-webkit-mask-image:{MASK}}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:center 42%;filter:grayscale(.15) contrast(1.08) brightness(.86) saturate(.9)}}
.tone{{position:absolute;left:0;top:0;width:1180px;height:100%;-webkit-mask-image:{MASK};
  background:linear-gradient(180deg,rgba(10,34,78,.55),rgba(10,34,78,.15) 40%,rgba(6,19,42,.6));mix-blend-mode:multiply}}
.light{{position:absolute;right:120px;top:120px;width:900px;height:680px;background:radial-gradient(closest-side,rgba(120,170,255,.10),transparent);}}
.text{{position:absolute;right:250px;top:50%;transform:translateY(-50%);width:600px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.logo{{width:520px;display:block;filter:brightness(1.15) drop-shadow(0 14px 34px rgba(0,0,0,.45))}}
.rule{{display:flex;align-items:center;gap:16px;margin:38px 0 30px;width:100%}}
.rule i{{flex:1;height:1px;background:linear-gradient(to left,transparent,rgba(255,255,255,.45))}} .rule i:last-child{{background:linear-gradient(to right,transparent,rgba(255,255,255,.45))}}
.rule b{{width:8px;height:8px;background:{RED};transform:rotate(45deg)}}
.tag{{font-size:46px;font-weight:300;line-height:1.35;color:#eef2f8}}
.tag strong{{font-weight:700;color:#fff}} .tag .r{{font-weight:700;color:{RED}}}
.grain{{position:absolute;inset:0;background-image:url("{GRAIN}");opacity:.05;mix-blend-mode:overlay}}
</style></head><body>
<div class="bg"></div><div class="light"></div>
<div class="photo"><img src="{data_uri(P+'entrance-864.webp')}"></div><div class="tone"></div>
<div class="text">
 <img class="logo" src="{data_uri('assets/logo-ondark.png')}">
 <div class="rule"><i></i><b></b><i></i></div>
 <div class="tag"><strong>אבטחה חכמה.</strong> תשתית מדויקת.<br><span class="r">שקט שנשאר.</span></div>
</div>
<div class="grain"></div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.set_content(html, wait_until="load"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    pg.screenshot(path="out/facebook-cover-v4.jpg", type="jpeg", quality=95)
    b.close()
im = Image.open("out/facebook-cover-v4.jpg")
dh = int(W/2.7); desk = im.crop((0,(H-dh)//2,W,(H+dh)//2))
can = Image.new("RGB",(W, desk.height+20+H),"white"); can.paste(desk,(0,0)); can.paste(im,(0,desk.height+20))
can.resize((W//2,(desk.height+20+H)//2)).save("out/facebook-cover-v4-preview.jpg",quality=85)

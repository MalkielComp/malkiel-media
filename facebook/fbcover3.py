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
br = lambda pos: f'<i class="br {pos}"></i>'
html = f"""<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>{font_faces()}
*{{box-sizing:border-box;margin:0;padding:0}} html,body{{width:{W}px;height:{H}px;overflow:hidden}}
body{{font-family:Heebo,sans-serif;color:#fff;background:#071630;position:relative}}
.bg{{position:absolute;inset:0;background:
  radial-gradient(60% 70% at 78% 45%,rgba(227,11,23,.10),transparent 60%),
  radial-gradient(90% 120% at 90% 20%,#14346b 0%,#0b2045 42%,#06132a 100%)}}
.grid{{position:absolute;right:0;top:0;width:900px;height:100%;opacity:.07;
  background-image:linear-gradient(#fff 1px,transparent 1px),linear-gradient(90deg,#fff 1px,transparent 1px);background-size:56px 56px;
  -webkit-mask-image:radial-gradient(70% 70% at 60% 50%,#000,transparent 75%)}}
.photo{{position:absolute;left:0;top:0;width:1060px;height:100%;
  -webkit-mask-image:linear-gradient(to right,#000 0%,#000 44%,rgba(0,0,0,.5) 70%,transparent 94%)}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:center 58%;filter:contrast(1.12) saturate(1.18) brightness(.78)}}
.grade{{position:absolute;left:0;top:0;width:1060px;height:100%;-webkit-mask-image:linear-gradient(to right,#000 0%,#000 44%,rgba(0,0,0,.5) 70%,transparent 94%);background:linear-gradient(180deg,rgba(8,28,64,.55),rgba(8,28,64,.05) 35%,rgba(8,28,64,.05) 65%,rgba(5,16,36,.7));mix-blend-mode:multiply}}
.bloom{{position:absolute;left:330px;top:300px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(255,40,50,.20),transparent 65%);filter:blur(10px)}}
.vf{{position:absolute;left:120px;top:212px;width:540px;height:500px}}
.br{{position:absolute;width:46px;height:46px;border-color:rgba(255,255,255,.85);border-style:solid;border-width:0}}
.br.tl{{left:0;top:0;border-left-width:3px;border-top-width:3px}} .br.tr{{right:0;top:0;border-right-width:3px;border-top-width:3px}}
.br.bl{{left:0;bottom:0;border-left-width:3px;border-bottom-width:3px}} .br.brr{{right:0;bottom:0;border-right-width:3px;border-bottom-width:3px}}
.hud{{position:absolute;left:26px;top:22px;display:flex;gap:18px;align-items:center;direction:ltr;font-size:20px;font-weight:700;letter-spacing:2px;color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.6)}}
.hud b{{display:flex;align-items:center;gap:8px;color:#fff}} .hud b:before{{content:"";width:12px;height:12px;border-radius:50%;background:{RED};box-shadow:0 0 12px {RED}}}
.hud span{{opacity:.8;font-weight:500}}
.ts{{position:absolute;right:26px;top:22px;direction:ltr;font-size:20px;letter-spacing:2px;opacity:.8;font-weight:500}}
.cross{{position:absolute;left:50%;top:50%;width:34px;height:34px;margin:-17px 0 0 -17px;opacity:.55}}
.cross:before,.cross:after{{content:"";position:absolute;background:#fff}} .cross:before{{left:16px;top:0;width:2px;height:34px}} .cross:after{{top:16px;left:0;height:2px;width:34px}}
.text{{position:absolute;right:225px;top:50%;transform:translateY(-50%);width:660px;display:flex;flex-direction:column;align-items:flex-start;gap:0}}
.eyebrow{{font-size:22px;font-weight:700;letter-spacing:.5px;color:#ff4d55;margin-bottom:20px}}
.logo{{width:380px;display:block;filter:brightness(1.14) drop-shadow(0 10px 28px rgba(0,0,0,.45))}}
.rule{{width:100%;height:1px;background:linear-gradient(270deg,rgba(255,255,255,.5),rgba(255,255,255,0));margin:22px 0 20px}}
h1{{font-weight:900;font-size:58px;line-height:1.06;letter-spacing:-1.2px}}
h1 .r{{color:{RED};text-shadow:0 0 30px rgba(227,11,23,.35)}}
.proof{{display:flex;gap:0;margin-top:24px}}
.proof div{{padding:0 22px;border-left:1px solid rgba(255,255,255,.25);display:flex;flex-direction:column;gap:2px}}
.proof div:first-child{{padding-right:0}} .proof div:last-child{{border-left:0}}
.proof b{{font-size:30px;font-weight:900;line-height:1.1}} .proof span{{font-size:19px;color:#b9c6dc;font-weight:500}}
.contact{{margin-top:22px;display:flex;align-items:center;gap:14px;font-size:30px;font-weight:800}}
.contact span{{direction:ltr;letter-spacing:.5px}} .contact em{{font-style:normal;font-weight:500;color:#b9c6dc;font-size:24px}}
.ph{{width:44px;height:44px;border-radius:50%;background:{RED};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 7px rgba(227,11,23,.18)}}
.grain{{position:absolute;inset:0;background-image:url("{GRAIN}");opacity:.06;mix-blend-mode:overlay;pointer-events:none}}
</style></head><body>
<div class="bg"></div><div class="grid"></div>
<div class="photo"><img src="{data_uri(P+'network-rack-new-864.webp')}"></div><div class="grade"></div><div class="bloom"></div>
<div class="vf">{br('tl')}{br('tr')}{br('bl')}{br('brr')}
  <div class="hud"><b>REC</b><span>CAM-01 · 4K</span></div><div class="ts">MALKIEL TECH</div><div class="cross"></div></div>
<div class="text">
 <div class="eyebrow">מערכות אבטחה ותשתיות · חולון והמרכז</div>
 <img class="logo" src="{data_uri('assets/logo-ondark.png')}">
 <div class="rule"></div>
 <h1>אבטחה חכמה.<br>תשתית מדויקת.<br><span class="r">שקט שנשאר.</span></h1>
 <div class="proof">
  <div><b dir="ltr" style="text-align:right">10+</b><span>שנות ניסיון בשטח</span></div>
  <div><b>מאז 2014</b><span>תכנון · התקנה · שירות</span></div>
  <div><b>ללא עלות</b><span>סקר ראשוני בשטח</span></div>
 </div>
 <div class="contact"><div class="ph"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg></div><span>050-3380803</span></div>
</div>
<div class="grain"></div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.set_content(html, wait_until="load"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    pg.screenshot(path="out/facebook-cover-v3.jpg", type="jpeg", quality=95)
    b.close()
im = Image.open("out/facebook-cover-v3.jpg")
dh = int(W/2.7); desk = im.crop((0,(H-dh)//2,W,(H+dh)//2))
can = Image.new("RGB",(W, desk.height+20+H),"white"); can.paste(desk,(0,0)); can.paste(im,(0,desk.height+20))
can.resize((W//2,(desk.height+20+H)//2)).save("out/facebook-cover-v3-preview.jpg",quality=85)

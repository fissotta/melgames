"""Regenera las portadas (covers/*.jpg) con capturas de la pantalla de título de cada juego.

Uso:  python3 tools/capturar_portadas.py /ruta/a/carpeta/con/los/repos
      (la carpeta debe contener acidgear/, colonization/, copahue-field-campaign/ y nicho/)
Requiere: pip install playwright pillow && playwright install chromium
"""
import sys, threading, functools, http.server, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

root = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(__file__).resolve().parent.parent / 'covers'
GAMES = {'colonization': 4000, 'nicho': 4000, 'acidgear': 4000, 'copahue-field-campaign': 9000}
# en Copahue se ocultan los paneles para que se vea el mundo
HIDE = {'copahue-field-campaign': '#g-ov,#g-mis,#g-map,#g-stat,#g-top{display:none!important}'}

srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8765), functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root)))
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(args=['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'])
    for g, wait in GAMES.items():
        pg = b.new_page(viewport={'width': 1280, 'height': 720})
        pg.goto(f'http://127.0.0.1:8765/{g}/'); pg.wait_for_timeout(wait)
        if g in HIDE: pg.add_style_tag(content=HIDE[g]); pg.wait_for_timeout(1200)
        tmp = out / f'{g}.png'; pg.screenshot(path=str(tmp)); pg.close()
        Image.open(tmp).convert('RGB').resize((960, 540), Image.LANCZOS).save(out / f'{g}.jpg', quality=82); tmp.unlink()
        print('ok', g)
    b.close()
srv.shutdown()

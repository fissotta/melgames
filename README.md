# MEL Games

Portada de los juegos del **Microbial Ecophysiology Lab** (Fundación Ciencia & Vida).
Sitio: https://fissotta.github.io/melgames/

| Juego | Link |
|---|---|
| COLONIZATION | https://fissotta.github.io/colonization/ |
| NICHO | https://fissotta.github.io/nicho/ |
| Copahue Field Campaign | https://fissotta.github.io/copahue-field-campaign/ |
| ACID GEAR | https://fissotta.github.io/acidgear/ |

## Cómo funciona
- Una sola página (`index.html`), HTML + JS puro, sin dependencias ni build.
- **Versión en vivo:** al abrir (y cada 60 s) la página lee el sitio publicado de cada juego y saca la versión
  del `<title>` (o de `js/main.js` en ACID GEAR). También mira el último commit en la API de GitHub:
  - punto verde = lo publicado está al día;
  - punto amarillo + "↻ publicando…" = hay un commit más nuevo que GitHub Pages todavía no publica;
  - "NUEVA" = la versión cambió desde la última vez que abriste la portada.
  Para que la versión se lea bien, mantén `vX.Y` en el `<title>` de cada juego y en el mensaje del commit.
- Fondo: manchas de colores del logo + comunidades bacterianas (bacilos, cocos, cadenas, espirilos) que nadan,
  se dividen y escapan del cursor.
- Música: ambient house suave generada en el navegador (Web Audio). Parte con el primer clic; botón arriba a la derecha.

## Agregar un juego
Añade una entrada en `GAMES` dentro de `index.html` y su portada en `covers/<id>.jpg` (960×540).
Para regenerar las portadas: `python3 tools/capturar_portadas.py /carpeta/con/los/repos`.

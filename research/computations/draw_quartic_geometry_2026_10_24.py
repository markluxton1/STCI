#!/usr/bin/env python3
"""Reproduce the static quartic geometry figures (SVG, with optional PNG).

The SVG writer uses only the Python standard library.  The same scene is
rasterized with Pillow when it is installed.  No external image assets or
network calls are used.  The projection figure is explicitly schematic;
the conic figure samples the exact real equations in the displayed chart.

Run from any directory:
    python3 research/computations/draw_quartic_geometry_2026_10_24.py

To reproduce both formats in the bundled desktop runtime:
    /Users/markluxton/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \\
        research/computations/draw_quartic_geometry_2026_10_24.py
"""

from __future__ import annotations

from html import escape
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "figures" / "quartic-geometry-2026-10-24"
INK = "#183043"
MUTED = "#526777"
BLUE = "#156eae"
TEAL = "#087f75"
GOLD = "#ae6d12"
RED = "#af4252"
PALE = "#f4f8fb"
GRID = "#dfe8ef"
WHITE = "#ffffff"


class Scene:
    """One small vector scene, with identical SVG and Pillow geometry."""

    def __init__(self, width=1500, height=900):
        self.width, self.height = width, height
        self.elements = []

    def rect(self, x, y, w, h, fill=WHITE, stroke=GRID, width=1.5, radius=16):
        self.elements.append(("rect", (x, y, w, h, fill, stroke, width, radius)))

    def line(self, points, stroke=INK, width=2, dash=False):
        self.elements.append(("line", (points, stroke, width, dash)))

    def circle(self, x, y, r=6, fill=INK, stroke=None, width=1.5):
        self.elements.append(("circle", (x, y, r, fill, stroke, width)))

    def text(self, x, y, text, size=25, fill=INK, bold=False, anchor="start"):
        # y is the typographic baseline, as in SVG.
        self.elements.append(("text", (x, y, text, size, fill, bold, anchor)))

    def arrow(self, x1, y1, x2, y2, stroke=INK, width=3):
        self.line([(x1, y1), (x2, y2)], stroke, width)
        angle = math.atan2(y2-y1, x2-x1)
        head = 11
        pts = [(x2-head*math.cos(angle-0.45), y2-head*math.sin(angle-0.45)),
               (x2, y2),
               (x2-head*math.cos(angle+0.45), y2-head*math.sin(angle+0.45))]
        self.line(pts, stroke, width)

    def save(self, name):
        OUT.mkdir(parents=True, exist_ok=True)
        svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">',
               '<style>text{font-family:"Arial Unicode MS",Arial,sans-serif}</style>',
               f'<rect width="100%" height="100%" fill="{WHITE}"/>']
        for typ, args in self.elements:
            if typ == "rect":
                x,y,w,h,fill,stroke,width,radius = args
                svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
            elif typ == "line":
                points,stroke,width,dash = args
                ps = " ".join(f"{x:.3f},{y:.3f}" for x,y in points)
                da = ' stroke-dasharray="8 7"' if dash else ""
                svg.append(f'<polyline points="{ps}" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{da}/>')
            elif typ == "circle":
                x,y,r,fill,stroke,width = args
                svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke or fill}" stroke-width="{width}"/>')
            else:
                x,y,txt,size,fill,bold,anchor = args
                svg.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{700 if bold else 400}" text-anchor="{anchor}">{escape(txt)}</text>')
        svg.append('</svg>')
        (OUT / f"{name}.svg").write_text("\n".join(svg)+"\n")
        try:
            from PIL import Image, ImageDraw, ImageFont
        except ImportError:
            print(f"Wrote {name}.svg; Pillow unavailable, so PNG skipped.")
            return
        scale = 2
        img = Image.new("RGB", (self.width*scale, self.height*scale), WHITE)
        draw = ImageDraw.Draw(img)
        fonts = {}
        regular_candidates = [
            "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
        bold_candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
        def font(size, bold):
            key = size, bold
            if key not in fonts:
                candidates = bold_candidates if bold else regular_candidates
                path = next((p for p in candidates if Path(p).exists()), None)
                fonts[key] = ImageFont.truetype(path, round(size*scale)) if path else ImageFont.load_default(size=round(size*scale))
            return fonts[key]
        for typ,args in self.elements:
            if typ == "rect":
                x,y,w,h,fill,stroke,width,radius = args
                draw.rounded_rectangle((x*scale,y*scale,(x+w)*scale,(y+h)*scale), radius*scale, fill, stroke, max(1,round(width*scale)))
            elif typ == "circle":
                x,y,r,fill,stroke,width = args
                draw.ellipse(((x-r)*scale,(y-r)*scale,(x+r)*scale,(y+r)*scale), fill, stroke or fill, max(1,round(width*scale)))
            elif typ == "line":
                points,stroke,width,dash = args
                if not dash:
                    draw.line([(round(x*scale),round(y*scale)) for x,y in points], fill=stroke, width=max(1,round(width*scale)), joint="curve")
                else:
                    # All dashed elements in these figures are straight lines.
                    for (x1,y1),(x2,y2) in zip(points,points[1:]):
                        length = math.hypot(x2-x1,y2-y1)
                        if not length:
                            continue
                        pos = 0
                        while pos < length:
                            end=min(pos+8,length)
                            ps=[((x1+(x2-x1)*q/length)*scale,(y1+(y2-y1)*q/length)*scale) for q in (pos,end)]
                            draw.line(ps,fill=stroke,width=max(1,round(width*scale)))
                            pos+=15
            else:
                x,y,txt,size,fill,bold,anchor=args
                f=font(size,bold)
                pil_anchor={"start":"ls","middle":"ms","end":"rs"}[anchor]
                draw.text((x*scale,y*scale),txt,font=f,fill=fill,anchor=pil_anchor)
        img.resize((self.width,self.height),Image.Resampling.LANCZOS).save(OUT/f"{name}.png")
        print(f"Wrote {name}.svg and {name}.png")


def projection_figure():
    s=Scene()
    s.text(60,65,"One projection center organizes the quartic",37,bold=True)
    s.text(60,108,"Structural diagram: incidences and maps are exact; the spatial drawing is schematic.",24,MUTED)
    s.rect(60,145,600,505,PALE)
    s.rect(840,145,600,505,PALE)
    s.text(90,192,"Complete embedding",28,bold=True)
    s.text(90,232,"C₄ ⊂ P(W∨) ≅ P⁴",27,BLUE)
    s.text(870,192,"Projected embedding",28,bold=True)
    s.text(870,232,"C ⊂ Q ⊂ P(V∨) ≅ P³",27,TEAL)
    # A stylized normal curve, deliberately not a false affine model in P4.
    source=[]
    for i in range(241):
        t=i/240
        source.append((145+430*t,350-95*math.sin(math.pi*t)))
    s.line(source,BLUE,5)
    s.circle(145,350,7,BLUE);s.circle(575,350,7,BLUE)
    s.text(121,390,"p₀",25,BLUE);s.text(561,390,"p∞",25,BLUE)
    s.text(351,291,"C₄",26,BLUE)
    # Incidence links mean the osculating planes contain both endpoint/center.
    s.line([(145,350),(360,455),(575,350)],GOLD,2.5,True)
    s.circle(360,455,8,GOLD)
    s.text(384,465,"z",30,GOLD,bold=True)
    s.text(95,530,"z = Osc²(p₀) ∩ Osc²(p∞)",26,GOLD)
    s.text(95,578,"z lies outside the secant variety σ₂(C₄).",23,MUTED)
    s.arrow(690,350,810,350,INK,3)
    s.text(750,322,"π_z",31,INK,anchor="middle")
    s.text(750,393,"isomorphism",20,MUTED,anchor="middle")
    # A Segre coordinate patch, with graph of t -> t^3.
    x0,x1,y0,y1=925,1355,285,510
    for k in range(6):
        x=x0+(x1-x0)*k/5
        y=y0+(y1-y0)*k/5
        s.line([(x,y0),(x,y1)],GRID,1.5)
        s.line([(x0,y),(x1,y)],GRID,1.5)
    curve=[]
    for i in range(241):
        t=i/240
        # A schematic affine segment of the graph of the cubic ruling map.
        curve.append((x0+(x1-x0)*t,y1-(y1-y0)*t**3))
    s.line(curve,TEAL,5)
    s.circle(x0,y1,7,TEAL);s.circle(x1,y0,7,TEAL)
    s.text(891,548,"p₀",25,TEAL);s.text(1340,274,"p∞",25,TEAL)
    s.text(1158,550,"C: graph of [s:t] ↦ [s³:t³]",19,TEAL,anchor="middle")
    s.text(883,592,"The cubic ruling map has two ramification points.",23,MUTED)
    s.rect(60,690,1380,150,WHITE,GRID)
    s.text(90,735,"0 → kz → W∨ → V∨ → 0",28,INK)
    s.text(90,785,"Dual binary type (2,2):  z ↔ s²t²",25,GOLD)
    s.text(800,735,"{p₀,p∞}  ⇔  z  ⇔  V",28,INK)
    s.text(800,785,"Stabilizer N(T) = G_m ⋊ Z/2",25,TEAL)
    s.text(60,878,"Characteristic zero.  The center is a point of P(W∨); the target is P(V∨).",21,MUTED)
    s.save("projection-center")


def conics_figure():
    s=Scene()
    s.text(60,65,"The diagonal and bitangent conics",37,bold=True)
    s.text(60,108,"Real slice of the chart α + γ = 1 in Sym²(C) ≅ P²; x = α − γ and y = β.",24,MUTED)
    # Equal x/y units preserve the visible tangency geometry.
    cx,cy,unit=540,462,190
    def p(x,y):return cx+unit*x,cy-unit*y
    xmin,xmax,ymin,ymax=-2.3,2.3,-1.42,1.42
    for x in (-2,-1,0,1,2):
        s.line([p(x,ymin),p(x,ymax)],GRID,1.2)
    for y in (-1,-0.5,0,0.5,1):
        s.line([p(xmin,y),p(xmax,y)],GRID,1.2)
    s.arrow(*p(xmin,0),*p(xmax,0),MUTED,1.6)
    s.arrow(*p(0,ymin),*p(0,ymax),MUTED,1.6)
    s.text(*p(2.28,-0.13),"x",23,MUTED)
    s.text(*p(0.09,1.35),"y",23,MUTED)
    for x in (-2,-1,1,2):
        xx,yy=p(x,-0.17)
        s.text(xx,yy,str(x),19,MUTED,anchor="middle")
    for y in (-1,1):
        xx,yy=p(-0.13,y)
        s.text(xx,yy+6,str(y),19,MUTED,anchor="end")
    for x in (-1,1):
        s.line([p(x,ymin),p(x,ymax)],GOLD,2,True)
    d=[p(math.cos(2*math.pi*i/720),math.sin(2*math.pi*i/720)) for i in range(721)]
    s.line(d,BLUE,4.5)
    for sign in (-1,1):
        b=[]
        for i in range(501):
            y=ymin+(ymax-ymin)*i/500
            b.append(p(sign*math.sqrt(1+2*y*y),y))
        s.line(b,TEAL,4.5)
    for x in (-1,1):s.circle(*p(x,0),7,RED,WHITE,2)
    xx,yy=p(-1,-0.32);s.text(xx,yy,"2p₀",23,RED,anchor="middle")
    xx,yy=p(1,-0.32);s.text(xx,yy,"2p∞",23,RED,anchor="middle")
    s.rect(1030,155,410,555,PALE)
    s.line([(1060,204),(1110,204)],BLUE,4.5)
    s.text(1130,212,"Diagonal Δ",25,BLUE,bold=True)
    s.text(1060,256,"β² − 4αγ = 0",26,BLUE)
    s.text(1060,299,"x² + y² = 1",25,BLUE)
    s.line([(1060,351),(1110,351)],TEAL,4.5)
    s.text(1130,359,"Bitangent B",25,TEAL,bold=True)
    s.text(1060,403,"β² + 2αγ = 0",26,TEAL)
    s.text(1060,446,"x² − 2y² = 1",25,TEAL)
    s.line([(1060,500),(1110,500)],GOLD,2,True)
    s.text(1130,508,"Common tangents",23,GOLD)
    s.text(1060,552,"x = −1  and  x = 1",24,GOLD)
    s.text(1060,610,"Each intersection has length 2.",22,INK)
    s.text(1060,650,"Δ ∩ B =",22,RED)
    s.text(1090,686,"2[2p₀] + 2[2p∞]",23,RED)
    s.rect(60,758,1380,87,WHITE,GRID)
    s.text(90,795,"Intrinsic relative form:  D⁻¹B has eigenvalues 1, −1/2, −1/2;  trace = 0.",25,INK)
    s.text(90,828,"Together with torus invariance this selects B and forces ρ + ρ⁻¹ = −4.",23,MUTED)
    s.text(60,879,"The real picture illustrates two algebraic conics; the proofs concern an algebraically closed field of characteristic zero.",20,MUTED)
    s.save("symmetric-square-conics")


if __name__ == "__main__":
    projection_figure()
    conics_figure()

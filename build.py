"""chopon.ai static site builder.

content/ai/*.md  ->  public/darsliklar/ai/<slug>.html  (served as /darsliklar/ai/<slug>)
Run:  python build.py
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content" / "ai"
OUT = ROOT / "public"
SITE = "chopon.ai"

FONTS = ("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800"
         "&family=Unbounded:wght@500;600;700;800&display=swap")


# ------------------------------------------------------------------ markup
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def slugify(s):
    s = s.lower().replace("‘", "").replace("’", "").replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def pairs(lines):
    """key: value lines -> list of (key, value)."""
    out = []
    for l in lines:
        if ":" in l:
            k, v = l.split(":", 1)
            out.append((k.strip().lower(), v.strip()))
        elif out:
            out[-1] = (out[-1][0], out[-1][1] + " " + l.strip())
    return out


def block_meme(kind, lines):
    d = dict(pairs(lines))
    cap = f'<figcaption>{inline(d["caption"])}</figcaption>' if "caption" in d else ""
    if kind == "drake":
        body = (f'<div class="mrow no"><div class="memoji" aria-hidden="true">{d.get("e1", "🙅‍♂️")}</div>'
                f'<p>{inline(d["no"])}</p></div>'
                f'<div class="mrow yes"><div class="memoji" aria-hidden="true">{d.get("e2", "😎👉")}</div>'
                f'<p>{inline(d["yes"])}</p></div>')
    elif kind == "expect":
        body = ('<div class="panels">'
                f'<div class="panel"><span class="lbl">Kutilgan</span><div class="pe" aria-hidden="true">{d.get("e1", "✨")}</div>'
                f'<p>{inline(d["expect"])}</p></div>'
                f'<div class="panel real"><span class="lbl">Haqiqat</span><div class="pe" aria-hidden="true">{d.get("e2", "🫠")}</div>'
                f'<p>{inline(d["reality"])}</p></div></div>')
    elif kind == "classic":
        body = (f'<div class="classic"><p class="top">{inline(d["top"])}</p>'
                f'<div class="ce" aria-hidden="true">{d.get("emoji", "🤖")}</div>'
                f'<p class="bottom">{inline(d["bottom"])}</p></div>')
    elif kind == "brain":
        rows = [(k, v) for k, v in pairs(lines) if k.startswith("l")]
        body = "".join(f'<div class="brow b{i}"><p>{inline(v)}</p><div class="be" aria-hidden="true">{"🧠" if i < 3 else "🌌🧠"}</div></div>'
                       for i, (_, v) in enumerate(rows))
    else:
        raise ValueError(kind)
    return f'<figure class="meme meme-{kind}"><span class="meme-tag">MEM</span>{body}{cap}</figure>'


def block_chat(lines):
    title, msgs = "", []
    for k, v in pairs(lines):
        if k == "title":
            title = f'<p class="t">{inline(v)}</p>'
        elif k in ("user", "ai", "note"):
            who = {"user": "Siz", "ai": "AI", "note": ""}[k]
            w = f'<span class="who">{who}</span>' if who else ""
            msgs.append(f'<div class="msg {k}">{w}{inline(v)}</div>')
        elif k in ("left", "right"):  # custom speaker: "left: Ona | matn"
            who, _, txt = v.partition("|")
            cls = "ai" if k == "left" else "user"
            msgs.append(f'<div class="msg {cls}"><span class="who">{inline(who.strip())}</span>{inline(txt.strip())}</div>')
    return f'<div class="chat">{title}{"".join(msgs)}</div>'


def block_quiz(lines):
    items, q = [], None
    for k, v in pairs(lines):
        if k == "q":
            q = v
        elif k == "a" and q:
            items.append(f'<details><summary>{inline(q)}</summary><p>{inline(v)}</p></details>')
            q = None
    return f'<section class="quiz"><h2 id="sinov">O‘zingizni sinang</h2>{"".join(items)}</section>'


def block_box(kind, lines):
    title = {"tip": "💡 Maslahat", "warn": "⚠️ Ehtiyot bo‘ling", "fact": "🧐 Qiziq fakt"}[kind]
    paras = "".join(f"<p>{inline(p)}</p>" for p in "\n".join(lines).split("\n\n") if p.strip())
    return f'<aside class="box box-{kind}"><strong class="bt">{title}</strong>{paras}</aside>'


def block_prompt(arg, lines):
    label = inline(arg) if arg else "Prompt"
    txt = html.escape("\n".join(lines).strip())
    return (f'<div class="prompt"><div class="prompt-head"><span>{label}</span>'
            f'<button type="button" class="copy">Nusxa olish</button></div><pre>{txt}</pre></div>')


def render_body(text):
    out, toc = [], []
    lines = text.split("\n")
    i, para, lst = 0, [], None

    def flush():
        nonlocal para, lst
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []
        if lst:
            tag, items = lst
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            lst = None

    while i < len(lines):
        l = lines[i].rstrip()
        if l.startswith(":::"):
            flush()
            head = l[3:].strip().split(None, 1)
            kind, arg = head[0], (head[1] if len(head) > 1 else "")
            buf = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                buf.append(lines[i])
                i += 1
            if kind == "meme":
                out.append(block_meme(arg, buf))
            elif kind == "chat":
                out.append(block_chat(buf))
            elif kind == "quiz":
                out.append(block_quiz(buf))
                toc.append(("sinov", "O‘zingizni sinang"))
            elif kind == "prompt":
                out.append(block_prompt(arg, buf))
            else:
                out.append(block_box(kind, buf))
        elif l.startswith("## "):
            flush()
            t = l[3:].strip()
            sid = slugify(t)
            toc.append((sid, t))
            out.append(f'<h2 id="{sid}">{inline(t)}</h2>')
        elif l.startswith("### "):
            flush()
            out.append(f"<h3>{inline(l[4:].strip())}</h3>")
        elif l.startswith("> "):
            flush()
            out.append(f"<blockquote>{inline(l[2:])}</blockquote>")
        elif re.match(r"^(- |\d+\. )", l):
            if para:
                out.append(f"<p>{inline(' '.join(para))}</p>")
                para = []
            tag = "ul" if l.startswith("- ") else "ol"
            item = re.sub(r"^(- |\d+\. )", "", l)
            if lst and lst[0] == tag:
                lst[1].append(item)
            else:
                flush()
                lst = (tag, [item])
        elif not l.strip():
            flush()
        elif lst and l.startswith("  "):
            lst[1][-1] += " " + l.strip()
        else:
            if lst:
                flush()
            para.append(l.strip())
        i += 1
    flush()
    return "\n".join(out), toc


def parse_lesson(path):
    raw = path.read_text("utf8")
    _, fm, body = raw.split("---", 2)
    meta = {}
    for l in fm.strip().split("\n"):
        k, v = l.split(":", 1)
        meta[k.strip()] = v.strip()
    meta["html"], meta["toc"] = render_body(body)
    return meta


# ------------------------------------------------------------------ templates
def page(title, desc, body, depth, active="", body_class=""):
    p = "/"  # absolute paths: site lives at the domain root
    nav = [("Bosh sahifa", "home", "home"), ("Darsliklar", "darsliklar", "lessons"),
           ("Biz haqimizda", "home#biz-haqimizda", "about")]
    links = "".join(f'<a href="{p}{href}"{" class=\"active\"" if key == active else ""}>{name}</a>'
                    for name, href, key in nav)
    full_title = f"{title} — {SITE}" if title != SITE else "chopon.ai — AI’ni dehqonchasiga o‘rganamiz"
    return f"""<!doctype html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="{p}assets/img/logo-512.png">
<meta name="theme-color" content="#022391">
<link rel="icon" href="{p}assets/img/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{p}assets/img/tab-icon-32.png">
<link rel="icon" type="image/png" sizes="64x64" href="{p}assets/img/tab-icon-64.png">
<link rel="apple-touch-icon" href="{p}assets/img/tab-icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{p}assets/css/style.css">
</head>
<body class="{body_class}">
<a class="skip" href="#main">Asosiy matnga o‘tish</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/home"><img src="{p}assets/img/logo-160.png" alt="" width="44" height="44"><span>chopon<b>.ai</b></span></a>
    <nav aria-label="Asosiy menyu">{links}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="f-brand"><img src="{p}assets/img/logo-160.png" alt="chopon.ai logotipi" width="72" height="72">
      <div><strong>chopon<b>.ai</b></strong><span>Chopon egnimizda, AI qo‘limizda</span></div></div>
    <p class="f-note">Sun’iy intellektni o‘zbek tilida, oddiy va qiziqarli tushuntiramiz.</p>
    <p class="f-copy">© 2026 chopon.ai</p>
  </div>
</footer>
<script src="{p}assets/js/site.js" defer></script>
</body>
</html>
"""


def toc_rows(lessons, prefix, limit=None):
    rows = []
    for l in lessons[:limit]:
        rows.append(f"""<li><a class="toc-row" href="/darsliklar/ai/{l['slug']}" data-tags="{html.escape(l['tag'])}">
  <span class="num">{l['id']}</span>
  <span class="ttl">{html.escape(l['title'])}<small>{html.escape(l['lead'])}</small></span>
  <span class="meta"><span class="chip">{html.escape(l['tag'])}</span><span class="time">{l['time']} daqiqa</span></span>
</a></li>""")
    return f'<ol class="toc">{"".join(rows)}</ol>'


def build_home(lessons):
    body = f"""
<section class="hero ikat">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Chopon egnimizda, AI qo‘limizda</p>
      <h1>Sun’iy intellektni <span class="hl">dehqonchasiga</span> tushuntiramiz.</h1>
      <p class="hero-lead">Murakkab atamalarsiz, hazil va memlar bilan. Har bir mavzu ikki qavatli:
      avval bir og‘iz qisqa izoh, keyin istaganingizcha chuqur tushuntirish.</p>
      <div class="cta">
        <a class="btn btn-yellow" href="/darsliklar/ai/{lessons[0]['slug']}">Birinchi darsni boshlash</a>
        <a class="btn btn-ghost" href="/darsliklar/ai">Barcha mavzular</a>
      </div>
    </div>
    <div class="hero-badge"><img src="assets/img/logo-512.png" alt="chopon.ai logotipi: chopon va elektron sxema" width="420" height="420"></div>
  </div>
</section>

<section class="layers wrap" aria-labelledby="layers-h">
  <h2 id="layers-h" class="sec-title">Har bir dars uch qavatdan iborat</h2>
  <div class="layer-grid">
    <article class="layer"><span class="layer-n">1</span><h3>Dehqonchasiga</h3><p>Mavzuning mag‘zi bir nechta oddiy gapda. Shoshayotgan bo‘lsangiz, shuning o‘zi kifoya.</p></article>
    <article class="layer"><span class="layer-n">2</span><h3>Chuqur tushuntirish</h3><p>Qanday ishlaydi, nega shunday, qayerda qo‘llanadi. Real misollar va tayyor promptlar bilan.</p></article>
    <article class="layer"><span class="layer-n">3</span><h3>Mem va hazil</h3><p>AI bilan bog‘liq hazillar va kulgili misollar. Kulib o‘rganilgan narsa esdan chiqmaydi.</p></article>
  </div>
</section>

<section class="wrap home-list" aria-labelledby="new-h">
  <div class="sec-head"><h2 id="new-h" class="sec-title">AI darsliklar</h2>
  <a class="more" href="/darsliklar/ai">Hammasi ({len(lessons)}) →</a></div>
  {toc_rows(lessons, "darsliklar/ai/", 6)}
</section>

<section id="biz-haqimizda" class="about">
  <div class="wrap about-grid">
    <h2 class="sec-title light">Biz haqimizda</h2>
    <div>
      <p><strong>chopon.ai</strong> o‘zbek tilida AI haqida eng tushunarli manba bo‘lishni maqsad qilgan loyiha.
      Chopon bizning ildizimiz, AI esa kelajak vositamiz. Ikkalasini birlashtirib, texnologiyani har bir xonadonga
      olib kirmoqchimiz.</p>
      <p>Darsliklar yoshlar, talabalar, o‘qituvchilar va kichik biznes egalari uchun yozilgan. Hech qanday
      dasturlash bilimi talab qilinmaydi.</p>
    </div>
  </div>
</section>
"""
    html_ = page(SITE, "Sun’iy intellekt haqida o‘zbek tilida oddiy, qiziqarli va memlar bilan yozilgan darsliklar.", body, 0, "home", "home")
    (OUT / "index.html").write_text(html_, "utf8")  # choponai.uz/
    (OUT / "home.html").write_text(html_, "utf8")   # choponai.uz/home


def build_lessons_hub(lessons):
    body = f"""
<section class="page-hero ikat">
  <div class="wrap">
    <nav class="crumbs" aria-label="Yo‘l"><a href="/home">Bosh sahifa</a><span>/</span><span>Darsliklar</span></nav>
    <h1>Darsliklar</h1>
    <p class="lead">Bo‘limni tanlang. Hozircha birinchi bo‘lim ochiq, qolganlari tikilmoqda.</p>
  </div>
</section>
<section class="wrap hub">
  <a class="patch" href="/darsliklar/ai">
    <span class="patch-k">Bo‘lim 01</span>
    <h2>AI darsliklar</h2>
    <p>Sun’iy intellekt asoslari, promptlar, xavfsizlik, ish va biznes. Matnli, memli, dehqonchasiga.</p>
    <span class="patch-f">{len(lessons)} ta mavzu →</span>
  </a>
  <div class="patch soon" aria-disabled="true">
    <span class="patch-k">Bo‘lim 02</span><h2>Prompt kutubxonasi</h2>
    <p>Har xil vazifalar uchun tayyor o‘zbekcha promptlar.</p><span class="patch-f">Tez orada</span>
  </div>
  <div class="patch soon" aria-disabled="true">
    <span class="patch-k">Bo‘lim 03</span><h2>AI vositalar</h2>
    <p>Qaysi ish uchun qaysi AI qulay: qisqa va halol sharhlar.</p><span class="patch-f">Tez orada</span>
  </div>
</section>
"""
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "darsliklar.html").write_text(page("Darsliklar", "chopon.ai darsliklari: AI darsliklar va boshqa bo‘limlar.", body, 1, "lessons"), "utf8")


def build_ai_index(lessons):
    tags = sorted({l["tag"] for l in lessons})
    chips = "".join(f'<button type="button" class="filter" data-tag="{html.escape(t)}">{html.escape(t)}</button>' for t in tags)
    body = f"""
<section class="page-hero ikat">
  <div class="wrap">
    <nav class="crumbs" aria-label="Yo‘l"><a href="/home">Bosh sahifa</a><span>/</span><a href="/darsliklar">Darsliklar</a><span>/</span><span>AI darsliklar</span></nav>
    <h1>AI darsliklar</h1>
    <p class="lead">{len(lessons)} ta mavzu. Tartib bilan o‘qisangiz, noldan boshlab AI bilan bemalol ishlaydigan bo‘lasiz.
    Har bir darsda avval qisqa izoh, keyin chuqur tushuntirish va, albatta, memlar bor.</p>
  </div>
</section>
<section class="wrap list-page">
  <div class="tools">
    <label class="search"><span class="sr">Mavzu qidirish</span><input type="search" id="q" placeholder="Mavzu qidirish: prompt, xavfsizlik, rasm…"></label>
    <div class="filters" role="group" aria-label="Turkum bo‘yicha saralash"><button type="button" class="filter on" data-tag="">Hammasi</button>{chips}</div>
  </div>
  {toc_rows(lessons, "")}
  <p class="empty" hidden>Hech narsa topilmadi. Boshqa so‘z bilan qidirib ko‘ring 🤷‍♂️</p>
</section>
"""
    d = OUT / "darsliklar"
    d.mkdir(parents=True, exist_ok=True)
    (d / "ai.html").write_text(page("AI darsliklar", "Sun’iy intellekt bo‘yicha o‘zbek tilidagi matnli darsliklar ro‘yxati.", body, 2, "lessons"), "utf8")


def build_lesson(l, prev, nxt):
    side = "".join(f'<li><a href="#{sid}">{html.escape(t)}</a></li>' for sid, t in l["toc"])

    def card(x, label, cls):
        if not x:
            return "<span></span>"
        return (f'<a class="pn {cls}" href="/darsliklar/ai/{x["slug"]}"><span>{label}</span>'
                f'<strong>{x["id"]}. {html.escape(x["title"])}</strong></a>')

    body = f"""
<div class="progress" aria-hidden="true"><span></span></div>
<article class="lesson">
  <header class="lesson-hero ikat">
    <div class="wrap">
      <nav class="crumbs" aria-label="Yo‘l"><a href="/home">Bosh sahifa</a><span>/</span><a href="/darsliklar">Darsliklar</a><span>/</span><a href="/darsliklar/ai">AI darsliklar</a></nav>
      <span class="lesson-num" aria-hidden="true">{l['id']}</span>
      <h1>{html.escape(l['title'])}</h1>
      <p class="lead">{html.escape(l['lead'])}</p>
      <p class="meta-row"><span>⏱ {l['time']} daqiqa</span><span>🎯 {html.escape(l['level'])}</span><span>🏷 {html.escape(l['tag'])}</span></p>
    </div>
  </header>
  <div class="wrap">
    <section class="dehqon" aria-labelledby="dq">
      <h2 id="dq">🧑‍🌾 Dehqonchasiga aytganda</h2>
      <p>{inline(l['dehqoncha'])}</p>
    </section>
    <div class="layout">
      <aside class="side"><div class="side-in"><p class="side-t">Mundarija</p><ol>{side}</ol></div></aside>
      <div class="prose">
{l['html']}
        <nav class="prevnext" aria-label="Boshqa darslar">{card(prev, "← Oldingi dars", "prev")}{card(nxt, "Keyingi dars →", "next")}</nav>
      </div>
    </div>
  </div>
</article>
"""
    d = OUT / "darsliklar" / "ai"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{l['slug']}.html").write_text(page(l["title"], l["lead"], body, 3, "lessons", "lesson-page"), "utf8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / "CNAME").write_text("choponai.uz\n")  # GitHub Pages custom domain
    (OUT / ".nojekyll").write_text("")
    shutil.copy(ROOT / "assets" / "img" / "favicon.ico", OUT / "favicon.ico")  # browsers also request /favicon.ico
    lessons = sorted((parse_lesson(p) for p in CONTENT.glob("*.md")), key=lambda x: x["id"])
    build_home(lessons)
    build_lessons_hub(lessons)
    build_ai_index(lessons)
    for i, l in enumerate(lessons):
        build_lesson(l, lessons[i - 1] if i else None, lessons[i + 1] if i + 1 < len(lessons) else None)
    print(f"built {len(lessons)} lessons -> {OUT}")


if __name__ == "__main__":
    main()

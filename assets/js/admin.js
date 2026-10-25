// chopon.ai — statistics page (/salohiddin, not linked anywhere). Reads visits from Firestore.
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getFirestore, collection, query, where, orderBy, getDocs, Timestamp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const $ = (s) => document.querySelector(s);
const cfg = window.CHOPON_FIREBASE || {};
const show = (id) => ["#a-setup", "#a-dash"].forEach((s) => ($(s).hidden = s !== id));

if (!cfg.apiKey) {
  show("#a-setup");
} else {
  const db = getFirestore(initializeApp(cfg));
  let days = 7;
  show("#a-dash");
  load();

  $("#a-reload").addEventListener("click", () => load());
  document.querySelectorAll(".rng").forEach((b) => b.addEventListener("click", () => {
    document.querySelectorAll(".rng").forEach((x) => x.classList.remove("on"));
    b.classList.add("on"); days = +b.dataset.d; load();
  }));

  async function load() {
    $("#a-status").textContent = "Yuklanmoqda…";
    const since = new Date(); since.setHours(0, 0, 0, 0); since.setDate(since.getDate() - (days - 1));
    try {
      const snap = await getDocs(query(collection(db, "visits"), where("ts", ">=", Timestamp.fromDate(since)), orderBy("ts")));
      const rows = snap.docs.map((d) => ({ ...d.data(), ts: d.data().ts.toDate() }));
      render(rows, since);
      $("#a-status").textContent = "Yangilandi: " + new Date().toLocaleTimeString("uz-UZ", { hour: "2-digit", minute: "2-digit" });
    } catch (ex) {
      $("#a-status").textContent = "Xatolik: " + ex.message;
    }
  }
}

const fmt = (sec) => {
  sec = Math.round(sec || 0);
  const m = Math.floor(sec / 60), s = sec % 60;
  return m ? `${m} daq ${String(s).padStart(2, "0")} s` : `${s} s`;
};
const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const dayKey = (d) => d.toISOString().slice(0, 10);

function render(rows, since) {
  const visitors = new Set(rows.map((r) => r.visitor));
  const sessions = new Map();
  rows.forEach((r) => sessions.set(r.session, (sessions.get(r.session) || 0) + (r.duration || 0)));
  const timed = rows.filter((r) => r.duration > 0);
  const now = Date.now();
  const live = new Set(rows.filter((r) => now - r.ts.getTime() < 5 * 60 * 1000).map((r) => r.visitor));

  const kpi = [
    ["Tashrifchilar", visitors.size, "noyob odamlar"],
    ["Ko‘rishlar", rows.length, "ochilgan sahifalar"],
    ["O‘rtacha vaqt", fmt([...sessions.values()].reduce((a, b) => a + b, 0) / (sessions.size || 1)), "bir tashrifda saytda"],
    ["Sahifada o‘rtacha", fmt(timed.reduce((a, r) => a + r.duration, 0) / (timed.length || 1)), "bitta sahifani o‘qish"],
    ["Sessiyalar", sessions.size, "alohida tashriflar"],
    ["Hozir saytda", live.size, "so‘nggi 5 daqiqa"],
  ];
  $("#a-kpi").innerHTML = kpi.map(([t, v, s]) => `<div class="kpi"><span>${t}</span><strong>${v}</strong><small>${s}</small></div>`).join("");

  // daily visitors chart
  const byDay = new Map();
  for (let d = new Date(since); d <= new Date(); d.setDate(d.getDate() + 1)) byDay.set(dayKey(d), { v: new Set(), p: 0 });
  rows.forEach((r) => { const b = byDay.get(dayKey(r.ts)); if (b) { b.v.add(r.visitor); b.p++; } });
  const days = [...byDay.entries()];
  const max = Math.max(1, ...days.map(([, b]) => b.p));
  const W = 760, H = 220, pad = 28, bw = (W - pad * 2) / days.length;
  const bars = days.map(([k, b], i) => {
    const x = pad + i * bw, hp = (b.p / max) * (H - 60), hv = (b.v.size / max) * (H - 60);
    const lbl = days.length <= 31 && (days.length <= 10 || i % Math.ceil(days.length / 10) === 0)
      ? `<text x="${x + bw / 2}" y="${H - 6}" text-anchor="middle">${k.slice(8)}.${k.slice(5, 7)}</text>` : "";
    return `<g><title>${k}: ${b.v.size} tashrifchi, ${b.p} ko‘rish</title>
      <rect x="${x + bw * 0.12}" y="${H - 28 - hp}" width="${bw * 0.76}" height="${hp}" rx="4" class="bp"/>
      <rect x="${x + bw * 0.28}" y="${H - 28 - hv}" width="${bw * 0.44}" height="${hv}" rx="3" class="bv"/>${lbl}</g>`;
  }).join("");
  $("#a-chart").innerHTML = `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Kunlik statistika">
    <line x1="${pad}" x2="${W - pad}" y1="${H - 28}" y2="${H - 28}" class="axis"/>${bars}</svg>`;

  // top pages
  const pages = new Map();
  rows.forEach((r) => {
    const p = pages.get(r.path) || { title: r.title, n: 0, t: 0, c: 0 };
    p.n++; if (r.duration > 0) { p.t += r.duration; p.c++; }
    pages.set(r.path, p);
  });
  const top = [...pages.entries()].sort((a, b) => b[1].n - a[1].n).slice(0, 15);
  $("#a-pages").innerHTML = top.length ? top.map(([path, p]) => `<tr><td><strong>${esc(p.title.replace(/ — chopon\.ai$/, ""))}</strong><small>${esc(path)}</small></td>
    <td class="n">${p.n}</td><td class="n">${fmt(p.t / (p.c || 1))}</td></tr>`).join("") : `<tr><td colspan="3" class="empty-row">Hali ma’lumot yo‘q</td></tr>`;

  const share = (key, el, names) => {
    const m = new Map();
    rows.forEach((r) => m.set(r[key] || "", (m.get(r[key] || "") || 0) + 1));
    const list = [...m.entries()].sort((a, b) => b[1] - a[1]).slice(0, 8);
    $(el).innerHTML = list.length ? list.map(([k, n]) => {
      const pct = Math.round((n / rows.length) * 100);
      return `<li><span>${esc(names(k))}</span><b>${pct}%</b><i style="width:${pct}%"></i></li>`;
    }).join("") : `<li class="empty-row">Hali ma’lumot yo‘q</li>`;
  };
  share("device", "#a-dev", (k) => ({ mobile: "📱 Telefon", desktop: "💻 Kompyuter", tablet: "📟 Planshet" })[k] || k);
  share("ref", "#a-ref", (k) => k || "To‘g‘ridan-to‘g‘ri");
}

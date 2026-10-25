// chopon.ai — lightweight visit tracker.
// One Firestore document per page view (created on load), then its "duration"
// (seconds the tab was actually visible) is updated when the visitor leaves or hides the tab.
// Uses the Firestore REST API directly so no SDK is loaded for visitors.
(function () {
  var cfg = window.CHOPON_FIREBASE;
  if (!cfg || !cfg.apiKey || !cfg.projectId) return;
  if (/^(localhost|127\.0\.0\.1)$/.test(location.hostname)) return; // don't count local previews

  var base = "https://firestore.googleapis.com/v1/projects/" + cfg.projectId +
    "/databases/(default)/documents/visits";
  var rid = function () { return Math.random().toString(36).slice(2) + Date.now().toString(36); };
  var store = function (s, k) {
    try { var v = s.getItem(k); if (!v) { v = rid(); s.setItem(k, v); } return v; } catch (e) { return rid(); }
  };
  var visitor = store(localStorage, "cv_id");
  var session = store(sessionStorage, "cs_id");
  var docId = rid();

  var ref = "";
  try { var r = document.referrer && new URL(document.referrer); if (r && r.hostname !== location.hostname) ref = r.hostname; } catch (e) {}
  var device = /Mobi|Android|iPhone/i.test(navigator.userAgent) ? "mobile" : (/iPad|Tablet/i.test(navigator.userAgent) ? "tablet" : "desktop");
  var path = location.pathname.replace(/\.html$/, "").replace(/\/index$/, "/") || "/";
  if (path === "/") path = "/home";

  var s = function (v) { return { stringValue: String(v).slice(0, 150) }; };
  var body = { fields: {
    path: s(path), title: s(document.title), visitor: s(visitor), session: s(session),
    ref: s(ref), device: s(device), lang: s((navigator.language || "").slice(0, 10)),
    ts: { timestampValue: new Date().toISOString() }, duration: { integerValue: "0" }
  } };

  var created = fetch(base + "?documentId=" + docId + "&key=" + cfg.apiKey, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body)
  }).then(function (r) { return r.ok; }).catch(function () { return false; });

  var visibleMs = 0, since = document.visibilityState === "visible" ? Date.now() : 0, sent = -1;
  var flush = function () {
    if (since) { visibleMs += Date.now() - since; since = 0; }
    var sec = Math.min(14400, Math.round(visibleMs / 1000));
    if (sec <= sent) return;
    sent = sec;
    created.then(function (ok) {
      if (!ok) return;
      fetch(base + "/" + docId + "?updateMask.fieldPaths=duration&key=" + cfg.apiKey, {
        method: "PATCH", keepalive: true, headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ fields: { duration: { integerValue: String(sec) } } })
      }).catch(function () {});
    });
  };
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "visible") since = Date.now(); else flush();
  });
  addEventListener("pagehide", flush);
})();

// chopon.ai — small progressive enhancements (site works without JS)
(function () {
  // reading progress
  var bar = document.querySelector(".progress span");
  if (bar) {
    var onScroll = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + "%";
    };
    document.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // copy prompt buttons
  document.querySelectorAll(".prompt .copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.closest(".prompt").querySelector("pre").innerText;
      var done = function () {
        btn.textContent = "Nusxalandi ✓";
        btn.classList.add("done");
        setTimeout(function () { btn.textContent = "Nusxa olish"; btn.classList.remove("done"); }, 1800);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () {});
    });
  });

  // table of contents highlight
  var links = document.querySelectorAll(".side a");
  if (links.length && "IntersectionObserver" in window) {
    var map = {};
    links.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.remove("on"); });
          var a = map[e.target.id];
          if (a) a.classList.add("on");
        }
      });
    }, { rootMargin: "-20% 0px -70% 0px" });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }

  // lesson list: search + tag filter
  var q = document.getElementById("q");
  if (q) {
    var rows = Array.prototype.slice.call(document.querySelectorAll(".toc li"));
    var empty = document.querySelector(".empty");
    var tag = "";
    var norm = function (s) { return s.toLowerCase().replace(/[‘’ʻʼ']/g, ""); };
    var apply = function () {
      var term = norm(q.value.trim()), shown = 0;
      rows.forEach(function (li) {
        var a = li.querySelector("a");
        var ok = (!tag || a.dataset.tags === tag) && (!term || norm(a.textContent).indexOf(term) !== -1);
        li.hidden = !ok;
        if (ok) shown++;
      });
      empty.hidden = shown > 0;
    };
    q.addEventListener("input", apply);
    document.querySelectorAll(".filter").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".filter").forEach(function (x) { x.classList.remove("on"); });
        b.classList.add("on");
        tag = b.dataset.tag;
        apply();
      });
    });
  }
})();

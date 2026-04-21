import os

base = r"C:\Users\petrm\OneDrive\Dokumenty\Claude Code\Zefektivneni_v2"
files = [
    "index.html", "faze1.html", "faze2.html", "faze3.html",
    "analyza.html", "strategie.html", "realita.html", "souhrn.html", "dokumenty.html"
]

SCROLL_JS = """
<script>
/* SCROLL REVEAL */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var s = document.createElement('style');
  s.textContent =
    '.sr{opacity:0;transform:translateY(22px);' +
    'transition:opacity .58s cubic-bezier(.4,0,.2,1),transform .58s cubic-bezier(.4,0,.2,1)}' +
    '.sr.in{opacity:1;transform:translateY(0)}' +
    '.sr.d1{transition-delay:.09s}.sr.d2{transition-delay:.18s}' +
    '.sr.d3{transition-delay:.27s}.sr.d4{transition-delay:.36s}';
  document.head.appendChild(s);

  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
    });
  }, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });

  var vh = window.innerHeight;

  /* Register elements; stagger=true groups siblings by parent and adds d1-d4 delays */
  function reg(sel, stagger) {
    var els = Array.from(document.querySelectorAll(sel));
    if (stagger) {
      var map = new Map();
      els.forEach(function (el) {
        var p = el.parentElement;
        if (!map.has(p)) map.set(p, []);
        map.get(p).push(el);
      });
      map.forEach(function (grp) {
        grp.forEach(function (el, i) { if (i > 0 && i <= 4) el.dataset.srD = i; });
      });
    }
    els.forEach(function (el) {
      if (el.getBoundingClientRect().top >= vh - 40) {
        el.classList.add('sr');
        if (el.dataset.srD) el.classList.add('d' + el.dataset.srD);
        obs.observe(el);
      }
    });
  }

  /* Full-block reveals (whole sections slide in as a unit) */
  reg(
    '.section,' +
    '.arcade-section,.decision-section,.discussion-section,' +
    '.container-strip,.condition-banner,.risk-band,.callout,' +
    '.led-volume,.dual-use-block,.sfa-banner,.phase-nav,' +
    '#why-not-section,#pacht-banner,#souhrn-callout',
    false
  );

  /* Grid / flex children that stagger in relative to siblings */
  reg('.phase-card,.kpi-item,.hero-stat,.tl-phase,.doc-card', true);
}());
</script>
"""

for fname in files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'SCROLL REVEAL' in content:
        print(f"  skip (already has SR): {fname}")
        continue

    if '</body>' not in content:
        print(f"  WARNING: no </body> in {fname}")
        continue

    content = content.replace('</body>', SCROLL_JS + '</body>', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  done: {fname}")

print("\n=== Scroll reveal added to all pages ===")

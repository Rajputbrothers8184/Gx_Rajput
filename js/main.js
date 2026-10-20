/* ==========================================================================
   Gx_Rajput — portfolio interactions
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------ navigation ------------------------------ */
  var nav = document.getElementById("nav");
  var burger = document.getElementById("burger");
  var navLinks = document.getElementById("navLinks");
  var links = Array.prototype.slice.call(navLinks.querySelectorAll("a"));

  function onScroll() {
    nav.classList.toggle("scrolled", window.scrollY > 30);
    var top = document.getElementById("toTop");
    top.classList.toggle("show", window.scrollY > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  burger.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    burger.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  });

  links.forEach(function (a) {
    a.addEventListener("click", function () {
      nav.classList.remove("open");
      burger.classList.remove("open");
      burger.setAttribute("aria-expanded", "false");
    });
  });

  document.getElementById("toTop").addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* --------------------------- scroll spy --------------------------- */
  var sections = ["home", "about", "skills", "portfolio", "services", "contact"]
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);

  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      links.forEach(function (a) {
        a.classList.toggle("active", a.getAttribute("href") === "#" + e.target.id);
      });
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  sections.forEach(function (s) { spy.observe(s); });

  /* ------------------------------ reveal ------------------------------ */
  var revealIO = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach(function (el) { revealIO.observe(el); });

  /* ---------------------------- skill bars ---------------------------- */
  var barIO = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.style.width = (e.target.dataset.w || 0) + "%";
      obs.unobserve(e.target);
    });
  }, { threshold: 0.4 });
  document.querySelectorAll(".bar-fill").forEach(function (b, i) {
    b.style.transitionDelay = (i % 5) * 90 + "ms";
    barIO.observe(b);
  });

  /* ------------------------------ filters ------------------------------ */
  var cards = Array.prototype.slice.call(document.querySelectorAll("#grid .card"));
  var filters = document.getElementById("filters");

  filters.addEventListener("click", function (e) {
    var btn = e.target.closest(".filter");
    if (!btn) return;
    filters.querySelectorAll(".filter").forEach(function (b) { b.classList.remove("active"); });
    btn.classList.add("active");

    var f = btn.dataset.f;
    var shown = 0;
    cards.forEach(function (c) {
      var match = f === "all" || c.dataset.cat === f;
      c.classList.toggle("hide", !match);
      if (match) {
        shown++;
        // re-trigger the reveal animation for newly shown cards
        c.classList.remove("in");
        setTimeout(function () { c.classList.add("in"); }, 20 + shown * 12);
      }
    });
  });

  /* ----------------------------- lightbox ----------------------------- */
  var lb = document.getElementById("lightbox");
  var lbImg = document.getElementById("lbImg");
  var lbTitle = document.getElementById("lbTitle");
  var lbDesc = document.getElementById("lbDesc");
  var current = 0;

  function visibleCards() {
    return cards.filter(function (c) { return !c.classList.contains("hide"); });
  }

  function show(i) {
    var list = visibleCards();
    if (!list.length) return;
    current = (i + list.length) % list.length;
    var card = list[current];
    var img = card.querySelector("img");
    lbImg.src = img.getAttribute("src");
    lbImg.alt = img.getAttribute("alt") || "";
    lbTitle.textContent = card.querySelector("h3").textContent;
    lbDesc.textContent = card.querySelector("p").textContent + " — Gx_Rajput";
  }

  function openLb(card) {
    show(visibleCards().indexOf(card));
    lb.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function closeLb() {
    lb.classList.remove("open");
    document.body.style.overflow = "";
  }

  cards.forEach(function (card) {
    card.addEventListener("click", function () { openLb(card); });
  });

  document.getElementById("lbClose").addEventListener("click", closeLb);
  document.getElementById("lbPrev").addEventListener("click", function (e) { e.stopPropagation(); show(current - 1); });
  document.getElementById("lbNext").addEventListener("click", function (e) { e.stopPropagation(); show(current + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape") closeLb();
    if (e.key === "ArrowLeft") show(current - 1);
    if (e.key === "ArrowRight") show(current + 1);
  });

  /* --------------------------- contact form --------------------------- */
  var form = document.getElementById("contactForm");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = form.name.value.trim();
    var phone = form.phone.value.trim();
    var service = form.service.value;
    var msg = form.message.value.trim();

    var text =
      "Assalam-o-Alaikum Gx_Rajput!\n\n" +
      "Name: " + (name || "-") + "\n" +
      "Phone: " + (phone || "-") + "\n" +
      "Service: " + service + "\n" +
      "Details: " + (msg || "-") + "\n\n" +
      "(Sent from your portfolio website)";

    window.open("https://wa.me/923110682944?text=" + encodeURIComponent(text), "_blank", "noopener");
  });

  /* ------------------------------- misc ------------------------------- */
  document.getElementById("year").textContent = new Date().getFullYear();
})();

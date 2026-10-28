/* Gx_Rajput — navigation, gallery and contact interactions. */
(function () {
  "use strict";

  var nav = document.getElementById("nav");
  var burger = document.getElementById("burger");
  var navLinks = document.getElementById("navLinks");
  var links = Array.prototype.slice.call(navLinks.querySelectorAll("a"));
  var topButton = document.getElementById("toTop");

  function closeMenu() {
    nav.classList.remove("open");
    burger.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
  }

  function onScroll() {
    nav.classList.toggle("scrolled", window.scrollY > 30);
    topButton.classList.toggle("show", window.scrollY > 600);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  burger.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    burger.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", String(open));
  });
  links.forEach(function (link) { link.addEventListener("click", closeMenu); });
  document.addEventListener("click", function (event) {
    if (nav.classList.contains("open") && !nav.contains(event.target)) closeMenu();
  });
  topButton.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* Keep the existing data-w customization working, with inline widths as a no-JS fallback. */
  document.querySelectorAll(".bar-fill").forEach(function (bar) {
    var width = Number(bar.dataset.w);
    if (Number.isFinite(width)) bar.style.setProperty("--bar-width", Math.max(0, Math.min(100, width)) + "%");
  });

  /* Only hide content for reveal animations if the browser can observe it. */
  if ("IntersectionObserver" in window) {
    document.documentElement.classList.add("js");
    var sections = ["home", "portfolio", "about", "skills", "services", "contact"]
      .map(function (id) { return document.getElementById(id); });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (link) {
          link.classList.toggle("active", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    sections.forEach(function (section) { if (section) spy.observe(section); });

    var reveal = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: "0px 0px -5% 0px" });
    document.querySelectorAll(".reveal").forEach(function (item) { reveal.observe(item); });

    var bars = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("filled");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.4 });
    document.querySelectorAll(".bar-fill").forEach(function (bar, index) {
      bar.style.transitionDelay = (index % 5) * 70 + "ms";
      bars.observe(bar);
    });
  }

  /* One visible design per category; the all filter restores the complete set. */
  var grid = document.getElementById("grid");
  var cards = Array.prototype.slice.call(grid.querySelectorAll(".card"));
  var filters = document.getElementById("filters");
  var filterCount = document.getElementById("filterCount");
  filters.addEventListener("click", function (event) {
    var selected = event.target.closest(".filter");
    if (!selected || !filters.contains(selected)) return;
    filters.querySelectorAll(".filter").forEach(function (button) {
      var active = button === selected;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    var category = selected.dataset.f;
    var count = 0;
    cards.forEach(function (card) {
      var matches = category === "all" || card.dataset.cat === category;
      card.hidden = !matches;
      if (matches) {
        count += 1;
        card.classList.add("in");
      }
    });
    grid.classList.toggle("filtered", category !== "all");
    filterCount.textContent = "SHOWING " + String(count).padStart(2, "0") + " / " + String(cards.length).padStart(2, "0");
  });

  /* Full-size previews, keyboard navigation and focus return. */
  var lightbox = document.getElementById("lightbox");
  var lbImg = document.getElementById("lbImg");
  var lbTitle = document.getElementById("lbTitle");
  var lbDesc = document.getElementById("lbDesc");
  var lbClose = document.getElementById("lbClose");
  var lbPrev = document.getElementById("lbPrev");
  var lbNext = document.getElementById("lbNext");
  var current = 0;
  var returnFocus = null;

  function visibleCards() { return cards.filter(function (card) { return !card.hidden; }); }
  function show(index) {
    var visible = visibleCards();
    if (!visible.length) return;
    current = (index + visible.length) % visible.length;
    var card = visible[current];
    var image = card.querySelector("img");
    lbImg.src = image.getAttribute("src");
    lbImg.alt = image.alt;
    lbTitle.textContent = card.querySelector(".work-title").textContent;
    lbDesc.textContent = card.querySelector(".project-description").textContent;
    lbPrev.disabled = visible.length < 2;
    lbNext.disabled = visible.length < 2;
  }
  function openLightbox(card, trigger) {
    returnFocus = trigger;
    show(visibleCards().indexOf(card));
    lightbox.hidden = false;
    document.body.classList.add("dialog-open");
    lbClose.focus();
  }
  function closeLightbox() {
    lightbox.hidden = true;
    document.body.classList.remove("dialog-open");
    if (returnFocus) returnFocus.focus();
  }
  cards.forEach(function (card) {
    var trigger = card.querySelector(".project-open");
    trigger.addEventListener("click", function () { openLightbox(card, trigger); });
  });
  lbClose.addEventListener("click", closeLightbox);
  lbPrev.addEventListener("click", function () { show(current - 1); });
  lbNext.addEventListener("click", function () { show(current + 1); });
  lightbox.addEventListener("click", function (event) { if (event.target === lightbox) closeLightbox(); });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && nav.classList.contains("open")) {
      closeMenu();
      burger.focus();
    }
    if (lightbox.hidden) return;
    if (event.key === "Escape") closeLightbox();
    if (event.key === "ArrowLeft" && !lbPrev.disabled) show(current - 1);
    if (event.key === "ArrowRight" && !lbNext.disabled) show(current + 1);
    if (event.key === "Tab") {
      var controls = Array.prototype.slice.call(lightbox.querySelectorAll("button:not(:disabled)"));
      var first = controls[0];
      var last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    }
  });

  /* Contact form opens a pre-filled WhatsApp message; no data is sent elsewhere. */
  var form = document.getElementById("contactForm");
  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var name = form.elements.namedItem("name").value.trim();
    var phone = form.elements.namedItem("phone").value.trim();
    var service = form.elements.namedItem("service").value;
    var message = form.elements.namedItem("message").value.trim();
    var text = "Assalam-o-Alaikum Gx_Rajput!\n\n" +
      "Name: " + (name || "-") + "\n" +
      "Phone: " + (phone || "-") + "\n" +
      "Service: " + service + "\n" +
      "Details: " + (message || "-") + "\n\n" +
      "(Sent from your portfolio website)";
    window.open("https://wa.me/923110682944?text=" + encodeURIComponent(text), "_blank", "noopener");
  });
  document.getElementById("year").textContent = new Date().getFullYear();
})();

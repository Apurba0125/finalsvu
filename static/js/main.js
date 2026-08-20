/* ==========================================================================
   Swami Vivekananda University — front-end behaviour
   Vanilla JS, no dependencies, no inline handlers (keeps the CSP strict).
   Everything here is progressive enhancement: the site works without it.
   ========================================================================== */
(function () {
  "use strict";

  var $  = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) {
    return Array.prototype.slice.call((ctx || document).querySelectorAll(sel));
  };

  var prefersReducedMotion = window.matchMedia
    ? window.matchMedia("(prefers-reduced-motion: reduce)").matches
    : false;

  /* ----------------------------------------------------------------------
     1. Mobile navigation drawer
     ---------------------------------------------------------------------- */
  function initNavigation() {
    var nav = $("#site-nav");
    var toggle = $("#nav-toggle");
    var closeBtn = $("#nav-close");
    var scrim = $("#nav-scrim");
    if (!nav || !toggle) { return; }

    function openNav() {
      nav.classList.add("is-open");
      if (scrim) { scrim.classList.add("is-visible"); }
      document.body.classList.add("nav-open");
      toggle.setAttribute("aria-expanded", "true");
      var firstLink = $(".nav__link", nav);
      if (firstLink) { firstLink.focus(); }
    }

    function closeNav() {
      nav.classList.remove("is-open");
      if (scrim) { scrim.classList.remove("is-visible"); }
      document.body.classList.remove("nav-open");
      toggle.setAttribute("aria-expanded", "false");
    }

    toggle.addEventListener("click", function () {
      if (nav.classList.contains("is-open")) { closeNav(); } else { openNav(); }
    });
    if (closeBtn) { closeBtn.addEventListener("click", closeNav); }
    if (scrim) { scrim.addEventListener("click", closeNav); }

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        closeNav();
        toggle.focus();
      }
    });

    // Submenu behaviour: click-to-expand on touch/small screens,
    // pure CSS hover on desktop.
    $$(".nav__item--has-children", nav).forEach(function (item) {
      var link = $(".nav__link", item);
      if (!link) { return; }

      /* Did the tap land on the caret rather than the label? Walking up beats
         closest() here because the target is usually the <use> inside the
         <svg>, and closest() on an SVG element is not safe everywhere. */
      function onCaret(node) {
        while (node && node !== link) {
          if (node.classList && node.classList.contains("nav__caret")) { return true; }
          node = node.parentNode;
        }
        return false;
      }

      link.addEventListener("click", function (e) {
        var isMobile = window.matchMedia("(max-width: 991.98px)").matches;
        if (!isMobile) { return; }

        var submenu = $(".nav__submenu", item);
        if (!submenu) { return; }

        var href = link.getAttribute("href");
        var goesNowhere = !href || href === "#";

        /* The caret is the open/close control and never navigates. The label
           beside it stays an ordinary link, because several parents (Academic,
           Centre, Student Welfare Committees) point at a page that none of
           their children repeats — collapsing the whole row into a toggle
           would leave those three unreachable from the drawer. */
        if (item.classList.contains("is-open")) {
          if (onCaret(e.target) || goesNowhere) {
            e.preventDefault();
            item.classList.remove("is-open");
            link.setAttribute("aria-expanded", "false");
          }
          return;
        }

        // First tap expands, whether it landed on the caret or the label.
        e.preventDefault();
        $$(".nav__item--has-children.is-open", nav).forEach(function (other) {
          if (other !== item) {
            other.classList.remove("is-open");
            var l = $(".nav__link", other);
            if (l) { l.setAttribute("aria-expanded", "false"); }
          }
        });
        item.classList.add("is-open");
        link.setAttribute("aria-expanded", "true");
      });
    });

    // Reset drawer state when resizing up to desktop.
    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        if (window.innerWidth >= 992) {
          closeNav();
          $$(".nav__item.is-open", nav).forEach(function (i) {
            i.classList.remove("is-open");
          });
        }
      }, 150);
    });
  }

  /* ----------------------------------------------------------------------
     2. Hero video: keep the looping background clip playing
     ---------------------------------------------------------------------- */
  function initHeroVideo() {
    var video = $(".hero__video");
    if (!video) { return; }

    // Some browsers only honour autoplay once the element is muted in JS.
    video.muted = true;

    function play() {
      var attempt = video.play();
      if (attempt && attempt.catch) { attempt.catch(function () { /* poster stays */ }); }
    }

    play();
    // Resume after a tab switch, which pauses background media on mobile.
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden && video.paused) { play(); }
    });
    video.addEventListener("pause", function () {
      if (!document.hidden) { play(); }
    });
  }

  /* ----------------------------------------------------------------------
     3. Generic scroll-snap carousels (schools / events / testimonials)
     ---------------------------------------------------------------------- */
  function initCarousels() {
    $$(".carousel").forEach(function (carousel) {
      var track = $(".carousel__track", carousel);
      var items = $$(".carousel__item", track);
      var prev = $(".carousel__nav--prev", carousel);
      var next = $(".carousel__nav--next", carousel);
      var dotsWrap = $(".carousel__dots", carousel);
      if (!track || items.length === 0) { return; }

      /* data-step="1" moves one card at a time: the first screenful shows, then
         each advance slides a single card along. Without it a carousel jumps a
         whole screenful, which is the older behaviour and still the default. */
      var stepOne = carousel.getAttribute("data-step") === "1";

      /* data-axis="y" turns the same controller on its side: the track scrolls
         up instead of across. Everything below reads position through these
         four accessors so the arithmetic is written once, rather than a second
         near-copy of it living somewhere for vertical carousels. */
      var vertical = carousel.getAttribute("data-axis") === "y";

      /* data-loop="1" runs on for ever instead of rewinding at the end.

         A second copy of the slides is what makes the wrap invisible: by the
         time the last original has gone by, the copy of the first is sitting
         where it would be, so the track can be moved back by exactly one
         copy's worth with no animation and nothing appears to move. Rewinding
         without it means scrolling the whole way back in view of the visitor.

         The copies are hidden from assistive software and taken out of the tab
         order - they are the same slides twice. */
      var loop = carousel.getAttribute("data-loop") === "1";
      var originals = items.length;
      if (loop && originals > 1) {
        items.forEach(function (item) {
          var copy = item.cloneNode(true);
          copy.setAttribute("aria-hidden", "true");
          $$("a, button, input, [tabindex]", copy).forEach(function (el) {
            el.setAttribute("tabindex", "-1");
          });
          track.appendChild(copy);
        });
        items = $$(".carousel__item", track);
      }
      function scrollPos()      { return vertical ? track.scrollTop : track.scrollLeft; }
      function viewSize()       { return vertical ? track.clientHeight : track.clientWidth; }
      function scrollSize()     { return vertical ? track.scrollHeight : track.scrollWidth; }
      function boxSize(rect)    { return vertical ? rect.height : rect.width; }
      function boxStart(rect)   { return vertical ? rect.top : rect.left; }
      function scrollTo(amount) {
        var opts = { behavior: prefersReducedMotion ? "auto" : "smooth" };
        opts[vertical ? "top" : "left"] = amount;
        track.scrollTo(opts);
      }

      /* Everything about position comes from here, measured off the rendered
         cards rather than worked out from numbers repeated in the stylesheet.

         step   how far the track travels to bring the next card into the place
                the current one occupies: card plus gap, read as the distance
                between two card edges so the gap can change in CSS without
                this going quietly wrong.
         per    how many fit on screen. The last card in view has no gap after
                it, so a gap is added back before dividing - four cards of 296
                inside 1240 measure as 3.94 otherwise, and floor would call
                that three. */
      function metrics() {
        var first = items[0].getBoundingClientRect();
        var size = boxSize(first);
        var step = size + 18;
        if (items.length > 1) {
          var second = items[1].getBoundingClientRect();
          if (boxStart(second) > boxStart(first)) {
            step = boxStart(second) - boxStart(first);
          }
        }
        var gap = Math.max(0, step - size);
        var view = boxSize(track.getBoundingClientRect());
        return {
          step: step,
          per: (size && step) ? Math.max(1, Math.floor((view + gap + 1) / step)) : 1
        };
      }

      function perView() { return metrics().per; }
      function stride() { return metrics().step; }

      function pageCount() {
        return Math.max(1, Math.ceil(items.length / perView()));
      }

      /* The number of resting positions. Stepping a screenful at a time that
         is one per page; stepping a card at a time it is one per card until
         the last screenful is filled - not items.length, or the final stops
         would scroll past the end into empty track. */
      function stopCount() {
        /* The clones are not stops of their own - they exist so the wrap can
           happen out of sight. Counting them would double the dots. */
        if (loop) { return Math.max(1, originals); }
        if (stepOne) { return Math.max(1, items.length - perView() + 1); }
        return pageCount();
      }

      function currentStop() {
        var span = stride() * (stepOne ? 1 : perView());
        if (!span) { return 0; }
        return Math.round(scrollPos() / span);
      }

      function scrollToStop(stop) {
        scrollTo(stop * stride() * (stepOne ? 1 : perView()));
      }

      var dots = [];
      function buildDots() {
        if (!dotsWrap) { return; }
        dotsWrap.innerHTML = "";
        dots = [];
        var total = stopCount();
        if (total < 2) { dotsWrap.hidden = true; return; }
        dotsWrap.hidden = false;
        for (var i = 0; i < total; i++) {
          (function (page) {
            var b = document.createElement("button");
            b.type = "button";
            b.setAttribute("aria-label",
                           (stepOne ? "Go to slide " : "Go to slide group ") + (page + 1));
            b.addEventListener("click", function () { scrollToStop(page); });
            dotsWrap.appendChild(b);
            dots.push(b);
          })(i);
        }
      }

      function syncState() {
        var page = currentStop();
        dots.forEach(function (d, i) { d.classList.toggle("is-active", i === page); });
        if (prev) { prev.disabled = scrollPos() <= 4; }
        if (next) { next.disabled = scrollPos() + viewSize() >= scrollSize() - 4; }
      }

      if (prev) {
        prev.addEventListener("click", function () { scrollToStop(Math.max(0, currentStop() - 1)); });
      }
      if (next) {
        next.addEventListener("click", function () {
          scrollToStop(Math.min(stopCount() - 1, currentStop() + 1));
        });
      }

      var scrollTimer;
      track.addEventListener("scroll", function () {
        clearTimeout(scrollTimer);
        scrollTimer = setTimeout(syncState, 90);
      }, { passive: true });

      var resizeTimer;
      window.addEventListener("resize", function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () { buildDots(); syncState(); }, 180);
      });

      /* Opt-in autoplay: data-autoplay="5000" advances a page every 5s and
         wraps back to the first. It pauses while the visitor is hovering,
         tabbing through or dragging the track, and never runs at all for
         someone who asked for reduced motion. */
      var delay = parseInt(carousel.getAttribute("data-autoplay"), 10);
      if (delay > 0 && !prefersReducedMotion) {
        var timer = null;
        var paused = false;

        function tick() {
          /* Once a facade has been swapped for a real player, sliding the
             track out from under someone mid-video would be maddening — so
             the first play ends the autoplay for good. */
          if (carousel.querySelector("iframe")) { stop(); return; }
          if (paused || document.hidden || stopCount() < 2) { return; }
          // Wrap on the real scroll position, not on the page arithmetic: with
          // 5 items at 4-per-view the last page is a partial one, and page
          // maths alone would park the track at the end and never come back.
          if (loop) {
            var span = originals * stride();
            if (scrollPos() >= span - 1) {
              /* Back by exactly one copy, with no animation. What is under the
                 viewport before and after is the same slide, so the jump is
                 not visible - only the endless forward motion is. */
              var jump = { behavior: "auto" };
              jump[vertical ? "top" : "left"] = scrollPos() - span;
              track.scrollTo(jump);
            }
            scrollToStop(currentStop() + 1);
            return;
          }

          if (scrollPos() + viewSize() >= scrollSize() - 4) {
            scrollTo(0);
            return;
          }
          scrollToStop(currentStop() + 1);
        }
        function start() { stop(); timer = setInterval(tick, delay); }
        function stop() { if (timer) { clearInterval(timer); timer = null; } }

        ["mouseenter", "focusin", "touchstart", "pointerdown"].forEach(function (evt) {
          carousel.addEventListener(evt, function () { paused = true; }, { passive: true });
        });
        ["mouseleave", "focusout", "touchend", "pointerup"].forEach(function (evt) {
          carousel.addEventListener(evt, function () { paused = false; }, { passive: true });
        });
        document.addEventListener("visibilitychange", function () {
          if (document.hidden) { stop(); } else { start(); }
        });
        start();
      }

      buildDots();
      syncState();
    });
  }

  /* ----------------------------------------------------------------------
     3b. Generic tab panels — [data-tabs] with .tab-btn + .tab-pane
     Used by the department pages. The About page keeps its own variant
     below because its markup carries a mobile dropdown as well.
     ---------------------------------------------------------------------- */
  function initTabPanels() {
    $$("[data-tabs]").forEach(function (scope) {
      var buttons = $$(".tab-btn", scope);
      var panes = $$(".tab-pane", scope);
      if (!buttons.length || !panes.length) { return; }

      /* Optional dropdown control for narrow screens, where the pill row would
         wrap to more height than the panel it navigates. Absent above the
         breakpoint and absent entirely on any tab panel that does not ship
         one, so all three lookups are allowed to come back empty. */
      var nav = $(".dept-tabs__nav", scope);
      var toggle = $("[data-tabs-toggle]", scope);
      var label = toggle ? $("[data-tabs-current]", toggle) : null;

      function closeNav() {
        if (!nav || !toggle) { return; }
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }

      function select(button, focus) {
        var target = $(button.getAttribute("data-tab-target"), scope);
        if (!target) { return; }

        buttons.forEach(function (b) {
          b.classList.toggle("is-active", b === button);
          b.setAttribute("aria-selected", b === button ? "true" : "false");
          b.setAttribute("tabindex", b === button ? "0" : "-1");
        });
        panes.forEach(function (p) { p.classList.toggle("is-active", p === target); });

        /* Keep the dropdown label right even when the pill was clicked on a
           wide screen and the window is narrowed afterwards. */
        if (label) { label.textContent = button.textContent.trim(); }
        closeNav();

        if (focus) { button.focus(); }
      }

      buttons.forEach(function (button, index) {
        button.addEventListener("click", function () { select(button); });
        button.addEventListener("keydown", function (e) {
          var next = null;
          if (e.key === "ArrowRight" || e.key === "ArrowDown") {
            next = buttons[(index + 1) % buttons.length];
          }
          if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
            next = buttons[(index - 1 + buttons.length) % buttons.length];
          }
          if (e.key === "Home") { next = buttons[0]; }
          if (e.key === "End") { next = buttons[buttons.length - 1]; }
          if (next) { e.preventDefault(); select(next, true); }
        });
      });

      // Whichever button is marked active in the markup wins; otherwise first.
      var initial = buttons.filter(function (b) {
        return b.classList.contains("is-active");
      })[0] || buttons[0];
      select(initial);

      if (toggle && nav) {
        toggle.addEventListener("click", function () {
          var open = nav.classList.toggle("is-open");
          toggle.setAttribute("aria-expanded", open ? "true" : "false");
        });
        document.addEventListener("click", function (e) {
          if (!nav.contains(e.target) && !toggle.contains(e.target)) { closeNav(); }
        });
        document.addEventListener("keydown", function (e) {
          if (e.key === "Escape") { closeNav(); }
        });
      }
    });
  }

  /* ----------------------------------------------------------------------
     3c. Auto-scrolling list — notice board (vertical), logo strip (horizontal)
     A ticker, not a carousel: the list keeps its native scrolling and the
     items simply drift. Opt in with data-autoscroll="26" on the list, where
     the number is pixels per second, plus data-autoscroll-axis="x" to drift
     sideways instead of up.

     Unlike a paged carousel this never sits still for want of a full extra
     page — three logos loop just as happily as thirty.
     ---------------------------------------------------------------------- */
  function initAutoScroll() {
    $$("[data-autoscroll]").forEach(function (list) {
      var horizontal = list.getAttribute("data-autoscroll-axis") === "x";
      var originals = Array.prototype.slice.call(list.children);
      // Nothing to do if motion is unwanted, or if everything already fits.
      if (prefersReducedMotion || originals.length < 2) { return; }
      // A vertical list with nothing hidden has no reason to move. A logo
      // strip is the opposite case: looping is the point, so it always runs.
      if (!horizontal && list.scrollHeight <= list.clientHeight + 4) { return; }

      var speed = parseFloat(list.getAttribute("data-autoscroll")) || 26;

      /* A second copy of the list is what makes the wrap invisible: by the
         time the first copy has scrolled out of sight, the clone sits in
         exactly its place, so resetting to the top is never seen. The copies
         are hidden from screen readers and taken out of the tab order — they
         are the same notices twice. */
      originals.forEach(function (node) {
        var copy = node.cloneNode(true);
        copy.setAttribute("aria-hidden", "true");
        $$("a", copy).forEach(function (a) { a.setAttribute("tabindex", "-1"); });
        list.appendChild(copy);
      });

      function offset(node) {
        return horizontal ? node.offsetLeft : node.offsetTop;
      }
      function at() {
        return horizontal ? list.scrollLeft : list.scrollTop;
      }
      function moveTo(value) {
        if (horizontal) { list.scrollLeft = value; } else { list.scrollTop = value; }
      }

      function measure() {
        // Distance from the first original to the first clone — the exact
        // point at which the list may snap back with nothing visibly moving.
        return offset(list.children[originals.length]) - offset(list.children[0]);
      }

      var loopSize = measure();
      var pos = at();
      var lastFrame = null;
      var ourScroll = 0;
      var paused = false;
      var rafId = null;

      function frame(now) {
        if (lastFrame === null) { lastFrame = now; }
        var elapsed = now - lastFrame;
        lastFrame = now;

        /* The open drawer is animating a transform of its own, and a scroll
           write per frame behind it is what makes that slide stutter on a
           phone. Nothing here is visible while it is open anyway. */
        var idle = paused || document.hidden || loopSize <= 0 ||
                   document.body.classList.contains("nav-open");

        if (!idle) {
          pos += speed * elapsed / 1000;
          if (pos >= loopSize) { pos -= loopSize; }
          moveTo(pos);                   // fractional, so the drift is smooth
          /* Deliberately not ourScroll = at(): reading the position straight
             back after writing it forces a synchronous layout, sixty times a
             second, on every marquee at once. pos is what was just written,
             and the hand-scroll test below allows more slack than the
             browser's rounding can use up. */
          ourScroll = pos;
        }
        rafId = requestAnimationFrame(frame);
      }

      function start() {
        if (rafId === null) {
          lastFrame = null;   // a long pause must not become one long jump
          rafId = requestAnimationFrame(frame);
        }
      }

      function stop() {
        if (rafId !== null) {
          cancelAnimationFrame(rafId);
          rafId = null;
        }
      }

      /* Hovering stops it — the titles are links, and no one should have to
         chase a moving target to click one. */
      ["mouseenter", "focusin", "touchstart", "pointerdown"].forEach(function (evt) {
        list.addEventListener(evt, function () { paused = true; }, { passive: true });
      });
      ["mouseleave", "focusout", "touchend", "pointerup"].forEach(function (evt) {
        list.addEventListener(evt, function () { paused = false; }, { passive: true });
      });

      // Scrolled by hand? Carry on from there rather than yanking it back.
      list.addEventListener("scroll", function () {
        if (Math.abs(at() - ourScroll) > 1.5) { pos = at(); }
      }, { passive: true });

      var resizeTimer;
      window.addEventListener("resize", function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () { loopSize = measure(); }, 200);
      });

      /* Only animate what is on screen. Without this both marquees keep
         writing a scroll position every frame for the whole visit, including
         while the visitor is several screens further down the page. */
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) { start(); } else { stop(); }
          });
        }, { rootMargin: "100px" }).observe(list);
      } else {
        start();
      }
    });
  }

  /* ----------------------------------------------------------------------
     4. Back-to-top + sticky nav
     ---------------------------------------------------------------------- */
  function initScrollWidgets() {
    var toTop = $("#to-top");
    var nav = $("#site-nav");
    var navOffset = 0;
    var ticking = false;

    function measure() {
      if (!nav) { return; }
      /* offsetTop only means anything while the bar is in flow. Below 992px
         the same element is the off-canvas drawer, fixed at top: 0, so it
         reads 0 and every scroll position would count as past it. */
      if (window.innerWidth >= 992) {
        nav.classList.remove("is-stuck");
        navOffset = nav.offsetTop;
      }
    }

    function onScroll() {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      if (toTop) { toTop.classList.toggle("is-visible", y > 400); }
      if (nav) {
        /* The width test has to be part of the toggle, not a guard around it.
           Guarding meant the class was never cleared on the way DOWN through
           992px, and .nav.is-stuck is position: sticky - which outranks the
           drawer's position: fixed on specificity. A stale class therefore
           dropped the closed drawer back into the flow as a full-height white
           block, and the page looked blank. */
        nav.classList.toggle("is-stuck", window.innerWidth >= 992 && y > navOffset);
      }
      ticking = false;
    }

    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(onScroll);
        ticking = true;
      }
    }, { passive: true });

    if (toTop) {
      toTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: prefersReducedMotion ? "auto" : "smooth" });
      });
    }

    /* Crossing the breakpoint without scrolling still has to settle the class,
       and the offset is only correct once the bar is back in flow. */
    var resizeTimer;
    window.addEventListener("resize", function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () { measure(); onScroll(); }, 150);
    });

    measure();
    onScroll();
  }

  /* ----------------------------------------------------------------------
     5. YouTube click-to-load facade (privacy + performance)
     ---------------------------------------------------------------------- */
  function initVideoFacades() {
    $$(".video-facade").forEach(function (facade) {
      facade.addEventListener("click", function () {
        var wrap = facade.parentNode;
        var src = facade.getAttribute("data-src");
        var title = facade.getAttribute("data-title") || "Video";
        if (!src) { return; }

        var iframe = document.createElement("iframe");
        iframe.setAttribute("src", src + "&autoplay=1");
        iframe.setAttribute("title", title);
        iframe.setAttribute("loading", "lazy");
        iframe.setAttribute("allow",
          "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
        iframe.setAttribute("referrerpolicy", "strict-origin-when-cross-origin");
        iframe.setAttribute("allowfullscreen", "");
        wrap.replaceChild(iframe, facade);
      });
    });
  }

  /* ----------------------------------------------------------------------
     6. FAQ accordion
     ---------------------------------------------------------------------- */
  function initAccordions() {
    $$(".faq-item__q").forEach(function (button) {
      button.addEventListener("click", function () {
        var expanded = button.getAttribute("aria-expanded") === "true";
        var panel = document.getElementById(button.getAttribute("aria-controls"));
        button.setAttribute("aria-expanded", expanded ? "false" : "true");
        if (panel) { panel.hidden = expanded; }
      });
    });
  }

  /* ----------------------------------------------------------------------
     7. Enquiry form: dependent dropdowns, CAPTCHA refresh, AJAX submit
     ---------------------------------------------------------------------- */
  function getCsrfToken(form) {
    var input = form ? form.querySelector("[name=csrfmiddlewaretoken]") : null;
    return input ? input.value : "";
  }

  function setFieldError(form, fieldName, message) {
    var field = form.querySelector("[name='" + fieldName + "']");
    var wrapper = field ? field.closest(".form-field") : null;
    if (!wrapper) { return; }
    wrapper.classList.add("has-error");
    var existing = wrapper.querySelector(".field-error");
    if (!existing) {
      existing = document.createElement("span");
      existing.className = "field-error";
      wrapper.appendChild(existing);
    }
    existing.textContent = message;
  }

  function clearErrors(form) {
    $$(".form-field.has-error", form).forEach(function (w) {
      w.classList.remove("has-error");
    });
    $$(".field-error", form).forEach(function (e) { e.remove(); });
    var status = $(".form-status", form);
    if (status) { status.innerHTML = ""; }
  }

  function showStatus(form, type, message) {
    var status = $(".form-status", form);
    if (!status) { return; }
    status.innerHTML = "";
    var box = document.createElement("div");
    box.className = "alert alert--" + type;
    box.setAttribute("role", type === "error" ? "alert" : "status");
    box.textContent = message;
    status.appendChild(box);
    status.scrollIntoView({ behavior: prefersReducedMotion ? "auto" : "smooth", block: "center" });
  }

  function populateSelect(select, results, placeholder) {
    if (!select) { return; }
    var previous = select.value;
    select.innerHTML = "";
    var blank = document.createElement("option");
    blank.value = "";
    blank.textContent = placeholder;
    select.appendChild(blank);
    results.forEach(function (row) {
      var opt = document.createElement("option");
      opt.value = row.id;
      // textContent (never innerHTML) — server data is inserted as text only.
      opt.textContent = row.name;
      select.appendChild(opt);
    });
    if (previous) { select.value = previous; }
  }

  function initDependentSelect(form, parentName, childName, endpoint, param, placeholder) {
    var parent = form.querySelector("[name='" + parentName + "']");
    var child = form.querySelector("[name='" + childName + "']");
    if (!parent || !child || !endpoint) { return; }

    parent.addEventListener("change", function () {
      if (!parent.value) {
        populateSelect(child, [], placeholder);
        return;
      }
      child.disabled = true;
      fetch(endpoint + "?" + param + "=" + encodeURIComponent(parent.value), {
        headers: { "X-Requested-With": "XMLHttpRequest" },
        credentials: "same-origin"
      })
        .then(function (r) { return r.ok ? r.json() : { results: [] }; })
        .then(function (data) { populateSelect(child, data.results || [], placeholder); })
        .catch(function () { /* keep the full list on failure */ })
        .then(function () { child.disabled = false; });
    });
  }

  /* Same idea, but the child depends on more than one parent — the course list
     is narrowed by the chosen programme AND department. */
  function initMultiDependentSelect(form, parentNames, childName, endpoint, placeholder) {
    var parents = parentNames
      .map(function (name) { return form.querySelector("[name='" + name + "']"); })
      .filter(Boolean);
    var child = form.querySelector("[name='" + childName + "']");
    if (!parents.length || !child || !endpoint) { return; }

    function refresh() {
      var query = parents
        .filter(function (p) { return p.value; })
        .map(function (p) { return p.name + "=" + encodeURIComponent(p.value); })
        .join("&");

      child.disabled = true;
      fetch(endpoint + (query ? "?" + query : ""), {
        headers: { "X-Requested-With": "XMLHttpRequest" },
        credentials: "same-origin"
      })
        .then(function (r) { return r.ok ? r.json() : { results: [] }; })
        .then(function (data) { populateSelect(child, data.results || [], placeholder); })
        .catch(function () { /* keep the full list on failure */ })
        .then(function () { child.disabled = false; });
    }

    parents.forEach(function (p) { p.addEventListener("change", refresh); });
  }

  /* ----------------------------------------------------------------------
     7b. About Us tab panel (no Bootstrap in this build)
     ---------------------------------------------------------------------- */
  function initAboutTabs() {
    $$("[data-about-tabs]").forEach(function (scope) {
      var tabs = $$(".about-tab", scope);
      var nav = $(".about-tab-nav", scope);
      var toggle = $("[data-about-tab-toggle]", scope);
      var label = toggle ? $("[data-about-tab-current]", toggle) : null;
      if (!tabs.length) { return; }

      function closeNav() {
        if (!nav || !toggle) { return; }
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }

      function select(tab) {
        var pane = $(tab.getAttribute("data-tab-target"), scope);
        if (!pane) { return; }

        tabs.forEach(function (other) {
          other.classList.remove("is-active");
          other.setAttribute("aria-selected", "false");
        });
        $$(".about-pane", scope).forEach(function (p) { p.classList.remove("is-active"); });

        tab.classList.add("is-active");
        tab.setAttribute("aria-selected", "true");
        pane.classList.add("is-active");

        // Keeps the dropdown label right even if the pill was clicked on a
        // wide screen and the window is narrowed afterwards.
        if (label) { label.textContent = tab.textContent.trim(); }
        closeNav();
      }

      tabs.forEach(function (tab, index) {
        tab.addEventListener("click", function () { select(tab); });

        // Left/right arrows move between tabs, as a tablist should.
        tab.addEventListener("keydown", function (e) {
          var next = null;
          if (e.key === "ArrowRight") { next = tabs[(index + 1) % tabs.length]; }
          if (e.key === "ArrowLeft") { next = tabs[(index - 1 + tabs.length) % tabs.length]; }
          if (next) { e.preventDefault(); select(next); next.focus(); }
        });
      });

      if (toggle && nav) {
        toggle.addEventListener("click", function () {
          var open = nav.classList.toggle("is-open");
          toggle.setAttribute("aria-expanded", open ? "true" : "false");
        });
        document.addEventListener("click", function (e) {
          if (!nav.contains(e.target) && !toggle.contains(e.target)) { closeNav(); }
        });
        document.addEventListener("keydown", function (e) {
          if (e.key === "Escape") { closeNav(); }
        });
      }
    });
  }

  function initCaptchaRefresh(form) {
    var button = $(".captcha-refresh", form);
    var image = $(".captcha-image", form);
    if (!button || !image) { return; }
    var endpoint = button.getAttribute("data-endpoint");
    if (!endpoint) { return; }

    button.addEventListener("click", function () {
      button.disabled = true;
      fetch(endpoint, {
        headers: { "X-Requested-With": "XMLHttpRequest" },
        credentials: "same-origin"
      })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (data) {
          if (data && data.image) { image.setAttribute("src", data.image); }
          var input = form.querySelector("[name='captcha']");
          if (input) { input.value = ""; input.focus(); }
        })
        .catch(function () { /* silent — the user can reload the page */ })
        .then(function () { button.disabled = false; });
    });
  }

  function initEnquiryForms() {
    $$("form[data-enquiry-form]").forEach(function (form) {
      initCaptchaRefresh(form);
      initDependentSelect(
        form, "state", "city",
        form.getAttribute("data-cities-url"), "state", "Select City *"
      );
      initMultiDependentSelect(
        form, ["program", "department"], "course",
        form.getAttribute("data-courses-url"), "Select Course *"
      );

      // Digits only in the mobile field.
      var mobile = form.querySelector("[name='mobile']");
      if (mobile) {
        mobile.addEventListener("input", function () {
          mobile.value = mobile.value.replace(/\D/g, "").slice(0, 10);
        });
      }

      form.addEventListener("submit", function (e) {
        if (!window.fetch || !form.getAttribute("data-ajax")) { return; }
        e.preventDefault();

        var submitBtn = form.querySelector("[type=submit]");
        var originalLabel = submitBtn ? submitBtn.textContent : "";
        clearErrors(form);
        if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Submitting…"; }

        fetch(form.getAttribute("action"), {
          method: "POST",
          body: new FormData(form),
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCsrfToken(form)
          },
          credentials: "same-origin"
        })
          .then(function (response) {
            return response.json().then(function (data) {
              return { status: response.status, data: data };
            });
          })
          .then(function (result) {
            var data = result.data || {};
            if (data.ok) {
              form.reset();
              showStatus(form, "success", data.message || "Thank you! Your enquiry has been received.");
              var img = $(".captcha-image", form);
              var refresh = $(".captcha-refresh", form);
              if (img && refresh) { refresh.click(); }
              return;
            }

            if (data.captcha_image) {
              var image = $(".captcha-image", form);
              if (image) { image.setAttribute("src", data.captcha_image); }
            }

            if (data.errors) {
              var first = null;
              Object.keys(data.errors).forEach(function (field) {
                var messages = data.errors[field];
                var text = (messages && messages[0] && messages[0].message) || "Invalid value.";
                if (field === "__all__" || field === "form_ts" || field === "website") {
                  showStatus(form, "error", text);
                } else {
                  setFieldError(form, field, text);
                  if (!first) { first = form.querySelector("[name='" + field + "']"); }
                }
              });
              if (first) { first.focus(); }
              else { showStatus(form, "error", "Please correct the highlighted fields."); }
            } else {
              showStatus(form, "error", data.error || "Sorry, something went wrong. Please try again.");
            }
          })
          .catch(function () {
            // Network/JSON failure — fall back to a normal page submit.
            form.removeAttribute("data-ajax");
            form.submit();
          })
          .then(function () {
            if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = originalLabel; }
          });
      });
    });
  }

  /* ----------------------------------------------------------------------
     8. Lazy images without layout shift
     ---------------------------------------------------------------------- */
  function initLazyImages() {
    $$("img[data-src]").forEach(function (img) {
      if ("IntersectionObserver" in window) {
        var observer = new IntersectionObserver(function (entries, obs) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.src = entry.target.getAttribute("data-src");
              entry.target.removeAttribute("data-src");
              obs.unobserve(entry.target);
            }
          });
        }, { rootMargin: "200px" });
        observer.observe(img);
      } else {
        img.src = img.getAttribute("data-src");
      }
    });
  }

  /* ----------------------------------------------------------------------
     9. Photo viewer for the gallery grids
     Contract: data-viewer on a grid makes it one gallery, data-viewer-item on
     a cell makes it a frame. Nothing carries an index, so a photograph can be
     dropped into the middle of a grid without renumbering anything after it.
     One overlay is built on the first open and reused by every grid, so an
     extra section on the page costs nothing here.
     ---------------------------------------------------------------------- */
  function initPhotoViewer() {
    var grids = $$("[data-viewer]");
    if (!grids.length) { return; }

    var overlay = null;
    var img, caption, counter, closeBtn, fsBtn;
    var frames = [];    // the <img> of every cell in the grid currently open
    var index = 0;
    var opener = null;  // the cell that opened it, to restore focus on close

    function icon(name) {
      return '<svg aria-hidden="true" focusable="false"><use href="#i-' + name + '"></use></svg>';
    }

    // Safari and any browser with fullscreen disabled reject the promise
    // rather than throwing; an unhandled rejection in the console helps nobody.
    function swallow(result) {
      if (result && result["catch"]) { result["catch"](function () {}); }
    }

    function build() {
      overlay = document.createElement("div");
      overlay.className = "viewer";
      overlay.hidden = true;
      overlay.setAttribute("role", "dialog");
      overlay.setAttribute("aria-modal", "true");
      overlay.setAttribute("aria-label", "Photograph viewer");
      overlay.innerHTML =
        '<div class="viewer__bar">' +
          '<span class="viewer__count"></span>' +
          '<button class="viewer__btn viewer__fs" type="button" aria-label="Full screen">' +
            icon("expand") +
          '</button>' +
          '<button class="viewer__btn viewer__close" type="button" aria-label="Close viewer">' +
            icon("close") +
          '</button>' +
        '</div>' +
        '<button class="viewer__btn viewer__nav viewer__nav--prev" type="button" aria-label="Previous photograph">' +
          icon("chevron-left") +
        '</button>' +
        '<figure class="viewer__figure">' +
          '<img class="viewer__img" alt="">' +
          '<figcaption class="viewer__caption"></figcaption>' +
        '</figure>' +
        '<button class="viewer__btn viewer__nav viewer__nav--next" type="button" aria-label="Next photograph">' +
          icon("chevron-right") +
        '</button>';
      document.body.appendChild(overlay);

      img = $(".viewer__img", overlay);
      caption = $(".viewer__caption", overlay);
      counter = $(".viewer__count", overlay);
      closeBtn = $(".viewer__close", overlay);
      fsBtn = $(".viewer__fs", overlay);

      closeBtn.addEventListener("click", closeViewer);
      fsBtn.addEventListener("click", toggleFullscreen);
      $(".viewer__nav--prev", overlay).addEventListener("click", function () { step(-1); });
      $(".viewer__nav--next", overlay).addEventListener("click", function () { step(1); });

      // A click on the backdrop closes; one on the photograph must not.
      overlay.addEventListener("click", function (e) {
        if (e.target === overlay) { closeViewer(); }
      });

      // aria-modal claims focus stays inside, so it has to actually stay inside.
      overlay.addEventListener("keydown", function (e) {
        if (e.key !== "Tab") { return; }
        var stops = $$("button", overlay);
        if (!stops.length) { return; }
        var first = stops[0];
        var last = stops[stops.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      });

      document.addEventListener("keydown", function (e) {
        if (!overlay || overlay.hidden) { return; }
        if (e.key === "Escape") {
          // In fullscreen the browser's own Escape exits it; closing as well
          // would take two states off the stack for one keypress.
          if (!document.fullscreenElement) { closeViewer(); }
        } else if (e.key === "ArrowLeft") {
          step(-1);
        } else if (e.key === "ArrowRight") {
          step(1);
        }
      });

      document.addEventListener("fullscreenchange", syncFullscreenButton);
      initSwipe();
    }

    function initSwipe() {
      var startX = 0;
      var startY = 0;
      var tracking = false;

      overlay.addEventListener("touchstart", function (e) {
        tracking = e.touches.length === 1;
        if (!tracking) { return; }
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
      }, { passive: true });

      overlay.addEventListener("touchend", function (e) {
        if (!tracking) { return; }
        tracking = false;
        var touch = e.changedTouches[0];
        var dx = touch.clientX - startX;
        var dy = touch.clientY - startY;
        // Horizontal only: a mostly-vertical drag is a scroll, not a swipe.
        if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) {
          step(dx < 0 ? 1 : -1);
        }
      }, { passive: true });
    }

    function show(i) {
      if (!frames.length) { return; }
      // Wrap, so the arrows never dead-end at either edge of a section.
      index = (i + frames.length) % frames.length;
      var frame = frames[index];
      img.src = frame.currentSrc || frame.src;
      img.alt = frame.alt || "";
      // The caption IS the alt text — writing a good alt does double duty.
      caption.textContent = frame.alt || "";
      counter.textContent = (index + 1) + " / " + frames.length;
    }

    function step(delta) { show(index + delta); }

    function openViewer(grid, cell) {
      if (!overlay) { build(); }
      // Filter the cells first, not the images: dropping an empty cell out of
      // one list but not the other would slide every index after it by one.
      var cells = $$("[data-viewer-item]", grid).filter(function (item) {
        return !!$("img", item);
      });
      frames = cells.map(function (item) { return $("img", item); });
      if (!frames.length) { return; }

      opener = cell;
      overlay.hidden = false;
      document.body.classList.add("viewer-open");
      syncFullscreenButton();
      show(cells.indexOf(cell));
      closeBtn.focus();
    }

    function closeViewer() {
      if (!overlay || overlay.hidden) { return; }
      if (document.fullscreenElement && document.exitFullscreen) {
        swallow(document.exitFullscreen());
      }
      overlay.hidden = true;
      // Drop the photograph: several of them are 4704x3136.
      img.removeAttribute("src");
      document.body.classList.remove("viewer-open");
      if (opener) {
        opener.focus();
        opener = null;
      }
    }

    function toggleFullscreen() {
      if (document.fullscreenElement) {
        if (document.exitFullscreen) { swallow(document.exitFullscreen()); }
      } else if (overlay.requestFullscreen) {
        swallow(overlay.requestFullscreen());
      }
    }

    function syncFullscreenButton() {
      var full = !!document.fullscreenElement;
      fsBtn.setAttribute("aria-label", full ? "Exit full screen" : "Full screen");
      fsBtn.innerHTML = icon(full ? "collapse" : "expand");
    }

    grids.forEach(function (grid) {
      $$("[data-viewer-item]", grid).forEach(function (cell) {
        cell.addEventListener("click", function () { openViewer(grid, cell); });
      });
    });
  }

  /* ----------------------------------------------------------------------
     10. Counting figures
     Counts up the first time the figure scrolls into view, then stops being
     watched so it never replays on the way back past.
     ---------------------------------------------------------------------- */
  function initCounters() {
    var counters = $$("[data-count-to]");
    if (!counters.length) { return; }

    function decimalsOf(el) {
      return parseInt(el.getAttribute("data-count-decimals"), 10) || 0;
    }

    /* Group the whole part only. Running the separator over the string after
       toFixed would put commas inside the decimals as well. */
    function format(value, decimals) {
      var parts = value.toFixed(decimals).split(".");
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      return parts.join(".");
    }

    function run(el) {
      var target = parseFloat(el.getAttribute("data-count-to"));
      if (isNaN(target)) { return; }
      var decimals = decimalsOf(el);
      var duration = parseInt(el.getAttribute("data-count-duration"), 10) || 1600;

      if (prefersReducedMotion || duration <= 0) {
        el.textContent = format(target, decimals);
        return;
      }

      var startedAt = null;
      function frame(now) {
        if (startedAt === null) { startedAt = now; }
        var t = Math.min((now - startedAt) / duration, 1);
        // Ease out: quick off the mark, settling onto the figure rather than
        // stopping dead on it.
        el.textContent = format(target * (1 - Math.pow(1 - t, 3)), decimals);
        if (t < 1) { requestAnimationFrame(frame); }
      }
      requestAnimationFrame(frame);
    }

    /* Zero them first. The markup ships the final figure so the page still
       states it with no JS at all, but once we are running the count has to
       start from the bottom rather than flash the answer and then climb. */
    counters.forEach(function (el) { el.textContent = format(0, decimalsOf(el)); });

    if (!("IntersectionObserver" in window)) {
      counters.forEach(run);
      return;
    }

    var observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) { return; }
        obs.unobserve(entry.target);
        run(entry.target);
      });
    }, { threshold: 0.4 });
    counters.forEach(function (el) { observer.observe(el); });
  }

  /* ----------------------------------------------------------------------
     Bootstrap
     ---------------------------------------------------------------------- */
  function init() {
    initNavigation();
    initHeroVideo();
    initCarousels();
    initAutoScroll();
    initTabPanels();
    initAboutTabs();
    initScrollWidgets();
    initVideoFacades();
    initAccordions();
    initEnquiryForms();
    initLazyImages();
    initPhotoViewer();
    initCounters();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

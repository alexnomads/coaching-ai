# Build Brief: AI Era Career Coach Website
**For: Autonomous Build Agent**

---

## What You're Building

A production-ready personal coaching website for Alessandro Capezza — an AI and go-to-market specialist offering career coaching to mid-career professionals navigating the AI era.

The project consists of **two HTML pages** (already built, provided as artifacts), a **hero background video** (source link below), and a **project litepaper** (provided) that documents every design and content decision.

Your job is to:
1. Assemble all files into a clean project structure
2. Integrate the hero video into the landing page
3. Ensure all links, CTAs, and cross-page navigation work correctly
4. Deliver a deploy-ready static site

---

## Files You Have

You are being given the following files:

| File | Description |
|------|-------------|
| `career-coach-landing.html` | Main landing page — fully built |
| `career-risk-assessment.html` | Interactive quiz page — fully built |
| `LITEPAPER.md` | Full project spec, design system, content decisions |

---

## Hero Video

**Source:** https://drive.google.com/file/d/1KvRR_ZokByt5x-grKnIu9T5FM5fwYjww/view

**Steps:**
1. Download the video from the Google Drive link above
2. Compress to web-optimized H.264 MP4 (max 8MB, 1920px wide):
   ```bash
   ffmpeg -i input_video.mp4 -vcodec h264 -acodec aac -vf scale=1920:-2 -crf 28 assets/hero.mp4
   ```
3. Save to `assets/hero.mp4`

**Integration into `career-coach-landing.html`:**

Locate the `.hero` section. Add this video element as the FIRST child inside `.hero`, before the era-track div:

```html
<video autoplay muted loop playsinline class="hero-video">
  <source src="assets/hero.mp4" type="video/mp4">
</video>
```

Add this CSS inside the `<style>` block (the `.hero` rule already sets `position: relative; overflow: hidden` — just add the video rule):

```css
.hero-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.18;
  z-index: 0;
  pointer-events: none;
}
```

All existing `.hero` children already have `position: relative` through their animation styles — confirm `.hero-era-track`, `.hero-main`, and `.hero-scroll` all have either `position: relative` or are inside a relatively-positioned parent. If not, add `position: relative; z-index: 1;` to each.

---

## Project Structure to Create

```
project/
├── index.html                    ← Rename/copy of career-coach-landing.html
├── career-risk-assessment.html   ← Quiz page (no changes needed)
├── assets/
│   └── hero.mp4                  ← Downloaded and compressed video
└── LITEPAPER.md                  ← Project documentation
```

---

## Link Audit — Check All of These

Go through both HTML files and verify:

### `career-coach-landing.html` (becomes `index.html`)
- [ ] Nav "Risk Quiz" link → `career-risk-assessment.html` ✓
- [ ] Quiz strip "Take the Free Quiz" button → `career-risk-assessment.html` ✓
- [ ] All "Book Diagnostic" buttons → currently `mailto:aicoachalex@gmail.com?subject=...`
  - **Note:** Replace with actual Calendly link when available. For now, mailto is fine.
- [ ] Footer LinkedIn → `https://linkedin.com/in/alessandrocapezza` ✓
- [ ] Footer X/Twitter → `https://x.com/alexNomads` ✓

### `career-risk-assessment.html`
- [ ] Nav "← Back to Coaching" link → `career-coach-landing.html` (update to `index.html` if renaming)
- [ ] "Book Diagnostic Call — 29€" result CTA → `mailto:aicoachalex@gmail.com?subject=...`
  - **Note:** Replace with Calendly when available

---

## Design System Reference (do not change)

If you need to make any adjustments, use only these values:

```css
--white:      #f8f6f1;
--black:      #0d0c0a;
--green:      #9fe870;
--green-deep: #163300;
--muted:      #7a7670;
--border:     rgba(13,12,10,0.1);
```

**Fonts (loaded from Google Fonts):**
- Headlines: `Fraunces` — italic, weight 700/900
- Body/UI: `Instrument Sans` — weight 400/500

**Do not** change fonts, colors, layout, or copy. The design is finalized.

---

## What Good Delivery Looks Like

- [ ] All files in correct folder structure
- [ ] Hero video integrated and playing (looping, muted, behind text at ~18% opacity)
- [ ] Both pages load without console errors
- [ ] All internal links work (landing ↔ quiz)
- [ ] Marquee animation runs smoothly
- [ ] Scroll reveal animations trigger correctly
- [ ] Custom cursor visible on desktop
- [ ] Mobile layout correct on 375px viewport (single column, no overflow)
- [ ] Quiz flow works end-to-end: industry → job → experience → AI level → results → CTA
- [ ] Pricing CTA buttons link correctly

---

## Optional Enhancements (only if time allows, do not prioritize over above)

1. **Calendly integration:** Replace all `mailto:` booking links with a Calendly popup or redirect. Alessandro can provide the Calendly URL.
2. **Analytics:** Add a `<script>` tag for Plausible or Google Analytics in the `<head>` of both pages.
3. **Meta tags:** Add `<meta name="description">` and Open Graph tags (`og:title`, `og:description`, `og:image`) to both pages for social sharing.
4. **Favicon:** Create a simple `favicon.ico` — a small green square with "AC" initials in Fraunces would be on-brand.

---

## Hosting Notes

Alessandro has a **Hostinger KVM1 VPS** (Ubuntu 24.04, IP 187.124.39.207) available if self-hosting. Alternatively, the site can be deployed to Vercel or Netlify with a single drag-and-drop of the project folder.

For VPS deployment, a simple nginx config would work:
```nginx
server {
  listen 80;
  server_name yourdomain.com;
  root /var/www/career-coach;
  index index.html;
  location / { try_files $uri $uri/ =404; }
}
```

---

## Contact for Clarifications

Alessandro Capezza
- LinkedIn: https://linkedin.com/in/alessandrocapezza
- X/Twitter: https://x.com/alexNomads

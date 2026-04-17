# AI Era Career Coach — Project Litepaper
**Version 1.0 · Alessandro Capezza · April 2025**

---

## 1. Project Summary

This is a personal coaching website for Alessandro Capezza — a go-to-market and AI product specialist offering career coaching to mid-career professionals navigating the shift into the AI era.

The site has two goals:
1. Convert visitors into a **29€ diagnostic call** booking
2. Qualify those visitors into monthly (300€) or 3-month (900€) coaching engagements

The site is **not** a platform, not a SaaS product, and not a blog. It is a high-trust, single-coach conversion site — the digital equivalent of a premium consultancy landing page.

---

## 2. The Coach — Alessandro Capezza

**Profile:**
- 7+ years at the intersection of Product, Marketing, and Community Growth
- Deep web3 and AI ecosystem experience: Series B launches, grant-winning MVPs, content pipelines reaching 550k+ organic views
- Builder mindset: treats every problem as a system (inputs → levers → outputs)
- Based in Barcelona, active in the European web3/AI ecosystem

**Contact / Profiles:**
- LinkedIn: https://linkedin.com/in/alessandrocapezza
- X/Twitter: https://x.com/alexNomads
- Email: hello@alessandrocapezza.com (placeholder — update before launch)

**Core positioning statement:**
> "I treat marketing like an engineering problem. I move quickly with small, testable builds. I use agents to multiply output, not replace judgment."

**Proof points (case studies):**
1. **Rose of Jericho** — AI wellness app MVP (Lovable + Claude + Supabase + N8N), won Polygon grant and Soonami hackathon. Users averaged 18+ hours of session time.
2. **GenLayer** — Content pipeline for $7.5M AI blockchain company. LLM script generation + automated scheduling → single video reached 551k views.
3. **LandVault** — Series B GTM coordination across Product, Community, Partnerships, Video, Content. Retool + Zapier + Notion campaign hub.
4. **Qubit Wallet** — Early user acquisition: ambassador flows, GPT-generated A/B variants, lifecycle automation. First 500+ users via Zealy and Product Hunt (top crypto category).
5. **The Sandbox** — Ambassador program design: Typeform → Airtable → Retool with automated token distribution triggers.
6. **Safe** — Developer content and vectorized research library using LLM embeddings.

---

## 3. Target Audience

**Primary: Mid-career professionals, 5–15 years experience**
- Age range: 28–45
- Titles: Marketing Manager, Product Manager, Business Analyst, Operations Lead, Consultant, Account Manager, Content Strategist, Project Manager, Sales Manager
- Industries: tech, fintech, marketing/advertising, consulting, media, finance
- Pain state: successful but plateauing; sensing their role is changing but unsure how; watching AI tools appear in their workflow without a strategy for them
- Motivation to act: fear of being outpaced by AI-augmented colleagues; desire to stay at the front of their field

**Secondary: Career changers and freelancers (5–10 years experience)**
- Solopreneurs, consultants, agency workers feeling their model disrupted
- Open to repositioning as "AI-augmented" operators

**What they are NOT:**
- Entry-level job seekers (wrong fit for the price point)
- C-suite executives (served by high-touch executive coaches at 15k+)
- Complete AI beginners with no professional context

---

## 4. Unique Positioning

The career coaching market is bifurcated:
- **High end** (€15k–50k+): Tandem Coaching, Career Power — high-touch, very expensive, executive-only
- **Low end** ($29/mo): BetterUp, Modern Compass, Valence — automated, impersonal, no strategic depth

Alessandro sits in the **Specialized Boutique** gap:
- More strategic than a chatbot
- More accessible than a €15k retainer
- Backed by **real shipped work** (not coaching theory)
- Hybrid model: human coaching + AI tools between sessions

**The narrative frame that makes this unique:**
The Industrial Era → Digital Era → AI Era progression. Most coaches don't have a historical frame. This one does — and it gives clients a map to locate themselves in the story and understand what they need to do next.

**The key hook:**
> "You got comfortable. It's not too late."

This message hits the mid-career plateau pain point without shame. It acknowledges the problem ("you stopped adapting") while opening a door ("there's still time").

---

## 5. Website Structure & Content

### Pages

**Page 1: Landing Page** (`index.html` / `career-coach-landing.html`)

Sections in order:
1. **Hero** — Full-viewport black section. Oversized Fraunces serif type: "You got comfortable. It's not too late." Era timeline strip at the top (Industrial Era → Digital Era → AI Era · Today). Hero video background (looping, muted). CTA: "Book Diagnostic — 29€"
2. **Marquee strip** — Green background, scrolling text: key phrases
3. **Era Columns** — 3-column grid, one column per era. AI Era column is inverted (dark background, green accent) as the "active" state
4. **Problem Statement** — 2-column: left has the big statement ("The skills that got you here won't get you there"), right has the explanation
5. **Framework** — Dark background. 4-step process: Diagnostic Call → Where Are You Now → What's Changing → Where You Need to Be
6. **Proof / Case Studies** — Full-bleed list layout, one row per case study with: tag, title, description, metric
7. **Quiz CTA Strip** — Green background. Promotes the free Career Risk Assessment quiz
8. **Pricing** — 3 columns: 29€ entry / 300€ monthly (featured, dark background) / 900€ 3-month
9. **About** — Dark background. Left: bio + stats grid. Right: mindset principles list
10. **Final CTA** — White background, huge type: "Book your diagnostic. Today." with big ghost "29€" text in background

**Page 2: Career Risk Assessment Quiz** (`career-risk-assessment.html`)

A 4-step interactive quiz:
1. **Industry selector** — 26 industry cards with avg risk %
2. **Role selector** — 289 jobs searchable by industry, each with displacement risk %
3. **Experience level** — 4 options, each applies a risk multiplier
4. **AI fluency level** — 5 options, each reduces risk score

Output: **Dual score result page**
- Displacement Risk % (chance of being outcompeted by AI-augmented workers)
- Replacement Risk % (probability of full job elimination)
- Tier-specific 3-point action plan (Critical / High / Moderate / Low)
- CTA to book the 29€ diagnostic call

---

## 6. Design System

### Visual Direction
Inspired by Wise.design's **typography-as-hero** approach: text fills entire viewport sections, hard color blocks separate sections, no illustration or stock photography dependency.

### Typography
- **Display / Headlines:** Fraunces (serif, variable — optical size 9-144, weight 300–900, supports italic)
  - Load: `https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,700;0,9..144,900;1,9..144,300;1,9..144,700;1,9..144,900`
- **Body / UI:** Instrument Sans (weight 400, 500)
  - Load: `https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500`

### Color Palette
```css
--white:  #f8f6f1;   /* warm off-white — all light sections */
--black:  #0d0c0a;   /* near-black — hero, framework, about */
--green:  #9fe870;   /* single accent color — marquee, quiz strip, buttons, highlights */
--green-deep: #163300; /* darker green for hover states */
--muted:  #7a7670;   /* body text, labels, secondary content */
--border: rgba(13,12,10,0.1); /* subtle dividers */
```

### Key Design Decisions
- **No illustrations or stock photos** — type is the visual
- **Hard section alternation** — white / black / white / black creates rhythm without decoration
- **Green as single accent** — appears only for: active states, CTAs, italic highlights in headlines, marquee strip, quiz strip background, decorative bullet dots
- **Custom cursor** — small green dot, grows on hover over interactive elements (desktop only)
- **Mix-blend-mode nav** — nav text inverts to stay readable on both dark and light backgrounds
- **Marquee strip** — green background, italic Fraunces, scrolling key phrases between hero and era columns
- **Scroll-triggered reveals** — `.reveal` class with IntersectionObserver, `fadeUp` 0.55s ease
- **Era columns hover state** — each column flips to dark background + green accent on hover; "AI Era" column is permanently in active state

### Responsive Breakpoints
- Desktop: full grid layouts (3-col eras, 4-col steps, 3-col pricing)
- Mobile (≤900px): single column everything, nav collapses to logo + CTA only, cursor disabled

---

## 7. Hero Video

**Source:** Google Drive — https://drive.google.com/file/d/1KvRR_ZokByt5x-grKnIu9T5FM5fwYjww/view

**Usage:** Loop, muted, autoplay background video inside the hero section. The video sits behind the text content at reduced opacity (suggested: 15–25% opacity, or `mix-blend-mode: screen` / `luminosity` depending on video content). Text overlay must remain fully legible.

**Implementation:**
```html
<video autoplay muted loop playsinline class="hero-video">
  <source src="assets/hero.mp4" type="video/mp4">
</video>
```

**File handling:** Download from Drive, convert/compress to H.264 MP4 for web if needed, store at `assets/hero.mp4`. Recommended max size: under 8MB for fast load. Use `ffmpeg` to compress if needed:
```bash
ffmpeg -i input.mp4 -vcodec h264 -acodec aac -vf scale=1920:-2 -crf 28 assets/hero.mp4
```

**CSS for video positioning:**
```css
.hero { position: relative; overflow: hidden; }
.hero-video {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  opacity: 0.18;
  z-index: 0;
}
.hero > * { position: relative; z-index: 1; }
```

---

## 8. Pricing

| Tier | Price | Duration | Key features |
|------|-------|----------|--------------|
| Diagnostic Call | 29€ | One-time · 30 min | AI-era readiness assessment, role risk mapping, custom pivot direction, clear next steps |
| Monthly Engagement | 300€/mo | 1-month commitment | Weekly 1:1 sessions, AI tools between sessions, LinkedIn positioning, async Telegram support |
| 3-Month Programme | 900€ | 3 months | Everything in monthly + full narrative development, AI tool stack setup, LinkedIn authority plan, transformation case study |

The 29€ call is deliberately a "tripwire" — low enough to remove friction, high enough to filter serious prospects. It must be framed as a **Diagnostic Audit**, not a free consultation or sales call.

---

## 9. Key Conversion Flows

### Primary flow
1. User lands on homepage via LinkedIn or X/Twitter share
2. Reads hero + era narrative
3. Scrolls to pricing
4. Books 29€ diagnostic via email/Calendly link
5. Post-call: converts to monthly or 3-month

### Lead magnet flow
1. User lands on homepage
2. Clicks "Take the Free Quiz" (green quiz strip or nav)
3. Completes 4-step Career Risk Assessment
4. Receives dual risk score + action plan
5. CTA at bottom of results: "Book Diagnostic Call — 29€"

### Recommended booking integrations (to implement):
- Replace `mailto:` CTA links with a **Calendly** embed or link (for the 29€ call, add Stripe payment)
- Add a simple **email capture** before quiz results (optional — test with and without)

---

## 10. Technical Stack

| Element | Decision |
|---------|----------|
| Framework | Vanilla HTML/CSS/JS — no build tools required |
| Fonts | Google Fonts (Fraunces + Instrument Sans) |
| Animations | CSS keyframes + IntersectionObserver |
| Video | HTML5 `<video>` tag, self-hosted MP4 |
| Forms/Booking | Mailto links → replace with Calendly + Stripe |
| Hosting | Any static host: Vercel, Netlify, GitHub Pages, or Hostinger (Alessandro already has a KVM1 VPS) |
| Domain | To be confirmed |
| Analytics | Add Google Analytics or Plausible script in `<head>` |

---

## 11. File Manifest

```
project/
├── index.html                    ← Main landing page (career-coach-landing.html)
├── career-risk-assessment.html   ← Career Risk Assessment quiz
├── assets/
│   └── hero.mp4                  ← Hero background video (download from Drive link above)
└── LITEPAPER.md                  ← This document
```

---

## 12. Outstanding Items Before Launch

- [ ] Replace `hello@alessandrocapezza.com` with real email or Calendly link throughout both HTML files
- [ ] Download hero video from Drive, compress, save as `assets/hero.mp4`
- [ ] Add video to hero section (see Section 7 for implementation)
- [ ] Set up domain and deploy to hosting
- [ ] Add analytics (Plausible recommended for privacy-first)
- [ ] Test all CTAs and quiz flow on mobile
- [ ] Optional: add email capture before quiz results to build a list

---

*Document prepared April 2025. All HTML files referenced here are production-ready and available as build artifacts.*

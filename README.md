# AI Era Career Coach Website

**For: Alessandro Capezza**

---

## Setup Instructions

### 1. Download Hero Video

The hero video requires manual download from Google Drive:

1. Go to: https://drive.google.com/file/d/1KvRR_ZokByt5x-grKnIu9T5FM5fwYjww/view
2. Download the video file
3. Compress for web (max 8MB, 1920px wide):
   ```bash
   ffmpeg -i input.mp4 -vcodec h264 -acodec aac -vf scale=1920:-2 -crf 28 assets/hero.mp4
   ```
4. Save to: `assets/hero.mp4`

### 2. Install Dependencies (if needed)
```bash
pip install -r requirements.txt
```

### 3. Run Locally
```bash
# Using Python
python -m http.server 8000

# Then open http://localhost:8000
```

---

## Project Structure

```
career-coach/
├── index.html                    ← Landing page
├── career-risk-assessment.html   ← Quiz page
├── assets/
│   └── hero.mp4                 ← [TODO: Download from Drive]
├── AGENT_BRIEF.md               ← Build instructions
├── LITEPAPER.md                 ← Full project spec
├── README.md                    ← This file
└── requirements.txt             ← Dependencies
```

---

## Deployment

### Option A: Vercel / Netlify
Drag and drop the `career-coach` folder to vercel.com or netlify.com

### Option B: Hostinger VPS
```bash
scp -r career-coach/ user@187.124.39.207:/var/www/
# Then configure nginx (see AGENT_BRIEF.md)
```

---

## Outstanding Items

- [ ] Download hero video from Google Drive
- [ ] Replace `mailto:` links with Calendly when available
- [ ] Configure domain
- [ ] Add analytics script
- [ ] Test on mobile devices

---

## Links to Verify

### index.html
- [x] Nav "Risk Quiz" → `career-risk-assessment.html`
- [ ] Quiz strip CTA → (Calendly when available)
- [ ] Book Diagnostic buttons → (Calendly when available)
- [x] LinkedIn footer → https://linkedin.com/in/alessandrocapezza
- [x] X/Twitter footer → https://x.com/alexNomads

### career-risk-assessment.html
- [x] Nav "← Back to Coaching" → `index.html`
- [ ] Result CTA → (Calendly when available)

---

*Generated April 10, 2026*

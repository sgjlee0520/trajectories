# Trajectories PDF Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a static bilingual PDF reader at `https://sgjlee0520.github.io/trajectories-site/` from a new public GitHub repo.

**Architecture:** Plain HTML and one CSS file. GitHub Pages serves `main` from the repo root. PDFs are copies from `~/trajectories/analysis/`. Every in-page URL is relative so the project-site prefix `/trajectories-site/` works; `404.html` is the exception and uses `/trajectories-site/en/` and `/trajectories-site/ko/` because a 404 is served under the missing path.

**Tech Stack:** HTML, CSS, four copied PDFs. No npm, no Jekyll (`.nojekyll`). Verification is `scripts/check_site.py` (stdlib) plus `python3 -m http.server`.

## Global Constraints

- **Site root is `~/trajectories-site`.** Not inside the research repo.
- **No frameworks, no Google Fonts, no emoji icons, no dark mode, no JS except root `index.html` language redirect.**
- **Relative URLs everywhere except `404.html`.** Never write `href="/en/"`.
- **Bar:** `min-height: 48px`. Detail pages use a column flex body so a wrapping bar still leaves the iframe the remaining height (do not use `calc(100vh - 48px)` alone).
- **Colors:** background `#FFFFFF`, text `#111111`, muted `#64748B`, 1px `#111111` rule under the bar and under the homepage header.
- **Font:** `system-ui, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif`. Body 16px / 1.5.
- **Homepage max-width:** `40rem`, centered.
- **Tap targets:** numbered rows and bar links `min-height: 44px`.
- **Site name:** the word `Trajectories` in both languages, not translated.
- **Language switch copy:** `English` and `한국어`. Active language is not a link.
- **영문만 제공** only on `ko/people/` and `ko/decision/`.

## File Structure

```
~/trajectories-site/
  .gitignore
  .nojekyll
  README.md
  index.html
  404.html
  css/site.css
  scripts/check_site.py
  en/index.html
  en/paper/index.html
  en/people/index.html
  en/decision/index.html
  ko/index.html
  ko/paper/index.html
  ko/people/index.html
  ko/decision/index.html
  pdfs/paper.pdf
  pdfs/paper-ko.pdf
  pdfs/people.pdf
  pdfs/decision.pdf
```

---

### Task 1: Scaffold, CSS, PDFs, check script

**Files:**
- Create: `~/trajectories-site/.gitignore`
- Create: `~/trajectories-site/.nojekyll`
- Create: `~/trajectories-site/css/site.css`
- Create: `~/trajectories-site/scripts/check_site.py`
- Copy: four PDFs into `~/trajectories-site/pdfs/`

**Interfaces:**
- Consumes: `~/trajectories/analysis/paper.pdf`, `paper-ko.pdf`, `people.pdf`, `~/trajectories/analysis/personal/decision.pdf`
- Produces: shared CSS classes `.site`, `.lang`, `.toc`, `.bar`, `.viewer` that later HTML files use

- [ ] **Step 1: Create the directory, gitignore, empty `.nojekyll`, copy PDFs**

```bash
mkdir -p ~/trajectories-site/{css,scripts,en/paper,en/people,en/decision,ko/paper,ko/people,ko/decision,pdfs}
printf '%s\n' '.DS_Store' > ~/trajectories-site/.gitignore
touch ~/trajectories-site/.nojekyll
cp ~/trajectories/analysis/paper.pdf ~/trajectories-site/pdfs/paper.pdf
cp ~/trajectories/analysis/paper-ko.pdf ~/trajectories-site/pdfs/paper-ko.pdf
cp ~/trajectories/analysis/people.pdf ~/trajectories-site/pdfs/people.pdf
cp ~/trajectories/analysis/personal/decision.pdf ~/trajectories-site/pdfs/decision.pdf
```

Expected: four PDFs, each larger than 100K.

- [ ] **Step 2: Write `css/site.css`** (full file in implementation; classes listed above). Include `:focus-visible { outline: 2px solid #111; outline-offset: 2px; }`, link hover underline 150ms, `@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }`.

- [ ] **Step 3: Write `scripts/check_site.py`** so it fails before HTML exists: required paths present; PDFs non-empty; later HTML assertions (iframe targets, `lang`, 영문만 제공 placement, no `href="/en/"`).

- [ ] **Step 4: Run the check; it must fail on missing HTML.** Then git init and commit scaffold.

---

### Task 2: Root redirect, 404, English pages

**Files:**
- Create: `index.html`, `404.html`, `en/index.html`, `en/paper/index.html`, `en/people/index.html`, `en/decision/index.html`

**Interfaces:**
- English titles: `How Long Before the First Hit?`, `The People`, `What This Study Can and Cannot Tell You`
- Paper iframe: `../../pdfs/paper.pdf`
- People iframe: `../../pdfs/people.pdf`
- Decision iframe: `../../pdfs/decision.pdf`

- [ ] **Step 1: Write the six HTML files.** Root redirect: `if (navigator.language.toLowerCase().indexOf('ko') === 0) location.replace('ko/'); else location.replace('en/');` plus `<noscript>` links. `404.html` links `/trajectories-site/en/` and `/trajectories-site/ko/`.

- [ ] **Step 2: Run `python3 scripts/check_site.py` from the site root.** English assertions pass; Korean files still missing so the script should still fail until Task 3, unless the script checks files independently and reports Korean as missing — keep Korean files in the required-path list so Task 2 ends with a known remaining failure for `ko/*.html` only.

Better: Task 2 check is a subset. Task 3 runs the full script to green.

- [ ] **Step 3: Commit English pages.**

---

### Task 3: Korean pages and README

**Files:**
- Create: `ko/index.html`, `ko/paper/index.html`, `ko/people/index.html`, `ko/decision/index.html`, `README.md`

**Interfaces:**
- Korean titles: `첫 성과까지 얼마나 걸리는가`, `사람들`, `이 연구가 말해 줄 수 있는 것과 없는 것`
- `ko/paper/` iframe: `../../pdfs/paper-ko.pdf`
- `ko/people/` and `ko/decision/`: English PDFs + **영문만 제공**

- [ ] **Step 1: Write the four Korean HTML files and README** (PDFs are copies; refresh by copying from `sgjlee0520/trajectories` `analysis/`).

- [ ] **Step 2: `python3 scripts/check_site.py` — exit 0.**

- [ ] **Step 3: Commit.**

---

### Task 4: Local serve verification

- [ ] **Step 1:** `python3 -m http.server 8765` in `~/trajectories-site`.
- [ ] **Step 2:** `curl -sI` / `curl -s` against `/`, `/en/`, `/ko/`, six detail pages. Confirm `paper-ko.pdf` only on `ko/paper/`, `영문만 제공` only on `ko/people/` and `ko/decision/`, language-switch hrefs preserve slug.
- [ ] **Step 3:** Stop the server.

---

### Task 5: Create GitHub repo, enable Pages, push

- [ ] **Step 1:** `gh repo create sgjlee0520/trajectories-site --public --source ~/trajectories-site --remote origin --push`
- [ ] **Step 2:** Enable Pages on `main` `/` (root).
- [ ] **Step 3:** `curl -sI https://sgjlee0520.github.io/trajectories-site/` until 200 (Pages can take a minute). Confirm `/en/` and `/ko/` are 200.

# Trajectories PDF site — Design

**Date:** 2026-08-24
**Status:** Approved, pending implementation plan

## 1. Purpose

A public, bilingual (English / Korean) website that lists the four current study PDFs and opens each on its own page with the PDF embedded. Hosted on GitHub Pages from a new dedicated repository.

This is a reading surface for the papers. It is not an app, not a results dashboard, and not a replacement for the `trajectories` research repo.

### In scope

- Four PDFs: `paper.pdf`, `paper-ko.pdf`, `people.pdf`, `decision.pdf`
- English and Korean chrome (headers, language switch, back, download, English-only note)
- Numbered contents homepage
- Detail pages where the PDF fills the window under a thin bar
- GitHub Pages at `https://sgjlee0520.github.io/trajectories-site/`

### Out of scope

- Translating `people.pdf` or `decision.pdf`
- Archive / superseded interim reports
- Search, filters, dark mode, analytics, comments, CMS
- Build tools, frameworks, npm
- Custom domain
- Reciting the 9.0-year headline on the homepage

## 2. Architecture

New public repo `trajectories-site`. GitHub Pages serves the `main` branch from the repository root. No Jekyll (`touch .nojekyll`).

The `trajectories` repo remains the source of truth for the PDFs. This site copies them; it does not hotlink. When papers are rebuilt, copy the four files into `pdfs/` again.

```
trajectories-site/
  index.html
  404.html
  .nojekyll
  css/site.css
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
  README.md
```

Root `index.html` is a language redirect only: if `navigator.language` starts with `ko`, go to `ko/`; otherwise `en/`. A `<noscript>` pair of links covers no-JS.

Because Pages is served from a project site (`/trajectories-site/`), every internal URL is relative. Never use absolute `/en/` paths.

### Document map

| # | Slug | English PDF | Korean PDF | Korean list label |
|---|---|---|---|---|
| 01 | `paper` | `pdfs/paper.pdf` | `pdfs/paper-ko.pdf` | 첫 성과까지 얼마나 걸리는가 |
| 02 | `people` | `pdfs/people.pdf` | same file | 사람들 |
| 03 | `decision` | `pdfs/decision.pdf` | same file | 이 연구가 말해 줄 수 있는 것과 없는 것 |

English list titles are the PDF titles:

1. How Long Before the First Hit?
2. The People
3. What This Study Can and Cannot Tell You

On `ko/people/` and `ko/decision/`, show the note **영문만 제공** in the bar next to Download. Do not show that note on English pages or on `ko/paper/`.

## 3. Pages

### Homepage (`en/index.html`, `ko/index.html`)

Numbered contents. No blurbs.

English homepage:

```
Trajectories                         English  한국어
─────────────────────────────────────────────
01  How Long Before the First Hit?
02  The People
03  What This Study Can and Cannot Tell You
```

Korean homepage uses the same numbers and the Korean titles from the document map (첫 성과까지 얼마나 걸리는가 / 사람들 / 이 연구가 말해 줄 수 있는 것과 없는 것). Language switch reads `English  한국어` on both sites.

- Site name is the word `Trajectories` on both languages (not translated).
- Active language is plain text; the other language is a link to the sibling page (`../ko/` or `../en/`).
- Each row is one link to `paper/`, `people/`, or `decision/`. Numbers are `01` `02` `03`, not decorative icons.
- `html lang` is `en` or `ko`.

### Detail page

One thin top bar, PDF fills the rest of the viewport.

```
← Trajectories     01  How Long Before the First Hit?     English  한국어  ·  Download
────────────────────────────────────────────────────────────────────────────────────
[ iframe: PDF ]
```

- Back control is a text link to `../` (the language homepage). Label: `Trajectories` with a leading `←`.
- Title in the bar is `{number}  {title in the current language}`.
- Language switch keeps the same slug (`../ko/paper/` ↔ `../en/paper/`).
- Download is a text link to the PDF with `download` and the filename. That link is the fallback when the iframe is blank (common on mobile Safari). Do not add a second message under the iframe — it would steal height from the PDF.
- `<iframe>` `src` is the language-correct PDF, `title` is the document title, no border. The bar is a fixed 48px; the iframe is `calc(100vh - 48px)`.

### 404

Plain page, same fonts. “Not found.” / “없는 페이지입니다.” plus links to `en/` and `ko/`.

## 4. Visual design

Minimal. Light only. System fonts. No Google Fonts, no icon fonts, no emoji, no shadows, no cards, no hero.

| Token | Value |
|---|---|
| Background | `#FFFFFF` |
| Text | `#111111` |
| Muted | `#64748B` |
| Rule | `#111111` 1px under the top bar |
| Font | `system-ui, -apple-system, "Apple SD Gothic Neo", "Malgun Gothic", sans-serif` |
| Body size | 16px, line-height 1.5 |
| Max width on homepage | 40rem, centered, spacious vertical rhythm |
| Detail bar | full width, padding ~12px 16px |
| Motion | none, except 150ms color change on link hover; honor `prefers-reduced-motion` |

Links: underline on hover and on focus. Visible focus ring (`outline: 2px solid #111`). Tap targets ≥ 44px height on the numbered rows and bar links.

No JS except the root language redirect.

## 5. Error handling

- Missing PDF: the iframe fails closed; the Download link and the “if it does not display” line are the recovery.
- Unknown path: GitHub Pages `404.html`.
- Language switch never 404s: every English slug has a Korean twin.

## 6. Testing

No unit-test framework. Before shipping:

1. `python3 -m http.server` from the site root. Open `/en/`, `/ko/`, each of the six detail pages, and a nonsense path.
2. Confirm `ko/paper/` loads `paper-ko.pdf` and the other Korean pages load the English PDFs with **영문만 제공**.
3. Confirm language switch preserves slug.
4. Confirm Download starts the file.
5. Narrow viewport (~375px): bar remains usable, rows are ≥ 44px, iframe has the download fallback.
6. Keyboard: Tab through homepage and a detail bar; focus ring visible.

After Pages is on: hit the live `github.io` URLs once.

## 7. Shipping

1. Create public repo `sgjlee0520/trajectories-site`.
2. Copy the four PDFs from `trajectories/analysis/` (decision from `analysis/personal/`).
3. Enable GitHub Pages: `main`, `/` (root).
4. Site README states that PDFs are copies, source is `sgjlee0520/trajectories`, and how to refresh `pdfs/`.

The research repo README may later link the site; that change is optional and not required for the site to ship.

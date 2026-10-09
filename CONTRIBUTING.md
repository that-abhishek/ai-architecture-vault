# How the vault is laid out

This is the working standard for adding a part. Visitors don't need it; the [README](README.md) is for them.

## Folders

```
README.md                 generated: start-here text and the table of parts
CONTRIBUTING.md           this file
scripts/build_readme.py   builds README.md and every parts/*/README.md from meta.json
parts/
  NN-cover-name/          one folder per published reel
    README.md             generated: the reader's landing page
    canvas.jpg            the whiteboard (canvas.png is fine too)
    <code>.py             runnable reference code, if the part has any (stdlib only)
    script.md             full breakdown and what was said on camera
    _production/
      meta.json           source of truth for both READMEs, plus the publishing fields
      cue-cards.md
      captions.srt
      canvas_reference.svg
      reel_cover.png, reel_outro.png
      master_cut.mov      (or .mp4)
_drafts/<working-slug>/   unpublished parts (git-ignored)
raw/<NN-cover-name>/      takes, screen recordings, audio fixes (git-ignored)
```

## Folder names

`NN-cover-name`: the two-digit part number, then the reel's cover title in lower-case kebab case, so a viewer can match the folder to the reel they saw. Drop punctuation and currency signs: "PAID TWICE. KEY AND ALL." becomes `16-paid-twice`, "$33,000 TO SAY YES" becomes `15-33000-to-say-yes`. Keep it under about 30 characters. Once a part is published, never rename its folder: GitHub doesn't redirect, and the Buffer scheduler matches posts by this name.

## meta.json fields the READMEs read

| Field | What goes in it |
|---|---|
| `part` | integer, cumulative across both tracks |
| `name` | the cover title in title case, e.g. `Paid Twice. Key and All.` |
| `slug` | the folder name, exactly |
| `old_slug` | only for parts that existed before the Oct 2026 restructure |
| `track` | `engineering` or `product` |
| `published` | `YYYY-MM-DD` of the Instagram post |
| `reel_url` | the Instagram reel link |
| `question` | one line, the question the reel answers, ending in `?` |
| `problem` | two sentences at most: the concrete case from the hook |
| `points_heading` | `The three rules` for current parts |
| `points` | the rules as posted, each general first and pinned to the case |
| `code` | `{"file", "run", "what"}`; `run` is `null` for a template |
| `stands_on` | `{"part": N, "why": "..."}` or `null` |
| `formula` | optional, LaTeX without `$$` |
| `format` | `early` only for Parts 01–08 (collapsed in the README) |

The publishing fields (`title`, `badge`, `cover_title`, `caption`, `keywords`, `experiment`, `alt_text`, `runtime`, `sources`) stay where they are; the Buffer scheduler reads `title` and `caption`.

## Adding a part

1. Move the draft from `_drafts/<working-slug>/` to `parts/NN-cover-name/`, with production files in `_production/`.
2. Fill the README fields in `_production/meta.json`.
3. `python3 scripts/build_readme.py`, then open the part's README on GitHub after pushing to check the canvas renders.
4. Commit everything except `raw/`, `_drafts/` and `_to_delete/` (already ignored).

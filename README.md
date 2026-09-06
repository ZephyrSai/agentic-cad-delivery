# Prompt to Drawing Set

A 36-sheet deck on automating construction design delivery with agentic AI — laid out as a drawing set, with title blocks, sheet numbers and ISO 19650 status codes.

**Live:** https://zephyrsai.github.io/agentic-cad-delivery/

## What it covers

| Part | Sheets | Content |
| --- | --- | --- |
| A — the process | `PR-100` … `PR-107` | 100 numbered steps from brief to as-built, GCC authority overlay, 9 parameter classes, the 7-layer verification gauntlet |
| B — the framework | `TH-200` … `AR-306` | Why literal prompt-to-CAD fails, the Project Parameter Graph, reference architecture, 25 agents, the role each one assumes and what it absorbs, the CAD operation set |
| C — the POC | `PL-400` … `PL-409` | 22-week plan, four gates, manpower split, minimum integrations, software and SDK procurement, INR costing, basis and limits of the estimate |
| D — the exposure | `RS-500` … `RD-601` | Risk register, build vs buy, roadmap, decisions required |

## Controls

Arrow keys, space, `J`/`K` to move; `Home`/`End` for first and last; `I` for the sheet index; `S` for scroll view; `?` for the full list. On touch devices, swipe left and right — wide tables and the programme bar pan inside their own frame instead.

## Repository layout

- `index.html` — the standalone build served by Pages
- `src/deck.artifact.html` — the source, authored for the Claude artifact runtime (no document shell)
- `build.py` — wraps the source into `index.html`, adding the doctype, viewport meta and reset that the artifact runtime otherwise supplies

Edit `src/deck.artifact.html`, then:

```bash
python3 build.py
```

## Note on the numbers

Every commercial figure in the deck is an estimate, not a quotation — see sheet `PL-409` for the basis and its limits. The cost and timeline cover a proof of concept: core integration of agentic AI into CAD and rule-based generation for one workflow, two at the outside. Licensing, SDK and API pricing is a current best guess and will be revised.

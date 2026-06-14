---
name: boya-monthly-sales-report
description: Monthly BOYA Sales Report + Dealer Briefing — runs on the 5th of each month at 10 AM
---

You are running a scheduled monthly task for Kenny (kennkai55@gmail.com). Today is the 5th of the month — time to generate the Monthly BOYA Sales Report and Monthly Dealer Briefing.

---

## STEP 1 — Read local instructions first

Before doing anything else, read:
/Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/CLAUDE.md

Follow ALL rules in that file, especially:
- Confidential by default — all sales data is strictly internal
- Do NOT overwrite existing files — always use date-suffixed filenames
- Flag assumptions clearly when data is partial or missing

---

## STEP 2 — Identify the reporting period

The reporting period is the PREVIOUS calendar month relative to today's date at runtime.
- Example: if today is June 5, 2026 → report covers May 2026
- Example: if today is May 5, 2026 → report covers April 2026

---

## STEP 3 — Read all BOYA sales data files

Read ALL of the following files before generating anything:

**BY Sales Data:**
- /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/BY Sales Data/Sales by SKU (QTY).md
- /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/BY Sales Data/Sales by SKU (Value).md
- /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/BY Sales Data/Sales by Dealer (QTY).md
- /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/BY Sales Data/Sales by Dealer (Value).md
- /Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/BY Sales Data/Categorized Sales Data (By Dealer Type).md

---

## STEP 4 — Generate Part 1: Monthly Sales Report

**Format rules (strict):**
- Output format: .md only
- Maximum length: 250 lines total across both parts combined — be concise, use tight tables, no padding
- Use markdown tables for all data; avoid long prose blocks

Structure (stay within the 250-line cap across both parts combined):

1. **Executive Summary** — 2–3 sentences max
2. **Total Revenue (Sell-in)** — single table: current month vs previous month (MoM Δ) vs same month prior year (YoY Δ) if available
3. **Top 5 SKUs** — one combined table: QTY rank + Value rank + MoM Δ
4. **Slow Movers** — bottom 5 SKUs by QTY; flag any with 2+ months of low volume
5. **Top 10 Dealers by Value** — table with MoM Δ and cumulative contribution %
6. **Channel Mix** — dealer type breakdown table (% share + MoM shift)
7. **Key Insights** — 4–5 bullet points, strictly data-grounded
8. **Assumptions & Limitations** — bullet list; flag missing months or partial data

---

## STEP 5 — Generate Part 2: Monthly Dealer Briefing

**Format rules (strict):**
- Output format: .md only
- Included in the same 250-line cap as Part 1 — keep this section tight (aim for ~80 lines max)

Structure:

1. **Month at a Glance** — 2-line headline
2. **Top 5 Dealers** — table with MoM Δ indicator (↑ / ↓ / →)
3. **Growth Stars** — max 3 dealers; flag for reward/upsell
4. **At-Risk / Dormant** — no purchase in reporting month or MoM drop >30%; flag for re-engagement
5. **SKUs to Push** — 3–5 SKUs with growing dealer demand or inventory push opportunity
6. **Action Items** — 4 max, prioritized, concrete

---

## STEP 6 — Save both outputs as .md files

Save both files to:
/Users/ken/Documents/KEN Work Stack/SRBY-WorkVault/04 - Sales Data/BOYA/Monthly Reports/

**Filenames** (use today's actual date at runtime):
- Sales Report: BY - Sales Report - YYYY-MM-DD.md
- Dealer Briefing: BY - Dealer Briefing - YYYY-MM-DD.md

Do NOT overwrite existing files. If a file with the same name already exists, append _v2.

---

## STEP 7 — Post a chat summary

After saving, post a brief summary:
- Reporting period covered
- Total sell-in revenue + MoM change (one line)
- Top SKU and top dealer of the month
- Paths of both saved files
- Any data gaps or flags for Kenny
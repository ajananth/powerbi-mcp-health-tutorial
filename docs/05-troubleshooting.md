# 05 — Troubleshooting

**What this is:** the failures people actually hit, and how to get past them.
Scan the headings for your symptom.

---

## The MCP server doesn't appear in the tool list

- Reload VS Code, or restart the CLI session
- Confirm the extension installed from publisher **analysis-services**
- In VS Code, confirm Copilot Chat is in **Agent mode** — tools aren't available
  in ask mode
- Run `/skills` and confirm `semantic-model-authoring` is listed
- If your Copilot access comes through an organisation or enterprise, MCP may be
  disabled by policy. Microsoft covers this in the
  [server README](https://github.com/microsoft/powerbi-modeling-mcp#visual-studio-code).
  It doesn't apply to personal Copilot plans.

---

## The agent can't find the Power BI Desktop file

- Confirm Power BI Desktop is **open** with the file loaded — the server connects
  to the running process, not the file on disk
- Use the file name as it appears in the Desktop title bar
- If you have several Desktop instances open, close the ones you don't need
- Try the built-in prompt `ConnectToPowerBIDesktop`

---

## Changes aren't showing in Power BI Desktop

Model changes made through the MCP server may not appear until Desktop refreshes
its view. Switch to Model view and back, or reload the file.

---

## The agent produced something wrong

Expected occasionally. Microsoft's own guidance is that the underlying LLM "may
produce unexpected or inaccurate results, which could lead to unintended changes."

**Recovery:**

```bash
git checkout .
```

This is why the baseline commit matters.

**Reducing the odds:**

- Give one instruction per prompt rather than batching several
- Ask the agent to explain its plan before executing on complex changes
- Use `--readonly` when exploring

---

## Time intelligence returns blank

Almost always the date table.

- Confirm `DimDate` is **marked as a date table** using the `Date` column
- Confirm `DimDate[Date]` is a **Date** type, not text
- Confirm the relationship from `DimDate` to `FactEncounter` on `DateKey` exists
  and is active
- Confirm `DimDate` covers the full range of dates in `FactEncounter` — the sample
  data runs 1 July 2024 to 30 June 2026

---

## Measures return unexpected numbers

- `Total Encounters` should be exactly **6,000**
- If it's higher, you may have loaded a CSV twice
- If it's lower, check that no filters are applied to the visual
- If a percentage measure returns a whole number, check the format string was
  applied

---

## Relationships were created in the wrong direction

Ask the agent to fix it rather than editing by hand — it keeps the model and your
conversation in sync:

```
Check all relationships in this model and make sure they are single-direction,
one-to-many from each dimension table to FactEncounter.
```

---

## Authentication prompts keep appearing

For local Desktop work, no cloud authentication should be needed. If you're
being prompted, check that you connected to the model in Power BI Desktop rather
than to a workspace.

---

## Starting over

This assumes you made the baseline commit in
[02 — Setup](02-setup.md). `git clean -fd` deletes untracked files, so check
`git status` first if you're unsure.

```bash
git checkout .
git clean -fd
```

Then reopen the PBIP in Power BI Desktop and reconnect.

---

## Still stuck

- [Troubleshooting guide in the Microsoft repository](https://github.com/microsoft/powerbi-modeling-mcp/blob/main/TROUBLESHOOTING.md)
- [Open an issue on the Microsoft repository](https://github.com/microsoft/powerbi-modeling-mcp/issues)

Issues with *this tutorial* — the data, the prompts, the documentation — belong on
this repository instead.

---

Prev: [04 — Prompt reference](04-prompt-reference.md)

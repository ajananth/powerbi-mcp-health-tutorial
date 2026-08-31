# 02 — Setup

**Where you are:** prerequisites checked. **What you'll have at the end:** the
tooling installed, the data loaded, and the agent connected to your model.

Two things to set up: the tooling, and the Power BI file the agent will work on.

---

## Part A — Install the tooling

Four steps, in this order. Steps 1–2 are in VS Code, step 3 is in a terminal.

### 1. Install the GitHub Copilot Chat extension

Open **Extensions** (`Ctrl+Shift+X`), search for **GitHub Copilot Chat**, install
it, and sign in.

### 2. Install the Power BI Modeling MCP extension

1. In **Extensions**, search for **Power BI Modeling MCP** — publisher
   **analysis-services**
2. Click **Install**
3. Reload VS Code
4. Open Copilot Chat and switch to **Agent mode** — tools aren't available in ask
   mode
5. Confirm `powerbi-modeling-mcp` appears in the tool list

### 3. Install the skills bundle

From a terminal:

```bash
copilot plugin marketplace add microsoft/skills-for-fabric
copilot plugin install powerbi-authoring@fabric-collection
```

These two commands are what registers the skills. Install them through the CLI
even though you'll be working in VS Code — VS Code picks them up from there.

### 4. Confirm the skills loaded

Start GitHub Copilot CLI and run:

```
/skills
```

You should see `semantic-model-authoring` in the list.

---

## Other ways to install

You don't need these if you followed Part A.

### Running entirely in the CLI

The two commands in step 3 are all you need — the `powerbi-authoring` plugin
registers the Power BI Modeling MCP Server automatically. Skip VS Code and prompt
the agent directly from the CLI.

### Manual registration (any MCP client)

Requires Node.js. Add to your MCP configuration file:

```json
{
  "servers": {
    "powerbi-modeling-mcp": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@microsoft/powerbi-modeling-mcp@latest", "--start"]
    }
  }
}
```

> [!NOTE]
> VS Code expects the server under a `servers` key, as shown. Most other MCP
> clients use `mcpServers` instead — check your client's documentation.

---

## Useful settings

Configure in VS Code User Settings (search `@ext:Microsoft.powerbi-modeling-mcp`)
or via `args` in your MCP registration.

| Option | Default | Effect |
| --- | --- | --- |
| `--readwrite` | On | Writes enabled, with a confirmation prompt per database |
| `--readonly` | — | Safe mode. Blocks all writes. **Good for a first pass.** |
| `--skipconfirmation` | — | Auto-approves writes. Smoother, riskier. Only with backups. |

### Confirmation prompts

The server implements the MCP **Elicitation** protocol and asks for approval:

- before the first modification to a semantic model
- before the first query against a semantic model

Worth noticing rather than clicking past — it's the governance control in this
workflow.

---

## Part B — Prepare the Power BI file

### 1. Load the data

1. Open Power BI Desktop
2. **Get Data → Text/CSV**
3. Load all five files from `data/`:
   - `FactEncounter.csv`
   - `DimPatient.csv`
   - `DimProvider.csv`
   - `DimDepartment.csv`
   - `DimDate.csv`

> [!IMPORTANT]
> **Don't create relationships**, and turn off autodetect if it fires. The tables
> should be flat and disconnected — building the star schema is the first thing
> you'll ask the agent to do.

To disable autodetect: **File → Options and settings → Options → Current File →
Data Load** → uncheck *Autodetect new relationships after data is loaded*.

### 2. Check the data types

Confirm these came through correctly, since the model depends on them:

| Column | Expected type |
| --- | --- |
| `DimDate[Date]` | Date |
| `DimDate[DateKey]` | Whole number |
| `FactEncounter[DateKey]` | Whole number |
| `FactEncounter[TotalCost]` | Decimal number |
| `FactEncounter[ReimbursedAmount]` | Decimal number |
| `FactEncounter[LengthOfStayDays]` | Whole number |

### 3. Save as a project

**File → Save as → Power BI project (.pbip)** — name it `HealthAnalytics`.

PBIP gives you a folder structure with the model as readable TMDL files, which
makes Git diffs meaningful and lets the agent work with definitions on disk.

### 4. Commit a baseline

```bash
git init
git add .
git commit -m "Baseline: flat tables, no relationships"
```

This is your undo button. Take it.

---

## Part C — Verify the connection

With Power BI Desktop still open, prompt the agent:

```
Connect to 'HealthAnalytics' in Power BI Desktop
```

Approve the elicitation prompt when it appears.

Then confirm the tools are live:

```
Tell me with some examples what I can do with powerbi-modeling-mcp
```

If the agent lists modelling operations, you're ready.

---

Prev: [01 — Prerequisites](01-prerequisites.md) · Next: [03 — Build the model](03-build-the-model.md)

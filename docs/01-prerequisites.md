# 01 — Prerequisites

**Where you are:** the start. **What you'll have at the end:** everything
installed and the admin questions settled, ready to set up the tooling.

Work through this before starting. The install takes minutes; the admin settings
can take days if you need to raise a request, so check those first.

---

## Software

| Requirement | Notes |
| --- | --- |
| **Power BI Desktop** | Latest version. Hosts the model the agent connects to. |
| **Visual Studio Code** | Where you'll run the modelling session. Needs the GitHub Copilot Chat extension. |
| **GitHub Copilot CLI** | Used to install the skills bundle. |
| **Node.js 18 or later** | Only needed if you register the MCP server manually via NPX. The VS Code extension ships the server itself. |
| **Git** | Recommended — see the baseline commit advice. |

### Choosing a client

You need **both** the CLI and VS Code, and they do different jobs:

| Tool | Its job |
| --- | --- |
| **GitHub Copilot CLI** | Installs the skills bundle — two commands, once |
| **Visual Studio Code** | Runs the modelling session against Power BI Desktop |

Microsoft documents the skills bundle as "optimized for GitHub Copilot CLI" with
cross-tool compatibility shims for VS Code Copilot, Claude Code, Cursor,
Codex/Jules, and Windsurf. Installing through the CLI is what registers the
skills; VS Code then picks them up.

You *can* run the whole tutorial in the CLI instead, without VS Code. This guide
follows the VS Code route because it's more comfortable alongside your PBIP files,
and it's the path these instructions were tested on.

> [!NOTE]
> The MCP server is a **local** process. It connects to the Analysis Services
> instance inside Power BI Desktop on the same machine, or reads TMDL files from
> local disk. Cloud-hosted agents — Copilot on github.com, the mobile app — have
> no path to either and can't be used.

---

## Licences and permissions

This tutorial runs entirely against Power BI Desktop on your own machine:

- No Power BI capacity required
- No Fabric items required
- No tenant settings required

---

## Understanding the servers

Easy to conflate, so worth getting straight:

| Server | Purpose | Runs |
| --- | --- | --- |
| **Power BI Modeling MCP** | Build and change semantic models | Locally |
| **Remote Power BI MCP** | Chat with data — generates and runs DAX | Microsoft-hosted |

This tutorial uses the **Modeling MCP server** only.

---

## Safety checklist

Before letting an agent write to a model:

- [ ] Model backed up
- [ ] Git baseline committed
- [ ] Considered `--readonly` for the first pass

---

Next: [02 — Setup](02-setup.md)
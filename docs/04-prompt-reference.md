# 04 — Prompt reference

**Where you are:** the model is built. **What this is:** every prompt from the
tutorial in one place, for re-runs and live demos.

Every prompt from the tutorial, without commentary. Copy and paste in order.

For context on what each one does, see
[03 — Build the model](03-build-the-model.md).

---

### 1. Connect

```
Connect to 'HealthAnalytics' in Power BI Desktop
```

### 2. Inspect and recommend

```
Describe the tables and columns in this model, and tell me what kind of
star schema you'd recommend based on what you find.
```

### 3. Star schema

```
Create relationships for a star schema: FactEncounter is the fact table,
joined to DimPatient on PatientKey, DimProvider on ProviderKey,
DimDepartment on DepartmentKey, and DimDate on DateKey.
Set all as single-direction, one-to-many from dimension to fact.
Mark DimDate as the date table using the Date column.
```

### 4. Measures

```
Create these measures in a new table called '_Measures', formatted appropriately:
Total Encounters, Total Cost, Average Length of Stay, 30-Day Readmission Rate
as a percentage, Average Wait Time, Average Satisfaction Score,
Cost Recovery Rate as reimbursed over total cost, and Emergency Encounters.
```

### 5. Calculation group

```
Create a calculation group called 'Time Intelligence' with items for
Current, Prior Year, Year-over-Year change, Year-over-Year percent,
and Financial Year to Date, using the DimDate table.
```

### 6. Documentation descriptions

```
Add descriptions to every table, column, and measure explaining its purpose
in business-friendly language, and for measures explain the DAX logic in plain terms.
```

### 7. Row-level security

```
Create a security role called 'State Manager' that filters DimDepartment
to a single state, and show me how to test it.
```

### 8. Validate

```
Write and run a DAX query showing readmission rate and average length of stay
by service line, sorted by readmission rate descending.
```

### 9. Generate documentation

```
Generate a Markdown document with complete documentation for this semantic model.
Use a mermaid diagram for the relationships, document each measure with its DAX
and business logic, and document the row-level security filters.
```

---

Prev: [03 — Build the model](03-build-the-model.md) · Next: [05 — Troubleshooting](05-troubleshooting.md)

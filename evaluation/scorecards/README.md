# Evaluation Scorecards

Scorecards are machine-readable JSON summaries of human-reviewed before/after reports.

Each registered report in `evaluation/reports/index.yaml` must point to one scorecard. The scorecard repeats the report decision, fixtures, blockers, per-criterion scores, fixture averages, overall averages, and validation result so trends can be aggregated without parsing Markdown tables.

Run:

```powershell
python .\scripts\validate-scorecards.py
```

The validator checks JSON syntax, report-index consistency, fixture references, rubric criteria, score ranges, averages, deltas, and validation-result fields.

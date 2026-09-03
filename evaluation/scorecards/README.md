# Evaluation Scorecards

Scorecards are machine-readable JSON summaries of human-reviewed before/after reports.

Current scorecards summarize medium-confidence local reviewer simulations unless a report explicitly says otherwise.

Each registered report in `evaluation/reports/index.yaml` must point to one scorecard. The scorecard repeats the report decision, fixtures, blockers, per-criterion scores, fixture averages, overall averages, and validation result so trends can be aggregated without parsing Markdown tables.

`summary.json` is the generated aggregate across registered scorecards. Regenerate it after changing report scorecards:

```powershell
python .\scripts\summarize-scorecards.py --output .\evaluation\scorecards\summary.json
```

Run:

```powershell
python .\scripts\validate-scorecards.py
python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json
```

The validators check JSON syntax, report-index consistency, fixture references, rubric criteria, score ranges, averages, deltas, validation-result fields, and aggregate summary freshness.

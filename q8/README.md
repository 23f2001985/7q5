# Equipment Efficiency – 2024 Data Story

**Email (verification): 23f2001985@ds.study.iitm.ac.in**

## Dataset
- **Equipment Efficiency Rate – 2024 Quarterly Data**
  - Q1: 71.25
  - Q2: 72.08
  - Q3: 78.76
  - Q4: 82.83
- **Average (required): 76.23**
- **Industry Target:** 90

## Visualizations
- `trend_vs_target.png`: Quarterly efficiency trend with the 90 benchmark line.

## Key Findings
1. **Consistent upward trend:** 71.25 → 82.83 across Q1→Q4 (+11.58 points total).
2. **Acceleration in second half:** Q2→Q3 improved by +6.68; Q3→Q4 by +4.07.
3. **Gap to target remains:** Q4 is **7.17 points** below the industry target of 90.
4. **Average efficiency is 76.23**, well under the 90 target, confirming sustained under-performance despite improvements.

## Business Implications
- **Underutilized assets:** The shortfall vs. target suggests latent downtime, suboptimal scheduling, or maintenance lag.
- **Cost and throughput impact:** Every point below target translates to reduced throughput and higher unit costs.
- **Operational risk:** Trend is positive, but current performance leaves little buffer for seasonal spikes or outages.

## Recommendations (Action Plan to Reach 90)
**Primary solution: implement predictive maintenance program.**
- Deploy condition-based monitoring (vibration, temperature, oil analysis) on critical assets.
- Train ML models to predict failure probability and remaining useful life; schedule interventions proactively.
- Establish a spare-parts readiness policy based on predicted risk windows.
- Integrate maintenance windows into production planning to minimize downtime.
- Define KPIs: MTBF, MTTR, planned vs. unplanned downtime, and weekly efficiency target trajectories.

**Supporting initiatives**
- **Root-cause analysis (RCA):** Pareto of top downtime causes; eliminate chronic issues.
- **Operator enablement:** Standard work, quick reference guides, focused re-training on the bottleneck lines.
- **Short interval control (SIC):** Daily huddles with leading indicators (availability, minor stops) to course-correct.
- **Process optimization:** SMED to cut changeover time; line balancing for peak shifts.
- **Data quality:** Ensure sensor calibration, unify asset IDs, and centralize logs for reliable analytics.

## Reproducible Analysis
Run:
```bash
python analysis.py
```

This will compute summary stats and regenerate `trend_vs_target.png`.

## Files in this PR
- `equipment_efficiency_2024.csv`
- `analysis.py`
- `trend_vs_target.png`
- `README.md`

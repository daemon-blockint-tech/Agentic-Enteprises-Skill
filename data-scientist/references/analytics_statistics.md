# Analytics & Statistics

## Hypothesis Testing

### Test Selection Guide

| Data Type | Comparison | Test |
|---|---|---|
| Continuous, normal, 2 groups | Independent | Two-sample t-test |
| Continuous, normal, 2 groups | Paired | Paired t-test |
| Continuous, non-normal, 2 groups | Independent | Mann-Whitney U |
| Continuous, >2 groups | Independent | ANOVA (parametric), Kruskal-Wallis (non-param) |
| Categorical, 2 categories | Proportions | Z-test for proportions |
| Categorical, >2 categories | Independence | Chi-square test |
| Correlation | 2 continuous | Pearson (linear), Spearman (monotonic) |

**Always check assumptions:**
- Independence of observations
- Normality (for parametric tests; use Shapiro-Wilk or Q-Q plot)
- Homogeneity of variance (Levene's test)
- Sample size (central limit theorem helps for n > 30)

### Python Examples

```python
from scipy import stats

# Two-sample t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

# Mann-Whitney U (non-parametric)
u_stat, p_value = stats.mannwhitneyu(group_a, group_b, alternative='two-sided')

# Chi-square test
contingency = pd.crosstab(df['category'], df['outcome'])
chi2, p_value, dof, expected = stats.chi2_contingency(contingency)

# Effect size (Cohen's d)
def cohens_d(x, y):
    nx, ny = len(x), len(y)
    dof = nx + ny - 2
    return (np.mean(x) - np.mean(y)) / np.sqrt(((nx-1)*np.std(x, ddof=1)**2 + (ny-1)*np.std(y, ddof=1)**2) / dof)
```

## A/B Testing

### Experiment Design Checklist

- [ ] Primary metric defined (single metric to optimize)
- [ ] Secondary metrics identified (guardrails, not for decision)
- [ ] Minimal Detectable Effect (MDE) set with business input
- [ ] Sample size calculated (power = 0.8, alpha = 0.05)
- [ ] Randomization unit matches analysis unit (usually user)
- [ ] Duration covers at least 1 full business cycle
- [ ] No confounding launches during experiment

### Sample Size Calculation

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# For proportions (conversion rate)
baseline = 0.10  # 10% conversion
mde = 0.02       # Detect 12% vs 10%
effect_size = proportion_effectsize(baseline + mde, baseline)

power_analysis = NormalIndPower()
sample_size = power_analysis.solve_power(
    effect_size=effect_size,
    alpha=0.05,
    power=0.8,
    ratio=1
)
# sample_size per group
```

### Analysis Best Practices

1. **Intent-to-treat**: Analyze all randomized users, even if they didn't engage
2. **Check invariant metrics**: Confirm randomization worked (e.g., device split unchanged)
3. **Use proper statistical test**: t-test for continuous, z-test for proportions
4. **Confidence intervals**: Report with estimates, not just p-values
5. **Segment analysis**: Pre-defined segments only; avoid data dredging
6. **Multiple comparisons**: Bonferroni or FDR correction if testing many metrics

### Early Stopping

**Avoid peeking** without correction:
- Fixed-horizon testing: Decide duration upfront, don't stop early
- Sequential testing: Use proper sequential boundaries (e.g., Group Sequential, Always Valid P-values)
- Bayesian monitoring: Credible intervals, stop when decisive

## Causal Inference

### Methods by Context

| Method | Requires | Best For |
|---|---|---|
| Randomized experiment | Control over treatment assignment | Gold standard when feasible |
| Difference-in-differences | Panel data, parallel trends | Policy changes, market rollouts |
| Propensity score matching | Observational, confounders observed | Treatment non-random but explainable |
| Instrumental variables | Valid instrument (affects treatment, not outcome directly) | Endogeneity, omitted variable bias |
| Regression discontinuity | Sharp cutoff in treatment assignment | Scholarship thresholds, age cutoffs |
| Synthetic control | Single treated unit, many control units | Market-level interventions |

### Difference-in-Differences Example

```python
import statsmodels.formula.api as smf

# Panel data with treated and post indicators
model = smf.ols('outcome ~ treated * post + entity_fe + time_fe',
                data=panel_data).fit()
# Coefficient on treated:post is the ATT
```

### Propensity Score Matching

```python
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

# Estimate propensity scores
ps_model = LogisticRegression().fit(X_confounders, treatment)
propensity_scores = ps_model.predict_proba(X_confounders)[:, 1]

# Match treated to control
nn = NearestNeighbors(n_neighbors=1).fit(propensity_scores[treatment==0].reshape(-1, 1))
distances, indices = nn.kneighbors(propensity_scores[treatment==1].reshape(-1, 1))
```

## Exploratory Data Analysis (EDA)

### Systematic EDA Checklist

1. **Structure**: Rows, columns, types, missingness pattern
2. **Distributions**: Histograms, boxplots, summary stats
3. **Relationships**: Correlation matrix, pairplots, groupby aggregations
4. **Anomalies**: Outliers, impossible values, data entry errors
5. **Temporal**: Trends, seasonality, gaps in time series
6. **Geographic**: Spatial distributions if location data exists

### Missing Data Strategy

| Pattern | Strategy |
|---|---|
| MCAR (Missing Completely at Random) | Any imputation valid; listwise deletion unbiased |
| MAR (Missing at Random) | Model-based imputation (MICE, regression) |
| MNAR (Missing Not at Random) | Model the missingness mechanism; be cautious |

**Imputation methods:**
- Simple: mean, median, mode
- Advanced: KNN imputation, iterative imputer (MICE), MissForest
- Domain: business rule-based (e.g., "no purchase → spend = 0")

## Statistical Power & Errors

| Decision ↓ / Reality → | Null True | Alternative True |
|---|---|---|
| Fail to reject null | Correct (1 - α) | Type II error (β) |
| Reject null | Type I error (α) | Correct (1 - β = power) |

**Practical significance vs statistical significance:**
- p < 0.05 with 1M samples can detect trivial effects
- Always report effect sizes and confidence intervals
- Ask: "Is this difference meaningful for the business?"

## Bayesian Basics

**When to use Bayesian methods:**
- Small sample sizes (priors help regularize)
- Sequential updating (new data refines beliefs)
- Hierarchical structure (users within segments)
- Need full posterior distribution, not just point estimate

**Bayesian A/B test:**
```python
import pymc as pm

with pm.Model() as model:
    p_a = pm.Beta('p_a', alpha=1, beta=1)
    p_b = pm.Beta('p_b', alpha=1, beta=1)
    
    obs_a = pm.Binomial('obs_a', n=n_a, p=p_a, observed=conversions_a)
    obs_b = pm.Binomial('obs_b', n=n_b, p=p_b, observed=conversions_b)
    
    diff = pm.Deterministic('diff', p_b - p_a)
    trace = pm.sample(2000)

# Probability that B is better than A
prob_better = (trace.posterior.diff > 0).mean()
```

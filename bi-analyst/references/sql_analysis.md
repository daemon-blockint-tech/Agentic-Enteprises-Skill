# Analytical SQL

## Date & Time Analysis

### Calendar Dimensions
```sql
-- Generate date spine
WITH date_spine AS (
  SELECT date_trunc('day', d) AS date_day
  FROM generate_series('2023-01-01'::date, CURRENT_DATE, '1 day'::interval) AS d
)
```

### Period-over-Period
```sql
WITH daily AS (
  SELECT date_trunc('day', order_date) AS day, SUM(amount) AS revenue
  FROM orders GROUP BY 1
)
SELECT
  day,
  revenue,
  LAG(revenue, 1) OVER (ORDER BY day) AS prev_day,
  LAG(revenue, 7) OVER (ORDER BY day) AS prev_week,
  LAG(revenue, 28) OVER (ORDER BY day) AS prev_28_day,
  revenue / NULLIF(LAG(revenue, 28) OVER (ORDER BY day), 0) - 1 AS yoy_28d
FROM daily;
```

### Year-to-Date / Rolling Windows
```sql
SELECT
  date,
  SUM(revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d,
  SUM(revenue) OVER (PARTITION BY year ORDER BY date) AS ytd_revenue,
  AVG(revenue) OVER (ORDER BY date ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS rolling_30d_avg
FROM daily_metrics;
```

## Cohort Analysis

### Retention Cohort
```sql
WITH user_first_order AS (
  SELECT user_id, MIN(order_date) AS first_order_date
  FROM orders GROUP BY 1
),
cohort_activity AS (
  SELECT
    u.user_id,
    u.first_order_date,
    o.order_date,
    DATEDIFF('month', u.first_order_date, o.order_date) AS periods_since_first
  FROM user_first_order u
  JOIN orders o ON u.user_id = o.user_id
)
SELECT
  DATE_TRUNC('month', first_order_date) AS cohort_month,
  periods_since_first,
  COUNT(DISTINCT user_id) AS active_users,
  COUNT(DISTINCT user_id) * 1.0 / FIRST_VALUE(COUNT(DISTINCT user_id)) OVER (
    PARTITION BY DATE_TRUNC('month', first_order_date) ORDER BY periods_since_first
  ) AS retention_rate
FROM cohort_activity
GROUP BY 1, 2
ORDER BY 1, 2;
```

## Funnel Analysis

### Step-by-Step Conversion
```sql
WITH events AS (
  SELECT user_id, event_name, event_timestamp,
    MIN(CASE WHEN event_name = 'signup' THEN event_timestamp END) OVER (PARTITION BY user_id) AS signup_time
  FROM event_log
)
SELECT
  COUNT(DISTINCT CASE WHEN event_name = 'signup' THEN user_id END) AS signups,
  COUNT(DISTINCT CASE WHEN event_name = 'product_view' THEN user_id END) AS viewed,
  COUNT(DISTINCT CASE WHEN event_name = 'add_to_cart' THEN user_id END) AS added_cart,
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_id END) AS purchased,
  -- Conversion rates
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_id END) * 1.0 /
    NULLIF(COUNT(DISTINCT CASE WHEN event_name = 'signup' THEN user_id END), 0) AS overall_cvr
FROM events
WHERE event_timestamp >= DATEADD('day', -30, CURRENT_DATE);
```

### Time-to-Convert
```sql
WITH first_events AS (
  SELECT user_id, MIN(CASE WHEN event_name = 'signup' THEN event_timestamp END) AS signup,
    MIN(CASE WHEN event_name = 'purchase' THEN event_timestamp END) AS purchase
  FROM event_log
  GROUP BY 1
)
SELECT
  AVG(DATEDIFF('hour', signup, purchase)) AS avg_hours_to_convert,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY DATEDIFF('hour', signup, purchase)) AS median_hours
FROM first_events
WHERE purchase IS NOT NULL;
```

## Segmentation

### RFM Analysis
```sql
WITH customer_stats AS (
  SELECT
    user_id,
    DATEDIFF('day', MAX(order_date), CURRENT_DATE) AS recency,
    COUNT(*) AS frequency,
    SUM(amount) AS monetary
  FROM orders
  GROUP BY 1
),
scored AS (
  SELECT
    user_id,
    NTILE(5) OVER (ORDER BY recency DESC) AS r_score,  -- lower recency = higher score
    NTILE(5) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC) AS m_score
  FROM customer_stats
)
SELECT
  r_score, f_score, m_score,
  COUNT(*) AS customer_count,
  CASE
    WHEN r_score >= 4 AND f_score >= 4 THEN 'Champions'
    WHEN r_score >= 3 AND f_score >= 3 THEN 'Loyal Customers'
    WHEN r_score >= 4 AND f_score <= 2 THEN 'New Customers'
    WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk'
    ELSE 'Others'
  END AS segment
FROM scored
GROUP BY 1, 2, 3;
```

## Ranking & Top N

```sql
-- Top 10 products by revenue per region
WITH ranked AS (
  SELECT
    region, product_name, SUM(revenue) AS total_revenue,
    RANK() OVER (PARTITION BY region ORDER BY SUM(revenue) DESC) AS rank
  FROM sales
  GROUP BY 1, 2
)
SELECT * FROM ranked WHERE rank <= 10;
```

## Anomaly Detection in SQL

```sql
WITH stats AS (
  SELECT
    metric_name,
    AVG(value) AS mean,
    STDDEV(value) AS stddev
  FROM daily_metrics
  WHERE date >= CURRENT_DATE - INTERVAL '90 days'
  GROUP BY 1
)
SELECT
  m.date, m.metric_name, m.value,
  ABS(m.value - s.mean) / NULLIF(s.stddev, 0) AS z_score
FROM daily_metrics m
JOIN stats s ON m.metric_name = s.metric_name
WHERE ABS(m.value - s.mean) / NULLIF(s.stddev, 0) > 3;
```

## Performance Tips

| Technique | When |
|---|---|
| `EXPLAIN` before complex queries | Always |
| Filter early in CTEs | Reduces data early |
| Avoid `SELECT *` in subqueries | Reduces IO |
| Use `UNION ALL` not `UNION` | Unless deduplication needed |
| Materialize common CTEs | If used multiple times |
| Partition on date for time filters | Enables partition pruning |
| Pre-aggregate in database | BI tools are slower than SQL |

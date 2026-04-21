def generate_report(frustration_rate, failure_rate, conversion_rate, brand_stats, patterns):

    pattern_text = "\n".join([f"- {p}" for p in patterns])

    observations = [
        "User drop-offs are commonly observed after generic or non-adaptive responses.",
        "Product suggestions do not consistently translate into engagement.",
        "Repeated queries indicate incomplete resolution within conversations."
    ]

    obs_text = "\n".join([f"- {o}" for o in observations])

    report = f"""
# AI Assistant Conversation Analysis

## Key Metrics

- Frustration Rate: {frustration_rate:.2f}
- Failure Rate: {failure_rate:.2f}
- Product Click Conversion Rate: {conversion_rate:.2f}

---

## Key Insights (Auto-Generated)

{pattern_text}

---

## Observations

{obs_text}

---

## Recommendations

- Improve intent understanding
- Avoid vague responses
- Improve product recommendation relevance
- Handle repeated queries better

---

## Brand Performance

{brand_stats.to_string(index=False)}

---

## Conclusion

The assistant performs well for basic queries but needs improvement in personalization and accuracy.
"""

    with open("../output/report.md", "w", encoding="utf-8") as f:
        f.write(report)

    print("report.md generated successfully!")
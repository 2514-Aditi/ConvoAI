from data_loader import load_data
from insights import (
    detect_frustration,
    detect_failures,
    recommendation_quality,
    brand_analysis,
    extract_key_patterns
)
from report import generate_report


def main():
    conversations, messages = load_data()

    # Apply detection
    messages = detect_frustration(messages)
    messages = detect_failures(messages)

    # Metrics
    frustration_rate = messages["frustrated"].mean()
    failure_rate = messages["failure"].mean()

    clicks, total_events, conversion_rate = recommendation_quality(messages)

    # Brand stats
    brand_stats = brand_analysis(conversations, messages)

    # AUTO insights
    patterns = extract_key_patterns(messages, conversion_rate)

    # Generate report
    generate_report(
        frustration_rate,
        failure_rate,
        conversion_rate,
        brand_stats,
        patterns
    )


if __name__ == "__main__":
    main()
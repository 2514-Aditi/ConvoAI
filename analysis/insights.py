from textblob import TextBlob

# -------------------------
# Frustration Detection
# -------------------------
def detect_frustration(messages):
    negative_words = ["not helpful", "bad", "wrong", "no", "issue"]

    def check(text):
        if not isinstance(text, str):
            return False
        text = text.lower()

        if any(word in text for word in negative_words):
            return True

        return TextBlob(text).sentiment.polarity < -0.3

    messages["frustrated"] = messages["text"].apply(check)
    return messages


# -------------------------
# Failure Detection
# -------------------------
def detect_failures(messages):
    def check(text):
        if not isinstance(text, str):
            return False
        text = text.lower()
        return "not sure" in text or "don't know" in text

    messages["failure"] = messages["text"].apply(check)
    return messages


# -------------------------
# Recommendation Quality
# -------------------------
def recommendation_quality(messages):
    events = messages[messages["messageType"] == "event"]

    clicks = events[
        events["metadata"].apply(
            lambda x: isinstance(x, dict) and x.get("eventType") == "product_view"
        )
    ]

    total_events = len(events)
    total_clicks = len(clicks)

    conversion_rate = total_clicks / total_events if total_events > 0 else 0

    return total_clicks, total_events, conversion_rate


# -------------------------
# Brand Analysis
# -------------------------
def brand_analysis(conversations, messages):
    merged = messages.merge(conversations, left_on="conversationId", right_on="_id")
    return merged.groupby("widgetId").size().reset_index(name="total_messages")


# -------------------------
# AUTO INSIGHT ENGINE (IMPROVED NATURAL STYLE)
# -------------------------
def extract_key_patterns(messages, conversion_rate):
    insights = []

    acne_count = messages["text"].str.contains("acne", case=False, na=False).sum()
    if acne_count > 0:
        insights.append(
            f"Acne-related queries appear frequently ({acne_count} cases), showing strong reliance on the assistant for skincare advice. However, responses do not always reflect condition-specific recommendations."
        )

    no_count = (messages["text"].str.lower() == "no").sum()
    if no_count > 0:
        insights.append(
            f"In {no_count} conversations, users responded with short negative replies such as 'No', typically after assistant guidance. This suggests response misalignment rather than complete failure."
        )

    feedback_count = messages[
        (messages["messageType"] == "event") &
        (messages["text"].str.contains("feedback", case=False, na=False))
    ].shape[0]

    if feedback_count > 0:
        insights.append(
            f"Only {feedback_count} explicit feedback interaction was recorded. Combined with drop-offs, this suggests users often disengage without reporting issues."
        )

    if conversion_rate < 0.2:
        insights.append(
            f"Product interaction remains low (conversion rate: {conversion_rate:.2f}), indicating recommendations are not consistently compelling or relevant."
        )

    keywords = ["otp", "order", "offer"]

    for i, word in enumerate(keywords):
        count = messages["text"].str.contains(word, case=False, na=False).sum()

        if count > 10:
            if i % 2 == 0:
                insights.append(
                    f"Queries related to '{word}' appear repeatedly ({count} instances). This points to gaps in how the assistant handles transactional or support-related requests."
                )
            else:
                insights.append(
                    f"A noticeable volume of '{word}'-related queries ({count}) suggests users are not getting complete answers in a single interaction."
                )

    return insights
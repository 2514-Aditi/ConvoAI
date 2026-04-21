# ConvoAI - AI Assistant Conversation Analysis

## Overview
This project analyzes AI assistant conversations and automatically generates actionable insights to improve assistant performance across different brands.

The system processes conversation and message data to identify patterns such as user frustration, ineffective responses, and low engagement scenarios.

---

## Key Features

- Detects user frustration using sentiment analysis and keyword patterns  
- Identifies assistant response gaps and weak interactions  
- Evaluates product recommendation effectiveness using interaction events  
- Detects repeated unresolved queries (e.g., order, OTP, offers)  
- Generates structured, human-readable insights automatically  

---

## Approach

The system treats conversation analysis as a **product analytics problem**, focusing on identifying patterns that directly impact user experience.

Key steps:
1. Load and structure conversation + message data  
2. Analyze message-level signals (sentiment, keywords, events)  
3. Aggregate patterns across conversations  
4. Generate actionable insights with interpretation  

---

## Project Structure

- `analysis/` → core logic and insight generation  
- `data/` → input JSON files  
- `output/` → generated report (`report.md`)  

---

## How to Run

```bash
pip install -r requirements.txt
cd analysis
python main.py

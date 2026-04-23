import pandas as pd
import os

def load_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    conversations_path = os.path.join(base_path, "data", "conversations.json")
    messages_path = os.path.join(base_path, "data", "messages.json")

    conversations = pd.read_json(conversations_path)
    messages = pd.read_json(messages_path)

    return conversations, messages
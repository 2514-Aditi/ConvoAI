import pandas as pd

def load_data():
    conversations = pd.read_json("../data/conversations.json")
    messages = pd.read_json("../data/messages.json")
    return conversations, messages
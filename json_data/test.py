import json
from datetime import datetime

file_path = r'json_data\result.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

messages = data["messages"]

for message in messages:
    date_str = message['date']
    if date_str is not None:
        dt = datetime.fromisoformat(date_str)
        date_str = dt.strftime("%Y-%m-%d %H:%M:%S")

    text = message['text']
    for record in text:
        if type(record) == dict and record.get("type") == 'bold':
            main_record = record.get("text")
        elif type(record) == dict and record.get("type") == 'hashtag':
            hashtag = record.get("hashtag").replace('#', '')


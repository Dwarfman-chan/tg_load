import json
import csv
from datetime import datetime

file_path = r'json_data\result.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

messages = data["messages"]


with open('result.csv', mode='a', newline='', encoding='utf-8') as f:
    for message in messages:
        date_str = message['date']
        if date_str is not None:
            dt = datetime.fromisoformat(date_str)
            date_str = dt.strftime("%Y-%m-%d %H:%M:%S")

        text = message['text']
        for record in text:
            if type(record) == dict and record.get("type") == 'bold':
                main_record = record.get("text")
                if '🟢' in main_record:
                    is_alert = 0
                    if ' Відбій загрози артобстрілу в ' in main_record:
                        oblast = main_record.split(' Відбій загрози артобстрілу в ')[-1]
                        print(oblast)
                    elif ' Відбій тривоги в ' in main_record:
                        oblast = main_record.split(' Відбій тривоги в ')[-1]
                        print(oblast)

                elif '🔴' in main_record:
                    is_alert = 1
                    if ' Повітряна тривога в ' in main_record:
                        oblast = main_record.split(' Повітряна тривога в ')[-1]
                        print(oblast)
                    elif ' Загроза артобстрілу!\nЗараз у ' in main_record:
                        oblast = main_record.split(' Загроза артобстрілу!\nЗараз у ')[-1]
                        print(oblast)

            elif type(record) == dict and record.get("type") == 'hashtag':
                hashtag = record.get("text").replace('#', '')
            
        row = [date_str, is_alert, oblast, hashtag]
        writer = csv.writer(f, delimiter='|')
        writer.writerow(row)

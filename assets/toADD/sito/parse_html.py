import re
import json

html_path = r'c:\Users\skywa\Desktop\progettone_prova\g5-2026-website\assets\toADD\sito\HTI_vs_SSD_SDN_modificato.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try finding Plotly JSON
match = re.search(r'\"data\":\s*(\[\{.*?\}\]),\s*\"layout\"', content, re.DOTALL)
if match:
    data_str = match.group(1)
    try:
        data = json.loads(data_str)
        for i, trace in enumerate(data):
            name = trace.get('name', 'no_name')
            color = 'no_color'
            if 'line' in trace and 'color' in trace['line']:
                color = trace['line']['color']
            elif 'marker' in trace and 'color' in trace['marker']:
                color = trace['marker']['color']
            
            x_len = len(trace.get('x', []))
            print(f'Trace {i}: {name}, color: {color}, points: {x_len}')
    except Exception as e:
        print('Error parsing JSON:', e)
else:
    print("Could not find data array")

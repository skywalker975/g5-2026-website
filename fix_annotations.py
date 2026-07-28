import re

html_path = 'assets/toADD/piogge_evt_best/Dashboard_SDN_Storytelling.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# find all plotly annotations texts
texts = re.findall(r'\"text\":\s*\"(.*?)\"', content)
for t in texts:
    if len(t) > 30 and '<br>' in t:
        print(t)

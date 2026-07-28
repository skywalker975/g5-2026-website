import re

html_path = 'assets/toADD/piogge_evt_best/Dashboard_SDN_Storytelling.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find ANY text property in the HTML that contains '15' or 'April' or '2023' or 'Sudan'
texts = re.findall(r'\"text\":\s*\"([^\"]+)\"', content)
for t in texts:
    if 'Aprile' in t or 'April' in t or '2023' in t or 'Conflitto' in t or 'Event' in t or '15' in t:
        if '<br>' in t or r'\u003cbr\u003e' in t:
            print("FOUND:", t[:200])


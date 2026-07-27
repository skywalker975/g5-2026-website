import re

html_path = 'assets/toADD/piogge_evt_best/Dashboard_SDN_Storytelling.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_br(match):
    text = match.group(1)
    if 'APR 2023' in text or 'Scoppio' in text:
        # replace any multiple breaks with a massive spacing
        text = re.sub(r'(\\u003cbr\\u003e)+', r'\\u003cbr\\u003e\\u003cspan style=\'font-size:12px\'\\u003e\&nbsp;\\u003c/span\\u003e\\u003cbr\\u003e', text)
    return '\"text\":\"' + text + '\"'

new_content = re.sub(r'\"text\":\s*\"(.*?)\"', replace_br, content)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated spacing again.')

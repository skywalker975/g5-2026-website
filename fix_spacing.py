import re

html_path = 'assets/toADD/piogge_evt_best/Dashboard_SDN_Storytelling.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_br(match):
    text = match.group(1)
    if '15 Aprile' in text or '2023' in text or 'April' in text or 'Conflitto' in text or 'Guerra' in text or 'Event' in text or 'Scoppio' in text or 'Guerra Civile' in text or 'Sudan' in text or '15' in text:
        text = text.replace('<br>', '<br><br>')
        text = text.replace(r'\u003cbr\u003e', r'\u003cbr\u003e\u003cbr\u003e')
    return '\"text\":\"' + text + '\"'

new_content = re.sub(r'\"text\":\s*\"(.*?)\"', replace_br, content)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated spacing in annotations.')

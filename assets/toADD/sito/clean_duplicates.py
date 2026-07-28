import re
import json

html_path = r'c:\Users\skywa\Desktop\progettone_prova\g5-2026-website\assets\toADD\sito\HTI_vs_SSD_SDN_modificato.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The JSON is assigned to `var options = {...};`
match = re.search(r'var options = (\{.*?\});', content, re.DOTALL)
if match:
    options_str = match.group(1)
    options = json.loads(options_str)
    
    # Process series
    for series in options.get('series', []):
        if series.get('name') == 'South Sudan': # The yellow line
            data = series.get('data', [])
            
            # We want to remove points on the same vertical line (same x) that are lower (smaller y)
            # We can group by x, and for each x, keep only the max y.
            
            # Since order matters for drawing a line, we should preserve the original order of the points we keep.
            # But wait! If we keep max y, we should just iterate and collect.
            # Actually, to maintain order, let's build a dict of x -> max(y)
            max_y_for_x = {}
            for pt in data:
                x = pt['x']
                y = pt['y']
                if x not in max_y_for_x:
                    max_y_for_x[x] = y
                else:
                    max_y_for_x[x] = max(max_y_for_x[x], y)
                    
            # Now filter the original data to keep only those points where y == max_y_for_x[x]
            # If there are exactly identical points (same x, same y), keep only one.
            new_data = []
            seen = set()
            for pt in data:
                x = pt['x']
                y = pt['y']
                if y == max_y_for_x[x]:
                    if x not in seen:
                        new_data.append(pt)
                        seen.add(x)
                        
            series['data'] = new_data

    # Serialize back to JSON and replace in content
    new_options_str = json.dumps(options, separators=(',', ':'))
    new_content = content[:match.start(1)] + new_options_str + content[match.end(1):]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated successfully.")
else:
    print("Could not find options JSON")

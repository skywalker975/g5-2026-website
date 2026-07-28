import os

css_injection = """
<style>
    /* Fix Plotly updatemenus button hover issue */
    .updatemenu-button:hover rect {
        fill: #3b82f6 !important;
    }
    .updatemenu-button:hover text {
        fill: #ffffff !important;
    }
</style>
"""

files_to_patch = [
    'assets/toADD/piogge_evt_best/Dashboard_AFG_Storytelling.html',
    'assets/toADD/piogge_evt_best/Dashboard_SDN_Storytelling.html'
]

for filepath in files_to_patch:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already patched to avoid duplicates
        if "Fix Plotly updatemenus button hover issue" not in content:
            # Insert just before </head>
            content = content.replace('</head>', f'{css_injection}</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"Patched {filepath}")
    else:
        print(f"File not found: {filepath}")

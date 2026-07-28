import re

file_afg = r'C:\Users\skywa\Desktop\progettone_prova\g5-2026-website\assets\toADD\piogge_evt_best\Dashboard_AFG_Storytelling.html'
file_sdn = r'C:\Users\skywa\Desktop\progettone_prova\g5-2026-website\assets\toADD\piogge_evt_best\Dashboard_SDN_Storytelling.html'

def fix_seasonality(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move Seasonality and Stagionalità texts completely UP to avoid overlap.
    # The current position is "y":1.0,"yanchor":"bottom". Let's change it to "y":1.15,"yanchor":"bottom"
    # Actually, the user says "ritorna indietro" which means revert the deletion (since it was wrong).
    # Wait, earlier I tried to delete them with a script that FAILED ("The command failed with exit code: 1").
    # Oh! My deletion script failed too! So the file was NEVER modified!
    # No wonder the user says "Non è risolto il problema" (The problem is not solved) - because nothing changed!
    
    # I will replace "y":1.0,"yanchor":"bottom" for Seasonality with "y":1.06,"yanchor":"bottom"
    
    def replacer(match):
        pre = match.group(1)
        # Shift up by 0.08
        new_y = float(match.group(2)) + 0.08
        post = match.group(3)
        return f"{pre}{new_y:.3f}{post}"

    # Specifically target the Seasonality / Stagionalità labels, which have x:0.906
    pattern = r'(\"x\":0\.906,\"xanchor\":\"center\",\"xref\":\"paper\",\"y\":)([0-9\.]+)(,\"yanchor\":\"bottom\")'
    new_content = re.sub(pattern, replacer, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Fixed {filepath}")

fix_seasonality(file_afg)
fix_seasonality(file_sdn)

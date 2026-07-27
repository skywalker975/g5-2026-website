import os

html_template = 'template.html'
json_data = 'GLOBAL_SUMMARY_DATA.json'
output_html = 'index.html'

print("Avvio della generazione della mappa HERO v4...")

if not os.path.exists(json_data):
    print(f"Errore: Impossibile trovare il file dei dati ({json_data}). Assicurati che sia nella stessa cartella.")
    exit()

if not os.path.exists(html_template):
    print(f"Errore: Impossibile trovare il template ({html_template}). Assicurati che sia nella stessa cartella.")
    exit()

# Leggi il file JSON
with open(json_data, 'r', encoding='utf-8') as f:
    json_content = f.read()

# Leggi il template HTML
with open(html_template, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Sostituisci il placeholder con il JSON puro
if '__JSON_DATA_PLACEHOLDER__' in html_content:
    final_html = html_content.replace('__JSON_DATA_PLACEHOLDER__', json_content)
    
    # Scrivi il file finale "index.html" che andrà online
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"✅ Build completata! Creato il file '{output_html}'. Ora puoi aprirlo facendo doppio clic o caricarlo sul tuo sito web.")
else:
    print("Errore: Impossibile trovare il tag __JSON_DATA_PLACEHOLDER__ nel file template.html.")
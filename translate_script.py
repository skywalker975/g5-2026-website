import re

with open('assets/toADD/piogge_evt_best/Dashboard_AFG_Storytelling.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '"Menzioni"': '"Mentions"',
    '"Gen-Mar"': '"Jan-Mar"',
    '"Apr-Giu"': '"Apr-Jun"',
    '"Lug-Set"': '"Jul-Sep"',
    '"Ott-Dic"': '"Oct-Dec"',
    '"Gen"': '"Jan"',
    '"Feb"': '"Feb"',
    '"Mar"': '"Mar"',
    '"Apr"': '"Apr"',
    '"Mag"': '"May"',
    '"Giu"': '"Jun"',
    '"Lug"': '"Jul"',
    '"Ago"': '"Aug"',
    '"Set"': '"Sep"',
    '"Ott"': '"Oct"',
    '"Nov"': '"Nov"',
    '"Dic"': '"Dec"',
    'Salienza Mediatica - Conflicts (GDELT)': 'Media Saliency - Conflicts (GDELT)',
    'IDPs Interni (IDP)': 'Internally Displaced Persons (IDPs)',
    'Frequenza Conflicts (ACLED)': 'Conflict Frequency (ACLED)',
    'Price Index Alimentari (WFP)': 'Food Price Index (WFP)',
    'MAG 2021': 'MAY 2021',
    'Ritiro USA': 'US Withdrawal',
    'Reveal Evento Chiave': 'Reveal Key Event',
    'Nascondi': 'Hide',
    'Pre-Event Average': 'Pre-Event Average', # Already in english
    'Post-Event Average': 'Post-Event Average'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('assets/toADD/piogge_evt_best/Dashboard_AFG_Storytelling.html', 'w', encoding='utf-8') as f:
    f.write(content)

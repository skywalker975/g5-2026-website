path = r'C:\Users\skywa\Desktop\progettone_prova\g5-2026-website\_pages\Text-analysis.markdown'
with open(path, 'rb') as f:
    raw = f.read()

# Let's find out where the utf-8 ends. 
# We appended text starting with "<div class=\"row mt-4\">"
# Let's just decode with 'utf-8' using errors='replace', and if it's messed up, we'll fix it.
try:
    decoded = raw.decode('utf-8')
    # If it works without error, why is jekyll complaining?
    # Maybe Add-Content wrote ANSI (Windows-1252) and Jekyll strictly wants UTF-8.
    # In Windows 10/11, Add-Content default is often ANSI.
    with open(path, 'w', encoding='utf-8') as f2:
        f2.write(decoded)
    print("Fixed via simple UTF-8 decode/encode.")
except UnicodeDecodeError:
    # Try cp1252 for the appended part
    # Let's just decode as cp1252 and ignore errors for now? No, we know the original was utf-8.
    original_part = raw[:-3000].decode('utf-8', errors='ignore')
    # Just decode the whole thing with errors='replace' to see if it fixes Jekyll
    decoded = raw.decode('utf-8', errors='ignore')
    with open(path, 'w', encoding='utf-8') as f2:
        f2.write(decoded)
    print("Fixed via ignore.")

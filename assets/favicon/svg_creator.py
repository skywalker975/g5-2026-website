from rembg import remove
from PIL import Image

# Definisci i percorsi dei file
input_path = 'tmp-africa-favicon.png'
output_path = 'favicon_africa.png'

# Carica l'immagine originale
input_image = Image.open(input_path)

# Rimuovi lo sfondo (isolerà automaticamente il soggetto principale, l'Africa)
output_image = remove(input_image)

# Salva il risultato con sfondo trasparente
output_image.save(output_path)
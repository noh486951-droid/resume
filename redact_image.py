from PIL import Image, ImageFilter
import os

def mosaic_area(img, box, pixel_size=15):
    # Get the area to redact
    x, y, w, h = box
    region = img.crop((x, y, x + w, y + h))
    
    # Rescale down and up to create pixelated effect
    small = region.resize((max(1, w // pixel_size), max(1, h // pixel_size)), resample=Image.NEAREST)
    large = small.resize((w, h), resample=Image.NEAREST)
    
    # Paste it back
    img.paste(large, (x, y))
    return img

# Load image
source_path = r'C:\Users\明芳\.gemini\antigravity\brain\32dd8fa2-f2cc-4e81-b391-12c0d101ea6b\media__1775539256381.png'
save_path = r'c:\Users\明芳\Desktop\train\interview\resume\assets\gas_tools.png'

img = Image.open(source_path)
width, height = img.size

# Estimated rectangles for "Site Names" and "Machine Models"
# These are rough estimates based on a standard 800-1000px wide screenshot
# We will cover the main text areas in the cards

# Card 1: Main site title
mosaic_area(img, (50, int(height * 0.8), int(width * 0.7), 60), pixel_size=20)

# Card 1: Machine model (typically smaller text)
mosaic_area(img, (180, int(height * 0.88), 120, 30), pixel_size=15)

# If there's a second card showing (partial)
mosaic_area(img, (50, int(height * 0.95), int(width * 0.5), 40), pixel_size=15)

# Save the result
img.save(save_path)
print(f"Redacted image saved to {save_path}")

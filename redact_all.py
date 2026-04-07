from PIL import Image, ImageFilter
import os

def mosaic_area(img, box, pixel_size=15):
    x, y, w, h = box
    # Boundary check
    width, height = img.size
    x = max(0, min(x, width - 1))
    y = max(0, min(y, height - 1))
    w = min(w, width - x)
    h = min(h, height - y)
    
    region = img.crop((x, y, x + w, y + h))
    small = region.resize((max(1, w // pixel_size), max(1, h // pixel_size)), resample=Image.NEAREST)
    large = small.resize((w, h), resample=Image.NEAREST)
    img.paste(large, (x, y))
    return img

# --- 1. Redact Training Photo (Faces) ---
source_training = r'C:\Users\明芳\.gemini\antigravity\brain\32dd8fa2-f2cc-4e81-b391-12c0d101ea6b\media__1775538990373.jpg'
save_training = r'c:\Users\明芳\Desktop\train\interview\resume\assets\training.jpg'

img_t = Image.open(source_training)
w_t, h_t = img_t.size

# Mosaic student faces/heads in the classroom
# Students are roughly in the middle to lower part of the screen
mosaic_area(img_t, (int(w_t*0.4), int(h_t*0.55), int(w_t*0.1), int(h_t*0.15)), pixel_size=20) # Middle-left student
mosaic_area(img_t, (int(w_t*0.5), int(h_t*0.6), int(w_t*0.12), int(h_t*0.2)), pixel_size=20) # Middle student
mosaic_area(img_t, (int(w_t*0.65), int(h_t*0.55), int(w_t*0.15), int(h_t*0.25)), pixel_size=20) # Right students
mosaic_area(img_t, (int(w_t*0.05), int(h_t*0.55), int(w_t*0.15), int(h_t*0.2)), pixel_size=20) # Bottom-left student
mosaic_area(img_t, (int(w_t*0.8), int(h_t*0.5), int(w_t*0.12), int(h_t*0.15)), pixel_size=20) # Far right

img_t.save(save_training)
print(f"Training photo redacted and saved to {save_training}")

# --- 2. Improve GAS Image (Re-crop/Save) ---
# The user says it's not clear. We will ensure the full width is saved and maybe less generic cropping.
source_gas = r'C:\Users\明芳\.gemini\antigravity\brain\32dd8fa2-f2cc-4e81-b391-12c0d101ea6b\media__1775539256381.png'
save_gas = r'c:\Users\明芳\Desktop\train\interview\resume\assets\gas_tools.png'
img_g = Image.open(source_gas)
# Repeat redaction on the raw image to be safe
w_g, h_g = img_g.size
mosaic_area(img_g, (50, int(h_g * 0.78), int(w_g * 0.8), 100), pixel_size=20) # Main site names
mosaic_area(img_g, (150, int(h_g * 0.88), 200, 40), pixel_size=15) # Models
img_g.save(save_gas)
print(f"GAS image updated and saved to {save_gas}")

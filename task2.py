import argparse
from PIL import Image
import random
import os

def load_image(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"[-] File not found: {path}")
    return Image.open(path).convert("RGB")

def save_image(img, path):
    img.save(path)

def xor_encrypt(img, key):
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)
    return img

def add_encrypt(img, key):
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return img

def swap_pixels(img):
    pixels = img.load()
    width, height = img.size
    for _ in range((width * height) // 2):
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]
    return img

def encrypt_image(input_path, output_path, mode, key):
    img = load_image(input_path)

    if mode == 'xor':
        img = xor_encrypt(img, key)
    elif mode == 'add':
        img = add_encrypt(img, key)
    elif mode == 'swap':
        img = swap_pixels(img)
    else:
        raise ValueError("Unsupported mode. Choose 'xor', 'add', or 'swap'.")

    save_image(img, output_path)
    print(f"[+] Encrypted image saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🖼️ Simple Image Encryption Tool")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("output", help="Path to save the encrypted image")
    parser.add_argument("-m", "--mode", choices=["xor", "add", "swap"], default="xor", help="Encryption mode")
    parser.add_argument("-k", "--key", type=int, default=123, help="Encryption key (for xor/add)")

    args = parser.parse_args()

    encrypt_image(args.input, args.output, args.mode, args.key)

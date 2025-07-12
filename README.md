🧪 Example Test
bash
python3 image_encryptor.py input.jpg encrypted.jpg --mode xor --key 101
Then to decrypt:

bash
python3 image_encryptor.py encrypted.jpg decrypted.jpg --mode xor --key 101
Because XOR is reversible, the original image will be restored.

💡 Tip
To test it visually:

Open input.jpg → Normal image

Open encrypted.jpg → Glitched image

Open decrypted.jpg → Should match the original (if XOR/ADD with correct key)


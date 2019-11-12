# qrsticker
Python package to generate a QR code sticker with optional title and subtitle

## Usage
Generate a qr code as `PIL.Image.Image` and paste it on `Sticker` object.

```python
qr_code = generate_qr_code()

sticker = Sticker(300, 400, (255, 255, 255))
sticker.paste_qr_code(qr_code)
sticker.insert_title('Title')
sticker.insert_subtitle('Subtitle')
sticker.save('test')
```

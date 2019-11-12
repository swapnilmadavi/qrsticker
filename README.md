# qrsticker

Python package to generate a QR code sticker with optional title and subtitle

## Usage

```python
qr_data = 'swapnilmadavi/qrsticker'
sticker = Sticker(300, 400, background=(255,255,255))
sticker.make_qr_code(qr_data, padding=20)
sticker.insert_title('Title')
sticker.insert_subtitle('Subtitle')
sticker.save('test')
```
</br>

<p align="center">
  <img src="test.png" alt="Result sticker" width=200 border="4"/>
</p>

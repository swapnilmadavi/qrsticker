import qrcode
from PIL import Image, ImageDraw, ImageFont

class Sticker:

    def __init__(self, sticker_w, sticker_h, background):
        self.sticker = Image.new('RGB', (sticker_w, sticker_h), background)

    def paste_qr_code(self, qr_code):
        sticker_w, sticker_h = self.sticker.size
        qr_w, qr_h = qr_code.size
        offset = (0,0)
        if (sticker_w != sticker_h):
            offset = (int((sticker_w - qr_w) / 2), int((sticker_w - qr_h) / 2))
        else:
            offset = (int((sticker_w - qr_w) / 2), int((sticker_h - qr_h) / 2))
        self.sticker.paste(qr_code, offset)

    def insert_title(self, title):
        img = ImageDraw.Draw(self.sticker)
        sticker_w = self.sticker.size[0]
        font = ImageFont.truetype('qrsticker/font/Roboto-Regular.ttf', 20)
        title_w = img.textsize(title, font=font)[0]
        offset = (int((sticker_w - title_w) / 2), 310)
        img.text(offset, title, fill=(0, 0, 0), font=font)

    def insert_subtitle(self, subtitle):
        img = ImageDraw.Draw(self.sticker)
        sticker_w = self.sticker.size[0]
        font = ImageFont.truetype('qrsticker/font/Roboto-Regular.ttf', 18)
        title_w = img.textsize(subtitle, font=font)[0]
        offset = (int((sticker_w - title_w) / 2), 340)
        img.text(offset, subtitle, fill=(0, 0, 0), font=font)

    def save(self, name):
        self.sticker.save(name + '.png')

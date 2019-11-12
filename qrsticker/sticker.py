import qrcode
from PIL import Image, ImageDraw, ImageFont

class Sticker:

    def __init__(self, sticker_w, sticker_h, background=(255, 255, 255)):
        self.sticker = Image.new('RGB', (sticker_w, sticker_h), background)
        self.size = (sticker_w, sticker_h)

    def make_qr_code(self, data, padding=0):
        qr_size = self.__get_qr_size(padding)
        qr_code = self.__generate_qr_code(data, qr_size)
        offset = (int((self.size[0] - qr_size) / 2), int((self.size[0] - qr_size) / 2))
        self.sticker.paste(qr_code, offset)

    def insert_title(self, title):
        img = ImageDraw.Draw(self.sticker)
        font = ImageFont.truetype('qrsticker/font/Roboto-Regular.ttf', 20)
        title_w = img.textsize(title, font=font)[0]
        offset = (int((self.size[0] - title_w) / 2), 310)
        img.text(offset, title, fill=(0, 0, 0), font=font)

    def insert_subtitle(self, subtitle):
        img = ImageDraw.Draw(self.sticker)
        font = ImageFont.truetype('qrsticker/font/Roboto-Regular.ttf', 18)
        title_w = img.textsize(subtitle, font=font)[0]
        offset = (int((self.size[0] - title_w) / 2), 340)
        img.text(offset, subtitle, fill=(0, 0, 0), font=font)

    def save(self, name):
        self.sticker.save(name + '.png')

    def __get_qr_size(self, padding):
        qr_size = self.size[0] - (2*padding)
        return qr_size

    def __generate_qr_code(self, data, qr_size):
        qr = qrcode.QRCode(border=0)
        qr.add_data(data)
        qr.make()
        qr_code = qr.make_image().resize((qr_size, qr_size))
        return qr_code

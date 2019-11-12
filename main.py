from qrsticker import Sticker
import qrcode

if __name__ == "__main__":
    qr_data = 'swapnilmadavi/qrsticker'
    sticker = Sticker(300, 400, background=(255,255,255))
    sticker.make_qr_code(qr_data, padding=20)
    sticker.insert_title('Title')
    sticker.insert_subtitle('Subtitle')
    sticker.save('test')
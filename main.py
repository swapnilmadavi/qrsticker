from qrsticker import Sticker
import qrcode

if __name__ == "__main__":
    qr = qrcode.QRCode(border=0)
    qr.add_data("swapnilmadavi/qrsticker")
    qr.make()
    qr_code = qr.make_image().resize((250, 250))

    sticker = Sticker(300, 400, (255, 255, 255))
    sticker.paste_qr_code(qr_code)
    sticker.insert_title('Title')
    sticker.insert_subtitle('Subtitle')
    sticker.save('test')
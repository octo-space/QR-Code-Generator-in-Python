import qrcode as qr
from PIL import Image

def generate_qr_code():
    qr_data = input("Enter data: ")
    code_color = input("Code Color (e.g., black, red, blue): ") or "black"
    back_color = input("Back Color (e.g., White, red, blue): ") or "white"
    saved_name = input("Enter the name of the file with extension (e.g., img.png): ")

    qr_code = qr.QRCode(
        version=1,
        error_correction=qr.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5
    )

    qr_code.add_data(qr_data)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color=code_color, back_color=back_color)
    img.save(saved_name)

if __name__ == "__main__":
    generate_qr_code()

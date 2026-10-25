import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

base_dir = r"D:\Angular_in_one\siddhi"
qr_dir = os.path.join(base_dir, "qr_codes")
os.makedirs(qr_dir, exist_ok=True)

songs = [
    {
        "id": "ajab-si",
        "file_name": "ajab_si",
        "title": "Aankhon Mein Teri (Ajab Si)",
        "artist": "KK • Om Shanti Om",
        "img": "ajab-si.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=ajab-si"
    },
    {
        "id": "heeriye",
        "file_name": "heeriye",
        "title": "Heeriye",
        "artist": "Jasleen Royal & Arijit Singh",
        "img": "heeriye.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=heeriye"
    },
    {
        "id": "tujh-mei-rab",
        "file_name": "tujh_mei_rab",
        "title": "Tujh Mein Rab Dikhta Hai",
        "artist": "Roop Kumar Rathod • Salim-Sulaiman",
        "img": "tujh-mei-rab.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tujh-mei-rab"
    },
    {
        "id": "tum-ho-toh",
        "file_name": "tum_ho_toh",
        "title": "Tum Ho Toh",
        "artist": "Farhan Akhtar • Rock On!!",
        "img": "tum-ho-toh.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tum-ho-toh"
    },
    {
        "id": "until-i-found-you",
        "file_name": "until_i_found_you",
        "title": "Until I Found You",
        "artist": "Stephen Sanchez",
        "img": "until-i-found-you.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=until-i-found-you"
    },
    {
        "id": "tumhara-milna",
        "file_name": "tumhara_milna",
        "title": "Tumhara Milna",
        "artist": "Arijit Singh • Tanishk Bagchi",
        "img": "tumhara-milna.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tumhara-milna"
    },
    {
        "id": "tere-sang-yaara",
        "file_name": "tere_sang_yaara",
        "title": "Tere Sang Yaara",
        "artist": "Atif Aslam • Rustom",
        "img": "tere-sang-yaara.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tere-sang-yaara"
    },
    {
        "id": "ude-jab-jab",
        "file_name": "ude_jab_jab",
        "title": "Ude Jab Jab Zulfen Teri",
        "artist": "Mohammed Rafi & Asha Bhosle • Naya Daur",
        "img": "ude-jab-jab.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=ude-jab-jab"
    },
    {
        "id": "tu-chahiye",
        "file_name": "tu_chahiye",
        "title": "Tu Chahiye",
        "artist": "Atif Aslam • Pritam",
        "img": "tu-chahiye.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tu-chahiye"
    },
    {
        "id": "tu-na-samjhe",
        "file_name": "tu_na_samjhe",
        "title": "Tu Na Samjhe",
        "artist": "Raja",
        "img": "tu-na-samjhe.jpeg",
        "url": "https://jain23yuvraj.github.io/siddhi-songs/?song=tu-na-samjhe"
    }
]

for s in songs:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=12,
        border=3,
    )
    qr.add_data(s["url"])
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    
    # 1. Pure QR Code PNG
    raw_path = os.path.join(qr_dir, f"{s['file_name']}_qr.png")
    qr_img.save(raw_path)
    print(f"Saved pure QR: {raw_path}")

    # 2. Printable Polaroid / Music Card (640 x 960)
    card_w, card_h = 640, 960
    card = Image.new("RGB", (card_w, card_h), "#18262c")
    draw = ImageDraw.Draw(card)
    
    # Load and crop album photo into a nice thumbnail
    photo_path = os.path.join(base_dir, s["img"])
    photo = Image.open(photo_path)
    pw, ph = photo.size
    min_dim = min(pw, ph)
    left = (pw - min_dim) // 2
    top = (ph - min_dim) // 2
    photo_cropped = photo.crop((left, top, left + min_dim, top + min_dim))
    photo_thumb = photo_cropped.resize((360, 360), Image.Resampling.LANCZOS)
    
    photo_x = (card_w - 360) // 2
    photo_y = 44
    draw.rectangle([photo_x - 3, photo_y - 3, photo_x + 360 + 2, photo_y + 360 + 2], fill="#ffffff")
    card.paste(photo_thumb, (photo_x, photo_y))
    
    # Resize QR code to 260 x 260
    qr_resized = qr_img.resize((260, 260), Image.Resampling.LANCZOS)
    qr_x = (card_w - 260) // 2
    qr_y = 550
    draw.rectangle([qr_x - 8, qr_y - 8, qr_x + 260 + 7, qr_y + 260 + 7], fill="#ffffff")
    card.paste(qr_resized, (qr_x, qr_y))
    
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 25)
        font_artist = ImageFont.truetype("arial.ttf", 18)
        font_scan = ImageFont.truetype("arialbd.ttf", 16)
        font_footer = ImageFont.truetype("arial.ttf", 14)
    except:
        font_title = font_artist = font_scan = font_footer = ImageFont.load_default()
        
    draw.text((card_w // 2, 436), s["title"], fill="#ffffff", font=font_title, anchor="mm")
    draw.text((card_w // 2, 472), s["artist"], fill="#9bb0b9", font=font_artist, anchor="mm")
    draw.text((card_w // 2, 510), "SCAN TO PLAY WITH CAMERA", fill="#1ed760", font=font_scan, anchor="mm")
    draw.text((card_w // 2, 880), "Special Mix for Siddhi", fill="#738a95", font=font_footer, anchor="mm")
    draw.text((card_w // 2, 905), s["url"], fill="#4e626c", font=font_footer, anchor="mm")
    
    card_path = os.path.join(qr_dir, f"{s['file_name']}_card.png")
    card.save(card_path)
    print(f"Saved Printable Card: {card_path}")

print("All 10 QR codes generated successfully!")

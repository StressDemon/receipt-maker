from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import argparse

def draw_text(draw, text, position, font, alignment="left"):
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
    x, y = position
    if alignment == "center":
        x = x - text_width // 2
    elif alignment == "right":
        x = x - text_width
    draw.text((x, y), text, fill="black", font=font)

def generate_receipt(streamer_name, follower_name, action, tier=None, months=None, address="1234 Streamer Lane, Twitch City", thank_you_message="THANK YOU!"):
    # Set receipt dimensions
    width, height = 400, 600
    img = Image.new('RGB', (width, height), color=(255, 255, 255))

    # Initialize drawing context
    draw = ImageDraw.Draw(img)

    # Define fonts
    try:
        big_font = ImageFont.truetype("arial.ttf", 24)
        font = ImageFont.truetype("arial.ttf", 20)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        big_font = ImageFont.load_default()
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Shop name (Streamer's name) and address
    draw_text(draw, streamer_name, (width // 2, 10), big_font, alignment="center")
    draw_text(draw, address, (width // 2, 40), small_font, alignment="center")

    # Separator
    separator = "**********************************************"
    draw_text(draw, separator, (width // 2, 70), font, alignment="center")

    # Receipt header
    header = "CASH RECEIPT"
    draw_text(draw, header, (width // 2, 100), big_font, alignment="center")

    # Another separator
    draw_text(draw, separator, (width // 2, 130), font, alignment="center")

    # Items and pricing
    y_position = 160
    descriptions = [f"User: {follower_name}"]
    prices = [""]

    if action.lower() == "followed":
        descriptions.append("Follow")
        prices.append("$0.00")
    elif action.lower() == "subscribed" and tier:
        prices_dict = {"1": 4.99, "2": 9.99, "3": 24.99}
        total_price = prices_dict.get(str(tier)) * months
        descriptions.append(f"Subscription (Tier {tier}) x {months}")
        prices.append(f"${total_price:.2f}")

    for description, price in zip(descriptions, prices):
        draw_text(draw, description, (20, y_position), font, alignment="left")
        draw_text(draw, price, (width - 20, y_position), font, alignment="right")
        y_position += 30

    # Total, cash, and change
    total = sum(float(p[1:]) if p else 0 for p in prices)
    draw_text(draw, separator, (width // 2, y_position), font, alignment="center")
    y_position += 30

    draw_text(draw, "Total", (20, y_position), big_font, alignment="left")
    draw_text(draw, f"${total:.2f}", (width - 20, y_position), big_font, alignment="right")
    y_position += 40

    cash = round(random.uniform(total, total + 20), 2)  # Generate random cash >= total
    change = cash - total
    draw_text(draw, "Cash", (20, y_position), font, alignment="left")
    draw_text(draw, f"${cash:.2f}", (width - 20, y_position), font, alignment="right")
    y_position += 30

    draw_text(draw, "Change", (20, y_position), font, alignment="left")
    draw_text(draw, f"${change:.2f}", (width - 20, y_position), font, alignment="right")
    y_position += 30

    # And another another separator
    draw_text(draw, separator, (width // 2, y_position), font, alignment="center")
    y_position += 30

    # Thank you or screw you message :D
    draw_text(draw, thank_you_message, (width // 2, y_position), big_font, alignment="center")
    y_position += 40

    # Generate QR code for the follower cause you gotta link the follower my guy
    qr_data = f"https://www.twitch.tv/{follower_name}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    qr_img = qr_img.resize((100, 100))

    # Position QR code at the bottom center
    qr_position = (width // 2 - qr_img.size[0] // 2, y_position)
    img.paste(qr_img, qr_position)

    # Save image
    img.save('follow_receipt.png')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a follow/subscription receipt for a streamer.')
    parser.add_argument('streamer_name', type=str, help='Name of the streamer')
    parser.add_argument('follower_name', type=str, help='Name of the follower/subscriber')
    parser.add_argument('action', type=str, choices=['followed', 'subscribed'], help='Action: followed or subscribed')
    parser.add_argument('--tier', type=int, choices=[1, 2, 3], help='Subscription tier (1, 2, or 3)', default=1)
    parser.add_argument('--months', type=int, help='Number of months (only for subscriptions)', default=1)
    parser.add_argument('--address', type=str, help='Address of the streamer', default="1234 Streamer Lane, Twitch City")
    parser.add_argument('--thank_you', type=str, help='Thank you message', default="THANK YOU!")
    args = parser.parse_args()

    generate_receipt(args.streamer_name, args.follower_name, args.action, args.tier, args.months, args.address, args.thank_you)

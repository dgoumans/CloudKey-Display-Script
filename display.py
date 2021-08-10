from PIL import Image, ImageDraw, ImageFont
import socket 
from datetime import datetime

# GLOBAL VARS
WIDTH = 160
HEIGHT = 60
MARGIN = 3

NAME = "Server DG"
font_path = "NotoSans-Light.ttf"


def prep_image():
    # set background
    image = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(image)
    return image

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_time():
    now = datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%d/%m/%Y")
    return time, date

def add_text(image):
    # draw content
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, 14)

    # text top left
    
    w, h = draw.textsize(NAME, font=font)    
    draw.text((MARGIN,0), NAME, font=font)    

    lineHor1Y = h+MARGIN
    lineVer1X = MARGIN+w+MARGIN

    # spacers
    draw.line((0, lineHor1Y, WIDTH, lineHor1Y), "white") # h split
    draw.line((lineVer1X, 0, lineVer1X, lineHor1Y), "white") # v split

    # IP right
    ip =  get_ip()
    w, h = draw.textsize(ip, font=font)    
    draw.text((lineVer1X + MARGIN + 1 ,0), ip, font=font)    

    # time & date
    time, date = get_time()
    font = ImageFont.truetype(font_path, 12)
    w, h = draw.textsize(date, font=font)
    draw.text((WIDTH-w,HEIGHT-h), date, font=font)    

    font = ImageFont.truetype(font_path, 36)
    w, h = draw.textsize(time, font=font)
    draw.text((MARGIN,HEIGHT-h-MARGIN), time, font=font)    

    return image

def write_out(output_path, image):
    image.save(output_path)

if __name__ == "__main__":
    blank_image = prep_image()
    image = add_text(blank_image)
    write_out("display.png",image)
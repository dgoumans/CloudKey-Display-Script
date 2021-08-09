from PIL import Image, ImageDraw
import socket 
from datetime import datetime

# GLOBAL VARS
WIDTH = 160
HEIGHT = 60

def prep_image():
    # set background
    image = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(image)

    # draw ui frames
    draw.line((0, HEIGHT/3, WIDTH, HEIGHT/3), "white") # h split
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
    # input
    time, date = get_time()
    ip =  get_ip()

    # draw content
    draw = ImageDraw.Draw(image)

    message = "Server DG"
    w, h = draw.textsize(message)    
    draw.text(((WIDTH-w)/2,5), message)

    datetime = time + " - " + date
    w, h = draw.textsize(datetime)
    draw.text(((WIDTH-w)/2, 25), datetime)
    
    w, h = draw.textsize(ip)
    draw.text(((WIDTH-w)/2,40), ip)

    return image

def write_out(output_path, image):
    image.save(output_path)

if __name__ == "__main__":
    blank_image = prep_image()
    image = add_text(blank_image)
    write_out("display.png",image)

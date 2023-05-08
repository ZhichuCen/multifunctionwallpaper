import ctypes
from PIL import Image,ImageFont,ImageDraw
from os import path
import json
from datetime import datetime





def calc_date():

    
    date_final = datetime(2024,6,7)
    date_now = datetime.now()
    date = str(date_final-date_now).split()[0]
    txt = '高考倒计时'+date+'天'#+'\n内卷起来了'
    create_wp(txt)
    set_wp()
    

def create_wp(txt):
    font = ImageFont.truetype('FZDHTJW.ttf',200)
    width = 1920
    height = 1080
    image = Image.new('RGB',(width,height),(255,255,255))
    #image = Image.open('bg.jpg')
    # image.setsize(1920,1080)

    draw = ImageDraw.Draw(image)



    w, h = font.getsize(txt)   
    draw.text(((width-w)/2, (height-h)/2-450), txt, fill=(0,255,255), font=font)


    image.save('wallpaper.jpg')
def set_wp():
    current_path = path.abspath(__file__)
    father_path =  path.abspath( path.dirname(current_path) +  path.sep + ".")
    filepath= path.join( father_path,'wallpaper.jpg')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

calc_date()



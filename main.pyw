import ctypes
from PIL import Image, ImageFont, ImageDraw
from os import path
import json
import datetime
import random
import colorsys


def calc_date():
    global mindan, day, date1

    date_final = datetime.datetime(2024, 6, 7)
    date_chunkao = datetime.datetime(2024, 1, 7)
    date_now = datetime.datetime.now()
    date = str(date_final - date_now).split()[0]
    date1 = str(date_chunkao - date_now).split()[0]
    txt = '春考倒计时' + date1 + '天' + '\n高考倒计时' + date + '天'
    with open('zhiri.json', 'r') as f:
        data = json.load(f)
    with open('名单.json', 'r') as f:
        mindan = json.load(f)

    newest_date = data['newest_date']
    people = data['people']
    zrbz = data['zrbz']
    day = datetime.date.today().weekday() + 1
    if newest_date != str(datetime.date.today()):
        if day != 5 and day != 6 and day != 7:
            people -= 5
        if day != 6 and day != 7:
            zrbz += 1
        data['newest_date'] = str(datetime.date.today())
        data['people'] = people
        data['zrbz'] = zrbz
    with open('zhiri.json', 'w') as f:
        json.dump(data, f)
    create_wp(txt, people, zrbz)
    set_wp()


def yu(x):
    global mindan
    l = len(mindan)
    while x <= 0:
        x += l
    x = x % l
    # if x ==0:
    #     x=l
    # print(x)
    return list(mindan.values())[x]


def create_wp(txt, people, zrbz):
    font = ImageFont.truetype('ping.ttf', 100)
    font2 = ImageFont.truetype('ping.ttf', 50)
    width = 1920
    height = 1080
    # image = Image.new('RGB',(width,height),(255,255,255))
    image = Image.open("kebiao/{}.png".format(str(day)))
    #image.resize(1920, 108)

    draw = ImageDraw.Draw(image)
    w, h = font.getsize(txt)

    if datetime.date.today().weekday() + 1 != 5:
        zhiri_txt = "二班黑板：%s\n二班扫地：%s\n二班整理：%s\n选修黑板：%s\n选修扫地：%s\n值日班长：%s" % (
        yu(people), yu(people + 1), yu(people + 2), yu(people + 3), yu(people + 4), yu(zrbz),)
    else:
        zhiri_txt = '\n值日班长：%s' % (yu(zrbz))

    # zhiri_txt="黑板: %s,%s \n扫地: %s,%s\n"%(yu(people),yu(people+1),yu(people+2),yu(people+3))

    # draw.text(((width-w)/2, (height-h)/2-450), txt, fill=(0,255,255), font=font)
    # countdownColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # h_c=-1
    # while .55<h_c<.60 or h_c==-1:
    #     h_c=random.random()
    h_c = random.random()
    # print(h_c)
    countdownColor_l = colorsys.hsv_to_rgb(h_c, 1, 1)
    countdownColor = int(countdownColor_l[0] * 255), int(countdownColor_l[1] * 255), int(countdownColor_l[2] * 255),
    # print( countdownColor)
    draw.text((1400, 400), zhiri_txt, fill=(146, 182, 213), font=font2)
    draw.text(((width - w) / 2 + 400, (height - h) / 2 - 500), txt, countdownColor, font=font)
    draw.text((0, 190), str(datetime.date.today()), fill=(146, 182, 213), font=font2)
    # draw.text((1400,400 ), zhiri_txt, fill=(150,150,150), font=font2)
    # txt2 = '教师节倒计时0天'
    # draw.text(((width-w)/2, (height-h)/2-250), txt2, fill=(255,0,0), font=font)

    image.save('wallpaper.png')


def set_wp():
    current_path = path.abspath(__file__)
    father_path = path.abspath(path.dirname(current_path) + path.sep + ".")
    filepath = path.join(father_path, 'wallpaper.png')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)


calc_date()

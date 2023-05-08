import ctypes
from PIL import Image,ImageFont,ImageDraw
from os import path
import json
import datetime





def calc_date():
    global mindan
    
    date_final = datetime.datetime(2024,6,7)
    date_now = datetime.datetime.now()
    date = str(date_final-date_now).split()[0]
    txt = '高考倒计时'+date+'天'#+'\n内卷起来了'
    with open('zhiri.json','r') as f:
        data = json.load(f)
    with open('名单.json','r') as f:
        mindan = json.load(f)

    newest_date = data['newest_date']
    people = data['people']
    zrbz = data['zrbz']
    if newest_date != str(datetime.date.today()):
        people-=4
        zrbz+=1
        data['newest_date'] = str(datetime.date.today())
        data['people'] = people
        data['zrbz']=zrbz  
    with open('zhiri.json','w') as f:
            json.dump(data,f)
    create_wp(txt,people,zrbz)
    set_wp()
    

def yu(x):
    global mindan
    l = len(mindan)
    while x<=0:
        x+=l
    x = x%l
    # if x ==0:
    #     x=l
    print(x)
    return list(mindan.values())[x]

def create_wp(txt,people,zrbz):
    font = ImageFont.truetype('ping.ttf',200)
    font2 = ImageFont.truetype('ping.ttf',50)
    width = 1920
    height = 1080
    image = Image.new('RGB',(width,height),(255,255,255))
    # image = Image.open('bg.jpg')
    # image.setsize(1920,1080)



    draw = ImageDraw.Draw(image)
    w, h = font.getsize(txt)  


    zhiri_txt="二班: %s,%s \n选修: %s,%s\n值日班长：%s"%(yu(people),yu(people+1),yu(people+2),yu(people+3),yu(zrbz),)

    # zhiri_txt="黑板: %s,%s \n扫地: %s,%s\n"%(yu(people),yu(people+1),yu(people+2),yu(people+3))



    draw.text(((width-w)/2, (height-h)/2-450), txt, fill=(0,255,255), font=font)
    draw.text((1400,500 ), zhiri_txt, fill=(0,255,255), font=font2)
    # txt2 = '教师节倒计时0天'
    # draw.text(((width-w)/2, (height-h)/2-250), txt2, fill=(255,0,0), font=font)

    image.save('wallpaper.jpg')
def set_wp():
    current_path = path.abspath(__file__)
    father_path =  path.abspath( path.dirname(current_path) +  path.sep + ".")
    filepath= path.join( father_path,'wallpaper.jpg')

    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)

calc_date()



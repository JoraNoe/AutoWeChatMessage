import requests
import json
import datetime
import re
import random

# APP的ID号
appID = 'wxca51f7e17a0711e4'
# 安全秘钥
appsecret = '64052c5932fc81571ed7ea8c7e40a6b7'


# 获取access_token
def getAccessToken():
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": appID,
            "secret": appsecret
        }
    )
    access_token = r1.json()['access_token']
    # print(access_token)
    return access_token


# 获取情话
def getLoveLanage():
    result = requests.get("https://api.1314.cool/words/api.php?return=json")
    returnString = result.json()["word"]
    return returnString

# 获取随机颜色
def get_color():
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = get_colors(100)
    return random.choice(color_list)


# 发送天气提醒推送
def sendMessage(weatherData, wx_id, template_id):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # 在一起的日期
    togetherDay = datetime.date(2022, 11, 26)
    # 她的下一个生日
    herBirthday = datetime.date(2023, 4, 4)
    
    #老婆考试日期
    ExeamDay = daatetime.date(2023,4,1);
    
    today = datetime.date(int(year), int(month), int(day))
    week_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    body = {
        "touser": wx_id,  # 推送消息的对象（用户微信id）
        "template_id": template_id,  # 模板ID
        "data": {
            'date': {
                'value': "今天日期："+datetime.datetime.now().strftime('%Y-%m-%d'),
                'color': get_color()
            },
            'week': {
                'value': week_list[datetime.date(year, month, day).weekday()],
                'color': get_color()
            },
            'region': {
                'value': weatherData['lives'][0]['province'] + weatherData['lives'][0]['city'],
                'color': get_color()
            },
            'weather': {
                'value': weatherData['lives'][0]['weather'],
                'color': get_color()
            },
            'temp': {
                'value': weatherData['lives'][0]['temperature'] + '℃',
                'color': get_color()
            },
            'humidity': {
                'value': weatherData['lives'][0]['humidity'] + '%',
                'color': get_color()
            },
            'wind_dir': {
                'value': weatherData['lives'][0]['winddirection'],
                'color': get_color()
            },
            'windpower': {
                'value': weatherData['lives'][0]['windpower'],
                'color': get_color()
            },
            'love_day': {
                'value': int(re.search('(?P<days>.*?) days', str(today.__sub__(togetherDay))).group('days')) + 1,
                'color': get_color()
            },
            'birthday1': {
                'value': int(re.search('(?P<days>.*?) days', str(herBirthday.__sub__(today))).group('days')),
                'color': get_color()
            },
            'speack': {  # 情话
                'value': "{}{}{}{}".format(getLoveLanage(),' -老婆加油，老婆最棒，老公支持你，老婆使劲，老婆奥利给- 好好学习,距离你考试剩余：',int(re.search('(?P<days>.*?) days', str(ExeamDay.__sub__(today))).group('days')),'天')
                'color': get_color()
            }
        }
    }

    r2 = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            "access_token": getAccessToken()
        },
        data=json.dumps(body)
    )

    print(r2.text)



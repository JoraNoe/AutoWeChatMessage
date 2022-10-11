import Gaode
import WeChat
import requests

# APP的ID号
aappID = 'wxca51f7e17a0711e4'
# 安全秘钥
aappsecret = '64052c5932fc81571ed7ea8c7e40a6b7'

# 获取access_token
def getAccessToken():
    r1 = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": aappID,
            "secret": aappsecret
        }
    )
    access_token = r1.json()['access_token']
    # print(access_token)
    return access_token



# 获取用户列表信息

url = 'https://api.weixin.qq.com/cgi-bin/user/get'
parms02 = {
   'access_token':getAccessToken()
}
resultinfo = requests.get(url,params=parms02)
print(resultinfo.json())


        #["oB63O6s0JNpJPxOtiUDWnGMlMwpI","oB63O6mW5gDQKJyFk2FLXSBdph7E","oB63O6lPUOtE7JaaMfUWUd-9RR7Y"]

# 微信id列表 给谁发加谁
wx_id =  resultinfo.json()["data"]["openid"]
# 模板消息id
template_id =  'wZFt0cBQW9QJ4mh9P2dUqNAHdw2E9WIlFxoyUZP-_7s' #'iPqP0v0KvpQAP_1X_iv79EYpRyD7Q8TyznMV4FGW-no'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)

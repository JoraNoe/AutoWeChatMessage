import Gaode
import WeChat

# 微信id列表 给谁发加谁
wx_id = ["oB63O6s0JNpJPxOtiUDWnGMlMwpI","oB63O6mW5gDQKJyFk2FLXSBdph7E"]
# 模板消息id
template_id = 'iPqP0v0KvpQAP_1X_iv79EYpRyD7Q8TyznMV4FGW-no'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)

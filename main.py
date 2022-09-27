import Gaode
import WeChat

# 微信id列表 给谁发加谁
wx_id = ["oB63O6s0JNpJPxOtiUDWnGMlMwpI"]
# 模板消息id
template_id = 'GhJOek7M9_iVym2I-D1iVbnTrE8y0IhnfacYv9z6LGE'

# 获取天气数据
weatherData = Gaode.getWeather()

if __name__ == '__main__':
    for a_id in wx_id:
        WeChat.sendMessage(weatherData, a_id, template_id)

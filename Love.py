import requests

# 获取情话接口
def getLoveLanage():
        loveLanageResult = requests.get("https://api.1314.cool/words/api.php")
        return loveLanageResult.json()


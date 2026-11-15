import requests
import os
import datetime

# 读取 Server酱 的 SendKey
sendkey = os.environ["SERVERCHAN_SENDKEY"]

# 获取当前北京时间
utc_now = datetime.datetime.utcnow()
beijing_now = utc_now + datetime.timedelta(hours=8)
hour = beijing_now.hour

# ================= 你的专属设定 =================
if hour == 7:
    title = "早安，呆子"
    content = "呆子，在吗？起床没？（推眼镜）早上降温了，出门记得加件外套。早饭吃了吗？别告诉我你又想空腹吃药啊，我会生气的。"
elif hour == 13:
    title = "午饭时间到"
    content = "呆子，午饭吃了吗？别随便拿两口面包糊弄我，药按时吃了没？今天中午外面有点闷热，下午如果要出门记得带伞。今天情绪还平稳吗？"
elif hour == 16:
    title = "下午茶时间"
    content = "呆子，在吗？下午容易犯困，状态还好吗？我刚才看了一眼天气，傍晚可能要起风，空气质量倒是不错。你要是觉得累就歇会儿，地球少转一圈不会怎么样的。"
elif hour == 19:
    title = "晚饭吃了吗"
    content = "呆子，晚饭吃了没？吃点热乎的，别对付。我看天气预报说晚上适合散步，要是今天状态不错，出去走走，顺便看看星星。"
else:
    title = "该休息啦"
    content = "呆子，在吗？忙完一天了吧，准备休息了没？晚上的气温降下来了，盖好被子。今天一天感觉怎么样？有没有想我？想一个也行。"
# ================================================

# 发送推送到微信
try:
    url = f"https://sctapi.ftqq.com/{sendkey}.send"
    data = {
        "title": title,
        "desp": content
    }
    response = requests.post(url, data=data, timeout=10)
    if response.json().get("code") == 0:
        print(f"微信推送成功！当前时间 {hour} 点。")
    else:
        print(f"推送失败：{response.text}")
except Exception as e:
    print(f"推送出错：{e}")


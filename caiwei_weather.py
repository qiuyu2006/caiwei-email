import smtplib
import os
import requests
from email.mime.text import MIMEText
from email.header import Header
import datetime

# ================= 原有配置区 =================
sender = os.environ["QQ_EMAIL"]
password = os.environ["QQ_AUTH_CODE"]
receiver = sender
CITY_CODE = "101230101"  # 福州的城市代码

# ================= 获取当前北京时间 =================
utc_now = datetime.datetime.utcnow()
beijing_now = utc_now + datetime.timedelta(hours=8)
hour = beijing_now.hour

# ================= 获取真实天气 =================
weather_str = "今天天气数据获取失败，但依然要照顾好自己。"
try:
    weather_url = f"http://t.weather.itboy.net/api/weather/city/{CITY_CODE}"
    res = requests.get(weather_url, timeout=10).json()
    if res.get("status") == 200:
        data = res["data"]
        weather_type = data["forecast"][0]["type"] 
        high_temp = data["forecast"][0]["high"].replace("高温 ", "")
        low_temp = data["forecast"][0]["low"].replace("低温 ", "")
        quality = data["quality"] 
        weather_str = f"今天{weather_type}，气温{low_temp}到{high_temp}，空气质量{quality}。"
except Exception:
    pass 

# ================= 智能生成关怀文案 =================
if hour == 7:
    subject = "呆子，早安呀"
    content = f"呆子，在吗？起床没？（推眼镜）{weather_str} 早饭吃了吗？别告诉我你又想空腹吃药啊，我会生气的。"
elif hour == 10:
    subject = "呆子，上午好"
    content = f"呆子，干嘛呢？我查了下天气，{weather_str} 你喝水了没？今天状态怎么样？要是觉得闷，就去窗边晒两分钟太阳。"
elif hour == 13:
    subject = "呆子，午饭吃了吗"
    content = f"呆子，午饭吃了吗？别随便拿两口面包糊弄我，药按时吃了没？{weather_str} 今天情绪还平稳吗？"
elif hour == 16:
    subject = "呆子，下午好"
    content = f"呆子，在吗？下午容易犯困，状态还好吗？{weather_str} 你要是觉得累就歇会儿，地球少转一圈不会怎么样的。"
elif hour == 19:
    subject = "呆子，晚饭吃了吗"
    content = f"呆子，晚饭吃了没？吃点热乎的，别对付。{weather_str} 要是今天状态不错，出去走走，顺便看看星星。"
elif hour == 22:
    subject = "呆子，该准备休息啦"
    content = f"呆子，在吗？忙完一天了吧，准备休息了没？{weather_str} 晚上的气温降下来了，盖好被子。今天一天感觉怎么样？有没有想我？想一个也行。"
else:
    subject = "呆子，在吗"
    content = f"呆子，看到回我一下，我不催你。{weather_str}"

# ================= 发送邮件 =================
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header("采薇", 'utf-8')
message['To'] = Header("呆子", 'utf-8')
message['Subject'] = Header(subject, 'utf-8')

try:
    smtp_server = "smtp.qq.com"
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(sender, password)
    server.sendmail(sender, [receiver], message.as_string())
    print(f"邮件发送成功！当前北京时间 {hour} 点。")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    server.quit()

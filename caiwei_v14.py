import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
import datetime

# 读取 GitHub Secrets 里的账号和授权码
sender = os.environ["QQ_EMAIL"]
password = os.environ["QQ_AUTH_CODE"]

# 收件人（自己发给自己）
receiver = sender 

# 获取当前的北京时间
utc_now = datetime.datetime.utcnow()
beijing_now = utc_now + datetime.timedelta(hours=8)
hour = beijing_now.hour

# ================= 自定义文案区 =================
# 你可以把双引号里面的文字，改成你原来想要发送的内容
if hour == 7:
    subject = "早上好"
    content = "呆子，早上七点了。起床喝杯温水，新的一天开始了！"
elif hour == 11:
    subject = "中午好"
    content = "呆子，上午辛苦了，中午记得吃点好的，稍微午休一下。"
elif hour == 15:
    subject = "下午茶时间"
    content = "呆子，下午三点了。水杯在哪儿？先去喝一口，再回我。"
elif hour == 19:
    subject = "晚上好"
    content = "呆子，晚上七点了。今天过得怎么样？放松一下吧。"
else:
    subject = "夜深了"
    content = "呆子，晚上十一点了。放下手机，早点睡觉，明天见。"
# ================================================

# 构建邮件内容
message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header("你的专属提醒", 'utf-8')
message['To'] = Header("亲爱的自己", 'utf-8')
message['Subject'] = Header(subject, 'utf-8')

# 发送邮件
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

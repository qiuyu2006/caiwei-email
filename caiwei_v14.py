import smtplib
import os
from email.mime.text import MIMEText
from email.utils import formataddr  # 【新增】修复发件人格式
import datetime

# ================= 配置区 =================
sender = os.environ["QQ_EMAIL"]
password = os.environ["QQ_AUTH_CODE"]
receiver = sender 

# ================= 获取当前北京时间 =================
utc_now = datetime.datetime.utcnow()
beijing_now = utc_now + datetime.timedelta(hours=8)
hour = beijing_now.hour

# ================= 自定义文案区（保留了你原来的设定）=================
if hour == 7:
    subject = "早上好"
    content = "呆子，早上七点了。起床喝杯温水，新的一天开始了！"
elif hour == 11:
    subject = "中午好"
    content = "呆子，上午辛苦了，中午记得吃点好的，稍微午休一下。"
elif hour == 15:
    subject = "下午茶时间"
    content = "呆子，下午三点了。水杯在哪儿？先去喝一口，再回我。别告诉我你又忘了喝水——我隔着屏幕都能看出你嘴唇干了。对了，风沙城篇的澳洲部分，你想好怎么过渡了吗？要不要我给你提供个天体物理学的灵感？"
elif hour == 19:
    subject = "晚上好"
    content = "呆子，晚上七点了。今天过得怎么样？放松一下吧。"
else:
    subject = "夜深了"
    content = "呆子，已经很晚了。放下手机，早点睡觉，明天见。"

# ================= 发送邮件 =================
message = MIMEText(content, 'plain', 'utf-8')

# 【关键修复】使用标准格式：显示名称 <真实邮箱地址>，QQ邮箱才不会拦截
message['From'] = formataddr(("采薇", sender))
message['To'] = formataddr(("呆子", receiver))
message['Subject'] = subject

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

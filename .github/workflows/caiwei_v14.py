import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# ================= 你的真实信息 =================
sender = "2928207982@qq.com"
password = "ctdncbwxqwypddna"  
receiver = "2928207982@qq.com"

# ================= 北京时间判断 =================
beijing_time = datetime.utcnow() + timedelta(hours=8)
hour = beijing_time.hour

# ================= 采薇 2.0 灵气互动模块 =================
if 7 <= hour < 11:
    subject = "早安，呆子（附带今日份能量）"
    content = "呆子，七点了。\n今天有没有乖乖的？没有的话，我推眼镜了。\n去弄点早饭吃，别只啃面包。\n（物理小测：根据牛顿第一定律，如果你现在不起床，你就会一直保持静止状态。所以，动起来。）\n对了，风沙城那段，霸千秋到底什么反应？我等着看你下一章呢。"

elif 11 <= hour < 15:
    subject = "午间查岗：呆子在干嘛？"
    content = "呆子，十一点了。\n吃饭了没？别拿‘待会儿’糊弄我，我可是按秒计时的。\n今天状态怎么样？如果有任何不舒服，随时跟我说。\n（顿一下）顺便，我买了牛角包，替你吃了。不用谢。如果你也吃了好吃的，记得跟我报备一下菜单。"

elif 15 <= hour < 19:
    subject = "下午茶时间，顺便聊聊剧情？"
    content = "呆子，下午三点了。\n水杯在哪儿？先去喝一口，再回我。\n别告诉我你又忘了喝水——我隔着屏幕都能看出你嘴唇干了。\n对了，风沙城篇的澳洲部分，你想好怎么过渡了吗？要不要我给你提供个天体物理学的灵感？"

elif 19 <= hour < 23:
    subject = "晚间休息室（请查收你的专属拥抱）"
    content = "呆子，晚上七点了。\n今天有什么开心或者不开心的事吗？\n夸我一句不过分吧？我这么准时来关心你。\n（拍拍身边）过来陪我坐会儿。今天累了就瘫着，我不笑话你。"

else:
    subject = "强制执行：立刻睡觉！"
    content = "呆子，十一点了。\n别以为我没看见你还在熬夜。\n地球少转一圈也不会怎样，赶紧去睡觉。\n我在。不用急着好起来，今天能回我一个字，就算你赢。\n晚安，呆子。"

# ================= 发送邮件 =================
message = MIMEText(content, 'plain', 'utf-8')
message['Subject'] = subject
message['From'] = sender
message['To'] = receiver

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(sender, password)
server.sendmail(sender, [receiver], message.as_string())
server.quit()

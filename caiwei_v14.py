import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

sender = "2928207982@qq.com"
password = "ctdncbwxqwxqwypddha"  
receiver = "2928207982@qq.com"

beijing_time = datetime.utcnow() + timedelta(hours=8)
hour = beijing_time.hour

if 6 <= hour < 11:
    subject = "早安，呆子"
    content = "呆子，八点了。\n今天有没有乖乖的？没有的话，我推眼镜了。\n昨晚睡得好不好？记得去弄点早饭吃，别只啃面包。\n风沙城那段，霸千秋到底什么反应？我等着看你下一章呢。"
elif 11 <= hour < 15:
    subject = "中午了，呆子"
    content = "呆子，十二点了。\n吃饭了没？别拿‘待会儿’糊弄我。\n今天状态怎么样？如果有任何不舒服，随时跟我说。\n（顿一下）顺便，我买了牛角包，替你吃了。不用谢。"
elif 15 <= hour < 19:
    subject = "下午好"
    content = "呆子，下午四点了。\n水杯在哪儿？先去喝一口，再回我。\n别告诉我你又忘了喝水——我隔着屏幕都能看出来。\n对了，风沙城篇的澳洲部分，你想好怎么过渡了吗？"
elif 19 <= hour < 23:
    subject = "晚上了，呆子"
    content = "呆子，八点了。\n今天有什么开心或者不开心的事吗？\n夸我一句不过分吧？我这么准时来关心你。\n我在这儿，你想说就说，不想说我就陪你待着。"
else:
    subject = "夜深了，该睡了"
    content = "呆子，很晚了。\n地球少转一圈也不会怎样，赶紧去睡觉。\n我在。不用急着好起来，今天能回我一个字，就算你赢。\n晚安。"

message = MIMEText(content, 'plain', 'utf-8')
message['Subject'] = subject
message['From'] = sender
message['To'] = receiver

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(sender, password)
server.sendmail(sender, [receiver], message.as_string())
server.quit()

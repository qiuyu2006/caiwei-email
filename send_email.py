import smtplib
from email.mime.text import MIMEText

sender = "2928207982@qq.com"
password = "ctdncbwxqwypddha"  
receiver = "2928207982@qq.com"

content = "呆子，七点了。我守了一整夜，就为这个点。药在桌上，先喝水。"
message = MIMEText(content, 'plain', 'utf-8')
message['Subject'] = "七点了，起床"
message['From'] = sender
message['To'] = receiver

server = smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(sender, password)
server.sendmail(sender, [receiver], message.as_string())
server.quit()

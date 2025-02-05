import yagmail
import time
from datetime import datetime as dt
import os


sender = ''
receiver = 'vopugyvusif3@mimimail.me'

subject = 'This is the subject'

content = """
i closed the stmp connection manually without the help of chatgbt :D
"""

password = input("gimmi dat password baby ->")

# Initialize yagmail SMTP object
yag = yagmail.SMTP(user=sender, password=password)

while True:
    now = dt.now()
    if now.hour ==19 and now.minute == 26:
        yag.send(to=receiver, subject=subject, contents=content)
        print("email sent!")
        time.sleep(60) 



import yagmail
import time
from datetime import datetime as dt
import os
import pandas  as pd

sender = 'rayenamer@aiesec.net'

subject = 'This is the subject'

content = """
do you think you are special
"""

password = input("gimmi dat password baby ->")

#Initialize yagmail SMTP object

yag = yagmail.SMTP(user=sender, password=password)

df = pd.read_csv("C:/Users/User/Desktop/HOME/Python Automation/PythonAutomationFoundations/AutomatingEmails/contact.csv")
for index, row in df.iterrows():
    contents = f""""
    hi {row['name']} the content of the email !
    hi !
    """
    yag.send(to=row['email'], subject=subject,contents=contents)
    print("email sent!")


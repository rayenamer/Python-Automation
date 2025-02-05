import yagmail

sender = ''
receiver = 'vopugyvusif3@mimimail.me'

subject = 'This is the subject'

content = """
i closed the stmp connection manually without the help of chatgbt :D
"""

password = input("gimmi dat password baby ->")

# Initialize yagmail SMTP object
yag = yagmail.SMTP(user=sender, password=password)

# Send the email
yag.send(to=receiver, subject=subject, contents=content)

# Print confirmation
print("email sent!")

yag.close()

print("connection closed")

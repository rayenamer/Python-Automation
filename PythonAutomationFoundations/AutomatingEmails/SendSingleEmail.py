import yagmail

sender = ''
receiver = 'vopugyvusif3@mimimail.me'

subject = 'This is the subject'

contents = ["""
Here is the content of the email! 
Hi!
""", 'text.txt']

password = input("gimmi dat password baby ->")

# Initialize yagmail SMTP object
yag = yagmail.SMTP(user=sender, password=password)

# Send the email
yag.send(to=receiver, subject=subject, contents=contents)

# Print confirmation
print("email sent!")

yag.close()

print("connection closed")

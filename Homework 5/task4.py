import smtplib


def prompt(prompt):
    return input(prompt).strip()


login = prompt("Login: ")
password = prompt("Password: ")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(login, password)
server.set_debuglevel(1)

fromaddr = prompt("From: ")
toaddrs = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")
# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n" % (fromaddr, ", ".join(toaddrs)))

# with input() as line:
#     msg = msg + line
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line
print("Message length is", len(msg))

server.sendmail(fromaddr, toaddrs, msg)
server.quit()

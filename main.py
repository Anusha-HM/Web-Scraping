import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
content = ''


def extract_news(url):
    print("Extracting Hacker News stories......")
    cnt = '<b>HN Top Stories:</b><br>' + '-' * 25 + '<br>'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Hacker News story titles are in <span class="titleline">
    story_num = 1
    for tag in soup.find_all('span', attrs={'class': 'titleline'}):
        link = tag.find('a')
        if link:
            title = link.text
            href = link.get('href', '#')
            cnt += f'{story_num}:: <a href="{href}">{title}</a><br>'
            story_num += 1

    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += '<br>---------<br>'
content += '<br><br>End of Message'

print("Composing email....")
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'XYZ@gmail.com'
TO = 'ABC@gmail.com'
PASS = 'XYZ'

msg = MIMEMultipart()
msg['Subject'] = f'Top NEWS Stories HN (Automated) {now.day}-{now.month}-{now.year}'
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))

print("Initiating server....")
server = smtplib.SMTP(SERVER, PORT)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())
print("Email sent!")
server.quit()

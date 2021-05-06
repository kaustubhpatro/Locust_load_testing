from Screenshot import Screenshot_Clipping
from selenium import webdriver
import os
import slack
from slack.errors import SlackApiError

# get html file page and take full page screenshot
ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome(executable_path='/home/kaustubhpatro/Downloads/chromedriver_linux64/chromedriver')
url = "file:///home/kaustubhpatro/PycharmProjects/Cnvrg_Locust_old/report.html"
driver.get(url)
img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='screenshot.png')
driver.close()
driver.quit()

# init slack client with access token
slack_token = os.environ['SLACK_TOKEN']
client = slack.WebClient(token=slack_token)

# upload file
try:
    response = client.files_upload(
        file='screenshot.png',
        initial_comment='This space ship needs some repairs I think...',
        channels='random'
    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")

import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from fake_headers import Headers
from webdriver_manager.firefox import GeckoDriverManager
import json
import os

username = input("user: ")
class Instagram:
    @staticmethod
    def scrap(username):
            driver = webdriver.Firefox()
            driver.get('https://instagram.com/{}'.format(username))
            wait = WebDriverWait(driver, 10)
            wait.until(EC.title_contains('@'))

            #data to collect
            data = driver.execute_script('return window._sharedData')['entry_data']
            is_private = data['ProfilePage'][0]['graphql']['user']['is_private']
            profile_page = data['ProfilePage'][0]['graphql']['user']
            bio = profile_page['biography']
            followings = profile_page['edge_follow']['count']
            followers= profile_page['edge_followed_by']['count']
            posts_count = profile_page['edge_owner_to_timeline_media']['count']
            profile_image = profile_page['profile_pic_url_hd']

            #output
            profile_data = {
                'profile_image' : profile_image,
                'bio' : bio,
                "posts_count" : posts_count,
                "followers" : followers,
                "followings" : followings,
                "is_private" : is_private
                }
            driver.close()
            driver.quit()
            return json.dumps(profile_data)

if __name__ == '__main__':
    print(Instagram.scrap(username))

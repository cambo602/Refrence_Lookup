from selenium import webdriver
import time
import random

sport = input('What sport?: ')
player = input('What player?: ')
yearCareer = input('Year or Career?: ')

goalie = "Hi"


class getStats():
    def __init__(self):
        s = sport
        p = player
        self.driver = webdriver.Chrome(
            "C:/Users/Camer/Documents/chromedriver.exe")
        if s.lower() == 'baseball':
            self.driver.get('https://www.baseball-reference.com/')
            self.driver.maximize_window()
            playerSearch = self.driver.find_element_by_name("search")

            playerSearch.send_keys(p)

            search = self.driver.find_element_by_xpath(
                '//*[@id="header"]/div[3]/form/input[1]')

            search.click()

            if yearCareer == 'c':

                WAR = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[1]/p[2]').text

                print('rWar ' + WAR)

                ab = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[2]/p[2]').text

                print('AB ' + ab)

                hits = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[3]/p[2]').text

                print('H ' + hits)

                hr = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[4]/p[2]').text

                print('HR ' + hr)

                ba = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[5]/p[2]').text

                print('BA ' + ba)

                hrab = int(ab)/int(hr)

                print('AB/HR ' + str(hrab))

                rbi = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[3]/div[2]/p[2]').text

                print('RBI ' + rbi)

                slg = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[4]/div[2]/p[2]').text

                print('SLG ' + slg)

                opsplus = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[4]/div[4]/p[2]').text

                print('OPS+ ' + opsplus)

            if yearCareer == 'y':

                WAR = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[1]/p[1]').text

                print('rWar ' + WAR)

                ab = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[2]/p[1]').text

                print('AB ' + ab)

                hits = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[3]/p[1]').text

                print('H ' + hits)

                hr = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[4]/p[1]').text

                print('HR ' + hr)

                ba = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[2]/div[5]/p[1]').text

                print('BA ' + ba)

                hrab = int(ab)/int(hr)

                print('AB/HR ' + str(hrab))

                rbi = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[3]/div[2]/p[1]').text

                print('RBI ' + rbi)

                slg = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[4]/div[2]/p[1]').text

                print('SLG ' + slg)

                opsplus = self.driver.find_element_by_xpath(
                    '//*[@id="info"]/div[4]/div[4]/div[4]/p[1]').text

                print('OPS+ ' + opsplus)

        elif s.lower() == 'hockey':
            self.driver.get('https://www.hockey-reference.com/')

            playerSearch = self.driver.find_element_by_name("search")
            self.driver.maximize_window()
            playerSearch.send_keys(p)

            search = self.driver.find_element_by_xpath(
                '//*[@id="header"]/div[3]/form/input[1]')

            search.click()

            #goalie = self.driver.find_element_by_xpath('//*[@id="meta"]/div[2]/p[1]/text()[1]').text

            if goalie == "G":
                print("Goalie KekW")
            else:
                if yearCareer == 'c':

                    gp = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[1]/p[2]').text

                    print('GP ' + gp)

                    goals = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[2]/p[2]').text

                    print('G ' + goals)

                    ass = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[3]/p[2]').text

                    print('A ' + ass)

                    PTS = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[4]/p[2]').text

                    print('PTS ' + PTS)

                    plusmin = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[5]/p[2]').text

                    print('+/- ' + plusmin)

                    ppg = int(PTS)/int(gp)

                    print('PPG ' + str(ppg))

                if yearCareer == 'y':

                    gp = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[1]/p[1]').text

                    print('GP ' + gp)

                    goals = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[2]/p[1]').text

                    print('G ' + goals)

                    ass = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[3]/p[1]').text

                    print('A ' + ass)

                    PTS = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[4]/p[1]').text

                    print('PTS ' + PTS)

                    plusmin = self.driver.find_element_by_xpath(
                        '//*[@id="info"]/div[4]/div[2]/div[5]/p[1]').text

                    print('+/- ' + plusmin)

                    ppg = int(PTS)/int(gp)

                    print('PPG ' + str(ppg))


player = getStats()

import requests
import logging
from bs4 import BeautifulSoup

# lmp_dict = {}
# # “DPL”:””,
# # “COMED”:””,
# # “AEP”:””,
# # “EKPC”:””,
# # “PEP”:””,
# # “JC”:””,
# # “PL”:””,
# # “DOM”:””
# # }
#
# def main():
#     try:
#         URL = "http://stuffin.space/?intldes=2003-058A&search=2003-058"
#         page = requests.get(URL)
#         soup = BeautifulSoup(page.content, "html.parser")
#         print(soup)
#         for i in soup.find_all("div", class_="sat-info-row", recursive=True):
#             divs = i.findChildren("div")
#             print(divs)
#             j = 0
#             while j < len(divs):
#                 value = divs[j].text
#                 if value in lmp_dict:
#                     lmp_dict[value] = divs[j + 1].text
#                 j += 1
#         print(lmp_dict)
#     except Exception as e:
#         raise e
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google-analytics.com/j/collect?v=1&_v=j87&a=612748086&t=pageview&_s=1&dl=http%3A%2F%2Fstuffin.space%2F%3Fintldes%3D2003-058A%26search%3D2003-058&ul=en-us&de=UTF-8&dt=Stuff%20in%20Space&sd=24-bit&sr=1536x864&vp=558x674&je=0&_u=AACAAEABAAAAAC~&jid=673580454&gjid=857716351&cid=1390232387.1611775439&tid=UA-64721672-1&_gid=1226326757.1611775439&_r=1&_slc=1&z=1904247135")
l = driver.find_element_by_id("sat-infobox")
ll = l.find_elements_by_class_name("sat-info-row")
print(ll.pop())

# mucho_cheese = driver.current_window_handle.
# print(mucho_cheese)
# if __name__ == "__main__":
#     main()



from urllib.request import urlopen
import re
url = "http://stuffin.space/?intldes=2003-058A&search=2003-058"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
# import mechanicalsoup
#/
# browser = mechanicalsoup.Browser()
# page = browser.get("http://stuffin.space/?intldes=2003-058A&search=2003-058")
# tag = page.soup.children
# # result = tag.altitude
# html = list(tag)[1]
# # page.text
# print(list(html.children))
#
# # print(f"The altitude is: {result}")
# # print(page.content)
# # print(page.text)


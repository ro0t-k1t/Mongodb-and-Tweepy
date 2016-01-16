__author__ = 'ronanpiercehiggins'

from urllib2 import urlopen
import re

my_address = "https://en.wikipedia.org/wiki/Web_scraping"
html_page = urlopen(my_address)
html_text = html_page.read()

start_tag = '<title>'
end_tag = '</title>'

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print html_text[start_index:end_index]

print re.findall("ab*c", "ac")

a_string = "Everything we do is <replaced> if it is indeed inside <tags>."

a_string = re.sub("<.*?>", "coming up roses", a_string)

print a_string


results = re.search("ab*c", "ABC", re.IGNORECASE)
print results.group()


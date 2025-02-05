import pyperclip as clip
import re

# regex_search = re.compile(r"[^\*].*")
regex_search = re.compile(r"[^\▢].*")

clipboard = clip.paste()

html_list = ''

for line in clipboard.splitlines():
    regex_match = regex_search.search(line)
    html_list += (f"'{regex_match[0]}',")

clip.copy(html_list)
print('CONVERTED SUCCESFULLY')

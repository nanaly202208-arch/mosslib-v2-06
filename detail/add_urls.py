import re
import os
from urllib.parse import quote

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'm.html')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match items like: { text: "...", source: "..." }
pattern = r'\{\s*text:\s*"([^"]*?)"\s*,\s*source:\s*"([^"]*?)"\s*\}'

count = 0
def count_replacer(match):
    global count
    count += 1
    text = match.group(1)
    source = match.group(2)
    encoded_text = quote(text, safe='')
    url = f"https://www.google.com/search?q={encoded_text}"
    return f'{{ text: "{text}", source: "{source}", url: "{url}" }}'

result = re.sub(pattern, count_replacer, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"修改完成，共处理 {count} 条数据")

import re

with open(r'D:\Work\新译\项目\Mosslib 2.0\分析模块\原型\0601\mosslib-v2-0602\detail\chat.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the his-view structure
idx = content.find('class="his-view')
print(f'his-view found at position: {idx}')

# Show 2000 chars context
if idx > 0:
    print(f'\n=== Context around his-view (2000 chars after) ===')
    print(content[idx:idx+2000])

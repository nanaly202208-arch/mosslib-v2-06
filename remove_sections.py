filepath = r'D:\Work\新译\项目\Mosslib 2.0\分析模块\原型\0601\mosslib-v2-0602\detail\MossLib.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find "最新内容" section start and end
start_marker = '<div data-v-ced27253="" class="flex-column pl-10px pr-10px">\n<div data-v-ced27253="" class="list-title-view mb-10px pl-10px font-bold">最新内容</div>'
end_marker = '<div data-v-ced27253="" class="flex-column pl-10px pr-10px mb-16px">'

start_pos = content.find(start_marker)
end_pos = content.find(end_marker, start_pos)

if start_pos > 0 and end_pos > start_pos:
    # Remove from start_marker to before end_marker
    content = content[:start_pos] + content[end_pos:]
    print(f"Removed '最新内容' section and its divider")
else:
    print(f"Could not find boundaries: start={start_pos}, end={end_pos}")

# Now find and remove "相关推荐" section
rel_start_marker = '<div data-v-ced27253="" class="flex-column pl-10px pr-10px mb-16px">\n<div data-v-ced27253="" class="list-title-view mb-10px ml-10px font-bold">相关推荐</div>'
rel_start = content.find(rel_start_marker)

if rel_start > 0:
    # Find the end: look for </div></div></div><div class="fullscreen-search-detail-dialog"
    # or multiple </div> that close this section
    # Structure: ...</div></div></div><div class="fullscreen...
    # The section ends with the closing </div> of its container and the right-view closing
    # Let's look for the pattern after 相关推荐 that leads to the next section
    closing_pattern = '</div>\n</div>\n</div>\n<div class="fullscreen-search-detail-dialog-modal'
    closing_pos = content.find(closing_pattern, rel_start)
    
    if closing_pos > 0:
        # Remove from rel_start to closing_pos
        content = content[:rel_start] + content[closing_pos:]
        print(f"Removed '相关推荐' section")
    else:
        # Try alternative: find closing of right-view after this section
        right_view_close = content.find('</div>\n</div>\n</div>\n</section>\n<div class="el-overlay is-drawer"', rel_start)
        if right_view_close > 0:
            content = content[:rel_start] + content[right_view_close:]
            print("Removed '相关推荐' section (alt method)")
        else:
            print("Could not find end of 相关推荐 section - searching from", rel_start)
            # Show context
            print(content[rel_start:rel_start+500])

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")

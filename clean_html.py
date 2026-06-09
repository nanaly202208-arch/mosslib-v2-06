with open('detail/detail.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find key line numbers
start_line = None
end_line = None
drawer_html = ''

for i, line in enumerate(lines):
    if 'class="detail-main-view' in line:
        start_line = i

# Extract entity-drawer HTML (line 4705 to line 4712+ in original)
# Find it by content
for i, line in enumerate(lines):
    if '<!-- 实体详情抽屉 -->' in line:
        # Extract from here until we hit </section>
        j = i
        drawer_lines = []
        while j < len(lines):
            drawer_lines.append(lines[j])
            if '</section>' in lines[j]:
                break
            j += 1
        drawer_html = '\n'.join(drawer_lines)
        end_line = j
        break

if start_line is None:
    print("ERROR: Could not find main content")
    exit(1)

main_lines = lines[start_line:end_line+1]

# Clean main content
import re
main_content = ''.join(main_lines)
main_content = re.sub(r' data-v-[a-zA-Z0-9-]+=""', '', main_content)
main_content = re.sub(r'<!--v-if-->', '', main_content)
main_content = re.sub(r'<!---->', '', main_content)

# Extract custom script and CSS
content = ''.join(lines)

# Custom JS: from function highlightEntityInArticle to the document.addEventListener + closing
script_start = content.find('function highlightEntityInArticle')
script_end = content.find('\n}\n\n</script>', script_start)
if script_end == -1:
    script_end = content.find('</script>', script_start)
custom_js = content[script_start:script_end]

# Custom CSS: in the <style> block after </script> 
style_start = content.find('</script>\n\n<style>')
style_end = content.find('</style>', style_start)
custom_css = content[style_start+len('</script>\n\n<style>'):style_end]

# CSS links (in detail/detail.html they point to ./detail_files/ which is detail/detail_files/)
css_links = re.findall(r'<link rel="stylesheet" href="\./MossLib_files/[^"]*\.css">', content)
# Keep path as ./MossLib_files/ since we have a copy at root too

result = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>MossLib</title>
<style>
.related-card-subtitle { display: flex; align-items: center; gap: 4px; }
.related-card-subtitle .translate-icon { width: 14px; height: 14px; flex-shrink: 0; color: #999; }
.translate-icon use { width: 14px; height: 14px; }
</style>
''' + '\n'.join(css_links) + '''
<script>
''' + custom_js + '''
</script>
<style>
''' + custom_css + '''
</style>
</head>
<body>
''' + main_content + '''
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(result)

print("Done!")
print("Main content:", len(main_content), "chars")
print("Custom JS:", len(custom_js), "chars")
print("Custom CSS:", len(custom_css), "chars")
print("CSS links:", len(css_links))

import re

with open('detail/MossLib.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove data-v-* attributes
html = re.sub(r' data-v-[a-zA-Z0-9-]+=""', '', html)

# Remove <!--v-if--> comments
html = re.sub(r'<!--v-if-->', '', html)

# Remove <!--  --> comments (non-v-if ones)
html = re.sub(r'<!--(?!\s*\[)(?!\s*<!)(?!\s*\])(?!\s*-->)(.*?)-->', '', html)

# Remove empty <!--v-if--> lines
html = re.sub(r'<!---->', '', html)

# Remove external script tags that reference .下载 files
html = re.sub(r'<script\s+[^>]*src="[^"]*\.下载"[^>]*>\s*</script>\s*', '', html)

# Remove link rel=modulepreload
html = re.sub(r'<link\s+rel="modulepreload"[^>]*>', '', html)

# Remove link to css files in MossLib_files (we'll inline the needed ones)
html = re.sub(r'<link\s+rel="stylesheet"\s+href="\./MossLib_files/[^"]*"[^>]*>\s*', '', html)

# Remove <link rel="icon" ...> tags that reference external
html = re.sub(r'<link\s+rel="icon"[^>]*>', '', html)

# Remove empty lines
lines = html.split('\n')
lines = [l for l in lines if l.strip()]
html = '\n'.join(lines)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! index.html created successfully.")

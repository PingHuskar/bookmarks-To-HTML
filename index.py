import re
import time

def toDate(epoch):
    try:
        # return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch)))
        return time.strftime('%Y-%m-%d', time.localtime(int(epoch)))
    except Exception:
        return ""

f = open('data.txt','r+',encoding='utf-8')
h = open('index.html','w+',encoding='utf-8')

# Start customize here
title = ""
target = "blank"
fr = f.readlines()

cols = ['name','href','group','date','epoch']
cols.remove("href")
# End customize here
rows = []
for i in fr:
    i = i.strip()
    try: q = re.match('<DT><H3 ADD_DATE="\d+" LAST_MODIFIED="\d+">(.+?)</H3>',i).group(1)
    except Exception: pass
    try: qq = re.match('<DT><A HREF="(.+?)" ADD_DATE="(.+?)">(.+?)</A>',i)
    except Exception: pass
    try:
        group = q
    except Exception: pass
    try:
        href = qq.group(1)
        epoch = re.match('^\d+',qq.group(2)).group()
        newDate = toDate(epoch)
        name = qq.group(3)
        rows.append(f'''<tr>
            <td><a href="{href}" target="_{target}">{name}</a></td>
            <td>{group}</td>
            <td>{newDate}</td>
            <td>{epoch}</td>
</tr>''')
#         rows.append(f'''<tr>
#             <td>{name}</td>
#             <td>{href}</td>
#             <td>{group}</td>
#             <td>{newDate}</td>
#             <td>{epoch}</td>
# </tr>''')
    except Exception: pass
strRows = "\n".join(rows)
# print(rows)
# print(strRows)
table = f"""<table class="w3-table-all w3-margin-top" id="myTable">
<tr>
{"".join([f'<th style="width:{round(100/len(cols),2)}%;">{i}</th>'.replace(".0","") for i in cols])}
</tr>
{strRows}
</table>"""
body = f"""<div class="w3-container">
  <h2>Filter Table</h2>
  <p>Search for a name in the input field.</p>
  
  <input class="w3-input w3-border w3-padding" type="text" placeholder="Search for names.." id="myInput" onkeyup="myFunction()">
  {table}
</div>"""
h.writelines(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="./w3.css">
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    {body}
    <script src="./script.js"></script>
</body>
</html>""")
f.close()
print("done")
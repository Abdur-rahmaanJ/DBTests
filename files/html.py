# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:25:15 2018

@author: Zeenat
"""
from random import *
skeleton_s ="""
<!DOCTYPE html>
<html>
<style type="">
img{border:5px solid black; border-radius:10px;width:50px; height:50px;}
*{margin:10px; text-align:center;}
.link-outer{border:5px solid black;}
</style>
<head>
	<title></title>
</head>
<body>
"""
skeleton_e = """
</body>
</html>
"""


from db_engine import DB

db = DB()

data = db.view_db('links')
# <span class="img__body" style="background-image: url(https://chat.whatsapp.com/invite/icon/FaXlieEBYiH4pFTXqO6lWe);"></span>
with open('output/sample_gen3.html','w+') as f:
    f.write(skeleton_s)
    for elem in data:
        name = elem[0]
        link = elem[1]
        placeholder = ''
        if link.strip() == '':
            placeholder = '--- unavailable ---'
        else:
            placeholder = link
        image_link = 'https://chat.whatsapp.com/invite/icon/'+link.split('/')[-1]
        
        text = ('''
                    <div class="link-outer">
                        <div class="group-name">{}</div>
                        <div class="group-image"><img src="{}"/></div>
                        <div class="group-link"><a href="{}">{}</a></div>
                    </div>'''.format(name, image_link, link, placeholder))
        print(image_link)
        f.write(text)
    f.write(skeleton_e)
    
print('*** generated ***')
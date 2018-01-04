# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:26:36 2018

@author: ARJ

p .class #id{
    
}
"""

s = """
p .class #id
{
    i was in an #class{here}
}
d = {'x':1, 'y':2003}

for key, value in d.items():
    print(key,value)
"""

import json
    
class DB:
    def __init__(self):
        self.db_folder = 'databases/'
        self.d = {}
        
    
    def create_db(self, name):
        with open(self.db_folder+name+'.json', 'w') as f:
            f.write('{}')
            f.close()
    
    def add_record(self, db, l_val, r_val):
        with open(self.db_folder+db+'.json', 'r') as f:
            self.d = json.load(f)
            self.d[l_val] = r_val
        j = json.dumps(self.d, indent=4)
        with open(self.db_folder+db+'.json', 'w') as f:
            f.write(j)


    def delete_record(self, db, record):
        with open(self.db_folder+db+'.json', 'r') as f:
            self.d = json.load(f)
        self.d.pop(record, None)
        j = json.dumps(self.d, indent=4)
        with open(self.db_folder+db+'.json', 'w') as f:
            f.write(j)
    
    def delete_db(self, db):
        pass
    
    def view_db(self, db):
        all_data = []
        with open(self.db_folder+db+'.json', 'r') as f:
            self.d = json.load(f)
            for key, value in self.d.items():
                #print(key,value)
                all_data.append([key,value])
        return all_data
                
    def add_csv(self):
        pass
    
#db = DB()
#db.create_db('ccc')
#db.add_record('ccc', 'x', '1')
#db.view_db('links')
#x = 1
"""
while x == 1:
    z = input('> ')
    if z == 'exit':
        x = 0
print('exited')
"""
    
    



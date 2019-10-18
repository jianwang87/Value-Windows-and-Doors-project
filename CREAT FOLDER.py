# This function creat the folder at the destination
'''rename the file name and the path everytime when you use'''

import os
newpath = r'C:\Users\Sales 2\Desktop\Jian\Messurements\10182019_Mario_door' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

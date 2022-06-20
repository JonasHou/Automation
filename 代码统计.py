#encoding=utf-8
import os
#dir_path = raw_input("Please input the folder name which your python code in:")
dir_path = r"D:\pythonstudy\lianxi"
def caculate_line():    
    count_file = 0    
    count_line = 0    
    for root, dirs, files in os.walk(dir_path):                          for file in files:            
            if ".py" in file:                
                count_file += 1                
                with open(os.path.join(root, file), "r") as fp:  
                    for line in fp:                                                      if "#" not in line:                                                  if line.strip():                                                     count_line += 1    
    return count_file,count_line
print u"统计的python文件个数为：",caculate_line()[0]
print u"统计的python代码行数为：",caculate_line()[1]
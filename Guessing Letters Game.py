import os
import string
import random

letter = random.choice(string.ascii_lowercase)
for i in range(1, 6):
    word = input("请输入一个小写字母：")
    if (word.islower()):
        if (word == letter):
            print("已回答" + str(i) + "次，答题成功！")
            letter = True
            break
        elif (word < letter):
            print("你猜小了！")
        elif (word > letter):
            print("你猜大了！")
    else:
        print("不是小写字母")
if (i == 5 and letter != True):
    print("已回答5次，答题失败！\n正在自动下载原神……")
    os.system('"C:/Program Files/Internet Explorer/iexplore.exe" '
              'https://ys-api.mihoyo.com/event/download_porter/link/ys_cn/official/pc_default')
input()
    

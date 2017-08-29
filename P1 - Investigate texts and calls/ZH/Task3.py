"""
Python入门 项目 1, 任务 0

完成该任务的文件中的每个任务. 以压缩文件提交整个文件夹或是GitHub repo。
在项目准备页面上有完整的提交说明。
"""


"""
读取短信与电话。
如果你不知道如何读取文件，也是可以的
您将在以后的课程中了解更多有关阅读文件的知识
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。 

第一部分: 找出由班加罗尔地区拨出的所有电话的区号和移动前缀（代码）。
 - 	固定电话以括号内的区域代码开始。区号的长度不定，但总是以0开始。
 - 	移动线路以包含在号码中的区号开始并且没有括号，
 	但数字中间添加了一个空格，以增加可读性。
 	一个移动电话的移动前缀指的是他的前四个数字，并且以7,8或9开头。
 -	电话促销员的号码没有括号或空格 , 但以140开头。
   
将答案以如下信息的一部分打印出来:
"由班加罗尔地区的人打出的电话含有如下代码："
 <代码的列表>
代码列表应该无重复，每行一条，并以字典序输出。
由位于班加罗尔的固定电话打出的电话号码，以及由班加罗尔固话打往班加罗尔的电话所占比例。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

将答案以如下信息的一部分打印出来:
"<多少>%的通话是由班加罗尔的固定电话拨往班加罗尔的固定电话的。"
注意：百分比应包含2位小数。
"""
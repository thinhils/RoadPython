# 身份证匹配案例
import re

# 待匹配字符串
str1 = '110101198001017032'  # 18位身份证号
str2 = '1101011980010170'    # 16位字符串

# 模式字符串
p1 = '^[1-9]\d{13,16}[0-9x]$'
p2 = '^[1-9]\d{14}(\d{2}[0-9x])?$'
p3 = '^([1-9]\d{16}[0-9x]|[1-9]\d{14})$'

# 模式字符串异常 - 同时可匹配多个场景的情况
# 有效的身份证号可以匹配：18位
print("-----------------有效身份证----------------------")
m = re.match(p1, str1)
print(m.group(0))
# 无效的省份证号，也可以匹配 16位数字
print("-----------------非有效身份证----------------------")
m = re.match(p1, str2)
print(m.group(0))

# 模式字符串优化：
# 约束后3位出现的次数为：0-1次; 15+3
print("-----------------增加后三位约束----------------------")
# p2 = '^[1-9]\d{14}(\d{2}[0-9x])?$'
print(re.match(p2, str2))

print("-----------------先匹配情况1，如果失败再匹配情况2------------------")
# p3 = '^([1-9]\d{16}[0-9x]|[1-9]\d{14})$'
m = re.match(p3, str1)
print(m.group(0))

m = re.match(p3, str2)
print(m)


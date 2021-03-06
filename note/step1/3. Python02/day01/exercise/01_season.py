# 练习:
#   写程序，实现以下需求:
#     将如下数据形成一个字典seasons
#        '键'    '值'
#        1       '春季有1,2,3月'
#        2       '夏季有4,5,6月'
#        3       '秋季有7,8,9月'
#        4       '冬季有10,11,12月'
#     让用户输入一个整数代表这个季度，打印这个季度的信息，如果用户输入的信息不在字典的键内，则打印信息不存在

seasons = {1: '春季有1,2,3月',
           2: '夏季有4,5,6月',
           3: '秋季有7,8,9月',
           4: '冬季有10,11,12月'
          }

n = int(input("请输入季度(1~4): "))

# 方法1
# if n in seasons:
#     print(seasons[n])
# else:
#     print("输入有误！")

# 方法2
print(seasons.get(n, "输入有误!"))
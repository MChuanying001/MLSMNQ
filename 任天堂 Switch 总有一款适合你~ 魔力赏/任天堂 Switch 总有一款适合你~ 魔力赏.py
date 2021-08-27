import time
import random


#开始进入Python的世界
# 变量归零
许愿结果 = 0
抽奖 = 0
许愿1 = 0
分钟 = 0
小时 = 0
许愿 = 0
变量 = 0
print('魔力赏模拟器')
time.sleep(1)
print('载入配置')
time.sleep(1)
print('任天堂 Switch 总有一款适合你~ 魔力赏')
time.sleep(1)
print('当前进度-0%')
time.sleep(1)
print('当前进度-23.33%')
time.sleep(1)
print('当前进度-66.66%')
time.sleep(1)
print('当前进度-100.00%')
time.sleep(1)
print('配置载入成功')
time.sleep(1)
print('请支付 633 魔石', '支付请按1')
变量 += int(input('确认支付？'))
if (变量 == 1):
    # 开始设置各项数值
    print('请设置星座，详见“星座.txt”')
    许愿 += int(input('你的星座？'))
    if (许愿 <= 12 and 许愿 >= 1):
        print('请设置时间-小时')
        小时 += int(input('请输入'))
        if (小时 <= 23 and 许愿 >= 0):
            print('请设置时间-分钟')
            分钟 += int(input('请输入'))
            if (分钟 <= 59 and 分钟 >= 0):
                print('请设置许愿款，详见“许愿.txt”')
                许愿1 += int(input('请输入许愿款'))
                许愿结果 += 许愿1
                if (许愿1 <= 12 and 许愿1 >= 1):
                    print('执行抽奖中')
                    time.sleep(1)
                    抽奖 += random.randint(1, 10000)
                    # 抽奖中
                    # 以下为中奖类型
                    if (抽奖 <= 196 and 抽奖 >= 50):
                        print('隐藏款！！！！')
                        time.sleep(1)
                        隐藏 = 0
                        隐藏 += random.randint(1, 3)
                        if (隐藏 == 1):
                            print('奖品：超级马里奥：奥德赛')
                            if (许愿结果 == 7):
                                print('愿望实现')
                        elif (隐藏 == 2):
                            print('奖品：超级马里奥：兄弟U 豪华版')
                            if (许愿结果 == 8):
                                print('愿望实现')
                        else:
                            print('奖品：马里奥赛车8 豪华版')
                            if (许愿结果 == 9):
                                print('愿望实现')
                    elif (抽奖 <= 686 and 抽奖 >= 197):
                        print('欧皇款！！')
                        time.sleep(1)
                        欧皇 = 0
                        欧皇 += random.randint(1, 5)
                        if (欧皇 == 1):
                            print('奖品：Joycon左红右蓝')
                            if (许愿结果 == 2):
                                print('愿望实现')
                        elif (欧皇 == 2):
                            print('奖品：Joycon左紫右橙')
                            if (许愿结果 == 5):
                                print('愿望实现')
                        elif (欧皇 == 3):
                            print('奖品：Joycon左粉右绿')
                            if (许愿结果 == 3):
                                print('愿望实现')
                        elif (欧皇 == 4):
                            print('奖品：Joycon左蓝右黄')
                            if (许愿结果 == 4):
                                print('愿望实现')
                        else:
                            print('奖品：任天堂Switch专业手柄')
                            if (许愿结果 == 6):
                                print('愿望实现')
                    elif (抽奖 <= 49 and 抽奖 >= 1):
                        print('超神款！！！！！！')
                        time.sleep(1)
                        print('奖品：任天堂Switch国行灰色')
                        if (许愿结果 == 1):
                            print('愿望实现')
                    else:
                        print('普通款')
                        time.sleep(1)
                        普通 = 0
                        普通 += random.randint(1, 3)
                        if (普通 == 1):
                            print('奖品：精灵球保护盒-红色')
                            if (许愿结果 == 11):
                                print('愿望实现')
                        elif (普通 == 2):
                            print('奖品：精灵球保护盒-黑色')
                            if (许愿结果 == 10):
                                print('愿望实现')
                        else:
                            print('奖品：皮卡丘保护盒')
                            if (许愿结果 == 12):
                                print('愿望实现')
                else:
                    print('退出')
                    time.sleep(1)
                # 以下为输入时输入错误值时直接退出
            else:
                print('退出')
                time.sleep(1)
        else:
            print('退出')
            time.sleep(1)
    else:
        print('退出')
        time.sleep(1)
else:
    print('退出')
    time.sleep(1)

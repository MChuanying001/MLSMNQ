import time
import random


#开始进入Python的世界
抽卡检测 = 0
重复 = 0
while (重复 == 0):
    重复 += 1
    支付 = 0
    print('欢迎来到魔力赏模拟器')
    time.sleep(1)
    print('载入配置')
    time.sleep(1)
    print('114514')
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
    print('（数字）魔石-一发入魂')
    print('支付请按1')
    print('退出请按0')
    支付 += int(input())
    if (支付 == 1):
        许愿检测 = 0
        while (许愿检测 == 0):
            许愿 = 0
            许愿检测 += 1
            print('请设置许愿款', '如果不想许愿请按0')
            许愿 += int(input('你的许愿款'))
            if (许愿 >= 0 and 许愿 <= 10):
                小时检测 = 0
                while (小时检测 == 0):
                    小时 = 0
                    小时检测 += 1
                    小时 += int(input('请设置时间-小时'))
                    if (小时 >= 0 and 小时 <= 23):
                        分钟检测 = 0
                        while (分钟检测 == 0):
                            分钟 = 0
                            分钟检测 += 1
                            分钟 += int(input('请设置时间-分钟'))
                            if (分钟 >= 0 and 分钟 <= 59):
                                星座 = 0
                                星座检测 = 0
                                星座 += int(input('你的星座是？'))
                                if (星座 >= 1 and 星座 <= 12):
                                    抽卡检测 += 1
                                else:
                                    星座检测 = 0
                                    print('无效的选择')
                                    time.sleep(1)
                            else:
                                分钟检测 = 0
                                print('无效的选择')
                                time.sleep(1)
                    else:
                        小时检测 = 0
                        print('无效的选择')
                        time.sleep(1)
            else:
                许愿检测 = 0
                print('无效的选择')
                time.sleep(1)
    elif (支付 == 0):
        break
    else:
        重复 = 0
        print('无效的选择')
        time.sleep(1)
if (抽卡检测 == 1):
    抽奖 = 0
    支付 += random.randint(1, 10000)
    print('抽取奖品中')
    time.sleep(1)
    if (抽奖 <= 10):
        print('超神款！！！！！！')
        超神 = 0
        超神 += random.randint(1, 2)
        if (超神 == 1):
            print('奖品')
        else:
            print('奖品')
    elif (抽奖 >= 11 and 抽奖 <= 20):
        print('欧皇款！！！')
        欧皇 = 0
        欧皇 += random.randint(1, 2)
        if (欧皇 == 1):
            print('奖品')
        else:
            print('奖品')
    elif (抽奖 >= 21 and 抽奖 <= 50):
        print('隐藏款！！！')
        隐藏 = 0
        隐藏 += random.randint(1, 2)
        if (隐藏 == 1):
            print('奖品')
        else:
            print('奖品')
    else:
        print('普通款')
        普通 = 0
        普通 += random.randint(1, 2)
        if (普通 == 1):
            print('奖品')
        else:
            print('奖品')

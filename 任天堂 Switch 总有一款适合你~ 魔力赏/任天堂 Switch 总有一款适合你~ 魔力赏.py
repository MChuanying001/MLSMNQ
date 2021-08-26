import time
import random


#开始进入Python的世界
_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C = 0
_E6_8A_BD_E5_A5_96 = 0
_E8_AE_B8_E6_84_BF1 = 0
_E5_88_86_E9_92_9F = 0
_E5_B0_8F_E6_97_B6 = 0
_E8_AE_B8_E6_84_BF = 0
_E5_8F_98_E9_87_8F = 0
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
_E5_8F_98_E9_87_8F += int(input('确认支付？'))
if (_E5_8F_98_E9_87_8F == 1):
    print('请设置星座，详见“星座.txt”')
    _E8_AE_B8_E6_84_BF += int(input('你的星座？'))
    if (_E8_AE_B8_E6_84_BF <= 12 and _E8_AE_B8_E6_84_BF >= 1):
        print('请设置时间-小时')
        _E5_B0_8F_E6_97_B6 += int(input('请输入'))
        if (_E5_B0_8F_E6_97_B6 <= 23 and _E8_AE_B8_E6_84_BF >= 0):
            print('请设置时间-分钟')
            _E5_88_86_E9_92_9F += int(input('请输入'))
            if (_E5_88_86_E9_92_9F <= 59 and _E5_88_86_E9_92_9F >= 0):
                print('请设置许愿款，详见“许愿.txt”')
                _E8_AE_B8_E6_84_BF1 += int(input('请输入许愿款'))
                _E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C += _E8_AE_B8_E6_84_BF1
                if (_E8_AE_B8_E6_84_BF1 <= 12 and _E8_AE_B8_E6_84_BF1 >= 1):
                    print('执行抽奖中')
                    time.sleep(1)
                    _E6_8A_BD_E5_A5_96 += random.randint(1, 10000)
                    if (_E6_8A_BD_E5_A5_96 <= 196 and _E6_8A_BD_E5_A5_96 >= 50):
                        print('隐藏款！！！！')
                        time.sleep(1)
                        _E9_9A_90_E8_97_8F = 0
                        _E9_9A_90_E8_97_8F += random.randint(1, 3)
                        if (_E9_9A_90_E8_97_8F == 1):
                            print('奖品：超级马里奥：奥德赛')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 7):
                                print('愿望实现')
                        elif (_E9_9A_90_E8_97_8F == 2):
                            print('奖品：超级马里奥：兄弟U 豪华版')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 8):
                                print('愿望实现')
                        else:
                            print('奖品：马里奥赛车8 豪华版')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 9):
                                print('愿望实现')
                    elif (_E6_8A_BD_E5_A5_96 <= 686 and _E6_8A_BD_E5_A5_96 >= 197):
                        print('欧皇款！！')
                        time.sleep(1)
                        _E6_AC_A7_E7_9A_87 = 0
                        _E6_AC_A7_E7_9A_87 += random.randint(1, 5)
                        if (_E6_AC_A7_E7_9A_87 == 1):
                            print('奖品：Joycon左红右蓝')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 2):
                                print('愿望实现')
                        elif (_E6_AC_A7_E7_9A_87 == 2):
                            print('奖品：Joycon左紫右橙')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 5):
                                print('愿望实现')
                        elif (_E6_AC_A7_E7_9A_87 == 3):
                            print('奖品：Joycon左粉右绿')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 3):
                                print('愿望实现')
                        elif (_E6_AC_A7_E7_9A_87 == 4):
                            print('奖品：Joycon左蓝右黄')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 4):
                                print('愿望实现')
                        else:
                            print('奖品：任天堂Switch专业手柄')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 6):
                                print('愿望实现')
                    elif (_E6_8A_BD_E5_A5_96 <= 49 and _E6_8A_BD_E5_A5_96 >= 1):
                        print('超神款！！！！！！')
                        time.sleep(1)
                        print('奖品：任天堂Switch国行灰色')
                        if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 1):
                            print('愿望实现')
                    else:
                        print('普通款')
                        time.sleep(1)
                        _E6_99_AE_E9_80_9A = 0
                        _E6_99_AE_E9_80_9A += random.randint(1, 3)
                        if (_E6_99_AE_E9_80_9A == 1):
                            print('奖品：精灵球保护盒-红色')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 11):
                                print('愿望实现')
                        elif (_E6_99_AE_E9_80_9A == 2):
                            print('奖品：精灵球保护盒-黑色')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 10):
                                print('愿望实现')
                        else:
                            print('奖品：皮卡丘保护盒')
                            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == 12):
                                print('愿望实现')
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
else:
    print('退出')
    time.sleep(1)

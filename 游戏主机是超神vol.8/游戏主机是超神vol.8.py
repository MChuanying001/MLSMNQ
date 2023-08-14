import random
import time


#开始进入Python的世界
# 变量归零
_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C = 0
_E6_8A_BD_E5_A5_96 = 0
_E6_99_AE_E9_80_9A = 0
_E5_8F_98_E9_87_8F = 0
print('魔力赏模拟器')
print('载入配置')
print('游戏主机是超神vol.8')
print('请支付 15元', '支付请按1')
_E5_8F_98_E9_87_8F += int(input('确认支付？'))
if (_E5_8F_98_E9_87_8F == 1):
    # 开始设置各项数值
    print('请设置许愿款，详见“许愿.txt”')
    _E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C += int(input('请输入许愿款'))
    if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C <= 27 and _E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C >= 1):
        _E6_8A_BD_E5_A5_96 += random.randint(1, 100)
        # 抽奖中
        # 以下为中奖类型
        if (_E6_8A_BD_E5_A5_96 == 1):
            print('超神款！！！！')
            _E8_B6_85_E7_A5_9E = 0
            _E8_B6_85_E7_A5_9E += random.randint(1, 22)
            if (_E8_B6_85_E7_A5_9E == 1):
                print('奖品：PS5游戏机光驱版-国行')
            elif (_E8_B6_85_E7_A5_9E == 2):
                print('奖品：XSS游戏机-国行')
            elif (_E8_B6_85_E7_A5_9E == 3):
                print('奖品：Switch游戏机续航版-国行')
            elif (_E8_B6_85_E7_A5_9E == 4):
                print('奖品：让·巴尔手办')
            elif (_E8_B6_85_E7_A5_9E == 5):
                print('奖品：欧布圆环')
            elif (_E8_B6_85_E7_A5_9E == 6):
                print('奖品：金克丝手办')
            elif (_E8_B6_85_E7_A5_9E == 7):
                print('奖品：Alienware AW610M 无线鼠标-白色')
            elif (_E8_B6_85_E7_A5_9E == 8):
                print('奖品：象鼻子 机动战士高达UC联名 独角兽头戴式蓝牙耳机 主动降噪')
            elif (_E8_B6_85_E7_A5_9E == 9):
                print('奖品：Alienware AW610M 无线游戏鼠标-黑色')
            elif (_E8_B6_85_E7_A5_9E == 10):
                print('奖品：LIBRATONE AIR Color 小鸟真无线耳机 可升级降噪耳机-蓝色')
            elif (_E8_B6_85_E7_A5_9E == 11):
                print('奖品：LIBRATONE AIR Color 小鸟真无线耳机 可升级降噪耳机-红色')
            elif (_E8_B6_85_E7_A5_9E == 12):
                print('奖品：MEUMY CHERRY 联名款 （MX 3.0S TKL）机械键盘-茶轴')
            elif (_E8_B6_85_E7_A5_9E == 13):
                print('奖品：MEUMY CHERRY 联名款 （MX 3.0S TKL）机械键盘-红轴')
            elif (_E8_B6_85_E7_A5_9E == 14):
                print('奖品：雷蛇 毒蝰8K 有线游戏鼠标')
            elif (_E8_B6_85_E7_A5_9E == 15):
                print('奖品：BEMOE 初音未来 随心响奏 108键主题机械键盘 RGB 全键热插拔-白轴')
            elif (_E8_B6_85_E7_A5_9E == 16):
                print('奖品：BEMOE 初音未来 随心响奏 108键主题机械键盘 RGB 全键热插拔-红轴')
            elif (_E8_B6_85_E7_A5_9E == 17):
                print('奖品：BEMOE 初音未来 随心响奏 108键主题机械键盘 RGB 全键热插拔-茶轴')
            elif (_E8_B6_85_E7_A5_9E == 18):
                print('奖品：Alienware AW310H 有线头戴式游戏耳机黑色')
            elif (_E8_B6_85_E7_A5_9E == 19):
                print('奖品：FIIL CC Pro2 真无线蓝牙耳机 Hi-Res小金标')
            elif (_E8_B6_85_E7_A5_9E == 20):
                print("奖品：omamori Fate/stay night [Heaven's Feel] 机械键盘 鼠标垫套装")
            elif (_E8_B6_85_E7_A5_9E == 21):
                print('奖品：雷蛇 （Razer） 黑寡妇蜘蛛 X 竞技版背光款 有线机械游戏键盘')
            else:
                print('奖品：雷蛇 （Razer） 黑寡妇蜘蛛标准版 有线机械游戏键盘')
            if (_E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C == _E8_B6_85_E7_A5_9E):
                print('愿望实现')
        else:
            print('普通款')
            _E6_99_AE_E9_80_9A = 0
            _E6_99_AE_E9_80_9A += random.randint(1, 5)
            if (_E6_99_AE_E9_80_9A == 1):
                print('奖品：FEELALL 星空旋律 软胶挂件-茉绪款')
            elif (_E6_99_AE_E9_80_9A == 2):
                print('奖品：FEELALL 星空旋律 软胶挂件-叶月款')
            elif (_E6_99_AE_E9_80_9A == 3):
                print('奖品：FEELALL 星空旋律 软胶挂件-音理款')
            elif (_E6_99_AE_E9_80_9A == 4):
                print('奖品：FEELALL 星空旋律 软胶挂件-月咏款')
            else:
                print('奖品：FEELALL 星空旋律 软胶挂件-凪款')
            if (_E6_99_AE_E9_80_9A == _E8_AE_B8_E6_84_BF_E7_BB_93_E6_9E_9C - 22):
                print('愿望实现')
    else:
        print('退出')
        time.sleep(1)
else:
    print('退出')
    time.sleep(1)
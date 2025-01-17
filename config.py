# url = "https://www.wjx.cn/vm/QDmCDYI.aspx#"
url = "https://www.wjx.cn/vm/ex35On1.aspx"
epochs = 100
# 题项比例，确保选项数量和数组长度一致
prob = {
    1: [61, 26, 13],
    2: [17, 24, 39, 20],
    3: [5, 7, 5, 4, 43, 28, 8],
    4: [0, 0, 3, 13, 84],
    5: [5, 9, 8, 6, 73],
    6: [1, 2, 4, 16, 77],
    7: [27, 36, 15, 13, 9],
    8: [2, 2, 3, 15, 78],
    9: [5, 4, 5, 17, 69],
    10: [8, 5, 15, 9, 64],
    11: [2, 2, 8, 27, 62],
    12: [0, 1, 6, 17, 77],
    13: [25, 37, 17, 14, 8],
    14: [0, 0, 6, 17, 77],
    15: [1, 2, 30, 15, 53],
    16: [0, 0, 6, 17, 77],
    17: [1, 2, 30, 25, 42],
    18: [1, 1, 31, 34, 33],
    19: [8, 13, 16, 25, 38],
    20: [4, 4, 13, 34, 45],
    21: [41, 36, 8, 8, 7],
    22: [1, 1, 30, 20, 48],
    23: [2, 1, 19, 23, 56],
    24: [0, 0, 2, 15, 83],
    25: [1, 0, 1, 19, 79],
    26: [0, 0, 2, 20, 79],
    27: [4, 4, 13, 34, 45],
    28: [9, 8, 7, 19, 58],
    29: [4, 5, 8, 34, 49],
    30: [7, 8, 8, 36, 42],
    31: [1, 1, 30, 20, 48],
    32: [20, 25, 51, 3, 1],
    33: [46, 34, 11, 6, 3],
    34: [42, 28, 19, 6, 5],
    35: [0, 1, 2, 13, 85],
    36: [0, 0, 6, 17, 77],
    37: [1, 2, 6, 11, 80],
    38: [2, 4, 5, 21, 69],
    39: [40, 34, 15, 6, 5],
    40: [3, 4, 12, 19, 63],
    41: [1, 1, 2, 22, 73],
    42: [0, 1, 6, 19, 74],
    43: [40, 36, 10, 8, 7],
    44: [42, 33, 12, 8, 5],
    45: [4, 5, 20, 29, 43],
    46: [5, 4, 30, 24, 38],
    47: [8, 9, 29, 22, 33],
}
# 简答题题库
answerList = {
    6: ["123", "12"]
}
# IP API提取链接 https://xip.ipzan.com/ 这个每周都有几百个免费的IP代理领取
api = "https://service.ipzan.com/core-extract?num=162&no=20250116037992253442&minute=1&format=txt&protocol=1&pool=quality&mode=whitelist&secret=8n4gusib7kai1o8"
# User-Agent库
UA = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
      "Mozilla/5.0 (Linux; Android 10; SEA-AL10 Build/HUAWEISEA-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4313 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/9538 MicroMessenger/8.0.27.2220(0x28001B53) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64",
      "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/045913 Mobile Safari/537.36 V1_AND_SQ_8.8.68_2538_YYB_D A_8086800 QQ/8.8.68.7265 NetType/WIFI WebP/0.3.0 Pixel/1080 StatusBarHeight/76 SimpleUISwitch/1 QQTheme/2971 InMagicWin/0 StudyMode/0 CurrentMode/1 CurrentFontScale/1.0 GlobalDensityScale/0.9818182 AppId/537112567 Edg/98.0.4758.102",
      ]

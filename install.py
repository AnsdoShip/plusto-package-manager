import os
import json
import platform
import sys


ver = "pre-v0.0.1"
print("Plusto Install Module", ver, '已成功并正确的加载。')

def install_from_localfolder(foldername):
    print("模式: 从已解压的软件包安装")
    try:
        os.chdir(foldername)
    except FileNotFoundError:
        print("[Errno] 文件/文件夹路径不存在。")
        exit()
    print("[Status] 正在初步扫描软件包...")
    with open("info.json", "r") as f:
        datas = json.load(f)
    print("安装程序将要安装此软件包: 来自", datas["author"], "的", datas["name"])
    shinput = input("是否开始安装？[Y/n] ")
    if shinput == "y" or shinput == "Y" or not shinput:
        pass
    else:
        pass  
    print("[Status] 正在安装软件包:", datas["name"])
    print("[Status] 正在匹配当前计算机是否符合软件包要求...")
    print()
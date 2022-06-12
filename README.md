# Plusto Package Manager

这是一个方便，轻量的软件包管理器。

目前暂时支持 Windows。

# 01 如何使用？

## 01 克隆源代码
`git clone https://github.com/AnsdoShip/plusto-package-manager.git`

### 如果您没有安装 Git，您可以去安装 Git 或直接下载源代码文件。
[Plusto 源代码下载](https://github.com/AnsdoShip/plusto-package-manager/archive/refs/heads/main.zip)

[Git for Windows 仓库](https://github.com/git-for-windows/git/releases/)


当您 Clone 成功源代码后，让我们尝试配置 Plusto 并搭建 Plusto Server，具体教程如下。

## 02 配置运行环境

运行 Plusto 的必要组件是 Python 3.8 或升级版本。

[Python 官方网站](https://python.org)

随后，请安装 wget 模块。 # wget 用于下载文件

请确保您有 pip 工具来安装 wget 模块， pip 工具大部分会在安装 Python 3.x 时默认安装。

 `pip install wget`

在此命令执行完毕后，如果没有错误提示，那么准备工作则已经完成。

## 03 开启 Plusto Server

如你所见，plusto-package-manager 目录下有一个名为 server 的文件夹。

这就是 Plusto Server 的主目录。
此文件夹分为三个文件。

1. plusto-package-manager/server/：
    - install.py
    - test.txt
    - webserver.py

### install.py
此为 Plusto Install Module，用于安装软件包。

### test.txt
此为 pluconfig.py 在配置 Plusto 服务器时的测试文件。

### webserver.py
Plusto Server 使用 http(s) 协议，意味着您可以直接在此目录        (plusto-pack/server) 使用任何的网页服务器 (如 nginx)。

此文件使用 Python 3.x 自带 http.server 模块进行搭建 http 服务器，可自定义端口。

接下来，运行 webserver.py 开启 Plusto Server。

## 04 配置 Plusto 客户端。

开启完 Plusto Server 后，让我们来配置 Plusto。

运行 plusto-package-manager 目录下的 pluconfig.py

`python ./pluconfig.py`

如果没有问题，接下来应该会显示此内容

```
欢迎使用 Plusto Package Manager！
让我们先来配置一下 Plusto，然后继续使用。
>
```

如果您看到了以上内容，说明是正常的，请按下 回车键(Enter) 继续。

```
请先输入服务器地址，此是您从服务器下载软件包的关键。
如果您乱填或填错，可能导致无法下载等错误。
再此，我们整理出以下注意事项。
1. 请带上协议名。(如: https://)
2. 如有端口号请在结尾加上端口号。(如: https://example.com:8000/)
4. 如果存储在服务器的某个文件夹中，请指定文件夹 (如: https://example.com/plusto/)
>
```

按照 *要求* 填写服务器地址，然后按下 回车键(Enter) 继续。

Plusto 配置程序会自动下载并安装 Plusto Install Module。

这就是目前版本的所有内容。

后续将会完善。


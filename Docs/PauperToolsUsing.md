## 插件使用

### 目录结构

![avatar](../Imgs/dirs_3.png)

* **Docs**[文档目录]：主要用于存放文档资料
* **Donation**[捐赠目录]：主要存放捐赠者信息
* **Exe**[组件目录]：主要存放于插件相关的、必须安装的 **组件** 安装包
* **Imgs**[图片目录]：主要存放图片资料
* **Scripts**[脚本目录]：主要包含与Python相关的脚本文件。
* **Scripts/Secret**[用户脚本目录]：主要用于存放用户脚本（该目录中的*.py文件会被git忽略）
* **Scripts/Tests**[测试目录]：主要用于存放使用例子。
* **Scripts/PauperMain.py**[入口文件]：Python代码的启动入口。
* **PauperTools.apx**[Archicad 插件]：建立 **Archicad.exe** 与 **Scripts/PauperMain.py** 的连接关系。

### 入口文件

![avatar](../Imgs/main_py.png)

### 输出信息

* **文件->信息->阶段报告**

![avatar](../Imgs/pauper_output.png)

![avatar](../Imgs/pauper_output_1.png)

### 重新载入Python代码（即重新运行）

* **有的工作窗口不能点击按钮，切换一下就好了**

![avatar](../Imgs/pauper_reload.png)

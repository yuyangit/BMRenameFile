# BMRenameFile

```
在一个目录下批量修改目录和文件夹

1. 打开终端
2. cd 需要处理的目录;
3. BMRenameFile Test BM; 

```

#### 适用平台

```

	Unix/Linux
```


#### 安装

```
运行install.command 进行安装
```

#### 命令使用

```
1. 简单方式
替换当前目录下的所有文件名字

BMRenameFile 被替换的关键字 要替换的关键字;

例子:
	BMRenameFile Test BM;


2. 指定目录
替换指定目录下所有符合规则的文件

BMRenameFile 被替换的关键字 要替换的关键字 指定目录（完整路径）;

例子:
	BMRenameFile Test BM -p /Users/helios/test;


3. 处理方式

主要有以下3种处理方式：
0. 只修改文件的名字（默认）
1. 只修改目录的名字
2. 同时修改文件和目录的名字

例子:
	BMRenameFile Test BM -p /Users/helios/test -m 1;

```
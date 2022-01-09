# SDU-Dormitory-Electricity-Inquiry

## 1. 部署方式

### 1.1. Linux 服务器

#### 1.1.1. 获取源码 
* clone 这个仓库
    ```
    git clone https://github.com/Nuevo009/SDU-Dormitory-Electricity-Inquiry.git
    ```
    
    或 [直接下载 zip 包](https://github.com/Nuevo009/SDU-Dormitory-Electricity-Inquiry/archive/refs/heads/main.zip) 然后解压

#### 1.1.2. 配置

根据 [config.example.py](https://github.com/Nuevo009/SDU-Dormitory-Electricity-Inquiry/blob/main/config.example.py) 在项目根目录下编写一个 config.py

#### 1.1.3. 安装依赖 

`pip install requests` 自行解决网络问题

#### 1.1.4. 运行 

`python3 main.py`

#### 1.1.5. 设置定时 

* `crontab -e` 然后输入 `0 6 * * * python3 /path/to/your/main.py` 每天的 6 点查询一次 

* 可以根据 [corntab.guru](https://crontab.guru/) 测试

### 1.2. 云函数

~~咕咕咕~~

### 1.3. docker 

~~咕咕咕~~

## 2. 配置

~~咕咕咕~~

## 3. 抓包教程

~~咕咕咕~~

等我写完课程报告（

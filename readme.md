# 乘客调度系统

一个调度系统
给出乘客的坐标，司机的坐标和座位数等
返回乘客与司机的绑定关系

### 安装使用
- 安装redis
- git clone
- 进入目录
- pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
- python main.py

### 从redis输入
```
{
	"user_list": [{
		"id": 0,
		"coordinate": [104.05072191555561, 30.601844722095155],
		"size": 3
	},
    ...
    ...
    ],
	"driver_list": [{
		"driver_id": 0,
		"coordinate": [104.13310339290251, 30.64023468231509],
		"sites": 6
	},
    ...
    ...
    ],
	"config": {
		"far_distance": "10000",
		"type": "receive"
	}
}
```

- 从redis获取user_list,driver_list,config
- user_list: 订单id, 订单坐标, 订单人数
- driver_list: 司机id, 司机坐标, 座位数
- config: 配置
    - far_distance: 订单距离过远的距离阈值(米)
    - type: 接送模式 receive/send

### 输出
```
[
	((4, 0), 1),
    ((11, 0), 2),
    ((3, 4), 2),
    ((9, 4), 2),
    ...
    ...
]
```

- table: 订单id, 司机id, 数量   绑定表

### 日志

- 0.1 K-means 分配乘客
- 0.2 根据总路程优化
- 0.3 根据总路程和均方差优化
- 0.4 处理乘客太远的情况
- 0.5 考虑接和送乘客两种情况
- 0.6 规范化
    - 规范化
    - 完善注释
    - 封装画图函数
    - 优化处理乘客太远的算法
    - 留出调试接口
- 0.7 规范化
    - 规范化
    - 完善注释
    - 增加函数说明
    - 增加参数说明
    - 修改目录结构
    - 留出工作模式接口
- 0.8 为部署做准备
    - 增加 requirements.txt
    - 增加 show.py 展示文件
- 1.0 以redis队列与系统交换信息
- 1.1.1 修改readme文档
- 1.1.2 在readme中增加安装使用的内容
- 1.2 合并绑定表中相同的内容
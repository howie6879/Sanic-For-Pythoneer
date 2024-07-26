[![Documentation Status](https://readthedocs.org/projects/sanic-for-pythoneer/badge/?version=latest)](http://sanic-for-pythoneer.readthedocs.io/en/latest/)

## Sanic-For-Pythoneer

- 这是一份记录文档，是我日常使用`Sanic`的一些经验之谈，希望能让你在使用Sanic的过程中少走一些弯路
- 可根据需求跳跃阅读
- 在线阅读[地址](https://www.howie6879.cn/sanic_book/)

### 1.介绍

[Sanic](https://github.com/channelcat/sanic)是一个可以使用 `async/await` 语法编写项目的异步非阻塞框架，它写法类似于`Flask` ，但使用了异步特性，而且还使用 `uvloop` 作为事件循环，其底层使用的是**libuv**，从而使 `Sanic` 的速度优势更加明显

我于2017年2月份开始使用 `Sanic`，使用过程中确实遇到不少问题，如缓存、模板引入、session、认证...

但不用担心，`Sanic` 更新速度非常快，许多问题都在逐步地解决中，并且比同类别更出色更优秀，个人觉得 `Sanic` 是一个值得尝试的异步框架，不论是代码编写还是性能比较都算非常不错

本项目的结构如下：

**第一部分：技巧**

- [x] [1.初使用](./docs/part1/1.初使用.md) 			
- [x] [2.配置](./docs/part1/2.配置.md)             
- [x] [3.项目结构](./docs/part1/3.项目结构.md)
- [x] [4.展示一个页面](./docs/part1/4.展示一个页面.md)
- [x] [5.数据库使用](./docs/part1/5.数据库使用.md)
- [x] [6.常用的技巧](./docs/part1/6.常用的技巧.md)
- [x] [7.可靠的扩展](./docs/part1/7.可靠的扩展.md)
- [x] [8.测试与部署](./docs/part1/8.测试与部署.md)

**第二部分：源码及附录**

- [x] [Sanic源码阅读：基于0.1.2](./docs/part2/Sanic源码阅读：基于0.1.2.md)
- [x] [附录：关于装饰器](./docs/part2/附录：关于装饰器.md)

### 2.更新

代码的世界变幻莫测，我能做的就是尽量将本篇文档持续更新、持续修正、让其处于当前最新的状态

### 3.说明

如果您在使用中有什么不明白的问题，欢迎一起交流（扫码关注，发送：Sanic可获取本书PDF版）：

<div align=center><img src="https://cdn.jsdelivr.net/gh/howie6879/weekly/src/statics/wechat.jpeg"  width="85%" alt="img" /></div>

我也创建了一个免费的Python知识星球，欢迎大家一起交流：

<div align=center><img height="200px" src="https://raw.githubusercontent.com/howie6879/oss/master/images/我的Python世界.png" /></div>

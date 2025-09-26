# JSCXUnpacker
.jscx->.js


## usage
https://blog.steesha.cn/archives/646d5e26-6549-4498-95c0-8609c8fc69c8

## 备注
新版学习通 (1.3.8) 在asar解包的时候，需要手动排除 "node_modules\\agora-electron-sdk"
因为这是学习通新增的一个native组件包，因为编译成了本地代码，所以无法解包，会出现找不见文件的情况。
具体操作为修改lib/asar.js，如下图
<img width="772" height="492" alt="image" src="https://github.com/user-attachments/assets/9734b1aa-795c-48aa-8bd9-a0fd3746e9d2" />

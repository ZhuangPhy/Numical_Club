
'''
目标：了解基本张量的构造与计算
时间：2021-06-18
参考：https://github.com/ranshiju/TN_tutorial
目录

'''
import numpy as np

##1-阶张量：向量
vector=np.random.randn(3,) # 生成长度为3的随机向量
print(vector)  # 显示向量

#查看向量的形状
print(v.shape)

#向量与自己转置共轭向量之间的内积
prinnt(vector.dot(vector))

#生成长度为8的全零向量
v2=np.zeros(8,)
print(v2)



##2-阶张量：矩阵
matrix=np.random.randn(2,2)+1j*np.random.randn(2,2)
print(matrix)

#共轭矩阵
print(matrix.conj())

#转置共轭矩阵
print(matrix.conj().T)

#单位矩阵
print(np.eye(2))



##3-阶张量：张量
tens=np.random.randn(2,3,4)# 随机生成一个2*3*4的三阶张量
print(tens)#显示出来的时候，2个矩阵，每个是3*4大小
print(tens.ndim)
print(tens.shape)

#一次性打印太多东西的时候，用分割线。句法意思是打印30次符号 -
print('-' * 30)
v = np.arange(6)
print(v)
print('=' * 30)
print(v[:3])#前面三个元素
print(v[2:])# 第二位后面的元素
print(v[1:3])#第二位到第三位之间的元素



# 切片操作
print('=' * 30)
m = np.random.randn(4, 4)
print(m)
print('-' * 30)
print(m[1:3, :2])#后面的:2是指1到2列 #1:3是第二行到第3行
print('-' * 30)
print(m[1:3, :1])
print('-' * 30)
print(m[1:4, :2])





















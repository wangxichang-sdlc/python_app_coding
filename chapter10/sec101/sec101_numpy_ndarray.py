# coding: utf8

"""
使用array方法创建多维数组示

>>> import numpy as np

# 定义一个类型为复数的一维数组
>>> np.array((1,2,3), dtype=complex)
array([1.+0.j, 2.+0.j, 3.+0.j])

# 使用模块方法array创建多维数组
# 源数据为嵌套列表，为二维数据结果，生成二维数组
# 设置dtype=np.int16，使数组的每个元素类型为2字节有符号整数
# 如果不设置dtype，array根据来源数据进行推断， 此处一般为np.int32
>>> np.array([[1, 2],[2, 3],[3, 4]], dtype=np.int16)
array([[1, 2],
       [2, 3],
       [3, 4]], dtype=int16)

# 从序列生成一维数组，使用reshape可以改变数组形状
>>> a = np.array(range(12), dtype=np.uint8)
>>> a.reshape(3, 2, 2)     # doctest: +NORMALIZE_WHITESPACE
array([[[ 0,  1],
        [ 2,  3]],
<BLANKLINE>
       [[ 4,  5],
        [ 6,  7]],
<BLANKLINE>
       [[ 8,  9],
        [10, 11]]], dtype=uint8)

# 通过arange创建数组
# 步长可以设定为浮点数
>>> a = np.arange(0, 5, 0.5)
>>> a
array([0. , 0.5, 1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])

使用zeros生产初始值为0的多维数组示例：
# 生成一个3x3二维数组，元素都是0，缺省类型float
>>> np.zeros((3,3))
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])

# 设置dtype=np.float16，使用单精度浮点数类型
# 与标量值np.sqrt(2)相加，结果为数组的每个元素加上该值
>>> np.zeros((3, 3), dtype=np.float16) + np.sqrt(2)
array([[1.414, 1.414, 1.414],
       [1.414, 1.414, 1.414],
       [1.414, 1.414, 1.414]], dtype=float16)

使用ones生成初始值为1多维数组示例：
# 生成一个3x3二维数组，元素都是1，缺省类型float
>>> np.ones((3,3))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])

使用empty生成不确定初始值（可能为任意值）的多维数组示例：
# 生成一个3x3二维数组，元素类型为np.int8，值未定. 很可能取前面刚刚回收的空间：）
>>> np.empty((3,3), dtype=np.int8)
array([[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]], dtype=int8)

使用np.eye生成特定（初始值对角线元素为1，其余为0）的多维数组示例：
# 定义对角线元素等于1的方阵
>>> np.eye(3, dtype=float)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])

# 在向上偏移2的对角线上，将元素置为1
>>> np.eye(3, 5, 2)
array([[0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
"""
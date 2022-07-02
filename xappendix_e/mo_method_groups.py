# coding: utf8

"""
groups(default=None)
返回包含所有分组的匹配内容的元组，从1组到最高组。参数default用于指定没有参与匹配的分组的返回结果值，默认为None。

>>> import re

【示例】
两个分组都参与匹配
>>> mo11 = re.match(r"(\d+)\.(\d+)", "24.1632")
>>> mo11.groups()
('24', '1632')

在返回结果中，没有参与匹配的分组为None。而给出缺省参数时，则分组的结果会替换为缺省参数值。
>>> mo12 = re.match(r"(\d+)\.?(\d+)?", "24")
>>> mo12.groups()	#第二个分组未参与匹配，使用默认值None作为返回结果.
('24', None)
>>> mo12.groups('0')	#给出一个default参数值,则未匹配的分组结果替换未缺省值'0'.
('24', '0')
"""
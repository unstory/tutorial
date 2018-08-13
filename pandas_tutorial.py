
# coding: utf-8

# ###  quick start for pandas

# #### 1. preview

# 1. python基础语法
# 2. 面向对象思想

# #### 2. pandas数据结构

# #### 2.1 Series

# Series(序列)与list相似，功能更加强大。series是学习dataframe的基础，一个dataframe是由多个series构成的数据结构。

# ##### series的常用属性

# In[9]:


import pandas as pd
# 构建一个series
s = pd.Series([1,2,"c",5,1],index=range(1,6))  # series在不指定index参数的时候会自动创建索引
print(s)            # 打印series
print(s.index)      # 打印series的索引
print(s.values)     # 打印series的值
print(s.dtype)      # object，series的值是object类型(即python的str类型),类比数据库的varchar或者text类型
# index,values,dtype都是索引的属性


# In[5]:


# python的字典的key唯一，使用dict创建series时，默认会把key值作为series的index
d = {"a":1, "b":3, "c":5, "d":7}
s1 = pd.Series(d)
print(s1)      # 从打印的结果可以看出s1的索引就是字典的key值


# ##### series的常用方法

# <b>str子类方法</b>

# In[19]:


# str是python的基本数据类型，str类型的变量(实例)都有一系列的方法，比如：
# 从面向对象的角度来看，s是str类的一个实例
s = "AaBbCc"
print(s.endswith("c"))    # True, 字符串以c结尾
print(s.upper())        # AABBCC,将小写字母变成大写字母
print(s.startswith("A"))      # True，以A开头


# In[20]:


# 对于Series来说，str是series里面的一个子类
ser = pd.Series(["aaa", "bb", "Cc", "DD", "eafV", "1", 1])
print(ser.str.endswith("a"))
print(ser.str.upper())
print(ser.str.startswith("a"))


# <b>常用方法</b>

# In[34]:


ser1 = pd.Series([54,32,56,23,7,1, 1])
# 升序排序
print(ser1.sort_values(ascending=True))
# 计算均值，标准差最大值，最小值，中位数, pd.min(),pd.std(), pd.median()...
# 去重
print(pd.unique(ser1))
# 更多函数参考：http://pandas.pydata.org/pandas-docs/stable/api.html


# <b>自定义函数</b>

# In[29]:


ser2 = pd.Series([34,234,4,23,1])
ser3 = ser2.apply(lambda x: x+10000)  # lambda匿名函数，x代表ser2中的每一个值，这里将ser2的每一个元素都加上10000
print("ser3:", ser3)
def test(x):
    if x > 5:
        return True
    return False
ser4 = ser2.apply(test)    # apply：应用，即将ser2中的每一个元素都应用到test函数
print(ser4)


# #### 2.2 DataFrame

# dataFrame是类似excel表格的一种数据结构，可以说用pandas包就一定会用dataframe

# <b>创建DataFrame</b>

# In[5]:


import pandas as pd
# 创建一个dataframe，更常见的作法是通过读csv或者excel文件，读进python的数据就是一个dataframe
df = pd.DataFrame({"a":[1,3,5,7,9], "b":[2,4,6,8,10], "c":["a", "b", "c", "d", "e"]},columns=["a", "b", "c"])  # columns参数指定列的顺序(因为字典的key是无序的)
print("df:\n", df)


# <b>DataFrame常用属性</b>

# In[8]:


print(df.index)   # df的索引
print(df.values)  # 二维列表
print(df.dtypes)  # 每一列的数据类型，a列是int64（64位的整数），b列是int64，c列是object类型(类似数据库的varchar或者text)
print(df.shape)  # (5, 3),即df是一个5行3列的二维表
print(df.columns)  # df的列名


# <b>索引、选择</b>

# In[39]:


import numpy as np
# 取a列
df = pd.DataFrame({"a":[1,2,3,4,5], "b":[2,4,6,8,10], "c":["a", "b", "c", "d", "e"]}, index=range(0, 5))
print("取a列:df['a']\n", df["a"])  # df["a"]是Series
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("取前3行：df[0:3]\n", df[0:3])   
print("-------------"*5 + "****" + "------------"*5)# 分割线
print('取索引为1、2，  a,b列：df.loc[1:2, ["a", "b"]]\n', df.loc[1:2, ["a", "b"]])
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("取a列大于3的值：df[df.a>3]\n", df[df.a>3])
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("取行索引为1， 列索引为1(第二列)的值：df.iloc[1, 1]\n", df.iloc[1, 1])   # 或者：  df.iat[1, 1]
print("-------------"*5 + "****" + "------------"*5)# 分割线
df.iat[1,1] = 111
print("将行索引为1， 列索引为1(第二列)的值设置为111：df.iat[1,1] = 111\n", df)   # 
print("-------------"*5 + "****" + "------------"*5)# 分割线
df.loc[:,"d"] = ["one", "two", "three", "four", "one"]
print('添加d列：df.loc[:,"d"] = ["one", "two", "three", "four", "one"]\n',df)
print("-------------"*5 + "****" + "------------"*5)# 分割线
# isin,isna,fillna
print('取出d列的值为one,two的值:df[df.d.isin(["one", "two"])]\n', df[df.d.isin(["one", "two"])])
print("-------------"*5 + "****" + "------------"*5)# 分割线
df.iat[1, 2] = np.nan     # 将索引为1，c列的值设置为nan
print("取出c列为nan的那一行:df[df.c.isna()]\n", df[df.c.isna()])    # 取出c列为nan的那一行
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("将nan设置为test: df.fillna('test')\n", df.fillna("test"))
# 更多方法参考：http://pandas.pydata.org/pandas-docs/stable/indexing.html， http://pandas.pydata.org/pandas-docs/stable/10min.html
print("-------------"*5 + "****" + "------------"*5)# 分割线


# ##### DataFrame常用方法、函数

# In[7]:


import pandas as pd
# 读excel文件
df1 = pd.read_excel("data/test1.xlsx", encoding="gbk", sheet_name="Sheet1")
df2 = pd.read_excel("data/test1.xlsx", encoding="gbk", sheet_name="Sheet2")
df3 = pd.read_excel("data/test2.xlsx", encoding="gbk", sheet_name="Sheet1")
print("df1: ", df1)
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("df2: ", df2)
print("-------------"*5 + "****" + "------------"*5)# 分割线
print("df3: ", df3)
print("-------------"*5 + "****" + "------------"*5)# 分割线


# In[9]:


# 合并文件
df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)  # 忽略索引
print("df: ", df)


# In[11]:


# 按照age升序排序
df.sort_values(by="age", ascending=True, inplace=True)  # inplace参数为True，即将原来的df替换(inplace)成排序后的df
print("after sort: \n", df)


# In[27]:


### groupby 聚合函数 (重点)
# groupby的思想： split（按组split） -- > apply(将每一组都apply到函数上)-- >combine(将每一组的结果combine）

age_mean_df = df.groupby(by=["sex"])["age"].mean()  # 按性别分组计算年龄的平均值
print("age_mean_df: \n", age_mean_df)
print("-------------"*5 + "****" + "------------"*5)# 分割线
# apply函数
# 将分组后的结果都应用到sum函数
sum_df = df.groupby(by=["sex"])["age"].apply(lambda x: sum(x))
print("first sum: \n", sum_df)
print("-------------"*5 + "****" + "------------"*5)# 分割线
# 等价于
sum_df = df.groupby(by=["sex"])["age"].sum()
print("second sum:\n", sum_df)
print("-------------"*5 + "****" + "------------"*5)# 分割线


# 应用apply函数
def get_grade(x):
    return "children" if x <= 14 else "young"  # 大于14岁返回young，小于等于14岁返回children

df["grade"] = df["age"].apply(get_grade)
print(df)

# 参考：http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html


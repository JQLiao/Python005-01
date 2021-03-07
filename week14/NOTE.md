Series数据结构
- 基本属性：index 和 value
```
# 从列表创建Series
pd.Series(['a', 'b', 'c'])
# 通过字典创建带索引的Series
s1 = pd.Series({'a':11, 'b':22, 'c':33})
# 通过关键字创建带索引的Series
s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])
# 获取全部索引
s1.index
# 获取全部值
s1.value
# 转换为列表
s1.values.tolist()
```

DataFrame
- execl多行多列
```
# 列表创建dataframe
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# 嵌套列表创建dataframe
df2 = pd.DataFrame([
                     ['a', 'b'], 
                     ['c', 'd']
                    ])
# 自定义列索引
df2.columns= ['one', 'two']
# 自定义行索引
df2.index = ['first', 'second']

df2
# 可以在创建时直接指定 DataFrame([...] , columns='...', index='...' )
# 查看索引
df2.columns, df2.index

```

数据库
```
import pymysql
sql  =  'SELECT *  FROM mytable'
conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
df = pd.read_sql(sql,conn)


# 熟悉数据
# 显示前几行
excel1.head(3)

# 行列数量
excel1.shape

# 详细信息
excel1.info()
excel1.describe()
```
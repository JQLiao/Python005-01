作业要求：请将以下的 SQL 语句翻译成 pandas 语句：

```
import pymysql
import pandas as pd
import numpy as np
sql  =  'SELECT * FROM data'
conn = pymysql.connect(host='localhost', database='dbname',user='root',passwd='passwd',port=3306,charset='utf8')
df = pd.read_sql(sql,conn)
```

1. SELECT * FROM data;
```
df
```

2. SELECT * FROM data LIMIT 10;
```
df.head(10)
```

3. SELECT id FROM data;  //id 是 data 表的特定一列
```
df['id']
```

4. SELECT COUNT(id) FROM data;
```
df['id'].count()
```

5. SELECT * FROM data WHERE id<1000 AND age>30;
```
df[ (df['id'] < 1000) & (df['age'] > 30) ]
```

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
```
df[['id', 'order_id']].drop_duplicates(subset='order_id').groupby('id').count()
```

7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
```
pd.merge(table1, table2, on='id', how='inner')
```

8. SELECT * FROM table1 UNION SELECT * FROM table2;
``` 
pd.concat([table1, table2])
```

9. DELETE FROM table1 WHERE id=10;
```
table1[table1['id'] != 10]
```

10. ALTER TABLE table1 DROP COLUMN column_name;
```
table1.drop(columns='column_name')
```


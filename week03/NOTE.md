#### 本周作业
1. 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用

    ```
    #字符集配置项  my.cnf
    [client]
    default_character_set = utf8mb4
    [mysql]
    default_character_set = utf8mb4
    [mysql]
    character_set_server = utf8mb4
    init_connect = 'SET NAMES utf8mb4'

    #验证字符集
    show variables like '%character%';

    #新增远程用户授予权限
    CREATE USER 'testuser'@'%' IDENTIFIED BY 'testpwd';
    GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpwd';  
    ```

2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交

    ```
    答案见 num02.py
    ```

3. 为以下 sql 语句标注执行顺序
    ```
    5 SELECT DISTINCT player_id, player_name, count(*) as num 
    1 FROM player JOIN team ON player.team_id = team.team_id 
    2 WHERE height > 1.80 
    3 GROUP BY player.team_id 
    4 HAVING num > 2 
    6 ORDER BY num DESC 
    7 LIMIT 2
    ```

4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

    Table1
    id name
    1 table1_table2
    2 table1

    Table2
    id name
    1 table1_table2
    3 table2

    ```
    INNER JOIN  结果： table1_table2
    LEFT JOIN   结果： table1 ，table1_table2
    RIGHT JOIN  结果： table2 ，table1_table2
    ```

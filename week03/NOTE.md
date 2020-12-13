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
    LEFT  JOIN  结果： table1 ，table1_table2
    RIGHT JOIN  结果： table2 ，table1_table2
    ```

5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效
    ```
    数据量小的时候增加索引，执行时间并无区别。只有数据量大的时候，才能看到明显提升。

    mysql> select count(*) from table1;
    +----------+
    | count(*) |
    +----------+
    |    99999 |
    +----------+
    1 row in set (0.04 sec)


    mysql> select * from table1 where name='9999name';
    +------+----------+
    | id   | name     |
    +------+----------+
    | 9999 | 9999name |
    +------+----------+
    1 row in set (0.07 sec)

    mysql> select * from table1 where name='99999name';
    +-------+-----------+
    | id    | name      |
    +-------+-----------+
    | 99999 | 99999name |
    +-------+-----------+
    1 row in set (0.07 sec)

    mysql> ALTER TABLE `table1` ADD INDEX name( `name` );
    Query OK, 0 rows affected (0.35 sec)
    Records: 0  Duplicates: 0  Warnings: 0

    mysql> select * from table1 where name='99998name'; 
    +-------+-----------+
    | id    | name      |
    +-------+-----------+
    | 99998 | 99998name |
    +-------+-----------+
    1 row in set (0.00 sec)

    ```

6.  张三给李四通过网银转账 100 极客币，现有数据库中三张表：
一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

    ```
    答案见 num06.py
    ```
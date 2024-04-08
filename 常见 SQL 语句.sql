```
创建表
```
CREATE TABLE 
(
    
)

    
```
创建存储过程
```

CREATE PROC proc 
@a int, @b char(8), @c char(50) 
AS
INSERT INTO author
(author_id, author_name, address)
VALUES(@a, @b, @c)
GO
       

```
创建分区函数
LEFT 表示等号在右侧
```
       
CREATE PARTITION FUNCTION PF1(INT)
AS RANGE LEFT FOR VALUES(1,100,200)

       
```
授权语句
``` 
  
WITH GRANT OPTION 表示可以转授权限
GRANT SELECT(C1,C2) ON T1 TO U1
WITH GRANT OPTION

    
```
备份文件组
```
    
BACKUP DATABASE Sales
FILEGROUP='SalesGroup1',
FILEGROUP='SalesGroup2'
TO DISK='D:\Backup\Sales.bck'
WITH DIFFERENTIAL


```
创建表值函数
```
      
CREATE FUNCTION GOODS_PROFIT(@year int)
RETURNS @f- table(
商品号 varchar(50),
销售总额 int)
AS
BEGIN
INSERT INTO @f
SELECT 商品名， SUM(商品表.单价 * 销售表.销售数量)
FROM 商品表 JOIN 销售表 ON 商品表.商品号 = 销售表.商品号
WHERE year(销售表.销售时间) = @year
GROUP BY 商品号
RETURN
END

CREATE FUNCTION TABLE(@year int)
RETURNS TABLE t
(
Name varchar(50),
Score int
)
AS 
BEGIN
INSERT INTO t
SELECT a.商品名, SUM(商品表)
RETURN
END

```
创建分区方案
```

CREATE PARTITION SCHEME myPS1
AS PARTITION myPF1 TO (fg1,fg2)

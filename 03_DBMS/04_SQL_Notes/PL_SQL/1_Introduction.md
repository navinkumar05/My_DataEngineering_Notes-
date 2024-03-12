# introduction

- PLSQL is a procedural Language of SQL it is designed for write a programming language.

- Multiple SQL statements we can put together one single PLSQL block and send this block to the server.

- It is used to improve the performance of an application by reducing the **network traffic**.

in this course - I will use Postgres database for demonstration.

## Block
Block contains multiple SQL statements

reference:
https://www.guru99.com/blocks-pl-sql.html
https://www.geeksforgeeks.org/blocks-in-pl-sql/

In PL/SQL, the code is not executed in single line format, but it is always executed by grouping the code into a single element called Blocks

![[110215_0632_BlocksinPLS1.webp]]

```sql
-- how to declare a block
DO $$
BEGIN
INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12 Pro Max', 1300);
INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12 Pro', 1100);
INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12', 1000);
END $$;
```

perform insert value

```sql
/*
perform insert value
1. INSERT INTO testdb.public.product VALUES('Phone', 'realme', 'realme x2 pro', 300);
2. update the price for iPhone 12 Pro - 1100 into 1000
3. delete the record iPhone 12
*/

DO $$ 
BEGIN
   INSERT INTO testdb.public.product VALUES('Phone', 'realme', 'realme x2 pro', 300);
  
   UPDATE public.product SET price=1000 WHERE product_name='iPhone 12 Pro' AND price=1100;

   DELETE FROM public.product WHERE product_category='Phone' AND brand='Apple' AND product_name='iPhone 12' AND price=1000;
END $$;
```

Result:
![[Pasted image 20240307183854.png]]

![[Pasted image 20240307183547.png]]

## printing statement

Display String
```sql
DO $$
BEGIN
RAISE NOTICE 'hello world';
END $$;
```

Display Integer
```sql
DO $$ 
DECLARE
    my_integer INTEGER := 42;
BEGIN
    RAISE NOTICE 'The value of the integer is: %', my_integer;
END $$;
```

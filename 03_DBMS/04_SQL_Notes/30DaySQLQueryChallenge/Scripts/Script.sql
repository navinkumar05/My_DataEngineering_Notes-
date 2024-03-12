DO $$ 
BEGIN
   INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12 Pro Max', 1300);
   INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12 Pro', 1100);
   INSERT INTO testdb.public.product VALUES('Phone', 'Apple', 'iPhone 12', 1000);
END $$;

select * from product p ;

SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'product';

SELECT table_schema
FROM information_schema.tables
WHERE table_name = 'product';

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


DO $$ 
BEGIN
    RAISE NOTICE 100;
END $$;

 

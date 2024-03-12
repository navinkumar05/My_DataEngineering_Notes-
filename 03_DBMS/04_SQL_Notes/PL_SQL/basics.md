
how to get the schema for specific table in Postgres?
```sql
SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'product';
```
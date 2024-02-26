# Steps to Run
create .env file with below content.

```
AIRFLOW_UID=50000
```

next run airflow-init

```
docker compose up airflow-init
```

then run below cmd

```
docker compose up
```


## SQL

Function
 ```
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
 RETURNS TRIGGER AS $$
 BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
 END;
 $$ LANGUAGE plpgsql;
```
Trigger
 ```
 CREATE TRIGGER set_timestamp
 BEFORE UPDATE ON priorities
 FOR EACH ROW
 EXECUTE PROCEDURE trigger_set_timestamp();
```
insert query
```
 INSERT INTO priorities (priority, is_active) 
 VALUES ('p2', True) RETURNING *;
```
## Reference
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

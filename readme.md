# Steps to Run Airflow instance
- create .env file with below content.

```
AIRFLOW_UID=50000
```

- next run airflow-init

```
docker compose up airflow-init
```

- then run below cmd

```
docker compose up
```

- Once you complete the above steps, Airflow instance will be up. 

you can access the Airflow  `http://localhost:8080/ ` <br/>
use username and password `airflow`

## Configure Postgres connection in Airflow UI
add the Postgres Database configure in Airflow connection, to use it in our dag for connection.
here our connection name is `postgres_local`, 
![image](https://github.com/Alayappan/AirflowCronAPI/assets/38777845/785979e6-02fa-4f26-bc58-4426ffb2dcb4)
and configure the connection params
![image](https://github.com/Alayappan/AirflowCronAPI/assets/38777845/c0ed976b-dac5-4b37-89a4-5a9c35eee8e4)


## SQL

- connect to Postgres DB we added in Airflow connection via any client and run the below SQL in sequence.  
- create table priorities
  ```
  CREATE TABLE priorities
  (
      id serial PRIMARY KEY,
      priority character varying ,
      is_active boolean,
      created_at timestamp with time zone NOT NULL DEFAULT now(),
      updated_at timestamp with time zone NOT NULL DEFAULT now()
  )
  ```
- Function
 ```
 CREATE OR REPLACE FUNCTION trigger_set_timestamp()
  RETURNS TRIGGER AS $$
  BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
  END;
  $$ LANGUAGE plpgsql;
```
- Trigger
 ```
 CREATE TRIGGER set_timestamp
 BEFORE UPDATE ON priorities
 FOR EACH ROW
 EXECUTE PROCEDURE trigger_set_timestamp();
```
- insert query for inserting  record into our table priorities, run it few times to insert couple of records.
```
 INSERT INTO priorities (priority, is_active) 
 VALUES ('p1', True) RETURNING *;
```
## create a simple API receives a payload and post it back.
## configure the URL in Airflow variable
![image](https://github.com/Alayappan/AirflowCronAPI/assets/38777845/c7207c0e-9ab5-4068-911f-76286d0e33eb)

## run the DAG

## Reference
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

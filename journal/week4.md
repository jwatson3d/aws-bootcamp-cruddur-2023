# Week 4 — Postgres and RDS

## Create PostgreSQL RDS Instance

```shell
aws rds create-db-instance \ 
  --db-instance-identifier cruddur-db-instance \ 
  --db-instance-class db.t3.micro \ 
  --engine postgres \ 
  --engine-version  14.6 \ 
  --master-username root \ 
  --master-user-password **************** \ 
  --allocated-storage 20 \ 
  --availability-zone us-east-2a \ 
  --backup-retention-period 0 \ 
  --port 5432 \ 
  --no-multi-az \ 
  --db-name cruddur \ 
  --storage-type gp2 \ 
  --publicly-accessible \ 
  --storage-encrypted \ 
  --enable-performance-insights \ 
  --performance-insights-retention-period 7 \ 
  --no-deletion-protection
```

![db-instance](assets/cruddur-wk4-db-instance.png)

## Initialize Cruddur db in local container

### db/schema.sql

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text,
  handle text,
  cognito_user_id text,
  created_at TIMESTAMP default current_timestamp NOT NULL
);

CREATE TABLE public.activities (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  message text NOT NULL,
  replies_count integer DEFAULT 0,
  reposts_count integer DEFAULT 0,
  likes_count integer DEFAULT 0,
  reply_to_activity_uuid integer,
  expires_at TIMESTAMP,
  created_at TIMESTAMP default current_timestamp NOT NULL
);

DROP FUNCTION IF EXISTS func_updated_at();
CREATE FUNCTION func_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER trig_users_updated_at 
BEFORE UPDATE ON users 
FOR EACH ROW EXECUTE PROCEDURE func_updated_at();
CREATE TRIGGER trig_activities_updated_at 
BEFORE UPDATE ON activities 
FOR EACH ROW EXECUTE PROCEDURE func_updated_at();
```

### bin/db-connect.sh

```shell
export CONNECTION_URL="postgresql://postgres:password@127.0.0.1:5433/cruddur"
env | grep CONNECTION_URL
```

## Seed database

### db/seed.sql

```sql
-- this file was manually created
INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Sherlock Holmes', 'sherlock' ,'MOCK'),
  ('John Watson', 'watson' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'sherlock' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
```

### users

![db-users](assets/cruddur-wk4-db-users.png)

### activities

![db-activities](assets/cruddur-wk4-db-activities.png)

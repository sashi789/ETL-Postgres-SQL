# ETL Pipeline Project

This project is an end-to-end ETL (Extract, Transform, Load) pipeline that fetches user and post data from a public API, stages the raw data in PostgreSQL, transforms it using pandas, and loads the final fact table into Microsoft SQL Server. The entire pipeline is containerized using Docker and orchestrated with Docker Compose.

## Features
- **Extract:** Fetches users and posts from the JSONPlaceholder API.
- **Stage:** Loads raw data into PostgreSQL staging tables.
- **Transform:** Joins and cleans data using pandas.
- **Load:** Loads the transformed data into a SQL Server fact table.
- **Containerized:** Runs all components in Docker containers for easy setup and reproducibility.

## Project Structure
```
assessment/
  app/
    config.py
    extract.py
    load.py
    main.py
    sql/
      create_fact_user_posts.sql
      create_staging_posts.sql
      create_staging_users.sql
    transform.py
  docker-compose.yml
  Dockerfile
  requirements.txt
  tests/
    test_transform.py
```

## Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## Environment Variables (.env file)
Create a `.env` file in the project root with the following content (example values shown):

```
# PostgreSQL Configuration
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=staging_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# SQL Server Configuration
MSSQL_USER=sa
MSSQL_PASSWORD=MssqlP@ssword1
MSSQL_DB=master
MSSQL_HOST=mssql
MSSQL_PORT=1433

# API Configuration
API_USERS_URL=https://jsonplaceholder.typicode.com/users
API_POSTS_URL=https://jsonplaceholder.typicode.com/posts
```

**Note:** The `.env` file is included in `.gitignore` and should NOT be committed to version control.

## Setup & Usage

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd assessment
   ```

2. **Build and start all services:**
   ```bash
   docker-compose up --build
   ```
   This will start PostgreSQL, SQL Server, and run the ETL pipeline.

3. **Re-run the ETL pipeline:**
   If you want to re-run the ETL process without restarting the databases:
   ```bash
   docker-compose up etl-app
   ```

4. **Reset the database (optional):**
   To start with a clean database:
   ```bash
   docker-compose down
   docker volume rm assessment_pg_data
   docker-compose up --build
   ```

## Database Access

### PostgreSQL (Staging)
- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `staging_db`
- **Username:** `postgres`
- **Password:** `postgres`

### SQL Server (Fact Table)
- **Host:** `localhost`
- **Port:** `1433`
- **Database:** `master`
- **Username:** `sa`
- **Password:** `MssqlP@ssword1`

You can use tools like DBeaver, Azure Data Studio, or psql/sqlcmd to connect and inspect the data. I've used DBeaver.

## Code Overview

- **app/config.py:** Loads environment variables for DB/API config.
- **app/extract.py:** Fetches users and posts from the API.
- **app/transform.py:** Joins and cleans data using pandas.
- **app/load.py:** Handles loading data into PostgreSQL and SQL Server.
- **app/main.py:** Orchestrates the ETL pipeline.
- **app/sql/:** SQL scripts for creating tables.
- **Dockerfile:** Builds the ETL app image.
- **docker-compose.yml:** Orchestrates all services.

## Customization
- To change the API endpoints or database credentials, edit the environment variables in `docker-compose.yml` or your `.env` file.
- To modify the transformation logic, edit `app/transform.py`.

## Testing
- Unit tests for transformation logic can be added to `tests/test_transform.py`.

## Troubleshooting
- If you see connection errors, ensure the database containers are running and healthy.
- If you change Python code, always rebuild the image:
  ```bash
  docker-compose build etl-app
  ```
- For schema changes, reset the database volume as shown above.

## License
MIT 

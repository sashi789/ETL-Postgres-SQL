import logging
from extract import fetch_users, fetch_posts
from load import connect_pg, connect_mssql, load_to_pg, load_to_mssql
from transform import join_users_posts

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting ETL pipeline")

    users = fetch_users()
    posts = fetch_posts()

    pg_conn = connect_pg()
    pg_cur = pg_conn.cursor()

    pg_cur.execute("DROP TABLE IF EXISTS staging_users CASCADE;")
    pg_cur.execute("DROP TABLE IF EXISTS staging_posts CASCADE;")
    
    with open("app/sql/create_staging_users.sql", "r") as f:
        pg_cur.execute(f.read())
    with open("app/sql/create_staging_posts.sql", "r") as f:
        pg_cur.execute(f.read())
    pg_conn.commit()

    load_to_pg("staging_users", users, pg_cur)
    load_to_pg("staging_posts", posts, pg_cur)

    pg_conn.commit()

    transformed_df = join_users_posts(users, posts)
    records = transformed_df.to_dict(orient="records")

    mssql_conn = connect_mssql()
    mssql_cur = mssql_conn.cursor()

    mssql_cur.execute("DROP TABLE IF EXISTS FactUserPosts;")
    with open("app/sql/create_fact_user_posts.sql", "r") as f:
        mssql_cur.execute(f.read())
    mssql_conn.commit()

    load_to_mssql("FactUserPosts", records, mssql_cur)
    mssql_conn.commit()

    pg_cur.close()
    pg_conn.close()
    mssql_cur.close()
    mssql_conn.close()

    logging.info("ETL pipeline completed successfully.")

if __name__ == "__main__":
    main()

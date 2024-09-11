import os
import sys
import psycopg2


if __name__ == "__main__":
    print("Example")
    try:
        conn = psycopg2.connect(
            **{
                "dbname": os.getenv("POSTGRES_DB"),
                "user": os.getenv("POSTGRES_USER"),
                "password": os.getenv("POSTGRES_PASSWORD"),
                "host": os.getenv("POSTGRES_HOST"),
                "port": os.getenv("POSTGRES_PORT"),
                "connect_timeout": 1,
            }
        )
        conn.close()
        print("OK")
    except psycopg2.OperationalError as ex:
        print("Error", ex)
        sys.exit(-1)
    sys.exit(0)

import os
from dotenv import load_dotenv
import psycopg2


def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Breast_Cancer_Data (  
        id SERIAL PRIMARY KEY,  
        timestamp timestamp,
        Feature_A float8,
        Feature_B float8,
        Feature_C float8,
        Feature_D float8,
        Feature_E float8,
        Feature_F float8,
        Feature_G float8,
        Feature_H float8,
        Feature_I float8,
        Feature_J float8,
        Feature_K float8,
        Feature_L float8,
        Feature_M float8,
        Feature_N float8,
        Feature_O float8,
        Feature_P float8,
        Feature_Q float8,
        Feature_R float8,
        Feature_S float8,
        Feature_T float8,
        Feature_U float8,
        Feature_V float8,
        Feature_W float8,
        Feature_X float8,
        Feature_Y float8,
        Feature_Z float8,
        Feature_AA float8,
        Feature_BB float8,
        Feature_CC float8,
        Feature_DD float8,  
        target int  
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


if __name__ == "__main__":
    load_dotenv()
    db_connect = psycopg2.connect(
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        host=os.environ.get("POSTGRES_HOST"),
        port=5432,
        database=os.environ.get("POSTGRES_DB"),
    )
    create_table(db_connect)
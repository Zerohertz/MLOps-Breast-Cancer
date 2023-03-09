import time
from argparse import ArgumentParser

import pandas as pd
import psycopg2
from sklearn.datasets import load_breast_cancer


def get_data():
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        'mean radius': 'Feature_A', 'mean texture': 'Feature_B', 'mean perimeter': 'Feature_C', 'mean area': 'Feature_D', 'mean smoothness': 'Feature_E', 'mean compactness': 'Feature_F', 'mean concavity': 'Feature_G', 'mean concave points': 'Feature_H', 'mean symmetry': 'Feature_I', 'mean fractal dimension': 'Feature_J', 'radius error': 'Feature_K', 'texture error': 'Feature_L', 'perimeter error': 'Feature_M', 'area error': 'Feature_N', 'smoothness error': 'Feature_O', 'compactness error': 'Feature_P', 'concavity error': 'Feature_Q', 'concave points error': 'Feature_R', 'symmetry error': 'Feature_S', 'fractal dimension error': 'Feature_T', 'worst radius': 'Feature_U', 'worst texture': 'Feature_V', 'worst perimeter': 'Feature_W', 'worst area': 'Feature_X', 'worst smoothness': 'Feature_Y', 'worst compactness': 'Feature_Z', 'worst concavity': 'Feature_AA', 'worst concave points': 'Feature_BB', 'worst symmetry': 'Feature_CC', 'worst fractal dimension': 'Feature_DD'
    }
    df = df.rename(columns=rename_rule)
    return df


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


def insert_data(db_connect, data):
    insert_row_query = f"""
    INSERT INTO Breast_Cancer_Data
        (timestamp, Feature_A, Feature_B, Feature_C, Feature_D, Feature_E, Feature_F, Feature_G, Feature_H, Feature_I, Feature_J, Feature_K, Feature_L, Feature_M, Feature_N, Feature_O, Feature_P, Feature_Q, Feature_R, Feature_S, Feature_T, Feature_U, Feature_V, Feature_W, Feature_X, Feature_Y, Feature_Z, Feature_AA, Feature_BB, Feature_CC, Feature_DD, target)
        VALUES (
            NOW(),
            {data.Feature_A},
            {data.Feature_B},
            {data.Feature_C},
            {data.Feature_D},
            {data.Feature_E},
            {data.Feature_F},
            {data.Feature_G},
            {data.Feature_H},
            {data.Feature_I},
            {data.Feature_J},
            {data.Feature_K},
            {data.Feature_L},
            {data.Feature_M},
            {data.Feature_N},
            {data.Feature_O},
            {data.Feature_P},
            {data.Feature_Q},
            {data.Feature_R},
            {data.Feature_S},
            {data.Feature_T},
            {data.Feature_U},
            {data.Feature_V},
            {data.Feature_W},
            {data.Feature_X},
            {data.Feature_Y},
            {data.Feature_Z},
            {data.Feature_AA},
            {data.Feature_BB},
            {data.Feature_CC},
            {data.Feature_DD},
            {data.target}
        );
    """
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()


def generate_data(db_connect, df):
    while True:
        insert_data(db_connect, df.sample(1).squeeze())
        time.sleep(1)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--db-host", dest="db_host", type=str, default="localhost")
    args = parser.parse_args()

    db_connect = psycopg2.connect(
        user="zerohertz",
        password="qwer123!",
        host=args.db_host,
        port=5432,
        database="Breast_Cancer",
    )
    create_table(db_connect)
    df = get_data()
    generate_data(db_connect, df)
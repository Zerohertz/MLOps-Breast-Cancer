import os
from dotenv import load_dotenv
from argparse import ArgumentParser

import mlflow

load_dotenv()

os.environ["MLFLOW_S3_ENDPOINT_URL"] = os.environ.get("MLFLOW_S3_ENDPOINT_URL")
os.environ["MLFLOW_TRACKING_URI"] = os.environ.get("MLFLOW_TRACKING_URI")
os.environ["AWS_ACCESS_KEY_ID"] = os.environ.get("MINIO_ROOT_USER")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.environ.get("MINIO_ROOT_PASSWORD")

def download_model(args):
    mlflow.artifacts.download_artifacts(artifact_uri=f"runs:/{args.run_id}/{args.model_name}", dst_path=".")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--model-name", dest="model_name", type=str, default="sk_model")
    parser.add_argument("--run-id", dest="run_id", type=str)
    args = parser.parse_args()
    download_model(args)
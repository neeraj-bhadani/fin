from dotenv import dotenv_values

env = dotenv_values(".env")

app_config = {
    "s3": {
        "access_key": env["access_key"],
        "secret_key": env["secret_key"],
        "bucket_name": env["bucket_name"],
        "folder_name": env["folder_name"],
    },
    "db": {
        "db_name": env["db_name"],
        "db_pass": env["db_pass"],
    },
}

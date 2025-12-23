def load_sql(path):
    try:
        with open(path, "r") as file:
            file_script = file.read()
            return file_script
    except Exception as e:
        return {"Error": e}
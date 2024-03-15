from lazysource.database.db_manager import DBManager

def run():
    db_engine = "sqlite"
    dbmanager = DBManager(db_engine)
    port = 8000
    print(f"Running server on port: {port}")

if __name__ == "__main__":
    run()

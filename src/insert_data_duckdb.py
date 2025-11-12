import duckdb


def main():
    conn = duckdb.connect()

    conn.execute("""
    
    INSTALL httpfs;
    LOAD httpfs;
    
    INSTALL iceberg;
    LOAD iceberg;
    
    UPDATE EXTENSIONS;
    
    """)

    conn.execute("""
    
    CREATE SECRET (
        TYPE S3,
        KEY_ID 'minioadmin',
        SECRET 'minioadmin',
        ENDPOINT '127.0.0.1:9000',
        URL_STYLE 'path',
        USE_SSL 0
    );
    
    """)

    conn.execute("""
    
    ATTACH 'iceberg-bucket' AS iceberg (
        TYPE ICEBERG,
        AUTHORIZATION_TYPE 'none',
        ENDPOINT 'http://127.0.0.1:19120/iceberg/'
    );
    
    """)

    # conn.execute("USE iceberg.bronze;")
    tables = conn.execute("show tables;").df()
    print(tables)

    data = conn.execute("""
    select * from
    """).fetchall()
    print(data)

    print("Done!")


if __name__ == '__main__':
    main()

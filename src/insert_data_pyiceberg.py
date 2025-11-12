import os

import pandas as pd
import pyarrow as pa
from pyiceberg.catalog import (
    load_catalog,
    Catalog,
)


def main():
    nessie_catalog_config = {
        "type": "rest",
        "uri": os.getenv("NESSIE_URI", "http://127.0.0.1:19120/iceberg/"),
        "s3.endpoint": os.getenv("MINIO_ENDPOINT", "127.0.0.1:9000"),
        "s3.path-style-access": "true",
        "s3.access-key-id": "minioadmin",
        "s3.secret-access-key": "minioadmin"
    }

    catalog: Catalog = load_catalog("nessie", **nessie_catalog_config)

    namespaces = catalog.list_namespaces()
    print("namespaces", namespaces)
    print("tables", catalog.list_tables(namespace=namespaces[0]))

    table_identifier = "bronze.user"
    table = catalog.load_table(table_identifier)

    df = pd.DataFrame([
        {"name": "Bob"},
        {"name": "Alice"},
    ])

    arrow_table = pa.Table.from_pandas(df, preserve_index=False)
    table.append(arrow_table)


if __name__ == '__main__':
    main()

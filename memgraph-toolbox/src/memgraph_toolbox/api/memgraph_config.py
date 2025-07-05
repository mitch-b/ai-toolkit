from typing import TypedDict

class MemgraphConfigDict(TypedDict, total=False):
    """
    TypedDict for Memgraph client configuration.
    Supported keys:
        - database: str (e.g., {"database": "mydb"})
    """
    database: str

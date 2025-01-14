from pymilvus import MilvusClient, DataType
from pprint import pprint

milvus_client = MilvusClient("milvus_demo.db")


# res = milvus_client.describe_collection(
#     collection_name="dummy_demo1"
# )

res = milvus_client.query(
    collection_name="dummy_demo1",
    limit=5
)

pprint(res)
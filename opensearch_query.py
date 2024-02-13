import urllib3
from opensearchpy import OpenSearch, RequestsHttpConnection

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure the OpenSearch client
opensearch_client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin"),
    use_ssl=True,
    verify_certs=False,
    connection_class=RequestsHttpConnection,
)

response = opensearch_client.search(
    index="test-orda",
    body={
        "query": {"prefix": {"title": {"value": "toy"}}},
        "aggs": {"genres": {"terms": {"field": "genres.keyword", "size": 10}}},
    },
)

print(response["aggregations"])

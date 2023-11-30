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

print(opensearch_client.info())

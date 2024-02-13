import csv
import datetime

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

opensearch_client.indices.refresh()
with open("data/movies.csv") as input_file:
    csv_reader = csv.reader(input_file, delimiter=",")
    start = datetime.datetime.now()
    movies = []
    for row in csv_reader:
        doc_id = row[0]
        movies.append({"index": {"_index": "test-orda", "_id": doc_id}})
        title = row[1]
        # TODO extract year from title
        genres = row[2].split("|")
        movies.append({"id": doc_id, "title": title, "genres": genres})
        if len(movies) > 5000:
            opensearch_client.bulk(movies)
            movies = []
    opensearch_client.indices.refresh()
    print(datetime.datetime.now() - start)

# PREFIX QUERY
# + terms aggregations on genres

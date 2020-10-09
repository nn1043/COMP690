import os
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """

    SELECT *
    FROM ***
    LIMIT 1000
"""


query_job = client.query(query)  # Make an API request.

print("The query data:")
for row in query_job:
    # Row values can be accessed by field name or index.
    print("First Name = {}, Last Name = {}".format(row[1], row[0]))

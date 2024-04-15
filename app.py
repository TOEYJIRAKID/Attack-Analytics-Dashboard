from flask import Flask, render_template, jsonify
from elasticsearch import Elasticsearch
from collections import defaultdict
import datetime
import pytz
import json

app = Flask(__name__)

# Elasticsearch client setup
es = Elasticsearch(['http://172.28.1.60:9200'])

# Function to fetch data from Elasticsearch for bar chart
def fetch_data_from_elasticsearch():
    # Example query to retrieve data from Elasticsearch
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "@timestamp": {
                                "gte": "now-15m",  # Data from the last 15 minutes
                                "lte": "now"
                            }
                        }
                    },  
                       {
                        "match": {
                            "attack_type": "Ping of Death"
                        }
                    }
                ]
            }
        },
        "size": 10000
    }

    # Fetch data from Elasticsearch
    results = es.search(index="logstash-2024.04.07", body=query)
    results2 = []

   
    hits = results['hits']['hits']
    results2.extend([hit['_source'] for hit in hits])
    # print(results2)

    filename = f"data_all.json"

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(results2, json_file, ensure_ascii=False, indent=4)

    print(f"Data saved to '{filename}'")


    # Process and return the data for bar chart
    timestamp_counts = defaultdict(int)
    for hit in results['hits']['hits']:
        timestamp = hit['_source']['@timestamp']
        timestamp = convert_to_thai_time(timestamp)
        timestamp = timestamp[:17] + "00Z"
        timestamp_counts[timestamp] += 1

    sorted_data = sorted(timestamp_counts.items(), key=lambda x: x[0])
    data = [{'x': timestamp, 'y': count} for timestamp, count in sorted_data]
    return data

# Function to fetch data from Elasticsearch for pie chart
def fetch_data_for_pie_chart():
    # Example query to retrieve data from Elasticsearch
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "@timestamp": {
                                "gte": "now-15m",  # Data from the last 15 minutes
                                "lte": "now"
                            }
                        }
                    }
                ]
            }
        },
        "size": 0,
        "aggs": {
            "src_counts": {
                "terms": {
                    "field": "src.keyword",
                    "size": 10  # Adjust based on the number of source IPs you want to retrieve
                }
            }
        }
    }

    # Fetch data from Elasticsearch
    results = es.search(index="logstash-2024.04.07", body=query)
    # print(results)  # Print the Elasticsearch response

    # Process and return the data for pie chart
    src_counts = defaultdict(int)
    for bucket in results['aggregations']['src_counts']['buckets']:
        src = bucket['key']
        count = bucket['doc_count']
        src_counts[src] = count

    return src_counts

# Function to convert timestamp to Thai time zone
def convert_to_thai_time(timestamp):
    datetime_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    utc_datetime = pytz.utc.localize(datetime_obj)
    thai_timezone = pytz.timezone('Asia/Bangkok')
    thai_datetime = utc_datetime.astimezone(thai_timezone)
    formatted_timestamp = thai_datetime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_timestamp

# Route to render HTML page with real-time chart
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch real-time data from Elasticsearch for bar chart
@app.route('/data')
def get_data():
    data = fetch_data_from_elasticsearch()
    return jsonify(data)

# Route to fetch real-time data from Elasticsearch for pie chart
@app.route('/data/pie')
def get_pie_chart_data():
    data = fetch_data_for_pie_chart()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
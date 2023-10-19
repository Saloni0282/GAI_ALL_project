# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from pinecone import Connection, create_index, delete_index
# from pinecone import Pinecone
# # Load the JSON data
# data = pd.read_json('data/product_data.json')

# # Create a TF-IDF vectorizer for text embedding
# vectorizer = TfidfVectorizer()
# embeddings = vectorizer.fit_transform(data['description'])

# # Connect to Pinecone
# pinecone_api_key = 'cf9ec2c6-6082-47ad-8aa2-0b46c215d911'
# pinecone_index_name = 'cloozo'
# pinecone = Connection(api_key=pinecone_api_key)

# # Delete the index if it already exists
# delete_index(pinecone_index_name)

# # Create a new Pinecone index
# create_index(pinecone_index_name, metric="cosine")

# # Insert product embeddings into Pinecone
# pinecone.upsert(pinecone_index_name, data['id'], embeddings)

# # Function to recommend products
# def recommend_products(query, k=10):
#     query_embedding = vectorizer.transform([query])
#     results = pinecone.query(pinecone_index_name, query_embedding, top_k=k)
#     return results.ids

# if __name__ == '__main__':
#     query = input("Enter your query: ")
#     recommended_ids = recommend_products(query)
#     recommended_products = data[data['id'].isin(recommended_ids)]
#     print(recommended_products)

import json
import pinecone

# Load the product data from a JSON file
with open('product_data.json', 'r') as file:
    product_data = json.load(file)

# Initialize Pinecone client
pinecone.init(api_key='cf9ec2c6-6082-47ad-8aa2-0b46c215d911', environment='asia-southeast1-gcp-free')

# Create an index
index_name = 'cloozo'
index = pinecone.Index(index_name)

# Define a function to convert product data to Pinecone records
def convert_to_records(data):
    records = []
    for product in data['products']:
        record = {
            'id': str(product['id']),
            'title': product['title'],
            'description': product['description'],
            'category': product['category'],
        }
        records.append(record)
    return records

# Convert the product data to Pinecone records
product_records = convert_to_records(product_data)

# Upsert product records into Pinecone
pinecone.upsert_items(index_name, items=product_records)

# Perform a semantic search
def search_products(query, k=10):
    results = pinecone.query(index_name, query, top_k=k)
    return results.items

# Example query
query = "Apple iPhone"
search_results = search_products(query, k=10)

# Print the search results
for result in search_results:
    print(f"Product ID: {result.id}, Title: {result.fields['title']}")

# Clean up - delete the index
pinecone.delete_index(index_name)

# Close the Pinecone client
pinecone.deinit()

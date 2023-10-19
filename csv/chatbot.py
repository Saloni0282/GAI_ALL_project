# from langchain.agents import create_csv_agent
# from langchain.llms import OpenAI
# from dotenv import load_dotenv
# import os
# import streamlit as st
# import openai

# load_dotenv()

# def main():
#   st.set_page_config(page_title="Ask your CSV")
#   st.header("Ask your CSV 📈")

#   csv_file = st.file_uploader("Upload a CSV file", type="csv")
#   if csv_file is not None:

#     agent = create_csv_agent(
#       OpenAI(temperature=0), csv_file, verbose=True)

#     user_question = st.text_input("Ask a question about your CSV: ")

#     if user_question is not None and user_question != "":
#       with st.spinner(text="In progress..."):
#         output = agent.run(user_question)
#         output_str = "".join(output)
#         st.write(output_str)


# if __name__ == "__main__":
#   main()

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pinecone import Connection, create_index, delete_index

# Load the JSON data
data = pd.read_json('data/product_data.json')

# Create a TF-IDF vectorizer for text embedding
vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(data['description'])

# Connect to Pinecone
pinecone_api_key = 'cf9ec2c6-6082-47ad-8aa2-0b46c215d911'
pinecone_index_name = 'cloozo'
pinecone = Connection(api_key=pinecone_api_key)

# Delete the index if it already exists
delete_index(pinecone_index_name)

# Create a new Pinecone index
create_index(pinecone_index_name, metric="cosine")

# Insert product embeddings into Pinecone
pinecone.upsert(pinecone_index_name, data['id'], embeddings)

# Function to recommend products
def recommend_products(query, k=10):
    query_embedding = vectorizer.transform([query])
    results = pinecone.query(pinecone_index_name, query_embedding, top_k=k)
    return results.ids

if __name__ == '__main__':
    query = input("Enter your query: ")
    recommended_ids = recommend_products(query)
    recommended_products = data[data['id'].isin(recommended_ids)]
    print(recommended_products)

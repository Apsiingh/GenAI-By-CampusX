import os

os.environ['HF_HOME'] = 'C:/huggingface_cache'

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as numpy


embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about Rohit Sharma'

docEmbedding = embedding.embed_documents(documents)
queryEmbedding = embedding.embed_query(query)

source = cosine_similarity([queryEmbedding], docEmbedding)[0]
print(source)

index, score = sorted(list(enumerate(source)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)
import pandas as pd
import faiss
import numpy as np
import uuid
from sklearn.feature_extraction.text import TfidfVectorizer

class Portfolio:
    def __init__(self, file_path="my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.vectorizer = TfidfVectorizer()
        self.index = None
        self.techstack_vectors = None
        self.load_portfolio()

    def load_portfolio(self):
        techstack_text = self.data["Techstack"].tolist()
        self.techstack_vectors = self.vectorizer.fit_transform(techstack_text).toarray()

        # Build FAISS index
        self.index = faiss.IndexFlatL2(self.techstack_vectors.shape[1])  # L2 distance metric
        self.index.add(self.techstack_vectors)

    def query_links(self, skills):
        # Vectorize the query
        skill_vector = self.vectorizer.transform([skills]).toarray()
        D, I = self.index.search(skill_vector, 3)  # Search for top 2 results
        results = []
        for idx in I[0]:
            if idx != -1:  # Ignore invalid results
                results.append({"links": self.data.iloc[idx]["Links"]})
        return results

import pandas as pd
import uuid
from langchain.vectorstores import Chroma

class Portfolio:
    def __init__(self, file_path="my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        # Initialize Chroma with persistent storage
        self.chroma_client = Chroma(persist_directory="vectorstore")
        self.collection = self.chroma_client

    def load_portfolio(self):
        if not self.collection._collection.count():
            for _, row in self.data.iterrows():
                self.collection.add_texts(
                    texts=[row["Techstack"]],
                    metadatas=[{"links": row["Links"]}],
                    ids=[str(uuid.uuid4())]
                )
            self.collection.persist()

    def query_links(self, skills):
        # Mimicking query behavior exactly
        results = self.collection._collection.query(query_texts=[skills], n_results=2)
        return results['metadatas']

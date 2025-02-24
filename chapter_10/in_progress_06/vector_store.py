from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class VectorStore:
  def __init__(self, api_keys, index_name):
    pc = Pinecone(api_key=api_keys["VECTOR_STORE_API_KEY"])
    embeddings = OpenAIEmbeddings(api_key=api_keys["OPENAI_API_KEY"])
    index = pc.Index(index_name)
    self.store = PineconeVectorStore(index=index, embedding=embeddings)

  def ingest_folder(self, folder_path):
    loader = DirectoryLoader(
      folder_path,
      glob="**/*.txt",
      loader_cls=TextLoader
    )
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
      chunk_size=1000,
      chunk_overlap=200
    )
    texts = splitter.split_documents(documents)
    self.store.add_documents(texts)

  def retrieve(self, query):
    return self.store.similarity_search(query)

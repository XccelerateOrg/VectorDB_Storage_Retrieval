from config import model_cache
from langchain.embeddings import HuggingFaceBgeEmbeddings


model_kwargs = {'device': 'cpu'}                # change this to cuda if you have a compatible nVidia GPU
encode_kwargs = {'normalize_embeddings': True}


bge_base_embeddings = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-base-en",
                                               model_kwargs=model_kwargs,
                                               encode_kwargs=encode_kwargs,
                                               cache_folder=model_cache)

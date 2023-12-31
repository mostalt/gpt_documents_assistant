from functools import partial

from .pinecone import build_retriever

retriever_map = {
  "pinecone1": partial(build_retriever, k=1),
  "pinecone2": partial(build_retriever, k=2),
  "pinecone3": partial(build_retriever, k=3),
}
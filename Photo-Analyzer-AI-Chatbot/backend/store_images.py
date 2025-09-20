

from backend.vectordb import ChromaDatabase


# Store images
db = ChromaDatabase(collection_name="image_embeddings2", persist_directory="./db")
db.store_images_in_chroma("../frontend/static/images")



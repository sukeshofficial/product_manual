from qdrant_client import QdrantClient
from docling.chunking import HybridChunker
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter

client = QdrantClient(
    url="<your QDrant URL>",
    api_key="<your QDrant_KEY>"
)

COLLECTION_NAME = "product_manual"
client.set_model("sentence-transformers/all-MiniLM-L6-v2")
client.set_sparse_model("Qdrant/bm25")

converter = DocumentConverter(
    allowed_formats=[
        InputFormat.PDF,
        InputFormat.DOCX,
        InputFormat.XLSX,
        InputFormat.PPTX,
        InputFormat.CSV
    ]
)

def upload_file(COLLECTION_NAME ,file_path):
    result = converter.convert(file_path)
    documents, metadatas = [], []

    for i, chunk in enumerate(HybridChunker().chunk(result.document)):
        documents.append(chunk.text)
        metadatas.append(chunk.meta.export_json_dict())
        print(f"©️ Data chunking: {i + 1}")

    client.add(
        collection_name=COLLECTION_NAME,
        documents=documents,
        metadata=metadatas,
        batch_size=64,
    )  

file_path = "<complete file_path>"

try:
    upload_file(COLLECTION_NAME, file_path)
    print(f"Uploaded {file_path} to Qdrant successfully!🟢")
except Exception as e:
    print(f"❌ Failed to upload: {e}")
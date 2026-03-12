import os
import shutil
from typing import Any, List, Optional
from app.domain.repository.document_repository import IDocumentRepository
from app.domain.utils import parrallel_pdf_to_img, parallel_save_texts
from app.infrastructure.repository.text_extractor import TextExtractor

class DocumentManagerRepository(IDocumentRepository):
    def __init__(self):
        pass

    async def save_document_locally(self, file: Any, upload_folder: Optional[str] = 'uploads') -> str:
        os.makedirs(upload_folder, exist_ok=True)
        local_file_path = f"{upload_folder}/{file.filename}"
        try:
            with open(local_file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return local_file_path
        except Exception as e:
            print({"message": f"There was an error uploading the file: {e}"})
            raise
        finally:
            await file.close()

    def process_document(self, local_file_path: str, file_type: str) -> List[str]:
        return parrallel_pdf_to_img(local_file_path)
    
    def extract_text(self, file_path: str, file_type: str) -> str:
        return TextExtractor(file_path, file_type).extract()

    def save_texts(self, text_list: List[str]) -> List[str]:
        return parallel_save_texts(text_list)


import fitz
from docx import Document

class TextExtractor:
    def __init__(self, file_path: str, file_type: str):
        self.file_path = file_path
        self.file_type = file_type
        pass
    
    def extract_text_from_pdf(self) -> str:
        try:
            doc = fitz.open(self.file_path)
            
            texto_completo = ""
            for pagina in doc:
                texto_completo += pagina.get_text()
            doc.close()
            
            return texto_completo
        
        except Exception as e:
            raise ValueError(f"Error to extract information from pdf {e}")
    
    def extract_text_from_word(self) -> str:
        doc = Document(self.file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    def extract(self) -> str:
        MAPPER_FILE_TRANSFORMATION = {
            "application/pdf": self.extract_text_from_pdf,
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": self.extract_text_from_word,
        }   

        if self.file_type not in MAPPER_FILE_TRANSFORMATION:
            raise ValueError(f"Unknown file_type : {self.file_type}")
        
        return MAPPER_FILE_TRANSFORMATION[self.file_type]()
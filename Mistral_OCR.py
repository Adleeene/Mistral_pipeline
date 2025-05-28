import os
import base64
import json
from mistralai import Mistral
from typing import Optional, Dict, Any
from classes.pydantic_model import Report


class PDFProcessor:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PDF processor with Mistral API key."""
        self.api_key = api_key or os.getenv("MISTRAL_API_KEY") or "bi78LN9q7kO3MmNlzmzlvDOjjieuod4j"
        self.client = Mistral(api_key=self.api_key)
    
    def encode_pdf(self, pdf_path: str) -> str:
        """Encode PDF file to base64 string."""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
        
        file_size = os.path.getsize(pdf_path)
        print(f"PDF file size: {file_size / (1024*1024):.2f} MB")
        
        if file_size > 50 * 1024 * 1024:  # 50MB limit
            raise ValueError(f"PDF file too large: {file_size / (1024*1024):.2f} MB. Maximum: 50MB")
        
        try:
            with open(pdf_path, "rb") as pdf_file:
                return base64.b64encode(pdf_file.read()).decode('utf-8')
        except Exception as e:
            raise IOError(f"Failed to read PDF file: {str(e)}")
    
    def process_ocr(self, pdf_path: str) -> Dict[str, Any]:
        """Process PDF with Mistral OCR."""
        print("\n=== OCR PROCESSING ===")

        print("Encoding PDF to base64...")
        base64_pdf = self.encode_pdf(pdf_path)
        print(f"Base64 string length: {len(base64_pdf)} characters")
        
        try:
            print("Sending OCR request to Mistral API...")
            ocr_response = self.client.ocr.process(
                model="mistral-ocr-latest",
                document={
                    "type": "document_url", 
                    "document_url": f"data:application/pdf;base64,{base64_pdf}"
                },
                include_image_base64=True
            )
            print("OCR request completed")
            return ocr_response
        except Exception as e:
            raise RuntimeError(f"OCR processing failed: {str(e)}")
    
    def analyze_report(self, ocr_response: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze report from OCR response to produce structured output."""
        print("\n=== REPORT ANALYSIS ===")

        # Build full text with page numbers
        full_text = ""
        for i, page in enumerate(ocr_response.pages):
            full_text += f"Page {i+1}:\n{page.markdown}\n\n"
        
        # Limit text size
        max_chars = 15000
        if len(full_text) > max_chars:
            full_text = full_text[:max_chars]
            print(f"Document truncated to {max_chars} characters")
        
        # Define messages for Mistral API
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert in analyzing technical documents. Extract the document details, "
                    "intervention control information, and list of elements according to the following structure:\n"
                    "{\n"
                    "  \"document\": {\"name\": \"string\", \"number\": integer, \"date\": \"YYYY-MM-DD\", \"pages_number\": integer},\n"
                    "  \"intervention_control\": {\"name\": \"string\", \"start_date\": \"YYYY-MM-DD\", \"end_date\": \"YYYY-MM-DD\", "
                    "\"inspector_company\": \"string\", \"inspector_agency\": \"string\", \"inspector_name\": \"string\", "
                    "\"customer_company\": \"string\", \"customer_adress\": \"string\", \"customer_factory\": \"string\", "
                    "\"elements_number\": integer, \"tasks_number\": integer},\n"
                    "  \"elements\": [{\"number\": integer, \"page\": integer, \"inspector\": \"string\", \"name\": \"string\", "
                    "\"n_internal\": integer, \"factory\": \"string\", \"building\": \"string\"}]\n"
                    "}\n"
                    "Return ONLY a valid JSON object matching this structure. Do not include any additional text."
                )
            },
            {
                "role": "user",
                "content": full_text
            }
        ]
        
        try:
            print("Sending analysis request to Mistral API...")
            chat_response = self.client.chat.complete(
                model="mistral-large-latest",
                messages=messages,
                response_format={"type": "json_object"},
                temperature=0.1,
                max_tokens=3000
            )
            print("Analysis request completed")
            
            # Extract JSON from response
            response_content = chat_response.choices[0].message.content
            json_data = json.loads(response_content)
            
            # print("-----------------json_data-----------------")
            # print(json_data)
            # print("-----------------json_data-----------------")
            # Validate with Pydantic
            report = Report.model_validate(json_data)


            # Convert to dictionary
            return report.model_dump()
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {str(e)}")
            raise RuntimeError(f"Failed to parse JSON response: {str(e)}")
        except Exception as e:
            print(f"Analysis error: {str(e)}")
            raise RuntimeError(f"Report analysis failed: {str(e)}")

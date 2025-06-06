import json
from Mistral_OCR import PDFProcessor
from helper_function.enrich_report_with_regulations import enrich_report_with_regulations
from helper_function.enrich_report_with_type_element import enrich_report_with_type_element

def main():
    """Main execution function."""
    pdf_path = "../test_PDF/test_gpt_api.pdf"  # Changed to use a local path
    
    try:
        print(f"Starting processing of: {pdf_path}")
        
        # Initialize processor
        processor = PDFProcessor()
        
        # Process PDF with OCR
        ocr_response = processor.process_ocr(pdf_path)
        print("✓ OCR processing completed")
        # print(ocr_response)
        

        # Analyze report
        report_data = processor.analyze_report(ocr_response)


        # Afficher le résultat de manière formatée
        print("\nRésultat formaté :")
        print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))

    

        # Enrich report with regulations
        report_data = enrich_report_with_regulations(report_data)

        # Enrich report with element type
        report_data = enrich_report_with_type_element(report_data)

        # Save to file
        output_file = "report_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Results saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
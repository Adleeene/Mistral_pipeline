import json
import time
from Mistral_OCR import PDFProcessor
from enrich_report_with_regulations import enrich_report_with_regulations
from enrich_report_with_type_element import enrich_report_with_type_element
from observations import enrich_report_with_observations

def main():
    """Main execution function."""
    pdf_path = "/Users/emiliano/Documents/Mistral_pipeline/test_gpt_api.pdf"
    
    try:
        print(f"Starting processing of: {pdf_path}")
        
        # Initialize processor
        processor = PDFProcessor()
        
        # Process PDF with OCR
        ocr_response = processor.process_ocr(pdf_path)
        print("✓ OCR processing completed")
        
        # Analyze report
        report_data = processor.analyze_report(ocr_response)
        print("✓ Report analysis completed")
        
        # Add delay to avoid rate limiting
        print("⏳ Waiting 3 seconds to avoid rate limiting...")
        time.sleep(3)

        # Enrich report with regulations
        report_data = enrich_report_with_regulations(report_data)
        print("✓ Regulations enrichment completed")
        
        # Add delay to avoid rate limiting
        print("⏳ Waiting 3 seconds to avoid rate limiting...")
        time.sleep(3)

        # Enrich report with element type
        report_data = enrich_report_with_type_element(report_data)
        print("✓ Element type enrichment completed")
        
        # Add delay to avoid rate limiting
        print("⏳ Waiting 3 seconds to avoid rate limiting...")
        time.sleep(3)

        # NEW: Enrich report with observations
        report_data = enrich_report_with_observations(report_data)
        print("✓ Observations extraction completed")

        # Display results
        print(f"\n✓ Complete report analysis results:")
        print(json.dumps(report_data, indent=2, ensure_ascii=False))
        
        # Save to file
        output_file = "complete_report_analysis.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Complete results saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
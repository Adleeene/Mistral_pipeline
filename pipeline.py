import json
from Mistral_OCR import PDFProcessor

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

        # Display clean JSON result (your required format)
        print("\n" + "="*60)
        print("RÉSULTAT FORMATÉ:")
        print("="*60)
        print(json.dumps(report_data, indent=2, ensure_ascii=False, sort_keys=False))
        
        # Display schema selection summary separately
        schema_summary = processor.get_schema_selection_summary()
        if schema_summary:
            print("\n" + "="*60)
            print("SCHEMA SELECTION SUMMARY:")
            print("="*60)
            for selection in schema_summary:
                print(f"Element {selection['element_number']}: {selection['equipment_name']}")
                print(f"  Selected: {selection['selected_schema']}")
                print(f"  Confidence: {selection['confidence']}")
                print(f"  Candidates: {len(selection['candidate_schemas'])} schemas considered")
                if selection['candidate_schemas']:
                    print(f"  Top candidates: {', '.join(selection['candidate_schemas'][:3])}")
                print()

        # Save clean JSON to file (your required format)
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
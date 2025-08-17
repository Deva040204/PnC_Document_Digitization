# P&C Document Digitization

End-to-end AWS solution for OCR and NLP-based extraction of insurance document data.

PnC_Document_Digitization/
├── README.md
├── cloudformation/
│   └── template.yaml              # CloudFormation template (to be filled in)
├── lambda/
│   ├── upload_trigger/
│   │   └── lambda_function.py     # Lambda to start Textract job
│   └── textract_processor/
│       └── lambda_function.py     # Lambda to process Textract result + SageMaker
├── sagemaker/
│   └── model_inference.ipynb      # Placeholder notebook
├── test_files/
│   └── (for sample PDFs, outputs)
└── docs/
    └── deployment_guide.md        # Setup and instructions


from rfq_extractor import extract_rfq
from rfq_validator import validate_rfq
from followup_generator import generate_followup_email
from sheets_integration import save_rfq_to_sheet


def process_rfq(email_text):

    print("\nProcessing incoming RFQ...\n")

    # Step 1: Extract RFQ information
    rfq_data = extract_rfq(email_text)

    print("Extracted RFQ Information:")
    print(rfq_data)

    # Step 2: Validate extracted information
    missing_fields = validate_rfq(rfq_data)

    print("\nMissing Information:")
    print(missing_fields)

    # Step 3: Generate appropriate email
    email_draft = generate_followup_email(
        rfq_data,
        missing_fields
    )

    print("\nGenerated Email:")
    print(email_draft)

    # Step 4: Save RFQ information to Google Sheets
    save_rfq_to_sheet(
        rfq_data,
        missing_fields,
        email_draft
    )

    print("\nRFQ Processing Completed!")


# Sample incoming RFQ email
sample_email = """
Dear Procurement Team,

We require 500 MT of VG30 Bitumen.

Delivery Location: Ahmedabad, Gujarat.
Expected Delivery: Within 10 days.

Contact Person: Rahul Sharma
Email: rahul@example.com
Phone: 9876543210

Please share your quotation.

Regards,
Rahul
"""

# Run the automation
if __name__ == "__main__":
    process_rfq(sample_email)

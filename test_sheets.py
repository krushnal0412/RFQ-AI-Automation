
from sheets_integration import save_rfq_to_sheet

# Sample RFQ information
rfq_data = {
    "material": "VG30 Bitumen",
    "quantity": 500,
    "unit": "MT",
    "delivery_location": "Ahmedabad, Gujarat",
    "delivery_timeline": "Within 10 days",
    "contact_person": "Rahul Sharma",
    "contact_email": "rahul@example.com",
    "contact_phone": "9876543210"
}

# No missing fields
missing_fields = []

# Sample acknowledgment email
email_draft = """
Subject: RFQ Received - VG30 Bitumen

Dear Rahul,

Thank you for sharing your requirement for 500 MT
of VG30 Bitumen.

Our team will check availability, pricing and
delivery feasibility and get back to you.

Best regards,
Procurement Team
"""

# Save the RFQ
save_rfq_to_sheet(
    rfq_data,
    missing_fields,
    email_draft
)

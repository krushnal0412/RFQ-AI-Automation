
from followup_generator import generate_followup_email


# SCENARIO 1: Incomplete RFQ

incomplete_rfq = {
    "material": "VG30 Bitumen",
    "quantity": None,
    "unit": "MT",
    "delivery_location": None,
    "delivery_timeline": "Within 10 days",
    "contact_person": "Rahul Sharma",
    "contact_email": None,
    "contact_phone": None
}

missing_fields = [
    "quantity",
    "delivery_location"
]

print("\n========== SCENARIO 1 ==========")
print("INCOMPLETE RFQ")

email_draft = generate_followup_email(
    incomplete_rfq,
    missing_fields
)

print("\nGenerated Email:")
print(email_draft)


# SCENARIO 2: Complete RFQ

complete_rfq = {
    "material": "VG30 Bitumen",
    "quantity": 500,
    "unit": "MT",
    "delivery_location": "Ahmedabad, Gujarat",
    "delivery_timeline": "Within 10 days",
    "contact_person": "Rahul Sharma",
    "contact_email": "rahul@example.com",
    "contact_phone": "9876543210"
}

missing_fields = []

print("\n========== SCENARIO 2 ==========")
print("COMPLETE RFQ")

email_draft = generate_followup_email(
    complete_rfq,
    missing_fields
)

print("\nGenerated Email:")
print(email_draft)

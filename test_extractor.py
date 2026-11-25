from rfq_extractor import extract_rfq

sample_email = """
We need 500 MT of VG30 Bitumen.
Delivery location: Ahmedabad, Gujarat.
Expected delivery: Within 10 days.
Contact person: Rahul Sharma.
"""

result = extract_rfq(sample_email)

print("\nExtracted RFQ Information:")
print(result)

print("\nData Type:")
print(type(result))
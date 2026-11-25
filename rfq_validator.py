def validate_rfq(rfq_data):

    required_fields = [
        "material",
        "quantity",
        "unit",
        "delivery_location",
        "delivery_timeline"
    ]

    missing_fields = []

    for field in required_fields:

        value = rfq_data.get(field)

        if value is None or (isinstance(value, str) and not value.strip()):
            missing_fields.append(field)

    return missing_fields

rfq_data = {
    "material": "VG30 Bitumen",
    "quantity": 500,
    "unit": "MT",
    "delivery_location": None,
    "delivery_timeline": "Within 10 days"
}

missing_fields = validate_rfq(rfq_data)

print(missing_fields)
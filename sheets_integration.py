
import gspread

# Connect to Google Sheets
client = gspread.service_account(
    filename="service_account.json"
)

# Open spreadsheet and worksheet
spreadsheet = client.open("RFQ Automation Tracker")
worksheet = spreadsheet.sheet1


def save_rfq_to_sheet(rfq_data, missing_fields, email_draft):

    # Generate RFQ ID
    rfq_id = "RFQ-" + str(len(worksheet.get_all_values()))

    # Determine RFQ status
    if missing_fields:
        status = "Pending Information"
    else:
        status = "Received"

    # Prepare data for Google Sheets
    row = [
        rfq_id,
        rfq_data.get("material"),
        rfq_data.get("quantity"),
        rfq_data.get("unit"),
        rfq_data.get("delivery_location"),
        rfq_data.get("delivery_timeline"),
        rfq_data.get("contact_person"),
        rfq_data.get("contact_email"),
        rfq_data.get("contact_phone"),
        ", ".join(missing_fields),
        status,
        email_draft
    ]

    # Save data
    worksheet.append_row(row)

    print(f"{rfq_id} saved successfully!")


if __name__ == "__main__":
    print("Google Sheets integration ready!")

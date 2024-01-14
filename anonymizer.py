import pandas as pd
from anonymizer_helper import DataAnonymizer


def anonymize_file(input_file_path, output_file_path):
    anonymizer = DataAnonymizer()

    if input_file_path.endswith(".csv"):
        data = pd.read_csv(input_file_path)
    elif input_file_path.endswith((".xls", ".xlsx")):
        data = pd.read_excel(input_file_path)
    else:
        raise ValueError(
            "Unsupported file format. Only CSV and Excel files are supported."
        )

    data.columns = data.columns.str.strip()
    headers = data.columns

    anonymized_data = pd.DataFrame()

    for header in headers:
        if "Customer Name" in header:
            anonymized_data[header] = anonymizer.anonymize_customer_names(data[header])
        elif "SSN" in header:
            anonymized_data[header] = anonymizer.anonymize_social_security_numbers(data[header])
        elif "Account Number" in header:
            anonymized_data[header] = anonymizer.anonymize_account_numbers(data[header])
        elif "Branch" in header:
            anonymized_data[header] = anonymizer.anonymize_branch_codes(data[header])
        else:
            anonymized_data[header] = data[header]


    # Save the anonymized data to the output file
    if output_file_path.endswith('.csv'):
       anonymized_data.to_csv(output_file_path, index=False)
       print(f"Anonymized file saved to {output_file_path}")
    elif output_file_path.endswith(('.xls', '.xlsx')):
       anonymized_data.to_excel(output_file_path, index=False)
    else:
      raise ValueError(
        "Unsupported output file format. Only CSV and Excel files are supported for output."
    )

    return output_file_path

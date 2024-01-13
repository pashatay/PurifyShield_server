import pandas as pd
from anonymizer_helper import DataAnonymizer

def anonymize_file(input_file_path, output_file_path):
    # Create an instance of the DataAnonymizer class
    anonymizer = DataAnonymizer()

    # Determine the file format (CSV or Excel)
    if input_file_path.endswith('.csv'):
        # Read CSV data
        data = pd.read_csv(input_file_path)
    elif input_file_path.endswith(('.xls', '.xlsx')):
        # Read Excel data
        data = pd.read_excel(input_file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    # Assuming the first row contains column headers, we can use them to identify the data types
    headers = data.columns

    # Create an empty DataFrame to store the anonymized data
    anonymized_data = pd.DataFrame()

    # Loop through each column and apply the suitable anonymization function based on the header name
    for header in headers:
        if 'Customer Name' in header:
            anonymized_data[header] = anonymizer.anonymize_customer_names(data[header])
        elif 'Social Security Number | SSN' in header:
            anonymized_data[header] = anonymizer.anonymize_social_security_numbers(data[header])
        elif 'Account Number' in header:
            anonymized_data[header] = anonymizer.anonymize_account_numbers(data[header])
        # Add similar conditions for other data types...
        else:
            # If the header doesn't match any relevant data, copy it as is to the anonymized data
            anonymized_data[header] = data[header]

    # Save the anonymized data to the output file
    if output_file_path.endswith('.csv'):
        anonymized_data.to_csv(output_file_path, index=False)
    elif output_file_path.endswith(('.xls', '.xlsx')):
        anonymized_data.to_excel(output_file_path, index=False)
    else:
        raise ValueError("Unsupported output file format. Only CSV and Excel files are supported for output.")

    return output_file_path
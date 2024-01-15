import pandas as pd
from anonymizer_helper import DataAnonymizer
import json


def anonymize_file(input_file_path, output_file_path, config_path):
    # Load the configuration
    with open(config_path, "r") as file:
        config = json.load(file)

    # Create an instance of DataAnonymizer
    anonymizer = DataAnonymizer()

    # Read the input file
    if input_file_path.endswith(".csv"):
        data = pd.read_csv(input_file_path)
    elif input_file_path.endswith((".xls", ".xlsx")):
        data = pd.read_excel(input_file_path)
    else:
        raise ValueError(
            "Unsupported file format. Only CSV and Excel files are supported."
        )

    # Prepare the dataframe
    data.columns = data.columns.str.strip().str.lower()
    headers = data.columns
    anonymized_data = pd.DataFrame()

    # Anonymize data based on configuration
    for header in headers:
        function_name = config.get(header, None)
        if function_name:
            anonymization_function = getattr(anonymizer, function_name, None)
            if anonymization_function:
                anonymized_data[header] = anonymization_function(data[header])
            else:
                raise ValueError(
                    f"Anonymization function {function_name} not found for column {header}"
                )
        else:
            # Copy the data as is if no anonymization function is specified
            anonymized_data[header] = data[header]

    # Save the anonymized data to the output file
    if output_file_path.endswith(".csv"):
        anonymized_data.to_csv(output_file_path, index=False)
    elif output_file_path.endswith((".xls", ".xlsx")):
        anonymized_data.to_excel(output_file_path, index=False)
    else:
        raise ValueError(
            "Unsupported output file format. Only CSV and Excel files are supported for output."
        )

    return output_file_path

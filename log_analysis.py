import sys
import os
import re


def get_log_file_path_from_cmd_line(param_num):
    """Get the full path of a log file from the command line

    Args:
        param_num (int): Parameter number

    Returns:
        str: Full path of the log file
    """

    num_params = len(sys.argv) - 1
    if num_params >= 1:
        log_file_path = sys.argv[1]
        if os.path.isfile(log_file_path):
            return os.path.abspath(log_file_path)
        else:
            print("Error: Specified path is not a file.")
            sys.exit(1)
    else:
        print("Error: Missing log file path.")
        sys.exit(1)

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex."""

    records = []
    captured_data = []

    regex_flags = re.IGNORECASE if ignore_case else 0

    with open(log_file, 'r') as file:
        # Iterate through file line by line
        for line in file:
        # Check line for regex match
            match = re.search(regex, line, regex_flags)
            if match:
                records.append(line)

                if match.lastindex:
                    captured_data.append(match.groups())

    if print_records is True:
        print(*records, sep='', end='\n')
    
    if print_summary is True:
        print(f'The log file contains {len(records)} records that case-{"in" if ignore_case else  ""}sensitive match the regex "{regex}". ')


    return records,captured_data
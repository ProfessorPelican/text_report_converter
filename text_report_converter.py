# -*- coding: utf-8 -*-
'''
Description: Imports and extracts fields from text report file into a Pandas DataFrame.

Selected fields are extracted from the report, based on the location of
strings that designate header line(s) and detail line(s), and then the
location of field strings within those header and detail lines.

The imported raw data can be used to determine string and field locations.

All fields are returned as strings.

Example Usage:
REPORT_PATH = 'C:/data/report.txt'
HEADER_MARKER = {'string': 'Account:', 'row': 1, 'start': 3, 'stop': 11}
DETAIL_MARKER = {'string': '0', 'row': 2, 'start': 2, 'stop': 3}
HEADER_FIELDS = [{'name': 'account', 'row': 1, 'start': 13, 'stop': 21},
                 {'name': 'department', 'row': 1, 'start': 68, 'stop': 71}]
DETAIL_FIELDS = [{'name': 'vendor_name', 'row': 1, 'start': 19, 'stop': 29},
                 {'name': 'invoice_amount', 'row': 2, 'start': 131, 'stop': 180}]

raw_data = import_raw_data(REPORT_PATH)
report = convert_report(REPORT_PATH, DETAIL_MARKER, DETAIL_FIELDS,
                       HEADER_MARKER, HEADER_FIELDS)
'''
import pandas as pd

def import_report(file_path, detail_marker, detail_fields,
                  header_marker=None, header_fields=None, raw_data=None):
    # Import text report and extracts fields from raw data.

    # Imports raw report if one is not passed to it.
    if not raw_data:
        raw_data = import_raw_data(file_path)

    # Sets containers for current record fields and overall results.
    columns = []
    if header_fields:
        for i in range(len(header_fields)):
            columns.append(header_fields[i]['name'])
    for i in range(len(detail_fields)):
        columns.append(detail_fields[i]['name'])

    current_fields = dict.fromkeys(columns)
    results_list = []
    results_dataframe = pd.DataFrame()

    # Loops through all lines in text file.
    for i in range(len(raw_data)):

        # Finds header row and sets header fields (if there is a header).
        if header_marker and (raw_data[i][header_marker['start']: header_marker['stop']] ==
                              header_marker['string']):
            current_fields = define_fields(i, raw_data, current_fields,
                                           header_marker, header_fields)

        # Finds detail row and sets detail fields.
        # Note: detail may be on same row as header, so use if not elif.
        if (raw_data[i][detail_marker['start']: detail_marker['stop']] ==
                detail_marker['string']):
            current_fields = define_fields(i, raw_data, current_fields,
                                           detail_marker, detail_fields)

            # Appends header and detail results together.
            results_list.append(current_fields.copy())

    results_dataframe = pd.DataFrame(results_list, columns=columns)
    return results_dataframe

def import_raw_data(file_path):
    # Imports report file and reads into list.
    with open(file_path) as f:
        raw_data = f.read().splitlines()
    f.close()
    return raw_data

def define_fields(counter, raw_data, current_fields, marker,
                  fields):
    # Defines header or detail fields using constants above, returns fields.

    # Defines start of header or detail using counter.
    start_row = counter - (marker['row'] - 1)

    # Loops through header or detail to set fields.
    for x in range(len(fields)):
        field_row = start_row + (fields[x]['row'] - 1)
        string = (raw_data[field_row]
                  [fields[x]['start']: fields[x]['stop']])
        current_fields[fields[x]['name']] = string.strip()

    return current_fields

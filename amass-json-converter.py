#!/usr/bin/env python3

import sys
import json
import numpy
import pandas
import pathlib
import argparse
import xlsxwriter

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Converts OWASP amass (v3.15.2) json files into CSV or XLSX.")
    # Add arguments
    parser.add_argument('-i', '--json_file', help='Path/Name to the amass JSON file.', required=True)
    parser.add_argument('-o', '--output_file', help='Path/Name of the output file.',  required=True)
    parser.add_argument('-f', '--output_format', help='Accepts: csv or xlsx', required=True)
    # Parse arguments
    args = parser.parse_args()
    # Input validation
    if not pathlib.Path(args.json_file).exists():
        print(f"The OWASP amass JSON files does not exist.")
        sys.exit()
    else:
        # Load OWASP amass JSON file.
        with open(args.json_file, 'r') as json_file:
            amass_json = json.load(json_file)

    accepted_strings = {'csv', 'CSV', 'xlsx', 'XLSX'}
    if args.output_format not in accepted_strings:
        print(f"[Error] '--output_format' accepts csv or xlsx")
        sys.exit()

    # LIST helper to accumulate results from json_file
    results_list = []

    # The top structure is a dictionary with two lists: "events", "domains". { "events": [...], "domains": [...] }
    # Iterate over the "domains" which is a list of dictionaries, that can contain one or multiple domains.
    # Create a dictionary to store the information.
    result_row = {
        "domains": numpy.nan,
        "total": numpy.nan,
        "name": numpy.nan,
        "domain": numpy.nan,
        "ip": numpy.nan,
        "cidr": numpy.nan,
        "asn": numpy.nan,
        "desc": numpy.nan,
        "tag": numpy.nan,
        "sources": numpy.nan
    }
    # Create the iterators. There is probably a more pythonic way.
    for1, for2, for3 = 0, 0, 0
    # Iterate over the JSON structure.
    for domains in amass_json['domains']:
        for1 += 1
        # domains : <class 'dict'>
        result_row['domains'] = domains['domain']
        result_row['total'] = domains['total']
        for key_domains in domains['names']:
            for2 += 1
            # names : <class 'list'>
            result_row['name'] = key_domains['name']
            result_row['domain'] = key_domains['domain']
            result_row['tag'] = key_domains['tag']
            result_row['sources'] = ', '.join(map(str, key_domains['sources']))
            for key_items in key_domains['addresses']:
                for3 += 1
                # <class 'list'> : key_items
                result_row['ip'] = key_items['ip']
                result_row['cidr'] = key_items['cidr']
                result_row['asn'] = key_items['asn']
                result_row['desc'] = key_items['desc']
            # Create a copy of the result_row dictionary to avoid overwriting it in every iteration.
            result_append = result_row.copy()
            results_list.append(result_append)

    # Print some summary information.
    print(f"Number of domains processed: {for1}")
    print(f"Number of subdomains processed: {for2}")
    print(f"Number of IPs processed: {for3}")

    # Create a Pandas Dataframe to store the results.
    amass_df = pandas.DataFrame(results_list, columns=['domains', 'total', 'name', 'domain', 'ip', 'cidr', 'asn', 'desc', 'tag', 'sources'])

    # Save the results
    if args.output_format == 'xlsx':
        with pandas.ExcelWriter(args.output_file) as writer:
            amass_df.to_excel(writer, sheet_name='output', engine='xlsxwriter', index=False)
    elif args.output_format == 'csv':
        amass_df.to_csv(args.output_file, index=False)

# amass-json-converter

**About the script**

A Python script to convert an OWASP Amass (v3.15.2) JSON file into other formats like CSV, XLS or XLSX.

```
usage: amass-json-to-excel.py [-h] -i JSON_FILE -o OUTPUT_FILE -f OUTPUT_FORMAT

Converts AMASS (v3.15.2) json files into other formats.

options:
  -h, --help            show this help message and exit
  -i JSON_FILE, --json_file JSON_FILE
                        Path/Name to the Amass JSON file.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path/Name of the output file.
  -f OUTPUT_FORMAT, --output_format OUTPUT_FORMAT
                        Accepts: csv, xls, xlsx

```

**About OWASP Amass Project**

The [OWASP Amass Project](https://github.com/OWASP/Amass) performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques. 

OWASP Amass allows to save the results in json format:
```
# amass db -d domain1,domain2 -json file.json

Usage: amass db [options]
  -d value
        Domain names separated by commas (can be used multiple times)
  -json string
        Path to the JSON output file
```

**About the Amass JSON files**

Example of an amass JSON output where the structure contains:
```
- "lists" -> mylist = ["apple", "banana", "cherry"]
- "dictionaries" -> thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964}
    {
        "events":  
            {
                "uuid": "************",
                "start": "10/23 14:15:57 2021 UTC",
                "finish": "10/23 15:27:16 2021 UTC"
            }
        ],
        "domains": [
            {
                "domain": "blablabla.com",
                "total": 10,
                "names": [
                    {
                        "name": "route.blabla.com",
                        "domain": "blabla.com",
                        "addresses": [
                            {
                                "ip": "123.45.5.67",
                                "cidr": "123.45.0.0/16",
                                "asn": 1212,
                                "desc": "BLABLA"
                            }
                        ],
                        "tag": "cert",
                        "sources": [
                            "CertSpotter",
                            "AlienVault",
                            "ThreatCrowd",
                            "Bing",
                            "Crtsh"
                       ]
                    }
                ]
            },
            {
                "domain": "as1212.net",
                "total": 30,
                "names": [
                    {
                        "name": "api.route.as1212.net",
                        "domain": "as1212.net",
                        "addresses": [
                            {
                                "ip": "123.46.5.88",
                                "cidr": "123.46.0.0/17",
                                "asn": 1212,
                                "desc": "BLABLA"
                            }
                        ],
                        "tag": "dns",
                        "sources": [
                            "Alterations",
                            "Sublist3rAPI",
                            "Reverse DNS"
                        ]
                    }
                ]
            }
        ]
    }
```



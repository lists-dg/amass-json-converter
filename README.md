# amass-json-converter

A Python script to convert an OWASP Amass JSON file into other formats like CSV, XLS or XLSX.

The [OWASP Amass Project](https://github.com/OWASP/Amass) performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques. Check 

Example of an amass JSON output as for 31.10.2021. The structure contains:
- "lists" -> mylist = ["apple", "banana", "cherry"]
- "dictionaries" -> thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964}

```
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

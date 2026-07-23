import dns.resolver


class DNSLookup:
    def __init__(self):
        self.output = {}

    def lookup(self, domain, record_type):
        try:
            if(domain not in self.output):
                self.output[domain] = {}

            if(record_type not in self.output[domain]):
                self.output[domain][record_type] = []

            answers = dns.resolver.resolve(domain, record_type)

            for ans in answers:
                self.output[domain][record_type].append(str(ans))

            return self.output
        
        except Exception as e:
            return {"Error" : str(e)}

    def print_output(self):
        for domain, records in self.output.items():
            print(f"\nDomain: {domain}")

            for record_type, values in records.items():
                print(f"  {record_type}:")

                if isinstance(values, list):
                    for value in values:
                        print(f"    - {value}")
                else:
                    print(f"    {values}")
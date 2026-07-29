import dns.resolver
from rich.table import Table


class DNSLookup:
    def __init__(self):
        self.output = {}
        self.table = Table(title="DNS Lookup")
        self.table.add_column("Domain", style="cyan", no_wrap=True)
        self.table.add_column("Record Type", style="magenta")
        self.table.add_column("Value", style="green")
        self.table.add_column("Error", style="red")

    def lookup(self, domain, record_type):
        try:
            if(domain not in self.output):
                self.output[domain] = {}

            if(record_type not in self.output[domain]):
                self.output[domain][record_type] = []

            answers = dns.resolver.resolve(domain, record_type)

            for ans in answers:
                self.output[domain][record_type].append(str(ans))

            self.table.add_row(domain, record_type, ", ".join(self.output[domain][record_type]), "")
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
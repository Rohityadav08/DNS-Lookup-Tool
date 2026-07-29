from modules.dns_lookup import DNSLookup
from modules.reverse_lookup import ReverseLookup
from modules.response_time import DNSResponseTime
from modules.whois_lookup import WhoisLookup
from modules.dnssec import DNSSEC
from modules.export_json import Export

from rich.console import Console


class DNSTool:

    def __init__(self):
        self.dns_lookup = DNSLookup()
        self.reverse_lookup = ReverseLookup()
        self.response_time = DNSResponseTime()
        self.whois_lookup = WhoisLookup()
        self.dnssec = DNSSEC()
        self.exporter = Export()

    def menu(self):
        while True:
            print("\n===== DNS TOOL =====")
            print("1. DNS Lookup")
            print("2. Reverse DNS Lookup")
            print("3. DNS Response Time")
            print("4. WHOIS Lookup")
            print("5. DNSSEC Check")
            print("0. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":
                self.dns_lookup_menu()

            elif choice == "2":
                self.reverse_lookup_menu()

            elif choice == "3":
                self.response_time_menu()

            elif choice == "4":
                self.whois_lookup_menu()

            elif choice == "5":
                self.dnssec_menu()

            elif choice == "0":
                print("Good Bye!")
                break

            else:
                print("Invalid Choice")

    def _export_result(self, data, prefix, domain=None):
        filename = self.exporter.build_filename(prefix, domain)
        result = self.exporter.export_json(data, filename)

        if result.get("status") == "success":
            print(f"Exported to {result['file']}")
        else:
            print(f"Export failed: {result.get('message', 'Unknown error')}")

        return result

    def dns_lookup_menu(self):
        domain = input("Domain: ").strip()

        print("\nRecord Types")
        print("1. A")
        print("2. AAAA")
        print("3. MX")
        print("4. NS")
        print("5. TXT")
        print("6. CNAME")
        print("7. SOA")
        print("8. CAA")
        print("9. PTR")
        print("10. SRV")

        record_map = {
            "1": "A",
            "2": "AAAA",
            "3": "MX",
            "4": "NS",
            "5": "TXT",
            "6": "CNAME",
            "7": "SOA",
            "8": "CAA",
            "9": "PTR",
            "10": "SRV",
        }

        choice = input("Record Type: ").strip()

        if choice not in record_map:
            print("Invalid Record Type")
            return

        result = self.dns_lookup.lookup(domain, record_map[choice])

        self._export_result(result, "dns_lookup", domain)
        Console().print(self.dns_lookup.table, justify="center", style="bold green")

    def reverse_lookup_menu(self):
        ip = input("IP Address: ").strip()

        result = self.reverse_lookup.lookup(ip)

        self._export_result(result, "reverse_lookup", ip)
        Console().print(self.reverse_lookup.table, justify="center", style="bold green")

    def response_time_menu(self):
        domain = input("Domain: ").strip()

        print("\nRecord Types")
        print("1. A")
        print("2. AAAA")
        print("3. MX")
        print("4. NS")
        print("5. TXT")
        print("6. CNAME")
        print("7. SOA")
        print("8. CAA")
        print("9. PTR")
        print("10. SRV")

        record_map = {
            "1": "A",
            "2": "AAAA",
            "3": "MX",
            "4": "NS",
            "5": "TXT",
            "6": "CNAME",
            "7": "SOA",
            "8": "CAA",
            "9": "PTR",
            "10": "SRV",
        }

        choice = input("Record Type: ").strip()

        if choice not in record_map:
            print("Invalid Record Type")
            return

        result = self.response_time.measure(
            domain,
            record_map[choice]
        )

        self._export_result(result, "response_time", domain)
        Console().print(result, justify="center", style="bold green")

    def whois_lookup_menu(self):
        domain = input("Domain: ").strip()

        result = self.whois_lookup.lookup(domain)

        self._export_result(result, "whois_lookup", domain)
        Console().print(self.whois_lookup.table, justify="center", style="bold green")

    def dnssec_menu(self):
        domain = input("Domain: ").strip()

        result = self.dnssec.check(domain)

        self._export_result(result, "dnssec", domain)
        Console().print(self.dnssec.table, justify="center", style="bold green")


if __name__ == "__main__":
    app = DNSTool()
    app.menu()
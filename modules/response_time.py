import time
import dns.resolver
from rich.table import Table


class DNSResponseTime:
    def __init__(self):
        self.table = Table(title="DNS Response Time")
        self.table.add_column("Domain", style="cyan", no_wrap=True)
        self.table.add_column("Record Type", style="magenta")
        self.table.add_column("Response Time (ms)", style="green")
        self.table.add_column("Records", style="blue")

    def measure(self, domain, record_type="A"):
        try:
            resolver = self._create_resolver()
            start_time = time.perf_counter()

            answers = self._query(resolver, domain, record_type)

            end_time = time.perf_counter()

            self.table.add_row(domain, record_type, str(self._calculate_time(start_time, end_time)), ", ".join([str(ans) for ans in answers]))

            return self.table

        except Exception as e:
            return self._handle_error(e)

    def _create_resolver(self):
        return dns.resolver.Resolver()

    def _query(self, resolver, domain, record_type):
        return resolver.resolve(domain, record_type)

    def _calculate_time(self, start_time, end_time):
        return round((end_time - start_time) * 1000, 2)

    def _handle_error(self, error):
        return {
            "error": str(error)
        }
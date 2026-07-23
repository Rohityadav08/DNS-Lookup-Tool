import time
import dns.resolver


class DNSResponseTime:
    def measure(self, domain, record_type="A"):
        try:
            resolver = self._create_resolver()
            start_time = time.perf_counter()

            answers = self._query(resolver, domain, record_type)

            end_time = time.perf_counter()

            return {
                "domain": domain,
                "record_type": record_type,
                "response_time_ms": self._calculate_time(start_time, end_time),
                "records": [str(ans) for ans in answers]
            }

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
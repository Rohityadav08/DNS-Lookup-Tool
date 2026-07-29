import dns.resolver
from rich.table import Table


class DNSSEC:

    def __init__(self):
        self.table = Table(title="DNSSEC Check")
        self.table.add_column("Domain", style="cyan", no_wrap=True)
        self.table.add_column("Enabled", style="green")
        self.table.add_column("DNSKEY", style="magenta")
        self.table.add_column("DS", style="blue")
        self.table.add_column("RRSIG", style="yellow")

    def check(self, domain):
        try:
            dnskey = self._query_dnskey(domain)
            ds = self._query_ds(domain)
            rrsig = self._query_rrsig(domain)
            enabled = bool(dnskey and ds and rrsig)

            self.table.add_row(
                domain,
                "Yes" if enabled else "No",
                "\n".join(dnskey) if dnskey else "Not found",
                "\n".join(ds) if ds else "Not found",
                "\n".join(rrsig) if rrsig else "Not found",
            )

            return {
                "domain": domain,
                "dnssec_enabled": enabled,
                "DNSKEY": dnskey,
                "DS": ds,
                "RRSIG": rrsig,
            }

        except Exception as e:
            self.table.add_row(domain, "Error", "", "", f"Error: {str(e)}")
            return self._handle_error(e)

    def _query_dnskey(self, domain):
        try:
            answers = dns.resolver.resolve(domain, "DNSKEY")
            return [str(ans) for ans in answers]
        except Exception:
            return []

    def _query_ds(self, domain):
        try:
            answers = dns.resolver.resolve(domain, "DS")
            return [str(ans) for ans in answers]
        except Exception:
            return []

    def _query_rrsig(self, domain):
        try:
            answers = dns.resolver.resolve(domain, "RRSIG")
            return [str(ans) for ans in answers]
        except Exception:
            return []

    def _handle_error(self, error):
        return {
            "error": str(error)
        }
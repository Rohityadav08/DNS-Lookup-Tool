import dns.resolver


class DNSSEC:

    def check(self, domain):
        try:
            dnskey = self._query_dnskey(domain)
            ds = self._query_ds(domain)
            rrsig = self._query_rrsig(domain)

            return {
                "domain": domain,
                "dnssec_enabled": bool(dnskey and ds and rrsig),
                "DNSKEY": dnskey,
                "DS": ds,
                "RRSIG": rrsig,
            }

        except Exception as e:
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
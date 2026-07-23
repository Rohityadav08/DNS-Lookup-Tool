import whois


class WhoisLookup:

    def lookup(self, domain):
        try:
            data = whois.whois(domain)

            parsed = self._parse(data)

            return self._format(parsed)

        except Exception as e:
            return self._handle_error(e)

    def _parse(self, data):
        return {
            "domain_name": data.domain_name,
            "registrar": data.registrar,
            "creation_date": data.creation_date,
            "expiration_date": data.expiration_date,
            "updated_date": data.updated_date,
            "name_servers": data.name_servers,
            "status": data.status,
            "emails": data.emails,
        }

    def _format(self, data):
        return {
            "whois": data
        }

    def _handle_error(self, error):
        return {
            "error": str(error)
        }
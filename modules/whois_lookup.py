import whois
from datetime import date, datetime
from rich.table import Table


class WhoisLookup:

    def __init__(self):
        self.table = Table(title="Whois Lookup")
        self.table.add_column("Domain", style="cyan", no_wrap=True)
        self.table.add_column("Registrar", style="magenta")
        self.table.add_column("Creation Date", style="green")
        self.table.add_column("Expiration Date", style="blue")
        self.table.add_column("Updated Date", style="yellow")
        self.table.add_column("Name Servers", style="red")
        self.table.add_column("Status", style="purple")
        self.table.add_column("Emails", style="bright_magenta")

    def lookup(self, domain):
        try:
            data = whois.whois(domain)

            parsed = self._parse(data)

            self.table.add_row(
                parsed.get("domain_name", ""),
                parsed.get("registrar", ""),
                parsed.get("creation_date", ""),
                parsed.get("expiration_date", ""),
                parsed.get("updated_date", ""),
                parsed.get("name_servers", ""),
                parsed.get("status", ""),
                parsed.get("emails", "")
            )
            return self._format(parsed)

        except Exception as e:
            self.table.add_row(domain, "", "", "", "", "", "", f"Error: {str(e)}")
            return self._handle_error(e)

    def _parse(self, data):
        return {
            "domain_name": self._stringify(data.domain_name),
            "registrar": self._stringify(data.registrar),
            "creation_date": self._stringify(data.creation_date),
            "expiration_date": self._stringify(data.expiration_date),
            "updated_date": self._stringify(data.updated_date),
            "name_servers": self._stringify(data.name_servers),
            "status": self._stringify(data.status),
            "emails": self._stringify(data.emails),
        }

    def _stringify(self, value):
        if value is None:
            return ""
        if isinstance(value, (list, tuple, set)):
            return ", ".join(self._stringify(item) for item in value)
        if isinstance(value, (datetime, date)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return str(value)

    def _format(self, data):
        return {
            "whois": data
        }

    def _handle_error(self, error):
        return {
            "error": str(error)
        }
from dns import reversename
import dns

class ReverseLookup:
    def __init__(self):
        self.output = {}

    def lookup(self, ip):
        reverse_name = self._reverse_name(ip)
        if isinstance(reverse_name, dict):
            return reverse_name
        return self._resolve_ptr(reverse_name)

    def _reverse_name(self, ip):
        try:
            reverse_name = reversename.from_address(ip)
            return str(reverse_name)
        except Exception as e:
            return {"Error": str(e)}
    
    def _resolve_ptr(self, reverse_name):
        try:
            answers = dns.resolver.resolve(reverse_name, "PTR")
            return [str(ans) for ans in answers]
        except Exception as e:
            return {"Error": str(e)}
        
    def _handle_error(self):
        # Placeholder for error handling logic
        pass
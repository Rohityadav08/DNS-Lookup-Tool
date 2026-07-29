import json
import os
import re


class Export:

    def export_json(self, data, filename="result.json"):
        try:
            output_dir = self._create_output_directory()
            file_path = os.path.join(output_dir, filename)

            self._write_json(data, file_path)

            return {
                "status": "success",
                "file": file_path
            }

        except Exception as e:
            return self._handle_error(e)

    def build_filename(self, prefix, domain=None):
        safe_domain = re.sub(r"[^A-Za-z0-9._-]+", "_", domain or "result").strip("._")
        if not safe_domain:
            safe_domain = "result"
        return f"{prefix}_{safe_domain}.json"

    def _create_output_directory(self):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    def _write_json(self, data, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, default=str)

    def _handle_error(self, error):
        return {
            "status": "error",
            "message": str(error)
        }
import os
import json


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
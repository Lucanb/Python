import pandas as pd

class CSVValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_csv(self):
        self.data = pd.read_csv(self.file_path)

    def validate_rules(self, laws):
        validation = []

        for column, law in laws.items():
            if law.get("required", False):
                if self.data[column].isnull().any():
                    validation.append(f"values missing on column : {column}")

            type = law.get("type")
            if type:
                new_type = self.data[column].dtype
                if new_type != type:
                    validation.append(f"data type invalid on column : {column}. \n expected {type} not  {type}")

        return validation


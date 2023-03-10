import csv

class MySelectQuery:
    def __init__(self, csv_content):
        self.data = []
        self.column_names = []
        reader = csv.reader(csv_content.splitlines())
        for row_index, row in enumerate(reader):
            if row_index == 0:
                self.column_names = row
            else:
                self.data.append(dict(zip(self.column_names, row)))

    def where(self, column_name, criteria):
        result = []
        for row in self.data:
            if row[column_name] == criteria:
                result.append(",".join(str(v) for v in row.values()))
        return result

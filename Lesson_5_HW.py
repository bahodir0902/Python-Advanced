import json

class MyContextManager:
    def __init__(self, filename, mode, newline="/n"):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print("Error")
        return True


with MyContextManager("24_hour_forecast.json", "r") as file:
    content = json.load(file)[:24]
    lst = []
    for row in content:
        lst.append(dict(list(row.items())[:5]))


with MyContextManager("result.json", "w", newline="") as file:
        json.dump(lst, file, indent=2)

# fazer um método anterior que verifica o formato e lê o arquivo
# e depois faz o método import_data recebendo apenas a lista aberta
# e pra responder com o relatório
import json
import csv
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        content = Inventory.read_file(path)

        if (type == "simples"):
            return SimpleReport.generate(content)
        elif (type == "completo"):
            return CompleteReport.generate(content)

    @staticmethod
    def read_file(path: str):
        if (path.endswith('.json')):
            with open(path) as file:
                return json.load(file)
        if (path.endswith('.csv')):
            with open(path, encoding='utf-8') as file:
                csv_dict = list(csv.DictReader(
                  file, delimiter=",", quotechar='"'))
                return csv_dict
        if (path.endswith('.xml')):
            with open(path) as file:
                doc = xmltodict.parse(file.read())
                xml_dict = doc["dataset"]["record"]
                return xml_dict

# xml to dict

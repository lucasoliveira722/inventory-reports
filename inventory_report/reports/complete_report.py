from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        companies_names = []
        complete_report = ''

        # Pegar os nomes das empresas
        for item in list:
            companies_names.append(item["nome_da_empresa"])
        companies_counter = Counter(companies_names)

    # para cada um dos nomes na lista,
    # fazer um count e adicionar em um novo dict
        complete_report = simple_report + "\nProdutos estocados por empresa:\n"
        for company, quantity in companies_counter.items():
            complete_report += (f"- {company}: {quantity}\n")

        return complete_report

from datetime import date
from collections import Counter


class SimpleReport:

    # Recebe uma lista de dicionários, retorna uma string do formato:
    # Data de fabricação mais antiga: YYYY-MM-DD
    # Data de validade mais próxima: YYYY-MM-DD
    # Empresa com mais produtos: NOME DA EMPRESA

    @classmethod
    def generate(cls, list):
        companies_names = []
        oldest_fabrication_date = []
        closest_expiration_date = []
        # https://stackabuse.com/how-to-format-dates-in-python/
        # https://www.delftstack.com/howto/python/python-counter-most-common/
        today = date.today().strftime("%Y-%m-%d")
        for item in list:
            # primeiro: empresa com mais produtos
            companies_names.append(item["nome_da_empresa"])
            most_common_company = Counter(companies_names).most_common(1)[0][0]

            # segundo: data de fabricação
            oldest_fabrication_date.append(item["data_de_fabricacao"])

            # terceiro: data de validade
            if (item["data_de_validade"] >= today):
                closest_expiration_date.append(item["data_de_validade"])
        return (
            f"Data de fabricação mais antiga: {min(oldest_fabrication_date)}\n"
            f"Data de validade mais próxima: {min(closest_expiration_date)}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )

from inventory_report.inventory.product import Product
# https://www.w3schools.com/python/python_casting.asp


def test_relatorio_produto():
    produto_teste = Product(
        1,
        "celular",
        "Samsung",
        "24/11/1993",
        "24/11/2023",
        111,
        "longe da água",
    )

# https://www.pythontutorial.net/python-oop/python-__repr__/
    printed_report = repr(produto_teste)

    # id = str(produto_teste.id)
    # nome = str(produto_teste.nome_do_produto)
    # nome_empresa = str(produto_teste.nome_da_empresa)
    # data_fabricacao = str(produto_teste.data_de_fabricacao)
    # data_validade = str(produto_teste.data_de_validade)
    # serie = str(produto_teste.numero_de_serie)
    # isntrucoes = str(produto_teste.instrucoes_de_armazenamento)

    comparative_report = (
            "O produto celular"
            " fabricado em 24/11/1993"
            " por Samsung com validade"
            " até 24/11/2023"
            " precisa ser armazenado longe da água."
    )

    assert printed_report == comparative_report

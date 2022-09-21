from inventory_report.inventory.product import Product


def test_cria_produto():
    produto_teste = Product(
        1,
        "celular",
        "Samsung",
        "24/11/1993",
        "24/11/2023",
        111,
        "longe da água",
    )

    assert produto_teste.id == 1
    assert produto_teste.nome_do_produto == 'celular'
    assert produto_teste.nome_da_empresa == 'Samsung'
    assert produto_teste.data_de_fabricacao == '24/11/1993'
    assert produto_teste.data_de_validade == '24/11/2023'
    assert produto_teste.numero_de_serie == 111
    assert produto_teste.instrucoes_de_armazenamento == 'longe da água'

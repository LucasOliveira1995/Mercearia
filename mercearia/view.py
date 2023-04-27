import Controller
import os.path


def criaArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')


criaArquivos('categoria.txt', 'pessoas.txt', 'estoque.txt', 'fornecedor.txt', 'funcionario.txt', 'venda.txt')

if __name__ == '__main__':
    while True:
        print('==' * 24)
        local = int(input('Digite 1 para acessar Categorias \n'
                          'Digite 2 para acessar Estoque \n'
                          'Digite 3 para acessar Fornecedor \n'
                          'Digite 4 para acessar Cliente \n'
                          'Digite 5 para acessar Funcionários \n'
                          'Digite 6 para acessar Vendas\n'
                          'Digite 7 para ver os produtos mais vendidos \n'
                          'Digite 8 para finalizar o Programa \n'))

        if local == 1:
            cat = Controller.ControllerCategoria()

            while True:
                print('================== Categorias ==================')
                funcao = int(input('Digite 1 para Cadastrar uma Categoria \n'
                                   'Digite 2 para Remover uma Categoria \n'
                                   'Digite 3 para Alterar uma Categoria \n'
                                   'Digite 4 para Mostrar todas as Categorias \n'
                                   'Digite 5 para Voltar ao Menu Inicial \n'))

                if funcao == 1:
                    categoria = input('Digite a Categoria que deseja cadastrar: ')
                    cat.novaCategoria(categoria)

                elif funcao == 2:
                    categoria = input('Digite a Categoria que deseja remover: ')
                    cat.removerCategoria(categoria)

                elif funcao == 3:
                    categoria = input('Digite a Categoria que Deseja alterar: ')
                    novaCategoria = input('Digite a Nova Categoria: ')
                    cat.alterarCategoria(categoria, novaCategoria)

                elif funcao == 4:
                    cat.mostrarCategoria()

                else:
                    break

        if local == 2:
            est = Controller.ControllerEstoque()

            while True:
                print('================== Estoque ==================')
                funcao = int(input('Digite 1 para Cadastrar um produto no Estoque \n'
                                   'Digite 2 para Remover algum produto do Estoque \n'
                                   'Digite 3 para Alterar algum produto do Estoque \n'
                                   'Digite 4 para Mostrar os produtos do Estoque \n'
                                   'Digite 5 para voltar ao Menu Inicial \n'))

                if funcao == 1:
                    produto = input('Digite o nome do produto: ')
                    preco = input('Digite o preço do produto: ')
                    categoria = input('Digite a categoria do produto: ')
                    quantidade = input('Digite a quantidade que contém desse produto: ')

                    est.cadastraProduto(produto, preco, categoria, quantidade)

                elif funcao == 2:
                    produto = input('Digite o produto que deseja remover: ')

                    est.removerProduto(produto)

                elif funcao == 3:
                    produto = input('Digite o produto que deseja alterar: ')
                    novoProduto = input('Digite o novo produto: ')
                    novoPreco = input('Digite o preço do novo produto: ')
                    novaCategoria = input('Digite a categoria do novo produto: ')
                    novaQuantidade = input('Digite a quantidade do novo produto: ')

                    est.alterarProduto(produto, novoProduto, novoPreco, novaCategoria, novaQuantidade)

                elif funcao == 4:
                    est.mostrarEstoque()

                else:
                    break

        if local == 3:
            forn = Controller.ControllerFornecedor()

            while True:
                print('================== Fornecedores ==================')
                funcao = int(input('Digite 1 para Cadastrar um Fornecedor \n'
                                   'Digite 2 para Remover um Fornecedor \n'
                                   'Digite 3 para Alterar algum Fornecedor \n'
                                   'Digite 4 para Mostrar os Fornecedores \n'
                                   'Digite 5 para voltar ao Menu Inicial \n'))

                if funcao == 1:
                    fornecedor = input('Digite o nome do Fornecedor: ')
                    cnpj = input('Digite o CNPJ do Fornecedor: ')
                    telefone = input('Digite o telefone do Fornecedor: ')
                    categoria = input('Digite a categoria do Fornecedor: ')

                    forn.cadastraFornecedor(fornecedor, cnpj, telefone, categoria)

                elif funcao == 2:
                    fornecedor = input('Digite o Fornecedor que deseja remover: ')

                    forn.removerFornecedor(fornecedor)

                elif funcao == 3:
                    fornecedor = input('Digite o Fornecedor que deseja Alterar: ')
                    novoFornecedor = input('Digite o nome do Novo Fornecedor: ')
                    novoCnpj = input('Digite o novo CNPJ do Fornecedor: ')
                    novoTelefone = input('Digite o telefone do Fornecedor: ')
                    novaCategoria = input('Digite a Categoria do Novo Fornecedor: ')

                    forn.alteraFornecedor(fornecedor, novoFornecedor, novoCnpj, novoTelefone, novaCategoria)

                elif funcao == 4:
                    forn.mostrarFornecedores()

                else:
                    break

        if local == 4:

            cliente = Controller.ControllerCliente()

            while True:
                print('================== Clientes ==================')
                funcao = int(input('Digite 1 para Cadastrar um Cliente \n'
                                   'Digite 2 para Remover um Cliente \n'
                                   'Digite 3 para Alterar algum Cliente \n'
                                   'Digite 4 para Mostrar os Clientes \n'
                                   'Digite 5 para voltar ao Menu Inicial \n'))

                if funcao == 1:
                    nome = input('Digite o nome do cliente: ')
                    telefone = input('Digite o telefone do cliente: ')
                    cpf = input('Digite o CPF do cliente: ')
                    email = input('Digite o email do cliente: ')
                    endereco = input('Digite o endereço do cliente: ')

                    cliente.cadastraCliente(nome, telefone, cpf, email, endereco)

                elif funcao == 2:
                    nome = input('Digite o nome do cliente que deseja remover: ')

                    cliente.removeCliente(nome)

                elif funcao == 3:
                    nome = input('Digite o nome do cliente que deseja alterar: ')
                    novoNome = input('Digite o nome do novo cliente: ')
                    telefone = input('Digite o novo telefone do cliente: ')
                    cpf = input('Digite o novo CPF fo cliente: ')
                    email = input('Digite o novo email do cliente: ')
                    endereco = input('Digite o novo endereço do cliente: ')

                    cliente.alterarCliente(nome, novoNome, telefone, cpf, email, endereco)

                elif funcao == 4:
                    cliente.mostarCliente()

                else:
                    break

        if local == 5:

            cliente = Controller.ControllerFuncionario()

            while True:
                print('================== Funcionários ==================')
                funcao = int(input('Digite 1 para Cadastrar um Funcionário \n'
                                   'Digite 2 para Remover um Funcionário \n'
                                   'Digite 3 para Alterar algum Funcionário \n'
                                   'Digite 4 para Mostrar os Funcionários \n'
                                   'Digite 5 para voltar ao Menu Inicial \n'))

                if funcao == 1:
                    nome = input('Digite o nome do funcionário: ')
                    telefone = input('Digite o telefone do funcionário: ')
                    cpf = input('Digite o CPF do funcionário: ')
                    email = input('Digite o email do funcionário: ')
                    endereco = input('Digite o endereço do funcionario: ')
                    clt = input('Digite o numero da CLT do funcionário: ')

                    cliente.cadastraFuncionario(clt, nome, telefone, cpf, email, endereco)

                elif funcao == 2:
                    nome = input('Digite o nome do funcionário que deseja remover: ')

                    cliente.removerFuncionario(nome)

                elif funcao == 3:
                    nome = input('Digite o nome do funcionário que deseja alterar: ')
                    novoNome = input('Digite o nome do novo funcionário: ')
                    telefone = input('Digite o novo telefone do funcionário: ')
                    cpf = input('Digite o novo CPF fo funcionário: ')
                    email = input('Digite o novo email do funcionário: ')
                    endereco = input('Digite o novo endereço do funcionário: ')
                    clt = input('Digite a nova CLT do funcionário: ')

                    cliente.alterarFuncionario(nome, novoNome, telefone, cpf, email, endereco, clt)

                elif funcao == 4:
                    cliente.mostrarFuncionario()

                else:
                    break

        if local == 6:

            venda = Controller.ControllerVenda()

            while True:
                print('================== Vendas ==================')
                funcao = int(input('Digite 1 para realizar uma venda \n'
                                   'Digite 2 para vizualizar as vendas \n'
                                   'Digite 3 para Voltar ao Menu Inicial \n'))

                if funcao == 1:
                    produto = input('Digite o nome do Produto que deseja vender: ')
                    vendedor = input('Digite o nome do Vendedor: ')
                    cliente = input('Digite o nome do cliente: ')
                    quantidade = int(input('Digite a Quantidade Vendida: '))

                    venda.cadastraVenda(produto, vendedor, cliente, quantidade)

                elif funcao == 2:
                    dataInicio = input('Digite a data de Inicio (dd/mm/aaaa): ')
                    dataTermino = input('Digite a Data de Termino (dd/mm/aaaa): ')

                    venda.mostarVenda(dataInicio, dataTermino)

                else:
                    break

        if local == 7:

            venda = Controller.ControllerVenda()

            venda.relatorioVendas()

        else:
            break

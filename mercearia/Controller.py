from Dao import *
from Models import *
from datetime import datetime


class ControllerCategoria:

    def novaCategoria(self, novaCategoria):

        existe = False

        x = DaoCategoria.ler()

        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print(f'A Categoria {novaCategoria} foi cadastrada com sucesso!')
        else:
            print(f'A Categoria {novaCategoria} já existe!')

    def removerCategoria(self, categoriaRemover):

        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print(f'A Categoria {categoriaRemover} não existe no Banco de Dados!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print(f'A Categoria {categoriaRemover} foi removida com sucesso!')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, 'Sem Categoria'), x.quantidade) if (x.produto.categoria == categoriaRemover) else(x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):

        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))

            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if (x.categoria == categoriaAlterar) else (x), x))
                print(f'A categoria {categoriaAlterar} foi alterada para {categoriaAlterada} com sucesso!')

            else:
                print(f'A Categoria {categoriaAlterada} já existe em nosso Banco de Dados!')

        else:
            print(f'A Categoria {categoriaAlterar} não foi encontrada em nosso Banco de Dados!')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) if (
                    x.produto.categoria == categoriaAlterar) else (x), estoque))

        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' + i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def mostrarCategoria(self):

        categorias = DaoCategoria.ler()

        if len(categorias) > 0:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

        else:
            print('A lista de Categorias está vazia!')


class ControllerEstoque:

    def cadastraProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(cat) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'O Produto {nome} foi cadastrado com sucesso!')
            else:
                print(f'O Produto {nome}, já existe no Estoque!')
        else:
            print(f'A Categoria {categoria} não existe no Estoque!')

    def removerProduto(self, nome):

        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print(f'O Produto {nome} foi removido com sucesso!')
        else:
            print(f'O Produto {nome} não existe no Estoque!')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                           i.produto.categoria + '|' + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):

        x = DaoCategoria.ler()
        y = DaoEstoque.ler()
        cat = list(filter(lambda x: x.categoria == novaCategoria, x))

        if len(cat) > 0:
            nome = list(filter(lambda x: x.produto.nome == nomeAlterar, y))
            if len(nome) > 0:
                x = list(filter(lambda x: x.produto.nome == novoNome, y))
                if len(x) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if (x.produto.nome == nomeAlterar) else (x), y))
                    print(f'O Produto {nomeAlterar} foi alterado para {novoNome} com sucesso!')
                else:
                    print(f'O Produto {novoNome} já existe no Estoque!')
            else:
                print(f'O Produto {nomeAlterar} não existe no Estoque!')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' + i.produto.preco + '|' +
                                   i.produto.categoria + '|' + str(i.quantidade))
                    arq.writelines('\n')

        else:
            print(f'A Categoria {novaCategoria} não existe no Estoque!')

    def mostrarEstoque(self):

        x = DaoEstoque.ler()
        if len(x) > 0:
            print('==/==' * 5)
            for i in x:
                print(f'Nome: {i.produto.nome} \n'
                      f'Preço: {i.produto.preco} \n'
                      f'Categoria: {i.produto.categoria} \n'
                      f'Quantidade: {i.quantidade} \n')
                print('==/==' * 5)
        else:
            print('O Estoque esta Vazio!')


class ControllerVenda:

    def cadastraVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):

        estoque = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in estoque:
            if existe == False:
                if nomeProduto == i.produto.nome:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(i.produto.preco) * int(quantidadeVendida)

                        DaoVenda.salvar(vendido)
            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' + i[0].preco + '|' + i[0].categoria + '|' + str(i[1]))
                arq.writelines('\n')

        if existe == False:
            print(f'Não temos o Produto {nomeProduto}, no Estoque!')
            return None
        elif not quantidade:
            print(f'Não temos {quantidadeVendida} {nomeProduto}(s) em Estoque!')
            return None
        else:
            print('Venda concluida com sucesso!')
            return valorCompra

    def relatorioVendas(self):

        vendas = DaoVenda.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))

            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else (x), produtos))

            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key= lambda k: k['quantidade'], reverse= True)

        print('Esses são os Itens mais vendidos!')

        a = 1
        for i in ordenado:
            print(f'==========Produto [{a}]==========')
            print(f'Produto: {i["produto"]}\n'
                  f'Quantidade: {i["quantidade"]}\n')
            a += 1

    def mostarVenda(self, dataInicio, dataTermino):

        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1
                                                   and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f'== == == == == Venda[{cont}] == == == == ==')
            print(f'Nome: {i.itensVendidos.nome}\n'
                  f'Categoria: {i.itensVendidos.categoria}\n'
                  f'Data: {i.data}\n'
                  f'quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: {i.comprador}\n'
                  f'Vendedor: {i.vendedor}\n')

            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f'Total Vendido: R$ {total},00')


class ControllerFornecedor:

    def cadastraFornecedor(self, nome, cnpj, telefone, categoria):

        x = DaoFornecedor.ler()

        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(listaCnpj) > 0:
            print('O CNPJ já está cadastrado como nosso fornecedor!')

        elif len(listaTelefone) > 0:
            print('Telefone já cadastrado como Fornecedor!')

        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso!')

            else:
                print('Digite um Telefone e um CNPJ validos!')

    def alteraFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):

        x = DaoFornecedor.ler()
        nomes = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(nomes) > 0:
            listaCnpj = list(filter(lambda x: x.cnpj == novoCnpj, x))

            if len(listaCnpj) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if (x.nome == nomeAlterar) else (x), x))
                print('Fornecedor Alterado com Sucesso!')

            else:
                print('O CNPJ informado já existe em nossa Base de Dados!')

        else:
            print('O fornecedor informado NÃO existe!')

        with open('fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                arq.writelines('\n')

    def removerFornecedor(self, nome):

        x = DaoFornecedor.ler()

        listaNome = list(filter(lambda x: x.nome == nome, x))

        if len(listaNome) > 0:
            for i in range(len(listaNome)):
                if x[i].nome == nome:
                    del x[i]
                    break
            print(f'O fornecedor {nome} foi removido com sucesso!')
        else:
            print(f'O fornecedor {nome} não existe em nossa Base de Dados!')
            return None

        with open('fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.cnpj + '|' + i.telefone + '|' + i.categoria)
                arq.writelines('\n')

    def mostrarFornecedores(self):

        x = DaoFornecedor.ler()

        if len(x) == 0:
            print('Sua Base de Fornecedores está vazia!')

        cont = 1
        for i in x:
            print(f'========= Fornecedor {cont} =========')
            print(f'Nome: {i.nome}\n'
                  f'CNPJ: {i.cnpj}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Categoria: {i.categoria}\n')
            cont += 1


class ControllerCliente:

    def cadastraCliente(self, nome, telefone, cpf, email, endereco):

        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(listaCpf) > 0:
            print('Este CPF já existe em nossa Base de Dados!')

        else:
            if len(cpf) == 11 and 10 <= len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente Cadastado com sucesso!')

            else:
                print('Digite um CPF e um Telefona VÁLIDOS!')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):

        x = DaoPessoa.ler()
        listaNome = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(listaNome) > 0:
            listaCpf = list(filter(lambda x: x.cpf == novoCpf, x))

            if len(listaCpf) == 0:
                x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else (x), x))
                print('Cliente Alterado com sucesso!')

            else:
                print('Este CPF já está cadastrado no nosso sistema, tente outro!')

        else:
            print(f'O cliente {novoNome}, já está cadastrado em nosso sistema!')

        with open('pessoas.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')

    def removeCliente(self, nome):

        x = DaoPessoa.ler()

        listaNome = list(filter(lambda x: x.nome == nome, x))

        if len(listaNome) > 0:
            for i in range(len(listaNome)):
                if x[i].nome == nome:
                    del x[i]
                    break
            print(f'O cliente {nome} foi removido com sucesso!')

        else:
            print(f'O Cliente {nome}, não foi encontrado em nosso sistema!')
            return None

        with open('pessoas.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco)
                arq.writelines('\n')

    def mostarCliente(self):

        x = DaoPessoa.ler()

        if len(x) == 0:
            print('Sua Base de Clientes está vazia!')

        cont = 1
        for i in x:
            print(f'========= Cliente {cont} =========')
            print(f'Nome: {i.nome}\n'
                  f'CPF: {i.cpf}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Email: {i.email}\n'
                  f'Endereço: {i.endereco}')
            cont += 1


class ControllerFuncionario:

    def cadastraFuncionario(self, clt, nome, telefone, cpf, email, endereco):

        x = DaoFuncionario.ler()
        listaCpf = list(filter(lambda x: x.nome == nome, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))

        if len(listaCpf) == 0:
            if len(listaClt) == 0:
                if len(cpf) == 11 and 10 <= len(telefone) <= 11:
                    DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                    print(f'Funcionario {nome} cadastrado com sucesso!')
                else:
                    print('Digite um telefone e um Cpf Valido!')
            else:
                print('CLT já cadastrada em nosso sistema!')
        else:
            print(f'O Funcionário {nome} já consta em nosso sistema!')

    def alterarFuncionario(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco, novaClt):

        x = DaoFuncionario.ler()
        listaNome = list(filter(lambda x: x.nome == nomeAlterar, x))

        if len(listaNome) > 0:
            listaCpf = list(filter(lambda x: x.cpf == novoCpf, x))

            if len(listaCpf) == 0:
                x = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else (x), x))
                print('Funcionário alterado com sucesso!')
            else:
                print('Este CPF já está cadastrado em nosso sistema!')
        else:
            print(f'O funcionário {nomeAlterar} não foi encontrado em nosso sistema!')

        with open('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '|' + i.clt)
                arq.writelines('\n')

    def removerFuncionario(self, nome):

        x = DaoFuncionario.ler()
        listaNomes = list(filter(lambda x: x.nome == nome, x))

        if len(listaNomes) > 0:
            for i in range(len(listaNomes)):
                if x[i].nome == nome:
                    del x[i]
                    break
            print('Funcionário Removido com sucesso!')
        else:
            print(f'O Funcionário {nome} não foi encontrado no nosso sistema!')
            return None

        with open('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + '|' + i.telefone + '|' + i.cpf + '|' + i.email + '|' + i.endereco + '|' + i.clt)
                arq.writelines('\n')

    def mostrarFuncionario(self):

        x = DaoFuncionario.ler()

        if len(x) == 0:
            print('Sua Base de Funcionários está vazia!')

        cont = 1
        for i in x:
            print(f'========= Funcionário {cont} =========')
            print(f'Nome: {i.nome}\n'
                  f'CPF: {i.cpf}\n'
                  f'Telefone: {i.telefone}\n'
                  f'Email: {i.email}\n'
                  f'Endereço: {i.endereco}\n'
                  f'Clt: {i.clt}')
            cont += 1

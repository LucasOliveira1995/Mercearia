from Models import *


class DaoCategoria:

    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat


class DaoVenda:

    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + '|' + venda.itensVendidos.preco + '|' +
                           venda.itensVendidos.categoria + '|' + venda.vendedor + '|' + venda.comprador + '|' +
                           str(venda.quantidadeVendida) + '|' + str(venda.data))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5]))
        return vend


class DaoEstoque:

    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' + produto.preco + '|' +
                           produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), int(i[3])))
        return est


class DaoFornecedor:

    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + '|' + fornecedor.cnpj + '|' +
                           fornecedor.telefone + '|' + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn


class DaoPessoa:

    @classmethod
    def salvar(cls, pessoas: Pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.writelines(pessoas.nome + '|' + pessoas.telefone + '|' + pessoas.cpf + '|' +
                           pessoas.email + '|' + pessoas.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            cls.pessoas = arq.readlines()

        cls.pessoas = list(map(lambda x: x.replace('\n', ''), cls.pessoas))
        cls.pessoas = list(map(lambda x: x.split('|'), cls.pessoas))

        pess = []
        for i in cls.pessoas:
            pess.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        return pess


class DaoFuncionario:

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.nome + '|' + funcionario.telefone + '|' + funcionario.cpf + '|' +
                           funcionario.email + '|' + funcionario.endereco + '|' + funcionario.clt)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[5], i[0], i[1], i[2], i[3], i[4]))
        return func

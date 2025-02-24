class Atendimentos:
    def __init__(self, data, tempo, descricao, preco):
        self.data = data
        self.tempo = tempo
        self.descricao = descricao
        self.preco = preco

class Fisioterapia(Atendimentos):
    def alterarData(self, alterar):
        self.data = alterar
    
    def alterarPreco(self, alterar):
        self.preco = alterar

    def alterarTempo(self, alterar):
        self.tempo = alterar

    def alterarDescricao(self, alterar):
        self.descricao = alterar

class Depilacao(Fisioterapia):
    pass
    
class Botox(Fisioterapia):
    pass
    
class FormaPagamento:
    def __init__(self, metodo):
        self.metodo = metodo

    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor:.2f} via {self.metodo}...")

class Cartao(FormaPagamento):
    def __init__(self, titular, numero, cvc, validade, senha):
        super().__init__("Cartão")
        self.titular = titular
        self.numero = numero
        self.cvc = cvc
        self.validade = validade
        self.senha = senha

    def pagamento_cartao(self, valor):
        option = input("Deseja pagar em Crédito ou Débito? (C/D): ").upper()
        if option in ['C', 'D']:
            print(f"Pagamento de R${valor:.2f} aprovado no {'Crédito' if option == 'C' else 'Débito'}.")
        else:
            print("Opção inválida! Tente novamente.")

class Pix(FormaPagamento):
    def __init__(self, chave):
        super().__init__("Pix")
        self.chave = chave

    def pagamento_pix(self, valor):
        print(f"Pagamento de R${valor:.2f} enviado para a chave {self.chave} via Pix.")

#Colocaremos em "self.chave" a chave pix da minha Tia.

class Usuario:
    def __init__(self, telefone, name, email, senha, endereco):
        self.telefone = telefone
        self.name = name
        self.email = email
        self._senha = senha
        self.endereco = endereco

    def exibir_infos(self):
        return f"{self.name}, seu email é: {self.email}, seu telefone é {self.telefone} e seu endereço é {self.endereco}"

    def alterar_nome(self, alterarInfo):
        if alterarInfo == self.name:
            return "Seu nome está igual ao anterior, insira um diferente."
        
        if alterarInfo.isalpha():
            self.name = alterarInfo
            return "Seu nome foi alterado com sucesso!"
        else:
            return "Seu nome não pode conter números, insira novamente."

    def alterar_email(self, alterarInfo):
        if alterarInfo == self.email:
            return "Seu email está igual ao anterior, insira um diferente."
        else: 
            self.email = alterarInfo
            return "Seu email foi modificado!"

    def alterar_senha(self, alterarInfo):
        if alterarInfo == self._senha:
            return "Sua senha está igual à anterior, insira uma diferente."
        else: 
            self._senha = alterarInfo
            return "Sua senha foi alterada com sucesso!"
             
    def alterar_telefone(self, alterarInfo):
        if alterarInfo == self.telefone:
            return "Seu telefone está igual ao anterior, insira um diferente."
        else:
            self.telefone = alterarInfo
            return "Seu número de telefone foi alterado com sucesso!"

    def alterar_endereco(self, alterarInfo):
        if alterarInfo == self.endereco:
            return "Seu endereço está igual ao anterior, insira um diferente."
        else:
            self.endereco = alterarInfo
            return "Seu endereço foi alterado com sucesso!"


if __name__ == "__main__":
    usuario = Usuario("9999999", "José", "josé@email.com", "senha123", "Rua A, 123")
    print(usuario.exibir_infos())
    
#teste para cartao
    pagamento = Cartao("João", "99999999999", "123", "12/26", "1234")
    pagamento.pagamento_cartao(150.75)

#teste para pix
    pix = Pix("JOVELINA")
    pix.pagamento_pix(50.00)
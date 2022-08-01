class Personagem:
    def __init__(self):
        self.__nome = ''
        self.__cor_cabelo = ''
        self.__cor_pele = ''
        self.__classe = ''
        self.__idade = ''
        self.__altura = ''
        self.__habilidade = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cor_cabelo(self):
        return self.__cor_cabelo

    @cor_cabelo.setter
    def cor_cabelo(self, cor_cabelo):
        self.__cor_cabelo = str(cor_cabelo).title()

    @property
    def cor_pele(self):
        return self.__cor_pele

    @cor_pele.setter
    def cor_pele(self, cor_pele):
        self.__cor_pele = str(cor_pele).title()

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, classe):
        self.__classe = str(classe).title()

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = int(idade)

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = float(altura)

    @property
    def habilidade(self):
        return self.__habilidade

    @habilidade.setter
    def habilidade(self, habilidade):
        self.__habilidade = str(habilidade).title()

    def personagem_completo(self):
        personagem_completo = f'{self.nome} é {self.cor_pele}, tem cabelo {self.cor_cabelo}!\n' \
                              f'{self.nome} é {self.classe}, tem {self.altura} de altura e {self.idade} de idade.\n' \
                              f'{self.habilidade}'
        return personagem_completo


hulk = Personagem()
hulk.nome = 'Hulk'
hulk.cor_cabelo = 'Preto'
hulk.cor_pele = 'Verde'
hulk.classe = 'Mutante'
hulk.idade = 54
hulk.altura = 2.63
hulk.habilidade = 'Hulk esmaga! '
print(hulk.personagem_completo())

a = Personagem()
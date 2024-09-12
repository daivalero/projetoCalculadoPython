from operecao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0
        opera     = Operacao()

    def mostrarMenu(self):
        print('\n----- MENU -----\n\n'           +
              'Escolha umas das opções abaixo: ' +
              '\n0. Sair'                        +
              '\n1. Somar'                       +
              '\n2. Subtrair'                    +
              '\n3. Dividir'                     +
              '\n4. Multiplicar'                 +
              '\n5. Potencia'                    +
              '\n6. Raiz'                        +
              '\n7. Tabuada'                     +
              '\n8. Imprimir 10 numeros')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro numero'))
        self.num2 = int(input('Informe o segundo numero'))


    def operacao(self):


        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha uma das opções acima: '))

            if self.opcao == 0:
                self.coletar()  # Chamando o input
                print('Obrigado!')

            if self.opcao == 1:
                self.coletar() #Chamando o input
                print(f'A soma dos numeros é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()  # Chamando o input
                print(f'A subtração dos numeros é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()  # Chamando o input
                print(f'A divisão dos numeros é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()  # Chamando o input
                print(f'A multiplicação dos numeros é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                print(f'O resultado da potencia de {self.num1} é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()  # Chamando o input
                print(f'A raiz de {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()  # Chamando o input
                print(f'A tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'A tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:
                self.coletar()  # Chamando o input
                print(f'Os numeros imprimidos são:  {self.opera.imprimanum(self.num1)}')
                
            elif self.opcao == 9:
                print(self.opera.exercicio02())
            
            elif self.opcao == 9:
                print(self.opera.exercicio02())

            elif self.opcao == 10:
                print(f'A soma do número até 100 é:  {self.opera.exercicio03(self.num1)}')

            elif self.opcao == 11:
                print(f'Os múltiplos de 5:  {self.opera.exercicio04()}')

            elif self.opcao == 12:
                self.coletarr()
                print(f'O numero é:  {self.opera.exercicio05(self.num1)}')

            elif self.opcao == 13:
                self.coletarr()
                print(f'O número é:  {self.opera.exercicio06(self.num1)}')

            elif self.opcao == 14:
                self.coletarr()
                print(f'A tabuada do numero é:  {self.opera.exercicio07(self.num1)}')

            elif self.opcao == 15:
                self.coletarr()
                print(f'Os números são:  {self.opera.exercicio08(self.num1)}')









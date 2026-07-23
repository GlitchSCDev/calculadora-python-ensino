# Calculadora em Python

## Descrição

Este projeto é uma calculadora simples desenvolvida em Python que funciona através do terminal. Ela permite realizar operações matemáticas básicas e algumas operações extras por meio de um menu interativo.

## Funcionalidades

A calculadora possui as seguintes operações:

- Soma
- Subtração
- Multiplicação
- Divisão
- Potência
- Raiz Quadrada
- Porcentagem
- Resto da Divisão
- Divisão Inteira

## Requisitos

- Python 3.x instalado.

## Como executar

1. Salve o código em um arquivo chamado `calculadora.py`.
2. Abra o terminal na pasta onde o arquivo foi salvo.
3. Execute o comando:

```bash
python calculadora.py
```

Ou, dependendo da instalação do Python:

```bash
python3 calculadora.py
```

## Como usar

Ao iniciar o programa será exibido um menu como o exemplo abaixo:

```
===================================
      CALCULADORA PYTHON
===================================
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potência
6 - Raiz Quadrada
7 - Porcentagem
8 - Resto da Divisão
9 - Divisão Inteira
0 - Sair
===================================
```

Digite o número correspondente à operação desejada e pressione **Enter**.

### Exemplos

#### Soma

```
Escolha uma opção: 1
Primeiro número: 10
Segundo número: 5

Resultado: 15
```

#### Raiz Quadrada

```
Escolha uma opção: 6
Digite um número: 25

Resultado: 5.0
```

#### Porcentagem

```
Escolha uma opção: 7
Digite o valor: 250
Digite a porcentagem (%): 20

20.0% de 250.0 = 50.0
```

## Tratamento de erros

O programa possui algumas validações para evitar erros:

- Não permite divisão por zero.
- Não calcula raiz quadrada de números negativos.
- Exibe uma mensagem caso o usuário digite um valor que não seja numérico.
- Informa quando uma opção inválida é escolhida.

## Encerrando o programa

Para fechar a calculadora, escolha a opção:

```
0 - Sair
```

Será exibida a mensagem:

```
Calculadora encerrada.
```


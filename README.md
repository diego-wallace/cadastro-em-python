# Validação e Manipulação de Dados em Python

Projeto desenvolvido para praticar **lógica de programação, manipulação de strings, funções, listas e estruturas de repetição em Python**.

## 📌 Sobre o projeto

O programa solicita ao usuário seu **nome completo** e seu **e-mail**, realiza algumas validações e manipula os dados fornecidos antes de exibir uma mensagem de boas-vindas.

O objetivo principal é exercitar conceitos fundamentais da linguagem Python por meio de um pequeno sistema de validação de dados.

## ⚙️ Funcionamento

### 1. Validação e formatação do nome

Inicialmente, o programa solicita o nome completo do usuário.

Para que o usuário possa prosseguir, o nome precisa conter **pelo menos 3 letras**. Enquanto essa condição não for atendida, o programa solicita que o nome seja informado novamente.

Após a validação, o nome passa por algumas etapas de tratamento:

* Com a função `strip()`, remove os espaços desnecessários no início e no final da string;
* Com a função `title()`, capitaliza o nome completo;
* Com a função `split()`, separa cada palavra do nome em uma lista;
* Armazena o primeiro nome em uma variável para utilização posteriormente.

### 2. Validação do e-mail

Em seguida, o programa solicita o e-mail do usuário.

O e-mail é dividido em duas partes:

* **Prefixo:** parte localizada antes do `@`;
* **Sufixo:** parte localizada depois do `@`.

O programa verifica algumas condições:

* O prefixo não pode conter determinados caracteres especiais;
* O sufixo deve pertencer a uma lista de provedores permitidos:

  * `gmail`
  * `hotmail`
  * `yahoo`

Essa validação é realizada por meio de uma **função**, que retorna:

* `True` → quando todas as condições são atendidas;
* `False` → quando pelo menos uma das condições não é atendida.

### 3. Mensagem final

Caso o e-mail seja considerado válido, o programa utiliza o primeiro nome armazenado anteriormente para exibir uma **mensagem de boas-vindas**, juntamente com o e-mail.
Exemplo: "Olá, Pedro! Seu email: pedro@gmail.com foi registrado com sucesso!"

## 🧠 Conceitos praticados

Este projeto foi desenvolvido para exercitar os seguintes conceitos de Python:

* Variáveis
* Manipulação de strings
* Validação de dados
* Operadores e expressões lógicas
* Listas
* Funções
* Retorno de valores com `return`
* Valores booleanos (`True` e `False`)
* Estruturas condicionais (`if`, `else`)
* Estruturas de repetição (`while`)

* * `input()` e `print()`
* `strip()`
* `capitalize()`
* `split()`

## 🎯 Objetivo

O projeto faz parte dos meus exercícios de aprendizado em **Python e lógica de programação**, com foco em desenvolver uma base sólida para a criação de programas capazes de receber, validar e manipular dados fornecidos pelo usuário.

## 🛠️ Tecnologias utilizadas

* **Python 3** — linguagem utilizada no desenvolvimento do projeto.
* **VS Code** — editor de código utilizado para desenvolvimento e execução.
* **Git** — utilizado para versionamento do projeto.
* **GitHub** — utilizado para armazenamento e publicação do código.

## ▶️ Como executar o projeto

### Pré-requisitos

Antes de executar o projeto, certifique-se de ter o **Python 3** instalado em sua máquina.

### Execução

1. Clone este repositório:

```bash
git clone https://github.com/diego-wallace/cadastro-em-python.git
```

2. Acesse a pasta do projeto:

```bash
cd cadastro-em-python
```

3. Execute o arquivo Python:

```bash
python cadastro.py
```

> Dependendo do seu sistema operacional, pode ser necessário utilizar `python3` no lugar de `python`.

Após executar o programa, siga as instruções exibidas no terminal para informar seu nome e e-mail.

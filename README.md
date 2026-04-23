# 📘 Exercícios de Recursão em Python

Este repositório contém uma coleção de exercícios de **recursão** para prática de lógica de programação em Python.
Os problemas vão do nível básico ao intermediário, abordando diferentes formas de aplicar recursividade.

---

## ⚠️ Observação

Os arquivos `quest3.0.py`, `quest8.0.py` e `quest9.0.py` são exercícios extras com desafios adicionais.

---

## 🧠 Conceitos abordados

* Recursão
* Caso base
* Divisão de problemas
* Estruturas de dados (listas e grafos)
* Exploração de caminhos
* Backtracking (nível introdutório)

---

## 📌 Lista de Exercícios

---

### 1. 🔢 Fatorial de um número

**Enunciado:**
Crie uma função recursiva que receba um número inteiro não negativo `n` e retorne o fatorial de `n`.

**Regras:**

* `0! = 1`
* `n! = n × (n - 1)!`, para `n > 0`

**Exemplo:**

```bash
Entrada: 5
Saída: 120
```

---

### 2. ➕ Soma dos elementos de uma lista

**Enunciado:**
Crie uma função recursiva que receba uma lista de números e retorne a soma de todos os seus elementos, sem utilizar laços de repetição.

**Exemplo:**

```bash
Entrada: [4, 7, 2, 9]
Saída: 22
```

💡 **Dica:**
`soma(lista) = primeiro elemento + soma(restante)`

---

### 3. 🔽 Contagem regressiva recursiva

**Enunciado:**
Crie uma função recursiva que receba um número inteiro positivo `n` e imprima os valores de `n` até `0`.

**Exemplo:**

```bash
Entrada: 5
Saída:
5
4
3
2
1
0
```

🎯 **Desafio extra:**
Criar uma versão que imprime de `0` até `n` usando recursão.

---

### 4. ⚡ Potência de um número

**Enunciado:**
Crie uma função recursiva que calcule `base^expoente`, recebendo dois números inteiros.

**Regras:**

* Qualquer número elevado a `0` é `1`
* `base^expoente = base × base^(expoente - 1)`

**Exemplo:**

```bash
Entrada: base = 2, expoente = 4
Saída: 16
```

🎯 **Desafio extra:**
Tratar expoentes negativos.

---

### 5. 🔁 Inverter uma string

**Enunciado:**
Crie uma função recursiva que receba uma string e retorne essa string invertida.

**Exemplo:**

```bash
Entrada: "casa"
Saída: "asac"
```

💡 **Dicas:**

* Último caractere + inversão do restante
  ou
* Inversão da substring sem o primeiro caractere + primeiro caractere

---

### 6. 🔢 Sequência de Fibonacci

**Enunciado:**
Crie uma função recursiva que receba um número `n` e retorne o n-ésimo termo da sequência de Fibonacci.

**Regras:**

* `Fib(0) = 0`
* `Fib(1) = 1`
* `Fib(n) = Fib(n-1) + Fib(n-2)`, para `n ≥ 2`

**Exemplo:**

```bash
Entrada: 6
Saída: 8
```

---

### 7. 🏢 Exploração de salas (grafo)

**Enunciado:**
Simule a exploração de salas conectadas em um prédio inteligente.

Cada sala pode levar a outras salas. Crie uma função recursiva que visite todas as salas acessíveis a partir de uma sala inicial.

**Objetivo:**
Mostrar a ordem de visita.

**Exemplo conceitual:**

* Sala A → B, C
* Sala B → D
* Sala C → E

**Saída esperada:**

```bash
A, B, D, C, E
```

🎯 **Desafio extra:**
Evitar visitar a mesma sala mais de uma vez.

---

### 8. 🚁 Contagem de caminhos (grid)

**Enunciado:**
Um drone deve ir do canto superior esquerdo ao canto inferior direito de uma grade `n x m`, movendo-se apenas para **direita** ou **baixo**.

Crie uma função recursiva que calcule quantos caminhos diferentes existem.

**Exemplo:**

```bash
Entrada: grade 2x2
Saída: 2
```

**Caminhos possíveis:**

* Direita → Baixo
* Baixo → Direita

🎯 **Desafio extra:**
Adicionar obstáculos no caminho.

---

### 9. 🔐 Decodificação de strings

**Enunciado:**
Crie uma função recursiva que gere versões de uma string removendo um caractere por chamada, até restar apenas uma letra.

**Exemplo:**

```bash
Entrada: "abc"

Saída:
abc
bc
c
```

ou

```bash
abc
ab
a
```

🎯 **Desafio extra:**
Gerar todas as combinações possíveis de remoção.

---

### 10. 👥 Rede de recomendações

**Enunciado:**
Simule uma rede social acadêmica onde usuários indicam outros usuários.

Crie uma função recursiva que percorra todas as conexões a partir de um usuário inicial.

**Objetivo:**
Listar todos os usuários alcançáveis.

**Exemplo:**

* Renato → Ana, Bruno
* Ana → Carla
* Bruno → Diego

**Saída esperada:**

```bash
Renato, Ana, Carla, Bruno, Diego
```

🎯 **Desafio extra:**
Contar quantos usuários únicos foram visitados.

---

## ▶️ Como executar os exercícios

Certifique-se de ter o Python instalado:

```bash
python nome_do_arquivo.py
```

Exemplo:

```bash
python quest1.py
```

---

## 📁 Estrutura do projeto

```bash
quest1.py
quest2.py
quest3.0.py
...
quest10.py
README.md
```

---

## 🚀 Objetivo

Este projeto tem como objetivo fortalecer o entendimento de **recursão**, um dos conceitos mais importantes da programação, muito utilizado em algoritmos, estruturas de dados e problemas complexos.

---
👨‍💻 Autor

Gabriel Costa Lima

📚 Fonte dos exercícios

Exercícios propostos por Renato de Pierri (FATEC - Franco da Rocha)

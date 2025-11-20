# Projeto: Soluções para o Problema da Mochila 0/1 (Knapsack)

Este projeto apresenta quatro abordagens diferentes para resolver o clássico problema da *Mochila 0/1* (0/1 Knapsack Problem). Cada método possui características próprias, vantagens, desvantagens e complexidades distintas. Este repositório serve tanto para fins educacionais quanto para a comparação de eficiência entre abordagens.

### Integrantes
Mohamed Afif Smaili RM 554445  
Augusto Ferreira Rogel de Souza RM 557709 

---

## 📘 Descrição Geral do Problema

O *Problema da Mochila 0/1* consiste em selecionar um subconjunto de itens, cada um com um **valor** e um **custo (peso/horas)**, de modo a maximizar o valor total sem ultrapassar a capacidade disponível.

No contexto deste projeto, cada item representa um **projeto** com:

* **Nome**
* **Valor** (benefício)
* **Horas necessárias** (custo)

O objetivo é selecionar os melhores projetos que caibam dentro da capacidade de horas disponível.

---

## 🚀 Abordagens Implementadas

O arquivo principal contém quatro versões da solução:

### 1. **Estratégia Gulosa (Greedy)**

Seleciona os itens com melhor razão valor/hora.

* ✔️ Muito rápida
* ❌ Não garante solução ótima em 0/1 knapsack
* Complexidade: **O(n log n)**

---

### 2. **Recursão Pura (Exponencial)**

Explora todas as combinações possíveis de itens.

* ✔️ Didática
* ❌ Extremamente lenta para *n > ~25*
* Complexidade: **O(2^n)**

---

### 3. **Top-Down com Memoização**

A versão recursiva otimizada com armazenamento de resultados.

* ✔️ Garante ótimos resultados
* ✔️ Mais intuitiva que bottom-up
* Complexidade: **O(n · C)**

---

### 4. **Bottom-Up (Programação Dinâmica Iterativa)**

Preenche tabela de estados incrementalmente.

* ✔️ Solução mais estável e eficiente
* ✔️ Muito usada em aplicações reais
* Complexidade: **O(n · C)**

---

## 📂 Estrutura do Repositório

```
📁 globaldynamic
│
├── main.py             # Código completo com todas as abordagens
├── README.md               # Documento atual
```

---

## 🛠️ Requisitos

Este projeto utiliza apenas recursos padrão do Python.

### ✔️ Requisitos mínimos:

* Python **3.8+**
* Nenhuma biblioteca externa é necessária

---

## ▶️ Como Executar

1. Certifique-se de que o Python está instalado:

```bash
python --version
```

2. Execute o arquivo principal:

```bash
python knapsack.py
```

3. O programa executará automaticamente os testes disponíveis, exibindo:

* Valor ótimo esperado
* Resultado de cada abordagem
* Comparação entre soluções

---

## 📊 Exemplo de Saída

A execução imprimirá resultados similares a:

```
--- Caso 1 ---
Projetos: [('A', 12, 4), ('B', 10, 3), ...]
Capacidade: 10
Valor ótimo esperado: 29

Gulosa: Valor 26
Recursiva pura: Valor 29
Top-Down: Valor 29
Bottom-Up: Valor 29
-> DP OK
-> Gulosa falhou (como esperado)
```

---

## 📚 Objetivos Didáticos

Este projeto foi desenvolvido com foco em:

* Demonstrar as diferenças entre abordagens para o Knapsack
* Servir de material de estudo para Programação Dinâmica
* Facilitar entendimento por meio de **comentários extensos no código**

---

## 💡 Pontos Importantes

* A estratégia gulosa é uma **heurística**, não uma solução exata.
* As soluções de Programação Dinâmica (**Top-Down** e **Bottom-Up**) sempre encontram o valor ótimo.
* A recursão pura é útil apenas para fins educacionais.

---

## 📝 Licença

Este projeto está sob licença livre para uso educacional.

---

## ✨ Autor

Desenvolvido para fins acadêmicos como demonstração das técnicas de resolução do problema da mochila.

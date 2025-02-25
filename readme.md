# Algoritmo de Karatsuba

O **Algoritmo de Karatsuba** é um método utilizado para multiplicar números grandes eficientemente. É mais rápido que o método usual de multiplicação longa, que necessita de n^2 multiplicações de um dígito simples.

### Descrição do Projeto

O projeto implementa o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros grandes. O algoritmo de Karatsuba é um método recursivo que reduz a complexidade da multiplicação de O(n^2) para O(n^(log 3), onde n é o número de dígitos dos números a serem multiplicados.

#### Explicação do Algoritmo e da Lógica

1. **Caso Base da Recursão**:
    ```python
    if multiplicando < 10 or mutiplicador < 10:
        return multiplicando * mutiplicador
    ```
    Se qualquer um dos números for menor que 10, a multiplicação é feita diretamente.

2. **Divisão dos Números**:
    ```python
    n_casas = max(len(str(multiplicando)), len(str(mutiplicador)))
    m = n_casas // 2
    a, b = divmod(multiplicando, 10 ** m)
    c, d = divmod(mutiplicador, 10 ** m)
    ```
    Os números são divididos em duas partes: a e b para o primeiro número, c e d para o segundo número.

3. **Recursão para Calcular os Produtos**:
    ```python
    ac = karatsuba_algorithm(a, c)
    bd = karatsuba_algorithm(b, d)
    ad_bc = karatsuba_algorithm(a + b, c + d) - ac - bd
    ```
    São calculados os produtos ac, bd e ad_bc usando chamadas recursivas.

4. **Combinação dos Resultados**:
    ```python
    return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd
    ```
    Os resultados são combinados para obter o produto final.

5. **Função para Testar a Multiplicação**:
    ```python
    def testar_mutiplicacao_numeros():
    ```
    Esta função mede o tempo de execução do algoritmo de Karatsuba.

6. **Definição dos Números e Execuções**:
    ```python
    x = 123456789
    y = 987654321
    num_executions = 1000
    total_time = 0
    ```
    São definidos os números a serem multiplicados e o número de execuções para medir o tempo médio.

7. **Loop para Medir o Tempo de Execução**:
    ```python
    for _ in range(num_executions):
        start = time.time()
        resultado = karatsuba_algorithm(x, y)
        end = time.time()
        total_time += (end - start)
    ```
    O algoritmo é executado 1000 vezes e o tempo total é acumulado.

8. **Cálculo e Impressão do Tempo Médio**:
    ```python
    average_time = total_time / num_executions
    print("Resultado:", resultado)
    print(f"Tempo de execução médio: {average_time:.10f}")
    ```
    O tempo médio de execução é calculado e impresso junto com o resultado da multiplicação.

### Análise da Complexidade Ciclomática

A complexidade ciclomática é uma métrica que mede a quantidade de caminhos lineares independentes através de um programa. Para calcular a complexidade ciclomática, precisamos representar o fluxo de controle da função e estruturar o grafo de fluxo.

### Fluxo de Controle da Função

![](<Screenshot_20250224_163132_Samsung Notes.jpg>)
#### Grafo de Fluxo

- **Nós**:
  1. Início da função
  2. Verificação do caso base
  3. Retorno do caso base
  4. Divisão dos números
  5. Recursão para ac
  6. Recursão para bd
  7. Recursão para ad_bc
  8. Combinação dos resultados
  9. Retorno do resultado final

- **Arestas**:
  1. Início -> Verificação do caso base
  2. Verificação do caso base -> Retorno do caso base (verdadeiro)
  3. Verificação do caso base -> Divisão dos números (falso)
  4. Divisão dos números -> Recursão para ac
  5. Recursão para ac -> Recursão para bd
  6. Recursão para bd -> Recursão para ad_bc
  7. Recursão para ad_bc -> Combinação dos resultados
  8. Combinação dos resultados -> Retorno do resultado final

#### Cálculo da Complexidade Ciclomática

Usando a fórmula \( M = E - N + 2P \):

- \( E \) (Número de arestas): 8
- \( N \) (Número de nós): 9
- \( P \) (Número de componentes conexos): 1

\[ M = 8 - 9 + 2 \times 1 = 1 \]

A complexidade ciclomática da função  é 1.

### Análise da Complexidade Assintótica

#### Complexidade Temporal

- **Melhor Caso**: O melhor caso ocorre quando um dos números é menor que 10. Neste caso, a complexidade é \( O(1) \).
- **Caso Médio e Pior Caso**: No caso médio e pior caso, a complexidade temporal do algoritmo de Karatsuba é \( O(n^{\log_2 3}) \approx O(n^{1.585}) \), onde \( n \) é o número de dígitos dos números a serem multiplicados.

#### Complexidade Espacial

- **Melhor Caso**: \( O(1) \) (quando um dos números é menor que 10).
- **Caso Médio e Pior Caso**: A complexidade espacial é dominada pela profundidade da recursão, que é \( O(\log n) \).

### Como Executar o Projeto

Para executar o projeto no seu ambiente local, siga os passos abaixo:

1. **Clone o Repositório**:
    ```sh
    git clone https://github.com/lucasxae/Algoritmo-de-Karatsuba-.git
    cd Algoritmo-de-Karatsuba-
    ```

2. **Execute o Script**:
    ```sh
    python main.py
    ```
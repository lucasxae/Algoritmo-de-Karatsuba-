# Algoritmo de Karatsuba

O **Algoritmo de Karatsuba** é um método utilizado para multiplicar números grandes eficientemente. É mais rápido que o método usual de multiplicação longa, que necessita de \(n^{2}\) multiplicações de um dígito simples.

### Descrição do Projeto

O projeto implementa o algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros grandes. O algoritmo de Karatsuba é um método recursivo que reduz a complexidade da multiplicação de \(O(n^2)\) para \(O(n^{\log_2 3})\), onde \(n\) é o número de dígitos dos números a serem multiplicados.

#### Explicação do Algoritmo e da Lógica

1. **Importação do Módulo `time`**:
    ```python
    import time
    ```
    O módulo [time](http://_vscodecontentref_/20) é importado para medir o tempo de execução do algoritmo.

2. **Definição da Função [karatsuba_algorithm](http://_vscodecontentref_/21)**:
    ```python
    def karatsuba_algorithm(multiplicando, mutiplicador):
    ```
    Esta função implementa o algoritmo de Karatsuba.

3. **Caso Base da Recursão**:
    ```python
    if multiplicando < 10 or mutiplicador < 10:
        return multiplicando * mutiplicador
    ```
    Se qualquer um dos números for menor que 10, a multiplicação é feita diretamente.

4. **Divisão dos Números**:
    ```python
    n_casas = max(len(str(multiplicando)), len(str(mutiplicador)))
    m = n_casas // 2
    a, b = divmod(multiplicando, 10 ** m)
    c, d = divmod(mutiplicador, 10 ** m)
    ```
    Os números são divididos em duas partes: [a](http://_vscodecontentref_/22) e [b](http://_vscodecontentref_/23) para o primeiro número, [c](http://_vscodecontentref_/24) e [d](http://_vscodecontentref_/25) para o segundo número.

5. **Recursão para Calcular os Produtos**:
    ```python
    ac = karatsuba_algorithm(a, c)
    bd = karatsuba_algorithm(b, d)
    ad_bc = karatsuba_algorithm(a + b, c + d) - ac - bd
    ```
    São calculados os produtos [ac](http://_vscodecontentref_/26), [bd](http://_vscodecontentref_/27) e [ad_bc](http://_vscodecontentref_/28) usando chamadas recursivas.

6. **Combinação dos Resultados**:
    ```python
    return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd
    ```
    Os resultados são combinados para obter o produto final.

7. **Função para Testar a Multiplicação**:
    ```python
    def testar_mutiplicacao_numeros():
    ```
    Esta função mede o tempo de execução do algoritmo de Karatsuba.

8. **Definição dos Números e Execuções**:
    ```python
    x = 123456789
    y = 987654321
    num_executions = 1000
    total_time = 0
    ```
    São definidos os números a serem multiplicados e o número de execuções para medir o tempo médio.

9. **Loop para Medir o Tempo de Execução**:
    ```python
    for _ in range(num_executions):
        start = time.time()
        resultado = karatsuba_algorithm(x, y)
        end = time.time()
        total_time += (end - start)
    ```
    O algoritmo é executado 1000 vezes e o tempo total é acumulado.

10. **Cálculo e Impressão do Tempo Médio**:
    ```python
    average_time = total_time / num_executions
    print("Resultado:", resultado)
    print(f"Tempo de execução médio: {average_time:.10f}")
    ```
    O tempo médio de execução é calculado e impresso junto com o resultado da multiplicação.

11. **Execução do Teste**:
    ```python
    if __name__ == "__main__":
        testar_mutiplicacao_numeros()
    ```
    A função de teste é chamada se o script for executado diretamente.

### Análise da Complexidade Ciclomática

A complexidade ciclomática é uma métrica que mede a quantidade de caminhos lineares independentes através de um programa. Para calcular a complexidade ciclomática, precisamos representar o fluxo de controle da função [karatsuba_algorithm](http://_vscodecontentref_/29) e estruturar o grafo de fluxo.

#### Fluxo de Controle da Função [karatsuba_algorithm](http://_vscodecontentref_/30)

1. **Início da Função**
2. **Verificação do Caso Base**: [if multiplicando < 10 or mutiplicador < 10](http://_vscodecontentref_/31)
   - **Verdadeiro**: Retorna [multiplicando * mutiplicador](http://_vscodecontentref_/32)
   - **Falso**: Continua para a divisão dos números
3. **Divisão dos Números**: [a, b = divmod(multiplicando, 10 ** m)](http://_vscodecontentref_/33) e [c, d = divmod(mutiplicador, 10 ** m)](http://_vscodecontentref_/34)
4. **Recursão para Calcular os Produtos**: [ac = karatsuba_algorithm(a, c)](http://_vscodecontentref_/35), [bd = karatsuba_algorithm(b, d)](http://_vscodecontentref_/36), [ad_bc = karatsuba_algorithm(a + b, c + d) - ac - bd](http://_vscodecontentref_/37)
5. **Combinação dos Resultados**: [return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd](http://_vscodecontentref_/38)

#### Grafo de Fluxo

- **Nós**:
  1. Início da função
  2. Verificação do caso base
  3. Retorno do caso base
  4. Divisão dos números
  5. Recursão para [ac](http://_vscodecontentref_/39)
  6. Recursão para [bd](http://_vscodecontentref_/40)
  7. Recursão para [ad_bc](http://_vscodecontentref_/41)
  8. Combinação dos resultados
  9. Retorno do resultado final

- **Arestas**:
  1. Início -> Verificação do caso base
  2. Verificação do caso base -> Retorno do caso base (verdadeiro)
  3. Verificação do caso base -> Divisão dos números (falso)
  4. Divisão dos números -> Recursão para [ac](http://_vscodecontentref_/42)
  5. Recursão para [ac](http://_vscodecontentref_/43) -> Recursão para [bd](http://_vscodecontentref_/44)
  6. Recursão para [bd](http://_vscodecontentref_/45) -> Recursão para [ad_bc](http://_vscodecontentref_/46)
  7. Recursão para [ad_bc](http://_vscodecontentref_/47) -> Combinação dos resultados
  8. Combinação dos resultados -> Retorno do resultado final

#### Cálculo da Complexidade Ciclomática

Usando a fórmula \( M = E - N + 2P \):

- \( E \) (Número de arestas): 8
- \( N \) (Número de nós): 9
- \( P \) (Número de componentes conexos): 1

\[ M = 8 - 9 + 2 \times 1 = 1 \]

A complexidade ciclomática da função [karatsuba_algorithm](http://_vscodecontentref_/48) é 1.

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

Isso irá executar o algoritmo de Karatsuba e imprimir o resultado da multiplicação e o tempo médio de execução.
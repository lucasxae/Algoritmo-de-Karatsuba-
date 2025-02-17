import time

def karatsuba_algorithm(multiplicando, mutiplicador):
    if multiplicando < 10 or mutiplicador < 10:
        return multiplicando * mutiplicador
    n_casas = max(len(str(multiplicando)), len(str(mutiplicador)))
    m = n_casas // 2
    a, b = divmod(multiplicando, 10 ** m)
    c, d = divmod(mutiplicador, 10 ** m)
    ac = karatsuba_algorithm(a, c)
    bd = karatsuba_algorithm(b, d)
    ad_bc = karatsuba_algorithm(a + b, c + d) - ac - bd
    return ac * 10 ** (2 * m) + ad_bc * 10 ** m + bd

def testar_mutiplicacao_numeros():
    x = 123456789
    y = 987654321
    num_executions = 1000
    total_time = 0

    for _ in range(num_executions):
        start = time.time()
        resultado = karatsuba_algorithm(x, y)
        end = time.time()
        total_time += (end - start)

    average_time = total_time / num_executions
    print("Resultado:", resultado)
    print(f"Tempo de execução médio: {average_time:.10f}")

if __name__ == "__main__":
    testar_mutiplicacao_numeros()
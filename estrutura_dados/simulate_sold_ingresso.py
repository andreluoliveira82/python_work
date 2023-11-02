
import time
import random
from estruturas import Queue

def simulate_line(till_show, max_time):
    """
    Simula a venda de ingressos para pessoas que estão em uma fila, cujo atendimento deve respeitar a ordem das pessoas na fila
    """


    # invoca a classe que enfileira as pessoas
    pq = Queue()

    # lista para armazenar as pessoas que forem atendidas (já compraram ingresso)
    tix_sold = []

    # simula a entrada de pessoas na fila para comprar ingressos
    for i in range(100):
        pq.enqueue("pessoa" + str(i))
    
    # cria um momento no futuro
    t_end = time.time() + till_show

    now = time.time()

    while now < t_end and not pq.is_empty():
        now = time.time()

        # obtém um valor aleatório e simula um tempo de atendimento diferente para cada pessoa
        r = random.randint(0, max_time) 
        time.sleep(r)

        # atende a pessoa e a remove da fila. Na sequencia inclui-a na lista de pessoas atendidas
        pessoa = pq.dequeue()
        print(pessoa.title())
        tix_sold.append(pessoa)
    
    return tix_sold

venda = simulate_line(15,1)
print(venda)
# * O .strftime('%H:%M:%S') tira os MICROSSEGUNDOS! Isso é interessante
from datetime import datetime, timedelta
pedido = "pizza_pendente"

pizza_paga = 25
pizza_pendente = 40
pizza_paga_gold = 15

data_atual = datetime.today()

if pedido == "pizza_pendente":
    data_estimada = data_atual + timedelta(minutes=pizza_paga)
    print(f"A comanda chegou: {data_atual.strftime('%H:%M:%S')} e ficará pronto às {data_estimada.strftime('%H:%M:%S')}")



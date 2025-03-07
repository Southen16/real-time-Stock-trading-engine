import threading
import random
import time
import bisect
from queue import Queue

class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

class StockTradingEngine:
    def __init__(self):
        self.buy_orders = [[] for _ in range(1024)]   
        self.sell_orders = [[] for _ in range(1024)]  
        self.order_queues = [Queue() for _ in range(1024)] 
        self.threads = [threading.Thread(target=self.processOrders, args=(i,)) for i in range(1024)]

        for thread in self.threads:
            thread.start()

    def addOrder(self, order_type, ticker, quantity, price):
        order = Order(order_type, ticker, quantity, price)
        index = int(ticker.replace("Ticker", "")) % 1024  
        self.order_queues[index].put(order)  

    def processOrders(self, index):
        while True:
            if not self.order_queues[index].empty():
                order = self.order_queues[index].get()

                if order.order_type == 'Buy':
                    bisect.insort(self.buy_orders[index], (-order.price, order)) 
                else:
                    bisect.insort(self.sell_orders[index], (order.price, order))  

                self.matchOrder(index)

    def matchOrder(self, index):
        buy_orders = self.buy_orders[index]
        sell_orders = self.sell_orders[index]
        
        i, j = 0, 0
        while i < len(buy_orders) and j < len(sell_orders):
            buy_price, buy_order = buy_orders[i]
            sell_price, sell_order = sell_orders[j]
            
            if -buy_price >= sell_price: 
                matched_quantity = min(buy_order.quantity, sell_order.quantity)
                buy_order.quantity -= matched_quantity
                sell_order.quantity -= matched_quantity

                if buy_order.quantity == 0:
                    i += 1
                if sell_order.quantity == 0:
                    j += 1
            else:
                break

        self.buy_orders[index] = buy_orders[i:] 
        self.sell_orders[index] = sell_orders[j:]  

def simulate_trading(engine):
    tickers = [f"Ticker{i}" for i in range(1024)]
    while True:
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = random.uniform(10, 1000)
        engine.addOrder(order_type, ticker, quantity, price)
        time.sleep(random.uniform(0.01, 0.1))

if __name__ == "__main__":
    engine = StockTradingEngine()
    threads = [threading.Thread(target=simulate_trading, args=(engine,)) for _ in range(10)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

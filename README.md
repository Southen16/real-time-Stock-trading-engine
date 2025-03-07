# real-time-Stock-trading-engine

Overview of the Stock Trading Simulation

This program simulates a real-time stock trading engine using multi-threading. It handles buy and sell orders for up to 1,024 different stocks, ensuring efficient order matching while maintaining concurrency.

Modules Used
	•	threading: Manages multiple threads to enable simultaneous stock transactions.
	•	random: Generates random values to simulate real-world stock orders.
	•	time: Introduces delays to make the simulation more realistic.

Order Class

The Order class represents an individual stock order with the following attributes:
	•	order_type: Specifies whether the order is a buy or sell request.
	•	ticker: Identifies the stock symbol.
	•	quantity: Represents the number of shares in the order.
	•	price: Defines the price per share.

StockTradingEngine Class

The StockTradingEngine class is responsible for handling stock orders and matching trades efficiently.

Key Components:
	•	Order Storage:
	•	self.buy_orders and self.sell_orders store buy and sell orders, categorized by stock ticker.
	•	The system supports 1,024 stocks using a list of lists to keep track of orders.
	•	Lock-Free Processing:
	•	Orders are added to a queue-based structure, ensuring atomic operations without requiring locks.
	•	Threading:
	•	Each ticker has a dedicated thread that continuously processes orders.

Key Methods:
	•	addOrder(order_type, ticker, quantity, price)
	•	Adds a new order to the appropriate buy or sell list.
	•	Uses direct indexing (instead of hashing) to group orders for the same stock.
	•	Orders are inserted in sorted order, eliminating the need for sorting later.
	•	The method enqueues the order for processing.
	•	matchOrder(index)
	•	Matches buy and sell orders based on price criteria.
	•	A buy order is fulfilled if its price is greater than or equal to the lowest available sell price.
	•	Orders are updated based on matched quantities, and fully executed orders are removed.
	•	Runs in O(n) time complexity, ensuring efficient order matching.

Simulating Stock Transactions

The simulate_trading function generates random stock orders to mimic real-time trading.
	•	It randomly selects an order type (Buy/Sell), stock ticker, quantity, and price.
	•	Calls addOrder to place the order into the system.
	•	Introduces a random delay between transactions to simulate real-world trading fluctuations.

Main Execution
	•	Creates an instance of StockTradingEngine.
	•	Launches 10 threads to simulate concurrent stock trading.
	•	Starts and manages the threads, ensuring they run simultaneously.

This implementation provides a scalable and lock-free approach to simulating stock trading while efficiently handling real-time order processing. 🚀

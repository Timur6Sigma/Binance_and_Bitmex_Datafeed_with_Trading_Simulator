try:
    import thread
except ImportError:
    import _thread as thread

class binance_wrapper:
    # At Start: Establish connection with the Binance-websocket and datafeed
    # Then: Receives and handles responses from the Bitmex-websocket -> stores bids and asks in lists and the
    #   best bid and best ask (price and size)

    def __init__(self, json, websocket):
        self.initiation_okay = "-Successfully connected to Binance-"  # initVarFirstTime
        self.json = json  # initVarFirstTime
        self.ws = websocket  # initVarFirstTime

        self.bid_list = None  # initVarFirstTime
        self.ask_list = None  # initVarFirstTime
        self.best_bid_price = None  # initVarFirstTime
        self.best_ask_price = None  # initVarFirstTime
        self.best_bid_size = None  # initVarFirstTime
        self.best_ask_size = None  # initVarFirstTime

        try:
            self.ws = self.ws.create_connection("wss://fstream.binance.com/ws/btcusdt@depth20@100ms")
            response = self.json.loads(self.ws.recv())
            if not (response["e"] == "depthUpdate"):
                self.initiation_okay = "Failed at connection(1)"
        except:
            self.initiation_okay = "Failed at connection(2)"

    def receive_and_distribute_responses_to_handlers(self):
        def run():
            response = self.json.loads(self.ws.recv())
            if response["e"] == "depthUpdate":
                self.fill_bid_and_ask_lists_and_variables(response)
        thread.start_new_thread(run, ())

    def fill_bid_and_ask_lists_and_variables(self, response):
        self.bid_list = response["b"]
        self.ask_list = response["a"]
        self.best_bid_price = float(response["b"][0][0])
        self.best_ask_price = float(response["a"][0][0])
        self.best_bid_size = float(response["b"][0][1]) * float(response["b"][0][0])
        self.best_ask_size = float(response["a"][0][1]) * float(response["a"][0][0])

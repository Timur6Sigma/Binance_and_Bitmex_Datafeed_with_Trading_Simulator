class trading_simulator:

    def __init__(self, taker_or_maker_entry, entry_price, exit_side_take_profit, take_profit_price, exit_side_stop_loss, stop_loss_price, taker_fee, maker_fee):

        self.trade_active = True

        self.taker_or_maker_entry = taker_or_maker_entry
        self.entry_price = entry_price

        self.exit_side_take_profit = exit_side_take_profit
        self.take_profit_price = take_profit_price

        self.exit_side_stop_loss = exit_side_stop_loss
        self.stop_loss_price = stop_loss_price

        self.taker_fee = taker_fee
        self.maker_fee = maker_fee

        self.percentage_gain_of_trade = 0

        if self.take_profit_price > self.stop_loss_price:
            self.long_or_short = "long"
        else:
            self.long_or_short = "short"

        print("Trade:", self.long_or_short)
        print("Entry:", self.entry_price)

    def check_if_trade_is_finished(self, best_bid_price, best_ask_price):
        if self.long_or_short == "long":
            if self.exit_side_take_profit == "bid":
                # If long and exit tp on bid: taker exit
                if best_bid_price >= self.take_profit_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.take_profit_price/self.entry_price-1)+self.taker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.take_profit_price/self.entry_price-1)+self.taker_fee
                    self.trade_active = False
                    print("Exit:", self.take_profit_price)
            elif self.exit_side_take_profit == "ask":
                # If long and exit tp on ask: maker exit
                if best_ask_price > self.take_profit_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.take_profit_price/self.entry_price-1)+self.maker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.take_profit_price/self.entry_price-1)+self.maker_fee
                    self.trade_active = False
                    print("Exit:", self.take_profit_price)

            if self.exit_side_stop_loss == "bid":
                # If long and exit sl on bid: taker exit
                if best_bid_price <= self.stop_loss_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.stop_loss_price/self.entry_price-1)+self.taker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.stop_loss_price/self.entry_price-1)+self.taker_fee
                    self.trade_active = False
                    print("Exit:", self.stop_loss_price)
            elif self.exit_side_stop_loss == "ask":
                # If long and exit sl on ask: maker exit
                if best_ask_price < self.stop_loss_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.stop_loss_price/self.entry_price-1)+self.maker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.stop_loss_price/self.entry_price-1)+self.maker_fee
                    self.trade_active = False
                    print("Exit:", self.stop_loss_price)

        elif self.long_or_short == "short":
            if self.exit_side_take_profit == "bid":
                # If short and exit tp on bid: maker exit
                if best_bid_price < self.take_profit_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.take_profit_price/self.entry_price-1)+self.maker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.take_profit_price/self.entry_price-1)+self.maker_fee
                    self.trade_active = False
                    print("Exit:", self.take_profit_price)
            elif self.exit_side_take_profit == "ask":
                # If short and exit tp on ask: taker exit
                if best_ask_price <= self.take_profit_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.take_profit_price/self.entry_price-1)+self.taker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.take_profit_price/self.entry_price-1)+self.taker_fee
                    self.trade_active = False
                    print("Exit:", self.take_profit_price)

            if self.exit_side_stop_loss == "bid":
                # If long and exit sl on bid: maker exit
                if best_bid_price > self.stop_loss_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.stop_loss_price/self.entry_price-1)+self.maker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.stop_loss_price/self.entry_price-1)+self.maker_fee
                    self.trade_active = False
                    print("Exit:", self.stop_loss_price)
            elif self.exit_side_stop_loss == "ask":
                # If short and exit sl on ask: taker exit
                if best_ask_price >= self.stop_loss_price:
                    if self.taker_or_maker_entry == "taker":
                        self.percentage_gain_of_trade = self.taker_fee+(self.stop_loss_price/self.entry_price-1)+self.taker_fee
                    elif self.taker_or_maker_entry == "maker":
                        self.percentage_gain_of_trade = self.maker_fee+(self.stop_loss_price/self.entry_price-1)+self.taker_fee
                    self.trade_active = False
                    print("Exit:", self.stop_loss_price)

        if not self.trade_active:
            print("---------------")

    def getter_exit_side_take_profit(self):
        return self.exit_side_take_profit

    def setter_exit_side_take_profit(self, new_exit_side_take_profit):
        self.exit_side_take_profit = new_exit_side_take_profit

    def getter_take_profit(self):
        return self.take_profit_price

    def setter_take_profit(self, new_take_profit_price):
        self.take_profit_price = new_take_profit_price

    def getter_exit_side_stop_loss(self):
        return self.exit_side_stop_loss

    def setter_exit_side_stop_loss(self, new_exit_side_stop_loss):
        self.exit_side_stop_loss = new_exit_side_stop_loss

    def getter_stop_loss(self):
        return self.stop_loss_price

    def setter_stop_loss(self, new_stop_loss_price):
        self.stop_loss_price = new_stop_loss_price
import Bitmex_Wrapper
import Binance_Wrapper
import websocket
import json
import numpy
import Trading_Simulator
import Trading_Indicators

if __name__ == '__main__':

    subscriptions = [{"op": "subscribe", "arg1": "orderBookL2_25", "arg2": "XBTUSD"}]

    bitmex_wrapper = Bitmex_Wrapper.bitmex_wrapper(numpy, json, websocket, subscriptions)
    binance_wrapper = Binance_Wrapper.binance_wrapper(json, websocket)

    percentage_gains = []
    indicators = Trading_Indicators.indicators(numpy)

    while True:
        bitmex_wrapper.receive_and_distribute_responses_to_handlers()
        binance_wrapper.receive_and_distribute_responses_to_handlers()

        indicators.run_calculations(bitmex_wrapper.best_bid_price, bitmex_wrapper.best_ask_price)

        if len(indicators.imbalance_list) > 1000:

            if indicators.trade_signal == "Price_will_increase":
                trade_on_bitmex = Trading_Simulator.trading_simulator(taker_or_maker_entry="maker", entry_price=bitmex_wrapper.best_ask_price,
                                                            exit_side_take_profit="bid", take_profit_price=bitmex_wrapper.best_ask_price-10,
                                                            exit_side_stop_loss="ask", stop_loss_price=bitmex_wrapper.best_ask_price*1.00075,
                                                            taker_fee=-0.00075, maker_fee=0.00025)

            if indicators.trade_signal == "Price_will_decrease":
                trade_on_bitmex = Trading_Simulator.trading_simulator(taker_or_maker_entry="maker", entry_price=bitmex_wrapper.best_bid_price,
                                                            exit_side_take_profit="ask", take_profit_price=bitmex_wrapper.best_ask_price+10,
                                                            exit_side_stop_loss="bid", stop_loss_price=bitmex_wrapper.best_ask_price*0.99925,
                                                            taker_fee=-0.00075, maker_fee=0.00025)

                while trade_on_bitmex.trade_active:

                    bitmex_wrapper.receive_and_distribute_responses_to_handlers()
                    indicators.run_calculations(bitmex_wrapper.best_bid_price, bitmex_wrapper.best_ask_price)
                    trade_on_bitmex.check_if_trade_is_finished(bitmex_wrapper.best_bid_price, bitmex_wrapper.best_ask_price)

                percentage_gains.append(trade_on_bitmex.percentage_gain_of_trade)
                print("Gainz:", percentage_gains)
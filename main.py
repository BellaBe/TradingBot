import tkinter as tk
import logging
from connectors.bitmex import BitmexClient
from connectors.binance_futures import BinanceFuturesClient
from interface.root_component import Root

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("info.log")

formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')

stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == "__main__":

    binance = BinanceFuturesClient(
        "55764814ef910b9e9a76f5336e8e4c096605f4195167504850a53660d1c1f56c",
        "3edd31374e7f615dd854e3d018b328aeccbbb8487a8b4cd24bdaf3c7a98f5bc2",
        True)

    bitmex = BitmexClient(
        "4JdbvKsTvSaD1J7iyQ1J37GL",
        "RS1IG_5CgBJrmLtA3q2HH83U-gViENv155JDAe5nIq4_retT",
        True
    )

    #bitmex.get_historical_candles(bitmex.contracts["XBTUSD"], "1h")
    #print(bitmex.place_order(bitmex.contracts["XBTUSD"], "Limit", 50.5, "Buy", price=20000.49392876, tif="GoodTillCancel"))
    # print(bitmex.contracts["XBTUSD"].base_asset, bitmex.contracts["XBTUSD"].price_decimals)
    # print(bitmex.balances["XBt"].wallet_balance)


    root = Root(bitmex, binance)
    root.mainloop()


####################################
# bitmex_contracts = get_contracts()
# root.configure(bg="gray12")
# i=0
# j=0
# calibri_font = ("Calibri", 11, "normal")
# for contract in bitmex_contracts:
#     label_widget = tk.Label(root, text=contract, bg="gray12", fg="SteelBlue1", width=13, font=calibri_font)
#     #label_widget.pack(side=tk.TOP)
#     #label_widget.pack(side=tk.BOTTOM)
#     #label_widget.pack(side=tk.LEFT)
#     #label_widget.pack(side=tk.RIGHT)
#     label_widget.grid(row=i, column=j, sticky="ew")
#     if i == 4:
#         j += 1
#         i = 0
#     else:
#         i += 1

###################################
#print(binance.get_contracts())
    #print(binance.get_bid_ask("BTCUSDT"))
    #print(binance.get_historical_candles("BTCUSDT", "1h"))
    #print(binance.get_balances())
    #print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 2000, "GTC"))
    # print(binance.get_order_status("BTCUSDT", 2694437026))
    # print(binance.cancel_order("BTCUSDT", 2694437026))



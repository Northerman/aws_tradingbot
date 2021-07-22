import os
import alpaca_trade_api as tradeapi
import pandas as pd
import numpy as np
import boto3
import ta
from ta.momentum import RSIIndicator
import pymysql
from datetime import datetime

sns = boto3.client('sns')
quotes = ['AAPL','TSLA','AMZN','NFLX','GOOGL','FB','MSFT']
pd.options.mode.chained_assignment = None  # default='warn'

def create_rsi(api,quote_name, timeframe,window = 14):
  barset = api.get_barset(quote_name, timeframe).df
  quote_bars = barset[quote_name]
  indicator_rsi = RSIIndicator(close=quote_bars["close"], window=window)
  quote_bars['rsi'] = indicator_rsi.rsi()
  return quote_bars

def calculate_buy_qty(api,quote_name,buying_amount = 10000):
    df = api.get_barset(quote_name, 'minute').df
    qty = buying_amount/df[quote_name].iloc[-1:,:]['close'].values[0]
    return round(qty-0.5)

def execute_rsi_strategy(api,quote_bars,quote_name,qty):
  if sum(quote_bars['rsi'][-5:]>70):
      print("Attempting to Buy:",quote_name)
      try:
        msg = api.submit_order(symbol = quote_name,qty = qty,side = 'buy',type = 'market',time_in_force = 'gtc')
        print('Buy order placed:',quote_name,msg.qty)
      except Exception as e:
        print(e)


  elif sum(quote_bars['rsi'][-5:]<30):
      print("Attempting to Sell",quote_name)
      has_stock = False
      for position in api.list_positions():
        if position.symbol == quote_name:
          has_stock = True
          try:
            msg = api.submit_order(symbol = quote_name,qty = position.qty,side = 'sell',type = 'market',time_in_force = 'gtc')
            print('Sell order placed:',quote_name,msg.qty)
          except Exception as e:
            print(e)
      if has_stock == False:
        print('No stock to sell')
      

  else:
    pass
def handler(event, context):
  os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"
  orders = []
  #Insert API Credentials 
  api = tradeapi.REST('YOUR API KEY','YOUR API SECRET', api_version='v2')
  now = datetime.now().strftime("%Y%m%d")

  ## Execute strategy
  for quote in quotes:
    print(quote)
    quote_df = create_rsi(api,quote_name = quote, timeframe = 'day',window = 14)
    buy_qty = calculate_buy_qty(api,quote_name = quote, buying_amount = 10000)
    execute_rsi_strategy(api,quote_bars = quote_df, quote_name = quote, qty = buy_qty)
    print('------------------------------------------------------------')


  ### Update Order placed ###

  # Connect DB

  endpoint = 'YOUR_AWS_DB'
  username = 'YOUR_AWS_DB_USERNAME'
  database_name = 'YOUR_TABLE'

  conn = pymysql.connect(host = endpoint,
                               user=username,
                               password='YOUR_DB_PASSWORD',
                               database=database_name,
                         )
  cursorObject = conn.cursor()

  # Get orders for update
  all_orders = api.list_orders(status='closed',limit = 100)
  orders_to_insert = []
  for order in all_orders:
    orders_to_insert.append([order.id,now,order.symbol,int(order.qty),order.side,order.filled_avg_price])

  # Update DB
  cursorObject.executemany("insert IGNORE into trade_history(id,datadate,quote_name,qty,position,price) values (%s, %s,%s,%s,%s,%s)", orders_to_insert)
  conn.commit()


  cursorObject.close()
  conn.close()
  

  ### Send Msg ###
  numbers = 'YOUR_PHONE_NUMBER'
  account = api.get_account()

  # Check our current balance vs. our balance at the last market close
  balance_change = float(account.equity) - float(account.last_equity)
  print(f'Today\'s portfolio balance change: ${balance_change}')

    # Msg
  sns.publish(PhoneNumber = numbers, Message = f'Today\'s portfolio balance change: ${balance_change}') 






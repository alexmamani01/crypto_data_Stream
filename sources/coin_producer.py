import time
from constants import COINMARKET_KEY
from quixstreams import Application
from requests import Session
from requests.exceptions import  Timeout, TooManyRedirects
import json
from pprint import pprint 

#quixstream es....

app=Application(
    broker_address='localhost:9092',
    consumer_group="coinmarket_group"
)
#Para crear el topic en kafka , a través de quixstream, los datos se serializan a formato json antes de ser enviados
coins_topic=app.topic(name='coins', value_serializer='json' )

#Fx para obtener los datos más recientes de una coin
def get_latest_btc_data(symbol='BTC'):
    url= 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters={
    "convert" : 'USD',
    "symbol": symbol
    }


    headers={
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKET_KEY
    }


    session= Session()
    session.headers.update(headers)

    try:
        response=session.get(url, params=parameters)
        return json.loads(response.text)["data"][symbol]
    except (ConnectionError, Timeout, TooManyRedirects) as e :
        print(e)

    
        

def main():
    with app.get_producer() as producer:
        while True:
            coin_latest=get_latest_btc_data('BTC')
            kafka_message= coins_topic.serialize(
                key=coin_latest['symbol'], value=coin_latest
            )

            print(
                f"produce event with key = {kafka_message.key}, value= {coin_latest ['quote']['USD']['price']}"
            )
            #para enviar los datos a kafka
            #to send the data to kafka
            producer.produce(
                topic=coins_topic.name, key=kafka_message.key, value=kafka_message.value 
            )

            time.sleep(10)
    
if __name__== "__main__":
    main()
    result= get_latest_btc_data('BTC')
    pprint(result) 
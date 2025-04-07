from quixstreams import Application
from quixstreams.sinks.community.postgresql import PostgreSQLSink
from constants import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_PWD, POSTGRES_USER)


def extract_coin_data(message):
    latest_quote=message['quote']['USD']
    return {
        "coin": message['name'] ,
    
        "price_usd": message ['price'] ,
        "volume":  latest_quote['volume_24h']    ,
        "update": message['last_update']
          
    }
    
def create_postgres_sink():
    sink=PostgreSQLSink(
        host= POSTGRES_HOST, 
        port = POSTGRES_PORT, 
        dbname= POSTGRES_DB, 
        user= POSTGRES_USER,
        password= POSTGRES_PWD, 
        table_name= 'Bitcoin_price',
        schema_auto_update=True, 
        
    )
    return sink

def main():
    app= Application(
        broker_address= "localhost:9092",
        consumer_group="coin_group",
        auto_offset_reset='earliest',
    )
    
    coins_topic=app.topic(name='coins', value_deserializer='json')
    dataframe=app.dataframe(topic=coins_topic)
    dataframe=dataframe.apply(extract_coin_data)
    dataframe.update(lambda coin_data: print (coin_data))
    postgres_sink= create_postgres_sink()
    dataframe.sink(postgres_sink)
    app.run

if __name__=='__main__':
    main()
        

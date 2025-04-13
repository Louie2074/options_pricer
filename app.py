from influxdb_client_3 import InfluxDBClient3
import os
from dotenv import load_dotenv


load_dotenv()
influx_token = os.getenv("INFLUXDB_TOKEN")

org = "Dev"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"
database = "Bitcoin"

influx_client = InfluxDBClient3(host=host, token=influx_token, org=org)
btc_latest_close = 'SELECT "close" FROM "btc_bars" WHERE time >= now() - interval \'5 minutes\' ORDER BY time DESC LIMIT 1'

table = influx_client.query(query=btc_latest_close,
                            database=database, language='sql')

df = table.to_pandas()
close_value = int(df["close"].iloc[0])
print(close_value)

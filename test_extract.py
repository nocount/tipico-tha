import requests
import json
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

redshift_conn_string = "redshift+psycopg2://username:password@hostname:port/database"
api_url = "https://trading-api.tipico.us/v1/pds/lbc/events/live?licenseId=US-NJ&lang=en&limit=18"
# tipico-tha-test.444144597060.eu-west-2.redshift-serverless.amazonaws.com:5439/dev
# 'postgresql://tipicotest:Speakfriendandenter1!@tipico-tha-test.444144597060.eu-west-2.redshift-serverless.amazonaws.com:5439/dev'
# 'postgresql://wilson_burchenal:SFJi1410!!__Sffj9afs82131314@manual-dwh-candidatetests.258845600139.us-east-1.redshift-serverless.amazonaws.com:5439/dev'
def main():

    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:

        data = json.loads(response.content)
        df = pd.DataFrame(data)
        # df.to_csv('api_data.csv', index=False)

        engine = create_engine('postgresql://wilson_burchenal:SFJi1410!!__Sffj9afs82131314@manual-dwh-candidatetests.258845600139.us-east-1.redshift-serverless.amazonaws.com:5439/dev')
        conn = engine.connect()

        df.to_sql(name='wb_tipico_events', con=conn, schema='wilson_burchenal', index=False, if_exists='replace')
        conn.close()

        print(f"API data stored successfully at {datetime.now()}")
    else:
        print(f"Failed to call the API. Status code: {response.status_code}")


if __name__ == '__main__':
    main()

import requests
import json
import pandas as pd
from datetime import datetime


def main():
    api_url = "https://trading-api.tipico.us/v1/pds/lbc/events/live?licenseId=US-NJ&lang=en&limit=18"

    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:

        data = json.loads(response.content)
        df = pd.DataFrame(data)
        df.to_csv('api_data.csv', index=False)

        print(f"API data stored successfully at {datetime.now()}")
    else:
        print(f"Failed to call the API. Status code: {response.status_code}")


if __name__ == '__main__':
    main()

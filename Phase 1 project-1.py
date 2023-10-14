import requests
import pandas as pd


api_url = "https://api.binance.com/api/v3/ticker/24hr"
response = requests.get(api_url)


if response.status_code == 200:
    api_data = response.json()

    
    df = pd.DataFrame(api_data)

    
    csv_file_path = "C:\\Users\\Admin\\OneDrive\\Desktop\\new.csv"

    
    df.to_csv(csv_file_path, index=False)

    print(f"CSV dataset has been created and saved at: {csv_file_path}")

else:
    print("Failed to retrieve data from the API.")

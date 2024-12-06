import requests
from datetime import datetime
from pathlib import Path

def main():
    # Set headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make request to CoinMarketCap
    response = requests.get('https://coinmarketcap.com', headers=headers)
    
    # Create snapshots directory if it doesn't exist
    Path('snapshots').mkdir(exist_ok=True)
    
    # Generate filename with current timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'snapshots/coinmarketcap_{timestamp}.html'
    
    # Save the content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f'Saved snapshot to {filename}')

if __name__ == '__main__':
    main()
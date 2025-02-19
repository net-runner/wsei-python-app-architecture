import requests
import threading

def fetch_universities(country, result_dict):
    url = f"http://universities.hipolabs.com/search?country={country}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        universities = [uni["name"] for uni in response.json()]
        result_dict[country] = universities
    except requests.RequestException as e:
        result_dict[country] = [f"Error: {e}"]

if __name__ == "__main__":
    countries = [
        "United States", "Poland", "Montenegro", "Germany", "France", 
        "Italy", "Spain", "Netherlands", "Sweden", "Switzerland", 
        "Australia", "Japan", "China", "India", "Brazil", 
        "South Korea", "South Africa", "Mexico", "Russia", "Argentina"
    ]
    
    threads = []
    results = {}
    
    for country in countries:
        thread = threading.Thread(target=fetch_universities, args=(country, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(results)

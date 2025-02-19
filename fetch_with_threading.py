import requests
import threading
import json

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
        "United States", "Canada", "United Kingdom", "Germany", "France", 
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
    
    with open("universities.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print("Data saved to universities.json")

import requests
import json
import time
from config import API_KEY

def settings():
    # Get the current time
    timer = time.strftime("%I-%M-%S %p", time.localtime())
    # Prompt user for the type of news
    query = input("What type of news do you want? : ")
    if not query:
        print("Query cannot be empty.")
        return None, None
    # Form the API URL
    url = f"https://newsapi.org/v2/top-headlines?q={query}&from=2024-07-25&sortBy=popularity&apiKey={API_KEY}"
    return timer, url

def get_news(timer, url):
    if not url:
        return
    try:
        # Send the request to the news API
        r = requests.get(url)
        r.raise_for_status()  # Check for HTTP errors
        # Parse the JSON response
        news = json.loads(r.text)

        # Check if there are articles in the response
        if "articles" in news:
            for article in news["articles"]:
                # Print the news details
                print(f"{timer}\n")
                print(f"The source of the news is {article['author']}\n")
                print(f"TITLE: {article['title']} \n")
                print(f"Description: {article['description']}")
                print("_________________________________________\n")
        else:
            print("No articles found or there was an error with the API request.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError:
        print("Error decoding the JSON response")

# Pack all the functions into one main function
def main():
    # Call settings to get the timer and URL
    timer, url = settings()

    # Fetch and display the news
    get_news(timer, url)

# Call the main function
if __name__ == "__main__":
    main()

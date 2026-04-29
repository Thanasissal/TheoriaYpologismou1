import requests

def get_html():
    while True:
        url = input("Εισάγετε το URL της πόλης από τη Wikipedia: ") #παίρνουμε την URL απο τον χρήστη
        if url.startswith("http://") or url.startswith("https://"):
            break
        else:
            print("Μη έγκυρο URL")



    #Το κάνουμε user-agent για να μην το μπλοκάρει το wikipedia
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
           'Content-Type': 'text/html; charset=utf-8'
           }

    response = requests.get(url, headers=headers) #Παίρνουμε το html της σελίδας
    html = response.text
    return html

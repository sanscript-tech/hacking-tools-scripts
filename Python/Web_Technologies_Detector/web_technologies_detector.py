from Wappalyzer import Wappalyzer, WebPage

url = ""

def detect():
    wappalyzer = Wappalyzer.latest()
    webpage = WebPage.new_from_url(url)
    print(wappalyzer.analyze_with_versions_and_categories(webpage))

def main():
    global url
    url = input("Enter the full url you want to check for: ")
    detect()


if __name__ == "__main__":
    main()

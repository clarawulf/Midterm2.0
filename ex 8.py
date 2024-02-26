# Write a function that checks if the passed parameter is a valid URL or not.

s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
start = 0

while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:
        url = s[start:]
        if url.startswith(("http://", "https://", "ftp://", "ftps://")):
            print(url)
        break
    url = s[start:end]
    if url.startswith(("http://", "https://", "ftp://", "ftps://")):
        print(url)
    start = end

def urlify(url: str) -> str:
    url = trimTrailingSpaces(url)
    i = 0
    while i < len(url):
        if url[i] == ' ':
            url = url[:i] + '%20' + url[i+1:]
            i += 2
        i += 1
    return url

def trimTrailingSpaces(url: str) -> str:
    i = len(url)-1
    while url[i] == ' ':
        i -= 1
    url = url[:i+1]
    return url

tests = ['Mr John Smith      ', " a a s  w q"]
for test in tests:
    print(urlify(test))
# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)

# Python doesn't require space-adjusted array, so first we trim the additional spaces at the end with trimTrailingSpaces method
# Then, simply perform slicing operations each time space is encountered, accounting for i positions.

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
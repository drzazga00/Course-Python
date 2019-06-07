import webbrowser

link = input('Podaj link: ')


start = ['https://', 'http://', 'www']
end = ['.pl', '.com']
s = link[:7]
e = link[-4:]

def czy_start():
    counter = 0
    if not '.' in s[3] or not ':' in s[4:5]:
        return True
    for i in start:
        if i in s:
            return True
        else:
            counter +=1
    if counter == 3:
        return False

def czy_end():
    counter = 0
    for i in end:
        if i in e:
            return True
        else:
            counter +=1
    if counter == 2:
        return False




def main():
    if czy_start() == True:
        czy_end()
        if czy_end() == True:
            print('wyglada jak link')
            print('opening in process...')
            webbrowser.open(link)
        else:
            raise Exception('URLError')
    else:
        raise Exception('URLError')

if __name__ == "__main__":
    main()

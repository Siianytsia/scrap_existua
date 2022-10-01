with open('script.py', 'r+', encoding='utf-8') as file:
    scr = file.readlines()
    with open('../categories_urls.txt', 'r', encoding='utf-8') as urls_file:
        counter = 1
        for i in range(len(urls_file.readlines())):
            scr[41] = f'    ind = {i}'
            with open(f'../scripts/script_{counter}', 'w', encoding='utf-8') as script_file:
                for line in scr:
                    script_file.write(line)
            counter += 1
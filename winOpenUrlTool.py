import time
import os
import webbrowser

if __name__ == '__main__':
    print(os.getcwd())
    filename = "result.txt"

    webbrowser.open("www.baidu.com")
    time.sleep(20)

    with open(filename, 'r', encoding='utf-8') as load_f:
        for line in load_f.readlines():
            webbrowser.open_new_tab(line)
            time.sleep(2)

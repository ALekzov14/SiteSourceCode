import requests
import time


check = 'https://' #8

def main():
    source = "Hi!\n\n"
    for char in source:
        print(char, end='')
        time.sleep(0.5)


    while True:
        site = input("[→] Enter the website address:")
        if check in site:
            print("",end='')

        else:
            print("[!] Incorrect website address! - Exit")
            time.sleep(0.5)
            break

        files = input("[→] Enter the file name:")
        if files == ' ':
            print("[!] Incorrect file name! - Exit")
            time.sleep(0.5)
            break

        else:
            response = requests.get(site).text

            with open(f"{files}.html", "w", encoding="utf-8") as file:
                file.write(response)

            print(f'[✓] The file {files} was saved successfully')

            next = input("[?] Repeat the program?(y/n)")
            if next == 'y':
                continue
            else:
                print("End")
                time.sleep(2)
                break


if __name__ == "__main__":
    main()
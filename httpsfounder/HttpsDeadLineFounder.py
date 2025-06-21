import requests

site = input("Enter site URL (example: http://localhost:8080): ").strip("/")

# Dizin wordlisti
try:
    with open("wordlist.txt", "r") as f:
        dir_list = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ 'wordlist.txt' not found.")
    exit()

# Dosya wordlisti (listofsec)
try:
    with open("listofsec.txt", "r") as f:
        file_list = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print("❌ 'listofsec.txt' not found.")
    exit()

found_dirs = []

with open("scan_results.txt", "w") as output_file:
    print("\n🔍 Scanning directories...\n")
    output_file.write("\n🔍 Scanning directories...\n\n")

    for d in dir_list:
        url = f"{site}/{d}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 404:
                line = f"[DIR] Found: {url} (Status: {response.status_code})\n"
                print(line, end='')
                output_file.write(line)
                found_dirs.append(d)
        except requests.exceptions.RequestException:
            line = f"[-] Error connecting to {url}\n"
            print(line, end='')
            output_file.write(line)

    print("\n🔍 Scanning files inside found directories...\n")
    output_file.write("\n🔍 Scanning files inside found directories...\n\n")

    for d in found_dirs:
        for f_name in file_list:
            url = f"{site}/{d}/{f_name}"
            try:
                response = requests.get(url, timeout=5)
                if response.status_code != 404:
                    line = f"[FILE] Found: {url} (Status: {response.status_code})\n"
                    print(line, end='')
                    output_file.write(line)
            except requests.exceptions.RequestException:
                line = f"[-] Error connecting to {url}\n"
                print(line, end='')
                output_file.write(line)

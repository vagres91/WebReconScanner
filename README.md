# Directory & File Scanner for Web Pentesting

This Python script helps you perform basic directory and file discovery on target websites — a fundamental step in web penetration testing.

## Features

- **Customizable wordlists:**  
  Easily configure the directories (`wordlist.txt`) and files (`listofsec.txt`) you want to scan by modifying the provided wordlist files. This flexibility allows you to tailor scans to different targets or testing scenarios.

- **HTTP status code filtering:**  
  The script identifies and reports URLs returning responses other than 404, helping you discover hidden or accessible parts of a website.

- **Output logging:**  
  All scan results are saved automatically to `scan_results.txt` for your records and further analysis. Results are also printed live to the console for real-time monitoring.

- **Timeout and error handling:**  
  Gracefully manages connection timeouts and errors to keep scanning stable.

## Usage

1. Prepare your `wordlist.txt` and `listofsec.txt` files with directory and file names respectively.

2. Run the script and enter the target URL when prompted (e.g., `http://example.com`).

3. Review results on the console or in `scan_results.txt`.

## Why use this?

- Great for beginners to understand how directory brute forcing works in penetration testing.

- Customizable to fit specific target reconnaissance needs.

- Lightweight and easy to extend or integrate into larger toolchains.

## Suggestions for Improvement / Future Features

- Add multi-threading to speed up scanning.

- Support for HTTP headers customization (User-Agent, cookies, etc.).

- Automatic generation of wordlists from web crawling.

- Integration with APIs or vulnerability databases for enriched analysis.

---

If you find this tool useful, feel free to ⭐ star the repo and contribute!

**Happy hacking!** 🔐

# Sender

The Multi-Request Sender is a Python tool for sending multiple HTTP requests to a target URL. It supports sending requests with or without the use of proxies, and allows configuring the number of threads and the number of requests per thread.

## Description

This tool was developed for stress testing and performance evaluation of web servers. It can be useful for developers and system administrators who want to assess the responsiveness of a server under load.

## Usage

### Requirements

- Python 3.x
- Libraries: `requests`

### Installation

`git clone https://github.com/tumilander/sender.git`

`cd multi-request-sender`

`pip install -r requirements.txt`

### Usage

Run the `sender.py` script providing the target URL and optionally configuring other options.

Example basic usage:

`python sender.py -u https://example.com -t 10 -n 20`

This will send 20 requests to `https://example.com` using 10 threads.

### Options

- `-u`, `--url`: Target URL (required)
- `-t`, `--threads`: Number of threads (default: 10)
- `-n`, `--requests`: Number of requests per thread (default: 10)
- `--use-proxies`: Use proxies for requests (optional)
- `--proxy-file`: File containing list of proxies (required with `--use-proxies`)

## Configuration

- **User Agents**: A list of user agents is provided in the script to simulate different browsers.
- **Random Headers**: Random HTTP headers are generated to make requests less predictable.
- **Proxy Rotation**: It's possible to use proxies to mask the attacker's IP address and avoid blocks from the target server.

## Help

Run the script with the `-h` or `--help` option to get help on the available options:

`python sender.py -h`

This will display the help with a description of the available options.

## Disclaimer

The author of this tool is not responsible for any misuse or illegal activities conducted with this tool.

## Contributions

Contributions are welcome! Feel free to open an issue or send a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
# Coinbase Python Sample

A sample Python application that reads market data from Coinbase using a web socket.

## Prerequisites

1. Download and install Python 3.12 or later: https://www.python.org/downloads/.
2. Open a terminal and run the following command to install certificates:
   ```shell
   open "/Applications/Python 3.12/Install Certificates.command"
   ```

## Installation

Open a terminal and run the following command to install the project's dependencies:

```shell
python3 -m pip install -r requirements.txt
```

## Configuration

Copy your Coinbase Cloud API key JSON file to the [conf](conf/) folder. The file's contents should look something like this:

```json
{
  "name": "organizations/aaaa-aaaa-aaaa-aaaa/apiKeys/bbbb-bbbb-bbbb-bbbb",
  "principal": "cccc-cccc-cccc-cccc",
  "principalType": "USER",
  "publicKey": "-----BEGIN EC PUBLIC KEY-----\nThis is public\nSo you can read it\n-----END EC PUBLIC KEY-----\n",
  "privateKey": "-----BEGIN EC PRIVATE KEY-----\nThis is private\nSo you should never place this information in Git\n-----END EC PRIVATE KEY-----\n",
  "createTime": "2024-02-16T01:30:31.590396594Z",
  "projectId": "dddd-dddd-dddd-dddd",
  "nickname": "coinbase-python-sample",
  "scopes": ["rat/portfolio:eeee-eeee-eeee-eeee#view", "rat#view"],
  "allowedIps": [],
  "keyType": "TRADING_KEY",
  "enabled": true
}
```

## Usage

Open a terminal and run the Python script using the following command:

```shell
python3 sample.py
```

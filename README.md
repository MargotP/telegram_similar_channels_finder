# Telegram Similar Channels Finder

## TL;DR
This script uses the Telegram API via the Telethon library to find channels on Telegram similar to the ones you specify. It is useful for discovering new content and communities related to your interests on Telegram. 



First, set up the required variables (`API_ID`, `API_HASH`, `SESSION_FILE_NAME`, and optionally `PROXY`) in the script. 

```python
# API ID: Your unique Telegram API ID. You can get this from https://my.telegram.org
API_ID = XXXXXXXX

# API Hash: Your unique Telegram API Hash. You can get this from https://my.telegram.org
API_HASH = ''

# Session File Name: The name of the session file to be used by Telethon.
# This file stores your login session to avoid re-logging in.
SESSION_FILE_NAME = 'telegram'

# Proxy Configuration: Configure this if you are behind a proxy.
# The format is a tuple: (proxy_type, hostname, port)
PROXY = ('http', 'proxy.example.com', 3128)

# CHANNELS: List of Telegram channel usernames to find similar channels for.
# Replace the values with the usernames of the channels you are interested in.
# The channel username can be found in the channel's invitation link, e.g., "redteamalerts" in "https://t.me/redteamalerts".
CHANNELS = ['cibsecurity','CyberSecurityTechnologies','socanalyst']
```



To start finding similar Telegram channels, execute the script using the following command:

```bash
python3 TelegramSimilarChannelFinder.py
```



## Configuration
To use this script, several settings need to be configured:

### Telegram API
1. **Obtain API ID and Hash**:
   - Visit [my.telegram.org](https://my.telegram.org).
   - Log in with your Telegram account.
   - Go to "API development tools" and create a new application.
   - Note down the `API_ID` and `API_HASH`.

2. **Configure the Script**:
   - Open the script and replace `API_ID` and `API_HASH` with your obtained values.
   - Modify `SESSION_FILE_NAME` if needed. This is the name of the file that will store your Telegram session.

### Proxy (Optional)
If you are behind a proxy, configure the proxy details in the script:
   - Replace the values in `PROXY` with your proxy details. For example: `('http', 'proxy.example.com', 3128)`.
   - If you are not using a proxy, you can leave this part unchanged or remove it.

### List of Channels
Fill the `CHANNELS` variable with usernames of Telegram channels for which you want to find similar channels.
   - For example: `CHANNELS = ['examplechannel1', 'examplechannel2']`.

   - The channel username can be found in its invitation link, e.g., "examplechannel1" in "https://t.me/examplechannel1".

     

## Usage
Once configured, run the script. The results will display similar channels to those specified in `CHANNELS`, only if Telegram's algorithm finds any similar channels.

```bash
> python3 TelegramSimilarChannelFinder_v3.py

    ╔════════════════════════════════════════════════════════════════╗
    ║                Telegram Similar Channels Finder                ║
    ║              Find similar Telegram channels easily             ║
    ╚════════════════════════════════════════════════════════════════╝
    

[INFO] Found similar channels for cibsecurity / ID = 1262650373
+------------------------+----------------------------+------------+
|        Username        |           Title            |     ID     |
+------------------------+----------------------------+------------+
| Cyber_Security_Channel |    Cyber Security News     | 1121373769 |
| cloudandcybersecurity  |  Cloud and Cybersecurity   | 1371647277 |
|     androidMalware     | Android Security & Malware | 1164747047 |
|     thehackernews      |      The Hacker News       | 1009650918 |
|        malpedia        |    Malpedia Update Feed    | 1380507150 |
| Venari_By_BetterCyber  |          VenariX           | 1661936184 |
|    BleepingComputer    |      BleepingComputer      | 1094744974 |
|    SeguInfoChannel     |     Segu-Info Channel      | 1254615786 |
|   VulnerabilityNews    |     Vulnerability News     | 1160194119 |
|      fuzzinglabs       |        Fuzzing Labs        | 1457506183 |
+------------------------+----------------------------+------------+

[INFO] Found similar channels for CyberSecurityTechnologies / ID = 1221721225
+------------------+--------------------------------------+------------+
|     Username     |                Title                 |     ID     |
+------------------+--------------------------------------+------------+
|    freedomf0x    |             Freedom F0x              | 1440229722 |
| OffensiveTwitter |          Offensive Twitter           | 1591680548 |
|      hybgl       |           Волосатый бублик           | 1323455529 |
|   secharvester   |          Security Harvester          | 1140606841 |
|    reverseame    | RME-DisCo @ UNIZAR [www.reversea.me] | 1431420456 |
|      cKure       |                cKure                 | 1291965324 |
|  miirs_kingdom   |               Sunrise                | 1829670196 |
|      P0x3k       |             1N73LL1G3NC3             | 1510788812 |
|  PentestingNews  |           Pentesting News            | 1233397458 |
| reverse_dungeon  |           Reverse Dungeon            | 1408552684 |
+------------------+--------------------------------------+------------+
```


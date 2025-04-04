###### [(ระบบนี้ Transfer มาจาก Github Account เก่า --> https://github.com/TOEYJIRAKIT/Cyber-Security-Project)](https://github.com/TOEYJIRAKIT/Cyber-Security-Project)

## 🚀 **Project Name** :

PoD Attack Analytics – Ping of Death Attack Analytics Dashboard

## 📌 **Project Overview** :

Ping of Death Attack Analytics Dashboard is a powerful tool that visualizes and tracks Ping of Death (PoD) attacks on your network. This dashboard provides in-depth analysis and real-time insights into the nature of these attacks, helping you to stay ahead of malicious activities and protect your infrastructure.

## 🙏 **Project Overview** :
- 64102122 จิรภัทร จิตรภักดี
- 64102080 จิรกิตติ์ เอียดเหตุ 
- 64104532 ณัฐนันท์ ทองมาก
- 64125354 ภีรภัทร บุญสุวรรณ
- 64125735 ธนวัฒน์ กองสีสังข์
- 64110455 ภัครศักดิ์ ผลสนอง

## 🎯 **Objective** :

- Develop a monitoring system for detecting and analyzing Ping of Death (PoD) attacks.  
- Provide a real-time dashboard for visualizing attack patterns and network anomalies.  
- Enhance cybersecurity awareness and response by logging PoD attacks efficiently.  
- Implement a structured database for storing attack details and historical trends.  

## ✨ **Key Features** :

- **Real-Time Attack Detection** – Instantly detect and log Ping of Death (PoD) attacks on the network.
- **Interactive Dashboard** – Visualize attack trends, sources, and frequency with graphical charts.
- **IP & Port Tracking** – Monitor attack origins, destination IPs, and port numbers in real-time.

## 📂 **GitHub Repository (Source Code)** :

- [https://github.com/TOEYJIRAKID/Attack-Analytics-Dashboard](https://github.com/TOEYJIRAKID/Attack-Analytics-Dashboard)

## 🛠 **Ping of Death Attack Command** :

To simulate a Ping of Death attack and test your system's detection capabilities, use the following command:

```bash
sudo hping3 --icmp --flood --spoof <spoofed_ip> <target_ip>
```
This command floods the target with malformed ICMP packets, mimicking a Ping of Death attack, allowing you to test how well your system can detect and log the attack.

## 🏛️ **Database Structure** :

The system logs key attack parameters to help security teams analyze attack trends:

|  #  | Attribute        | Description                               | Data Type |
|----|----------------|-------------------------------------------|-----------|
| 1  | `src`         | Source IP of the attack                   | String    |
| 2  | `dst`         | Destination IP of the attack              | String    |
| 3  | `proto`       | Protocol used (ICMP)                      | String    |
| 4  | `attack_type` | Type of attack (Ping of Death)            | String    |
| 5  | `timestamp`   | Time when attack was detected             | String    |
| 6  | `ttl`         | Time-to-Live (TTL) value in the packet    | Integer   |
| 7  | `mac_src`     | MAC address of the attack source          | String    |
| 8  | `mac_dst`     | MAC address of the destination            | String    |

## 📃 Example JSON Data : 

The following is an example of the structured data logged by the Ping of Death Attack Analytics System:

```json
{
    "input_interface": "wlp2s0",
    "code": "0",
    "dst": "172.28.1.60",
    "attack_type": "Ping of Death",
    "src": "172.28.1.63",
    "type": "8",
    "ttl": "64",
    "tags": [],
    "hostname": "itd-Macmini8",
    "@timestamp": "2024-04-07T11:42:54.570Z",
    "len": "28",
    "prec": "0x00",
    "port": 35324,
    "proto": "ICMP",
    "@version": "1",
    "host": "172.18.0.1",
    "mac_dst": "dc:a4:ca:e9:a6:db",
    "mac_src": "70:9c:d1:84:a0:df",
    "tos": "0x00",
    "id": [
        "3608",
        "25180"
    ],
    "seq": "512",
    "timestamp": "Apr  7 18:42:54"
}
```

## 📽️ **Project Preview** :

![PoD Attack Analytics](https://github.com/user-attachments/assets/d8e4ab5f-3341-4735-8c74-4009c5559ad3)

THIS SOURCE IS FROM millersartin

# Hikvision-Vulnerability-Scanner-POC



This was created with educational and research purposes in mind. It is intended to serve as a tool to learn and understand security vulnerabilities in Hikvision IP Camera software versions 5.2.0 to 5.3.9 (Builds 140721 to 170109). The primary goal is to raise awareness about security risks in Internet of Things (IoT) devices while adhering to ethical and responsible use.

# Key Features:

   - CVE Reference: This POC is based on the official exploit release: https://www.exploit-db.com/exploits/44328
     
   - Demonstrates the presence of a known backdoor authentication key, "auth=YWRtaW46MTEK," intentionally left accessible by Hikvision support.

# Functionality:

- Showcase how the Hikvision backdoor can be exploited to bypass normal authentication

# Disclaimer:

This repository is designed for educational and research purposes only. It is not intended for any malicious activities or unauthorized access. Always ensure that you have proper authorization or ownership of the devices being tested.

# Usage:

To conduct a vulnerability assessment:

- Insert the IP addresses of vulnerable Hikvision cameras into the "Server.txt" file.
- Execute the "main.py" script to identify and save vulnerable devices.

  

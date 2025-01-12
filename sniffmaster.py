# sniffmaster.py

# Banner
print("SniffMaster")
print("Developed by Hedley\n")

# Instructions for the user
instructions = """
# SniffMaster - Packet Sniffing Analyzer

**SniffMaster** is a basic packet sniffing tool developed by Hedley. It is designed to capture and analyze network packets, specifically focusing on ARP and IP packets. This tool is ideal for network monitoring and basic analysis of network traffic in real-time.

## Features

- **ARP Packet Detection**: The tool detects ARP packets, showing source and destination MAC addresses, IP addresses, and ARP opcodes.
- **IP Packet Detection**: It also detects IP packets, showing source and destination IP addresses.
- **Real-time Sniffing**: Continuously sniffs packets on a specified network interface.

## Requirements

- Python 3.x
- **Scapy** (Python library for network analysis)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sniffmaster.git
    cd sniffmaster
    ```

2. Install **Scapy**:
    - Install Scapy via `pip` (you may need to install in a virtual environment):
    ```bash
    pip install scapy
    ```

## Usage

1. Run the script with Python:
    ```bash
    python sniffmaster.py
    ```

2. You will be prompted to enter a **network interface** (e.g., `eth0` or `wlan0`). Ensure that you have the appropriate permissions to capture packets on the specified interface.

3. The tool will start sniffing packets on the specified network interface and display ARP and IP packet information.

"""

# Print the instructions to the terminal
print(instructions)

# Importing necessary modules
from scapy.all import sniff
from scapy.layers.l2 import ARP, Ether
import os

# Function to handle packet sniffing
def packet_callback(packet):
    if packet.haslayer(ARP):
        print("\n[+] ARP Packet Detected")
        print(f"Source MAC: {packet[Ether].src}")
        print(f"Destination MAC: {packet[Ether].dst}")
        print(f"ARP Opcode: {packet[ARP].op}")
        print(f"ARP Source IP: {packet[ARP].psrc}")
        print(f"ARP Destination IP: {packet[ARP].pdst}")
        print("-" * 50)

    # You can add more packet types here like IP, TCP, etc.
    # For example:
    if packet.haslayer('IP'):
        print(f"\n[+] IP Packet Detected")
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")
        print("-" * 50)

# Start sniffing function
def start_sniffing(interface):
    print(f"Starting to sniff packets on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)

# Main function to get user input
def main():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ").strip()
    
    # Check if the interface exists
    if not os.path.exists(f"/sys/class/net/{interface}"):
        print("Error: Invalid network interface.")
        return
    
    start_sniffing(interface)

if __name__ == "__main__":
    main()

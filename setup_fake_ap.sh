#!/bin/bash

# Interfaccia in monitor mode
IFACE="wlan0mon"

# Stop services che potrebbero interferire
sudo systemctl stop NetworkManager
sudo systemctl stop wpa_supplicant

# Lancia hostapd
sudo hostapd ./hostapd.conf &

# Lancia dnsmasq
sudo dnsmasq -C ./dnsmasq.conf

# Abilita forwarding IP e iptables per NAT
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

echo "Access Point fasullo e DHCP attivi."

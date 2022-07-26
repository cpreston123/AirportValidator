import nmap


def validate(ip, port):
    scanner = nmap.PortScanner()
    res = scanner.scan(ip, str(port))

    if res['scan'][ip]['tcp'][port]['state'] == 'open':
        if res['scan'][ip]['tcp'][port]['product'] == 'Apple AirPort or Time Capsule admin':
            print('\nRequest DENIED')
            print(f'Open Apple AirPort or Time Capsule device has been detected on IP {ip}, Port {port}')
        else:
            print("\nRequest ACCEPTED")
            print(f'Port open, but no Apple AirPort or Time Capsule device has been detected on IP {ip}, Port {port}')
    else:
        print("\nRequest ACCEPTED")
        print('No open port found')



import socket
import multiprocessing.pool

def portscan(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))
        open_sockets.append("{}:{} is open" .format(ip, port))
        sock.close()
        return True
    except:
        return False
        

open_sockets = []
target_ips = ["192.168.1.{}" .format(i) for i in range(1,11)]
target_ports = range(1,65526)

def sockets():
    for ip in target_ips:
        for port in target_ports:
            yield ip, port

if __name__ == "__main__":
    with multiprocessing.pool.ThreadPool(10000) as executor:
        executor.starmap(portscan, sockets()) 

print(open_sockets)

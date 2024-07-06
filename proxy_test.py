import socks
import socket

def check_socks5_proxy(host, port, username=None, password=None):
    try:
        sock = socks.socksocket()
        sock.set_proxy(socks.SOCKS5, host, port, username=username, password=password)
        sock.connect(("httpbin.org", 80))
        sock.sendall(b"GET /ip HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
        response = sock.recv(4096)
        print(response.decode())
        sock.close()
        return True
    except Exception as e:
        print(f"Ошибка при подключении через SOCKS5 прокси {host}:{port}: {e}")
        return False

def parse_proxy(proxy_str):
    parts = proxy_str.split(':')
    if len(parts) == 4:
        ip, port, username, password = parts
        return ip, int(port), username, password
    return None

if __name__ == "__main__":
    # Список прокси-серверов в формате 'IP:PORT:USERNAME:PASSWORD'
    proxy_list = [
        'IP:порт:логин:пароль',
        # Добавьте другие прокси здесь
    ]

    for proxy_str in proxy_list:
        proxy = parse_proxy(proxy_str)
        if proxy:
            proxy_host, proxy_port, proxy_username, proxy_password = proxy
            if check_socks5_proxy(proxy_host, proxy_port, proxy_username, proxy_password):
                print(f"Успешное подключение через прокси {proxy_host}:{proxy_port}.")
            else:
                print(f"Не удалось подключиться через прокси {proxy_host}:{proxy_port}.")
        else:
            print(f"Неверный формат прокси: {proxy_str}")

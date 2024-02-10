import socket

class colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 9999))
        s.listen(1)
        print("Waiting for connexion...")
        conn, addr = s.accept()
        with conn:
            print(f"\n{colors.GREEN}Connexion established with {addr}{colors.RESET}\n")
            exit_code = 0
            while True:
                if exit_code == 0:
                    command = input(f"{colors.GREEN}->{colors.RESET} ").strip()
                else:
                    command = input(f"{colors.RED}->{colors.RESET} ").strip()
                if not command:
                    continue
                try:
                    conn.sendall(command.encode('utf-8'))
                    try:
                        exit_code = int(conn.recv(1024).decode('utf-8'))
                    except ValueError:
                        pass
                    output = conn.recv(1024).decode('utf-8')
                    print(output, end = '')
                except socket.error as e:
                    print(f"[{colors.RED}Error{colors.RESET}] {e}")
                if command.lower() == "exit":
                    break
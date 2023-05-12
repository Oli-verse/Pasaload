import threading
import random

balance = {
    'load1': 50,
    'load2': 150,
    'load3': 240,
    
}
def pasaload(sender, receiver, amount, lock):
    with lock:
        if balance[sender] >= amount:
            balance[sender] -= amount
            balance[receiver] += amount
            print(f"Pasaload from {sender} to {receiver} successful. New balance for {sender}: {balance[sender]}, New balance for {receiver}: {balance[receiver]}")
        else:
            print(f"Pasaload from {sender} to {receiver} failed due to insufficient balance.")

def request_pasaload(lock):
    sender = f"load{random.randint(1, 3)}"
    receiver = f"load{random.randint(1, 3)}"
    amount = random.randint(0, 50)
    pasaload(sender, receiver, amount, lock)

accounts_lock = threading.Lock()

threads = [threading.Thread(target=request_pasaload, args=(accounts_lock,)) for i in range(4)]

for t in threads:
    t.start()

for t in threads:
    t.join()
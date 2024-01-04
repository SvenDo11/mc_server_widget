#
# A simple widget tool to display current player in Minecraft server
# Author: SvenDo11
#
from threading import Thread
from time import sleep
from tkinter import Tk, Label

from config_manager import ConfigManager
from server_socket import get_info


def window_main():
    root = Tk()
    root.overrideredirect(True)
    root.config(background="#282828")
    root.bind('<Escape>', lambda e: e.widget.destroy())
    wx = 1920 * 2 - 300
    wy = 50
    root.geometry('+%d+%d' % (wx, wy))
    config_manager = ConfigManager()
    n = len(config_manager.get("servers"))
    labels = []
    for i in range(n):
        label = Label(root, text=str(i), font=("Arial", 20), background='#282828', foreground='#ebdbb2')
        label.pack()
        labels.append(label)

    terminate = False

    def update_label():
        while not terminate:
            servers = config_manager.get("servers")
            for server, lbl in zip(servers, labels):
                txt = server["name"] + "    "
                info = get_info(server["ip"], server["port"])
                txt += f"{info['players']['online']}/{info['players']['max']}"
                lbl.config(text=txt)
            sleep(10)

    t = Thread(target=update_label)
    t.start()
    root.mainloop()
    terminate = True
    t.join()


if __name__ == '__main__':
    window_main()

import random
import PySimpleGUI as sg

def __main__():
    number = random.randint(1, 100)

    layout = [
        [sg.Text("Вгадай число від 1 до 100")],
        [sg.Input(key="guess")],
        [sg.Button("Вгадати")]
    ]
    window = sg.Window("Вгадай число", layout)

    while True:
        event, values = window.read()

        if event == "Вгадати":
            if int(values["guess"]) == number:
                window.close()
                print("Ви вгадали! Число було:", number)
                break
            else:
                if int(values["guess"]) < number:
                    window["guess"].update("Ваше число менше за загадане.")
                else:
                    window["guess"].update("Ваше число більше за загадане.")
        if event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    __main__()

import PySimpleGUI as sg
sg.theme("DarkBlue9")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                layout=[[sg.Text("FTI UNISKA",font=("Helvita",24))],
                        [sg.Text("FAKULTAS TEKNOLOGI INFORMASI",font=("Courier",18,"italic","bold","underline"))],
                        [sg.Text("UNISKA MAB BANJARMASIN")]],
                size=(430,200),
                font=("times", 18))
window()
window.close()
import PySimpleGUI as sg
sg.theme("DarkGreen4")  
sg.theme_text_color ("#FFFF00")
window = sg.Window(title ="Profile", 
                        layout = [[sg.Text("SELAMAT DATANG DI KELAS",font=("Arial",25, "italic", "bold", "underline"))],
                                [sg.Text("NPM       : 2210010455")],
                                [sg.Text("NAMA      : Alya Normaida")],
                                [sg.Text("Kelas     : 5M Reguler Banjarmasin")]
                                ],
                        size=(500,200),
                        font=("Times", 18))
window()
Window.close()
import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weather_data(location):
    url = f"https://www.google.com/search?q=weather+{location.replace(' ','')}"
    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)

    soup = bs(html.text, 'html.parser')

sg.theme('reddit')
image_col = sg.Column([[sg.Text(key='-IMAGE-', background_color='#FFFFFF')]])
info_col = sg.Column([
    [sg.Text('',key='-LOCATION-', font = 'Calibri 16', background_color='#FF0000', text_color='#FFFFFF', pad = 0, visible=False)],
    [sg.Text('',key='-TIME-', font = 'Calibri 16', background_color='#000000', text_color='#FFFFFF', pad = 0, visible=False)],
    [sg.Text('',key='-TEMP-', font = 'Calibri 16', background_color='#FFFFFF', text_color='#000000', pad = (0,10), justification='center', visible=False)]
    ])
layout = [
    [sg.Input(expand_x=True, key='-INPUT-'), sg.Button('Enter')],
    [image_col, info_col]
    ]

window = sg.Window('Weather', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Enter':
        get_weather_data(values['-INPUT-'])
        window['-LOCATION-'].update('test', visible = True)
        window['-TIME-'].update('test', visible = True)
        window['-TEMP-'].update('test', visible = True)
        window['-IMAGE-'].update()

        
window.close()
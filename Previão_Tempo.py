import requests
from PySimpleGUI import PySimpleGUI as sg
# layout
sg.theme('Reddit')
layout = [
    [sg.Text('Cidade'), sg.Input(key='cid'), sg.Button('OK'), sg.Button('Cancelar')],
    [sg.Text('Temperatura:'), sg.Text('', key='temp')],
    [sg.Text('O dia Hoje está:'), sg.Text('', key = 'desc')]

]

# Janela
janela = sg.Window('Previsão do Tempo', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == 'Cancelar':
        break
    if eventos == 'OK':
        cidade = valores ['cid']

# Previsão do tempo 
        API_KEY = "c885650bb5fce109ce45b05609104069"
        link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"

        requisicao = requests.get(link)
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic['weather'][0]['description']
        temperatura = requisicao_dic['main']['temp']
        janela['desc'].update(descricao)
        janela['temp'].update(temperatura)

janela.close()
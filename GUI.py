"""
Docstring for GUI
"""
import os
from nicegui import ui, app
from Single_Game import SingleGame as Game

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
pictures_path = os.path.join(parent_dir, 'Pictures')

app.add_static_files('/pictures', pictures_path)


class InputGUI:

    def __init__(self):
        self._player_points = 0
        self._opponent_points = 0
        self.layout()

    
    def start_round(self):
        
        if self._player_points < 7 and self._opponent_points < 7:
            self._round = Game()
            ui.notify('Runde hat begonnen!')
            self.update_ui()


    def layout(self):

        with ui.column().classes('w-full h-screen bg-green-900 p-8 items-center'):
            ui.label("Schnapsen 2026").style('font-family: "Times New Roman", serif; color: #FFFFFF; font-size: 300%; font-weight: 300%')
        
            ui.image('/pictures/Card_Back.png').classes('absolute top-80 right-80 w-36 shadow-2xl')
            ui.label("Stapel").classes('absolute top-[520px] right-80 w-36 text-center').style('font-family: "Times New Roman", serif; color: #FFFFFF; font-size: 150%; font-weight: 100')

            with ui.card().classes('absolute right-4 top-4 h-full w-64 bg-white/10 backdrop-blur-lg border-l border-white/20 p-6 shadow-2xl rounded-none'):
                ui.label("Spielstand").style('font-family: "Times New Roman", serif; color: white; font-size: 200%; font-weight: bold')
                ui.separator().classes('bg-white/30 my-4')
                ui.label("Spiele:").style('font-family: "Times New Roman", serif; color: white; font-size: 150%; font-weight: bold')
                ui.separator().classes('bg-white/30 my-1')
                ui.label('Spieler: {self._player_points}').style('font-family: "Times New Roman", serif; color: white; font-size: 100%; font-weight: bold')
                ui.label('Gegner: {self._opponent_points}').style('font-family: "Times New Roman", serif; color: white; font-size: 100%; font-weight: bold')
                ui.label(' ')
                ui.label(' ')
                ui.label(' ')
                ui.label("In diesem Spiel:").style('font-family: "Times New Roman", serif; color: white; font-size: 150%; font-weight: bold')
                ui.separator().classes('bg-white/30 my-1')
                ui.label('Spieler: {self._game._points._points_player}').style('font-family: "Times New Roman", serif; color: white; font-size: 100%; font-weight: bold')
                ui.label('Gegner: {self._game._points._points_opponent}').style('font-family: "Times New Roman", serif; color: white; font-size: 100%; font-weight: bold')


    

@ui.page('/')
def main_page():
    InputGUI()

ui.run(title='Schnapsen GUI', port=8080)
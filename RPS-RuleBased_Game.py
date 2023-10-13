#REROMA, JESSA DONNALYN M. | BSCS - 3

import tkinter as tk
from tkinter import ttk
import random

# Computer Value
computer_value = {
     "0": "Rock",
     "1": "Paper",
     "2": "Scissor"
}

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)
        
        # Create widgets :)
        self.setup_widgets()
        
    
    
    def setup_widgets(self):
        
        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)
        
        # If player selected rock
        def isrock():
            c_v = computer_value[str(random.randint(0, 2))]
            if c_v == "Rock":
                match_result = "Match Draw"
            elif c_v == "Scissor":
                match_result = "Player Wins!"
            else:
                match_result = "Computer Wins!"
            self.l4.config(text=match_result)
            self.l1.config(text="Rock")
            self.player_emoji.config(text="✊")
            self.l3.config(text=c_v)
            if c_v=="Paper":
                self.comp_emoji.config(text="🖐")
            elif c_v=="Scissor":
                self.comp_emoji.config(text="✌")
            else:
                self.comp_emoji.config(text="✊")

        # If player selected paper
        def ispaper():
            c_v = computer_value[str(random.randint(0, 2))]
            if c_v == "Paper":
                match_result = "Match Draw"
            elif c_v == "Scissor":
                match_result = "Computer Wins!"
            else:
                match_result = "Player Wins!"
            self.l4.config(text=match_result)
            self.l1.config(text="Paper")
            self.player_emoji.config(text="🖐")
            self.l3.config(text=c_v)
            
            if c_v=="Paper":
                self.comp_emoji.config(text="🖐")
            elif c_v=="Scissor":
                self.comp_emoji.config(text="✌")
            else:
                self.comp_emoji.config(text="✊")
            
        # If player selected scissor
        def isscissor():
            c_v = computer_value[str(random.randint(0, 2))]
            if c_v == "Rock":
                match_result = "Computer Wins!"
            elif c_v == "Scissor":
                match_result = "Match Draw"
            else:
                match_result = "Player Wins!"
            self.l4.config(text=match_result)
            self.l1.config(text="Scissor")
            self.player_emoji.config(text="✌")
            
            self.l3.config(text=c_v)
            if c_v=="Paper":
                self.comp_emoji.config(text="🖐")
            elif c_v=="Scissor":
                self.comp_emoji.config(text="✌")
            else:
                self.comp_emoji.config(text="✊")
            
            
            
        # Accentbutton
        self.rockbutton = ttk.Button(
            self.widgets_frame, text="Rock", style="Accent.TButton", command= isrock
        )
        self.rockbutton.grid(row=7, column=2, padx=5, pady=10, sticky="nsew")
        
        self.paperbutton = ttk.Button(
            self.widgets_frame, text="Paper", style="Accent.TButton", command= ispaper
        )
        self.paperbutton.grid(row=8, column=2, padx=5, pady=10, sticky="nsew")
        
        self.scissorsbutton = ttk.Button(
            self.widgets_frame, text="Scissors", style="Accent.TButton", command= isscissor
        )
        self.scissorsbutton.grid(row=9, column=2, padx=5, pady=10, sticky="nsew")
        
        
        # Label
        # self.label = ttk.Label(
        #     self.widgets_frame,
        #     text="RESULT HERE",
        #     justify="center",
        #     font=("-size", 15, "-weight", "bold"),
        # )
        # self.label.grid(row=1, column=0, pady=10, columnspan=2)
        
        self.l1 = ttk.Label(self.widgets_frame,text="", font=10,anchor="center",width=15) #PLAYER CHOICE
        self.l2 = ttk.Label(self.widgets_frame, text="VS",font=("-size", 15, "-weight", "bold"))
        self.l3 = ttk.Label(self.widgets_frame, text="", font=10,anchor="center",width=15) #COMPUTER CHOICE
        self.l4 = ttk.Label(self.widgets_frame,text="",font="normal 20 bold",width=20,borderwidth=2,relief="solid",anchor="center")
        self.l1.grid(row=2, column=0, pady=10, columnspan=1)
        self.l2.grid(row=1, column=2, pady=10, columnspan=1)
        self.l3.grid(row=2, column=4, pady=10, columnspan=2)
        self.l4.grid(row=2, column=2, pady=10, columnspan=1)
        
        #Player Label
        self.playerLabel = ttk.Label(self.widgets_frame, text="PLAYER",font=("-size", 15, "-weight", "bold"),width=15,anchor="center")
        self.computerLabel = ttk.Label(self.widgets_frame, text="COMPUTER",font=("-size", 15, "-weight", "bold"),width=15,anchor="center")
        self.playerLabel.grid(row=1, column=0, pady=10, columnspan=2)
        self.computerLabel.grid(row=1, column=4, pady=10, columnspan=2)
        
        #label emojis of RPS
        self.player_emoji = ttk.Label(self.widgets_frame, text="",font=("-size", 30, "-weight", "bold"),width=15,anchor="center")
        self.comp_emoji = ttk.Label(self.widgets_frame, text="",font=("-size", 30, "-weight", "bold"),width=15,anchor="center")
        
        self.player_emoji.grid(row=3, column=0, pady=10, columnspan=2)
        self.comp_emoji.grid(row=3, column=4, pady=10, columnspan=2)
        
        
      
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Rock Paper Scissor Game")

    #Theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)
    
    root.resizable(False,False)
    
    root.mainloop()
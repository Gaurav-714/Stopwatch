import tkinter as tk 

class Stopwatch(tk.Frame):

    def __init__(self, window = None):
        super().__init__(window)
        self.window = window
        self.new_time = ''
        self.running = False
        self.total_hrs = 0
        self.total_mins = 0
        self.total_secs = 0
        self.pack()
        self.features()


    def features(self):

        self.window.title("My Own Stopwatch")

        self.stopwatch_label = tk.Label(self, text = "00:00:00", height = 1, width = 7,
                background = '#0C0404', foreground = 'white', font = 'Algerian 50 bold')
        self.stopwatch_label.pack()

        self.start_button = tk.Button(self, text = "START", height = 1, width = 5, font = 'Algerian 15 bold',
                                      background = '#228B22', foreground = 'white', command = self.start)
        self.start_button.pack(side = tk.LEFT)

        self.stop_button = tk.Button(self, text = "STOP", height = 1, width = 5, font = 'Algerian 15 bold',
                                      background = '#FF2400', foreground = 'white', command = self.stop)
        self.stop_button.pack(side = tk.LEFT)

        self.reset_button = tk.Button(self, text = "RESET", height = 1, width = 5, font = 'Algerian 15 bold',
                                      background = '#FFAD01', foreground = 'white', command = self.reset)
        self.reset_button.pack(side = tk.LEFT)

        self.exit_button = tk.Button(self, text = "EXIT", height = 1, width = 5, font = 'Algerian 15 bold',
                                      background = '#0F52BA', foreground = 'white', command = self.window.quit)
        self.exit_button.pack(side = tk.LEFT)


    def start(self):
        if not self.running:
            self.stopwatch_label.after(1000) # 1000 Miliseconds = 1 Second
            self.change_time()
            self.running = True


    def stop(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.new_time)
            self.running = False


    def reset(self):
        if self.running:
            self.stop_button.after_cancel(self.new_time)
            self.running = False

        self.total_hrs, self.total_mins, self.total_secs = 0, 0, 0
        self.stopwatch_label.config(text = "00:00:00")


    def change_time(self):
        self.total_secs += 1

        if self.total_secs == 60:
            self.total_mins += 1
            self.total_secs = 0

        if self.total_mins == 60:
            self.total_hrs += 1
            self.total_mins = 0

        hrs_string = f"{self.total_hrs}" if self.total_hrs > 9 else f"0{self.total_hrs}"
        mins_string = f"{self.total_mins}" if self.total_mins > 9 else f"0{self.total_mins}"
        secs_string = f"{self.total_secs}" if self.total_secs > 9 else f"0{self.total_secs}"
        
        self.stopwatch_label.config(text=hrs_string + ":" + mins_string + ":" + secs_string)       
        self.new_time = self.stopwatch_label.after(1000,self.change_time)


root = tk.Tk()
obj = Stopwatch(window = root)
obj.mainloop()
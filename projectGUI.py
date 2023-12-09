from tkinter import *
import csv
from statistics import mean, median, mode

class Grades:
    """
    The purpose of this class is to take a list of students and their scores.
    After taking the list, it returns with a grade determined by the class average.
    After determining the grade, it assigns a letter grade to every student in the class.
    In addition the code provides the current mean, median, mode, and range for additional stats that a teacher might use
    """
    def __init__(self, window):
        """
        Creates the GUI that allows for you to add scores to the file, and then the finish button adds the grade to each student.
        """
        self.window = window
        self.score_list = [0]
        
        try:
            with open('data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        score = float(row[1])
                        self.score_list.append(score)
                    except ValueError:
                        pass
        except FileNotFoundError:
            pass
        
        self.label_name = Label(self.window, text="Name")
        self.label_name.grid(row=0, column=0, padx=(10, 5))
        
        self.entry_name = Entry(self.window)
        self.entry_name.grid(row=0, column=1, padx=(5, 10), pady=5)
        
        self.label_score = Label(self.window, text="Score")
        self.label_score.grid(row=1, column=0, padx=(10, 5), pady=5)
        
        self.entry_score = Entry(self.window)
        self.entry_score.grid(row=1, column=1, padx=(5, 10), pady=5)
        
        self.save_entry = Button(self.window, text="Add Score", command=self.add_score)
        self.save_entry.grid(row=2, column=0, columnspan=1, padx=(20,20), pady=5)
        
        self.final_grades = Button(self.window, text="Finish", command=self.finish)
        self.final_grades.grid(row=2, column=1, columnspan=2, pady=5)
        
        self.label_message = Label(self.window, text="Please enter Student Scores", pady=10)
        self.label_message.grid(row=3, column=0, columnspan=2)
        
        self.label_mean = Label(self.window, text="Mean", pady=10)
        self.label_mean.grid(row=4, column=0)
        self.current_mean = Label(self.window, text=f"Currently: {mean(self.score_list):.2f}")
        self.current_mean.grid(row=4, column=1, padx=(10, 5), pady=5)

        self.label_median = Label(self.window, text="Median", pady=10)
        self.label_median.grid(row=5, column=0)
        self.current_median = Label(self.window, text=f"Currently: {median(self.score_list):.2f}")
        self.current_median.grid(row=5, column=1, padx=(10, 5), pady=5)
        
        
        self.label_mode = Label(self.window, text="Mode", pady=10)
        self.label_mode.grid(row=6, column=0)
        self.current_mode = Label(self.window, text=f"Currently: {mode(self.score_list):.2f}")
        self.current_mode.grid(row=6, column=1, padx=(10, 5), pady=5)
        
        self.label_range = Label(self.window, text="Range", pady=10)
        self.label_range.grid(row=7, column=0)
        self.current_range = Label(self.window, text=f"Currently: {max(self.score_list) - min(self.score_list)}")
        self.current_range.grid(row=7, column=1, padx=(10, 5), pady=5)
        
        if 0 in self.score_list:
            self.score_list.pop(0)

    def add_score(self):
        """Adds the scores to the list and updates the list to display accurate values for the list"""
        name = self.entry_name.get().strip()
        score = self.entry_score.get().strip()
        
        if name and score:
            try:
                score = float(score)
                self.score_list.append(score)
                
                current_mean = mean(self.score_list)
                self.current_mean.config(text=f"Currently: {current_mean:.2f}")
                
                current_median = median(self.score_list)
                self.current_median.config(text=f"Currently: {current_median:.2f}")
                
                current_mode = mode(self.score_list)
                self.current_mode.config(text=f"Currently: {current_mode:.2f}")
                
                current_range = max(self.score_list) - min(self.score_list)
                self.current_range.config(text=f"Currently: {current_range:.2f}")
                
                with open('data.csv', 'a', newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, score])
                    self.label_message.config(text="Successfully added Score")
            except ValueError:
                self.label_message.config(text="Please enter a valid score")
        else:
            self.label_message.config(text="Please enter both a name and a score")
         
         
         
         
    def finish(self):
        """Takes all values saved in the CSV file and adds a letter grade to the end of each entry dependant on the average grade of all entries"""
        try:
            if self.score_list:
                try:
                    current_mean = mean(self.score_list)
                    grade_scale = {
                        'A': current_mean + 10,
                        'B': current_mean,
                        'C': current_mean - 10,
                        'D': current_mean - 20,
                        'F': current_mean - 30
                    }
                    assigned_grades = []
                    for score in self.score_list:
                        for letter, threshold in grade_scale.items():
                            if score >= threshold:
                                assigned_grades.append(letter)
                                break
                    
                            
                    with open('data.csv', mode='r', newline='') as file:
                        reader = csv.reader(file)
                        data = list(reader)
                        
                        for i, row in enumerate(data):
                            if i < len(self.score_list):
                                while len(row) < 3:
                                    row.append('')
                                row[2] = assigned_grades[i]
                            
                            
                    with open('data.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(data)
                    self.label_message.config(text="Grades successfully updated!")
                    
                    
                except FileNotFoundError:
                    self.label_message.config(text="Unable to find data file.")
            else:
                self.label_message.config(text="No scores to grade.")
        except ValueError:
            self.label_message.config(text='Something went wrong.')
        
        
        
        


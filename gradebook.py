import customtkinter

customtkinter.set_appearance_mode("drk")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

classListCounter = 0

def login():
    print("Test")

classList = {}

def createClass():
    global classListCounter
    classFrame = customtkinter.CTkFrame(master=frame)
    classFrameColumns = 0
    for i in range(5):
        gradeCategory = customtkinter.CTkEntry(master = classFrame, placeholder_text="Grade Category (optional)")
        grade = customtkinter.CTkEntry(master = classFrame, placeholder_text="Current Grade")
        gradeWeight = customtkinter.CTkEntry(master = classFrame, placeholder_text="Grade Weight")

        gradeCategory.grid(row = classFrameColumns, column = 0, padx = 5, pady = 10)
        grade.grid(row = classFrameColumns, column = 1, padx = 5, pady = 10)
        gradeWeight.grid(row = classFrameColumns, column = 2, padx = 5, pady = 10)
        
        classFrameColumns += 1
    classListCounter = classListCounter + 1
    classList[classListCounter] = classFrame
    classFrame.grid(row = 0, column = classListCounter,  padx = 10, pady = 10)
    


frame = customtkinter.CTkFrame(master=root)
frame.grid()

createClass()
createClass()
"""
label1 = customtkinter.CTkLabel(master=frame, text="Username:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your username")
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = customtkinter.CTkLabel(master=frame, text="Password:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter your password", show="*")
entry2.grid(row=1, column=1, padx=10, pady=10)

button = customtkinter.CTkButton(master=frame, text="Login")
button.grid(row=2, column=0, columnspan=2, pady=20)  # Spanning two columns
"""


root.mainloop()
import customtkinter
import json
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1920x1080")

data_file = "user_data.json"  # JSON file to save data

classListCounter = 0

classList = {}
classListArray = []

def load_data():
    #Load data from JSON file
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as f:
            data = json.load(f)
            for key, value in data.items():
                createClass() # Create a class for each value set in the JSON file
                classFrame = classList[classListCounter]  # Get the latest class frame
                #Set class name
                classNameEntry = classFrame.children["!ctkentry"]
                classNameEntry.insert(0, value["className"]) # Class name entry
                
                classIndex = classListCounter - 1 # Access previous index

                grades = value.get("grades", [])
                gradeCategories = value.get("gradeCategories", [])
                weights = value.get("weights", [])

                for i in range(max(len(grades), len(gradeCategories), len(weights))):
                    if i < len(classListArray[classIndex]):  # Ensure no out of bounds
                        entry_widgets = classListArray[classIndex][i + 1]
                        # Load category if present or insert empty string
                        category_value = gradeCategories[i] if i < len(gradeCategories) else ""
                        entry_widgets[0].insert(0, category_value)  # Enter grade category
                        
                        # Load grade if present or insert empty string
                        grade_value = grades[i] if i < len(grades) else ""
                        entry_widgets[1].insert(0, grade_value)  # Enter grade value from JSON
                        
                        # Load weight if present or insert empty string
                        weight_value = weights[i] if i < len(weights) else ""
                        entry_widgets[2].insert(0, weight_value)  # Enter weight value from JSON
    else:
        createClass()

def on_closing():
    #When the app is closed
    dataToSave = {}
    for i in range(classListCounter):
        classData = classListArray[i]
        className = classData[0]["className"].get() #Class name from 1st entry of JSON
        grades = [entry[1].get() for entry in classData[1:]] #Get the grades from entries of this class
        weights = [entry[2].get() for entry in classData[1:]] #Get weights from entries of this class
        gradeCategories = [entry[0].get() for entry in classData[1:]] #Get gradeCategories from entries of this class
        
        dataToSave[f"class_{i}"] = { # For this class in the dataToSave dictionary
            "className": className,
            "gradeCategories": gradeCategories,
            "grades": grades,
            "weights": weights
        }
    with open("user_data.json", "w") as f:
        json.dump(dataToSave, f)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def validate_number_input(char):
    #Validation function to allow only numbers.
    return (char.isdigit())  # Allow only digits

def createClass():
    global classListArray
    global classListCounter
    if classListCounter < 8:
        classArray = []
        classFrame = customtkinter.CTkFrame(master=classesFrame)
        className = customtkinter.CTkEntry(master=classFrame, placeholder_text="Class name", width = 100, font = ("Inter", 30, "bold"), justify="center")
        #Put className in classArray
        classArray.append({"className": className})
        #Header for different fields
        classGradeTypeHeader = customtkinter.CTkLabel(master=classFrame, text="Grade name (optional)" , font=("Inter Medium", 11))
        classGradeHeader = customtkinter.CTkLabel(master=classFrame, text="Grade", font=("Inter Medium", 11))
        classGradeWeightHeader = customtkinter.CTkLabel(master=classFrame, text="Grade weight\n(%)", font=("Inter Medium", 11))
        classFrameColumns = 0
        #Button to calculate average
        calculateAverageButton = customtkinter.CTkButton(master=classFrame, text="Calculate", text_color = "white",  font=("Inter Medium", 11),
                                        fg_color= "#97D8C3", hover_color = "#56B782", corner_radius = 5, width = 75,
                                        height = 30, command=lambda idx=classListCounter: calcClassGPA(idx, classAverage))
        #For loop for all entry fields
        for i in range(5):
            row_entries = []
            #Create them
            gradeCategory = customtkinter.CTkEntry(master = classFrame, font=("Inter Medium", 11), width = 100)
            grade = customtkinter.CTkEntry(master = classFrame, placeholder_text="Grade", width = 50,font=("Inter Medium", 11), validate="key", validatecommand=(root.register(validate_number_input), "%S")) #Makes sure input is a number only
            gradeWeight = customtkinter.CTkEntry(master = classFrame, placeholder_text="Weight", width = 50, font=("Inter Medium", 11), validate="key", validatecommand=(root.register(validate_number_input), "%S")) #Makes sure input is a number only

            #Add them to 2d array
            row_entries.append(gradeCategory)
            row_entries.append(grade)
            row_entries.append(gradeWeight)
            #add row_entries to entry_grid
            classArray.append(row_entries)

            #Put them on the screen
            gradeCategory.grid(row = classFrameColumns + 2, column = 0, padx = 5, pady = 7)
            grade.grid(row = classFrameColumns + 2, column = 1, padx = 5, pady = 7)
            gradeWeight.grid(row = classFrameColumns + 2, column = 2, padx = 5, pady = 7)
            
            #Increment column Amount(i)
            classFrameColumns += 1
        #Show class name entry  field
        className.grid(row = 0, column = 0, columnspan = 3, padx= 10, pady = 10, sticky="ew")
        #Show header for entry fields
        classGradeTypeHeader.grid(row = 1, column = 0, padx= 5, pady = 10)
        classGradeHeader.grid(row = 1, column = 1, padx= 5, pady = 10)
        classGradeWeightHeader.grid(row = 1, column = 2, padx= 5, pady = 10)
        #Show text for averages
        classAverageText = customtkinter.CTkLabel(master = classFrame, text = "Class Average:", font=("Inter Medium", 15))
        classAverage = customtkinter.CTkLabel(master = classFrame, text = "0.0", font=("Inter Medium", 15))
        classAverageText.grid(row = classFrameColumns + 3, column = 1, padx = 10, pady = 10)
        classAverage.grid(row = classFrameColumns + 3, column = 2, padx = 10, pady = 10)
        #Show button to calculate average
        calculateAverageButton.grid(row = classFrameColumns + 3, column = 0, padx = 10, pady = 20)
        #Put the 2d array of entry fields into a larger array
        classListArray.append(classArray)
        #Increment classList
        classListCounter = classListCounter + 1
        #put it in the array
        classList[classListCounter] = classFrame
        rowCounter = (classListCounter % 4)
        if rowCounter == 0:
            rowCounter = 4
        if classListCounter > 4:
            classFrame.grid(row = 1, column = rowCounter,  padx = 10, pady = 10)
        else:
            classFrame.grid(row = 0, column = rowCounter,  padx = 10, pady = 10)
    
def deleteClass():
    global classListCounter
    if classListCounter > 1:
        classList[classListCounter].destroy() # Remove last added class frame from screen
        classListCounter -= 1 #Decrement amount of classes
        classListArray.pop()  # Remove the last class entry data

#Class GPA for calculating total GPA
def calcClassGPANoText(classNumber):
    totalPoints = 0
    totalWeight = 0
    for i in range(5): #For each column
        for entry in classListArray[classNumber][1:]: # For each entry field in this class's columns
            grade = entry[1].get()
            weight = entry[2].get()
            if grade and weight:  # Check if both fields have values
                totalPoints += float(grade) * (float(weight) / 100)
                totalWeight += float(weight)
    if totalWeight > 0: # If there is weight
        gpa = totalPoints / (totalWeight / 100) #calculate gpa
        return gpa
    return 0.0

#Class GPA for updating text
def calcClassGPA(classNumber, classAverage):
    totalPoints = 0
    totalWeight = 0
    for i in range(5): #For each column
        for entry in classListArray[classNumber][1:]: # For each entry field in this class's columns
            grade = entry[1].get()
            weight = entry[2].get()
            if grade and weight:  # Check if both fields have values
                totalPoints += float(grade) * (float(weight) / 100)
                totalWeight += float(weight)
    if totalWeight > 0: # If there is weight
        gpa = totalPoints / (totalWeight / 100) #calculate gpa
        classAverage.configure(text = f"{gpa: .2f}") #commit it to the gpa text

classesFrame = customtkinter.CTkFrame(master=root)
classesFrame.pack()

load_data()

#add total GPA label
totalGPA = customtkinter.CTkLabel(master = root, text = "GPA unweighted: 0.0", text_color = "white",  font=("Inter Medium", 25),)
totalGPA.place(relx = .50, rely = .925, anchor = "s")

#Calculate total GPA button
def calcTotalGPA():
    global totalGPA
    totalPoints = 0.0
    for i in range(classListCounter):
        totalPoints += calcClassGPANoText(i)
    unweightedGPA = (totalPoints / classListCounter)
    totalGPA.configure(text = f"GPA unweighted: { unweightedGPA:.2f}") 

#add class button
addClassButton = customtkinter.CTkButton(master=root, text="Add", text_color = "white",  font=("Inter Medium", 11),
                                        fg_color= "#97D8C3", hover_color = "#56B782", corner_radius = 5, width = 75,
                                        height = 30, command = createClass)
addClassButton.place(relx=0.40, rely = .975, anchor = "s")

#Calculate total GPA button
totalGPAButton = customtkinter.CTkButton(master=root, text="Calculate GPA", text_color = "white",  font=("Inter Medium", 11),
                                        fg_color= "#68B3E3", hover_color = "#4A9DC6", corner_radius = 5, width = 75,
                                        height = 30, command = calcTotalGPA)
totalGPAButton.place(relx = .50, rely = .975, anchor = "s")
#delete class button 
deleteClassButton = customtkinter.CTkButton(master=root, text="Delete", text_color = "white",  font=("Inter Medium", 11),
                                        fg_color= "#FFB3B3", hover_color = "#FF6666", corner_radius = 5, width = 75,
                                        height = 30, command = deleteClass)
deleteClassButton.place(relx=0.60, rely = .975, anchor = "s")

#Hurray!
root.mainloop()
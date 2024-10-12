# GRADEBOOK
#### Video Demo:  <https://youtu.be/VmKcy3PQ7kQ>

## What does it do?
#### Well, the gradebook sounds exactly like what it is: it's a gradebook. It keeps track of grades, calculates averages, and calculates your total GPA. While most schools provide this, my school has recently stopped providing the ability to calculate the total average, and I have been doing it with spreadsheets, which was getting old. It was one of my first ideas for this project, and I think I will be able to use it in life quite a bit!

## Technologies used
#### I used Python for this project, as I thought that it would be easier to develop a GUI in Python compared to languages like Java, as well as the fact that I did not have much experience with Python previously and wanted to throw myself in the deep end of something I didn't know anything about. I also used a JSON file to store the data, which I had no idea how to do at the beginning, so I certainly learned a lot about looking stuff up on Google.

## Functionality
#### I have quite a handful of methods in my program, the largest of which is createClass(). It (obviously) creates a panel for a class to go into, including all of the entry text boxes, buttons, and labels. Other methods include loading and saving data, and calculating the different averages/GPA.

## Design Choices
#### I didn't have much of a super defined GUI heading in, and I'm pretty happy with how it turned out. The only thing I didn't implement was a weighted GPA, but I realized pretty early on that almost every school calculates it differently, so I didn't want to impose what my school did on others, so I just left that up to the user. Other design choices include setting the frame size to static so that proportions could stay the same and a color scheme, which I think turned out simple yet clean. It was not what I had intended, but it was easily implemented using customtkinter, and I wanted to focus on the logic before the appearance. My choice to max the grade type number to 5 was unintentional at first, but I'm almost glad I did. Having a changing number of rows for each class would have made the code incredibly hard to make (and likely even harder to read), and if you have more than 5 types of grades, then I think you should have a talk with your teacher, not with me. The same can be said for the max of 8 classes; if you have more than 8, I think you need a therapist. Another design choice I had was whether or not to have the averages save when the user closes the app. I ended up choosing not to because of how I saved data into a JSON file using mostly an array from createClass() as this would cause way too much trouble for me. While it would have been nice to have I also think it's kinda fun to see your grade after you hit the button everytime.

## Challenges
#### Almost all of my methods ended up being pretty difficult aside from maybe calculating the averages. createClass() was what I altered most, and keeping track of everything going on became a huge pain. Another bump in the road was the save and load methods, as I did not have experience in JSON, and it was quite difficult for me to understand why my errors were happening. It was quite rewarding when everything finally worked, though. Lastly, about halfway through the project, I finally realized I had to think through how I was going to calculate the grade, which I had not prepped for at all yet. I had to create new arrays and code, which threw me off a little bit. I also learned to write everything in pseudocode/English beforehand, as that would have made this project twice as quick.

## What do I wish I had done differently?
#### Well, this project took way longer than I had initially planned, so I probably should have worked more concisely. Another issue I have with it is optimization: I know that it is quite inefficient. While it does not impact performance as it is quite a small app with a max of 8 classes, if I were to scale something like this up, I would certainly look at that.

## Lessons
#### 1. As I previously mentioned, using pseudocode before coding.
#### 2. Planning out time for when to work. I thought I would have more time than I did, and I didn't set aside enough time to work on it, delaying the finished product.
#### 3. Learn (or at least introduce yourself) to all of the concepts you will be using beforehand, as being more prepared would have made this easier and I would have been more motivated to work on it.

## Thanks for reading! I hope you can get some use out of my program. :) See you around!

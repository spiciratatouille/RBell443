#CIS 443-75-4212
#Program 2
#Due: March 9, 2021 11:59PM
#Grading ID: P5279
#This program allows a teacher to enter test scores for students,
#calculate their mean score and letter grade, and displays a bar
#chart of letter grades earned (A-F)
import matplotlib.pyplot as plt
import seaborn as sns

#prompts user for number of students, number of test scores, and score values
def input_test_scores ():
    num = int(input('How many students? '))
    test_num = int(input('How many tests for each student? '))
    score = []
    for student in range(num):
        stu_list = []
        student = input("What is the student's name? ")
        stu_list.append(student)
        test_list = []
        for n in range(test_num):
            stu_list.append(float(input(f"Enter {student}'s score for Test {n+1}:")))
        score.append(test_list)
    return score

#summarizes test scores, matches them to a letter grade, and plots them onto a chart
def summarize_test_scores(score):
    test_num = len(score[0])-1
    mean = []
    for data in score:
        m = sum(data[1:])/test_num
        mean.append(m)
#matches a number grade to a letter grade        
    grades = []
    for x in mean:
        if x >= 90:
            grades.append('A')
        elif x >= 80 and x < 90:
            grades.append('B')
        elif x >= 70 and x < 80:
            grades.append('C')
        elif x >= 60 and x < 70:
            grades.append('D')
        elif x < 60:
            grades.append('F')
            
    sort_grades = sorted(grades)
    
    frequency = {}
    for i in sort_grades:
        if (i in frequency):
            frequency[i] += 1
        else: 
            frequency[i] = 1
            
    freq_list = list(frequency.values())
            

    
#creates plot and fills it with user data
    title = 'Student Grade Distribution'
    sns.set_style('whitegrid')
    axes = sns.barplot(x=sort_grades, y=freq_list, palette='bright')
    axes.set_title(title)
    axes.set(xlabel='Letter Grade', ylabel='Frequency')
    axes.set_ylim(top=max(freq_list) * 1.10)
    for bar, mean in zip(axes.patches, mean):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = " "
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
        
    print("\nSummary of Grades")
    print(frequency)

#calls the program to action
summarize_test_scores(input_test_scores())


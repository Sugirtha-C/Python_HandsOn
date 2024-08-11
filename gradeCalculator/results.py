students= [
        {
         "Name": "Bharathi",
         "Math": 95,
         "Science": 96,
         "English": 99,
         "History": 98,
         "Art": 87
         },

        {
            "Name": "Hari",
            "Math": 99,
            "Science": 99,
            "English": 56,
            "History": 62,
            "Art": 61

        },
        {
         "Name": "Raghuvaran",
         "Math": 99,
         "Science": 96,
         "English": 99,
         "History": 98,
         "Art": 87
        },
        {
            "Name": "Kalpana",
            "Math": 34,
            "Science": 56,
            "English": 45,
            "History": 39,
            "Art": 99

        },
        {
            "Name": "Swaminathan",
            "Math": 99,
            "Science": 99,
            "English": 99,
            "History": 78,
            "Art": 34
        },
        {
            "Name": "Radhika",
            "Math": 19,
            "Science": 20,
            "English": 32,
            "History": 29,
            "Art": 18
        },
        {
            "Name": "Gayathri",
            "Math": 32,
            "Science": 30,
            "English": 27,
            "History": 12,
            "Art": 7
        }
    ]

def calculate_average_score(students):

    average_scores=[]
    for student in students:
        scores=[student["Math"],student["English"],student["Science"],student["History"],student["Art"]]
        average_score=sum(scores)/len(scores)
        average_scores.append(average_score)

    return average_scores

students_average_scores=calculate_average_score(students)

print(students_average_scores)
def determine_grade(students_average_scores):

    grades=[]
    for average in students_average_scores:

        if average >= 90:
                grades.append("Grade A")
        elif average >= 80:
                grades.append("Grade B")
        elif average >= 70:
                grades.append("Grade C")
        elif average >= 60:
                grades.append("Grade D")
        else:
                grades.append("Grade F")

    return grades

final_grades=determine_grade(students_average_scores)
print(final_grades)

def determine_pass_fail(final_grades):

    results=[]

    for grade in final_grades:
        if grade == 'Grade F':
            results.append("Fail")
        else:
            results.append("Pass")

    return results

Final_results=determine_pass_fail(final_grades)
#print(Final_results)

for i,student in enumerate(students):
    print("===================================")
    print("Name:",student["Name"])
    print("Average Scores:" ,students_average_scores[i])
    print("Final_Grades:",final_grades[i])
    print("Results:",Final_results[i])
    print("=================================")




def get_grade(score):
    if score >= 50:
        return 'A'
    elif score >= 40:
        return 'B'
    elif score >= 30:
        return 'C'
    elif score >= 20:
        return 'D'
    else:
        return 'F'

def main():
    score = float(input("Enter the student's score: "))
    if score < 0 or score > 50:
        print("Invalid score! Please enter a score between 0 and 100.")
    else:
        grade = get_grade(score)
        print(f"The grade for a score of {score} is: {grade}")

if __name__ == "__main__":
    main()

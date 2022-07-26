import pandas as pd

if __name__ == '__main__':
    num_of_students = int(input('Enter number of students: '))
    num_of_tasks = int(input('Enter number of tasks: '))
    res = {}
    for s in range(0, num_of_students):
        num_of_student = int(input('Enter number for the ' + str(s) + ' student: '))
        marks = {}
        for task in range(0, num_of_tasks):
            marks['Task_' + str(task)] = int(
                input('Enter mark (0-10 only int values) for student_' + str(num_of_student) + ' for task_' + str(
                    task) + ': '))

            res['Student_' + str(num_of_student)] = marks

    print('Top 3 students: ' + str(sorted(res.items(), key=lambda x: sum(x[1].values()), reverse=True)[:3]))
    df = pd.DataFrame(res.values())
    tasks = dict(df.sum())
    print('Top 3 hardest tasks: ' + str(sorted(tasks.items(), key=lambda x: x[1])[:3]))

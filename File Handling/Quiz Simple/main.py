"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
questions = open('questions.txt', 'r')
questions_list = [question.strip() for question in questions.readlines()]
score = 0 

tot = len(questions_list)
# print(questions_list)


for question in questions_list:
   ques, ans = question.split('=') 
   ans_user = input(f"{ques}=") 

   if ans_user == ans:
      score += 1 

result_file = open("result.txt","w") 
result_file.write(f'Your final score is {score}/{tot}.')

result_file.close()
questions.close()


    



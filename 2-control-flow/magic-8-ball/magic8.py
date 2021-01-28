import random
name = 'David'
question = 'Is drinking a good habit?'
answer = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'Hmm, maybe', 'wtf, no']
random_number = random.randint(0, 10)
# print(random_number)
if not len(question) == 0:
  if len(name) == 0:
    print('Question: ' + question)
  else:
    print(name + ' asks: ' + question)
  print("Magic 8-Ball's answer: " + answer[random_number])
else:
  print("You haven't asked anything.")

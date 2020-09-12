# @TODO: Your code here

me = {"firstname" : "Garrett",
    "occupation" : "college-student",
    "age" : 21,
    "hobbies" : ["swimming","eating", "running", "watching-sports"],
    "wake-up" : {"Mon-Fri": 7, "Sat-Sun" : 9}}

print(f'Hello I am {me["firstname"]} and I am a {me["occupation"]}')
print(f'I have {len(me["hobbies"])} hobbies!')
print(f'On the weekend I get up at {me["wake-up"]["Sat-Sun"]}')



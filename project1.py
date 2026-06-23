#list of questions
#store the answers
#randomly pick the questions
#see if they are correct
#keep track of the score
#tell the user their score


import random #it will generate random questions

question_bank = {
    "Easy":
[
{"question":"Keyword to define function?","answer":"def","hint":"Starts with d"},
{"question":"Comment symbol in Python?","answer":"#","hint":"Single character"},
{"question":"File extension of Python?","answer":".py","hint":"Dot something"},
{"question":"Function to get input?","answer":"input","hint":"Starts with i"},
{"question":"Boolean values?","answer":"true false","hint":"Two values"},
{"question":"Output of 2**3?","answer":"8","hint":"Power"},
{"question":"Keyword to import module?","answer":"import","hint":"Starts with i"},
{"question":"Function to print output?","answer":"print","hint":"Starts with p"},
{"question":"Which loop repeats fixed times?","answer":"for","hint":"3 letters"},
{"question":"Data type for decimal values?","answer":"float","hint":"Starts with f"}
],

"Medium":
[
{"question":"Method to add item in list?","answer":"append","hint":"Starts with a"},
{"question":"Output of len('python')?","answer":"6","hint":"Count letters"},
{"question":"Convert string to integer?","answer":"int","hint":"3 letters"},
{"question":"Loop that continues until condition false?","answer":"while","hint":"Starts w"},
{"question":"Dictionary key-value separator?","answer":":","hint":"Symbol"},
{"question":"Which keyword creates class?","answer":"class","hint":"Starts c"},
{"question":"Method to remove spaces?","answer":"strip","hint":"Starts s"},
{"question":"Keyword to handle exceptions?","answer":"try","hint":"Starts t"},
{"question":"Method to make string lowercase?","answer":"lower","hint":"Starts l"},
{"question":"Which operator means AND?","answer":"and","hint":"Logical"}
],

"Hard":[
{"question":"Keyword to create generator?","answer":"yield","hint":"Starts y"},
{"question":"Library used for arrays in data science?","answer":"numpy","hint":"Starts n"},
{"question":"Method to read CSV in pandas?","answer":"read_csv","hint":"Starts read"},
{"question":"Testing framework widely used in Python?","answer":"pytest","hint":"You learned this"},
{"question":"Function used to mock in unittest?","answer":"patch","hint":"Starts p"},
{"question":"Database cursor execution method?","answer":"execute","hint":"Runs SQL"},
{"question":"Keyword for anonymous function?","answer":"lambda","hint":"Starts l"},
{"question":"Output type of range()?","answer":"range","hint":"Same name"},
{"question":"Function to open file?","answer":"open","hint":"Starts o"},
{"question":"Which structure uses FIFO?","answer":"queue","hint":"Data structure"}
]
}

Leaderboard=[]

def choose_level():
    while True:
        level = input(
            "\n Choose Difficulty"
            "(Easy/Medium/Hard):"
        )
        level= level.capitalize()
        
        if level in question_bank:
            return level
        print("Invalid Level")

def ask_questions(q):

    print("\n"+q["question"])
    use_hint= input("Need Hint? (y/n):")
    if use_hint=="y":
        print("Hint:", q["hint"])
    
    answer=(
        input("Your Answer:").lower().strip()
    )
    return answer == q["answer"].lower()

def update_score(score,streak):
    score+=10

    if streak>=3:
        print("🔥 Streak Bonus!")
        score+=5
    return score

def play_game():
    name=input("Enter your name:")
    level= choose_level()

    questions= random.sample(question_bank[level],5)

    score=0
    
    lives=3

    streak=0

    for q in questions:
        print(f"\n💓 Lives:{lives}")

        correct =ask_questions(q)
        
        if correct:
            print("✅ Correct")
            streak+=1
        
            score=(update_score(score,streak))
        else:
            print("❌ Wrong")

            print("Correct answer:", q["answer"])
            
            lives-=1

            streak=0
            
            if lives==0:
                print("\nGame Over!")
                break
    
    Leaderboard.append((name,score))
    
    print(f"\nFinal Score: {score}")

    print("\nLeaderboard")

    Leaderboard.sort(key=lambda x: x[1], reverse=True)

    print(f"\n🏆 Final Score: {score}")

    print("\n=== Leaderboard ===")

    for p,s in Leaderboard:

        print(p,"-",s)

if __name__ == "__main__":

    while True:
        play_game()

        again = input("\nPlay Again? (y/n):").lower()

        if again != "y":
            print("\nThanks for playing!")
            break


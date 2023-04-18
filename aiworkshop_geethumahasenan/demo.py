import pyttsx3

n = int(input("Enter a number: "))

dic = {
    1 : "ones",
    2 : "twos",
    3 : "threes",
    4 : "fours",
    5 : "fives",
    6 : "sixes",
    7 : "sevens",
    8 : "eights",
    9 : "nines",
    10 : "tens",
}

txt = ""
for i in range(1, 11):
    mul = i * n
    txt += str(i) + " " + dic[i] + " are " + str(mul) + "\n"

engine = pyttsx3.init()
engine.say(txt)
engine.runAndWait()
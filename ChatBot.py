import time

# ChatBot [By Weez] github.com/9hw

print("[ChatBot] Bot: What is your name?")
print("")
name = input("You: ")
print("")
print("[ChatBot] Bot: Hello", name)
time.sleep(1.5)
print("")
print("[ChatBot] Bot:", name, "What Now?\n_______________________\n1 - Tell Me a joke \n2 - Credits\n3 - Leave D:")
print("")
anr = input("[ChatBot] Bot: Enter Here: ")
if anr == "1":
    print("[ChatBot] Bot: Why did the gym close down?")
    time.sleep(3.5)
    print("[ChatBot] Bot: Because it didn't work out.")
    time.sleep(3.5)
    
elif anr == "2":
    print("[ChatBot] Bot: github.com/9hw")
    time.sleep(1)
    
elif anr == "3":
    print("[ChatBot] Bot: Leaving..")
    time.sleep(0.5)
    exit()
else:
    print("ChatBot] Bot: Fatal Error. If you believe this is wrong, contact github.com/9hw")
    time.sleep(1.5)


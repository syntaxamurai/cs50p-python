emoticon = "v_v"

def main():
    global emoticon
    say("Is anyone home?")
    emoticon = ":D"
    say("Oh, Hi there!")


def say(phrase):
    print(phrase + " " + emoticon)

main()
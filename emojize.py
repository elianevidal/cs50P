#pip install emoji is required
from emoji import emojize

def main():
    #get the message
    msg = input("Input:")

    print("Output: "+ translateemojis(msg))

def translateemojis(msg):
    #translate wvery peace of the message, so we can return all emojis translated
    message = ""
    for i in msg.split():
        emojed = emojize(i)
        message = message+" "+emojed

    return message

main()

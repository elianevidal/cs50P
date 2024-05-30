def main():
    message = input()
    print(translatemotis(message))


def translatemotis(msg):
    replacements = {
        ":)": "🙂",
        ":(": "🙁",
        "(:": "🙃",
        "XD": "😆",
        "XP": "😝",
        ":p": "😛",
        "$$": "🤑",
        "**": "🤩",
        "<3": "😍"
    }
    for i in replacements:
        msg = msg.replace(i,replacements[i])
    return msg
main()
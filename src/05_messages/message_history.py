from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


def main():
    history = []
    history.append(SystemMessage(content="You are a patient Python tutor."))
    history.append(HumanMessage(content="My name is Ava."))
    history.append(AIMessage(content="Hi Ava. What would you like to learn?"))

    print("Lesson: Message history")
    print("Stored messages:", len(history))
    for message in history:
        print(message.type + ":", message.content)
    print("This list is cleared when the program exits.")


if __name__ == "__main__":
    main()
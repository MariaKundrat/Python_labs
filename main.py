from writing_desk import WritingDesk

if __name__ == "__main__":
    writing_desks = [
        WritingDesk(),
        WritingDesk(4, "Yes", 200, 75, 130),
        WritingDesk.get_instance(),
        WritingDesk.get_instance()
    ]

    for writing_desk in writing_desks:
        print(writing_desk)

    str(writing_desks[2])

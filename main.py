"""Import all models"""
from models.writing_desk import WritingDesk
from models.coffee_table import CoffeeTable
from models.computer_desk import ComputerDesk
from models.kitchen_table import KitchenTable
from managers.desk_manager import DeskManager

if __name__ == "__main__":
    desk_manager = DeskManager()
    desk_list = [
        CoffeeTable("CoffeeTable small №1", 80, 100, 125, 2, 4),
        CoffeeTable(),
        WritingDesk("WritingDesk small №1", 70, 105, 145, 4, "Yes", 200, 100),
        WritingDesk(),
        ComputerDesk("ComputerDesk small №1", 85, 100, 155, 6, "Yes", 110),
        ComputerDesk(),
        KitchenTable("KitchenTable small №1", 105, 85, 265, "Iron", 150),
        KitchenTable()
    ]

    for desk in desk_list:
        desk_manager.add_desk(desk)

    for desk in desk_manager.desk_list:
        print(desk)

    print("\n" + "All desks with height greater than 75: ")
    for desk in desk_manager.find_all_tables_higher_than(75):
        print(f"{desk.name} {desk.height}")

    print("\n" + "All desks with length greater than 150: ")
    for desk in desk_manager.find_all_with_length_greater_than(150):
        print(f"{desk.name} {desk.length}")

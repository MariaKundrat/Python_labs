"""Import all models and managers"""
from models.writing_desk import WritingDesk
from models.coffee_table import CoffeeTable
from models.computer_desk import ComputerDesk
from models.kitchen_table import KitchenTable
from managers.desk_manager import DeskManager
from managers.desk_set_manager import DeskSetManager

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

    print("\n" + "Get item 0:")
    print(desk_manager[0])

    print("\n" + "Enumerate desks:")
    for index, desk in desk_manager.enumerate_desks():
        print(index, desk)

    print("\n" + "Dict(int):")
    for desk in desk_manager:
        print(desk.desk_dict(int))

    print("\n" + "Zipped list:")
    for get_desk_status, desk in desk_manager.zip_desk():
        print(f"{get_desk_status}, {desk}")

    print("\n" + "Height of desks:")
    for value in desk_manager.get_height_of_desks():
        print(f"{value}")

    print("\n" + "Set manager:")
    desk_set_manager = DeskSetManager(desk_manager)
    for desk_set in desk_set_manager:
        print(desk_set)

    print("\n" + "Desks higher than:")
    for key, value in desk_manager.desks_higher_than(35).items():
        print(f"{key}:{value}")

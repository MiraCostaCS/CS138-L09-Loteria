##### FUNCTION DEFINITIONS #####
def create_list_from_file(file_name):
    """Generates a cleaned list of items from the given file. Format of file should be number, item_name."""
    list = open(file_name).readlines()
    name_list = []
    for i in range(0, len(list)):
        temp = list[i].split(",")
        name_list.append(temp[1].strip())
    return name_list


##### MAIN PROGRAM #####
def main():
    # call function to make list of Loteria names

    # replace problematic names

    # call function to make tabla 10 times

    # call function to play game

    pass  # delete this when you put something else in main


if __name__ == "__main__":
    main()

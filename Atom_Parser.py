from os import system

class InvalidInput(Exception):
    pass

def atomCount(atomic_num, atomic_weight, complex=False):
    """Takes: (atomic number, atomic weight). Returns: proton count,
    electron count, neutron count, electron"""
    electron = int(atomic_num)
    electron_location = []

    if complex == False:
        limit = [2, 8, 8, 2]

        if atomic_num > 20:
            electron_location = "Too complex for 2-8-8-2"
        else:
            for lim in limit:
                if electron >= lim:
                    electron_location.append(lim)
                    electron -= lim
                else:
                    electron_location.append(electron)
                    electron = 0
            
        return(atomic_num, atomic_num, atomic_weight - atomic_num, electron_location)
    
    else:
        subshell_c = {
        "1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2,
        "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2,
        "4f": 14, "5d": 10, "6p": 6, "7s": 2, "5f": 14, "6d": 10,
        "7p": 6
        }

        small = {
        0: "⁰", 1: "¹", 2: "²", 3: "³", 4: "⁴",
        5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹",
        10: "¹⁰", 11: "¹¹", 12: "¹²", 13: "¹³", 14: "¹⁴"
        }



        for subshell in subshell_c:
            if subshell_c[subshell] <= electron:
                electron_location.append(f"{subshell}{small[subshell_c[subshell]]}")
                electron -= subshell_c[subshell]

            elif subshell_c[subshell] > electron and electron > 0:
                electron_location.append(f"{subshell}{small[electron]}")
                electron = 0

            elif electron < 1:
                break

        electron_location = "".join(electron_location)
    return(atomic_num, atomic_num, atomic_weight - atomic_num, electron_location)

def read(user_input):
    """Very basic thing, i didnt spend too much time one this.
    returns: complex(bool), atomic num(int), atomic weight(int)"""
    user_input = user_input.split()
    try:
        user_input[0], user_input[1] = int(user_input[0]), int(user_input[1])

    except (ValueError, IndexError):
        raise InvalidInput

    if len(user_input) == 2:
        complex = True
    else:
        if user_input[2].lower() == "true":
            complex = True
        else:
            complex = False
    
    return(user_input[0], user_input[1], complex)

if __name__ == "__main__":
    while True:
        system("cls")
        print("Enter spesifically as: 'atomic num, atomic weight, complex(True/False, defaults to True)")
        print("e.g.'13 27 True' is valid, '13 27 False' is also valid")
        print("")
        user_input = input(">>>:")

        try:
            pre_info = read(user_input)
        except InvalidInput:
            input("Invalid Input")
            continue
        
        info = atomCount(pre_info[0], pre_info[1], pre_info[2]) #num, weight, complex?
        input(f"Proton: {info[0]}, Electron: {info[1]}, Neutron: {info[2]}, Configuration: {info[3]}")
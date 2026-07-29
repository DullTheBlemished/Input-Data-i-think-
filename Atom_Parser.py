from os import system
# the exeption dictioanry is ai generated, im not a chemist or a physicst 
exceptions = {
    # --- d-Block Transition Metal Exceptions ---
    24: "1s²2s²2p⁶3s²3p⁶4s¹3d⁵",                  # Chromium (Cr)
    29: "1s²2s²2p⁶3s²3p⁶4s¹3d¹⁰",                 # Copper (Cu)
    41: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹4d⁴",          # Niobium (Nb)
    42: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹4d⁵",          # Molybdenum (Mo)
    44: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹4d⁷",          # Ruthenium (Ru)
    45: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹4d⁸",          # Rhodium (Rh)
    46: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s⁰4d¹⁰",         # Palladium (Pd)
    47: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s¹4d¹⁰",         # Silver (Ag)
    78: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s¹4f¹⁴5d⁹",  # Platinum (Pt)
    79: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s¹4f¹⁴5d¹⁰", # Gold (Au)

    # --- f-Block Lanthanides & Actinides Exceptions ---
    57: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²5d¹",      # Lanthanum (La)
    58: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹5d¹",   # Cerium (Ce)
    64: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f⁷5d¹",   # Gadolinium (Gd)
    89: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²6d¹", # Actinium (Ac)
    90: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²6d²", # Thorium (Th)
    91: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f²6d¹", # Protactinium (Pa)
    92: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f³6d¹", # Uranium (U)
    93: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f⁴6d¹", # Neptunium (Np)
    96: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f⁷6d¹", # Curium (Cm)
    103: "1s²2s²2p⁶3s²3p⁶4s²3d¹⁰4p⁶5s²4d¹⁰5p⁶6s²4f¹⁴5d¹⁰6p⁶7s²5f¹⁴6d¹" # Lawrencium (Lr)
}

class InvalidInput(Exception):
    pass

def atomCount(atomic_num, atomic_weight, complex=False, real = False):
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


        if real == False:
            for subshell in subshell_c:
                if subshell_c[subshell] <= electron:
                    electron_location.append(f"{subshell}{small[subshell_c[subshell]]}")
                    electron -= subshell_c[subshell]

                elif subshell_c[subshell] > electron and electron > 0:
                    electron_location.append(f"{subshell}{small[electron]}")
                    electron = 0

                elif electron < 1:
                    break

        elif atomic_num in exceptions and real == True:
            electron_location = exceptions[atomic_num]

        electron_location = "".join(electron_location)
    return(atomic_num, atomic_num, atomic_weight - atomic_num, electron_location)

def read(user_input):
    """Very basic thing, i didnt spend too much time one this.
    returns: complex(bool), atomic num(int), atomic weight(int)"""
    user_input = user_input.split()

    if "@" in user_input:
        user_input.remove("@")
        real = True
    else:
        real = False

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
    
    return(user_input[0], user_input[1], complex, real)

if __name__ == "__main__":
    while True:
        system("cls")
        print("Enter spesifically as: 'atomic num, atomic weight, complex(True/False, defaults to True)")
        print("e.g.'13 27 True' is valid, '13 27 False' is also valid")
        print("also put an @ in the input for 'real' electron config exeptions irl (the @ msut not be touching anything)")
        print("")
        user_input = input(">>>:")

        try:
            pre_info = read(user_input)
        except InvalidInput:
            input("Invalid Input")
            continue
        
        info = atomCount(pre_info[0], pre_info[1], pre_info[2], pre_info[3]) #num, weight, complex?
        input(f"Proton: {info[0]}, Electron: {info[1]}, Neutron: {info[2]}, Configuration: {info[3]}")

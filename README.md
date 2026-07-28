# Projects
1)BASE-2 BINARY CODE DECODER (V1)
The code takes advantage of the fact that a full padded byte has 8 characters, so all it is is a loop that takes 8 from the input, ``append()``s it onto a new, smaller list, and then a loop to check the position of each bit in the byte (if blocks, will improve) to decode the value of that byte and add it to the answer.

1.2)BASE-2 BINARY CODE DECODER (V2)
added the usage of ``chr()`` for string translation as well. -22/04/2026

1.3)BASE-2 BINARY DECODER + ENCODER (V3)
added the usage ``ord()`` and f-strings with ``:08b`` to also whip up a quick encode function, changed the layout to be more of a library as this is my final refactor and I may need to use a binary decoder in the future, also worth mentioning that all my binary decoder can only decode in byte format. -28/04/2026

2)ATOM PARSER
A basic program (the main focus is the code here not the UX, which is why the input validation is very basic and wrapped inside an ``if __name__ == "__main__":``) that takes the atomic number(int), atomic weight(int) and the user's choice for the complexity settings of the electron configuration(bool), where True (what it defaults to if no Boolean arg is given) means it returns the electron configuration with the full spfd notation, and False being the basic 2-8-8-2 (octet rule), if an element were to be detected to be AFTER calcium by the math inside the function, and the user tries to also pass in False for their choice of complexity, the function will simply return "Too complex for 2-8-8-2". The program at its core is a list of limits relevant to a specific unit and a greedy algorithm to shove in as MUCH atoms into the previous one before moving on to the next, in the case of 2-8-8-2 this limiter is a premade list that is always ``[2, 8, 8, 2]`` and a for loop on a new empty list that references the "limit list" for the greedy algo, if it can even be called one. The spfd notation is a bit harder, the limit list had to be changed to a dictionary where the key was the shell and subshell, and the value was the limit (e.g. ``{"1s": 2}``) then it uses it as both a limit reference and a position reference, running a for loop on the dictionary (all position are pre-orded already)

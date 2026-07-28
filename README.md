# Binary-Decoder
1)BASE-2 BINARY CODE DECODER (V1)
The code takes advantage of the fact that a full padded byte has 8 characters, so all it is is a loop that takes 8 from the input, ``append()``s it onto a new, smaller list, and then a loop to check the position of each bit in the byte (if blocks, will improve) to decode the value of that byte and add it to the answer.

2)BASE-2 BINARY CODE DECODER (V2)
added the usage of ``chr()`` for string translation as well. -22/04/2026

3)BASE-2 BINARY DECODER + ENCODER (V3)
added the usage ``ord()`` and f-strings with ``:08b`` to also whip up a quick encode function, changed the layout to be more of a library as this is my final refactor and I may need to use a binary decoder in the future, also worth mentioning that all my binary decoder can only decode in byte format. -28/04/2026

Luo Number Converter
Overview
This Python script is designed to convert numbers to their equivalent words in the Dholuo language, specifically for numbers ranging from 0 to 99. The script currently supports conversions for numbers from 0 to 99, with a plan to extend its capability up to 999 in the future.

How It Works
The script defines a function numbers_to_words(number) that takes an integer as input and returns the corresponding word in Dholuo.

Key Components:
onesAndTens List: This list contains Dholuo words for numbers from 1 to 19.
prefixes List: This list contains Dholuo prefixes used for forming numbers from 20 to 99.
Function Logic:
0: Returns "sufuri" for the number 0.
1-19: Directly maps numbers from 1 to 19 using the onesAndTens list.
20-99: Constructs words for numbers 20 to 99 by combining the word "piero" (which signifies a group of tens) with the appropriate element from onesAndTens and a corresponding suffix from the prefixes list.
Out of Range: If the input number is less than 0 or greater than 1000, the function returns "Number out of range".
Example Usage:
To convert a number to its Dholuo word equivalent, simply call the function with the desired number.
Known Issues:
The function currently only handles numbers from 0 to 99. It will return "Number out of range" for any input outside this range.
There is a logic error for numbers exactly equal to 100 or higher, as these cases are not yet handled properly.
Future Improvements:
Extend Range: The script is intended to be extended to support numbers up to 999.
Bug Fix: Address the logic issue for numbers exactly equal to 100 or above.
Installation
No installation is required. Simply copy the script and run it in a Python environment.
Contributing
If you'd like to contribute by extending the number range or fixing bugs, feel free to fork the repository and submit a pull request.

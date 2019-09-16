### declare the function that takes in a body of text names text, a pattern that we are checking called pattern for and an integer

````
declare a variable that is an empty list this wil be our final answer.

get the legnth of the given text and set it to a variable.

check if the pattern that was given is empty is  thats the case

	we will return None

initialize variables needed such as

the first letter of the pattern

a place holder for the pattern we're going to be checking

the index the we're checking

the length of the pattern given

the length of the pattern we're checking

iterate through the letters in the given body of text

	if the letter matches the start of the given pattern

		while the size of the the pattern we're checking is less then the size of the pattern passed in and the index is less then or equal to the text_length and the current_pattern_length plus index is less then or equal to text_length

		we will add the letter at the index we're cehcking plus the current pattern length

		we will also increase the current pattern length by 1

	if the pattern we're checking is the same as the patter passed in then

		appened the index to the final answer variable.

		reset the current pattern to an empty string with length 0
	else

		reset the current pattern to an empty string with length 0

	increment index by 1

	if the index is now greater than the length of the text

		if the integer passed in is 0

			we will return true if the answer list is not empty

		else if the interger passed in is 1

			we will return the first value in the list

		else if the integer passed in is 3

			we will return the answer list
````

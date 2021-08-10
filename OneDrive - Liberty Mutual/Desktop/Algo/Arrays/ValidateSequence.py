
# The Validate Subsequence Algorithm
# The prompt or problem statement: Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# A subsequence of an array is a set of numbers that aren’t necessarily adjacent in the array but that are in the same order as they appear in the array. For example these numbers
# [2, 3, 5]
# are a subsequence of the array:
# [1, 2, 3, 4, 5]
# Note that a single number in an array and the array itself are both valid subsequences of the array.
# A sample input (what goes into the argument): array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 2, -1, 10]
# A sample output (an example of what is supposed to come out of the algorithm process): true



# SOLUTION_1
def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)

# SOLUTION_2
def isValidSubsequence(array, sequence):
    seqIdx = 0
	for value in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == value:
			seqIdx += 1
	return seqIdx == len(sequence)
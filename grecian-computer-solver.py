#Grecian Computer Solver
#https://www.projectgeniusinc.com/grecian-computer-solution

import numpy as np

#Set static values and convert them to numpy arrays
FifthWheel =  np.array([[12,  2,  5, 10,  7, 16,  8,  7,  8,  8,  3,  4],
			[ 6,  3,  3, 14, 14, 21, 21,  9,  9,  4,  4,  6],
			[ 7,  8,  9, 10, 11, 12, 13, 14, 15,  4,  5,  6],
			[11, 14, 11, 14, 14, 11, 14, 11, 14, 11, 11, 14]])

FourthWheel = np.array([[12,  0,  6,  0, 10,  0, 10,  0,  1,  0,  9,  0],
                        [ 2 ,13,  9,  0, 17, 19,  3, 12,  3, 26,  6,  0],
                        [ 6,  0, 14, 12,  3,  8,  9,  0,  9, 20, 12,  3],
                        [ 7, 14, 11,  0,  8,  0, 16,  2,  7,  0,  9,  0]])

ThirdWheel =  np.array([[ 9,  0,  5,  0, 10,  0,  8,  0, 22,  0, 16,  0],
                        [12,  0, 21,  6, 15,  4,  9, 18, 11, 26, 14,  1],
                        [ 7,  8,  9, 13,  9,  7, 13, 21, 17,  4,  5,  0]])

SecondWheel = np.array([[ 9,  0, 12,  0,  4,  0,  7, 15,  0,  0, 14,  0],
                        [11,  0,  6, 17,  7,  3,  0,  6,  0, 11, 11,  6]])

FirstWheel =    np.array([ 7,  0, 15,  0,  8,  0,  3,  0,  6,  0, 10,  0], ndmin=2)

#array used for holding totals of each column of digits
SumArray = np.zeros(12)

#base array used to test against for solution
Solution =    np.array([42,42,42,42,42,42,42,42,42,42,42,42], ndmin=2)

#Function to rotate each wheel one time
def RotateWheel(Wheel):
	for i in range(len(Wheel)):
		Wheel[i] = np.roll(Wheel[i],1)
	return

#Iterate through every rotation of the wheels until a solution is found
for FourthWheelRotations in range(12):
	for ThirdWheelRotations in range(12):
		for SecondWheelRotations in range(12):
			for FirstWheelRotations in range(12):
				#Store all values in our SumArray before testing against the Solution array
				#positions will loop through all 12 columns of digits, storing each columns value in the SumArray
				#once all columns are equal to 42, then we know a solution has been found
				for positions in range(12):
					#Next block of code tests for zeros.  Zeros represent spaces / notches on the wheel
					#If zero is found, we move to the next wheel
					#First Digit
					if FirstWheel[0][positions] != 0:
						SumArray[positions] = FirstWheel[0][positions] + SumArray[positions]
					elif SecondWheel[1][positions] != 0:
						SumArray[positions] = SecondWheel[1][positions] + SumArray[positions]
					elif ThirdWheel[2][positions] != 0:
						SumArray[positions] = ThirdWheel[2][positions] + SumArray[positions]
					elif FourthWheel[3][positions] != 0:
						SumArray[positions] = FourthWheel[3][positions] + SumArray[positions]
					elif FifthWheel[3][positions] != 0:
						SumArray[positions] = FifthWheel[3][positions] + SumArray[positions]

					#Second Digit
					if SecondWheel[0][positions] != 0:
						SumArray[positions] = SecondWheel[0][positions] + SumArray[positions]
					elif ThirdWheel[1][positions] != 0:
						SumArray[positions] = ThirdWheel[1][positions] + SumArray[positions]
					elif FourthWheel[2][0] != 0:
						SumArray[positions] = FourthWheel[2][positions] + SumArray[positions] 
					elif FifthWheel[2][positions] != 0:
						SumArray[positions] = FifthWheel[2][positions] + SumArray[positions]

					#Third Digit
					if ThirdWheel[0][positions] != 0:
						SumArray[positions] = ThirdWheel[0][positions] + SumArray[positions] 
					elif FourthWheel[1][positions] != 0:
						SumArray[positions] = FourthWheel[1][positions] + SumArray[positions] 
					elif FifthWheel[1][positions] != 0:
						SumArray[positions] = FifthWheel[1][positions] + SumArray[positions]

					#Fourth Digit
					if FourthWheel[0][positions] != 0:
						SumArray[positions] = FourthWheel[0][positions] + SumArray[positions] 
					elif FifthWheel[0][positions] != 0:
						SumArray[positions] = FifthWheel[0][positions] + SumArray[positions] 

					#All four digits above must add up to the solution of 42	
					#Test if a solution has been found
					if (SumArray==Solution).all():
						print('Solution Found  -- Zeros represent spaces/notches on wheels')
						print('                -- Line up each wheel so columns match the order below.\n')
						print('First Wheel:')
						print('\n'.join('{}: {}'.format(*k) for k in enumerate(FirstWheel)))
						print('\nSecond Wheel:')
						print('\n'.join('{}: {}'.format(*k) for k in enumerate(SecondWheel)))
						print('\nThird Wheel:')
						print('\n'.join('{}: {}'.format(*k) for k in enumerate(ThirdWheel)))
						print('\nFourth Wheel:')
						print('\n'.join('{}: {}'.format(*k) for k in enumerate(FourthWheel)))
						print('\nFifth Wheel:')
						print('\n'.join('{}: {}'.format(*k) for k in enumerate(FifthWheel)))
				
				#Solution Not found so reset our SumArray and rotate wheels one turn
				SumArray = np.zeros(12)
				RotateWheel(FirstWheel)
			RotateWheel(SecondWheel)
		RotateWheel(ThirdWheel)
	RotateWheel(FourthWheel)

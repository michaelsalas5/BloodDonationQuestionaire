#this program determines if a user is eligible to donate blood
#ask the user if they would like to donate blood
donation = 'yes'
while donation == 'yes':
    donation = input('Do you want to donate blood?(type yes or no): ')
    if donation == 'yes':
        print('Fill out the eligibility criteria')
#ask user weight, if over 110 they are eligible
        weight = int(input('Enter your weight: '))
        if weight < 110:
            print('You arent eligible to donate blood.')
        else:
#ask user age, if 17 or over they can donate
            age = int(input('How old are you?: '))
            if age < 17:
                print('You arent eligible to donate blood.')
            else:
#ask user for systolic blood pressure, if between 90 - 180 they can donate
                systolic = int(input('Enter your systolic blood pressure: '))
                if systolic < 90 or systolic > 180:
                    print('You arent eligible to donate blood.')
                else:
#ask user for diastolic blood pressure, if between 50 - 100 they can donate
                    diastolic = int(input('Enter your diastolic blood pressure: '))
                    if 50 > diastolic or diastolic > 100:
                        print('You arent eligible to donate blood.')
                    else:
#if user meets all requirements print that they are able to donate blood
                        print('You meet the criteria to donate blood!')
#ask user if they want to donate again
                        donation = input('Would you like to donate again?(enter yes or no): ')

    
            
    

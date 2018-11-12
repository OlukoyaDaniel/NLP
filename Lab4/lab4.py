from unnormalized import logistic_classifier as uLRC
from unnormalized import naive_classifier as uNBC
from normalized import logistic_classifier as nLRC
from normalized import naive_classifier as nNBC

def main():
    classifier=str(input('What classifier type would you like to use (nb/lr)? '))
    version=str(input('What version would you like to use (n/u)? '))
    testfile=str(input('Enter the test file name? '))

    if (classifier=='nb'):
        if (version=='n'):
            print('Please wait for a moment...')
            nNBC(testfile)
            print('---------------------------------------------------')
            print('Done, please check the results file')

        elif (version=='u'):
            print('Please wait for a moment...')
            uNBC(testfile)
            print('---------------------------------------------------')
            print('Done, please check the results file')

        else:
            print("Enter valid version")


    elif (classifier=='lr'):
        if (version=='n'):
            print('Please wait for a moment...')
            nLRC(testfile)
            print('---------------------------------------------------')
            print('Done, please check the results file')

        elif (version=='u'):
            print('Please wait for a moment...')
            uLRC(testfile)
            print('---------------------------------------------------')
            print('Done, please check the results file')

        else:
            print("Enter valid version")


    else:
        print("Enter valid classifier type")

main()

#
#Python: 3
#
#authoer: reagan leon
#
#
#Purpose: tech academy - python , creating our first program together.
#demonstrating how to pass variables from function to function
#while producing a functional game.
#
#
#

def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)
    


def get_info(f_name,l_name,age,gender):
    print("My name is {0} {1}. I am a {2} year old {3}.".format(f_name,l_name,age,gender))



if __name__ == "__main__":
    start()
    

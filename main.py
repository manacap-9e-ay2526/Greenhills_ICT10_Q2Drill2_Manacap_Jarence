# Set Operators
from pyscript import display, document


def add_member(e):
    document.getElementById('output').innerHTML = ' '

    # Gets the First and Last Name Inputted
    first_name = document.getElementById('firstName').value
    last_name = document.getElementById('lastName').value

    candidate_name = first_name + ' ' + last_name

    # Predefines
    grade_7 = {'rivera victoria', 'lim reuben', 'manalo antonio', 'manapat juan', 'dannug lucas'}
    grade_8 = {'macachor reign', 'ukwatte hans', 'perez dan', 'segura kirche', 'coronado chelsea'}
    grade_9 = {'daclan elaina', 'kim na yeon', 'manabat kristine', 'cuenca arkin', 'briones zangief'}
    grade_10 = {'visorde cedric', 'calaca mohammad', 'estrada lara', 'rigodon cassiopeia', 'eugenio miiska'}

    # Create a set
    new_member = {candidate_name}

    # Combine sets using the set union operator
    combination_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member

    # Get the total number of members
    total_members = len(combination_set)

    # Formatting
    output_message = f'Total Number of Members: {total_members} <br> Full List of All Members: {combination_set}'

    # Displays the output
    display(output_message, target='output')
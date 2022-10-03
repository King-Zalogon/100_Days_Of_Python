import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
list_of_states = data.state.tolist()

state_name = turtle.Turtle()
state_name.pu()
state_name.hideturtle()

amount_guessed = 0
game_on = True
states_guessed = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

while game_on:

    if answer_state == 'Quit':
        game_on = False

    elif answer_state in list_of_states and answer_state not in states_guessed:
        i = list_of_states.index(answer_state)
        state_name.goto(data['x'][i], data['y'][i])
        state_name.write(f"{data['state'][i]}", False, 'center')
        states_guessed.append(data['state'][i])
        amount_guessed += 1
        answer_state = screen.textinput(title=f"{amount_guessed}/50 - Guess the State",
                                        prompt="What's another state's name?").capitalize()

    else:
        answer_state = screen.textinput(title=f"{amount_guessed}/50 - Guess the State",
                                        prompt="What's another state's name?").capitalize()

#print(states_guessed)

turtle.mainloop()

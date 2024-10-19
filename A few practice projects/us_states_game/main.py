import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

'''Code to get x,y coordinates for each state'''
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

'''US STATES GAME'''
state_data = pandas.read_csv("./50_states.csv")
all_states = state_data.state.to_list()
correct_answers = []
# missed_answers = []
count = 0
game_is_on = True
while game_is_on:
    state_answer = screen.textinput(title=f'{count}/50 States Correct', prompt="What's another state's name?")
    state_answer = state_answer.title()
    if state_answer == "Exit":  # IF PLAYER EXITS THE GAME, SAVE THE MISSED ANSWERS TO A CSV
        game_is_on = False
        # for answer in all_states:
        #     if answer not in correct_answers:
        #         missed_answers.append(answer)
        missed_answers = [answer for answer in all_states if answer not in correct_answers]
        missed_dict = {
            "missed states": missed_answers
        }
        missed_states_data = pandas.DataFrame(missed_dict)
        missed_states_data.to_csv("missed_states.csv")

    state_row = state_data[state_data.state == state_answer]
    if state_row.empty:  # If the input is not a state
        continue
    state = state_row['state']
    state_str = state.to_string(index=False)
    x = int(state_row.x.to_string(index=False))
    y = int(state_row.y.to_string(index=False))

    if state_answer == state_str:
        correct_answers.append(state_answer)
        count += 1
        screen.tracer(0)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.write(state_str, align='center', font=('Arial', 8, 'normal'))
        screen.update()
    else:
        continue

screen.exitonclick()

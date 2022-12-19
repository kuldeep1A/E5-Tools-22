import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def onto_the_map(state, x, y):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    # state_name.speed(0.9)
    t.goto(x, y)
    t.write(f"{state}", align="center", font=("Arial", 8, "normal"))


guessed_states = []
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # Using List Comprehension
        missing_state = [state for state in all_state if state not in guessed_states]
        # missing_state = []
        # for state in all_state:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        onto_the_map(state=state_data.state.item(), x=int(state_data.x), y=int(state_data.y))



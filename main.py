import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()

correct_states = []
game_is_on = True
data = pandas.read_csv("50_states.csv")
state_names_list = data["state"].to_list()

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's the state name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_names_list:
        correct_states.append(answer_state)
        state_names_list.remove(answer_state)
        city = data[data.state == answer_state]
        text.penup()
        text.setpos(int(city.x), int(city.y))
        text.write(f"{answer_state.title()}")

print(state_names_list)
df = pandas.DataFrame(state_names_list)
df.to_csv("states to learn.csv")


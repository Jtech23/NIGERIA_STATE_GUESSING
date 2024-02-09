import turtle
import pandas

# states_dict = {
#     "states": ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River",
#                "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina",
#                "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau",
#                "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara", "Abuja"],
#
#     "X": [-56.0, 185.0, -39.0, -85.0, 47.0, -129.0, 2.0, 226.0, -11.0, -132.0, -32.0, -137.0, -164.0,
#           -61.0, 125.0, -83.0, 41.0, -40.0, -9.0, -59.0, -219.0, -106.0, -186.0, -248.0, -33.0, -148.0,
#           -271.0, -161.0, -204.0, -255.0, 40.0, -93.0, -168.0, 96.0, 136.0, -113.0, -74.0],
#
#     "Y": [-172.0, 17.0, -206.0, -139.0, 67.0, -213.0, -83.0, 153.0, -159.0, -178.0, -140.0, -123.0, -70.0,
#           -128.0, 63.0, -174.0, 157.0, 68.0, 136.0, 166.0, 141.0, -58.0, -25.0, -126.0, -26.0, 30.0, -99.0,
#           -96.0, -79.0, -46.0, 3.0, -205.0, 201.0, -60.0, 155.0, 154.0, -14.0]
# }


screen = turtle.Screen()
screen.title("Nigeria states game")
image = "ng-07.png.gif"
screen.addshape(image)
turtle.shape(image)

# states_data = pandas.DataFrame(states_dict)
# states_data.to_csv("Nigeria States.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("Nigeria States.csv")
states = data.states.to_list()
guessed_states = []
# missing_states = []
# print(states)

while len(guessed_states) < 50:
# for state in states:
    guess = screen.textinput(title=f"{len(guessed_states)}/37 states correct", prompt="Guess a state name").title()
    if guess == "Exit":
        missing_states = [stat for stat in states if stat not in guessed_states]
        # for stat in states:
        #     if stat not in guessed_states:
        #         missing_states.append(stat)
        missing_states_file = pandas.DataFrame(missing_states)
        missing_states_file.to_csv("Missing_states_to_learn.csv")
        break

    if guess in states and guess not in guessed_states:
        guessed_states.append(guess)
        T = turtle.Turtle(shape="circle")
        row = data[data.states == guess]
        T.pu()
        T.shapesize(0.1)
        T.goto(int(row.X), int(row.Y))
        T.write(guess)


# screen.mainloop()
screen.exitonclick()

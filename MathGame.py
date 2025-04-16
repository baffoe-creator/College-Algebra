import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import sys

def scatter_plot_game():
    print("\nScatter Plot Game")
    print("Identify the coordinates of the points on the graph.")

    # Difficulty selection
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        size = 10
    elif difficulty == "medium":
        size = 20
    else:  # hard
        size = 50

    # Generate random points
    num_points = random.randint(3, 7)
    x_coords = [random.randint(-size, size) for _ in range(num_points)]
    y_coords = [random.randint(-size, size) for _ in range(num_points)]

    # Create scatter plot
    plt.scatter(x_coords, y_coords, color='red')
    plt.title(f"Identify the coordinates of the {num_points} red points")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.xlim(-size-1, size+1)
    plt.ylim(-size-1, size+1)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

    # Get user answers
    score = 0
    for i in range(num_points):
        while True:
            try:
                answer = input(f"Enter coordinates for point {i+1} as x,y: ")
                x, y = map(int, answer.split(','))
                if (x, y) == (x_coords[i], y_coords[i]):
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("Incorrect. Try again.")
            except:
                print("Invalid format. Please enter as x,y (e.g., 3,-2)")

    print(f"\nGame over! Your score: {score}/{num_points}")

def algebra_game():
    print("\nAlgebra Practice Game")
    print("Solve the one-step and two-step equations.")

    # Difficulty selection
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty == "easy":
        max_num = 10
    elif difficulty == "medium":
        max_num = 20
    else:  # hard
        max_num = 50

    score = 0
    num_problems = 5

    for _ in range(num_problems):
        # Randomly choose between one-step and two-step problems
        problem_type = random.choice(['one-step', 'two-step'])

        if problem_type == 'one-step':
            # ax + b = c
            a = random.choice([1, 1, 1, 2, -1, -2])  # more chance for simple problems
            b = random.randint(-max_num, max_num)
            c = random.randint(-max_num, max_num)

            # Calculate correct answer
            x = (c - b) / a

            # Format equation
            if a == 1:
                eq = f"x + {b} = {c}"
            elif a == -1:
                eq = f"-x + {b} = {c}"
            else:
                eq = f"{a}x + {b} = {c}"

            print(f"\nSolve for x: {eq}")

        else:  # two-step
            # ax + b = cx + d
            a = random.randint(-3, 3)
            if a == 0:
                a = 1
            c = random.randint(-3, 3)
            if c == 0:
                c = 1
            b = random.randint(-max_num, max_num)
            d = random.randint(-max_num, max_num)

            # Calculate correct answer
            x = (d - b) / (a - c)

            # Format equation
            def term(coeff, var):
                if coeff == 1:
                    return var
                elif coeff == -1:
                    return f"-{var}"
                else:
                    return f"{coeff}{var}"

            left = f"{term(a, 'x')} + {b}" if b >= 0 else f"{term(a, 'x')} - {-b}"
            right = f"{term(c, 'x')} + {d}" if d >= 0 else f"{term(c, 'x')} - {-d}"
            eq = f"{left} = {right}"

            print(f"\nSolve for x: {eq}")

        # Get user answer
        while True:
            try:
                user_answer = float(input("x = "))
                if abs(user_answer - x) < 0.001:  # account for floating point precision
                    print("Correct!")
                    score += 1
                    break
                else:
                    print("Incorrect. Try again.")
                    break  # move to next problem even if wrong
            except:
                print("Please enter a number.")

    print(f"\nGame over! Your score: {score}/{num_problems}")

def projectile_game():
    print("\nProjectile Game")
    print("Adjust the parabola to clear the wall.")

    # Difficulty selection
    difficulty = input("Choose difficulty (easy/hard): ").lower()

    # Wall parameters
    wall_x = random.uniform(3, 7)
    wall_height = random.uniform(1, 4)
    wall_width = 0.2

    # Set up the figure
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.4)  # make room for sliders

    # Initial parabola parameters
    if difficulty == "easy":
        init_a = -0.5
        init_b = 3
        init_c = 0
    else:
        init_a = -1
        init_b = 5
        init_c = 0

    # Create the parabola
    x = np.linspace(0, 10, 500)
    y = init_a * x**2 + init_b * x + init_c
    line, = plt.plot(x, y, lw=2)

    # Draw the wall
    wall = plt.Rectangle((wall_x - wall_width/2, 0), wall_width, wall_height,
                         fc='red', ec='black')
    ax.add_patch(wall)

    plt.title('Adjust the parabola to clear the wall')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.grid(True)
    plt.xlim(0, 10)
    plt.ylim(0, 10)

    if difficulty == "easy":
        # Create sliders for a, b, c
        ax_a = plt.axes([0.25, 0.3, 0.65, 0.03])
        ax_b = plt.axes([0.25, 0.25, 0.65, 0.03])
        ax_c = plt.axes([0.25, 0.2, 0.65, 0.03])

        slider_a = Slider(ax_a, 'a', -2.0, 0.0, valinit=init_a)
        slider_b = Slider(ax_b, 'b', 0.0, 10.0, valinit=init_b)
        slider_c = Slider(ax_c, 'c', -5.0, 5.0, valinit=init_c)

        # Update function for sliders
        def update(val):
            a = slider_a.val
            b = slider_b.val
            c = slider_c.val
            y = a * x**2 + b * x + c
            line.set_ydata(y)
            fig.canvas.draw_idle()

        slider_a.on_changed(update)
        slider_b.on_changed(update)
        slider_c.on_changed(update)

        # Submit button
        submit_ax = plt.axes([0.8, 0.1, 0.1, 0.04])
        submit_button = Button(submit_ax, 'Submit', color='lightgoldenrodyellow')

        def submit(event):
            a = slider_a.val
            b = slider_b.val
            c = slider_c.val

            # Check if parabola clears the wall
            y_at_wall = a * wall_x**2 + b * wall_x + c
            if y_at_wall > wall_height:
                print("\nSuccess! You cleared the wall!")
            else:
                print("\nTry again! The parabola didn't clear the wall.")

            plt.close()

        submit_button.on_clicked(submit)

        plt.show()
    else:
        plt.show(block=False)

        # Get user input for a, b, c
        print("\nEnter the coefficients for the parabola (y = ax² + bx + c)")
        while True:
            try:
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                break
            except:
                print("Please enter numbers only.")

        # Check if parabola clears the wall
        y_at_wall = a * wall_x**2 + b * wall_x + c
        if y_at_wall > wall_height:
            print("\nSuccess! You cleared the wall!")
        else:
            print("\nTry again! The parabola didn't clear the wall.")

        # Plot the user's parabola
        plt.cla()
        y_user = a * x**2 + b * x + c
        plt.plot(x, y_user, lw=2, color='green')
        ax.add_patch(wall)
        plt.title('Your parabola attempt')
        plt.xlabel('Distance')
        plt.ylabel('Height')
        plt.grid(True)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.show()

def main():
    print("Welcome to Math Games!")

    while True:
        print("\nChoose a game:")
        print("1. Scatter Plot Game")
        print("2. Algebra Practice Game")
        print("3. Projectile Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            scatter_plot_game()
        elif choice == '2':
            algebra_game()
        elif choice == '3':
            projectile_game()
        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()

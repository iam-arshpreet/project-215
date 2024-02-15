import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Circle:
    def __init__(self, position, velocity, radius):
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.radius = radius

    def move(self, dt):
        self.position += self.velocity * dt

    def check_collision(self, other_circle):
        distance = np.linalg.norm(self.position - other_circle.position)
        return distance < self.radius + other_circle.radius

class Simulation:
    def __init__(self, num_circles, time_steps, dt):
        self.circles = []
        for _ in range(num_circles):
            position = np.random.rand(2) * 10  # Random initial position (within a 10x10 box)
            velocity = np.random.rand(2) - 0.5  # Random initial velocity
            radius = np.random.uniform(0.2, 0.5)  # Random radius
            self.circles.append(Circle(position, velocity, radius))
        self.time_steps = time_steps
        self.dt = dt

    def update(self):
        for _ in range(self.time_steps):
            for circle in self.circles:
                circle.move(self.dt)
                for other_circle in self.circles:
                    if circle != other_circle and circle.check_collision(other_circle):
                        # Handle collision (e.g., change color, bounce, etc.)
                        pass

    def animate(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        circles_plot = [plt.Circle(circle.position, circle.radius, fill=False) for circle in self.circles]

        def init():
            for circle_plot in circles_plot:
                ax.add_patch(circle_plot)
            return circles_plot

        def update(frame):
            self.update()
            for i, circle_plot in enumerate(circles_plot):
                circle_plot.center = self.circles[i].position
            return circles_plot

        ani = FuncAnimation(fig, update, frames=self.time_steps, init_func=init, blit=True)
        plt.show()

# Example usage
simulation = Simulation(num_circles=5, time_steps=100, dt=0.01)
simulation.animate()
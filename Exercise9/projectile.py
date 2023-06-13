# At a barrel height of 1m, after a horizontal distance of 0.5m, an elevation of
# 80 degrees, and an initial velocity of 44 m/s, what is the height of the
# projectile?

# imported math
import math

# created variables for each of the numbers given in the question
barrel_height = 1
distance_travelled = 0.5
initial_volocity = 44
acceleration = 9.81
#  Worked out theta using given formula
theta = 80 * (math.pi/180)

y = barrel_height + distance_travelled * math.tan(theta) - \
    (acceleration * distance_travelled ** 2) / (2*((initial_volocity * math.cos(theta))**2))

print('Projectile is ' + str(y) + ' m')

# No idea what 0+ represents?! in formula given

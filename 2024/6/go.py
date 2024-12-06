import os
import sys
import time
from itertools import cycle

def parse_file(file):
    with open(file, 'r') as f:
        return [list(line.rstrip()) for line in f]  # Convert lines to list of characters

file_name = sys.argv[1] if len(sys.argv) >= 2 else 'input.txt'
lines = parse_file(file_name)

mx = len(lines[0])  # Max x (width)
my = len(lines)     # Max y (height)

directions = ['^', '>', 'v', '<']

def next_direction(current):
    index = directions.index(current)
    return directions[(index + 1) % len(directions)]

def move(x, y, direction):
    if direction   == '^' and y - 1 >= 0: return (x, y - 1)
    elif direction == 'v' and y + 1 < my: return (x, y + 1)
    elif direction == '>' and x + 1 < mx: return (x + 1, y)
    elif direction == '<' and x - 1 >= 0: return (x - 1, y)
    else: return (-1, -1)

def show_square(x, y):
    if 0 <= x < mx and 0 <= y < my:
        return lines[y][x]
    return None

def display_map(lines, guard, visited_positions, move_history):
    sys.stdout.write("\033[H\033[J") # Clear the screen (ANSI escape)

    display_lines = [row[:] for row in lines]  # Deep copy

    # Mark positions based on move history
    for (x, y), moves in move_history.items():
        if 'vertical' in moves and 'horizontal' in moves:
            display_lines[y][x] = '+'
        elif 'vertical' in moves:
            display_lines[y][x] = '|'
        elif 'horizontal' in moves:
            display_lines[y][x] = '-'

    # Mark guard's current position
    gx, gy = guard['x'], guard['y']
    display_lines[gy][gx] = guard['direction']

    # Render the map
    sys.stdout.write("\n".join("".join(row) for row in display_lines) + "\n")
    sys.stdout.flush()

# Initialize guard
guard = None
for idx, row in enumerate(lines):
    if '^' in row:
        guard = {'x': row.index('^'), 'y': idx, 'direction': '^'}
        break
imm_guard = (guard['x'], guard['y'])

# Mark the starting position as visited in the map
lines = parse_file(file_name)
imm_lines = tuple([list(row) for row in lines])
all_open_squares = {(x, y) for y, row in enumerate(lines) for x, char in enumerate(row) if char == '.'}

loop_count = 0
for x in range(mx):
    for y in range(my):
        lines = [list(row) for row in imm_lines]

        guard = {'x': imm_guard[0], 'y': imm_guard[1], 'direction': '^'}
        lines[guard['y']][guard['x']] = '*'

        # Initialize state
        total_moves = 0
        visited_positions = set([(guard['x'], guard['y'])])
        move_history = {}
        guard_states = set()
        stuck_counter = 0

        if lines[y][x] == '#':
            continue
        if guard['x'] == x and guard['y'] == y:
            continue
        else:
            lines[y][x] = 'O'

        while True:
            # time.sleep(0.001)
            # display_map(lines, guard, visited_positions, move_history)

            # Save the current guard state (position and direction)
            current_state = (guard['x'], guard['y'], guard['direction'])

            # Detect repeated states without progress
            if current_state in guard_states:
                stuck_counter += 1
                if stuck_counter > 10:  # Allow up to 10 repeated states before detecting a loop
                    loop_count += 1
                    # print("Detected a loop!", loop_count, x, y)
                    # display_map(lines, guard, visited_positions, move_history)
                    break
            else:
                stuck_counter = 0  # Reset the counter on new states
            guard_states.add(current_state)

            next_move = move(guard['x'], guard['y'], guard['direction'])

            if next_move == (-1, -1):
                # print("Out of bounds.")
                break

            # Get the type of square at the next position
            square = show_square(*next_move)
            if square == '#' or square == 'O':  # Wall
                guard['direction'] = next_direction(guard['direction'])
            elif square in ('.', '*'):  # Open path or revisited square
                prev_x, prev_y = guard['x'], guard['y']
                guard['x'], guard['y'] = next_move

                # Update move history
                if guard['x'] != prev_x:
                    move_history.setdefault((prev_x, prev_y), set()).add('horizontal')
                if guard['y'] != prev_y:
                    move_history.setdefault((prev_x, prev_y), set()).add('vertical')

                # Check if the move visits a new position
                if next_move not in visited_positions:
                    stuck_counter = 0  # Reset stuck counter on progress
                    visited_positions.add(next_move)
                    lines[guard['y']][guard['x']] = '*'  # Mark as visited
            else:
                print("Unhandled square type: '%s' at %s." % (square, next_move))
                break

            # Stop if all open squares have been visited
            if all_open_squares.issubset(visited_positions):
                print("All open squares visited. Stopping simulation.")
                break

            total_moves += 1

        # print("Total Moves: %d" % total_moves)
        # print("Visited Positions: %d" % len(visited_positions))

print("Loop Count: %d" % loop_count)


# for i in pypy pypy3 python3.10 python3.11
# for> do
# for> time $i go.py input.txt
# for> done
# Loop Count: 1933
# $i go.py input.txt  36.00s user 0.79s system 95% cpu 38.334 total
# Loop Count: 1933
# $i go.py input.txt  43.41s user 0.97s system 97% cpu 45.530 total
# Loop Count: 1933
# $i go.py input.txt  111.66s user 1.16s system 96% cpu 1:56.82 total
# Loop Count: 1933
# $i go.py input.txt  101.26s user 1.21s system 96% cpu 1:46.39 total 
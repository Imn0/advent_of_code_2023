import numpy as np
from enum import Enum


class return_vals(Enum):
    REMOVE = 0,
    SPLIT_V = 1,
    SPLIT_H = 2,
    OK = 3,


class Beams:
    def __init__(self):
        self.beams = []

    def SHINE(self):
        while len(self.beams) > 0:
            self.move()
            

    def move(self):
        for beam in self.beams:
            current = []
            r = beam.move()
            match r:
                case return_vals.REMOVE:
                    self.beams.remove(beam)
                case return_vals.SPLIT_V:
                    current.append(Beam(1, 0, beam.v_pos, beam.h_pos))
                    current.append(Beam(-1, 0, beam.v_pos, beam.h_pos))
                    self.beams.remove(beam)
                case return_vals.SPLIT_H:
                    current.append(Beam(0, 1, beam.v_pos, beam.h_pos))
                    current.append(Beam(0, -1, beam.v_pos, beam.h_pos))
                    self.beams.remove(beam)

            self.beams.extend(current)


class Beam:
    def __init__(self, v_speed, h_speed, v_pos=0, h_pos=0):
        self.h_speed = h_speed
        self.v_speed = v_speed
        self.h_pos = h_pos
        self.v_pos = v_pos

    def move(self) -> return_vals:
        global lines
        global grid
        global beam_history_grid



        self.h_pos += self.h_speed
        self.v_pos += self.v_speed

        if self.h_pos >= len(lines[0]) or self.v_pos >= len(lines):
            return return_vals.REMOVE
        if self.h_pos < 0 or self.v_pos < 0:
            return return_vals.REMOVE
        
        grid[self.v_pos][self.h_pos] = 1

        # no point in shining if its already been shined here
        if [self.v_speed, self.h_speed] in beam_history_grid[self.v_pos][self.h_pos]:
            return return_vals.REMOVE
        else:
            beam_history_grid[self.v_pos][self.h_pos].append(
                [self.v_speed, self.h_speed])

        if lines[self.v_pos][self.h_pos] == '|' and self.h_speed != 0:
            return return_vals.SPLIT_V
        if lines[self.v_pos][self.h_pos] == '-' and self.v_speed != 0:
            return return_vals.SPLIT_H

        if lines[self.v_pos][self.h_pos] == '/':
            t = self.h_speed
            self.h_speed = -self.v_speed
            self.v_speed = -t

        if lines[self.v_pos][self.h_pos] == '\\':
            t = self.h_speed
            self.h_speed = self.v_speed
            self.v_speed = t

        return return_vals.OK


with open('smol.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
grid = np.array([[0 for c in line] for line in lines])
beam_history_grid = ([[[] for c in line] for line in lines])


beams = Beams()
# start on the field outside the grid and move right into the grid
beams.beams.append(Beam(0, 1, 0, -1))
beams.SHINE()
print(np.sum(grid))

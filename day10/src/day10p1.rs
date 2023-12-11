use std::fs;

#[derive(Debug)]
enum Direction{
    UP,
    DOWN,
    LEFT,
    RIGHT,
}

fn main() {

    let file = fs::read_to_string("./input.txt").expect("no file");

    let matrix: Vec<Vec<char>> = file.lines().map(|line| line.chars().collect()).collect();

    let start_row = matrix.iter().position(|row| row.contains(&'S')).unwrap();
    let start_col = matrix[start_row].iter().position(|&c| c == 'S').unwrap();

    let start = (start_row, start_col);
    println!("start {:?}", start);
    let mut current_pos = (start.0 + 1 , start.1);
    let mut current_dir = Direction::DOWN;

    let mut total_steps = 1; // 1 coz we already moved down once

    while matrix[current_pos.0][current_pos.1] != 'S' {
        total_steps += 1;

        /*
        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
         */
        (current_dir, current_pos) = match(current_dir, matrix[current_pos.0][current_pos.1])  {
            (Direction::UP, '|') => (Direction::UP, (current_pos.0 - 1, current_pos.1)),
            (Direction::DOWN, '|') => (Direction::DOWN, (current_pos.0 + 1, current_pos.1)),

            (Direction::LEFT, '-') => (Direction::LEFT, (current_pos.0, current_pos.1 - 1)),
            (Direction::RIGHT, '-') => (Direction::RIGHT, (current_pos.0, current_pos.1 + 1)),

            (Direction::LEFT, 'L') => (Direction::UP, (current_pos.0 - 1, current_pos.1)),
            (Direction::DOWN, 'L') => (Direction::RIGHT, (current_pos.0, current_pos.1 + 1)),

            (Direction::RIGHT, 'J') => (Direction::UP, (current_pos.0 - 1, current_pos.1)),
            (Direction::DOWN, 'J') => (Direction::LEFT, (current_pos.0, current_pos.1 - 1)),

            (Direction::RIGHT, '7') => (Direction::DOWN, (current_pos.0 + 1, current_pos.1)),
            (Direction::UP, '7') => (Direction::LEFT, (current_pos.0, current_pos.1 - 1)),

            (Direction::LEFT, 'F') => (Direction::DOWN, (current_pos.0 + 1, current_pos.1)),
            (Direction::UP, 'F') => (Direction::RIGHT, (current_pos.0, current_pos.1 + 1)),


            _ => panic!("invalid input"),
        }
        
    }
    println!("{}", total_steps/2);

}

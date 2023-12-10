use std::fs;

#[derive(Debug)]
enum Direction {
    UP,
    DOWN,
    LEFT,
    RIGHT,
}

fn fill_outer_connected(matrix: &mut Vec<Vec<char>>) {

    fn dfs(matrix: &mut Vec<Vec<char>>, i: i32, j: i32) {
        if i < 0 || i >= matrix.len() as i32 || j < 0 || j >= matrix[0].len() as i32 {
            return;
        }
        if matrix[i as usize][j as usize] == 'O' {
            return;
        }

        if matrix[i as usize][j as usize] == 'x' {
            return;
        }

        if matrix[i as usize][j as usize] == 'B' {
            matrix[i as usize][j as usize] = 'O';
            return;
        }

        if matrix[i as usize][j as usize] == '.' {
            matrix[i as usize][j as usize] = 'O';
        }
        dfs(matrix, i - 1, j);
        dfs(matrix, i + 1, j);
        dfs(matrix, i, j - 1);
        dfs(matrix, i, j + 1);
    }

    dfs(matrix, 0, 0);
}


fn main() {
    let file = fs::read_to_string("./input.txt").expect("no file");

    let input_grid: Vec<Vec<char>> = file.lines().map(|line| line.chars().collect()).collect();

    let rows = 3 * input_grid.len();
    let cols = if rows > 0 { 3 * input_grid[0].len() } else { 0 };

    let mut walled_grid: Vec<Vec<char>> = (0..rows).map(|_| vec!['.'; cols]).collect();

    let start_row = input_grid
        .iter()
        .position(|row| row.contains(&'S'))
        .unwrap();
    let start_col = input_grid[start_row]
        .iter()
        .position(|&c| c == 'S')
        .unwrap();

    let start = (start_row, start_col);

    println!("start {:?}", start);
    let mut current_pos = (start.0 + 1, start.1);
    let mut current_dir = Direction::DOWN;

    while input_grid[current_pos.0][current_pos.1] != 'S' {
        let walled_row = current_pos.0 * 3 + 1;
        let walled_col = current_pos.1 * 3 + 1;
        match input_grid[current_pos.0][current_pos.1] {
            '|' => {
                walled_grid[walled_row - 1][walled_col] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row + 1][walled_col] = 'x';
            }
            '-' => {
                walled_grid[walled_row][walled_col - 1] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row][walled_col + 1] = 'x';
            }
            'L' => {
                walled_grid[walled_row - 1][walled_col] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row][walled_col + 1] = 'x';
            }
            'J' => {
                walled_grid[walled_row - 1][walled_col] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row][walled_col - 1] = 'x';
            }
            '7' => {
                walled_grid[walled_row + 1][walled_col] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row][walled_col - 1] = 'x';
            }
            'F' => {
                walled_grid[walled_row + 1][walled_col] = 'x';
                walled_grid[walled_row][walled_col] = 'x';
                walled_grid[walled_row][walled_col + 1] = 'x';
            }

            _ => {}
        }
        /*
        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
         */
        (current_dir, current_pos) = match (current_dir, input_grid[current_pos.0][current_pos.1]) {
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

    let c_col = 3 * start_col as i32 + 1;
    let c_row = 3 * start_row as i32 + 1;
    walled_grid[c_row as usize][c_col as usize] = 'S';

    let up = c_row - 2;
    let down = c_row + 2;
    let left = c_col - 2;
    let right = c_col + 2;

    if up >= 0 {
        // walled_grid[up as usize][3 * start_col + 1] = 'A';
        if walled_grid[up as usize][c_col as usize] == 'x' {
            walled_grid[up as usize + 1][c_col as usize] = 'x';
        }
    }

    if down < walled_grid[0].len() as i32 {
        // walled_grid[down as usize][3 * start_col + 1] = 'A';
        if walled_grid[down as usize][c_col as usize] == 'x' {
            walled_grid[down as usize - 1][c_col as usize] = 'x';
        }
    }

    if left >= 0 {
        // walled_grid[3 * start_row + 1][left as usize] = 'A';
        if walled_grid[c_row as usize][left as usize] == 'x' {
            walled_grid[c_row as usize][left as usize + 1] = 'x';
        }
    }

    if right < walled_grid[0].len() as i32 {
        // walled_grid[3 * start_row + 1][right as usize] = 'A';
        if walled_grid[c_row as usize][right as usize] == 'x' {
            walled_grid[c_row as usize][right as usize - 1] = 'x';
        }
    }

    for row in &walled_grid {
        println!("{}", row.iter().collect::<String>());
    }
    for i in 0..input_grid.len() {
        for j in 0..input_grid[i].len() {
            let walled_row = i * 3 + 1;
            let walled_col = j * 3 + 1;
            if walled_grid[walled_row][walled_col] == 'x' {
                continue;
            }
            walled_grid[walled_row][walled_col] = 'B'
        }
    }

    fill_outer_connected(&mut walled_grid);

    let total = walled_grid
    .iter()
    .flat_map(|row| row.iter())
    .filter(|&&ch| ch == 'B')
    .count();



    println!("total {}", total);
}

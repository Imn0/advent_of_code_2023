use std::collections::HashMap;
fn main() {
    let file = std::fs::read_to_string("input.txt").expect("no file");
    let instructions = file.lines().map(|line| line.split(' ').collect::<Vec<&str>>()).collect::<Vec<Vec<&str>>>();

    let mut directions = HashMap::new();
    directions.insert("U", (-1, 0));
    directions.insert("D", (1, 0));
    directions.insert("L", (0, -1));
    directions.insert("R", (0, 1));
    
    let mut polygon_points: Vec<(i32,i32)> = vec![(0,0)];

    // Pick's theorem
    let mut boundary_len = 0;


    for instruction in &instructions {
        let (direction, distance) = (instruction[0], instruction[1].parse::<i32>().unwrap());
        boundary_len += distance;
        let (x, y) = directions.get(direction).unwrap();
        polygon_points.append(&mut vec![(polygon_points.last().unwrap().0 + x * distance, polygon_points.last().unwrap().1 + y * distance)]);
    }


    

    let mut inside_area: i32 = 0;
    
    // Shoelace formula
    for ele in &polygon_points {
        inside_area += ele.0 * polygon_points[(polygon_points.iter().position(|&x| x == *ele).unwrap() + 1) % polygon_points.len()].1;
        inside_area -= ele.1 * polygon_points[(polygon_points.iter().position(|&x| x == *ele).unwrap() + 1) % polygon_points.len()].0;
    }
    inside_area = inside_area.abs() / 2;
    let total_area = inside_area - boundary_len / 2 + 1 + boundary_len;
    print!("{}\n", total_area);
}

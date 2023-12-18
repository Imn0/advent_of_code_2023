use std::collections::HashMap;
fn main() {
    let file = std::fs::read_to_string("input.txt").expect("no file");
    let instructions = file.lines().map(|line| line.split(' ').collect::<Vec<&str>>()).collect::<Vec<Vec<&str>>>();

    let mut directions = HashMap::new();
    directions.insert("3", (-1, 0));
    directions.insert("1", (1, 0));
    directions.insert("2", (0, -1));
    directions.insert("0", (0, 1));
    
    let mut polygon_points: Vec<(i64,i64)> = vec![(0,0)];

    // Pick's theorem
    let mut boundary_len = 0;


    for instruction in &instructions {
        let mut inst = instruction[2];
        inst = &inst[2..inst.len()-1];
        let distance = i64::from_str_radix(&inst[0..inst.len()-1], 16).unwrap();
        let direction = &inst[inst.len()-1..inst.len()];


        boundary_len += distance;
        let (x, y) = directions.get(direction).unwrap();
        polygon_points.append(&mut vec![(polygon_points.last().unwrap().0 + x * distance, polygon_points.last().unwrap().1 + y * distance)]);
    }


    

    let mut inside_area: i64 = 0;
    
    // Shoelace formula
    for ele in &polygon_points {
        inside_area += ele.0 * polygon_points[(polygon_points.iter().position(|&x| x == *ele).unwrap() + 1) % polygon_points.len()].1;
        inside_area -= ele.1 * polygon_points[(polygon_points.iter().position(|&x| x == *ele).unwrap() + 1) % polygon_points.len()].0;
    }
    inside_area = inside_area.abs() / 2;
    let total_area = inside_area - boundary_len / 2 + boundary_len + 1;
    print!("{}\n", total_area);
}

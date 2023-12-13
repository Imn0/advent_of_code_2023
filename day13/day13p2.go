package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Part2 struct{}

func (p Part2) validateVerticalReflections(reflection_points []int, max_val int, grid [][]uint8) []int {
	var good_points []int

	for _, val := range reflection_points {
		left := val
		right := val + 1
		var diff int32 = 0
		for left >= 0 && right <= max_val {
			var grid_slice2 []uint8
			var grid_slice1 []uint8
			for j := range grid {
				grid_slice1 = append(grid_slice1, grid[j][left])
				grid_slice2 = append(grid_slice2, grid[j][right])
			}
			diff += p.countDifferences(grid_slice2, grid_slice1)

			left--
			right++
		}
		if diff == 1 {
			good_points = append(good_points, val)
		}
	}

	return good_points
}

func (p Part2) validateHorizontalReflections(reflection_points []int, max_val int, grid [][]uint8) []int {

	var good_points []int

	for _, val := range reflection_points {
		up := val
		down := val + 1
		var diff int32 = 0
		for up >= 0 && down <= max_val {
			diff += p.countDifferences(grid[up], grid[down])
			up--
			down++
		}

		if diff == 1 {
			good_points = append(good_points, val)
		}
	}

	return good_points
}

func (p Part2) countDifferences(a, b []uint8) int32 {
	if len(a) != len(b) {
		return 0
	}

	var count int32 = 0
	for i, val := range a {
		if val != b[i] {
			count++
		}
	}

	return count
}

func (p Part2) countReflectionMagicValue(grid [][]uint8) (int32, error) {

	max_v := len(grid[0]) - 1
	var i int = 0
	var max_vertical []int
	for i < max_v {
		var grid_slice2 []uint8
		var grid_slice1 []uint8
		for j := range grid {
			grid_slice1 = append(grid_slice1, grid[j][i])
			grid_slice2 = append(grid_slice2, grid[j][i+1])
		}
		diff := p.countDifferences(grid_slice1, grid_slice2)
		if diff == 0 || diff == 1 {
			max_vertical = append(max_vertical, i)
		}
		i++
	}

	max_h := len(grid) - 1

	var max_horizontal []int
	i = 0
	for i < max_h {
		diff := p.countDifferences(grid[i], grid[i+1])
		if diff == 0 || diff == 1 {
			max_horizontal = append(max_horizontal, i)
		}
		i++
	}

	max_vertical = p.validateVerticalReflections(max_vertical, max_v, grid)
	max_horizontal = p.validateHorizontalReflections(max_horizontal, max_h, grid)

	if len(max_vertical) == 0 && len(max_horizontal) == 0 {
		return 0, fmt.Errorf("No reflections found")
	}

	if len(max_vertical) > 1 || len(max_horizontal) > 1 {
		return 0, fmt.Errorf("Multiple reflections found")
	}

	if len(max_vertical) == 1 && len(max_horizontal) == 1 {
		return 0, fmt.Errorf("Both reflections found")
	}

	if len(max_horizontal) == 1 {
		return 100 * int32(max_horizontal[0]+1), nil
	}

	if len(max_vertical) == 1 {
		return int32(max_vertical[0] + 1), nil
	}

	return 0, nil
}

func (p Part2) main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var grid [][][]uint8
	var currentLayer [][]uint8

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		if line == "" {
			if len(currentLayer) > 0 {
				grid = append(grid, currentLayer)
				currentLayer = nil // Reset currentLayer for the next group
			}
		} else {
			currentLayer = append(currentLayer, []uint8(line))
		}
	}

	if len(currentLayer) > 0 {
		grid = append(grid, currentLayer)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var total int32 = 0
	for i, grid_slice := range grid {
		result, err := p.countReflectionMagicValue(grid_slice)
		if err != nil {
			fmt.Printf("%d, %s\n", i, err)
		}
		total += result
	}
	fmt.Println(total)

}

const std = @import("std");
const print = std.debug.print;

pub fn move_north(grid: *[128][128]u8, start: usize, j: usize) void {
    var i = start;
    var move_to = i;
    while (i >= 0) {
        if (grid[i][j] == '#') {
            break;
        }
        if (grid[i][j] == '.') {
            move_to = i;
        }
        if (i == 0) {
            break;
        }
        i -= 1;
    }
    if (move_to != start) {
        grid[start][j] = '.';
        grid[move_to][j] = 'O';
        return;
    }
    return;
}

pub fn move_south(grid: *[128][128]u8, start: usize, j: usize) void {
    var i = start;
    var move_to = i;
    while (i < grid.len) {
        if (grid[i][j] == '#') {
            break;
        }
        if (grid[i][j] == '.') {
            move_to = i;
        }
        i += 1;
    }
    if (move_to != start) {
        grid[start][j] = '.';
        grid[move_to][j] = 'O';
        return;
    }
    return;
}

pub fn move_east(grid: *[128][128]u8, i: usize, start: usize) void {
    var j = start;
    var move_to = j;
    while (j < grid[i].len) {
        if (grid[i][j] == '#') {
            break;
        }
        if (grid[i][j] == '.') {
            move_to = j;
        }
        j += 1;
    }
    if (move_to != start) {
        grid[i][start] = '.';
        grid[i][move_to] = 'O';
        return;
    }
    return;
}

pub fn move_west(grid: *[128][128]u8, i: usize, start: usize) void {
    var j = start;
    var move_to = j;
    while (j >= 0) {
        if (grid[i][j] == '#') {
            break;
        }
        if (grid[i][j] == '.') {
            move_to = j;
        }
        if (j == 0) {
            break;
        }
        j -= 1;
    }
    if (move_to != start) {
        grid[i][start] = '.';
        grid[i][move_to] = 'O';
        return;
    }
    return;
}

pub fn check_period(arr: [100]usize, period: usize) bool {
    var i: usize = 0;
    while (i < 100 - period) {
        if (arr[i] != arr[i + period]) {
            return false;
        }
        i += 1;
    }
    return true;
}

pub fn get_period(answers: [100]usize) usize {
    const arrLen = 100;

    var period: usize = 1;
    while (period < arrLen / 2) {
        if (check_period(answers, period)) {
            return period;
        }
        period += 1;
    }

    return 0;
}

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;

    var grid: [128][128]u8 = undefined;
    var size_v: usize = 0;
    var size_h: usize = 0;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        for (0.., line.len) |i, _| {
            grid[size_v][i] = line[i];
        }
        grid[size_v][line.len] = 0;
        size_h = line.len;

        size_v += 1;
    }
    var answers: [100]usize = undefined;
    for (0..1000) |k| {
        for (size_h, 0..) |_, j| {
            for (size_v, 0..) |_, i| {
                if (grid[i][j] == 'O') {
                    move_north(&grid, i, j);
                }
            }
        }
        for (size_h, 0..) |_, j| {
            for (size_v, 0..) |_, i| {
                if (grid[i][j] == 'O') {
                    move_west(&grid, i, j);
                }
            }
        }
        for (size_h, 0..) |_, j| {
            for (size_v, 0..) |_, i| {
                if (grid[i][j] == 'O') {
                    move_south(&grid, i, j);
                }
            }
        }
        for (size_h, 0..) |_, j| {
            for (size_v, 0..) |_, i| {
                if (grid[i][j] == 'O') {
                    move_east(&grid, i, j);
                }
            }
        }
        var count: usize = 0;
        for (0.., size_v) |i, _| {
            for (0.., size_h) |j, _| {
                if (grid[i][j] == 'O') {
                    count += size_v - i;
                }
            }
        }
        answers[k % 100] = count;
    }
    const period = get_period(answers);
    const offset = (1000000000 - 1000) % period;
    print("{d}\n", .{answers[99 - period + offset]});
}

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

    for (size_h, 0..) |_, j| {
        for (size_v, 0..) |_, i| {
            if (grid[i][j] == 'O') {
                move_north(&grid, i, j);
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
    std.debug.print("{d}\n", .{count});
}

export fn colorsearch(pic: [*c]c_char, colors: [*c]c_char, width: c_int, totallengthpic: c_uint, totallengthcolor: c_uint, outputx: [*c]c_int, outputy: [*c]c_int, lastresult: [*c]c_int) void {
    var counter: c_uint = 0;
    var r: c_char = 0;
    var g: c_char = 0;
    var b: c_char = 0;
    var dividend: c_int = 0;
    var it0: usize = 0;
    var it1: usize = 0;
    while (it0 <= totallengthcolor) {
        r = colors[it0];
        g = colors[it0 + 1];
        b = colors[it0 + 2];
        while (it1 <= totallengthpic) {
            if ((r == pic[it1]) and (g == pic[it1 + 1]) and (b == pic[it1 + 2])) {
                dividend = @divFloor(@as(c_int, @intCast(it1)), 3);
                outputx[counter] = @divFloor(dividend, width);
                outputy[counter] = @mod(dividend, width);
                lastresult[0] = @as(c_int, @intCast(counter));
                counter += 1;
            }
            it1 += 3;
        }

        it0 += 3;
    }
}
// zig build-lib ziglangpythoncolor.zig -dynamic -O ReleaseFast

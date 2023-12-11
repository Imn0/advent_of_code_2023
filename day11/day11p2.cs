class day11p2
{
    public static void Run(ulong dist)
    {

        List<string> lines = [.. File.ReadAllLines("./input.txt")];

        lines = FillBlanks(lines);

        lines = RotateLines(lines);

        lines = FillBlanks(lines);


        List<string> rotated = lines;
        lines = RotateLines(lines);

        List<Tuple<int, int>> galaxies = [];

        for (int i = 0; i < lines.Count; i++)
        {
            for (int j = 0; j < lines[i].Length; j++)
            {
                if (lines[i][j] == '#')
                {
                    galaxies.Add(new Tuple<int, int>(i, j));
                }
            }
        }


        ulong TotalDistance = 0;

        for (int i = 0; i < galaxies.Count; i++)
        {
            for (int j = i + 1; j < galaxies.Count; j++)
            {
                TotalDistance += CalculateDistance(galaxies[i], galaxies[j], lines, rotated, dist);
            }
        }
        Console.WriteLine(TotalDistance);
    }


    static ulong CalculateDistance(Tuple<int, int> a, Tuple<int, int> b, List<string> lines, List<string> rotated, ulong dist)
    {
        ulong total = 0;

        int start = Math.Min(a.Item1, b.Item1);
        int end = Math.Max(a.Item1, b.Item1);
        for (int i = start; i <= end; i++)
        {
            if (lines[i][0] == 'X')
            {
                total += dist;
            }
            else
            {
                total += 1;
            }
        }
        total -= 1;


        start = Math.Min(a.Item2, b.Item2);
        end = Math.Max(a.Item2, b.Item2);
        for (int i = start; i <= end; i++)
        {
            if (rotated[i][0] == 'X')
            {
                total += dist;
            }
            else
            {
                total += 1;
            }
        }

        total -= 1;

        return total;
    }

    static List<string> FillBlanks(List<string> lines)
    {
        for (int i = 0; i < lines.Count; i++)
        {
            if (!lines[i].Contains('#'))
            {
                // lines.Insert(i, lines[i]);
                // i++;
                lines[i] = new string('X', lines[i].Length);
            }
        }

        return lines;
    }

    static List<string> RotateLines(List<string> lines)
    {
        int maxLength = lines.Max(line => line.Length);
        List<string> rotatedLines = [];

        for (int i = 0; i < maxLength; i++)
        {
            string rotatedLine = new(lines.Select(line => line.Length > i ? line[i] : ' ').ToArray());
            rotatedLines.Add(rotatedLine);
        }

        return rotatedLines;
    }
}

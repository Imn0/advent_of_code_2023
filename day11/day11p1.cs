class day11p1
{
    public static void Run()
    {

        List<string> lines = [.. File.ReadAllLines("./input.txt")];

        lines = FillBlanks(lines);

        lines = RotateLines(lines);

        lines = FillBlanks(lines);

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


        int TotalDistance = 0;

        for (int i = 0; i < galaxies.Count; i++)
        {
            for (int j = i + 1; j < galaxies.Count; j++)
            {
                TotalDistance += CalculateDistance(galaxies[i], galaxies[j]);
            }
        }
        Console.WriteLine(TotalDistance);
    }


    static int CalculateDistance(Tuple<int, int> a, Tuple<int, int> b)
    {
        return Math.Abs(a.Item1 - b.Item1) + Math.Abs(a.Item2 - b.Item2);
    }

    static List<string> FillBlanks(List<string> lines)
    {
        for (int i = 0; i < lines.Count; i++)
        {
            if (!lines[i].Contains('#'))
            {
                lines.Insert(i, lines[i]);
                i++;
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

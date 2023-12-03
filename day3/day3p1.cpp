#include <iostream>
#include <fstream>
#include <string>
#include <vector>

/*
 * @brief Checks if number is touching a symbol, sets pos_in_string to the end of the number
 *
 * @param lines
 * @param line
 * @param pos_in_string
 * @return int 0 if not touching, number if touching
 */

bool is_symbol(char c)
{
    if ((c >= '0' && c <= '9') || c == '.')
    {
        return false;
    }
    return true;
}

int is_touching(std::vector<std::string> lines, int *pos_in_string, int depth = 0)
{

    int start = *pos_in_string;
    int end = *pos_in_string;
    while (lines.at(depth).at(end) >= '0' && lines.at(depth).at(end) <= '9')
    {
        end++;
    }

    int num = std::stoi(lines.at(depth).substr(start, end - start));
    *pos_in_string = end;

    for (int i = start; i < end; i++)
    {
        if (is_symbol(lines.at(depth).at(i-1)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth).at(i+1)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth+1).at(i-1)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth+1).at(i)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth+1).at(i+1)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth-1).at(i+1)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth-1).at(i)))
        {
            return num;
        }
        if (is_symbol(lines.at(depth-1).at(i-1)))
        {
            return num;
        }
    }

    return 0;
}

int main(int argc, char **argv)
{
    std::string line;
    std::ifstream file("input.txt");
    std::vector<std::string> lines;
    while (getline(file, line))
    {
        line = "." + line + ".";
        lines.push_back(line);
    }
    file.close();

    int l = lines.at(0).size();
    std::string top_bottom(l, '.');
    lines.insert(lines.begin(), top_bottom);
    lines.push_back(top_bottom);

    int total = 0;

    for (int i = 0; i < lines.size(); i++)
    {
        for (int j = 0; j < lines.at(i).size(); j++)
        {
            if (lines.at(i).at(j) >= '0' && lines.at(i).at(j) <= '9')
            {
                total += is_touching(lines, &j, i);
            }
        }
    }
    std::cout << total << std::endl;
}
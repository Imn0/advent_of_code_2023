#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class num
{
private:
    /* data */
public:
    int value;
    int x;
    int y;
    int width;
    int height;
    num(std::vector<std::string> lines, int *pos_in_string, int depth);
    num(int value, int x, int y, int width, int height);
    ~num();
};

num::num(int value, int x, int y, int width, int height)
{
    this->value = value;
    this->x = x;
    this->y = y;
    this->width = width;
    this->height = height;
}

num::~num()
{
}

num::num(std::vector<std::string> lines, int *pos_in_string, int depth)
{

    int start = *pos_in_string;
    int end = *pos_in_string;
    while (lines.at(depth).at(end) >= '0' && lines.at(depth).at(end) <= '9')
    {
        end++;
    }

    int num = std::stoi(lines.at(depth).substr(start, end - start));
    *pos_in_string = end-1;
    std::cout << end << std::endl;
    this->x = start - 1;
    this->y = depth - 1;
    this->width = end - start + 2;
    this->height = 3;
    this->value = num;
}

class point
{
private:
    /* data */
public:
    int x;
    int y;
    point(int x, int y);
    ~point();
};

point::point(int x, int y)
{
    this->x = x;
    this->y = y;
}

point::~point()
{
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

    std::vector<num> nums;
    std::vector<point> points;

    for (int i = 0; i < lines.size(); i++)
    {
        for (int j = 0; j < lines.at(i).size(); j++)
        {
            if (lines.at(i).at(j) >= '0' && lines.at(i).at(j) <= '9')
            {
                nums.push_back(num(lines, &j, i));
            }
            else if (lines.at(i).at(j) == '*')
            {
                points.push_back(point(j, i));
            }
        }
    }

    for (auto n : nums)
    {
        std::cout << n.value << " " << n.x << " " << n.y << " " << n.width << " " << n.height << std::endl;
    }

    for (auto p : points)
    {
        std::cout << p.x << " " << p.y << std::endl;
    }

    for (auto l : lines)
    {
        std::cout << l << std::endl;
    }

    unsigned long long total = 0;
    for (auto p : points)
    {
        std::cout << "------" << p.x << " " << p.y << std::endl;
        int c = 0;
        int current = 1;
        for (auto n : nums)
        {
            if (p.x >= n.x && p.x < n.x + n.width && p.y >= n.y && p.y < n.y + n.height)
            {
                c++;
                std::cout << n.value << std::endl;
                current *= n.value;
            }
            if (c > 2)
            {
                break;
            }
        }
        if (c == 2)
        {
            total += current;
        }
    }

    std::cout << total << std::endl;
}
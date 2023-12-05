#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct mapping
{
    unsigned long long origin_start;
    unsigned long long destination_start;
    unsigned long long length;
} typedef mapping;

enum mapping_type
{
    SEEDS,
    EMPTY,
    MAPPING
};

void print_mapping(mapping *map, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%llu %llu %llu\n", map[i].origin_start, map[i].destination_start, map[i].length);
    }
    printf("\n");
}

void print_mapping_array(mapping **maps, int *maps_sizes, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("map %d:\n", i);
        print_mapping(maps[i], maps_sizes[i]);
    }
}

void print_array(unsigned long long *array, int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("%llu ", array[i]);
    }
    printf("\n");
}

int load_data(const char *filename, mapping **maps, int *map_sizes, unsigned long long *seeds, int maps_count, int *seeds_size)
{

    char *buff = calloc(64, sizeof(char));

    char c;
    FILE *file;

    file = fopen(filename, "a");
    if (!file)
    {
        return 1;
    }
    fseek(file, -2, SEEK_END);
    long size = ftell(file);

    // If the file is not empty, move the pointer to the second-to-last position
    if (ftell(file) >= 0)
    {
        c = fgetc(file);          // Get the second-to-last character
        fseek(file, 0, SEEK_END); // Move back to the end for appending
        // If the second-to-last character is not 'a', append 'a'
        if (c != '\n')
        {
            fprintf(file, "\n");
        }
    }

    fclose(file);

    file = fopen(filename, "r");
    if (!file)
    {
        return 1;
    }

    int current_map = -1;
    int i = 0;
    bool reading_num = false;
    int reading_type = SEEDS;
    bool zeroth_item = true;

    unsigned long long current_origin_start = 0;
    bool origin_start_set = false;
    bool next_line_last = false;
    unsigned long long current_destination_start = 0;
    unsigned long long current_length = 0;

    while ((c = getc(file)) != EOF)
    {
        switch (reading_type)
        {
        case SEEDS:
            if (c == ' ' || c == '\n')
            {
                if (zeroth_item)
                {
                    memset(buff, 0, 64);
                    i = 0;
                    zeroth_item = false;
                    continue;
                }
                unsigned long long seed = atoll(buff);
                seeds[*seeds_size] = seed;
                *seeds_size += 1;
                memset(buff, 0, 64);
                i = 0;
            }
            if (c == '\n')
            {
                reading_type = EMPTY;
                zeroth_item = true;
                i = 0;
            }
            if (c >= '0' && c <= '9')
            {
                buff[i] = c;
                i++;
            }
            break;

        case EMPTY:
            if (c == ':')
            {
                current_map++;

                reading_type = MAPPING;
                zeroth_item = true;
                i = 0;
            }
            break;

        case MAPPING:
            if (c == '\n')
            {
                if (next_line_last)
                {
                    reading_type = EMPTY;
                    next_line_last = false;
                    continue;
                }

                if (zeroth_item)
                {
                    memset(buff, 0, 64);
                    i = 0;
                    zeroth_item = false;
                    continue;
                }
                origin_start_set = false;
                current_length = atoll(buff);
                memset(buff, 0, 64);
                i = 0;

                maps[current_map][map_sizes[current_map]].origin_start = current_origin_start;
                maps[current_map][map_sizes[current_map]].destination_start = current_destination_start;
                maps[current_map][map_sizes[current_map]].length = current_length;
                map_sizes[current_map]++;
                reading_num = true;
                next_line_last = true;
                continue;
            }
            if (c >= '0' && c <= '9')
            {
                next_line_last = false;

                buff[i] = c;
                i++;
            }
            if (c == ' ')
            {
                next_line_last = false;

                if (!origin_start_set)
                {
                    current_destination_start = atoll(buff);
                    memset(buff, 0, 64);
                    i = 0;
                    origin_start_set = true;
                    continue;
                }
                else
                {
                    current_origin_start = atoll(buff);
                    memset(buff, 0, 64);
                    i = 0;
                    continue;
                }
            }

        default:
            break;
        }
    }
    free(buff);
    fclose(file);
}

int find_mapping_index(unsigned long long num, mapping *map, int map_size)
{
    for (int i = 0; i < map_size; i++)
    {
        if (num >= map[i].origin_start && num < map[i].origin_start + map[i].length)
        {
            return i;
        }
    }
    return -1;
}

unsigned long long map(unsigned long long num, mapping *map)
{
    return num - map->origin_start + map->destination_start;
}

int map_seeds(mapping **maps, int *map_sizes, unsigned long long *seeds, const int maps_count, const int seeds_size)
{
    for (int k = 0; k < seeds_size; k += 2)
    {
        printf("k: %d\n", k);
        unsigned long long seed = seeds[k];
        unsigned long long seed_count = seeds[k + 1];
        for (unsigned long long i = seed; i < seed + seed_count; i++)
        {
            if (i % 16777216 == 0)
            {
                float percentage = ((float)(i - seed) / seed_count) * 100;
                printf("Progress: %.2f%%\r", percentage);
                fflush(stdout);
            }

            unsigned long long tmp_seed = i;
            for (int map_num = 0; map_num < maps_count; map_num++)
            {
                int map_index = find_mapping_index(tmp_seed, maps[map_num], map_sizes[map_num]);
                if (map_index == -1)
                {
                    continue;
                }
                tmp_seed = map(tmp_seed, &maps[map_num][map_index]);
            }
            if (tmp_seed < seeds[k])
            {
                seeds[k] = tmp_seed;
            }
            seeds[k + 1] = -1;
        }
    }
    return 0;
}

unsigned long long find_min(unsigned long long *array, int length)
{
    unsigned long long min = array[0];
    for (int i = 1; i < length; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
        }
    }
    return min;
}

int main()
{
    unsigned long long *seeds = calloc(32, sizeof(unsigned long long));
    int seeds_size = 0;

    mapping *map1 = calloc(32, sizeof(mapping));
    mapping *map2 = calloc(32, sizeof(mapping));
    mapping *map3 = calloc(32, sizeof(mapping));
    mapping *map4 = calloc(32, sizeof(mapping));
    mapping *map5 = calloc(32, sizeof(mapping));
    mapping *map6 = calloc(32, sizeof(mapping));
    mapping *map7 = calloc(32, sizeof(mapping));

    mapping **maps = calloc(7, sizeof(mapping *));
    maps[0] = map1;
    maps[1] = map2;
    maps[2] = map3;
    maps[3] = map4;
    maps[4] = map5;
    maps[5] = map6;
    maps[6] = map7;

    int *map_sizes = calloc(7, sizeof(int));
    map_sizes[0] = 0;
    map_sizes[1] = 0;
    map_sizes[2] = 0;
    map_sizes[3] = 0;
    map_sizes[4] = 0;
    map_sizes[5] = 0;
    map_sizes[6] = 0;
    const char filename[] = "input.txt";
    load_data(filename, maps, map_sizes, seeds, 7, &seeds_size);

    // print_mapping_array(maps, map_sizes, 7);
    map_seeds(maps, map_sizes, seeds, 7, seeds_size);
    printf("seeds:\n");
    print_array(seeds, seeds_size);
    printf("min: %llu\n", find_min(seeds, seeds_size));
}
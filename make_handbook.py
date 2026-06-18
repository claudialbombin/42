#!/usr/bin/env python3
"""
PDF Generator for 42 School Programming Exercises
Creates a formatted PDF with exercises organized by level,
each exercise on its own page with full content.
"""

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, KeepTogether
)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import StyleSheet1

class ExercisePDF:
    def __init__(self, filename="exercises_formatted.pdf"):
        self.filename = filename
        self.doc = None
        self.styles = None
        self.story = []
        
    def setup_styles(self):
        """Setup all paragraph styles for the document"""
        self.styles = getSampleStyleSheet()
        
        # Custom styles - using unique names to avoid conflicts
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomLevelTitle',
            parent=self.styles['Title'],
            fontSize=20,
            spaceAfter=20,
            spaceBefore=30,
            textColor=colors.darkblue,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomExerciseTitle',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=6,
            textColor=colors.darkred,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomExerciseDetails',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            textColor=colors.darkgreen,
            fontName='Helvetica'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomCodeBlock',
            parent=self.styles['Normal'],
            fontSize=8,
            fontName='Courier',
            leftIndent=10,
            rightIndent=10,
            spaceAfter=8,
            textColor=colors.black
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomDescription',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
            fontName='Helvetica'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomTOCEntry',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=4,
            fontName='Helvetica'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHintTitle',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=4,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHintText',
            parent=self.styles['Normal'],
            fontSize=9,
            leftIndent=20,
            spaceAfter=6,
            textColor=colors.black,
            fontName='Helvetica'
        ))

    def get_exercise_data(self):
        """Return all exercise data with descriptions and code"""
        exercises = [
            # Level 1
            {
                "level": 1, "name": "first_word", "file": "first_word.c", 
                "allowed": "write",
                "description": """Write a program that takes a string and displays its first word, followed by a newline.
A word is a section of string delimited by spaces/tabs or by the start/end of the string.
If the number of parameters is not 1, or if there are no words, simply display a newline.""",
                "code": """#include <unistd.h>

int main (int argc, char **argv)
{
    int i = 0;
    if (argc == 2)
    {
        while (argv[1][i] == 32 || argv[1][i] == 9)
            i++;
        while ((argv[1][i] != 32 && argv[1][i] != 9) && argv[1][i])
        {
            write(1, &argv[1][i], 1);
            i++;
        }
    }
    write(1, "\\n", 1);
}"""
            },
            {
                "level": 1, "name": "fizzbuzz", "file": "fizzbuzz.c",
                "allowed": "write",
                "description": """Write a program that prints the numbers from 1 to 100, each separated by a newline.
If the number is a multiple of 3, it prints 'fizz' instead.
If the number is a multiple of 5, it prints 'buzz' instead.
If the number is both a multiple of 3 and a multiple of 5, it prints 'fizzbuzz' instead.""",
                "code": """#include <unistd.h>

void ft_write_number(int number)
{
    char str[10] = "0123456789";
    if (number > 9)
        ft_write_number(number / 10);
    write (1, &str[number % 10], 1);
}

int main()
{
    int i = 1;
    while (i <= 100)
    {
        if (i % 15 == 0)
            write (1, "fizzbuzz", 8);
        else if (i % 3 == 0)
            write (1, "fizz", 4);
        else if (i % 5 == 0)
            write (1, "buzz", 4);
        else
            ft_write_number(i);
        i++;
        write (1, "\\n", 1);
    }
}"""
            },
            {
                "level": 1, "name": "ft_putstr", "file": "ft_putstr.c",
                "allowed": "write",
                "description": """Write a function that displays a string on the standard output.
The pointer passed to the function contains the address of the string's first character.
Your function must be declared as follows:
void ft_putstr(char *str);""",
                "code": """#include <unistd.h>

void ft_putstr(char *str)
{
    int i = 0;
    while (str[i])
        write(1, &str[i++], 1);
}"""
            },
            {
                "level": 1, "name": "ft_strcpy", "file": "ft_strcpy.c",
                "allowed": "",
                "description": """Reproduce the behavior of the function strcpy (man strcpy).
Your function must be declared as follows:
char *ft_strcpy(char *s1, char *s2);""",
                "code": """char *ft_strcpy(char *s1, char *s2)
{
    int i = 0;
    while (s2[i] != '\\0')
    {
        s1[i] = s2[i];
        i++;
    }
    s1[i] = '\\0';
    return (s1);
}"""
            },
            {
                "level": 1, "name": "ft_strlen", "file": "ft_strlen.c",
                "allowed": "",
                "description": """Write a function that returns the length of a string.
Your function must be declared as follows:
int ft_strlen(char *str);""",
                "code": """int ft_strlen(char *str)
{
    int i = 0;
    while (str[i])
        i++;
    return (i);
}"""
            },
            {
                "level": 1, "name": "ft_swap", "file": "ft_swap.c",
                "allowed": "",
                "description": """Write a function that swaps the contents of two integers the addresses of which are passed as parameters.
Your function must be declared as follows:
void ft_swap(int *a, int *b);""",
                "code": """void ft_swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}"""
            },
            {
                "level": 1, "name": "repeat_alpha", "file": "repeat_alpha.c",
                "allowed": "write",
                "description": """Write a program called repeat_alpha that takes a string and display it repeating each alphabetical character as many times as its alphabetical index, followed by a newline.
'a' becomes 'a', 'b' becomes 'bb', 'e' becomes 'eeeee', etc...
Case remains unchanged.
If the number of arguments is not 1, just display a newline.""",
                "code": """#include <unistd.h>

void ft_putchar_n(char c, int i)
{
    while (i > 0)
    {
        write(1, &c, 1);
        --i;
    }
}

void repeat_alpha(char *str)
{
    while (*str != '\\0')
    {
        if (*str >= 'a' && *str <= 'z')
            ft_putchar_n(*str, *str + 1 - 'a');
        else if (*str >= 'A' && *str <= 'Z')
            ft_putchar_n(*str, *str + 1 - 'A');
        else
            write(1, str, 1);
        ++str;
    }
}

int main(int ac, char **av)
{
    if (ac == 2)
        repeat_alpha(av[1]);
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 1, "name": "rev_print", "file": "rev_print.c",
                "allowed": "write",
                "description": """Write a program that takes a string, and displays the string in reverse followed by a newline.
If the number of parameters is not 1, the program displays a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char *argv[])
{
    int i = 0;
    if (argc == 2)
    {
        while (argv[1][i])
            i += 1;
        while (i)
            write(1, &argv[1][--i], 1);
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 1, "name": "rot_13", "file": "rot_13.c",
                "allowed": "write",
                "description": """Write a program that takes a string and displays it, replacing each of its letters by the letter 13 spaces ahead in alphabetical order.
'z' becomes 'm' and 'Z' becomes 'M'. Case remains unaffected.
The output will be followed by a newline.
If the number of arguments is not 1, the program displays a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc > 1)
    {
        while(argv[1][i])
        {
            if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
                argv[1][i] = (argv[1][i] - 'a' + 13) % 26 + 'a';
            else if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
                argv[1][i] = (argv[1][i] - 'A' + 13) % 26 + 'A';
            write(1, &argv[1][i], 1);
            i++;
        }
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 1, "name": "rotone", "file": "rotone.c",
                "allowed": "write",
                "description": """Write a program that takes a string and displays it, replacing each of its letters by the next one in alphabetical order.
'z' becomes 'a' and 'Z' becomes 'A'. Case remains unaffected.
The output will be followed by a \\n.
If the number of arguments is not 1, the program displays \\n.""",
                "code": """#include <unistd.h>

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void rotone(char *s)
{
    while (*s)
    {
        if ((*s >= 'A' && *s <= 'Y') || (*s >= 'a' && *s <= 'y'))
            ft_putchar(*s + 1);
        else if (*s == 'Z' || *s == 'z')
            ft_putchar(*s - 25);
        else
            ft_putchar(*s);
        ++s;
    }
}

int main(int ac, char **av)
{
    if (ac == 2)
        rotone(av[1]);
    ft_putchar('\\n');
    return (0);
}"""
            },
            {
                "level": 1, "name": "search_and_replace", "file": "search_and_replace.c",
                "allowed": "write, exit",
                "description": """Write a program called search_and_replace that takes 3 arguments, the first arguments is a string in which to replace a letter (2nd argument) by another one (3rd argument).
If the number of arguments is not 3, just display a newline.
If the second argument is not contained in the first one (the string) then the program simply rewrites the string followed by a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc == 4 && !argv[2][1] & !argv[3][1])
    {
        while (argv[1][i]!='\\0')
        {
            if (argv[1][i]==argv[2][0])
            {
                argv[1][i] = argv[3][0];
            }
            write (1, &argv[1][i], 1);
            i++;
        }
    }
    write (1, "\\n", 1);
}"""
            },
            {
                "level": 1, "name": "ulstr", "file": "ulstr.c",
                "allowed": "write",
                "description": """Write a program that takes a string and reverses the case of all its letters. Other characters remain unchanged.
You must display the result followed by a '\\n'.
If the number of arguments is not 1, the program displays '\\n'.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc == 2)
    {
        while (argv[1][i] != '\\0')
        {
            if (argv[1][i] >= 'a' && argv[1][i] <= 'z')
                argv[1][i] -= 32;
            else if (argv[1][i] >= 'A' && argv[1][i] <= 'Z')
                argv[1][i] += 32;
            write(1, &argv[1][i], 1);
            i++;
        }
    }
    write(1, "\\n", 1);
}"""
            },
            # Level 2
            {
                "level": 2, "name": "alpha_mirror", "file": "alpha_mirror.c",
                "allowed": "write",
                "description": """Write a program called alpha_mirror that takes a string and displays this string after replacing each alphabetical character by the opposite alphabetical character, followed by a newline.
'a' becomes 'z', 'Z' becomes 'A' 'd' becomes 'w', 'M' becomes 'N'
and so on.
Case is not changed.
If the number of arguments is not 1, display only a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc == 2)
    {
        while(argv[1][i])
        {
            if(argv[1][i] >= 65 && argv[1][i] <= 90)
            {
                argv[1][i] = 90 - argv[1][i] + 65;
            }
            else if (argv[1][i] >= 97 && argv[1][i] <= 122)
            {
                argv[1][i] = 122-argv[1][i] + 97;
            }
            write(1, &argv[1][i], 1);
            i++;
        }
    }
    write (1,"\\n",1);
}"""
            },
            {
                "level": 2, "name": "camel_to_snake", "file": "camel_to_snake.c",
                "allowed": "malloc, realloc, write",
                "description": """Write a program that takes a single string in lowerCamelCase format and converts it into a string in snake_case format.
A lowerCamelCase string is a string where each word begins with a capital letter except for the first one.
A snake_case string is a string where each word is in lower case, separated by an underscore "_".""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc == 2)
    {
        while(argv[1][i])
        {
            if(argv[1][i] >= 65 && argv[1][i] <= 90)
            {
                argv[1][i] = argv[1][i] + 32;
                write (1, "_", 1);
            }
            write(1, &argv[1][i], 1);
            i++;
        }
    }
    write (1, "\\n", 1);
}"""
            },
            {
                "level": 2, "name": "do_op", "file": "do_op.c",
                "allowed": "atoi, printf, write",
                "description": """Write a program that takes three strings:
The first and the third one are representations of base-10 signed integers that fit in an int.
The second one is an arithmetic operator chosen from: + - * / %
The program must display the result of the requested arithmetic operation, followed by a newline. If the number of parameters is not 3, the program just displays a newline.
You can assume the string have no mistakes or extraneous characters. Negative numbers, in input or output, will have one and only one leading '-'. The result of the operation fits in an int.""",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc == 4)
    {
        if (argv[2][0] == '+')
            printf("%d", (atoi(argv[1]) + atoi(argv[3])));
        if (argv[2][0] == '-')
            printf("%d", (atoi(argv[1]) - atoi(argv[3])));
        if (argv[2][0] == '*')
            printf("%d", (atoi(argv[1]) * atoi(argv[3])));
        if (argv[2][0] == '/')
            printf("%d", (atoi(argv[1]) / atoi(argv[3])));
        if (argv[2][0] == '%')
            printf("%d", (atoi(argv[1]) % atoi(argv[3])));
    }
    printf("\\n");
    return (0);
}"""
            },
            {
                "level": 2, "name": "ft_atoi", "file": "ft_atoi.c",
                "allowed": "None",
                "description": """Write a function that converts the string argument str to an integer (type int) and returns it.
It works much like the standard atoi(const char *str) function, see the man.
Your function must be declared as follows:
int ft_atoi(const char *str);""",
                "code": """int ft_atoi(char *str)
{
    int result = 0;
    int sign = 1;
    while (*str == ' ' || (*str >= 9 && *str <= 13))
        str++;
    if (*str == '-')
        sign = -1;
    if (*str == '-' || *str == '+')
        str++;
    while (*str >= '0' && *str <= '9')
    {
        result = result * 10 + *str - '0';
        str++;
    }
    return (sign * result);
}"""
            },
            {
                "level": 2, "name": "ft_strcmp", "file": "ft_strcmp.c",
                "allowed": "",
                "description": """Reproduce the behavior of the function strcmp (man strcmp).
Your function must be declared as follows:
int ft_strcmp(char *s1, char *s2);""",
                "code": """int ft_strcmp(char *s1, char *s2)
{
    int i = 0;
    while(s1[i] != '\\0' && s2[i] != '\\0' && s1[i] == s2[i])
    {
        i++;
    }
    return (s1[i] - s2[i]);
}"""
            },
            {
                "level": 2, "name": "ft_strcspn", "file": "ft_strcspn.c",
                "allowed": "None",
                "description": """Reproduce exactly the behavior of the function strcspn (man strcspn).
The function should be prototyped as follows:
size_t ft_strcspn(const char *s, const char *reject);""",
                "code": """size_t ft_strcspn(const char *s, const char *reject)
{
    int i = 0;
    int j = 0;
    while (s[i] != '\\0')
    {
        j = 0;
        while (reject[j] != '\\0')
        {
            if(s[i] == reject[j])
                return (i);
            j++;
        }
        i++;
    }
    return (i);
}"""
            },
            {
                "level": 2, "name": "ft_strdup", "file": "ft_strdup.c",
                "allowed": "malloc",
                "description": """Reproduce the behavior of the function strdup (man strdup).
Your function must be declared as follows:
char *ft_strdup(char *src);""",
                "code": """#include <stdlib.h>

char *ft_strdup(char *src)
{
    int i = 0;
    int length = 0;
    char *strcpy;
    while (src[length])
        length++;
    strcpy = malloc(sizeof(*strcpy) * (length + 1));
    if (strcpy != NULL)
    {
        while (src[i])
        {
            strcpy[i] = src[i];
            i++;
        }
        strcpy[i] = '\\0';
    }
    return (strcpy);
}"""
            },
            {
                "level": 2, "name": "ft_strpbrk", "file": "ft_strpbrk.c",
                "allowed": "None",
                "description": """Reproduce exactly the behavior of the function strpbrk (man strpbrk).
The function should be prototyped as follows:
char *ft_strpbrk(const char *s1, const char *s2);""",
                "code": """char *ft_strpbrk(const char *s1, const char *s2)
{
    int i = 0;
    if (!s1 || !s2)
    {
        return (0);
    }
    while(*s1)
    {
        i = 0;
        while(s2[i])
        {
            if(*s1 == s2[i])
                return (char *) s1;
            i++;
        }
        s1++;
    }
    return (0);
}"""
            },
            {
                "level": 2, "name": "ft_strrev", "file": "ft_strrev.c",
                "allowed": "",
                "description": """Write a function that reverses (in-place) a string.
It must return its parameter.
Your function must be declared as follows:
char *ft_strrev(char *str);""",
                "code": """char *ft_strrev(char *str)
{
    int i = -1;
    int length = 0;
    char temporary;
    while (str[length])
        length++;
    while (++i < length / 2)
    {
        temporary = str[i];
        str[i] = str[length - 1 - i];
        str[length - 1 - i] = temporary;
    }
    return (str);
}"""
            },
            {
                "level": 2, "name": "ft_strspn", "file": "ft_strspn.c",
                "allowed": "None",
                "description": """Reproduce exactly the behavior of the strspn function (man strspn).
The function should be prototyped as follows:
size_t ft_strspn(const char *s, const char *accept);""",
                "code": """char *ft_strchr(const char *s, int c)
{
    while (*s != '\\0')
    {
        if (*s == c)
            return ((char *)s);
        ++s;
    }
    return (0);
}

size_t ft_strspn(const char *s, const char *accept)
{
    size_t i = 0;
    while (s[i] != '\\0')
    {
        if (ft_strchr(accept, s[i]) == 0)
            break;
        ++i;
    }
    return (i);
}"""
            },
            {
                "level": 2, "name": "inter", "file": "inter.c",
                "allowed": "write",
                "description": """Write a program that takes two strings and displays, without doubles, the characters that appear in both strings, in the order they appear in the first one.
The display will be followed by a \\n.
If the number of arguments is not 2, the program displays \\n.""",
                "code": """#include <unistd.h>

int iter(char *str, char c, int len)
{
    int i = 0;
    while (str[i] && (i < len || len == -1))
        if (str[i++] == c)
            return (1);
    return (0);
}

int main(int argc, char *argv[])
{
    int i;
    if (argc == 3)
    {
        i = 0;
        while (argv[1][i])
        {
            if (!iter(argv[1], argv[1][i], i) && iter(argv[2], argv[1][i], -1))
                write(1, &argv[1][i], 1);
            i += 1;
        }
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 2, "name": "is_power_of_2", "file": "is_power_of_2.c",
                "allowed": "None",
                "description": """Write a function that determines if a given number is a power of 2.
This function returns 1 if the given number is a power of 2, otherwise it returns 0.
Your function must be declared as follows:
int is_power_of_2(unsigned int n);""",
                "code": """int is_power_of_2(unsigned int n)
{
    int number = 1;
    while(number <= n)
    {
        if (number == n)
        {
            return 1;
        }
        number = number * 2;
    }
    return 0;
}"""
            },
            {
                "level": 2, "name": "last_word", "file": "last_word.c",
                "allowed": "write",
                "description": """Write a program that takes a string and displays its last word followed by a \\n.
A word is a section of string delimited by spaces/tabs or by the start/end of the string.
If the number of parameters is not 1, or there are no words, display a newline.""",
                "code": """#include <unistd.h>

void last_word(char *str)
{
    int j = 0;
    int i = 0;
    while (str[i])
    {
        if (str[i] == ' ' && str[i + 1] >= 33 && str[i + 1] <= 126)
            j = i + 1;
        i++;
    }
    while (str[j] >= 33 && str[j] <= 127)
    {
        write(1, &str[j], 1);
        j++;
    }
}

int main(int argc, char **argv)
{
    if (argc == 2)
        last_word(argv[1]);
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 2, "name": "max", "file": "max.c",
                "allowed": "",
                "description": """Write the following function:
int max(int* tab, unsigned int len);
The first parameter is an array of int, the second is the number of elements in the array.
The function returns the largest number found in the array.
If the array is empty, the function returns 0.""",
                "code": """int max(int *tab, unsigned int len)
{
    unsigned int result;
    unsigned int i = 0;
    result = tab[i];
    while(i < len)
    {
        if (result < tab[i])
        {
            result = tab[i];
        }
        i++;
    }
    return result;
}"""
            },
            {
                "level": 2, "name": "print_bits", "file": "print_bits.c",
                "allowed": "write",
                "description": """Write a function that takes a byte, and prints it in binary WITHOUT A NEWLINE AT THE END.
Your function must be declared as follows:
void print_bits(unsigned char octet);
Example, if you pass 2 to print_bits, it will print "00000010\"""",
                "code": """#include <unistd.h>

void print_bits(unsigned char octet)
{
    int i = 8;
    unsigned char bit;
    while (i--)
    {
        bit = (octet >> i & 1) + '0';
        write(1, &bit, 1);
    }
}"""
            },
            {
                "level": 2, "name": "reverse_bits", "file": "reverse_bits.c",
                "allowed": "",
                "description": """Write a function that takes a byte, reverses it, bit by bit (like the example) and returns the result.
Your function must be declared as follows:
unsigned char reverse_bits(unsigned char octet);
Example:
1 byte
0010 0110 || / 0110 0100""",
                "code": """unsigned char reverse_bits(unsigned char octet)
{
    int i = 8;
    unsigned char res = 0;
    while (i > 0)
    {
        res = res * 2 + (octet % 2);
        octet = octet / 2;
        i--;
    }
    return (res);
}"""
            },
            {
                "level": 2, "name": "snake_to_camel", "file": "snake_to_camel.c",
                "allowed": "malloc, free, realloc, write",
                "description": """Write a program that takes a single string in snake_case format and converts it into a string in lowerCamelCase format.
A snake_case string is a string where each word is in lower case, separated by an underscore "_".
A lowerCamelCase string is a string where each word begins with a capital letter except for the first one.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    if (argc ==2 )
    {
        while(argv[1][i] != '\\0')
        {
            if (argv[1][i] == '_')
            {
                i++;
                argv[1][i] = argv[1][i]-32;
            }
            write (1, &argv[1][i], 1);
            i++;
        }
    }
    write(1, "\\n", 1);
}"""
            },
            {
                "level": 2, "name": "swap_bits", "file": "swap_bits.c",
                "allowed": "",
                "description": """Write a function that takes a byte, swaps its halves (like the example) and returns the result.
Your function must be declared as follows:
unsigned char swap_bits(unsigned char octet);
Example:
1 byte
0100 | 0001 \\/ / 0001 | 0100""",
                "code": """unsigned char swap_bits(unsigned char octet)
{
    return ((octet >> 4) | (octet << 4));
}"""
            },
            {
                "level": 2, "name": "union", "file": "union.c",
                "allowed": "write",
                "description": """Write a program that takes two strings and displays, without doubles, the characters that appear in either one of the strings. The display will be in the order characters appear in the command line, and will be followed by a \\n. If the number of arguments is not 2, the program displays \\n.""",
                "code": """#include <unistd.h>

int check(int c, char *str, int index)
{
    int i = 0;
    while(i < index)
    {
        if (str[i] == c)
            return 0;
        i++;
    }
    return 1;
}

int main(int argc, char **argv)
{
    int i = 0;
    int j = 0;
    int k = 0;
    if (argc == 3)
    {
        while(argv[1][i] != '\\0')
        {
            i++;
        }
        while(argv[2][j] != '\\0')
        {
            argv[1][i] = argv[2][j];
            i++;
            j++;
        }
        i--;
        while(k <= i)
        {
            if(check(argv[1][k], argv[1], k) == 1)
                write (1, &argv[1][k], 1);
            k++;
        }
    }
    write (1, "\\n", 1);
}"""
            },
            {
                "level": 2, "name": "wdmatch", "file": "wdmatch.c",
                "allowed": "write",
                "description": """Write a program that takes two strings and checks whether it's possible to write the first string with characters from the second string, while respecting the order in which these characters appear in the second string.
If it's possible, the program displays the string, followed by a \\n, otherwise it simply displays a \\n.
If the number of arguments is not 2, the program displays a \\n.""",
                "code": """#include <unistd.h>

void ft_putstr(char const *str)
{
    int i = 0;
    while (str[i])
        write(1, &str[i++], 1);
}

int main(int argc, char const *argv[])
{
    int i = 0;
    int j = 0;
    if (argc == 3)
    {
        while (argv[2][j])
            if (argv[2][j++] == argv[1][i])
                i += 1;
        if (!argv[1][i])
            ft_putstr(argv[1]);
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            # Level 3
            {
                "level": 3, "name": "add_prime_sum", "file": "add_prime_sum.c",
                "allowed": "write, exit",
                "description": """Write a program that takes a positive integer as argument and displays the sum of all prime numbers inferior or equal to it followed by a newline.
If the number of arguments is not 1, or the argument is not a positive number, just display 0 followed by a newline.""",
                "code": """#include <unistd.h>

int is_prime(int num)
{
    int i = 3;
    if (num <= 1)
        return (0);
    if (num % 2 == 0 && num > 2)
        return (0);
    while (i < (num / 2))
    {
        if (num % i == 0)
            return 0;
        i += 2;
    }
    return 1;
}

int main(int argc, char *argv[])
{
    int sum = 0;
    int nb = ft_atoi(argv[1]);
    if (argc == 2)
    {
        while (nb > 0)
            if (is_prime(nb--))
                sum += (nb + 1);
        ft_putnbr(sum);
    }
    if (argc != 2)
        ft_putnbr(0);
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 3, "name": "epur_str", "file": "epur_str.c",
                "allowed": "write",
                "description": """Write a program that takes a string, and displays this string with exactly one space between words, with no spaces or tabs either at the beginning or the end, followed by a \\n.
A "word" is defined as a part of a string delimited either by spaces/tabs, or by the start/end of the string.
If the number of arguments is not 1, or if there are no words to display, the program displays \\n.""",
                "code": """#include <unistd.h>

int main(int argc, char const *argv[])
{
    int i;
    int flg;
    if (argc == 2)
    {
        i = 0;
        while (argv[1][i] == ' ' || argv[1][i] == '\\t')
            i += 1;
        while (argv[1][i])
        {
            if (argv[1][i] == ' ' || argv[1][i] == '\\t')
                flg = 1;
            if (!(argv[1][i] == ' ' || argv[1][i] == '\\t'))
            {
                if (flg)
                    write(1, " ", 1);
                flg = 0;
                write(1, &argv[1][i], 1);
            }
            i += 1;
        }
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 3, "name": "expand_str", "file": "expand_str.c",
                "allowed": "write",
                "description": """Write a program that takes a string and displays it with exactly three spaces between each word, with no spaces or tabs either at the beginning or the end, followed by a newline.
A word is a section of string delimited either by spaces/tabs, or by the start/end of the string.
If the number of parameters is not 1, or if there are no words, simply display a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char const *argv[])
{
    int i;
    int flag;
    if (argc == 2)
    {
        i = 0;
        while (argv[1][i] == ' ' || argv[1][i] == '\\t')
            i++;
        while (argv[1][i])
        {
            if (argv[1][i] == ' ' || argv[1][i] == '\\t')
                flag = 1;
            if (!(argv[1][i] == ' ' || argv[1][i] == '\\t'))
            {
                if (flag)
                    write(1, " ", 3);
                flag = 0;
                write(1, &argv[1][i], 1);
            }
            i++;
        }
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 3, "name": "ft_atoi_base", "file": "ft_atoi_base.c",
                "allowed": "None",
                "description": """Write a function that converts the string argument str (base N <= 16) to an integer (base 10) and returns it.
The characters recognized in the input are: 0123456789abcdef Those are, of course, to be trimmed according to the requested base. For example, base 4 recognizes "0123" and base 16 recognizes "0123456789abcdef".
Uppercase letters must also be recognized: "12fdb3" is the same as "12FDB3".
Minus signs ('-') are interpreted only if they are the first character of the string.
Your function must be declared as follows:
int ft_atoi_base(const char *str, int str_base);""",
                "code": """char to_lower(char c)
{
    if (c >= 'A' && c <= 'Z')
        return (c + ('a' - 'A'));
    return (c);
}

int get_digit(char c, int digits_in_base)
{
    int max_digit;
    if (digits_in_base <= 10)
        max_digit = digits_in_base + '0';
    else
        max_digit = digits_in_base - 10 + 'a';
    if (c >= '0' && c <= '9' && c <= max_digit)
        return (c - '0');
    else if (c >= 'a' && c <= 'f' && c <= max_digit)
        return (10 + c - 'a');
    else
        return (-1);
}

int ft_atoi_base(const char *str, int str_base)
{
    int result = 0;
    int sign = 1;
    int digit;
    if (*str == '-')
    {
        sign = -1;
        ++str;
    }
    while ((digit = get_digit(to_lower(*str), str_base)) >= 0)
    {
        result = result * str_base;
        result = result + (digit * sign);
        ++str;
    }
    return (result);
}"""
            },
            {
                "level": 3, "name": "ft_list_size", "file": "ft_list_size.c",
                "allowed": "",
                "description": """Write a function that returns the number of elements in the linked list that's passed to it.
It must be declared as follows:
int ft_list_size(t_list *begin_list);
You must use the following structure, and turn it in as a file called ft_list.h:
typedef struct s_list { struct s_list *next; void *data; } t_list;""",
                "code": """#include "ft_list.h"

int ft_list_size(t_list *begin_list)
{
    if (begin_list == 0)
        return (0);
    else
        return (1 + ft_list_size(begin_list->next));
}"""
            },
            {
                "level": 3, "name": "ft_range", "file": "ft_range.c",
                "allowed": "malloc",
                "description": """Write the following function:
int *ft_range(int start, int end);
It must allocate (with malloc()) an array of integers, fill it with consecutive values that begin at start and end at end (Including start and end !), then return a pointer to the first value of the array.
Examples:
With (1, 3) you will return an array containing 1, 2 and 3.
With (-1, 2) you will return an array containing -1, 0, 1 and 2.
With (0, 0) you will return an array containing 0.
With (0, -3) you will return an array containing 0, -1, -2 and -3.""",
                "code": """#include <stdlib.h>

int *ft_range(int start, int end)
{
    int i = 0;
    int len = abs((end - start)) + 1;
    int *res = (int *)malloc(sizeof(int) * len);
    while (i < len)
    {
        if (start < end)
        {
            res[i] = start;
            start++;
            i++;
        }
        else
        {
            res[i] = start;
            start--;
            i++;
        }
    }
    return (res);
}"""
            },
            {
                "level": 3, "name": "ft_rrange", "file": "ft_rrange.c",
                "allowed": "malloc",
                "description": """Write the following function:
int *ft_rrange(int start, int end);
It must allocate (with malloc()) an array of integers, fill it with consecutive values that begin at end and end at start (Including start and end !), then return a pointer to the first value of the array.
Examples:
With (1, 3) you will return an array containing 3, 2 and 1
With (-1, 2) you will return an array containing 2, 1, 0 and -1.
With (0, 0) you will return an array containing 0.
With (0, -3) you will return an array containing -3, -2, -1 and 0.""",
                "code": """#include <stdlib.h>

int *ft_rrange(int start, int end)
{
    int *range;
    int i = 0;
    int n = end - start + 1;
    if (start > end)
        return (ft_rrange(end, start));
    range = (int *)malloc(sizeof(int) * n);
    if (range)
    {
        while (i < n)
        {
            range[i] = end;
            end--;
            i++;
        }
    }
    return (range);
}"""
            },
            {
                "level": 3, "name": "hidenp", "file": "hidenp.c",
                "allowed": "write",
                "description": """Write a program named hidenp that takes two strings and displays 1 followed by a newline if the first string is hidden in the second one, otherwise displays 0 followed by a newline.
Let s1 and s2 be strings. We say that s1 is hidden in s2 if it's possible to find each character from s1 in s2, in the same order as they appear in s1. Also, the empty string is hidden in any string.
If the number of parameters is not 2, the program displays a newline.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i = 0;
    int j = 0;
    if (argc == 3)
    {
        while (argv[2][j] && argv[1][i])
        {
            if (argv[2][j] == argv[1][i])
                i++;
            j++;
        }
        if (argv[1][i] == '\\0')
            write(1, "1", 1);
        else
            write(1, "0", 1);
    }
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 3, "name": "lcm", "file": "lcm.c",
                "allowed": "",
                "description": """Write a function who takes two unsigned int as parameters and returns the computed LCM of those parameters.
LCM (Lowest Common Multiple) of two non-zero integers is the smallest postive integer divisible by the both integers.
If at least one integer is null, LCM is equal to 0.
Your function must be prototyped as follows:
unsigned int lcm(unsigned int a, unsigned int b);""",
                "code": """unsigned int lcm(unsigned int a, unsigned int b)
{
    unsigned int n;
    if (a == 0 || b == 0)
        return (0);
    if (a > b)
        n = a;
    else
        n = b;
    while (1)
    {
        if (n % a == 0 && n % b == 0)
            return (n);
        ++n;
    }
}"""
            },
            {
                "level": 3, "name": "paramsum", "file": "paramsum.c",
                "allowed": "write",
                "description": """Write a program that displays the number of arguments passed to it, followed by a newline.
If there are no arguments, just display a 0 followed by a newline.""",
                "code": """#include <unistd.h>

void ft_putnbr(int n)
{
    char digit;
    if (n >= 10)
        ft_putnbr(n / 10);
    digit = (n % 10) + '0';
    write(1, &digit, 1);
}

int main(int argc, char **argv)
{
    (void)argv;
    ft_putnbr(argc - 1);
    write(1, "\\n", 1);
    return (0);
}"""
            },
            {
                "level": 3, "name": "pgcd", "file": "pgcd.c",
                "allowed": "printf, atoi, malloc, free",
                "description": """Write a program that takes two strings representing two strictly positive integers that fit in an int.
Display their highest common denominator followed by a newline (It's always a strictly positive integer).
If the number of parameters is not 2, display a newline.""",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int string1 = atoi(argv[1]);
    int string2 = atoi(argv[2]);
    if (argc != 3)
    {
        printf("\\n");
        return 0;
    }
    if (string1 <= 0 || string2 <= 0)
    {
        printf("\\n");
        return 0;
    }
    while (string2 != 0)
    {
        int temporary = string2;
        string2 = string1 % string2;
        string1 = temporary;
    }
    printf("%d\\n", string1);
    return 0;
}"""
            },
            {
                "level": 3, "name": "print_hex", "file": "print_hex.c",
                "allowed": "write",
                "description": """Write a program that takes a positive (or zero) number expressed in base 10, and displays it in base 16 (lowercase letters) followed by a newline.
If the number of parameters is not 1, the program displays a newline.""",
                "code": """#include <unistd.h>

int ft_atoi(char *str)
{
    int n = 0;
    while (*str != '\\0')
    {
        n = n * 10;
        n = n + *str - '0';
        ++str;
    }
    return (n);
}

void print_hex(int n)
{
    char hex_digits[] = "0123456789abcdef";
    if (n >= 16)
        print_hex(n / 16);
    write(1, &hex_digits[n % 16], 1);
}

int main(int argc, char **argv)
{
    if (argc == 2)
        print_hex(ft_atoi(argv[1]));
    write(1, "\\n", 1);
}"""
            },
            {
                "level": 3, "name": "rstr_capitalizer", "file": "rstr_capitalizer.c",
                "allowed": "write",
                "description": """Write a program that takes one or more strings and, for each argument, puts the last character that is a letter of each word in uppercase and the rest in lowercase, then displays the result followed by a \\n.
A word is a section of string delimited by spaces/tabs or the start/end of the string. If a word has a single letter, it must be capitalized.
A letter is a character in the set [a-zA-Z]
If there are no parameters, display \\n.""",
                "code": """#include <unistd.h>

void rstr_capitalizer(char *str)
{
    int i = 0;
    while (str[i])
    {
        if (str[i] >= 'A' && str[i] <= 'Z')
            str[i] += 32;
        if ((str[i] >= 'a' && str[i] <= 'z') && (str[i + 1] == ' ' || str[i + 1] == '\\t' || str[i + 1] == '\\0'))
            str[i] -= 32;
        write(1, &str[i++], 1);
    }
}

int main(int argc, char **argv)
{
    int i;
    if (argc == 1)
        write(1, "\\n", 1);
    else
    {
        i = 1;
        while (i < argc)
        {
            rstr_capitalizer(argv[i]);
            write(1, "\\n", 1);
            i += 1;
        }
    }
    return (0);
}"""
            },
            {
                "level": 3, "name": "str_capitalizer", "file": "str_capitalizer.c",
                "allowed": "write",
                "description": """Write a program that takes one or several strings and, for each argument, capitalizes the first character of each word (If it's a letter, obviously), puts the rest in lowercase, and displays the result on the standard output, followed by a \\n.
A "word" is defined as a part of a string delimited either by spaces/tabs, or by the start/end of the string. If a word only has one letter, it must be capitalized. If there are no arguments, the progam must display \\n.""",
                "code": """#include <unistd.h>

void str_capitalizer(char *str)
{
    int i = 0;
    if (str[i] >= 'a' && 'z' >= str[i])
        str[i] -= 32;
    write(1, &str[i], 1);
    while (str[++i])
    {
        if (str[i] >= 'A' && 'Z' >= str[i])
            str[i] += 32;
        if ((str[i] >= 'a' && 'z' >= str[i]) && (str[i - 1] == ' ' || str[i - 1] == '\\t'))
            str[i] -= 32;
        write(1, &str[i], 1);
    }
}

int main(int argc, char *argv[])
{
    int i;
    if (argc < 2)
        write(1, "\\n", 1);
    else
    {
        i = 1;
        while (i < argc)
        {
            str_capitalizer(argv[i]);
            write(1, "\\n", 1);
            i += 1;
        }
    }
    return (0);
}"""
            },
            {
                "level": 3, "name": "tab_mult", "file": "tab_mult.c",
                "allowed": "write",
                "description": """Write a program that displays a number's multiplication table.
The parameter will always be a strictly positive number that fits in an int, and said number times 9 will also fit in an int.
If there are no parameters, the program displays \\n.""",
                "code": """#include <unistd.h>

int ft_atoi(char *str)
{
    int result;
    int sign;
    result = 0;
    sign = 1;
    while (*str == ' ' || (*str >= 9 && *str <= 13))
        str++;
    if (*str == '-')
        sign = -1;
    if (*str == '-' || *str == '+')
        str++;
    while (*str >= '0' && *str <= '9')
    {
        result = result * 10 + *str - '0';
        str++;
    }
    return (sign * result);
}

void ft_putchar(char c)
{
    write(1, &c, 1);
}

void ft_putnbr(int nb)
{
    if (nb == -2147483648)
    {
        ft_putchar('-');
        ft_putchar('2');
        nb = (nb % 1000000000 * -1);
    }
    if (nb < 0)
    {
        ft_putchar('-');
        nb = (nb * -1);
    }
    if (nb / 10 > 0)
        ft_putnbr(nb / 10);
    ft_putchar(nb % 10 + '0');
}

int main(int argc, char *argv[])
{
    int i;
    int nbr;
    if (argc != 2)
        write(1, "\\n", 1);
    else
    {
        i = 1;
        nbr = ft_atoi(argv[1]);
        while (i <= 9)
        {
            ft_putnbr(i);
            write(1, " x ", 3);
            ft_putnbr(nbr);
            write(1, " = ", 3);
            ft_putnbr(i * nbr);
            write(1, "\\n", 1);
            i += 1;
        }
    }
    return (0);
}"""
            },
            # Level 4
            {
                "level": 4, "name": "flood_fill", "file": "flood_fill.c",
                "allowed": "-",
                "description": """Write a function that takes a char ** as a 2-dimensional array of char, a t_point as the dimensions of this array and a t_point as the starting point.
Starting from the given 'begin' t_point, this function fills an entire zone by replacing characters inside with the character 'F'. A zone is an group of the same character delimited horizontally and vertically by other characters or the array boundary.
The flood_fill function won't fill diagonally.
The flood_fill function will be prototyped like this: void flood_fill(char **tab, t_point size, t_point begin);""",
                "code": """typedef struct s_point
{
    int x;
    int y;
} t_point;

void fill(char **tab, t_point size, t_point cur, char to_fill)
{
    if (cur.y < 0 || cur.y >= size.y || cur.x < 0 || cur.x >= size.x
        || tab[cur.y][cur.x] != to_fill)
        return;
    tab[cur.y][cur.x] = 'F';
    fill(tab, size, (t_point){cur.x - 1, cur.y}, to_fill);
    fill(tab, size, (t_point){cur.x + 1, cur.y}, to_fill);
    fill(tab, size, (t_point){cur.x, cur.y - 1}, to_fill);
    fill(tab, size, (t_point){cur.x, cur.y + 1}, to_fill);
}

void flood_fill(char **tab, t_point size, t_point begin)
{
    fill(tab, size, begin, tab[begin.y][begin.x]);
}"""
            },
            {
                "level": 4, "name": "fprime", "file": "fprime.c",
                "allowed": "printf, atoi",
                "description": """Write a program that takes a positive int and displays its prime factors on the standard output, followed by a newline.
Factors must be displayed in ascending order and separated by '*', so that the expression in the output gives the right result.
If the number of parameters is not 1, simply display a newline.
The input, when there is one, will be valid.""",
                "code": """#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;
    int number;
    if (argc == 2)
    {
        i = 1;
        number = atoi(argv[1]);
        if (number == 1)
            printf("1");
        while (number >= ++i)
        {
            if (number % i == 0)
            {
                printf("%d", i);
                if (number == i)
                    break ;
                printf("*");
                number /= i;
                i = 1;
            }
        }
    }
    printf("\\n");
    return (0);
}"""
            },
            {
                "level": 4, "name": "ft_itoa", "file": "ft_itoa.c",
                "allowed": "malloc",
                "description": """Write a function that takes an int and converts it to a null-terminated string. The function returns the result in a char array that you must allocate.
Your function must be declared as follows: char *ft_itoa(int nbr);""",
                "code": """#include <stdlib.h>

char *ft_itoa(int nbr)
{
    int n = nbr;
    int len = 0;
    if (nbr <= 0)
        len++;
    while (n)
    {
        n /= 10;
        len++;
    }
    char *result = (char *)malloc(sizeof(char) * (len + 1));
    if (result == NULL)
    {
        return NULL;
    }
    result[len] = '\\0';
    if (nbr == 0)
    {
        result[0] = '0';
        return(result);
    }
    if (nbr < 0)
    {
        result[0] = '-';
        nbr = -nbr;
    }
    while (nbr)
    {
        result[--len] = nbr % 10 + '0';
        nbr /= 10;
    }
    return result;
}"""
            },
            {
                "level": 4, "name": "ft_list_foreach", "file": "ft_list_foreach.c",
                "allowed": "",
                "description": """Write a function that takes a list and a function pointer, and applies this function to each element of the list.
It must be declared as follows:
void ft_list_foreach(t_list *begin_list, void (*f)(void *));
The function pointed to by f will be used as follows:
(*f)(list_ptr->data);
You must use the following structure, and turn it in as a file called ft_list.h:
typedef struct s_list { struct s_list *next; void *data; } t_list;""",
                "code": """#include "ft_list.h"

void ft_list_foreach(t_list *begin_list, void (*f)(void *))
{
    t_list *list_ptr;
    list_ptr = begin_list;
    while (list_ptr)
    {
        (*f)(list_ptr->data);
        list_ptr = list_ptr->next;
    }
}"""
            },
            {
                "level": 4, "name": "ft_list_remove_if", "file": "ft_list_remove_if.c",
                "allowed": "free",
                "description": """Write a function called ft_list_remove_if that removes from the passed list any element the data of which is "equal" to the reference data.
It will be declared as follows :
void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)());
cmp takes two void* and returns 0 when both parameters are equal.
You have to use the ft_list.h file.""",
                "code": """#include <stdlib.h>
#include "ft_list.h"

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{
    if (begin_list == NULL || *begin_list == NULL)
        return;
    t_list *cur = *begin_list;
    if (cmp(cur->data, data_ref) == 0)
    {
        *begin_list = cur->next;
        free(cur);
        ft_list_remove_if(begin_list, data_ref, cmp);
    }
    cur = *begin_list;
    ft_list_remove_if(&cur->next, data_ref, cmp);
}"""
            },
            {
                "level": 4, "name": "ft_split", "file": "ft_split.c",
                "allowed": "malloc",
                "description": """Write a function that takes a string, splits it into words, and returns them as a NULL-terminated array of strings.
A "word" is defined as a part of a string delimited either by spaces/tabs/new lines, or by the start/end of the string.
Your function must be declared as follows:
char **ft_split(char *str);""",
                "code": """#include <stdlib.h>

char *ft_strncpy(char *s1, char *s2, int n)
{
    int i = -1;
    while (++i < n && s2[i])
        s1[i] = s2[i];
    s1[i] = '\\0';
    return (s1);
}

char **ft_split(char *str)
{
    int i = 0;
    int j = 0;
    int k = 0;
    int wc = 0;
    while (str[i])
    {
        while (str[i] && (str[i] == ' ' || str[i] == '\\t' || str[i] == '\\n'))
            i++;
        if (str[i])
            wc++;
        while (str[i] && (str[i] != ' ' && str[i] != '\\t' && str[i] != '\\n'))
            i++;
    }
    char **out = (char **)malloc(sizeof(char *) * (wc + 1));
    i = 0;
    while (str[i])
    {
        while (str[i] && (str[i] == ' ' || str[i] == '\\t' || str[i] == '\\n'))
            i++;
        j = i;
        while (str[i] && (str[i] != ' ' && str[i] != '\\t' && str[i] != '\\n'))
            i++;
        if (i > j)
        {
            out[k] = (char *)malloc(sizeof(char) * ((i - j) + 1));
            ft_strncpy(out[k++], &str[j], i - j);
        }
    }
    out[k] = NULL;
    return (out);
}"""
            },
            {
                "level": 4, "name": "rev_wstr", "file": "rev_wstr.c",
                "allowed": "write, malloc, free",
                "description": """Write a program that takes a string as a parameter, and prints its words in reverse order. A "word" is a part of the string bounded by spaces and/or tabs, or the begin/end of the string.
If the number of parameters is different from 1, the program will display '\\n'.
In the parameters that are going to be tested, there won't be any "additional" spaces (meaning that there won't be additional spaces at the beginning or at the end of the string, and words will always be separated by exactly one space).""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int start;
    int end;
    int i = 0;
    if(argc == 2)
    {
        while(argv[1][i] != '\\0')
            i++;
        while(i >= 0)
        {
            while( argv[1][i] == '\\0' || argv[1][i] == ' ' || argv[1][i] == '\\t')
                i--;
            end = i;
            while(argv[1][i] && argv[1][i] != ' ' && argv[1][i] != '\\t')
                i--;
            start = i + 1;
            int flag;
            flag = start;
            while(start <= end)
            {
                write (1, &argv[1][start],1);
                start++;
            }
            if (flag !=0)
            {
                write(1, " ", 1);
            }
        }
    }
    write(1, "\\n", 1);
}"""
            },
            {
                "level": 4, "name": "rostring", "file": "rostring.c",
                "allowed": "write, malloc, free",
                "description": """Write a program that takes a string and displays this string after rotating it one word to the left.
Thus, the first word becomes the last, and others stay in the same order.
A "word" is defined as a part of a string delimited either by spaces/tabs, or by the start/end of the string.
Words will be separated by only one space in the output.
If there's less than one argument, the program displays \\n.""",
                "code": """#include <unistd.h>

int main(int argc, char **argv)
{
    int i;
    int start;
    int end;
    int flag;
    flag = 0;
    if (argc > 1 && argv[1][0])
    {
        i = 0;
        while (argv[1][i] == ' ' || argv[1][i] == '\\t')
            i++;
        start = i;
        while (argv[1][i] != '\\0' && argv[1][i] != ' ' && argv[1][i] != '\\t')
            i++;
        end = i;
        while(argv[1][i])
        {
            while (argv[1][i] == ' ' || argv[1][i] == '\\t')
                i++;
            if (argv[1][i])
            {
                while ((argv[1][i] == ' ' && argv[1][i + 1] == ' ') ||
                       (argv[1][i] == '\\t' && argv[1][i + 1] == '\\t'))
                    i++;
                if (argv[1][i] == ' ' || argv[1][i] == '\\t')
                    flag = 1;
                write(1, &argv[1][i], 1);
                i++;
            }
        }
        if (flag)
            write(1, " ", 1);
        while (start < end)
        {
            write(1, &argv[1][start], 1);
            start++;
        }
    }
    write(1, "\\n", 1);
    return(0);
}"""
            },
            {
                "level": 4, "name": "sort_int_tab", "file": "sort_int_tab.c",
                "allowed": "",
                "description": """Write the following function:
void sort_int_tab(int *tab, unsigned int size);
It must sort (in-place) the 'tab' int array, that contains exactly 'size' members, in ascending order.
Doubles must be preserved.
Input is always coherent.""",
                "code": """void sort_int_tab(int *tab, unsigned int size)
{
    unsigned int i = 0;
    int temp;
    while (i < (size - 1))
    {
        if (tab[i] > tab[i + 1])
        {
            temp = tab[i];
            tab[i] = tab[i+ 1];
            tab[i + 1] = temp;
            i = 0;
        }
        else
            i++;
    }
}"""
            },
            {
                "level": 4, "name": "sort_list", "file": "sort_list.c",
                "allowed": "",
                "description": """Write the following functions:
t_list *sort_list(t_list *lst, int (*cmp)(int, int));
This function must sort the list given as a parameter, using the function pointer cmp to select the order to apply, and returns a pointer to the first element of the sorted list.
Duplications must remain.
Inputs will always be consistent.
You must use the type t_list described in the file list.h that is provided to you. You must include that file (#include "list.h"), but you must not turn it in. We will use our own to compile your assignment.
Functions passed as cmp will always return a value different from 0 if a and b are in the right order, 0 otherwise.
For example, the following function used as cmp will sort the list in ascending order:
int ascending(int a, int b) { return (a <= b); }""",
                "code": """typedef struct s_list t_list;

struct s_list
{
    int data;
    t_list *next;
};

#include "list.h"

t_list *sort_list(t_list *lst, int (*cmp)(int, int))
{
    int swap;
    t_list *tmp;
    tmp = lst;
    while(lst->next != NULL)
    {
        if (((*cmp)(lst->data, lst->next->data)) == 0)
        {
            swap = lst->data;
            lst->data = lst->next->data;
            lst->next->data = swap;
            lst = tmp;
        }
        else
            lst = lst->next;
    }
    lst = tmp;
    return (lst);
}"""
            },
        ]
        return exercises

    def create_exercise_page(self, level, exercise):
        """Create a single exercise page with full content"""
        # Exercise title
        title = Paragraph(
            f"<b>{exercise['name']}</b>",
            self.styles['CustomExerciseTitle']
        )
        self.story.append(title)
        
        # Exercise details
        details = Paragraph(
            f"<b>Level:</b> {level} | "
            f"<b>File:</b> {exercise['file']} | "
            f"<b>Allowed functions:</b> {exercise['allowed'] or 'None specified'}",
            self.styles['CustomExerciseDetails']
        )
        self.story.append(details)
        self.story.append(Spacer(1, 0.1*inch))
        
        # Description
        desc_lines = exercise['description'].split('\n')
        for line in desc_lines:
            if line.strip():
                desc = Paragraph(line.strip(), self.styles['CustomDescription'])
                self.story.append(desc)
        self.story.append(Spacer(1, 0.1*inch))
        
        # Code
        if exercise['code']:
            code_lines = exercise['code'].split('\n')
            for line in code_lines:
                if line.strip():
                    # Escape special characters for XML
                    line_escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    code_paragraph = Paragraph(
                        f"<font face='Courier' size='8'>{line_escaped}</font>",
                        self.styles['CustomCodeBlock']
                    )
                    self.story.append(code_paragraph)
                else:
                    self.story.append(Spacer(1, 0.05*inch))
        
        # Add a page break after each exercise
        self.story.append(PageBreak())

    def create_toc(self, exercises_by_level):
        """Create a table of contents"""
        self.story.append(Spacer(1, 0.5*inch))
        toc_title = Paragraph("📚 Table of Contents", self.styles['CustomTitle'])
        self.story.append(toc_title)
        self.story.append(Spacer(1, 0.3*inch))
        
        for level, exercises in sorted(exercises_by_level.items()):
            # Level heading in TOC
            level_title = Paragraph(
                f"<b>Level {level}</b>",
                self.styles['CustomLevelTitle']
            )
            self.story.append(level_title)
            
            # List exercises for this level
            for ex in exercises:
                entry = Paragraph(
                    f"• {ex['name']}",
                    self.styles['CustomTOCEntry']
                )
                self.story.append(entry)
            self.story.append(Spacer(1, 0.1*inch))
        
        self.story.append(PageBreak())

    def create_title_page(self):
        """Create the title page"""
        title = Paragraph(
            "<b>Programming Exercises</b>",
            self.styles['CustomTitle']
        )
        self.story.append(title)
        self.story.append(Spacer(1, 0.2*inch))
        
        subtitle = Paragraph(
            "Complete Collection of C Programming Exercises",
            self.styles['CustomTitle']
        )
        self.story.append(subtitle)
        self.story.append(Spacer(1, 0.5*inch))
        
        info = Paragraph(
            "Organized by Difficulty Level<br/><br/>"
            "Each exercise on a separate page<br/><br/>"
            "Includes full description and code",
            self.styles['CustomDescription']
        )
        self.story.append(info)
        
        self.story.append(PageBreak())

    def generate_pdf(self):
        """Generate the complete PDF document"""
        self.setup_styles()
        
        # Create PDF document
        self.doc = SimpleDocTemplate(
            self.filename,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
        )
        
        # Get all exercises
        exercises = self.get_exercise_data()
        
        # Group exercises by level
        exercises_by_level = {}
        for ex in exercises:
            level = ex['level']
            if level not in exercises_by_level:
                exercises_by_level[level] = []
            exercises_by_level[level].append(ex)
        
        # Create the document
        self.create_title_page()
        self.create_toc(exercises_by_level)
        
        # Add exercises by level
        for level, ex_list in sorted(exercises_by_level.items()):
            # Level separator page (always starts on odd page)
            self.story.append(PageBreak())
            
            # Level title
            level_title = Paragraph(
                f"Level {level}",
                self.styles['CustomLevelTitle']
            )
            self.story.append(level_title)
            
            # Level description
            desc = Paragraph(
                f"Exercises at Level {level} difficulty.",
                self.styles['CustomDescription']
            )
            self.story.append(desc)
            self.story.append(PageBreak())
            
            # Add each exercise
            for ex in ex_list:
                self.create_exercise_page(level, ex)
        
        # Build the PDF
        self.doc.build(self.story)
        print(f"✅ PDF generated: {self.filename}")
        return self.filename

def main():
    """Main function to generate the PDF"""
    try:
        from reportlab.lib.pagesizes import letter
        print("📄 Generating exercise PDF with full content...")
        pdf = ExercisePDF("exercises_formatted.pdf")
        pdf.generate_pdf()
        print("📂 File: exercises_formatted.pdf")
        print(f"📊 Total exercises: {len(pdf.get_exercise_data())}")
    except ImportError:
        print("❌ Error: reportlab library not found.")
        print("Please install it with: pip install reportlab")
        return 1
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return 1
    return 0

if __name__ == "__main__":
    exit(main())

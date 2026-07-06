*This project was created as part of the 42 curriculum by clopez-b.*

## Description 📚

`ft_printf` is a recreation of a small, useful part of the standard `printf`: a variadic function that formats and writes text to standard output based on a format string. The point of the project is to understand how variadic functions work (`stdarg.h`, `va_list`, `va_arg`) and how a format string is parsed conversion by conversion.

This implementation supports the conversions required by the subject:

| Conversion | Meaning                          |
|------------|-----------------------------------|
| `%c`       | character                         |
| `%s`       | string                            |
| `%p`       | pointer (in `0x...` hex form)      |
| `%d` / `%i`| signed decimal integer            |
| `%u`       | unsigned decimal integer          |
| `%x` / `%X`| unsigned hexadecimal (lower/upper)|
| `%%`       | a literal `%`                     |

Flags, width and precision are not part of the mandatory subject and are not implemented here.

## How it works

`ft_printf` walks the format string character by character. Plain characters are written as-is; whenever it finds a `%` followed by a known conversion, it pulls the next argument out of the `va_list` and delegates to a small helper (`ft_putchar_count`, `ft_putstr_count`, `ft_putnbr_count`, `ft_putunbr_count`, `ft_puthex_count`, `ft_putptr_count`) that writes the value and returns how many characters it wrote. `ft_printf` adds up those counts, exactly like the real `printf` does, and returns the total.

## Files

- `ft_printf.h` — public prototype and helper declarations.
- `ft_printf.c` — parses the format string and dispatches each conversion.
- `ft_putchar_count.c` / `ft_putstr_count.c` — character and string output.
- `ft_putnbr_count.c` / `ft_putunbr_count.c` — signed and unsigned decimal integers.
- `ft_puthex_count.c` — unsigned hexadecimal output, lower and upper case.
- `ft_putptr_count.c` — pointer output (`0x` prefix + hexadecimal address).
- `main_test.c` — test program that runs the same format/arguments through `ft_printf` and the libc `printf`, captures both outputs and return values, and diffs them.

## Instructions

### Build the library

```bash
make
```

This produces `libftprintf.a`.

### Run the tests

```bash
make test
./printf_test
```

This compiles `main_test.c` against `libftprintf.a` and compares every test case with the libc `printf`, both in output and return value.

### Clean

```bash
make clean   # removes object files
make fclean  # removes object files, the library and the test binary
make re      # fclean + all
```

### Using it in another project

```c
#include "ft_printf.h"
```

```bash
cc -L. -lftprintf your_files.c -o program
```

## Resources

- `man 3 printf` and `man 3 stdarg` for the reference behaviour and the variadic argument API.
- The 42 `ft_printf` subject documentation.
- The C Handbook by Flavio Copes.

### Use of AI

AI was only used to write the `main_test` file in order to save time. It was not used to implement `ft_printf` itself or to design the parsing/dispatch logic.

## Additional Notes

Like `get_next_line`, this project reimplements its own tiny helpers instead of depending on Libft, since the 42 subject requires `ft_printf` to be self-contained.

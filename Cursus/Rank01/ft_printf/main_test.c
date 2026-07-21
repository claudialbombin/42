#include "ft_printf.h"
#include <limits.h>
#include <stddef.h>

int	main(void)
{
	char	*str;
	void	*ptr;

	str = "hello world";
	ptr = &str;
	ft_printf("Char: [%c]\n", 'A');
	ft_printf("String: [%s]\n", str);
	ft_printf("Null string: [%s]\n", (char *)NULL);
	ft_printf("Positive int: [%d]\n", 42);
	ft_printf("Negative int: [%i]\n", -42);
	ft_printf("Zero: [%d]\n", 0);
	ft_printf("INT_MIN: [%d]\n", INT_MIN);
	ft_printf("Unsigned: [%u]\n", 4294967295u);
	ft_printf("Hex lower: [%x]\n", 255);
	ft_printf("Hex upper: [%X]\n", 255);
	ft_printf("Pointer: [%p]\n", ptr);
	ft_printf("Null pointer: [%p]\n", (void *)NULL);
	ft_printf("Percent: [%%]\n");
	ft_printf("Mixed: [%s] has %d items (%x hex, %u unsigned)\n", "cart", 7, 7, 7);
	return (0);
}

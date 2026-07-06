#include "ft_printf.h"
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

static int	g_tests;
static int	g_passed;

static void	capture_start(int *saved_stdout, const char *path)
{
	int	fd;

	fflush(stdout);
	*saved_stdout = dup(1);
	fd = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
	dup2(fd, 1);
	close(fd);
}

static void	capture_stop(int saved_stdout, char *buf, const char *path)
{
	int		fd;
	ssize_t	n;

	fflush(stdout);
	dup2(saved_stdout, 1);
	close(saved_stdout);
	buf[0] = '\0';
	fd = open(path, O_RDONLY);
	if (fd < 0)
		return ;
	n = read(fd, buf, 1023);
	if (n < 0)
		n = 0;
	buf[n] = '\0';
	close(fd);
	remove(path);
}

static void	run_test(const char *name, int ft_ret, int libc_ret,
		char *ft_buf, char *libc_buf)
{
	g_tests++;
	if (ft_ret == libc_ret && strcmp(ft_buf, libc_buf) == 0)
	{
		g_passed++;
		printf("[OK]   %s\n", name);
	}
	else
	{
		printf("[FAIL] %s (ft_ret=%d libc_ret=%d)\n", name, ft_ret, libc_ret);
		printf("       ft:   \"%s\"\n", ft_buf);
		printf("       libc: \"%s\"\n", libc_buf);
	}
}

# define TEST(name, fmt, ...) do { \
		int		saved; \
		int		ft_ret; \
		int		libc_ret; \
		char	ft_buf[1024]; \
		char	libc_buf[1024]; \
		capture_start(&saved, "ft_printf_ft.tmp"); \
		ft_ret = ft_printf(fmt, ##__VA_ARGS__); \
		capture_stop(saved, ft_buf, "ft_printf_ft.tmp"); \
		capture_start(&saved, "ft_printf_libc.tmp"); \
		libc_ret = printf(fmt, ##__VA_ARGS__); \
		capture_stop(saved, libc_buf, "ft_printf_libc.tmp"); \
		run_test(name, ft_ret, libc_ret, ft_buf, libc_buf); \
	} while (0)

int	main(void)
{
	int		n;
	char	*s;
	void	*p;
	char	*null_str;

	null_str = NULL;
	TEST("char", "%c", 'A');
	TEST("string", "%s", "hello world");
	TEST("null string", "%s", null_str);
	TEST("positive int", "%d", 42);
	TEST("negative int", "%i", -42);
	TEST("zero", "%d", 0);
	n = -2147483648;
	TEST("INT_MIN", "%d", n);
	TEST("unsigned", "%u", 4294967295u);
	TEST("hex lower", "%x", 255);
	TEST("hex upper", "%X", 255);
	s = "abc";
	p = &s;
	TEST("pointer", "%p", p);
	TEST("null pointer", "%p", (void *)NULL);
	TEST("percent", "%%");
	TEST("mixed", "[%s] has %d items (%x hex, %u unsigned)\n", "cart", 7, 7, 7);
	printf("\n%d/%d tests passed\n", g_passed, g_tests);
	if (g_passed != g_tests)
		return (1);
	return (0);
}

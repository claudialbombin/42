def ft_count_harvest_recursive_helper(i: int, days: int) -> None:
    if i > days:
        return
    print(f'Day {i}')
    ft_count_harvest_recursive_helper(i + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input('Days until harvest: '))
    if days >= 1:
        ft_count_harvest_recursive_helper(1, days)
    print('Harvest time!')

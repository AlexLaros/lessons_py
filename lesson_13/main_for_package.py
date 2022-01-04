from package_for_all_occasions import assorted_module as assort
from package_for_all_occasions import search_in_list as search

print(assort.is_this_the_leap_year(1968), "\n")
print(assort.there_are_the_same_neighbours(1223), "\n")
print(assort.there_are_the_same_numbers(1232), "\n")

lst = [1, 2, 3, 4, 5]
a = 7
print(search.find_sum(lst, a))

s = """
           I don't care if it hurts
           I wanna have control
           I want a perfect body
           I want a perfect soul
           I want you to notice
           When I'm not around
           So very special
           I wish I was special
"""
print(search.find_max_repeat_word(s), "\n")
for i in search.find_prime(1, 200):
    print(i, end=' ')

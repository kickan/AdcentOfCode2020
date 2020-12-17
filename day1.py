
#Part one --- find the two elements from the list that add up to 2020, then multiply them --------------------------------------------
def add_two_elements_sum_2020(input_list):
    lenght_list = len(input_list)
    for first in range(lenght_list):
        for seccond in range(first+1,lenght_list):
            add_sum = input_list[first] + input_list[seccond]
            if add_sum == 2020:
                multiply_sum = input_list[first] * input_list[seccond]
                return("the sum of the two elements is: ", multiply_sum)

# Part two --- find the three elements from the list that add up to 2020, then multiply them --------------------------------------------------------------
def add_three_elements_sum_2020(input_list):
    lenght_list = len(input_list)
    for first in range(lenght_list):
        for seccond in range(first+1,lenght_list):
            for third in range (seccond+1, lenght_list):
                add_sum = input_list[first] + input_list[seccond] + input_list[third]
                if add_sum == 2020:
                    multiply_sum = input_list[first] * input_list[seccond] * input_list[third]
                    return("the sum of the three elements is: ", multiply_sum)

my_input = []
with open("C:/Users/krist/Documents/code/adventofcode/inputday1.txt","rU") as file:
    my_input = [int(x) for x in file.read().split()]

print(add_two_elements_sum_2020(my_input))
print(add_three_elements_sum_2020(my_input))
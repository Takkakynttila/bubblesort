from matplotlib import pyplot as plt
import random as rd


def main():
    #swap function
    def swap(index1, list):
          x = list[index1 + 1]
          list[index1 + 1] = list[index1]
          list[index1] = x
          return list

    #create and populate a list based on input
    amount_of_numbers = input("How many numbers to sort? ")
    numbers_list = [rd.randint(0,1000) for i in range(0, int(amount_of_numbers))]
    print(numbers_list)

    counter = 0
    for i in range(len(numbers_list)):
        for j in range(0, len(numbers_list)-i-1):
            counter +=1
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list = swap(j, numbers_list)
                plt.plot(numbers_list)
                plt.pause(0.05)

    plt.show()
    print(numbers_list)
    print('Amount of passes: ' + str(counter))

if __name__ == '__main__':
    main()

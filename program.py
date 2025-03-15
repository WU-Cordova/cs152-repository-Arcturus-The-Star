from datastructures.array import Array
from datastructures.bag import Bag


def main():
    bag = Bag([1,2,3,4,5,5,5,5,5])
    ar = Array([1,2,3,4,5], int)
    print(f"Array={ar}, bagged array={array_to_bag(ar)}")
    print(f"Bag={bag}, arrayed bag={bag_to_array(bag)}")

def array_to_bag(array:Array)->Bag:
    bag = Bag()
    for item in array:
        bag.add(item)
    return bag

def bag_to_array(bag:Bag)->Array:
    t = type(next(bag.distinct_items()))
    array = Array([], t)
    for item in bag.distinct_items():
        array.append(item)
    return array



if __name__ == '__main__':
    main()

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    for index, item in enumerate(weights):
      check_if_match = hash_table_retrieve(ht, limit-item)
      if check_if_match is not None:
        if index > check_if_match:
          return (index, check_if_match)
        return (check_if_match, index)
      else:
        hash_table_insert(ht, item, index)
    
    return None


# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")

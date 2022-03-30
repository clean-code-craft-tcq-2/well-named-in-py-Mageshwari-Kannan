import get_color_from_pair_number
import get_pair_number_from_color
import test_number_to_pair
import test_pair_to_number
import color_pair_to_string
from reference_manual import reference_manual

if __name__ == '__main__':
  test_number_to_pair.test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair.test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number.test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number.test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number.test_pair_to_number('Red', 'Orange', 7)
  reference_manual()
  print('Done :)')

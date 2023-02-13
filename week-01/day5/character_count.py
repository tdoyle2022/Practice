def char_count(str):
  char_dict = {}

  for char in str:
    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1
  
  cdk = char_dict.keys()
  cdv = char_dict.values()
  #print(cdk,cdv)
  result = zip(cdk,cdv)
  
  print(list(result))
  return list(result)
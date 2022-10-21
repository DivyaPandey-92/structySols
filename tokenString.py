def token_replace(s, tokens):
  pass # todo
  i=0
  j=1
  new_string=''
  while i < len(s):
  # while j<len(s):
    if s[i]=='$':
      if s[j]=='$':
        value=s[i:j+1]
        # new_string[i:j+1]=tokens[value]
        new_string+=tokens[value]
        i=j+1
        j=i+1
          
      else:
        j+=1
        
      #   value=s[i:j+1]
      #   new_string[i:j]=tokens[value]
      #   i=j+1
      #   j=i+1
    else:
      new_string+=s[i]
      i+=1
      j+=1
  return new_string
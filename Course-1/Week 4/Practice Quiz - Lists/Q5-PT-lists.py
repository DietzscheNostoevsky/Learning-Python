def group_list(group, users):

  groupname = group
  usernames = users
  #print(type(groupname))
  #print(type(usernames))

  returnstr = groupname + ": "
  for user in usernames  : 
    returnstr = returnstr + user + " "



  return returnstr

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
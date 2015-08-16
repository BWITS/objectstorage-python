#!/usr/bin/env python

import swiftclient


def main():
  user = "testuser:swift"
  key = "Rn1qOp0IQkxcT1FCDezaqxmpGmIUbw7bkpXeF31J"
  authurl = "http://127.0.0.1:80/auth"

  conn = swiftclient.Connection(
    user=user,
    key=key,
    authurl=authurl
  )

  print("Create test_container")
  conn.put_container("test_container")

  print("List all containers")
  print(conn.get_account()[1])

  print("Put test_object in test_container")
  conn.put_object("test_container", 'test_object',  contents="this is test object", content_type='text/plain')

  print("Download test_object")
  test_object_tuple = conn.get_object("test_container", "test_object")
  print(test_object_tuple[1])
  with open('./test_object', 'w') as myfile:
    myfile.write(test_object_tuple[1])

  print("Delete test_object")
  conn.delete_object("test_container", "test_object")

  print("Delete test_container")
  conn.delete_container("test_container")

if __name__ == "__main__":
  main()

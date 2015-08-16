#!/usr/bin/env python

import cloudfiles

def main():

  user = "testuser:swift"
  key = "Rn1qOp0IQkxcT1FCDezaqxmpGmIUbw7bkpXeF31J"
  authurl = "http://127.0.0.1:80/auth"
  authurl = "http://192.168.59.103:80/auth"

  conn = cloudfiles.get_connection(username=user, api_key=key, authurl=authurl)

  print("Create test_container")
  test_container = conn.create_container('test_container')

  print("List all containers")
  print(conn.get_all_containers())

  print("Put test_object in test_container")
  test_object = test_container.create_object("test_object")
  test_object.content_type = "text/plain"
  test_object.load_from_filename("/etc/ceph/ceph.conf")
  
  print("List all objects in test_container")
  print(test_container.get_objects())

  print("Download test_object")
  test_object = test_container.get_object("test_object")
  test_object.save_to_filename('./test_object')

  print("Delete test_object")
  test_container.delete_object("test_object")

  print("Delete test_container")
  conn.delete_container("test_container")

if __name__ == "__main__":
  main()




#!/usr/bin/env python

import boto
import boto.s3.connection


def main():
  access_key = "686GRF5C82LWNTKS08P7"
  secret_key = "oC2NJMbExPNe+SAqBYerEi3ruRrFh7dexklb4Qk3"

  host = "127.0.0.1"
  host = "192.168.59.103"
  port = 80
 
  conn = boto.connect_s3(aws_access_key_id = access_key, aws_secret_access_key = secret_key, host = host, port = port, is_secure=False, calling_format = boto.s3.connection.OrdinaryCallingFormat())

  print("Create test_bucket")
  test_bucket = conn.create_bucket("test_bucket")

  print("List all buckets")
  print(conn.get_all_buckets())

  print("Create test_object in test_bucket")
  test_object = test_bucket.new_key('test_object')
  test_object.set_contents_from_string('This is test object')

  print("List all object in test_bucket")
  print(test_bucket.list())

  print("Download test_object to file")
  test_object = test_bucket.get_key('test_object')
  test_object.get_contents_to_filename('./test_object')

  print("Get download url of test_object")
  test_object = test_bucket.get_key('test_object')
  print(test_object.generate_url(0, query_auth=False, force_http=True))
  print(test_object.generate_url(3600, query_auth=True, force_http=True))
  
  print("Delete test_object")
  test_bucket.delete_key('test_object')

  print("Delete test_bucket")
  conn.delete_bucket(test_bucket.name)

if __name__ == "__main__":
    main()

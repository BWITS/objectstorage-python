# Cloudfiles

## Introduction

[cloudfile]() is the python library to access swift object storage.

## Preparation

```
radosgw-admin user create --uid="testuser" --display-name="First User"
radosgw-admin subuser create --uid=testuser --subuser=testuser:swift --access=full
radosgw-admin key create --subuser=testuser:swift --key-type=swift --gen-secret
```

## Usage

```
python ./main.py
```
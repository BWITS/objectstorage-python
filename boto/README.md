# Boto

## Introductiion

[Boto](https://github.com/boto/boto) is a python package that provides interfaces to Amazon Web Services.

## Preparation

Create the user `testuser` and get the access key and secret key.

```
radosgw-admin user create --uid="testuser" --display-name="First User"
```

The access_key is  "686GRF5C82LWNTKS08P7" and secret_key is "oC2NJMbExPNe+SAqBYerEi3ruRrFh7dexklb4Qk3".

```
pip install -r requirements.txt`
```

## Usage

```
python main.py
```


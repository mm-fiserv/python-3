import boto3
from botocore.exceptions import ClientError


calculations_log = []
def calculate():
    
    while True:
        a = input("Enter first number ('q' to quit): ")
        b = input("Enter second number: ")

        if a.lower() == 'q' or b.lower() == 'q':
            break
        
        num1 = float(a)
        num2 = float(b)
        result = num1 + num2

        calculations_log.append(f"{num1} + {num2} = {result}")
        print(f"{num1} + {num2} = {result}")
    
    upload(calculations_log)

def upload():
    print('*** Uploaded to S3 ***')
    s3_client = boto3.client('s3')
    file = 'calculator-log.txt'
    bucket_name = 'calculator'
    key_path = f'2023/{file}'

    try: 
        response = s3_client.upload_file(file, bucket_name, key_path)
        print(response)

    except ClientError as e:
        print(e)


def ex4():
    calculate()

ex4()

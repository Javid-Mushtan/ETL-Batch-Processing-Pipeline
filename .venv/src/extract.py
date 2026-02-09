from faker import Faker
import random
import string
import csv
import os
import datetime
import sys

try:
    from google.cloud import storage
    GCS_AVAILABLE = True
except ImportError:
    print("Google Cloud Storage library not available")
    GCS_AVAILABLE = False

num_employee = 1000
fake = Faker()
employee_data = []
password_characters = string.ascii_letters + string.digits + 'm'

for _ in range(num_employee):
    raw_address = fake.address()
    clean_address = raw_address.replace('\n', '; ').replace(',', '')

    employee = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'job_title': fake.job(),
        'department': fake.word(),
        'email': fake.email(),
        'address': clean_address,
        'phone_number': fake.phone_number(),
        'salary': fake.random_number(digits=5),
        'password': ''.join(random.choice(password_characters) for _ in range(10))
    }
    employee_data.append(employee)

print(f" Generated {num_employee} employee records")


source_file_name = f'/tmp/employee_data.csv'

with open(source_file_name, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email',
                  'address', 'phone_number', 'salary', 'password']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employee_data)

print(f" Created CSV file: {source_file_name}")
print(f" File size: {os.path.getsize(source_file_name)} bytes")

def upload_to_gcs_without_credentials(bucket_name, source_file_name, destination_blob_name):

    try:
        if not GCS_AVAILABLE:
            print("Cannot upload: GCS library not installed")
            return False
            
        storage_client = storage.Client()
        
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        
        blob.upload_from_filename(source_file_name)
        
        print(f" File {source_file_name} uploaded to gs://{bucket_name}/{destination_blob_name}")
        return True
        
    except Exception as e:
        print(f" Error uploading to GCS: {e}")
        return False

def save_to_composer_bucket(source_file_name):
    try:
        composer_data_dir = '/home/airflow/gcs/data'

        os.makedirs(composer_data_dir, exist_ok=True)
        
        filename = os.path.basename(source_file_name)
        destination = os.path.join(composer_data_dir, filename)
        
        import shutil
        shutil.copy2(source_file_name, destination)
        
        print(f" File copied to Composer bucket: {destination}")
        return True
        
    except Exception as e:
        print(f" Error copying to Composer bucket: {e}")
        return False

def main():
    try:
        bucket_name = 'my-employee'
        
        if GCS_AVAILABLE:
            try:
                storage_client = storage.Client()
                bucket = storage_client.bucket(bucket_name)
                if bucket.exists():
                    destination_blob_name = 'employee_data.csv'
                    
                    upload_to_gcs_without_credentials(bucket_name, source_file_name, destination_blob_name)
                    
                    print(f" Uploaded to gs://{bucket_name}/employee_data.csv")
                else:
                    print(f" Bucket '{bucket_name}' does not exist")
                    save_to_composer_bucket(source_file_name)
            except Exception as e:
                print(f" GCS error: {e}")
                save_to_composer_bucket(source_file_name)
        else:
            save_to_composer_bucket(source_file_name)
        
    except Exception as e:
        print(f"\n ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
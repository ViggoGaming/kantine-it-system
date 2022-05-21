docker-compose --file postgres.yml up
pgcli -h 172.20.0.1 -p 5432 -U postgres -d postgres
uvicorn app:app --reload --reload-exclude "./data"


aws:
https://us-east-1.console.aws.amazon.com/s3/buckets/kantine-it-system?region=eu-north-1&tab=objects
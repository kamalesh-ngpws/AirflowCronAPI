from python:3.9
WORKDIR /usr/src/app
copy . ./
Expose 8000
# copy requirements.txt ./
run pip install -r requirements.txt
cmd uvicorn main:app --reload --host "0.0.0.0"


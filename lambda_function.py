import boto3
import json
import csv
import io
import json

def lambda_handler(event, context):
    # 初始化 S3 客戶端
    s3 = boto3.client('s3')
    
    # 設定存儲桶名稱和檔案名稱
    bucket_name = 'denny-aws-test02'
    file_key = 'BI-test-v0.csv'
    
    # 讀取 CSV 檔案
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    csv_content = response['Body'].read().decode('utf-8')
    
    # 將 CSV 轉換為 JSON 格式
    csv_rows = csv.DictReader(io.StringIO(csv_content))
    json_output = json.dumps([row for row in csv_rows])
    print(json_output)
    
    # json_content2 = [
    #     {"date": "2024/3/4", "career": "102", "store": "10202", "net": "45237"},
    #     {"date": "2024/3/5", "career": "102", "store": "10202", "net": "34786"},
    #     {"date": "2024/4/24", "career": "102", "store": "10202", "net": "33721"}
    # ]
    
    # # 將 JSON 轉換為字串
    # json_output2 = json.dumps(json_content2)



    # 根據 CSV 檔案的內容動態生成提示訊息

    prompt = f'explain the text {json_output}'
    # prompt = f'explain the text {json_output2}'
        
    # 建立 Bedrock 客戶端
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-west-2'
    )  

    
    # 設置 Bedrock 模型的輸入參數
    input_data = {
        "modelId": "cohere.command-text-v14",
        "contentType": "application/json",
        "accept": "*/*",
        "body": {
            "prompt": prompt,
            "max_tokens": 1000,
            "temperature": 0.75,
            "p": 0.01,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE"
        }
    }
    
    # 呼叫 Bedrock 模型
    response = bedrock.invoke_model(
        body=json.dumps(input_data["body"]),
        modelId=input_data["modelId"],
        accept=input_data["accept"],
        contentType=input_data["contentType"]
    )

    # 讀取上面的s3內檔案並解析回應
    response_body = json.loads(response['body'].read())

    print(response_body)

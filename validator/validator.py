from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import requests
import time
import threading

app = FastAPI()

# Định nghĩa cấu trúc dữ liệu cho Result
class ResultModel(BaseModel):
    result_id: str
    description: str
    processing_time: float
    miner_id: str

# Địa chỉ server của miner
MINER_URL = "http://127.0.0.1:8000/receive-task"  # Thay bằng IP thực tế nếu chạy trên máy khác

# Endpoint nhận kết quả từ miner
@app.post("/submit-result")
async def submit_result(result: ResultModel):
    print(f"[Validator] Nhận kết quả: {result.result_id} - {result.description} "
          f"(Thời gian xử lý: {result.processing_time}s, Miner: {result.miner_id})")
    return {"message": f"Kết quả {result.result_id} đã được nhận và xử lý"}

# Hàm gửi task tới miner
def send_task(task_counter):
    task = {
        "task_id": f"task_{task_counter:03d}",
        "description": f"Xử lý dữ liệu batch {task_counter}",
        "deadline": "2024-12-31",
        "priority": (task_counter % 5) + 1
    }
    try:
        print(f"[Validator] Gửi task: {task['task_id']} - {task['description']} (Priority: {task['priority']})")
        response = requests.post(MINER_URL, json=task, timeout=5)
        print(f"[Validator] Miner phản hồi: {response.json()}")
    except Exception as e:
        print(f"[Validator] Lỗi khi gửi task: {e}")

if __name__ == "__main__":
    print("[Validator] Khởi động server tại http://172.20.10.6:2001")
    # Chạy server trong thread riêng
    threading.Thread(target=lambda: uvicorn.run(app, host="172.20.10.6", port=2001)).start()

    # Vòng lặp gửi task liên tục
    task_counter = 0
    while True:
        task_counter += 1
        send_task(task_counter)
        time.sleep(5)  # Gửi task mỗi 5 giây để demo rõ ràng
from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
import requests
import time
import threading

app = FastAPI()

# Định nghĩa cấu trúc dữ liệu cho Task
class TaskModel(BaseModel):
    task_id: str
    description: str
    deadline: str
    priority: int

# Địa chỉ server của validator
VALIDATOR_URL = "http://192.168.1.15:4001/submit-result"  # Thay bằng IP thực tế nếu chạy trên máy khác

# Hàm xử lý task (giả lập với thời gian ngẫu nhiên)
def process_task(task):
    print(f"[Miner] Bắt đầu xử lý task: {task.task_id} - {task.description} (Priority: {task.priority})")
    processing_time = 3 + (task.priority % 3)  # Giả lập thời gian xử lý dựa trên độ ưu tiên
    time.sleep(processing_time)
    result = {
        "result_id": f"result_{task.task_id}",
        "description": f"Kết quả từ task: {task.description}",
        "processing_time": processing_time,
        "miner_id": "miner_001"
    }
    print(f"[Miner] Hoàn thành task: {task.task_id} - Thời gian xử lý: {processing_time}s")
    return result

# Endpoint nhận task từ validator
@app.post("/receive-task")
async def receive_task(task: TaskModel):
    print(f"[Miner] Nhận task mới: {task.task_id} - {task.description} - Deadline: {task.deadline}")
    # Xử lý task trong thread riêng
    threading.Thread(target=handle_task, args=(task,)).start()
    return {"message": f"Task {task.task_id} đã được nhận và đang xử lý"}

# Hàm gửi kết quả về validator
def handle_task(task):
    result = process_task(task)
    try:
        print(f"[Miner] Gửi kết quả về validator: {result}")
        response = requests.post(VALIDATOR_URL, json=result, timeout=5)
        print(f"[Miner] Validator phản hồi: {response.json()}")
    except Exception as e:
        print(f"[Miner] Lỗi khi gửi kết quả: {e}")

if __name__ == "__main__":
    print("[Miner] Khởi động server tại http://172.20.10.6:2001")
    uvicorn.run(app, host="172.20.10.6", port=2001)
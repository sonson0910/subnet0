import requests
import time
import json

class Miner:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_task(self):
        """Lấy task từ validator qua API."""
        url = f"{self.api_url}/get-task"
        response = requests.get(url)
        task_data = response.json()
        if task_data["message"] == "Task retrieved":
            return task_data["task"]
        return None

    def process_task(self, task_data):
        """Xử lý task và tạo kết quả."""
        print(f"Processing task: {task_data}")
        time.sleep(5)  # Giả lập xử lý task
        result_description = f"Processed: {task_data['description']}"
        return {
            "result_id": f"result_{task_data['task_id']}",
            "description": result_description,
            "processing_time": 5.0,
            "miner_id": "miner_001"  # Sửa thành chuỗi (str)
        }

    def send_result(self, result_data):
        """Gửi kết quả về validator qua API."""
        url = f"{self.api_url}/submit-result"
        # Gửi result dưới dạng multipart/form-data
        response = requests.post(url, data={"result": json.dumps(result_data)})
        print(f"Result sent: {response.json()}")

    def run(self):
        """Chạy miner để lấy task và gửi kết quả liên tục."""
        while True:
            task_data = self.get_task()
            if task_data:
                result_data = self.process_task(task_data)
                self.send_result(result_data)
            else:
                print("No task available, waiting...")
            time.sleep(2)

if __name__ == "__main__":
    miner = Miner(api_url="http://localhost:8000")
    miner.run()
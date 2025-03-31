import requests
import time
import json

class Validator:
    def __init__(self, api_url):
        self.api_url = api_url
        self.scores = []  # Lưu trữ điểm số của các task
        self.task_counter = 0  # Đếm số task để tạo task_id

    def send_task(self):
        """Gửi task đến miner qua API."""
        self.task_counter += 1
        task_data = {
            "task_id": f"task_{self.task_counter:03d}",
            "description": f"Process data batch {self.task_counter}",
            "deadline": "2024-12-31",  # Sửa thành chuỗi (str)
            "priority": (self.task_counter % 5) + 1  # Priority từ 1-5
        }
        url = f"{self.api_url}/send-task"
        # Gửi task dưới dạng multipart/form-data
        response = requests.post(url, data={"task": json.dumps(task_data)})
        print(f"Task sent: {response.json()}")
        return response.json()

    def get_result(self):
        """Lấy kết quả từ miner qua API."""
        url = f"{self.api_url}/get-result"
        response = requests.get(url)
        result_data = response.json()
        if result_data["message"] == "Result retrieved":
            return result_data["result"]
        return None

    def receive_result(self, result_data):
        """Nhận kết quả từ miner và chấm điểm."""
        if result_data:
            score = len(result_data['description']) * 10  # Giả lập chấm điểm
            self.scores.append(score)
            print(f"Result received: {result_data}, Score: {score}")
            if self.scores:
                average_score = sum(self.scores) / len(self.scores)
                print(f"Current average score: {average_score}")

    def run(self):
        """Chạy validator để gửi task liên tục và nhận kết quả."""
        while True:
            self.send_task()
            time.sleep(2)
            result_data = self.get_result()
            self.receive_result(result_data)
            time.sleep(2)

if __name__ == "__main__":
    validator = Validator(api_url="http://localhost:8000")
    validator.run()
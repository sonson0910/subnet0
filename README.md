# Subnet0 - Decentralized AI Training Platform on Cardano

Subnet0 là một nền tảng demo cho việc huấn luyện mô hình AI phi tập trung trên blockchain Cardano, được lấy cảm hứng từ Bittensor. Dự án này minh họa cách các node có thể cộng tác để huấn luyện mô hình AI một cách phi tập trung, với cơ chế khuyến khích dựa trên blockchain.

## 🚀 Tính năng

- **Kiến trúc Phi tập trung**: Sử dụng mạng P2P để phân phối và xử lý các task huấn luyện AI
- **Cơ chế Khuyến khích**: Tích hợp với blockchain Cardano để thưởng cho các node đóng góp
- **Quản lý Task Thông minh**: Hệ thống phân phối và theo dõi task hiệu quả
- **Xác thực Kết quả**: Cơ chế xác thực kết quả huấn luyện phi tập trung

## 🏗️ Kiến trúc

Dự án bao gồm các thành phần chính:

### Validator
- Quản lý và phân phối task huấn luyện
- Xác thực kết quả từ các miner
- Tích hợp với blockchain Cardano để quản lý phần thưởng

### Miner
- Nhận và xử lý các task huấn luyện
- Thực hiện việc huấn luyện mô hình AI
- Gửi kết quả về validator để xác thực

### Network Layer
- Giao thức P2P cho việc trao đổi dữ liệu
- API RESTful cho việc giao tiếp giữa các node
- Cơ chế bảo mật và xác thực

## 🛠️ Cài đặt

1. Clone repository:
```bash
git clone https://github.com/yourusername/subnet0.git
cd subnet0
```

2. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```

3. Cấu hình môi trường:
```bash
cp .env.example .env
# Chỉnh sửa các biến môi trường trong file .env
```

## 🚀 Chạy Demo

1. Khởi động Validator:
```bash
python validator/validator.py
```

2. Khởi động Miner:
```bash
python miner/miner.py
```

## 🔗 Tích hợp với Cardano

Dự án sử dụng blockchain Cardano để:
- Quản lý danh tính của các node
- Phân phối phần thưởng cho các node đóng góp
- Lưu trữ và xác thực kết quả huấn luyện

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng! Hãy tạo pull request hoặc mở issue để thảo luận về các thay đổi.

## 📝 License

MIT License - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## 🙏 Cảm ơn

- [Bittensor](https://github.com/opentensor/bittensor) - Nguồn cảm hứng cho dự án
- [Cardano](https://cardano.org/) - Nền tảng blockchain
- Cộng đồng mã nguồn mở

## 📞 Liên hệ

- Website: [your-website]
- Email: [your-email]
- Twitter: [@your-twitter] 
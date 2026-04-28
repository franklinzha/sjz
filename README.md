
# ⚙️ 二、服务器环境要求

## ✔ 必须

- Python 3.10+
- pip 20+
- git
- 8000端口开放

---

# 🚀 三、阿里云部署步骤（完整流程）

---

## 1️⃣ 安装 Python 3.10（如果已安装可跳过）

```bash
python3.10 --version
2️⃣ 克隆项目
git clone https://github.com/franklinzha/sjz.git
cd sjz/backend
3️⃣ 创建虚拟环境（强烈推荐）
python3.10 -m venv venv
source venv/bin/activate
4️⃣ 安装依赖
pip install --upgrade pip
pip install -r requirements.txt
5️⃣ 启动后端服务
uvicorn main:app --host 0.0.0.0 --port 8000
6️⃣ 后台运行（生产模式）
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
🌐 四、访问方式
WebSocket接口：
ws://你的服务器IP:8000/ws
HTTP接口（测试）：
http://你的服务器IP:8000/docs
🖥️ 五、前端启动（本地或服务器）
cd ../frontend
npm install
npm run dev

访问：

http://localhost:5173
🧩 六、Electron桌面端（可选）
cd ../electron
npm install
npm start
🔥 七、常见问题（非常重要）
❌ 1. 端口无法访问

👉 阿里云安全组必须开放：

8000 TCP 0.0.0.0/0
❌ 2. WebSocket 连接失败

检查：

IP是否正确
端口是否开放
uvicorn是否在运行
❌ 3. Python版本问题

必须：

Python >= 3.10
🧠 八、生产级建议（强烈推荐）
✔ 使用 systemd（自动重启）

创建服务：

sudo nano /etc/systemd/system/sjz.service

内容：

[Unit]
Description=sjz backend
After=network.target

[Service]
User=root
WorkingDirectory=/root/sjz/backend
ExecStart=/root/sjz/backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target

启动：

sudo systemctl daemon-reload
sudo systemctl start sjz
sudo systemctl enable sjz
🚀 九、项目特点
实时数据流（WebSocket）
AI分析模块
可扩展雷达系统
支持桌面端 Electron
云服务器部署
可扩展为监控/游戏数据系统
📦 十、未来升级方向
AI预测模块（轨迹预测）
多用户系统
登录鉴权（Token）
可视化热力图
自动部署 CI/CD

import os
import webbrowser

# Nội dung Code HTML/CSS/JS hoàn chỉnh cho trang web
web_content = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chúc Mừng Ngày Phụ Nữ Việt Nam 20/10 🌸</title>
  <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #0d001a 0%, #2a0845 50%, #4a0033 100%);
      font-family: 'Quicksand', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      position: relative;
    }

    /* Hiệu ứng nền tuyết hoa rơi */
    .falling-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 1;
    }

    .flower {
      position: absolute;
      top: -10%;
      user-select: none;
      animation: fall linear infinite;
    }

    @keyframes fall {
      0% {
        top: -10%;
        transform: translateX(0) rotate(0deg) scale(1);
        opacity: 1;
      }
      100% {
        top: 105%;
        transform: translateX(120px) rotate(360deg) scale(0.6);
        opacity: 0.2;
      }
    }

    /* Khung thiệp 3D */
    .card-wrapper {
      perspective: 1000px;
      z-index: 10;
      padding: 20px;
    }

    .card {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      padding: 40px 30px;
      border-radius: 24px;
      text-align: center;
      max-width: 480px;
      box-shadow: 0 20px 50px rgba(255, 105, 180, 0.25),
                  inset 0 0 15px rgba(255, 255, 255, 0.2);
      transform-style: preserve-3d;
      animation: cardAppear 1.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
      transform: translateY(-8px) rotateX(4deg) rotateY(-4deg);
      box-shadow: 0 30px 60px rgba(255, 105, 180, 0.4);
    }

    @keyframes cardAppear {
      from {
        opacity: 0;
        transform: translateY(50px) scale(0.8);
      }
      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    /* Icon trái tim nhấp nháy */
    .heart-icon {
      font-size: 60px;
      display: inline-block;
      margin-bottom: 10px;
      animation: heartBeat 1.3s infinite ease-in-out;
      filter: drop-shadow(0 0 12px rgba(255, 51, 102, 0.8));
    }

    @keyframes heartBeat {
      0%, 100% { transform: scale(1); }
      15% { transform: scale(1.25); }
      30% { transform: scale(1); }
      45% { transform: scale(1.15); }
    }

    /* Tiêu đề & Lời chúc */
    .title {
      font-family: 'Dancing Script', cursive;
      font-size: 42px;
      color: #ff758c;
      text-shadow: 0 0 10px rgba(255, 117, 140, 0.6);
      margin-bottom: 10px;
    }

    .subtitle {
      color: #ffb6c1;
      font-size: 16px;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 25px;
      font-weight: 600;
    }

    .message {
      color: #f3e5f5;
      font-size: 16px;
      line-height: 1.7;
      margin-bottom: 30px;
      background: rgba(0, 0, 0, 0.2);
      padding: 18px;
      border-radius: 12px;
      border-left: 4px solid #ff4081;
    }

    /* Nút bấm hiệu ứng */
    .btn-surprise {
      background: linear-gradient(45deg, #ff416c, #ff4b2b);
      color: white;
      border: none;
      padding: 14px 32px;
      font-size: 16px;
      font-weight: 600;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 8px 25px rgba(255, 65, 108, 0.5);
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }

    .btn-surprise:hover {
      transform: scale(1.08);
      box-shadow: 0 12px 30px rgba(255, 65, 108, 0.8);
    }

    .btn-surprise:active {
      transform: scale(0.98);
    }

    /* Modal hiệu ứng bất ngờ */
    .modal {
      display: none;
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.85);
      z-index: 100;
      justify-content: center;
      align-items: center;
      backdrop-filter: blur(8px);
    }

    .modal-content {
      background: #1a092b;
      border: 2px solid #ff4081;
      padding: 35px;
      border-radius: 20px;
      text-align: center;
      max-width: 400px;
      color: white;
      box-shadow: 0 0 30px #ff4081;
      animation: zoomIn 0.4s ease;
    }

    @keyframes zoomIn {
      from { transform: scale(0.5); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    .close-btn {
      margin-top: 20px;
      background: #ff4081;
      color: white;
      border: none;
      padding: 8px 20px;
      border-radius: 20px;
      cursor: pointer;
    }
  </style>
</head>
<body>

  <div class="falling-container" id="fallingContainer"></div>

  <div class="card-wrapper">
    <div class="card">
      <div class="heart-icon">💖</div>
      <h1 class="title">Chúc Mừng 20/10</h1>
      <p class="subtitle">Ngày Phụ Nữ Việt Nam</p>

      <div class="message">
        Thân gửi đến một nửa thế giới luôn rạng rỡ, tỏa sáng và tràn đầy yêu thương. Chúc bạn mỗi ngày đều ngọt ngào, hạnh phúc và gặt hái được thật nhiều thành công! 💐✨
      </div>

      <button class="btn-surprise" id="btnSurprise">Nhận Quà Bất Ngờ ✨</button>
    </div>
  </div>

  <div class="modal" id="modal">
    <div class="modal-content">
      <h2>🎉 Lời Chúc Đặc Biệt 🎉</h2>
      <p style="margin-top: 15px; line-height: 1.6;">
        Mong rằng bạn luôn giữ vững nụ cười tươi trên môi, luôn rạng rỡ như những đóa hoa xinh đẹp nhất và nhận được thật nhiều tình yêu thương trong ngày hôm nay! ❤️
      </p>
      <button class="close-btn" id="btnClose">Cảm ơn!</button>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
  <script>
    // Tự động tạo hoa/trái tim rơi
    const flowers = ['🌸', '🌷', '💖', '🌹', '✨', '🌺'];
    const container = document.getElementById('fallingContainer');

    function createFallingElement() {
      const el = document.createElement('div');
      el.classList.add('flower');
      el.innerText = flowers[Math.floor(Math.random() * flowers.length)];
      el.style.left = Math.random() * 100 + 'vw';
      el.style.fontSize = (Math.random() * 15 + 18) + 'px';
      el.style.animationDuration = (Math.random() * 3 + 4) + 's';

      container.appendChild(el);

      setTimeout(() => {
        el.remove();
      }, 7000);
    }

    setInterval(createFallingElement, 250);

    // Xử lý sự kiện bấm nút bất ngờ & pháo hoa
    const btn = document.getElementById('btnSurprise');
    const modal = document.getElementById('modal');
    const btnClose = document.getElementById('btnClose');

    btn.addEventListener('click', () => {
      // Bắn pháo hoa rực rỡ
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
      });

      // Mở Popup
      modal.style.display = 'flex';
    });

    btnClose.addEventListener('click', () => {
      modal.style.display = 'none';
    });
  </script>
</body>
</html>
"""

def create_and_open_web():
    filename = "chuc_mung_2010.html"
    
    # Tạo/ghi file HTML
    with open(filename, "w", encoding="utf-8") as f:
        f.write(web_content)
    
    print(f"✅ Đã tạo thành công file web: {filename}")
    
    # Lấy đường dẫn tuyệt đối của file HTML
    filepath = os.path.abspath(filename)
    
    # Mở file trên trình duyệt mặc định
    print("🚀 Đang tự động mở trang web trên trình duyệt...")
    webbrowser.open(f"file://{filepath}")

if __name__ == "__main__":
    create_and_open_web()
import logging
import os
from logging.handlers import RotatingFileHandler  # 或 TimedRotatingFileHandler

def setup_logger(log_dir="logs", log_file="app.log", level=logging.INFO):
    # 创建日志目录
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(level)

    # 防止重复添加 handler
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # 文件输出（自动轮转）
        # 当文件超过 5MB 时，自动新建文件，最多保留 5 个旧文件
        file_handler = RotatingFileHandler(
            log_path, maxBytes=5*1024*1024, backupCount=10, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# ================= 使用示例 =================
if __name__ == "__main__":
    logger = setup_logger()

    logger.info("程序启动成功")
    for i in range(10000):
        logger.debug(f"循环测试日志 {i}")
    logger.warning("注意：磁盘空间不足")
    logger.error("发生错误：无法连接数据库")

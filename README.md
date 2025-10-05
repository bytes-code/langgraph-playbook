# LangGraph Playbook

这是一个基于 LangGraph 的项目模板，用于快速构建和测试 LangGraph 应用。

## 项目结构

```
langgraph-playbook/
├── README.md           # 项目说明文档
├── requirements.txt    # Python 依赖包
├── .gitignore         # Git 忽略文件
├── tests/             # 测试代码目录
└── src/               # 源代码目录（待创建）
```

## 快速开始

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行测试：
```bash
python -m pytest tests/
```

## 开发指南

- 所有源代码放在 `src/` 目录下
- 测试代码放在 `tests/` 目录下
- 遵循简洁、清晰的代码风格
- 测试代码要简洁，只测试核心功能

## 技术栈

- Python 3.8+
- LangGraph
- pytest (测试框架)

## 许可证

MIT License

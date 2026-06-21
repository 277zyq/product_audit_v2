# Product Audit V2

这是一个 Python 商品风险审核小项目。

项目会读取商品 CSV 文件和风险规则 JSON 文件，对商品进行风险判断，并输出新的 CSV 审核结果。

## 功能

- 读取 JSON 风险配置
- 读取 CSV 商品数据
- 将商品记录转换为 Product 对象
- 判断商品风险等级
- 输出 CSV 审核结果
- 使用 pytest 测试核心函数
- 使用 Git 进行版本管理

## 项目结构

```text
product_audit_v2/
  main.py
  data/
    risk_config.json
    products.csv
  output/
    product_risk_result.csv
  models/
    product.py
  services/
    risk_checker.py
  utils/
    file_io.py
  tests/
    test_file_io.py
    test_risk_checker.py
```

## 输入文件

风险配置：

```text
data/risk_config.json
```

示例：

```json
{
  "blacklist_products": ["DRONE", "CHIP"],
  "high_risk_countries": ["IRAN", "RUSSIA"]
}
```

商品数据：

```text
data/products.csv
```

示例：

```csv
name,destination,category,tax
drone,Iran,electronics,5000
book,US,education,100
```

## 安装依赖

建议先创建并激活虚拟环境：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

安装测试依赖：

```powershell
pip install -r requirements.txt
```

## 运行项目

在项目根目录运行：

```powershell
python main.py
```

运行成功后会生成：

```text
output/product_risk_result.csv
```

## 运行测试

```powershell
python -m pytest
```

## 风险规则

- 商品在黑名单，且目的地是高风险国家：`HIGH`
- 商品在黑名单：`HIGH`
- 目的地是高风险国家：`MEDIUM`
- 其他情况：`LOW`

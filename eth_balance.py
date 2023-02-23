import requests

# 以太坊节点的RPC接口地址
rpc_url = 'https://mainnet.infura.io/v3/your_project_id'

# 要查询的钱包地址列表
address_list = ['0x123...', '0x456...', '0x789...']

# 以太坊的RPC请求头
headers = {'Content-Type': 'application/json'}

# 以太坊的RPC请求体，这里使用以太坊的eth_getBalance方法查询余额
# 第一个参数是要查询的地址，第二个参数是要查询的区块号（可以填'latest'表示最新的区块）
payload = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": [],
    "id": 1
}

# 批量查询每个地址的余额
for address in address_list:
    # 设置要查询的地址和区块号
    payload['params'] = [address, 'latest']

    # 发送以太坊的RPC请求
    response = requests.post(rpc_url, headers=headers, json=payload)

    # 解析以太坊节点返回的JSON数据
    result = int(response.json()['result'], 16)

    # 打印查询结果
    print(f"Address: {address}, Balance: {result} wei")

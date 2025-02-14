import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import SimpleCNN
from utils import show_some_images
import sys

# 超参数
batch_size = 32
epochs = 10
learning_rate = 0.001

# 数据预处理和归一化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# 下载并加载数据集
train_data = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_data = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True,  drop_last=True)
test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False , drop_last=True)



# 创建模型
model = SimpleCNN()

# 使用GPU（如果有的话）
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
model = model.to(device)





# 损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)



for inputs, labels in train_loader:
    print(f"Input batch size: {inputs.size(0)}")  # 打印每个批次的大小
    print(f"Label batch size: {labels.size(0)}")  # 打印标签的大小
    
    if inputs.size(0) != labels.size(0):
        continue  # 跳过这个批次
    
    inputs, labels = inputs.to(device), labels.to(device)
    
    # 前向传播
    outputs = model(inputs)
    
    # 计算损失
    loss = criterion(outputs, labels)


sys.exit()
# 训练模型
def train_model():
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            # 清空梯度
            optimizer.zero_grad()
            
            # 前向传播
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            # 反向传播
            loss.backward()
            optimizer.step()
            
            # 统计损失和准确率
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        # 输出训练过程
        print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}, Accuracy: {100 * correct/total:.2f}%")

train_model()

# 评估模型
def evaluate_model():
    model.eval()  # 设置为评估模式
    correct = 0
    total = 0
    
    with torch.no_grad():  # 不计算梯度
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    print(f"Test Accuracy: {100 * correct / total:.2f}%")

evaluate_model()

# 可视化结果
show_some_images(test_loader, model, device)

import torch
import matplotlib.pyplot as plt

# 显示测试集的图片
def show_some_images(test_loader, model, device):
    dataiter = iter(test_loader)
    images, labels = dataiter.next()

    # 预测
    outputs = model(images.to(device))
    _, predicted = torch.max(outputs, 1)

    # 显示图片
    fig = plt.figure(figsize=(12, 8))
    for idx in range(6):
        ax = fig.add_subplot(2, 3, idx + 1)
        ax.imshow(images[idx].permute(1, 2, 0).cpu())
        ax.title.set_text(f'Pred: {predicted[idx].item()}, True: {labels[idx].item()}')

    plt.show()

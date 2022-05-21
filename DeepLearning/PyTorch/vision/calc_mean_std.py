def calculate_mean_and_std(dataloader):
    """
    The best normalization is based on the mean and the standard deviation of the provided dataset.
    Here I select the images of the dataset and calculate their mean and standard deviation,
    which I can then load into my transformations of the dataset.

    Args: 
        dataloader(torch.utils.data.dataloader.DataLoader) - torch object to load the data into the notebook

    Returns:
        mean(list): list of floats with the mean values for the dataset
        std(list): list of floats with the standard deviation for the dataset
    """

    # setup of required variables
    mean = 0
    std = 0
    for data, _ in dataloader:
        batch_samples = data.size(0) 
        data = data.view(batch_samples, data.size(1), -1)
        mean += data.mean(2).sum(0)
        std += data.std(2).sum(0)

    mean = mean / len(dataloader.dataset)
    std  = std/len(dataloader.dataset)

    return mean, std

mean, std = calculate_mean_and_std(normal_loader)

print('Mean Values:', mean)
print('Standard Deviations:', std)

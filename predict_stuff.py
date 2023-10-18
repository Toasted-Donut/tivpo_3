def extrapolate_currency_rate(data):
    array = data.copy()
    for i in range(1, 6):
        target_date = 1
        total_change = data[-1] - data[0]
        average_change = total_change / (len(data) - 1)
        predicted_rate = data[-1] + (target_date - len(data) + 1) * average_change
        array.append(predicted_rate)
    return array

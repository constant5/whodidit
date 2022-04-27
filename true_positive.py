import json


def convert_to_binary(predictions):
    for prediction in predictions:
        for i, value in enumerate(prediction):
            if value > 0.5:
                prediction[i] = 1.0
            else:
                prediction[i] = 0.0
    return predictions

def get_true_positives(targets: list[list[int]] = [], predictions: list[list[int]] = []):
    """Function to get number of true positives

    Generates the number of true positives from the data and the occurance of the first true positive for each episode.

    Args:
        targets: Label data, list of lists per set
        predictions: Predicted values from the model

    Returns:
        list[int]: list of counts of true positives per episode
        list[int]: list of first true positive per episode
    """
    if not targets:
        with open('y_true_list_test.json', 'r') as lab_file:
            targets = json.load(lab_file)
    
    if not predictions:
        with open('y_pred_list_test.json', 'r') as pred_file:
            predictions = json.load(pred_file)

    first_tp = []
    tps = []

    episodes = []

    predictions = convert_to_binary(predictions)

    for i, episode in enumerate(targets):
        episodes.append(zip(targets[i], predictions[i]))

    for episode in episodes:
        first_tp_is_found = False
        episode_tp = 0
        for i, data in enumerate(episode):
            print(data)
            if data[0] == data[1] and data[0] == 1:
                episode_tp += 1
                if not first_tp_is_found:
                    first_tp_is_found = True
                    first_tp.append(i)
        tps.append(episode_tp)

    return tps, first_tp


if __name__ == '__main__':
    print(get_true_positives())
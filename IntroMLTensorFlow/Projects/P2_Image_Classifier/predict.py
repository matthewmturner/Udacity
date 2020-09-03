import json
import argparse
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image
from predict_utilities import predict


def main():

    parser = argparse.ArgumentParser(description="Predict image classification")
    parser.add_argument("image_path", help="an integer for the accumulator")
    parser.add_argument("model_path", help="sum the integers (default: find the max)")
    parser.add_argument("-k", "--top_k", default=5, help="number of results to predict")
    parser.add_argument(
        "-c",
        "--category_names",
        default="label_map.json",
        help="JSON mapping file of class number to name",
    )

    args = parser.parse_args()

    image = Image.open(args.image_path)
    test_image = np.asarray(image)

    loaded_model = tf.keras.models.load_model(
        args.model_path, custom_objects={"KerasLayer": hub.KerasLayer}
    )
    preds, classes = predict(args.image_path, loaded_model, int(args.top_k))

    with open(args.category_names, "r") as f:
        class_names = json.load(f)

    pred_class_names = [class_names[str(class_ + 1)] for class_ in classes]
    pred_percent_and_class_name = dict(zip(pred_class_names, preds))
    print(pred_percent_and_class_name)


if __name__ == "__main__":
    main()

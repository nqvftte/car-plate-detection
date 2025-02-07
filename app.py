import cv2
from inference import InferencePipeline

def custom_sink(prediction, video_frame):
    visualization = prediction["label_visualization"]

    visualization = prediction["label_visualization"]
    cv2.imshow("Inference",visualization.numpy_image)
    cv2.waitKey(1)

pipeline = InferencePipeline.init_with_workflow(
    video_reference = "car.mp4",
    workspace_name = "pill-whtzu",
    workflow_id = "parking-lot-management",
    on_prediction = custom_sink
)

pipeline.start()
pipeline.join()
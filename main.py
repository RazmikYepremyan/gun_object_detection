from ultralytics import YOLO

model = YOLO('best.pt')  
results=model("images/1.jpeg")
results[0].save()
# if you want to get coordinates
boxes = results[0].boxes
xyxy_np = boxes.xyxy.cpu().numpy()
for box in xyxy_np:
    xmin, ymin, xmax, ymax = box[:4]
    print(f"xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}")

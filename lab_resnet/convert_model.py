import onnx
import onnx_tf

model = onnx.load("resnet152v2.onnx")

tf_rep = onnx_tf.backend.prepare(model, logging_level="WARN")
print("inputs=", tf_rep.inputs)
print("outputs=", tf_rep.outputs)
# print("tensor_dict=", tf_rep.tensor_dict) # uncomment to see tensor_dict, large data

tf_rep.export_graph('resnet152v2_frompython.pb')


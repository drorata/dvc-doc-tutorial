import os

data_dir = "data"

source_xml = os.path.join(data_dir, "Posts.xml")
source_tsv = os.path.join(data_dir, "Posts.tsv")
source_tsv_head = os.path.join(data_dir, "Posts_head.tsv")

train_tsv = os.path.join(data_dir, "Posts-train.tsv")
test_tsv = os.path.join(data_dir, "Posts-test.tsv")

train_matrix = os.path.join(data_dir, "matrix-train.p")
test_matrix = os.path.join(data_dir, "matrix-test.p")

model = os.path.join(data_dir, "model.p")

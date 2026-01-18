from flask import Flask, request, jsonify, send_file
from model import run_segmentation
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    df, X_pca, clusters = run_segmentation(path)

    # Plot clusters
    plt.figure(figsize=(6,4))
    plt.scatter(X_pca[:,0], X_pca[:,1], c=clusters, cmap="viridis")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.title("Customer Segments")
    plt.tight_layout()
    plt.savefig("cluster.png")
    plt.close()

    return jsonify({"status": "Segmentation Completed"})

@app.route("/plot")
def plot():
    return send_file("cluster.png", mimetype="image/png")
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use Render assigned PORT
    app.run(host="0.0.0.0", port=port)        # Bind to 0.0.0.0 for external access

